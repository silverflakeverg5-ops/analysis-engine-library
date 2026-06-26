import csv
import os
from pathlib import Path

MASTER_PATH = Path("data/master/domains_master.csv")
OUTPUT_DIR = Path("data/domains")

FIELD_ORDER = [
    "id",
    "name_ja",
    "name_en",
    "category_ja",
    "summary_ja",
    "status",
    "confidence",
    "source_level",
    "memo",
]


def yaml_escape(value: str) -> str:
    value = "" if value is None else str(value)
    value = value.replace('"', '\\"')
    return f'"{value}"'


def row_to_yaml(row: dict) -> str:
    lines = []
    for field in FIELD_ORDER:
        value = row.get(field, "")
        if field == "confidence":
            lines.append(f"{field}: {value}")
        else:
            lines.append(f"{field}: {yaml_escape(value)}")
    lines.append('version: "0.1.0"')
    lines.append('created_by: "ChatGPT"')
    lines.append('updated_by: "ChatGPT"')
    return "\n".join(lines) + "\n"


def main():
    if not MASTER_PATH.exists():
        raise FileNotFoundError(f"Master CSV not found: {MASTER_PATH}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with MASTER_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        raise ValueError("Master CSV is empty.")

    ids = set()
    for row in rows:
        item_id = row.get("id", "").strip()
        if not item_id:
            raise ValueError("Missing id in master CSV.")
        if item_id in ids:
            raise ValueError(f"Duplicate id found: {item_id}")
        ids.add(item_id)

        output_path = OUTPUT_DIR / f"{item_id}.yml"
        output_path.write_text(row_to_yaml(row), encoding="utf-8")

    print(f"Generated {len(rows)} domain YAML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
