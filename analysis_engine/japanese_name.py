"""Calculation-only Japanese five-grid name adapter with explicit strokes."""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Any, Mapping, Sequence

from .divination import DIVINATION_SAFETY_MESSAGE_JA
from .library import API_VERSION, RUNTIME_VERSION


CALCULATION_CONVENTION = "japanese_five_grid_explicit_strokes_v1"
ELEMENT_BY_LAST_DIGIT = {
    1: "wood",
    2: "wood",
    3: "fire",
    4: "fire",
    5: "earth",
    6: "earth",
    7: "metal",
    8: "metal",
    9: "water",
    0: "water",
}


class JapaneseNameValidationError(ValueError):
    """Raised when a Japanese name calculation cannot be reproduced safely."""


@dataclass(frozen=True)
class GridCalculation:
    knowledge_id: str
    value: int
    components: tuple[int, ...]
    virtual_strokes: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "knowledge_id": self.knowledge_id,
            "value": self.value,
            "components": list(self.components),
            "virtual_strokes": self.virtual_strokes,
        }


@dataclass(frozen=True)
class JapaneseNameCalculation:
    stroke_dictionary: str
    single_character_adjustment: str
    surname_strokes: tuple[int, ...]
    given_strokes: tuple[int, ...]
    grids: tuple[tuple[str, GridCalculation], ...]
    yin_yang_sequence: tuple[str, ...]
    three_talents: tuple[tuple[str, str], ...]
    stroke_resolution: str = "explicit_sequence"

    def to_dict(self) -> dict[str, Any]:
        return {
            "api_version": API_VERSION,
            "runtime_version": RUNTIME_VERSION,
            "calculation": {
                "knowledge_type": "name_divination",
                "convention": CALCULATION_CONVENTION,
                "stroke_dictionary": self.stroke_dictionary,
                "stroke_resolution": self.stroke_resolution,
                "single_character_adjustment": self.single_character_adjustment,
                "input_summary": {
                    "surname_character_count": len(self.surname_strokes),
                    "given_character_count": len(self.given_strokes),
                    "raw_names_returned": False,
                    "names_stored": False,
                    "stroke_sequence_returned_for_audit": True,
                },
                "stroke_trace": {
                    "surname": list(self.surname_strokes),
                    "given": list(self.given_strokes),
                },
                "grids": {
                    name: calculation.to_dict()
                    for name, calculation in self.grids
                },
                "yin_yang": {
                    "knowledge_id": "NAM-000038",
                    "sequence": list(self.yin_yang_sequence),
                    "rule": "odd_yang_even_yin",
                },
                "three_talents": {
                    "knowledge_id": "NAM-000040",
                    "sequence": {
                        name: element for name, element in self.three_talents
                    },
                    "rule": "grid_last_digit_to_five_phase",
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
                "name_quality_assessed": False,
                "message_ja": DIVINATION_SAFETY_MESSAGE_JA,
            },
        }


def _is_japanese_name_character(character: str) -> bool:
    code = ord(character)
    return (
        0x3040 <= code <= 0x309F
        or 0x30A0 <= code <= 0x30FF
        or 0x3400 <= code <= 0x4DBF
        or 0x4E00 <= code <= 0x9FFF
        or 0xF900 <= code <= 0xFAFF
        or character in {"々", "〆"}
    )


def _validate_name_part(value: str, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise JapaneseNameValidationError(f"{field} must be a non-empty Japanese string")
    if len(value) > 20:
        raise JapaneseNameValidationError(f"{field} must be 20 characters or fewer")
    if any(not _is_japanese_name_character(character) for character in value):
        raise JapaneseNameValidationError(
            f"{field} contains a character outside supported kanji, hiragana, or katakana"
        )
    return value


def _validate_strokes(
    values: Sequence[int],
    expected_length: int,
    field: str,
) -> tuple[int, ...]:
    if isinstance(values, (str, bytes)):
        raise JapaneseNameValidationError(f"{field} must be a sequence of integers")
    try:
        normalized = tuple(values)
    except TypeError as exc:
        raise JapaneseNameValidationError(
            f"{field} must be a sequence of integers"
        ) from exc
    if len(normalized) != expected_length:
        raise JapaneseNameValidationError(
            f"{field} count must match the corresponding name character count"
        )
    if any(
        not isinstance(value, int)
        or isinstance(value, bool)
        or not 1 <= value <= 64
        for value in normalized
    ):
        raise JapaneseNameValidationError(
            f"{field} values must be integers from 1 to 64"
        )
    return normalized


def _element(value: int) -> str:
    return ELEMENT_BY_LAST_DIGIT[value % 10]


def _validate_dictionary_id(value: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise JapaneseNameValidationError("stroke_dictionary must be declared")
    if len(value) > 100:
        raise JapaneseNameValidationError(
            "stroke_dictionary must be 100 characters or fewer"
        )
    return value.strip()


def calculate_japanese_name(
    surname: str,
    given_name: str,
    *,
    surname_strokes: Sequence[int],
    given_strokes: Sequence[int],
    stroke_dictionary: str,
    single_character_adjustment: str = "virtual_one",
) -> JapaneseNameCalculation:
    """Calculate five-grid arithmetic from user-declared, auditable strokes."""
    normalized_surname = _validate_name_part(surname, "surname")
    normalized_given = _validate_name_part(given_name, "given_name")
    family = _validate_strokes(
        surname_strokes, len(normalized_surname), "surname_strokes"
    )
    given = _validate_strokes(
        given_strokes, len(normalized_given), "given_strokes"
    )
    dictionary_id = _validate_dictionary_id(stroke_dictionary)
    if single_character_adjustment not in {"virtual_one", "none"}:
        raise JapaneseNameValidationError(
            "single_character_adjustment must be: virtual_one or none"
        )

    virtual_family = int(
        single_character_adjustment == "virtual_one" and len(family) == 1
    )
    virtual_given = int(
        single_character_adjustment == "virtual_one" and len(given) == 1
    )
    heaven_components = family
    person_components = (family[-1], given[0])
    earth_components = given
    outer_components = family[:-1] + given[1:]
    total_components = family + given

    heaven_value = sum(heaven_components) + virtual_family
    person_value = sum(person_components)
    earth_value = sum(earth_components) + virtual_given
    outer_value = sum(outer_components) + virtual_family + virtual_given
    total_value = sum(total_components)

    grids = (
        (
            "heaven",
            GridCalculation(
                "NAM-000031", heaven_value, heaven_components, virtual_family
            ),
        ),
        (
            "person",
            GridCalculation("NAM-000032", person_value, person_components, 0),
        ),
        (
            "earth",
            GridCalculation(
                "NAM-000033", earth_value, earth_components, virtual_given
            ),
        ),
        (
            "outer",
            GridCalculation(
                "NAM-000034",
                outer_value,
                outer_components,
                virtual_family + virtual_given,
            ),
        ),
        (
            "total",
            GridCalculation("NAM-000035", total_value, total_components, 0),
        ),
    )
    yin_yang = tuple(
        "yang" if stroke % 2 else "yin" for stroke in total_components
    )
    talents = (
        ("heaven", _element(heaven_value)),
        ("person", _element(person_value)),
        ("earth", _element(earth_value)),
    )
    return JapaneseNameCalculation(
        stroke_dictionary=dictionary_id,
        single_character_adjustment=single_character_adjustment,
        surname_strokes=family,
        given_strokes=given,
        grids=grids,
        yin_yang_sequence=yin_yang,
        three_talents=talents,
    )


def calculate_japanese_name_from_dictionary(
    surname: str,
    given_name: str,
    *,
    stroke_dictionary: Mapping[str, int],
    stroke_dictionary_id: str,
    single_character_adjustment: str = "virtual_one",
) -> JapaneseNameCalculation:
    """Resolve exact characters through a caller-selected stroke dictionary."""
    normalized_surname = _validate_name_part(surname, "surname")
    normalized_given = _validate_name_part(given_name, "given_name")
    dictionary_id = _validate_dictionary_id(stroke_dictionary_id)
    if not isinstance(stroke_dictionary, Mapping):
        raise JapaneseNameValidationError("stroke_dictionary must be a character mapping")
    if not stroke_dictionary:
        raise JapaneseNameValidationError("stroke_dictionary mapping cannot be empty")
    if len(stroke_dictionary) > 100_000:
        raise JapaneseNameValidationError(
            "stroke_dictionary mapping cannot exceed 100000 entries"
        )

    used_characters = tuple(dict.fromkeys(normalized_surname + normalized_given))
    missing = [character for character in used_characters if character not in stroke_dictionary]
    if missing:
        raise JapaneseNameValidationError(
            "stroke_dictionary has no exact entry for: " + ", ".join(missing)
        )

    family = _validate_strokes(
        [stroke_dictionary[character] for character in normalized_surname],
        len(normalized_surname),
        "resolved surname strokes",
    )
    given = _validate_strokes(
        [stroke_dictionary[character] for character in normalized_given],
        len(normalized_given),
        "resolved given strokes",
    )
    result = calculate_japanese_name(
        normalized_surname,
        normalized_given,
        surname_strokes=family,
        given_strokes=given,
        stroke_dictionary=dictionary_id,
        single_character_adjustment=single_character_adjustment,
    )
    return replace(result, stroke_resolution="dictionary_lookup")
