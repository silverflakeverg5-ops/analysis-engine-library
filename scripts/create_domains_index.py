from pathlib import Path

ROOT = Path("data/domains")
OUT = ROOT / "domains_index.yml"

files = sorted(p.name for p in ROOT.glob("DOM-*.yml"))

lines = [
    "category: Domains",
    "name_ja: 知識領域",
    "items:",
]

for name in files:
    lines.append(f"  - {name}")

lines.extend([
    "notes:",
    "  - domainsは知識領域・根拠領域・利用領域の参照材料として扱う",
    "  - Knowledge DB側では推論しない",
    "  - アプリ側で領域タグや根拠分類に利用する"
])

OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

print(f"Created: {OUT}")
print(f"Items: {len(files)}")