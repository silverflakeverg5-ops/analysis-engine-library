from __future__ import annotations

from pathlib import Path
import unittest

from analysis_engine import KnowledgeLibrary, SignalValidationError


ROOT = Path(__file__).resolve().parents[1]


class SignalMatchingIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.library = KnowledgeLibrary(ROOT / "data")

    def test_observation_signal_id_resolves_to_candidate_knowledge(self) -> None:
        result = self.library.match_signals(["OBS-000014"], limit=100)
        ids = {match.item["id"] for match in result.matches}
        self.assertIn("DEC-000091", ids)
        self.assertNotIn("OBS-000014", ids)
        reference = result.inputs[0]
        self.assertEqual(reference.resolved_signal_id, "OBS-000014")
        self.assertIn("Decision Latency", reference.terms)

    def test_match_evidence_is_field_level_and_auditable(self) -> None:
        result = self.library.match_signals(
            ["Decision Latency"],
            target_knowledge_types=["decision_strategy"],
            limit=100,
        )
        match = next(entry for entry in result.matches if entry.item["id"] == "DEC-000091")
        self.assertEqual(match.matched_inputs, ("Decision Latency",))
        self.assertTrue(
            any(
                evidence["field"] == "name_en"
                and evidence["matched_term"] == "Decision Latency"
                for evidence in match.evidence
            )
        )

    def test_all_mode_requires_every_input(self) -> None:
        result = self.library.match_signals(
            ["Decision Latency", "判断潜時"],
            mode="all",
            target_knowledge_types=["decision_strategy"],
            limit=100,
        )
        ids = {match.item["id"] for match in result.matches}
        self.assertIn("DEC-000091", ids)
        self.assertTrue(
            all(len(match.matched_inputs) == 2 for match in result.matches)
        )

    def test_operational_items_are_excluded_by_default(self) -> None:
        default = self.library.match_signals(["Decision Latency"], limit=100)
        included = self.library.match_signals(
            ["Decision Latency"],
            include_operational=True,
            limit=100,
        )
        self.assertNotIn("OBS-000014", {match.item["id"] for match in default.matches})
        self.assertIn("OBS-000014", {match.item["id"] for match in included.matches})

    def test_response_never_reports_score_rank_or_inference(self) -> None:
        response = self.library.match_signals(["選択潜時"], limit=10).to_dict()
        self.assertTrue(response["safety"]["mapping_only"])
        self.assertFalse(response["safety"]["inference_performed"])
        self.assertFalse(response["safety"]["scoring_performed"])
        self.assertFalse(response["safety"]["ranking_performed"])
        self.assertNotIn("score", response)
        self.assertNotIn("confidence", response)
        self.assertNotIn("diagnosis", response)

    def test_pagination_is_deterministic(self) -> None:
        first = self.library.match_signals(["反応時間"], offset=0, limit=10)
        second = self.library.match_signals(["反応時間"], offset=10, limit=10)
        first_ids = [match.item["id"] for match in first.matches]
        second_ids = [match.item["id"] for match in second.matches]
        self.assertEqual(first_ids, sorted(first_ids))
        self.assertEqual(second_ids, sorted(second_ids))
        self.assertFalse(set(first_ids) & set(second_ids))
        self.assertEqual(first.total, second.total)

    def test_signal_input_validation(self) -> None:
        invalid_inputs = (
            [],
            [""],
            ["a"],
            ["EMO-000001"],
            ["OBS-999999"],
        )
        for signals in invalid_inputs:
            with self.subTest(signals=signals):
                with self.assertRaises(SignalValidationError):
                    self.library.match_signals(signals)
        with self.assertRaises(SignalValidationError):
            self.library.match_signals(["反応時間"], mode="weighted")
        with self.assertRaises(SignalValidationError):
            self.library.match_signals(["反応時間"], limit=101)


if __name__ == "__main__":
    unittest.main()
