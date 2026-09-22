from __future__ import annotations

from pathlib import Path
import unittest

from analysis_engine import KnowledgeLibrary, PipelineValidationError


ROOT = Path(__file__).resolve().parents[1]


class ApplicationPipelineIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.library = KnowledgeLibrary(ROOT / "data")

    def test_signal_match_is_paired_with_same_knowledge_bundle(self) -> None:
        result = self.library.application_pipeline(
            ["OBS-000014"],
            target_knowledge_types=["decision_strategy"],
            limit=20,
        )
        candidate = next(
            entry for entry in result.candidates if entry.match.item["id"] == "DEC-000091"
        )
        self.assertEqual(candidate.materials.knowledge["id"], "DEC-000091")
        self.assertEqual(candidate.match.matched_inputs, ("OBS-000014",))
        self.assertTrue(candidate.match.evidence)

    def test_pipeline_preserves_match_pagination(self) -> None:
        direct = self.library.match_signals(["反応時間"], offset=1, limit=2)
        pipeline = self.library.application_pipeline(["反応時間"], offset=1, limit=2)
        self.assertEqual(pipeline.total, direct.total)
        self.assertEqual(pipeline.offset, direct.offset)
        self.assertEqual(
            [entry.match.item["id"] for entry in pipeline.candidates],
            [entry.item["id"] for entry in direct.matches],
        )

    def test_every_candidate_has_fixed_safety_baseline(self) -> None:
        result = self.library.application_pipeline(
            ["Decision Latency"],
            target_knowledge_types=["decision_strategy"],
            limit=5,
        )
        self.assertTrue(result.candidates)
        expected = (
            "SAF-000001",
            "SAF-000006",
            "SAF-000007",
            "SAF-000008",
            "SAF-000009",
            "SAF-000010",
        )
        for candidate in result.candidates:
            self.assertEqual(
                tuple(link.item["id"] for link in candidate.materials.safety_constraints),
                expected,
            )

    def test_unresolved_material_values_remain_visible(self) -> None:
        result = self.library.application_pipeline(
            ["Decision Latency"],
            target_knowledge_types=["decision_strategy"],
            limit=20,
        )
        candidate = next(
            entry for entry in result.candidates if entry.match.item["id"] == "DEC-000091"
        )
        self.assertIn("判断領域", candidate.materials.modifiers.unresolved_values)

    def test_response_contract_has_no_score_rank_or_conclusion_fields(self) -> None:
        response = self.library.application_pipeline(
            ["Decision Latency"],
            target_knowledge_types=["decision_strategy"],
            limit=1,
        ).to_dict()
        self.assertEqual(
            set(response),
            {
                "api_version", "runtime_version", "pipeline", "pagination",
                "candidates", "application_guidance", "safety",
            },
        )
        self.assertIsNone(response["application_guidance"])
        self.assertEqual(
            set(response["candidates"][0]),
            {"match", "interpretation_materials"},
        )
        self.assertFalse(response["safety"]["inference_performed"])
        self.assertFalse(response["safety"]["scoring_performed"])
        self.assertFalse(response["safety"]["ranking_performed"])
        self.assertFalse(response["safety"]["evidence_strength_assessed"])
        self.assertFalse(response["safety"]["applicability_assessed"])

    def test_material_items_are_excluded_from_pipeline_candidates(self) -> None:
        result = self.library.application_pipeline(["疲労"], limit=20)
        self.assertNotIn(
            "modifier",
            {entry.match.item["knowledge_type"] for entry in result.candidates},
        )

    def test_pipeline_limit_is_bounded_for_bundle_payloads(self) -> None:
        for invalid in (0, 21, True):
            with self.subTest(limit=invalid):
                with self.assertRaises(PipelineValidationError):
                    self.library.application_pipeline(["反応時間"], limit=invalid)


if __name__ == "__main__":
    unittest.main()
