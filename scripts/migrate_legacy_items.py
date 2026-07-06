from pathlib import Path
import yaml

ROOT = Path("data")

TARGET_DIRS = [
    "domains",
    "vol1_core",
    "vol2_personality",
    "vol3_behavior",
]

DEFAULTS = {
    "knowledge_type": "legacy_item",
    "device_level": "DB管理用",
    "status": "active",
    "parent": [],
    "related": [],
    "observable_data": [],
    "signal_candidates": [],
    "modifiers": [],
    "evidence": "Legacy knowledge item migrated automatically."
}


def is_target(path: Path):
    return len(path.parts) >= 2 and path.parts[1] in TARGET_DIRS


def is_item(path: Path):
    if path.name.endswith("_index.yml"):
        return False
    if path.name in {"core_index.yml", "personality_index.yml"}:
        return False
    return path.suffix == ".yml"


updated = 0

for path in ROOT.rglob("*.yml"):

    if not is_item(path):
        continue

    if not is_target(path):
        continue

    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    if not isinstance(data, dict):
        continue

    for k, v in DEFAULTS.items():
        data.setdefault(k, v)

    data.setdefault("category", path.parent.name.replace("_", " ").title())
    data.setdefault("attribute", path.parent.name)
    data.setdefault("definition_ja", data.get("name_ja", ""))

    if "tags" not in data or not isinstance(data["tags"], list):
        data["tags"] = [
            f"CAT:{data['category']}",
            f"ATTR:{data['attribute']}"
        ]

    path.write_text(
        yaml.safe_dump(
            data,
            allow_unicode=True,
            sort_keys=False
        ),
        encoding="utf-8"
    )

    updated += 1

print(f"Updated {updated} files.")