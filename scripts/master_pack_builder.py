from pathlib import Path
import json

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

def validate_item(item: dict):
    missing = [f for f in REQUIRED_FIELDS if f not in item]
    if missing:
        raise ValueError(f"{item.get('id', 'NO_ID')} missing fields: {missing}")

def build_pack(output_path, output_dir, index_filename, index_name_ja, category, items, notes=None):
    notes = notes or []
    ids = set()
    filenames = []

    for item in items:
        validate_item(item)

        if item["id"] in ids:
            raise ValueError(f"Duplicate ID: {item['id']}")

        ids.add(item["id"])
        filenames.append(item["filename"])

    index_content = f"category: {category}\n"
    index_content += f"name_ja: {index_name_ja}\n"
    index_content += "items:\n"
    for filename in filenames:
        index_content += f"  - {filename}\n"

    if notes:
        index_content += "notes:\n"
        for note in notes:
            index_content += f"  - {note}\n"

    pack = {
        "output_dir": output_dir,
        "index_filename": index_filename,
        "index_content": index_content,
        "items": items,
    }

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(pack, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"Built master pack: {output_path}")
    print(f"Items: {len(items)}")