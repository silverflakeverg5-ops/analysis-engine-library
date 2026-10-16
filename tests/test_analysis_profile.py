from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path
import json
import pickle
import unittest

from analysis_engine import KnowledgeLibrary
from analysis_profile import (
    AnalysisInputError,
    StreakState,
    analyze,
    apply_streak_event,
    derive_parameters,
    load_rules,
    recommend_presets,
    to_parameters,
    undo_decision,
)


ROOT = Path(__file__).resolve().parents[1]
AXES = {"leadTime", "notificationTolerance", "encouragementStyle", "instructionGranularity", "outgoingness"}
TODAY = date(2026, 10, 16)


class RulesContractTests(unittest.TestCase):
    def test_every_knowledge_ref_resolves(self) -> None:
        library = KnowledgeLibrary(ROOT / "data")
        rules = load_rules()
        for group in ("behavior_signals", "tendencies", "axes"):
            for entry in rules[group]:
                for item_id in entry.get("knowledge_refs", []):
                    with self.subTest(item_id=item_id):
                        self.assertIsNotNone(library.get(item_id))

    def test_rules_define_five_axes_and_ten_questions(self) -> None:
        rules = load_rules()
        self.assertEqual({axis["id"] for axis in rules["axes"]}, AXES)
        self.assertEqual(len(rules["questionnaire"]["items"]), 10)
        self.assertTrue(all(rule["streak"] == 5 for rule in rules["streak_rules"]))

    def test_user_facing_reasons_avoid_clinical_terms(self) -> None:
        rules = load_rules()
        texts = [rule["reason_ja"] for rule in rules["streak_rules"]]
        texts += [preset["label_ja"] for preset in rules["presets"]]
        texts += [item["text_ja"] for item in rules["questionnaire"]["items"]]
        for text in texts:
            for term in rules["forbidden_output_terms"]:
                self.assertNotIn(term, text)


class AnalysisTests(unittest.TestCase):
    def test_no_input_gives_neutral_axes(self) -> None:
        parameters = derive_parameters()
        self.assertEqual(dict(parameters.axes), dict(load_rules()["default_axes"]))
        self.assertEqual(parameters.fortune_stance, "enjoy")

    def test_axes_stay_within_scale_for_extreme_answers(self) -> None:
        for value in (1, 5):
            answers = {f"q{index}": value for index in range(1, 11)}
            parameters = derive_parameters(answers)
            self.assertEqual(set(parameters.axes), AXES)
            self.assertTrue(all(1 <= axis <= 5 for axis in parameters.axes.values()))

    def test_is_deterministic(self) -> None:
        answers = {"q1": 4, "q2": 2, "q3": 5, "q5": 1, "q9": 4}
        self.assertEqual(derive_parameters(answers).to_dict(), derive_parameters(answers).to_dict())

    def test_behavior_below_min_samples_is_ignored(self) -> None:
        few = derive_parameters(behavior={"ignore_rate": {"rate": 1.0, "samples": 3}})
        many = derive_parameters(behavior={"ignore_rate": {"rate": 1.0, "samples": 40}})
        self.assertEqual(few.axes["notificationTolerance"], 3)
        self.assertLess(many.axes["notificationTolerance"], 3)

    def test_rejects_invalid_inputs(self) -> None:
        with self.assertRaises(AnalysisInputError):
            analyze({"q1": 6})
        with self.assertRaises(AnalysisInputError):
            analyze({"q99": 3})
        with self.assertRaises(AnalysisInputError):
            analyze(behavior={"snooze_rate": {"rate": 1.5, "samples": 30}})
        with self.assertRaises(AnalysisInputError):
            derive_parameters(fortune_stance="maybe")


class TendencyIsolationTests(unittest.TestCase):
    def test_snapshot_refuses_persistence_paths(self) -> None:
        snapshot = analyze({"q1": 5})
        self.assertEqual(repr(snapshot), "<TendencySnapshot redacted>")
        with self.assertRaises(TypeError):
            pickle.dumps(snapshot)
        with self.assertRaises(TypeError):
            json.dumps(snapshot)
        self.assertFalse(hasattr(snapshot, "__dict__"))

    def test_discarded_snapshot_cannot_be_read(self) -> None:
        snapshot = analyze({"q1": 5})
        to_parameters(snapshot)
        snapshot.discard()
        self.assertTrue(snapshot.discarded)
        with self.assertRaises(RuntimeError):
            snapshot.value("early_start")

    def test_parameters_carry_no_tendency_names(self) -> None:
        rules = load_rules()
        payload = json.dumps(derive_parameters({"q2": 5, "q4": 5}).to_dict(), ensure_ascii=False)
        for tendency in rules["tendencies"]:
            self.assertNotIn(tendency["id"], payload.replace('"outgoingness"', ""))
        for term in rules["forbidden_output_terms"]:
            self.assertNotIn(term, payload)
        self.assertEqual(set(json.loads(payload)), {"axes", "fortuneStance", "rulesVersion"})


