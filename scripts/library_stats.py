from pathlib import Path
from collections import Counter
import yaml

ROOT = Path("data")

INDEX_NAMES = {
    "core_index.yml",
    "personality_index.yml",
}

def is_item_file(path: Path) -> bool:
    name = path.name
    if name.endswith("_index.yml"):
        return False
    if name in INDEX_NAMES:
        return False
    return True

def main():
    yml_files = sorted(ROOT.rglob("*.yml"))
    item_files = [p for p in yml_files if is_item_file(p)]

    knowledge_types = Counter()
    categories = Counter()
    attributes = Counter()
    volumes = Counter()
    statuses = Counter()

    errors = []

    for path in item_files:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"[READ ERROR] {path}: {e}")
            continue

        if not isinstance(data, dict):
            errors.append(f"[INVALID YAML] {path}")
            continue

        knowledge_types[data.get("knowledge_type", "unknown")] += 1
        categories[data.get("category", "unknown")] += 1
        attributes[data.get("attribute", "unknown")] += 1
        statuses[data.get("status", "unknown")] += 1

        parts = path.parts
        if len(parts) >= 2:
            volumes[parts[1]] += 1

    print("=== Library Statistics ===")
    print(f"YAML files : {len(yml_files)}")
    print(f"Item files : {len(item_files)}")
    print(f"Read errors: {len(errors)}")

    print("\n--- By Volume ---")
    for k, v in sorted(volumes.items()):
        print(f"{k}: {v}")

    print("\n--- By Knowledge Type ---")
    for k, v in sorted(knowledge_types.items()):
        print(f"{k}: {v}")

    print("\n--- By Category ---")
    for k, v in sorted(categories.items()):
        print(f"{k}: {v}")

    print("\n--- By Status ---")
    for k, v in sorted(statuses.items()):
        print(f"{k}: {v}")

    if errors:
        print("\n--- Errors ---")
        for e in errors:
            print(e)

if __name__ == "__main__":
    main()