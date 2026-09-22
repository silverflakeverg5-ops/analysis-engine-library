from __future__ import annotations

import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from analysis_engine import KnowledgeLibrary
from analysis_engine.contracts import build_runtime_contract_snapshot


ROOT = Path(__file__).resolve().parents[1]


class RuntimeContractIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.library = KnowledgeLibrary(ROOT / "data")
        cls.report = cls.library.runtime_contract_report()

    def test_reviewed_v1_snapshot_matches_all_endpoints(self) -> None:
        self.assertTrue(self.report.passed)
        self.assertTrue(self.report.api_version_compatible)
        self.assertEqual(self.report.failed, 0)
        self.assertEqual(len(self.report.checks), 10)
        self.assertTrue(all(check.passed for check in self.report.checks))

    def test_expected_public_responses_are_versioned(self) -> None:
        self.assertEqual(
            tuple(check.endpoint for check in self.report.checks),
            (
                "application_guidance",
                "application_pipeline",
                "divination_registry",
                "interpretation_bundle",
                "japanese_name_calculation",
                "metadata",
                "numerology_calculation",
                "safety_contract",
                "search",
                "signal_matching",
            ),
        )

    def test_contract_response_is_non_inferential(self) -> None:
        response = self.report.to_dict()
        self.assertTrue(response["contract"]["passed"])
        self.assertTrue(response["safety"]["audit_only"])
        self.assertFalse(response["safety"]["inference_performed"])
        self.assertFalse(response["safety"]["scoring_performed"])
        self.assertFalse(response["safety"]["ranking_performed"])

    def test_current_snapshot_generation_is_deterministic(self) -> None:
        first = build_runtime_contract_snapshot(self.library)
        second = build_runtime_contract_snapshot(self.library)
        self.assertEqual(first, second)
        self.assertEqual(first["api_version"], "1.0")

    def test_modified_fingerprint_is_detected(self) -> None:
        snapshot = build_runtime_contract_snapshot(self.library)
        snapshot["schema_fingerprints"]["search"] = "sha256:invalid"
        with TemporaryDirectory() as directory:
            path = Path(directory) / "modified_contract.json"
            path.write_text(
                json.dumps(snapshot, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            report = self.library.runtime_contract_report(path)
        self.assertFalse(report.passed)
        failed = {check.endpoint for check in report.checks if not check.passed}
        self.assertEqual(failed, {"search"})

    def test_missing_endpoint_is_detected(self) -> None:
        snapshot = build_runtime_contract_snapshot(self.library)
        del snapshot["schema_fingerprints"]["metadata"]
        with TemporaryDirectory() as directory:
            path = Path(directory) / "missing_endpoint.json"
            path.write_text(json.dumps(snapshot), encoding="utf-8")
            report = self.library.runtime_contract_report(path)
        self.assertFalse(report.passed)
        metadata = next(
            check for check in report.checks if check.endpoint == "metadata"
        )
        self.assertIsNone(metadata.expected_fingerprint)


if __name__ == "__main__":
    unittest.main()
