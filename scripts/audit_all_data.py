from pathlib import Path
import re

BASE = Path("data")

REQUIRED_FIELDS = [
    "id:",
    "name_ja:",
    "name_en:",
    "category:",
    "attribute:",
    "definition_ja:",
    "parent:",
    "related:",
    "observable_data:",
    "signal_candidates:",
    "device_level:",
    "modifiers:",
    "evidence:",
    "status:",
]

def is_item_file(path: Path):
    name = path.name
    if name.endswith("_index.yml"):
        return False
    if name in ["core_index.yml", "personality_index.yml"]:
        return False
    return True

def main():
    yml_files = sorted(BASE.rglob("*.yml"))
    item_files = [p for p in yml_files if is_item_file(p)]

    ids = {}
    errors = []

    for path in item_files:
        text = path.read_text(encoding="utf-8")

        id_match = re.search(r"^id:\s*(.+)$", text, re.MULTILINE)
        if not id_match:
            errors.append(f"[NO ID] {path}")
            continue

        item_id = id_match.group(1).strip()

        if item_id in ids:
            errors.append(f"[DUPLICATE ID] {item_id}: {ids[item_id]} / {path}")

        ids[item_id] = path

        for field in REQUIRED_FIELDS:
            if field not in text:
                errors.append(f"[MISSING {field}] {path}")

    print("=== All Data Audit ===")
    print(f"YAML files: {len(yml_files)}")
    print(f"Item files: {len(item_files)}")
    print(f"Item IDs: {len(ids)}")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\n--- Errors ---")
        for e in errors:
            print(e)
    else:
        print("\nOK: No critical errors found.")

if __name__ == "__main__":
    main()