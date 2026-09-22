"""Fail-closed audit for the Vol31 divination-reference boundary."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from analysis_engine import KnowledgeLibrary


EXPECTED_CATALOGS = {
    "divination_reference": {f"DIV-{number:06d}" for number in range(1, 101)},
    "western_astrology": {f"AST-{number:06d}" for number in range(1, 101)},
    "yin_yang_wuxing": {f"WUX-{number:06d}" for number in range(1, 101)},
    "four_pillars": {f"BAZ-{number:06d}" for number in range(1, 101)},
    "indian_astrology": {f"JYO-{number:06d}" for number in range(1, 101)},
    "zi_wei_dou_shu": {f"ZWD-{number:06d}" for number in range(1, 101)},
    "nine_star_ki": {f"NSK-{number:06d}" for number in range(1, 101)},
    "sukuyo": {f"SUK-{number:06d}" for number in range(1, 101)},
    "numerology": {f"NUM-{number:06d}" for number in range(1, 101)},
    "name_divination": {f"NAM-{number:06d}" for number in range(1, 101)},
    "feng_shui": {f"FSH-{number:06d}" for number in range(1, 101)},
}
REQUIRED_FIELDS = {
    "tradition",
    "source_type",
    "evidence_class",
    "required_inputs",
    "calculation_basis",
    "trait_links",
    "interpretive_scope",
    "safe_expression",
    "provenance",
}
FORBIDDEN_MODALITIES = {"手相", "顔相", "palmistry", "physiognomy"}


def main() -> None:
    library = KnowledgeLibrary(ROOT / "data")
    items = []
    errors: list[str] = []

    for knowledge_type, expected_ids in EXPECTED_CATALOGS.items():
        result = library.search(
            knowledge_type=knowledge_type,
            status="active",
            limit=100,
        )
        catalog_items = list(result.items)
        items.extend(catalog_items)
        actual_ids = {str(item.get("id")) for item in catalog_items}
        if result.total != 100:
            errors.append(
                f"{knowledge_type}: expected 100 active items, found {result.total}"
            )
        missing_ids = sorted(expected_ids - actual_ids)
        unexpected_ids = sorted(actual_ids - expected_ids)
        if missing_ids:
            errors.append(f"{knowledge_type}: missing IDs: " + ", ".join(missing_ids))
        if unexpected_ids:
            errors.append(
                f"{knowledge_type}: unexpected IDs: " + ", ".join(unexpected_ids)
            )

    for item in items:
        item_id = str(item.get("id", "unknown"))
        missing = sorted(REQUIRED_FIELDS - set(item))
        if missing:
            errors.append(f"{item_id}: missing fields: {', '.join(missing)}")
        if item.get("evidence_class") != "traditional_cultural_interpretation":
            errors.append(f"{item_id}: invalid evidence_class")
        safe_expression = str(item.get("safe_expression", ""))
        if "断定するものではありません" not in safe_expression:
            errors.append(f"{item_id}: safe_expression lacks non-assertion boundary")
        searchable = " ".join(str(value) for value in item.values()).casefold()
        for modality in FORBIDDEN_MODALITIES:
            if modality.casefold() in searchable:
                errors.append(f"{item_id}: deferred image modality found: {modality}")

    print("=== Divination Reference Audit ===")
    print(f"Items: {len(items)}")
    print(f"Errors: {len(errors)}")
    if errors:
        print("\n--- Errors ---")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)
    print("\nOK: Vol31-Vol41 preserve provenance, evidence, and non-diagnostic boundaries.")


if __name__ == "__main__":
    main()
