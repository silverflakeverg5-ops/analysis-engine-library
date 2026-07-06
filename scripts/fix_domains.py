from pathlib import Path
import yaml

ROOT = Path("data/domains")

for path in sorted(ROOT.glob("DOM-*.yml")):

    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    if not isinstance(data, dict):
        continue

    item_id = data["id"]

    slug = (
        data.get("name_en")
        or data.get("name_ja")
        or item_id
    )

    slug = (
        slug.lower()
        .replace(" ", "_")
        .replace("/", "_")
        .replace("-", "_")
    )

    new_name = f"{item_id}_{slug}.yml"

    if path.name != new_name:
        path.rename(path.with_name(new_name))

print("Domains renamed.")