from pathlib import Path
import json

ROOT = Path("data/master_packs")
OUTPUT_ROOT = Path("data")

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

def to_yaml_value(value, indent=0):
    space = "  " * indent
    if isinstance(value, list):
        if not value:
            return "[]"
        return "\n" + "\n".join(f"{space}- {v}" for v in value)
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(f"{space}{k}: {to_yaml_value(v, indent + 1)}")
        return "\n" + "\n".join(lines)
    return str(value)

def item_to_yaml(item):
    missing = [f for f in REQUIRED_FIELDS if f not in item]
    if missing:
        raise ValueError(f"{item.get('id', 'NO_ID')} missing fields: {missing}")

    lines = []
    for field in REQUIRED_FIELDS:
        value = item[field]
        if isinstance(value, list):
            lines.append(f"{field}:")
            for v in value:
                lines.append(f"  - {v}")
        else:
            lines.append(f"{field}: {value}")
    return "\n".join(lines) + "\n"

def main():
    master_files = sorted(ROOT.rglob("*.json"))
    if not master_files:
        print("No master pack files found.")
        return

    generated = 0

    for master_path in master_files:
        pack = json.loads(master_path.read_text(encoding="utf-8"))

        output_dir = OUTPUT_ROOT / pack["output_dir"]
        output_dir.mkdir(parents=True, exist_ok=True)

        for item in pack["items"]:
            filename = item["filename"]
            (output_dir / filename).write_text(item_to_yaml(item), encoding="utf-8")
            generated += 1

        index_path = output_dir / pack["index_filename"]
        index_path.write_text(pack["index_content"], encoding="utf-8")

    print(f"Generated {generated} items from {len(master_files)} master packs.")

if __name__ == "__main__":
    main()