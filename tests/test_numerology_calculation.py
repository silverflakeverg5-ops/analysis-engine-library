from __future__ import annotations

from pathlib import Path
import unittest

from analysis_engine import KnowledgeLibrary, NumerologyValidationError


ROOT = Path(__file__).resolve().parents[1]


class NumerologyCalculationIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.library = KnowledgeLibrary(ROOT / "data")

    def test_birth_date_calculations_are_deterministic_and_traced(self) -> None:
        result = self.library.calculate_numerology(
            "1990-01-01",
            target_year=2026,
        ).to_dict()
        values = result["calculation"]["results"]
        self.assertEqual(values["life_path"]["reduction_steps"], [21, 3])
        self.assertEqual(values["life_path"]["value"], 3)
        self.assertEqual(values["birthday"]["value"], 1)
        self.assertEqual(values["attitude"]["value"], 2)
        self.assertEqual(values["personal_year"]["value"], 3)
        for calculation in values.values():
            reference = self.library.require(calculation["knowledge_id"])
            self.assertEqual(reference["knowledge_type"], "numerology")

    def test_master_number_policy_is_explicit(self) -> None:
        preserved = self.library.calculate_numerology("2000-01-08").to_dict()
        reduced = self.library.calculate_numerology(
            "2000-01-08",
            preserve_master_numbers=False,
        ).to_dict()
        self.assertEqual(
            preserved["calculation"]["results"]["life_path"]["value"], 11
        )
        self.assertTrue(
            preserved["calculation"]["results"]["life_path"][
                "master_number_preserved"
            ]
        )
        self.assertEqual(
            reduced["calculation"]["results"]["life_path"]["value"], 2
        )

    def test_latin_name_calculations_do_not_echo_raw_inputs(self) -> None:
        response = self.library.calculate_numerology(
            "1990-01-01",
            name="Jane Doe",
        ).to_dict()
        calculation = response["calculation"]
        self.assertEqual(calculation["results"]["expression"]["value"], 9)
        self.assertEqual(calculation["results"]["soul_urge"]["value"], 8)
        self.assertEqual(calculation["results"]["personality"]["value"], 1)
        self.assertEqual(calculation["input_summary"]["normalized_name_letter_count"], 7)
        self.assertFalse(calculation["input_summary"]["raw_inputs_returned"])
        self.assertNotIn("Jane", str(response))

    def test_accented_latin_letters_are_normalized(self) -> None:
        accented = self.library.calculate_numerology(
            "1990-01-01", name="José"
        ).to_dict()
        plain = self.library.calculate_numerology(
            "1990-01-01", name="Jose"
        ).to_dict()
        self.assertEqual(
            accented["calculation"]["results"],
            plain["calculation"]["results"],
        )

    def test_invalid_or_unsupported_inputs_fail_closed(self) -> None:
        invalid_calls = (
            lambda: self.library.calculate_numerology("1990-02-30"),
            lambda: self.library.calculate_numerology("1990-1-1"),
            lambda: self.library.calculate_numerology("1990-01-01", name="山田太郎"),
            lambda: self.library.calculate_numerology("1990-01-01", target_year=0),
            lambda: self.library.calculate_numerology(
                "1990-01-01", preserve_master_numbers=1
            ),
        )
        for call in invalid_calls:
            with self.subTest(call=call):
                with self.assertRaises(NumerologyValidationError):
                    call()

    def test_output_is_calculation_only(self) -> None:
        response = self.library.calculate_numerology("1990-01-01").to_dict()
        safety = response["safety"]
        self.assertTrue(safety["calculation_only"])
        self.assertFalse(safety["interpretation_performed"])
        self.assertFalse(safety["inference_performed"])
        self.assertFalse(safety["diagnosis_performed"])
        self.assertFalse(safety["prediction_performed"])
        self.assertFalse(safety["mathematical_validity_implies_symbolic_validity"])


if __name__ == "__main__":
    unittest.main()
