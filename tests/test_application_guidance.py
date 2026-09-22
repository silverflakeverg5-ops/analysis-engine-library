from __future__ import annotations

from pathlib import Path
import unittest

from analysis_engine import (
    GuidanceValidationError,
    ItemNotFoundError,
    KnowledgeLibrary,
)


ROOT = Path(__file__).resolve().parents[1]


class ApplicationGuidanceIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.library = KnowledgeLibrary(ROOT / "data")

    def test_guidance_preserves_app_definition_and_source(self) -> None:
        guidance = self.library.application_guidance("APP-000001")
        self.assertEqual(guidance.application["id"], "APP-000001")
        self.assertTrue(guidance.application_source.endswith("APP-000001_personality_diagnosis_app.yml"))

    def test_display_baseline_is_fixed_and_auditable(self) -> None:
        guidance = self.library.application_guidance("APP-000001")
        ids = tuple(link.item["id"] for link in guidance.display_baseline)
        self.assertEqual(
            ids,
            (
                "DSP-000001", "DSP-000002", "DSP-000003", "DSP-000006",
                "DSP-000013", "DSP-000021", "DSP-000022", "DSP-000023",
                "DSP-000024", "DSP-000025", "DSP-000027", "DSP-000030",
            ),
        )
        self.assertTrue(
            all(link.method == "runtime_baseline_policy" for link in guidance.display_baseline)
        )

    def test_mapping_rules_are_contract_references_not_inferred_links(self) -> None:
        guidance = self.library.application_guidance("APP-000051")
        self.assertEqual(
            tuple(link.item["id"] for link in guidance.mapping_rules),
            ("MAP-000024", "MAP-000025"),
        )
        self.assertTrue(
            all(link.method == "runtime_contract_reference" for link in guidance.mapping_rules)
        )

    def test_response_discloses_baseline_only_status(self) -> None:
        response = self.library.application_guidance("APP-000001").to_dict()
        status = response["guidance"]["mapping_status"]
        self.assertTrue(status["baseline_only"])
        self.assertFalse(status["app_specific_mapping_resolved"])
        self.assertFalse(response["safety"]["inference_performed"])
        self.assertFalse(response["safety"]["scoring_performed"])
        self.assertFalse(response["safety"]["ranking_performed"])
        self.assertFalse(response["safety"]["display_suitability_assessed"])

    def test_application_materials_preserve_unresolved_values(self) -> None:
        guidance = self.library.application_guidance("APP-000001")
        self.assertEqual(
            guidance.application_modifiers.source_values,
            ("用途", "対象ユーザー", "安全性", "表示形式"),
        )
        self.assertTrue(guidance.application_modifiers.unresolved_values)

    def test_invalid_app_requests_fail_closed(self) -> None:
        with self.assertRaises(GuidanceValidationError):
            self.library.application_guidance("bad-id")
        with self.assertRaises(ItemNotFoundError):
            self.library.application_guidance("APP-999999")
        with self.assertRaises(GuidanceValidationError):
            self.library.application_guidance("DEC-000091")

    def test_pipeline_can_attach_application_guidance_once(self) -> None:
        result = self.library.application_pipeline(
            ["OBS-000014"],
            target_knowledge_types=["decision_strategy"],
            application_id="APP-000001",
            limit=1,
        )
        self.assertIsNotNone(result.application_guidance)
        self.assertEqual(result.application_guidance.application["id"], "APP-000001")
        response = result.to_dict()
        self.assertEqual(
            response["application_guidance"]["application"]["id"],
            "APP-000001",
        )


if __name__ == "__main__":
    unittest.main()
