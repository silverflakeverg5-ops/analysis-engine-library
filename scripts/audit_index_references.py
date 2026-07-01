from pathlib import Path
import yaml

ROOT = Path("data")

def main():
    errors = []
    index_files = sorted(ROOT.rglob("*_index.yml"))

    for index_path in index_files:
        data = yaml.safe_load(index_path.read_text(encoding="utf-8"))

        if not isinstance(data, dict):
            errors.append(f"[INVALID INDEX YAML] {index_path}")
            continue

        items = data.get("items", [])
        if not isinstance(items, list):
            errors.append(f"[ITEMS NOT LIST] {index_path}")
            continue

        for item_name in items:
            item_path = index_path.parent / item_name
            if not item_path.exists():
                errors.append(f"[MISSING ITEM] {index_path} -> {item_name}")

    print("=== Index Reference Audit ===")
    print(f"Index files: {len(index_files)}")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\n--- Errors ---")
        for e in errors:
            print(e)
    else:
        print("\nOK: No index reference errors found.")

if __name__ == "__main__":
    main()