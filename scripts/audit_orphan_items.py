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
    item_files = {p.resolve() for p in ROOT.rglob("*.yml") if is_item_file(p)}
    referenced_files = set()
    errors = []

    index_files = sorted(ROOT.rglob("*_index.yml"))

    for index_path in index_files:
        try:
            data = yaml.safe_load(index_path.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"[INDEX READ ERROR] {index_path}: {e}")
            continue

        items = data.get("items", []) if isinstance(data, dict) else []

        for item_name in items:
            referenced_files.add((index_path.parent / item_name).resolve())

    orphan_files = sorted(item_files - referenced_files)

    print("=== Orphan Item Audit ===")
    print(f"Item files: {len(item_files)}")
    print(f"Referenced item files: {len(referenced_files)}")
    print(f"Orphan files: {len(orphan_files)}")
    print(f"Errors: {len(errors)}")

    if orphan_files:
        print("\n--- Orphan Files ---")
        for p in orphan_files:
            print(p)

    if errors:
        print("\n--- Errors ---")
        for e in errors:
            print(e)

    if not orphan_files and not errors:
        print("\nOK: No orphan item files found.")

if __name__ == "__main__":
    main()