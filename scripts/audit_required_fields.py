from pathlib import Path
import yaml

ROOT = Path("data")

REQUIRED_FIELDS = [
    "id",
    "knowledge_type",
    "name_ja",
    "name_en",
    "category",
    "attribute",
    "definition_ja",
    "tags",
    "parent",
    "related",
    "observable_data",
    "signal_candidates",
    "device_level",
    "modifiers",
    "evidence",
    "status",
]

def is_item_file(path: Path) -> bool:
    if path.name.endswith("_index.yml"):
        return False
    if path.name in {"core_index.yml", "personality_index.yml"}:
        return False
    return path.suffix == ".yml"

def main():
    errors = []

    item_files = sorted(
        p for p in ROOT.rglob("*.yml")
        if is_item_file(p)
    )

    for path in item_files:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"[READ ERROR] {path}: {e}")
            continue

        if not isinstance(data, dict):
            errors.append(f"[INVALID YAML] {path}")
            continue

        for field in REQUIRED_FIELDS:
            if field not in data:
                errors.append(f"[MISSING FIELD] {path}: {field}")
                continue

            value = data[field]

            if value is None:
                errors.append(f"[NULL FIELD] {path}: {field}")
                continue

            if isinstance(value, str) and value.strip() == "":
                errors.append(f"[EMPTY STRING] {path}: {field}")
                continue

            if isinstance(value, list) and len(value) == 0:
                errors.append(f"[EMPTY LIST] {path}: {field}")

    print("=== Required Fields Audit ===")
    print(f"Item files: {len(item_files)}")
    print(f"Required fields: {len(REQUIRED_FIELDS)}")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\n--- Errors ---")
        for e in errors:
            print(e)
    else:
        print("\nOK: All required fields are valid.")

if __name__ == "__main__":
    main()