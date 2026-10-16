"""Secretary step: transient tendencies -> notification parameters.

Also holds the reference logic for preset recommendation and streak-based
adjustment, so the app's secretary module can be checked against it.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import date
from typing import Any, Mapping

from .analysis import AnalysisInputError, TendencySnapshot, analyze, load_rules


FORTUNE_STANCES = ("believer", "enjoy", "joke")


@dataclass(frozen=True)
class NotificationParameters:
    """The only analysis-derived values the app may store or pass on."""

    axes: Mapping[str, int]
    fortune_stance: str
    rules_version: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "axes": dict(self.axes),
            "fortuneStance": self.fortune_stance,
            "rulesVersion": self.rules_version,
        }


def _round_half_up(value: float) -> int:
    return int(value + 0.5)


def to_parameters(
    snapshot: TendencySnapshot,
    fortune_stance: str = "enjoy",
    rules: Mapping[str, Any] | None = None,
) -> NotificationParameters:
    """Convert tendencies to axis values; the snapshot is not retained."""
    rules = rules or load_rules()
    if fortune_stance not in FORTUNE_STANCES:
        raise AnalysisInputError(f"unknown fortune stance: {fortune_stance}")
    low, high = rules["axis_scale"]["min"], rules["axis_scale"]["max"]
    axes: dict[str, int] = {}
    for axis in rules["axes"]:
        total = 0.0
        weight_sum = 0.0
        for entry in axis["combine"]:
            value = snapshot.value(entry["tendency"])
            if entry.get("reverse"):
                value = 1.0 - value
            total += entry["weight"] * value
            weight_sum += entry["weight"]
        mean = total / weight_sum
        axes[axis["id"]] = min(high, max(low, low + _round_half_up(mean * (high - low))))
    return NotificationParameters(axes, fortune_stance, rules["rules_version"])


def derive_parameters(
    answers: Mapping[str, int] | None = None,
    behavior: Mapping[str, Mapping[str, float]] | None = None,
    fortune_stance: str = "enjoy",
    rules: Mapping[str, Any] | None = None,
) -> NotificationParameters:
    """Analyze, convert, and discard the tendencies in one step."""
    rules = rules or load_rules()
    snapshot = analyze(answers, behavior, rules)
    try:
        return to_parameters(snapshot, fortune_stance, rules)
    finally:
        snapshot.discard()


def recommend_presets(
    axes: Mapping[str, int],
    rules: Mapping[str, Any] | None = None,
    count: int = 3,
) -> list[dict[str, Any]]:
    """Return the nearest presets by L1 distance, ties kept in rules order."""
    rules = rules or load_rules()
    ranked = sorted(
        enumerate(rules["presets"]),
        key=lambda pair: (
            sum(abs(pair[1]["axes"][key] - axes[key]) for key in pair[1]["axes"]),
            pair[0],
        ),
    )
    return [
        {
            "presetId": preset["id"],
            "label_ja": preset["label_ja"],
            "axes": dict(preset["axes"]),
            "distance": sum(abs(preset["axes"][key] - axes[key]) for key in preset["axes"]),
        }
        for _, preset in ranked[:count]
    ]


@dataclass(frozen=True)
class StreakState:
    """Secretary-side state for streak adjustment. Holds no tendencies."""

    axes: Mapping[str, int]
    user_baseline: Mapping[str, int]
    counters: Mapping[str, int] = field(default_factory=dict)
    last_auto_change: Mapping[str, str] = field(default_factory=dict)

    @classmethod
    def from_parameters(cls, parameters: NotificationParameters) -> "StreakState":
        return cls(axes=dict(parameters.axes), user_baseline=dict(parameters.axes))

    def with_user_axis(self, axis: str, value: int) -> "StreakState":
        """Record a manual setting; it becomes the new baseline for that axis."""
        return replace(
            self,
            axes={**self.axes, axis: value},
            user_baseline={**self.user_baseline, axis: value},
        )


@dataclass(frozen=True)
class StreakDecision:
    rule_id: str
    mode: str
    axis: str
    from_value: int
    to_value: int
    reason_ja: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "ruleId": self.rule_id,
            "mode": self.mode,
            "axis": self.axis,
            "from": self.from_value,
            "to": self.to_value,
            "reasonJa": self.reason_ja,
        }


def _counter_key(rule: Mapping[str, Any], target_id: str | None) -> str:
    if rule.get("per_target"):
        if not target_id:
            raise AnalysisInputError(f"{rule['event']} requires a target_id")
        return f"{rule['id']}:{target_id}"
    return rule["id"]


def apply_streak_event(
    state: StreakState,
    event: str,
    today: date,
    target_id: str | None = None,
    rules: Mapping[str, Any] | None = None,
) -> tuple[StreakState, list[StreakDecision]]:
    """Count one reaction event and return the new state plus any decisions.

    Callers must not send events from excluded periods (travel, quiet hours).
    Auto rules change the axis by one step within the daily and baseline
    limits; propose rules only return a decision for the user to accept.
    """
    rules = rules or load_rules()
    limits = rules["streak_limits"]
    low, high = rules["axis_scale"]["min"], rules["axis_scale"]["max"]
    counters = dict(state.counters)
    axes = dict(state.axes)
    last_auto = dict(state.last_auto_change)
    decisions: list[StreakDecision] = []
    today_text = today.isoformat()

    for rule in rules["streak_rules"]:
        if event in rule["broken_by"]:
            if rule.get("per_target"):
                if target_id:
                    counters.pop(f"{rule['id']}:{target_id}", None)
            else:
                counters.pop(rule["id"], None)
            continue
        if event != rule["event"]:
            continue
        key = _counter_key(rule, target_id)
        counters[key] = counters.get(key, 0) + 1
        if counters[key] < rule["streak"]:
            continue
        counters.pop(key)
        axis = rule["axis"]
        current = axes[axis]
        proposed = min(high, max(low, current + rule["direction"]))
        if proposed == current:
            continue
        if rule["mode"] == "propose":
            decisions.append(StreakDecision(rule["id"], "propose", axis, current, proposed, rule["reason_ja"]))
            continue
        if limits["auto_allowed_directions"].get(axis) != rule["direction"]:
            continue
        if last_auto.get(axis) == today_text:
            continue
        baseline = state.user_baseline[axis]
        if abs(proposed - baseline) > limits["max_auto_deviation_from_user_baseline"]:
            continue
        axes[axis] = proposed
        last_auto[axis] = today_text
        decisions.append(StreakDecision(rule["id"], "auto", axis, current, proposed, rule["reason_ja"]))

    new_state = replace(state, axes=axes, counters=counters, last_auto_change=last_auto)
    return new_state, decisions


def undo_decision(state: StreakState, decision: StreakDecision) -> StreakState:
    """Restore the value before an automatic change without moving the baseline."""
    if decision.mode != "auto" or state.axes.get(decision.axis) != decision.to_value:
        return state
    return replace(state, axes={**state.axes, decision.axis: decision.from_value})
