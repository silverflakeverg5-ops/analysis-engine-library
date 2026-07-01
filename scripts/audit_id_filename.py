from pathlib import Path
import re
import yaml

ROOT = Path("data")

def is_item_file(path: Path) -> bool:
    if path.name.endswith("_index.yml"):
        return False
    if path.name in {"core_index.yml", "personality_index.yml"}:
        return False
    return path.suffix == ".yml"

def main():
    errors = []
    item_files = [p for p in ROOT.rglob("*.yml") if is_item_file(p)]

    for path in item_files:
        text = path.read_text(encoding="utf-8")
        data = yaml.safe_load(text)

        item_id = data.get("id")
        if not item_id:
            errors.append(f"[NO ID] {path}")
            continue

        if not path.name.startswith(item_id + "_"):
            errors.append(f"[FILENAME ID MISMATCH] id={item_id} file={path}")

        if not re.match(r"^[A-Z]+-[0-9]{6}$", item_id):
            errors.append(f"[INVALID ID FORMAT] {item_id} file={path}")

    print("=== ID / Filename Audit ===")
    print(f"Item files: {len(item_files)}")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\n--- Errors ---")
        for e in errors:
            print(e)
    else:
        print("\nOK: No ID / filename errors found.")

if __name__ == "__main__":
    main()