from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import json
import subprocess
import sys
import unittest

from analysis_engine import KnowledgeLibrary, JapaneseNameValidationError


ROOT = Path(__file__).resolve().parents[1]


class JapaneseNameCalculationIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.library = KnowledgeLibrary(ROOT / "data")

    def test_kanji_name_five_grids_are_reproducible(self) -> None:
        response = self.library.calculate_japanese_name(
            "山田",
            "太郎",
            surname_strokes=[3, 5],
            given_strokes=[4, 9],
            stroke_dictionary="modern_glyph_declared_v1",
        ).to_dict()
        grids = response["calculation"]["grids"]
        self.assertEqual(
            {name: result["value"] for name, result in grids.items()},
            {"heaven": 8, "person": 9, "earth": 13, "outer": 12, "total": 21},
        )
        self.assertEqual(
            response["calculation"]["yin_yang"]["sequence"],
            ["yang", "yang", "yin", "yang"],
        )
        self.assertEqual(
            response["calculation"]["three_talents"]["sequence"],
            {"heaven": "metal", "person": "water", "earth": "fire"},
        )

    def test_single_character_virtual_strokes_are_disclosed(self) -> None:
        response = self.library.calculate_japanese_name(
            "林",
            "光",
            surname_strokes=[8],
            given_strokes=[6],
            stroke_dictionary="modern_glyph_declared_v1",
        ).to_dict()
        grids = response["calculation"]["grids"]
        self.assertEqual(grids["heaven"]["value"], 9)
        self.assertEqual(grids["earth"]["value"], 7)
        self.assertEqual(grids["outer"]["value"], 2)
        self.assertEqual(grids["outer"]["virtual_strokes"], 2)

    def test_kana_and_katakana_are_supported_with_declared_strokes(self) -> None:
        response = self.library.calculate_japanese_name(
            "やまだ",
            "ハナ",
            surname_strokes=[3, 4, 4],
            given_strokes=[2, 2],
            stroke_dictionary="kana_handwriting_declared_v1",
        ).to_dict()
        self.assertEqual(response["calculation"]["input_summary"]["surname_character_count"], 3)
        self.assertEqual(response["calculation"]["input_summary"]["given_character_count"], 2)

    def test_raw_names_are_not_returned_or_stored(self) -> None:
        response = self.library.calculate_japanese_name(
            "山田",
            "太郎",
            surname_strokes=[3, 5],
            given_strokes=[4, 9],
            stroke_dictionary="modern_glyph_declared_v1",
        ).to_dict()
        self.assertNotIn("山田", str(response))
        self.assertNotIn("太郎", str(response))
        self.assertFalse(response["calculation"]["input_summary"]["raw_names_returned"])
        self.assertFalse(response["calculation"]["input_summary"]["names_stored"])

    def test_versioned_dictionary_resolves_exact_characters(self) -> None:
        response = self.library.calculate_japanese_name_from_dictionary(
            "山田",
            "太郎",
            stroke_dictionary={"山": 3, "田": 5, "太": 4, "郎": 9},
            stroke_dictionary_id="modern_glyph_test_v1",
        ).to_dict()
        self.assertEqual(response["calculation"]["stroke_resolution"], "dictionary_lookup")
        self.assertEqual(response["calculation"]["stroke_trace"]["surname"], [3, 5])
        self.assertEqual(response["calculation"]["stroke_trace"]["given"], [4, 9])
        self.assertEqual(response["calculation"]["grids"]["total"]["value"], 21)

    def test_dictionary_lookup_never_guesses_missing_or_variant_characters(self) -> None:
        invalid_calls = (
            lambda: self.library.calculate_japanese_name_from_dictionary(
                "山田",
                "太郎",
                stroke_dictionary={"山": 3, "田": 5, "太": 4},
                stroke_dictionary_id="incomplete_v1",
            ),
            lambda: self.library.calculate_japanese_name_from_dictionary(
                "髙田",
                "太郎",
                stroke_dictionary={"高": 10, "田": 5, "太": 4, "郎": 9},
                stroke_dictionary_id="variant_missing_v1",
            ),
            lambda: self.library.calculate_japanese_name_from_dictionary(
                "山田",
                "太郎",
                stroke_dictionary={"山": 3, "田": 5, "太": 4, "郎": True},
                stroke_dictionary_id="invalid_value_v1",
            ),
        )
        for call in invalid_calls:
            with self.subTest(call=call):
                with self.assertRaises(JapaneseNameValidationError):
                    call()

    def test_cli_loads_versioned_json_dictionary(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "strokes.json"
            path.write_text(
                json.dumps({"山": 3, "田": 5, "太": 4, "郎": 9}, ensure_ascii=False),
                encoding="utf-8",
            )
            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "analysis_engine",
                    "--japanese-surname",
                    "山田",
                    "--japanese-given-name",
                    "太郎",
                    "--stroke-dictionary",
                    "modern_glyph_test_v1",
                    "--stroke-dictionary-file",
                    str(path),
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        response = json.loads(completed.stdout)
        self.assertEqual(response["calculation"]["stroke_resolution"], "dictionary_lookup")
        self.assertEqual(response["calculation"]["grids"]["total"]["value"], 21)

    def test_grid_references_resolve_to_name_catalog(self) -> None:
        response = self.library.calculate_japanese_name(
            "山田",
            "太郎",
            surname_strokes=[3, 5],
            given_strokes=[4, 9],
            stroke_dictionary="modern_glyph_declared_v1",
        ).to_dict()
        for grid in response["calculation"]["grids"].values():
            item = self.library.require(grid["knowledge_id"])
            self.assertEqual(item["knowledge_type"], "name_divination")

    def test_ambiguous_or_mismatched_inputs_fail_closed(self) -> None:
        invalid_calls = (
            lambda: self.library.calculate_japanese_name(
                "Yamada", "太郎", surname_strokes=[3, 5], given_strokes=[4, 9], stroke_dictionary="x"
            ),
            lambda: self.library.calculate_japanese_name(
                "山田", "太郎", surname_strokes=[3], given_strokes=[4, 9], stroke_dictionary="x"
            ),
            lambda: self.library.calculate_japanese_name(
                "山田", "太郎", surname_strokes=[3, 5], given_strokes=[4, 0], stroke_dictionary="x"
            ),
            lambda: self.library.calculate_japanese_name(
                "山田", "太郎", surname_strokes=[3, 5], given_strokes=[4, 9], stroke_dictionary=""
            ),
        )
        for call in invalid_calls:
            with self.subTest(call=call):
                with self.assertRaises(JapaneseNameValidationError):
                    call()

    def test_response_is_calculation_only(self) -> None:
        response = self.library.calculate_japanese_name(
            "山田",
            "太郎",
            surname_strokes=[3, 5],
            given_strokes=[4, 9],
            stroke_dictionary="modern_glyph_declared_v1",
        ).to_dict()
        safety = response["safety"]
        self.assertTrue(safety["calculation_only"])
        self.assertFalse(safety["interpretation_performed"])
        self.assertFalse(safety["name_quality_assessed"])
        self.assertFalse(safety["diagnosis_performed"])
        self.assertFalse(safety["prediction_performed"])


if __name__ == "__main__":
    unittest.main()
