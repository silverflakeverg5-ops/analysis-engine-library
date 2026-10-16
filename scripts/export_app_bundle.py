"""Export the versioned data bundle that the secretary app ships.

The bundle contains only data: a knowledge subset, the notification-profile
rules, and a precomputed daily calendar table. The app reads these files and
never runs Python. Every file is listed in ``manifest.json`` with its SHA-256.

Usage:
    python scripts/export_app_bundle.py [--out exports/app_bundle] [--start 2020-01-01] [--end 2040-12-31]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from analysis_engine import KnowledgeLibrary  # noqa: E402
from analysis_engine.library import RUNTIME_VERSION  # noqa: E402
from analysis_profile import load_rules  # noqa: E402
from calendar_tables import (  # noqa: E402
    LUNISOLAR_METHOD,
    NINE_STAR_METHOD,
    SHANICHI_METHOD,
    SUPPORTED_END,
    SUPPORTED_START,
    daily_notes,
)


BUNDLE_FORMAT = "secretary-app-bundle-v1"
CATALOG_TYPES = ("calendar_notes", "nine_star_ki", "numerology", "sukuyo")
SEASONAL_BASE_NAMES = {
    "春の彼岸入り": "彼岸", "春の彼岸中日": "彼岸", "春の彼岸明け": "彼岸",
    "秋の彼岸入り": "彼岸", "秋の彼岸中日": "彼岸", "秋の彼岸明け": "彼岸",
    "春社日": "社日", "秋社日": "社日",
    "冬の土用入り": "土用", "春の土用入り": "土用", "夏の土用入り": "土用", "秋の土用入り": "土用",
}
PUBLIC_FIELDS = (
    "id", "knowledge_type", "name_ja", "name_en", "category", "attribute",
    "definition_ja", "tags", "status", "tradition", "evidence_class",
    "required_inputs", "calculation_basis", "interpretive_scope",
    "safe_expression", "provenance",
)


def _collect_rule_refs(rules) -> set[str]:
    refs: set[str] = set()
    for group in ("behavior_signals", "tendencies", "axes"):
        for entry in rules[group]:
            refs.update(entry.get("knowledge_refs", []))
    return refs


def _public_item(item) -> dict:
    return {field: item[field] for field in PUBLIC_FIELDS if field in item}


def build_knowledge(library: KnowledgeLibrary, rules) -> dict:
    items: dict[str, dict] = {}
    for knowledge_type in CATALOG_TYPES:
        offset = 0
        while True:
            page = library.search(knowledge_type=knowledge_type, offset=offset, limit=100)
            for item in page.items:
                items[item["id"]] = _public_item(item)
            offset += page.returned
            if not page.has_more:
                break
    # Rule references stay traceable by ID only. They carry no display text so
    # the app cannot show tendency or domain names to the user (spec A.3).
    for item_id in sorted(_collect_rule_refs(rules)):
        library.require(item_id)
        items.setdefault(item_id, {"id": item_id, "rule_reference_only": True})
    return {"runtimeVersion": RUNTIME_VERSION, "catalogTypes": list(CATALOG_TYPES), "items": [items[key] for key in sorted(items)]}


def _name_index(library: KnowledgeLibrary, knowledge_type: str) -> dict[str, str]:
    page = library.search(knowledge_type=knowledge_type, limit=100)
    return {item["name_ja"]: item["id"] for item in page.items}


def build_calendar(library: KnowledgeLibrary, start: date, end: date) -> dict:
    koy = _name_index(library, "calendar_notes")
    nsk = _name_index(library, "nine_star_ki")
    days = []
    day = start
    while day <= end:
        notes = daily_notes(day)
        names = [notes["rokuyo"], notes["twelveDirective"], *notes["selectedDays"]]
        names += [SEASONAL_BASE_NAMES.get(label, label) for label in notes["seasonalDays"]]
        note_ids = []
        for name in names:
            if name not in koy:
                raise KeyError(f"calendar note without KOY item: {name}")
            if koy[name] not in note_ids:
                note_ids.append(koy[name])
        notes["noteIds"] = note_ids
        notes["nineStarDay"]["starId"] = nsk[notes["nineStarDay"]["star"]]
        days.append(notes)
        day += timedelta(days=1)
    return {
        "range": {"start": start.isoformat(), "end": end.isoformat()},
        "timezone": "Asia/Tokyo",
        "dayBoundary": "00:00 JST",
        "methods": {
            "lunisolar": LUNISOLAR_METHOD,
            "nineStarDay": NINE_STAR_METHOD,
            "shanichi": SHANICHI_METHOD,
            "astronomy": "Meeus VSOP87 truncated Sun, ELP-2000/82 truncated Moon, Espenak-Meeus Delta T",
        },
        "boundary_ja": "暦注は民間の伝承であり、事実の予測ではない。範囲外の日付では暦注を表示しない。",
        "days": days,
    }


def _write(path: Path, payload: dict) -> str:
    text = json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=False)
    path.write_text(text + "\n", encoding="utf-8")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def export_bundle(out_dir: Path, start: date = SUPPORTED_START, end: date = SUPPORTED_END) -> dict:
    if start < SUPPORTED_START or end > SUPPORTED_END or start > end:
        raise ValueError(f"range must be within {SUPPORTED_START}..{SUPPORTED_END}")
    library = KnowledgeLibrary(ROOT / "data")
    rules = load_rules()
    out_dir.mkdir(parents=True, exist_ok=True)
    files = {
        "knowledge.json": build_knowledge(library, rules),
        "notification_profile_rules.json": dict(rules),
        f"calendar_{start.year}_{end.year}.json": build_calendar(library, start, end),
    }
    manifest_files = []
    for name, payload in files.items():
        digest = _write(out_dir / name, payload)
        manifest_files.append({"path": name, "sha256": digest, "bytes": (out_dir / name).stat().st_size})
    manifest = {
        "format": BUNDLE_FORMAT,
        "runtimeVersion": RUNTIME_VERSION,
        "rulesVersion": rules["rules_version"],
        "calendarRange": {"start": start.isoformat(), "end": end.isoformat()},
        "files": manifest_files,
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", default=str(ROOT / "exports" / "app_bundle"))
    parser.add_argument("--start", default=SUPPORTED_START.isoformat())
    parser.add_argument("--end", default=SUPPORTED_END.isoformat())
    args = parser.parse_args()
    manifest = export_bundle(Path(args.out), date.fromisoformat(args.start), date.fromisoformat(args.end))
    for entry in manifest["files"]:
        print(f"{entry['path']}: {entry['bytes']} bytes sha256={entry['sha256'][:12]}")


if __name__ == "__main__":
    main()
