"""Deterministic, calculation-only adapter for modern Western numerology."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any
import unicodedata

from .divination import DIVINATION_SAFETY_MESSAGE_JA
from .library import API_VERSION, RUNTIME_VERSION


CALCULATION_CONVENTION = "modern_western_digit_sum"
MASTER_NUMBERS = (11, 22, 33)
VOWELS = frozenset("AEIOU")


class NumerologyValidationError(ValueError):
    """Raised when numerology calculation inputs are missing or ambiguous."""


@dataclass(frozen=True)
class NumberCalculation:
    """One auditable digit-reduction result without symbolic interpretation."""

    knowledge_id: str
    initial_total: int
    reduction_steps: tuple[int, ...]
    value: int
    master_number_preserved: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "knowledge_id": self.knowledge_id,
            "initial_total": self.initial_total,
            "reduction_steps": list(self.reduction_steps),
            "value": self.value,
            "master_number_preserved": self.master_number_preserved,
        }


@dataclass(frozen=True)
class NumerologyCalculation:
    """Privacy-minimized envelope containing arithmetic results and trace."""

    name_provided: bool
    normalized_name_letter_count: int
    target_year: int | None
    preserve_master_numbers: bool
    results: tuple[tuple[str, NumberCalculation], ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "api_version": API_VERSION,
            "runtime_version": RUNTIME_VERSION,
            "calculation": {
                "knowledge_type": "numerology",
                "convention": CALCULATION_CONVENTION,
                "master_numbers": list(MASTER_NUMBERS),
                "preserve_master_numbers": self.preserve_master_numbers,
                "input_summary": {
                    "birth_date_provided": True,
                    "name_provided": self.name_provided,
                    "normalized_name_letter_count": self.normalized_name_letter_count,
                    "target_year": self.target_year,
                    "raw_inputs_returned": False,
                    "inputs_stored": False,
                },
                "results": {
                    name: calculation.to_dict()
                    for name, calculation in self.results
                },
            },
            "safety": {
                "calculation_only": True,
                "cultural_interpretation_only": True,
                "interpretation_performed": False,
                "inference_performed": False,
                "scoring_performed": False,
                "ranking_performed": False,
                "diagnosis_performed": False,
                "prediction_performed": False,
                "mathematical_validity_implies_symbolic_validity": False,
                "message_ja": DIVINATION_SAFETY_MESSAGE_JA,
            },
        }


def _parse_birth_date(value: str) -> date:
    if not isinstance(value, str) or not value.strip():
        raise NumerologyValidationError("birth_date must be an ISO date string (YYYY-MM-DD)")
    if value != value.strip():
        raise NumerologyValidationError("birth_date cannot contain surrounding whitespace")
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise NumerologyValidationError(
            "birth_date must be a valid ISO date string (YYYY-MM-DD)"
        ) from exc
    if parsed.isoformat() != value:
        raise NumerologyValidationError("birth_date must use zero-padded YYYY-MM-DD format")
    return parsed


def _normalize_latin_name(value: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise NumerologyValidationError("name must contain at least one Latin letter")
    if len(value) > 200:
        raise NumerologyValidationError("name must be 200 characters or fewer")

    letters: list[str] = []
    for character in value:
        decomposed = unicodedata.normalize("NFKD", character)
        ascii_letters: list[str] = []
        unsupported_alpha = False
        for entry in decomposed:
            if unicodedata.combining(entry):
                continue
            upper = entry.upper()
            if len(upper) == 1 and "A" <= upper <= "Z":
                ascii_letters.append(upper)
            elif entry.isalpha():
                unsupported_alpha = True
        if ascii_letters:
            if unsupported_alpha:
                raise NumerologyValidationError(
                    "name contains letters outside the supported Latin mapping"
                )
            letters.extend(ascii_letters)
            continue
        if character.isspace() or character in "-'’.":
            continue
        if character.isalpha() or unsupported_alpha:
            raise NumerologyValidationError(
                "name contains letters outside the supported Latin mapping"
            )
        raise NumerologyValidationError("name contains an unsupported character")
    if not letters:
        raise NumerologyValidationError("name must contain at least one Latin letter")
    return "".join(letters)


def _letter_value(letter: str) -> int:
    return ((ord(letter) - ord("A")) % 9) + 1


def _reduce_number(
    initial_total: int,
    knowledge_id: str,
    preserve_master_numbers: bool,
) -> NumberCalculation:
    current = initial_total
    steps = [current]
    while current > 9 and not (
        preserve_master_numbers and current in MASTER_NUMBERS
    ):
        current = sum(int(digit) for digit in str(current))
        steps.append(current)
    return NumberCalculation(
        knowledge_id=knowledge_id,
        initial_total=initial_total,
        reduction_steps=tuple(steps),
        value=current,
        master_number_preserved=(
            preserve_master_numbers and current in MASTER_NUMBERS
        ),
    )


def calculate_numerology(
    birth_date: str,
    *,
    name: str | None = None,
    target_year: int | None = None,
    preserve_master_numbers: bool = True,
) -> NumerologyCalculation:
    """Calculate disclosed arithmetic values without generating interpretations."""
    if not isinstance(preserve_master_numbers, bool):
        raise NumerologyValidationError("preserve_master_numbers must be a boolean")
    parsed_date = _parse_birth_date(birth_date)
    if target_year is not None:
        if (
            not isinstance(target_year, int)
            or isinstance(target_year, bool)
            or not 1 <= target_year <= 9999
        ):
            raise NumerologyValidationError("target_year must be an integer from 1 to 9999")

    date_digits = [int(digit) for digit in birth_date if digit.isdigit()]
    results: list[tuple[str, NumberCalculation]] = [
        (
            "life_path",
            _reduce_number(sum(date_digits), "NUM-000011", preserve_master_numbers),
        ),
        (
            "birthday",
            _reduce_number(parsed_date.day, "NUM-000012", preserve_master_numbers),
        ),
        (
            "attitude",
            _reduce_number(
                parsed_date.month + parsed_date.day,
                "NUM-000018",
                preserve_master_numbers,
            ),
        ),
    ]

    if target_year is not None:
        results.append(
            (
                "personal_year",
                _reduce_number(
                    parsed_date.month
                    + parsed_date.day
                    + sum(int(digit) for digit in str(target_year)),
                    "NUM-000050",
                    preserve_master_numbers,
                ),
            )
        )

    normalized_name = ""
    if name is not None:
        normalized_name = _normalize_latin_name(name)
        values = [_letter_value(letter) for letter in normalized_name]
        vowel_values = [
            value
            for letter, value in zip(normalized_name, values)
            if letter in VOWELS
        ]
        consonant_values = [
            value
            for letter, value in zip(normalized_name, values)
            if letter not in VOWELS
        ]
        results.append(
            (
                "expression",
                _reduce_number(sum(values), "NUM-000013", preserve_master_numbers),
            )
        )
        if vowel_values:
            results.append(
                (
                    "soul_urge",
                    _reduce_number(
                        sum(vowel_values), "NUM-000014", preserve_master_numbers
                    ),
                )
            )
        if consonant_values:
            results.append(
                (
                    "personality",
                    _reduce_number(
                        sum(consonant_values),
                        "NUM-000015",
                        preserve_master_numbers,
                    ),
                )
            )

    return NumerologyCalculation(
        name_provided=name is not None,
        normalized_name_letter_count=len(normalized_name),
        target_year=target_year,
        preserve_master_numbers=preserve_master_numbers,
        results=tuple(results),
    )
