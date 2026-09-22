from __future__ import annotations

from pathlib import Path
import unittest

from analysis_engine import KnowledgeLibrary


ROOT = Path(__file__).resolve().parents[1]


class SafetyContractIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.library = KnowledgeLibrary(ROOT / "data")
        cls.report = cls.library.safety_contract_report()

    def test_all_public_runtime_boundaries_pass(self) -> None:
        self.assertTrue(self.report.passed)
        self.assertEqual(self.report.failed, 0)
        self.assertEqual(len(self.report.checks), 9)
        self.assertTrue(all(check.passed for check in self.report.checks))

    def test_expected_contracts_are_covered(self) -> None:
        self.assertEqual(
            tuple(check.name for check in self.report.checks),
            (
                "metadata_boundary",
                "search_boundary",
                "signal_matching_boundary",
                "interpretation_bundle_boundary",
                "application_guidance_boundary",
                "application_pipeline_boundary",
                "divination_registry_boundary",
                "numerology_calculation_boundary",
                "japanese_name_calculation_boundary",
            ),
        )

    def test_audit_response_is_itself_non_inferential(self) -> None:
        response = self.report.to_dict()
        self.assertTrue(response["audit"]["passed"])
        self.assertEqual(response["audit"]["failed_checks"], 0)
        self.assertTrue(response["safety"]["audit_only"])
        self.assertFalse(response["safety"]["inference_performed"])
        self.assertFalse(response["safety"]["scoring_performed"])
        self.assertFalse(response["safety"]["ranking_performed"])
        self.assertFalse(response["safety"]["display_suitability_assessed"])

    def test_report_is_deterministic(self) -> None:
        repeated = self.library.safety_contract_report().to_dict()
        self.assertEqual(repeated, self.report.to_dict())


if __name__ == "__main__":
    unittest.main()
