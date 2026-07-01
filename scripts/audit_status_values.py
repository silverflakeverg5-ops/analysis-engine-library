from pathlib import Path
import yaml

ROOT = Path("data")

ALLOWED_STATUS = {
    "active",
    "draft",
    "deprecated",
    "archived",
}

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
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"[READ ERROR] {path}: {e}")
            continue

        if not isinstance(data, dict):
            errors.append(f"[INVALID YAML] {path}")
            continue

        status = data.get("status")

        if status is None:
            errors.append(f"[NO STATUS] {path}")
            continue

        if status not in ALLOWED_STATUS:
            errors.append(f"[INVALID STATUS] {path}: {status}")

    print("=== Status Value Audit ===")
    print(f"Item files: {len(item_files)}")
    print(f"Errors: {len(errors)}")

    if errors:
        print("\n--- Errors ---")
        for e in errors:
            print(e)
    else:
        print("\nOK: No status value errors found.")

if __name__ == "__main__":
    main()