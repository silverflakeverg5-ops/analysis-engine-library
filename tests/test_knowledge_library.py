from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from analysis_engine import (
    DuplicateItemIdError,
    ItemNotFoundError,
    KnowledgeLibrary,
    QueryValidationError,
)


ROOT = Path(__file__).resolve().parents[1]


class KnowledgeLibraryIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.library = KnowledgeLibrary(ROOT / "data")

    def test_loads_complete_audited_catalog(self) -> None:
        self.assertEqual(len(self.library), 4434)
        metadata = self.library.metadata()
        self.assertTrue(metadata["read_only"])
        self.assertFalse(metadata["inference_performed"])
        self.assertFalse(metadata["scoring_performed"])

    def test_get_returns_independent_public_copy(self) -> None:
        item = self.library.require("ATT-000001")
        self.assertEqual(item["name_en"], "Sustained Attention")
        self.assertIsInstance(item["tags"], list)
        item["name_en"] = "changed by caller"
        self.assertEqual(
            self.library.require("ATT-000001")["name_en"],
            "Sustained Attention",
        )

    def test_missing_item_contract(self) -> None:
        self.assertIsNone(self.library.get("ZZZ-999999"))
        with self.assertRaises(ItemNotFoundError):
            self.library.require("ZZZ-999999")

    def test_category_and_type_filter(self) -> None:
        result = self.library.search(
            category="Decision Strategy",
            knowledge_type="decision_strategy",
            limit=7,
        )
        self.assertEqual(result.total, 100)
        self.assertEqual(result.returned, 7)
        self.assertTrue(result.has_more)
        self.assertTrue(all(item["id"].startswith("DEC-") for item in result.items))

    def test_tag_filter_and_japanese_keyword(self) -> None:
        result = self.library.search(
            "文化",
            tags=["CAT:文化・文脈"],
            limit=100,
        )
        self.assertEqual(result.total, 100)
        self.assertTrue(all(item["id"].startswith("CUL-") for item in result.items))

    def test_divination_reference_is_searchable_and_evidence_labeled(self) -> None:
        result = self.library.search(
            "四柱推命",
            knowledge_type="divination_reference",
            limit=20,
        )
        self.assertGreater(result.total, 0)
        self.assertTrue(all(item["id"].startswith("DIV-") for item in result.items))
        self.assertTrue(
            all(
                item["evidence_class"] == "traditional_cultural_interpretation"
                for item in result.items
            )
        )
        self.assertTrue(
            all("断定するものではありません" in item["safe_expression"] for item in result.items)
        )

    def test_detailed_divination_catalogs_are_separate(self) -> None:
        catalogs = {
            "western_astrology": "AST-",
            "yin_yang_wuxing": "WUX-",
            "four_pillars": "BAZ-",
            "indian_astrology": "JYO-",
            "zi_wei_dou_shu": "ZWD-",
            "nine_star_ki": "NSK-",
            "sukuyo": "SUK-",
            "numerology": "NUM-",
            "name_divination": "NAM-",
            "feng_shui": "FSH-",
        }
        for knowledge_type, prefix in catalogs.items():
            with self.subTest(knowledge_type=knowledge_type):
                result = self.library.search(knowledge_type=knowledge_type, limit=100)
                self.assertEqual(result.total, 100)
                self.assertTrue(all(item["id"].startswith(prefix) for item in result.items))
                self.assertTrue(
                    all(
                        item["evidence_class"]
                        == "traditional_cultural_interpretation"
                        for item in result.items
                    )
                )

    def test_pagination_is_stable(self) -> None:
        first = self.library.search(knowledge_type="emotion_core", offset=0, limit=10)
        second = self.library.search(knowledge_type="emotion_core", offset=10, limit=10)
        first_ids = {item["id"] for item in first.items}
        second_ids = {item["id"] for item in second.items}
        self.assertFalse(first_ids & second_ids)
        self.assertEqual(first.total, 100)
        self.assertEqual(second.total, 100)

    def test_response_explicitly_contains_no_inference(self) -> None:
        response = self.library.search("注意", limit=3).to_dict()
        self.assertFalse(response["safety"]["inference_performed"])
        self.assertFalse(response["safety"]["scoring_performed"])
        self.assertNotIn("score", response)
        self.assertNotIn("diagnosis", response)

    def test_query_validation(self) -> None:
        with self.assertRaises(QueryValidationError):
            self.library.search(limit=0)
        with self.assertRaises(QueryValidationError):
            self.library.search(limit=101)
        with self.assertRaises(QueryValidationError):
            self.library.search(tags="CAT:注意")
        with self.assertRaises(QueryValidationError):
            self.library.search(sort="score")


class KnowledgeLibraryFailureTests(unittest.TestCase):
    def test_duplicate_ids_fail_closed(self) -> None:
        item = """id: TST-999999
knowledge_type: test
name_ja: テスト
name_en: Test
category: Test
attribute: Test
definition_ja: テスト項目。
tags:
  - CAT:Test
parent: []
related: []
observable_data: []
signal_candidates: []
device_level: none
modifiers: []
evidence: test
status: active
"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "one.yml").write_text(item, encoding="utf-8")
            (root / "two.yml").write_text(item, encoding="utf-8")
            with self.assertRaises(DuplicateItemIdError):
                KnowledgeLibrary(root)


if __name__ == "__main__":
    unittest.main()
