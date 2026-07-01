from pathlib import Path
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
    warnings = []
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

        tags = data.get("tags")

        if not isinstance(tags, list):
            errors.append(f"[TAGS NOT LIST] {path}")
            continue

        if not tags:
            errors.append(f"[NO TAGS] {path}")
            continue

        has_cat = any(isinstance(t, str) and t.startswith("CAT:") for t in tags)
        has_attr = any(isinstance(t, str) and t.startswith("ATTR:") for t in tags)

        if not has_cat:
            warnings.append(f"[NO CAT TAG] {path}")

        if not has_attr:
            warnings.append(f"[NO ATTR TAG] {path}")

        for tag in tags:
            if not isinstance(tag, str):
                errors.append(f"[TAG NOT STRING] {path}: {tag}")
                continue

            if ":" not in tag:
                warnings.append(f"[TAG WITHOUT PREFIX] {path}: {tag}")

            if tag.strip() != tag:
                errors.append(f"[TAG HAS EXTRA SPACE] {path}: {tag}")

    print("=== Tag Consistency Audit ===")
    print(f"Item files: {len(item_files)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if errors:
        print("\n--- Errors ---")
        for e in errors:
            print(e)

    if warnings:
        print("\n--- Warnings ---")
        for w in warnings:
            print(w)

    if not errors and not warnings:
        print("\nOK: No tag consistency issues found.")

if __name__ == "__main__":
    main()