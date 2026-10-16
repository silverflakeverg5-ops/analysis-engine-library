from __future__ import annotations

from pathlib import Path
import unittest

from analysis_engine import KnowledgeLibrary


ROOT = Path(__file__).resolve().parents[1]


class DivinationRegistryIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.library = KnowledgeLibrary(ROOT / "data")
        cls.registry = cls.library.divination_registry()

    def test_lists_every_detailed_tradition_in_stable_order(self) -> None:
        self.assertEqual(
            tuple(entry.knowledge_type for entry in self.registry.traditions),
            (
                "western_astrology",
                "yin_yang_wuxing",
                "four_pillars",
                "indian_astrology",
                "zi_wei_dou_shu",
                "nine_star_ki",
                "sukuyo",
                "numerology",
                "name_divination",
                "feng_shui",
                "calendar_notes",
            ),
        )
        self.assertEqual(self.registry.total_items, 1100)

    def test_exposes_application_input_contract(self) -> None:
        feng_shui = next(
            entry
            for entry in self.registry.traditions
            if entry.knowledge_type == "feng_shui"
        )
        self.assertEqual(feng_shui.prefix, "FSH")
        self.assertEqual(feng_shui.item_count, 100)
        self.assertIn("方位測定", feng_shui.required_inputs)
        self.assertEqual(
            feng_shui.evidence_class,
            "traditional_cultural_interpretation",
        )

    def test_calendar_notes_need_only_a_date(self) -> None:
        calendar_notes = next(
            entry
            for entry in self.registry.traditions
            if entry.knowledge_type == "calendar_notes"
        )
        self.assertEqual(calendar_notes.prefix, "KOY")
        self.assertEqual(calendar_notes.item_count, 100)
        self.assertIn("対象日", calendar_notes.required_inputs)
        self.assertNotIn("生年月日", calendar_notes.required_inputs)
        rokuyo = self.library.search(
            knowledge_type="calendar_notes",
            category="Calendar Notes",
            tags=["CAT:六曜"],
            limit=100,
        )
        self.assertEqual(
            {item["name_ja"] for item in rokuyo.items},
            {"先勝", "友引", "先負", "仏滅", "大安", "赤口"},
        )

    def test_response_prohibits_inference_diagnosis_and_prediction(self) -> None:
        response = self.registry.to_dict()
        self.assertEqual(response["registry"]["tradition_count"], 11)
        self.assertTrue(response["safety"]["reference_only"])
        self.assertTrue(response["safety"]["cultural_interpretation_only"])
        self.assertFalse(response["safety"]["inference_performed"])
        self.assertFalse(response["safety"]["diagnosis_performed"])
        self.assertFalse(response["safety"]["prediction_performed"])


if __name__ == "__main__":
    unittest.main()