class PresetTests(unittest.TestCase):
    def test_exact_preset_is_recommended_first(self) -> None:
        for preset in load_rules()["presets"]:
            with self.subTest(preset=preset["id"]):
                ranked = recommend_presets(preset["axes"])
                self.assertEqual(ranked[0]["presetId"], preset["id"])
                self.assertEqual(ranked[0]["distance"], 0)
                self.assertEqual(len(ranked), 3)


class StreakTests(unittest.TestCase):
    def setUp(self) -> None:
        self.state = StreakState.from_parameters(derive_parameters())

    def _repeat(self, state, event, times, day=TODAY, target=None):
        decisions = []
        for _ in range(times):
            state, new = apply_streak_event(state, event, day, target)
            decisions.extend(new)
        return state, decisions

    def test_four_ignores_do_nothing_five_lower_tolerance(self) -> None:
        state, decisions = self._repeat(self.state, "notification_ignored", 4)
        self.assertEqual(decisions, [])
        state, decisions = self._repeat(state, "notification_ignored", 1)
        self.assertEqual(len(decisions), 1)
        self.assertEqual(decisions[0].mode, "auto")
        self.assertEqual(state.axes["notificationTolerance"], 2)

    def test_response_breaks_the_streak(self) -> None:
        state, _ = self._repeat(self.state, "notification_ignored", 4)
        state, _ = apply_streak_event(state, "notification_responded", TODAY)
        state, decisions = self._repeat(state, "notification_ignored", 4)
        self.assertEqual(decisions, [])
        self.assertEqual(state.axes["notificationTolerance"], 3)

    def test_only_one_auto_step_per_axis_per_day(self) -> None:
        state, decisions = self._repeat(self.state, "notification_ignored", 10)
        self.assertEqual(len(decisions), 1)
        state, decisions = self._repeat(state, "notification_ignored", 5, day=TODAY + timedelta(days=1))
        self.assertEqual(state.axes["notificationTolerance"], 1)

    def test_auto_change_stays_within_two_steps_of_baseline(self) -> None:
        state = self.state
        for offset in range(5):
            state, _ = self._repeat(state, "todo_overdue", 5, day=TODAY + timedelta(days=offset))
        self.assertEqual(state.axes["leadTime"], 5)
        self.assertLessEqual(state.axes["leadTime"] - state.user_baseline["leadTime"], 2)

    def test_increasing_notifications_is_only_proposed(self) -> None:
        state, decisions = self._repeat(self.state, "notification_quick_start", 5)
        self.assertEqual([decision.mode for decision in decisions], ["propose"])
        self.assertEqual(state.axes["notificationTolerance"], 3)

    def test_snooze_streak_is_counted_per_todo(self) -> None:
        state = self.state
        for target in ("a", "b", "a", "b", "a", "b", "a", "b"):
            state, decisions = apply_streak_event(state, "todo_snoozed", TODAY, target)
            self.assertEqual(decisions, [])
        state, decisions = apply_streak_event(state, "todo_snoozed", TODAY, "a")
        self.assertEqual(decisions[0].axis, "leadTime")
        with self.assertRaises(AnalysisInputError):
            apply_streak_event(state, "todo_snoozed", TODAY)

    def test_undo_restores_previous_value(self) -> None:
        state, decisions = self._repeat(self.state, "notification_ignored", 5)
        restored = undo_decision(state, decisions[0])
        self.assertEqual(restored.axes["notificationTolerance"], 3)
        self.assertEqual(restored.user_baseline, state.user_baseline)

    def test_manual_setting_moves_the_baseline(self) -> None:
        state = self.state.with_user_axis("notificationTolerance", 1)
        state, decisions = self._repeat(state, "notification_ignored", 5)
        self.assertEqual(decisions, [])
        self.assertEqual(state.axes["notificationTolerance"], 1)


if __name__ == "__main__":
    unittest.main()
