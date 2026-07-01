from pathlib import Path
import yaml
from collections import Counter

ROOT = Path("data")

counter = Counter()
knowledge = Counter()

for f in ROOT.rglob("*.yml"):
    if "index" in f.name.lower():
        continue

    counter["yaml"] += 1

    try:
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
    except Exception:
        counter["error"] += 1
        continue

    knowledge[data.get("knowledge_type", "unknown")] += 1
    counter[data.get("category", "Unknown")] += 1

print("\n=== Library Statistics ===")
print(f"YAML Files : {counter['yaml']}")
print(f"Read Errors: {counter['error']}")

print("\nKnowledge Types")
for k, v in sorted(knowledge.items()):
    print(f"{k:25} {v}")

print("\nCategories")
for k, v in sorted(counter.items()):
    if k in ("yaml", "error"):
        continue
    print(f"{k:25} {v}")