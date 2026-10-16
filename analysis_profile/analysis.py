"""Analysis step: answers and behavior aggregates -> transient tendencies."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping
import json


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RULES_PATH = ROOT / "rules" / "notification_profile_rules_v1.json"
NEUTRAL = 0.5


class AnalysisInputError(ValueError):
    """Raised when answers or behavior aggregates violate the rules contract."""


@lru_cache(maxsize=4)
def _load_rules_cached(path: str) -> Mapping[str, Any]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_rules(data)
    return MappingProxyType(data)


def load_rules(path: Path | None = None) -> Mapping[str, Any]:
    """Load and validate a versioned rules file (read-only view)."""
    return _load_rules_cached(str(path or DEFAULT_RULES_PATH))


def _validate_rules(rules: Mapping[str, Any]) -> None:
    question_ids = {item["id"] for item in rules["questionnaire"]["items"]}
    signal_ids = {signal["id"] for signal in rules["behavior_signals"]}
    sources = question_ids | signal_ids
    tendency_ids = set()
    for tendency in rules["tendencies"]:
        tendency_ids.add(tendency["id"])
        for entry in tendency["inputs"]:
            if entry["source"] not in sources:
                raise ValueError(f"unknown tendency input: {entry['source']}")
            if entry["weight"] <= 0:
                raise ValueError(f"weight must be positive: {tendency['id']}")
    axis_ids = set()
    for axis in rules["axes"]:
        axis_ids.add(axis["id"])
        for entry in axis["combine"]:
            if entry["tendency"] not in tendency_ids:
                raise ValueError(f"unknown axis tendency: {entry['tendency']}")
    for preset in rules["presets"]:
        if set(preset["axes"]) != axis_ids:
            raise ValueError(f"preset axes mismatch: {preset['id']}")
    if set(rules["default_axes"]) != axis_ids:
        raise ValueError("default_axes mismatch")
    for rule in rules["streak_rules"]:
        if rule["axis"] not in axis_ids or rule["mode"] not in {"auto", "propose"}:
            raise ValueError(f"invalid streak rule: {rule['id']}")


class TendencySnapshot:
    """Transient tendency values that refuse every persistence path.

    The snapshot has no dict view, cannot be pickled or JSON-encoded, and hides
    its values from ``repr``. Call ``discard()`` once the parameters exist.
    """

    __slots__ = ("_values", "_rules_version")

    def __init__(self, values: dict[str, float], rules_version: str) -> None:
        self._values: dict[str, float] | None = values
        self._rules_version = rules_version

    @property
    def rules_version(self) -> str:
        return self._rules_version

    @property
    def discarded(self) -> bool:
        return self._values is None

    def value(self, tendency_id: str) -> float:
        if self._values is None:
            raise RuntimeError("tendency snapshot was already discarded")
        return self._values[tendency_id]

    def discard(self) -> None:
        if self._values is not None:
            self._values.clear()
        self._values = None

    def __repr__(self) -> str:
        state = "discarded" if self._values is None else "redacted"
        return f"<TendencySnapshot {state}>"

    __str__ = __repr__

    def __reduce__(self):
        raise TypeError("TendencySnapshot cannot be pickled or persisted")

    def __getstate__(self):
        raise TypeError("TendencySnapshot cannot be pickled or persisted")


def _normalized_answers(
    answers: Mapping[str, int] | None, rules: Mapping[str, Any]
) -> dict[str, float]:
    if not answers:
        return {}
    likert = rules["questionnaire"]["likert"]
    low, high = likert["min"], likert["max"]
    known = {item["id"] for item in rules["questionnaire"]["items"]}
    normalized: dict[str, float] = {}
    for key, value in answers.items():
        if key not in known:
            raise AnalysisInputError(f"unknown question: {key}")
        if isinstance(value, bool) or not isinstance(value, int) or not low <= value <= high:
            raise AnalysisInputError(f"answer must be an integer from {low} to {high}: {key}")
        normalized[key] = (value - low) / (high - low)
    return normalized


def _normalized_behavior(
    behavior: Mapping[str, Mapping[str, float]] | None, rules: Mapping[str, Any]
) -> dict[str, float]:
    if not behavior:
        return {}
    signals = {signal["id"]: signal for signal in rules["behavior_signals"]}
    normalized: dict[str, float] = {}
    for key, aggregate in behavior.items():
        if key not in signals:
            raise AnalysisInputError(f"unknown behavior signal: {key}")
        rate = aggregate.get("rate")
        samples = aggregate.get("samples")
        if isinstance(samples, bool) or not isinstance(samples, int) or samples < 0:
            raise AnalysisInputError(f"samples must be a non-negative integer: {key}")
        if isinstance(rate, bool) or not isinstance(rate, (int, float)) or not 0 <= rate <= 1:
            raise AnalysisInputError(f"rate must be between 0 and 1: {key}")
        if samples >= signals[key]["min_samples"]:
            normalized[key] = float(rate)
    return normalized


def analyze(
    answers: Mapping[str, int] | None = None,
    behavior: Mapping[str, Mapping[str, float]] | None = None,
    rules: Mapping[str, Any] | None = None,
) -> TendencySnapshot:
    """Return transient tendencies in [0, 1] from answers and aggregates.

    ``answers`` maps question IDs to Likert values. ``behavior`` maps signal IDs
    to ``{"rate": float, "samples": int}`` aggregates; signals below their
    ``min_samples`` are ignored. Missing inputs fall back to neutral.
    """
    rules = rules or load_rules()
    sources = {**_normalized_answers(answers, rules), **_normalized_behavior(behavior, rules)}
    values: dict[str, float] = {}
    for tendency in rules["tendencies"]:
        total = 0.0
        weight_sum = 0.0
        for entry in tendency["inputs"]:
            if entry["source"] not in sources:
                continue
            value = sources[entry["source"]]
            if entry.get("reverse"):
                value = 1.0 - value
            total += entry["weight"] * value
            weight_sum += entry["weight"]
        values[tendency["id"]] = total / weight_sum if weight_sum else NEUTRAL
    sources.clear()
    return TendencySnapshot(values, rules["rules_version"])
