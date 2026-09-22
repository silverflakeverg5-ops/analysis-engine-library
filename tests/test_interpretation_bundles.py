from __future__ import annotations

from pathlib import Path
import unittest

from analysis_engine import (
    BundleValidationError,
    ItemNotFoundError,
    KnowledgeLibrary,
)


ROOT = Path(__file__).resolve().parents[1]


class InterpretationBundleIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.library = KnowledgeLibrary(ROOT / "data")

    def test_bundle_preserves_primary_knowledge_and_source(self) -> None:
        bundle = self.library.interpretation_bundle("DEC-000091")
        self.assertEqual(bundle.knowledge["id"], "DEC-000091")
        self.assertTrue(bundle.knowledge_source.endswith("DEC-000091_decision_latency_signal.yml"))

    def test_modifier_links_include_exact_audit_evidence(self) -> None:
        bundle = self.library.interpretation_bundle("ATT-000001")
        links = {link.item["id"]: link for link in bundle.modifiers.links}
        self.assertIn("MOD-000011", links)
        fatigue = links["MOD-000011"]
        self.assertEqual(fatigue.source_value, "疲労")
        self.assertEqual(fatigue.method, "deterministic_text_containment")
        self.assertIn(fatigue.matched_field, {"name_ja", "definition_ja"})
        self.assertIn("疲労", fatigue.matched_value)

    def test_evidence_links_are_derived_from_source_text(self) -> None:
        bundle = self.library.interpretation_bundle("DEC-000091")
        links = {link.item["id"]: link for link in bundle.evidence.links}
        self.assertIn("EVD-000001", links)
        self.assertIn("EVD-000012", links)
        self.assertEqual(links["EVD-000012"].source_value, "意思決定科学")

    def test_unresolved_materials_are_visible(self) -> None:
        bundle = self.library.interpretation_bundle("DEC-000091")
        self.assertIn("判断領域", bundle.modifiers.unresolved_values)
        self.assertTrue(bundle.evidence.source_values)

    def test_safety_baseline_is_fixed_and_auditable(self) -> None:
        bundle = self.library.interpretation_bundle("DEC-000091")
        ids = tuple(link.item["id"] for link in bundle.safety_constraints)
        self.assertEqual(
            ids,
            (
                "SAF-000001",
                "SAF-000006",
                "SAF-000007",
                "SAF-000008",
                "SAF-000009",
                "SAF-000010",
            ),
        )
        self.assertTrue(
            all(link.method == "runtime_baseline_policy" for link in bundle.safety_constraints)
        )

    def test_response_never_claims_interpretation_or_evidence_strength(self) -> None:
        response = self.library.interpretation_bundle("DEC-000091").to_dict()
        self.assertTrue(response["safety"]["materials_only"])
        self.assertFalse(response["safety"]["inference_performed"])
        self.assertFalse(response["safety"]["scoring_performed"])
        self.assertFalse(response["safety"]["ranking_performed"])
        self.assertFalse(response["safety"]["evidence_strength_assessed"])
        self.assertFalse(response["safety"]["applicability_assessed"])

    def test_invalid_bundle_requests_fail_closed(self) -> None:
        with self.assertRaises(BundleValidationError):
            self.library.interpretation_bundle("bad-id")
        with self.assertRaises(ItemNotFoundError):
            self.library.interpretation_bundle("ZZZ-999999")
        with self.assertRaises(BundleValidationError):
            self.library.interpretation_bundle("MOD-000011")


if __name__ == "__main__":
    unittest.main()
