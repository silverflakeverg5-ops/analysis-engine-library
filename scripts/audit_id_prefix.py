"""Audit Knowledge Item ID prefixes without modifying repository data.

The audit targets Knowledge Items through the latest volume registered in
``EXPECTED_PREFIX_BY_VOLUME``. It also compares their IDs with later volumes so that
reserved-prefix and duplicate-ID collisions are visible before migration.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
import re


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = REPOSITORY_ROOT / "data"
ID_PATTERN = re.compile(r"^(?P<prefix>[A-Z]+)-(?P<number>[0-9]{6})$")
ID_LINE_PATTERN = re.compile(r"^id:\s*(?P<id>.+?)\s*$", re.MULTILINE)
VOLUME_PATTERN = re.compile(r"^vol(?P<number>[0-9]+)(?:_|$)")

# Approved by the project guide.  A volume number and an ID prefix describe
# different things; this table therefore maps the current domain volumes to
# their canonical Knowledge domain prefixes only where the guide defines one.
APPROVED_PREFIXES = {
    "ATT": "Attention",
    "MEM": "Memory",
    "EXE": "Executive Function",
    "PRO": "Processing",
    "REA": "Reasoning",
    "SPA": "Spatial Cognition",
    "PER": "Personality",
    "BEH": "Behavior",
    "COG": "Cognitive Bias",
    "CSC": "Cognitive Science",
    "NEU": "Neuroscience",
    "ENV": "Environment",
    "PHY": "Physiology",
    "SOC": "Social Psychology",
    "LEA": "Learning Theory",
    "OBS": "Observation Signal",
    "MOD": "Modifier",
    "EVD": "Evidence",
    "APP": "App Use Case",
    "DSP": "Display Design",
    "SAF": "Safety",
    "LIB": "Library Governance",
    "RDM": "Roadmap",
    "MAP": "Mapping Rule",
    "API": "API Contract",
    "TST": "Test Case",
    "DOC": "Documentation",
    "EMO": "Emotion",
    "MOT": "Motivation",
    "COM": "Communication",
    "REL": "Relationship",
    "GMB": "Game Behavior",
    "DEC": "Decision Strategy",
    "DEV": "Development",
    "CUL": "Culture",
    "DIV": "Divination Reference",
    "AST": "Western Astrology",
    "WUX": "Yin Yang and Five Phases",
    "BAZ": "Four Pillars",
    "JYO": "Indian Astrology",
    "ZWD": "Zi Wei Dou Shu",
    "NSK": "Nine Star Ki",
    "SUK": "Sukuyo",
    "NUM": "Numerology",
    "NAM": "Name Divination",
    "FSH": "Feng Shui",
}

EXPECTED_PREFIX_BY_VOLUME = {
    2: "PER",
    3: "BEH",
    4: "COG",
    5: "CSC",
    6: "NEU",
    7: "ENV",
    8: "PHY",
    9: "SOC",
    10: "LEA",
    11: "OBS",
    12: "MOD",
    13: "EVD",
    14: "APP",
    15: "DSP",
    16: "SAF",
    17: "LIB",
    18: "RDM",
    19: "MAP",
    20: "API",
    21: "TST",
    22: "DOC",
    23: "EMO",
    24: "MOT",
    25: "COM",
    26: "REL",
    27: "GMB",
    28: "DEC",
    29: "DEV",
    30: "CUL",
    31: "DIV",
    32: "AST",
    33: "WUX",
    34: "BAZ",
    35: "JYO",
    36: "ZWD",
    37: "NSK",
    38: "SUK",
    39: "NUM",
    40: "NAM",
    41: "FSH",
}

AUDIT_MAX_VOLUME = max(EXPECTED_PREFIX_BY_VOLUME)

# These prefixes belong to planned or newly added domain volumes.  Their use
# in Vol1-22 is a collision even though the prefix itself is approved.
RESERVED_PREFIXES = {
    "EMO": "vol23_emotion_core",
    "MOT": "vol24_motivation_core",
    "COM": "vol25_communication_core",
    "REL": "vol26_relationship_core",
    "GMB": "vol27_game_behavior",
    "DEC": "vol28_decision_strategy",
    "DEV": "vol29_development",
    "CUL": "vol30_culture_context",
    "DIV": "vol31_divination_reference",
    "AST": "vol32_western_astrology",
    "WUX": "vol33_yin_yang_wuxing",
    "BAZ": "vol34_four_pillars",
    "JYO": "vol35_indian_astrology",
    "ZWD": "vol36_zi_wei_dou_shu",
    "NSK": "vol37_nine_star_ki",
    "SUK": "vol38_sukuyo",
    "NUM": "vol39_numerology",
    "NAM": "vol40_name_divination",
    "FSH": "vol41_feng_shui",
}


@dataclass(frozen=True)
class Item:
    path: Path
    item_id: str
    prefix: str | None
    volume: int


def volume_number(path: Path) -> int | None:
    """Return the data volume number for a path, if it is in a volume."""
    try:
        relative = path.relative_to(DATA_ROOT)
    except ValueError:
        return None
    if not relative.parts:
        return None
    match = VOLUME_PATTERN.match(relative.parts[0])
    return int(match.group("number")) if match else None


def is_item_file(path: Path) -> bool:
    """Match the repository's existing Knowledge Item audit convention."""
    if path.suffix != ".yml":
        return False
    if path.name.endswith("_index.yml"):
        return False
    if path.name in {"core_index.yml", "personality_index.yml"}:
        return False
    return volume_number(path) is not None


def relative(path: Path) -> str:
    return path.relative_to(REPOSITORY_ROOT).as_posix()


def load_items(paths: list[Path]) -> tuple[list[Item], list[str], list[str]]:
    items: list[Item] = []
    missing_ids: list[str] = []
    read_errors: list[str] = []

    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            read_errors.append(f"{relative(path)}: {exc}")
            continue

        id_line = ID_LINE_PATTERN.search(text)
        if id_line is None:
            missing_ids.append(relative(path))
            continue

        item_id = id_line.group("id").strip()
        if len(item_id) >= 2 and item_id[0] == item_id[-1] and item_id[0] in {'"', "'"}:
            item_id = item_id[1:-1].strip()
        match = ID_PATTERN.fullmatch(item_id)
        volume = volume_number(path)
        assert volume is not None
        items.append(
            Item(
                path=path,
                item_id=item_id,
                prefix=match.group("prefix") if match else None,
                volume=volume,
            )
        )

    return items, missing_ids, read_errors


def print_list(title: str, values: list[str], empty_message: str = "None") -> None:
    print(f"\n--- {title} ({len(values)}) ---")
    if not values:
        print(empty_message)
        return
    for value in values:
        print(f"- {value}")


def main() -> None:
    all_item_paths = sorted(path for path in DATA_ROOT.rglob("*.yml") if is_item_file(path))
    target_paths = [
        path
        for path in all_item_paths
        if (number := volume_number(path)) is not None and 1 <= number <= AUDIT_MAX_VOLUME
    ]
    external_paths = [
        path
        for path in all_item_paths
        if (number := volume_number(path)) is not None and number > AUDIT_MAX_VOLUME
    ]

    items, missing_ids, read_errors = load_items(target_paths)
    external_items, _, external_read_errors = load_items(external_paths)
    read_errors.extend(external_read_errors)

    valid_items = [item for item in items if item.prefix is not None]
    invalid_items = [item for item in items if item.prefix is None]
    prefix_counts = Counter(item.prefix for item in valid_items)
    prefix_directories: dict[str, set[str]] = defaultdict(set)
    prefix_volumes: dict[str, set[str]] = defaultdict(set)
    ids: dict[str, list[Path]] = defaultdict(list)

    for item in items:
        ids[item.item_id].append(item.path)
        if item.prefix is not None:
            prefix_directories[item.prefix].add(relative(item.path.parent))
            prefix_volumes[item.prefix].add(item.path.relative_to(DATA_ROOT).parts[0])

    print(f"=== ID Prefix Audit (Vol1-Vol{AUDIT_MAX_VOLUME}, report only) ===")
    print(f"Item files: {len(target_paths)}")
    print(f"Loaded IDs: {len(items)}")
    print(f"Prefixes in use: {len(prefix_counts)}")
    print(f"Read errors: {len(read_errors)}")
    print(f"Missing IDs: {len(missing_ids)}")
    print(f"Invalid ID format: {len(invalid_items)}")

    print("\n--- Approved Prefixes ---")
    for prefix, domain in APPROVED_PREFIXES.items():
        reservation = f"; reserved for {RESERVED_PREFIXES[prefix]}" if prefix in RESERVED_PREFIXES else ""
        print(f"- {prefix}: {domain}{reservation}")

    print("\n--- Prefix Usage ---")
    for prefix in sorted(prefix_counts):
        print(f"\nPrefix: {prefix}")
        print(f"Count: {prefix_counts[prefix]}")
        print("Volumes:")
        for volume in sorted(prefix_volumes[prefix]):
            print(f"- data/{volume}")
        print("Directories:")
        for directory in sorted(prefix_directories[prefix]):
            print(f"- {directory}")

    unregistered = [
        f"{prefix}: {prefix_counts[prefix]} item(s) in {', '.join(sorted(prefix_volumes[prefix]))}"
        for prefix in sorted(prefix_counts)
        if prefix not in APPROVED_PREFIXES
    ]
    print_list("Unregistered / Unexpected Prefixes", unregistered)

    format_errors = [f"{item.item_id!r}: {relative(item.path)}" for item in invalid_items]
    print_list("Invalid ID Format or Prefix-less IDs", format_errors)
    print_list("Missing IDs", missing_ids)
    print_list("Read Errors", read_errors)

    wrong_volume_groups: Counter[tuple[int, str, str]] = Counter()
    wrong_volume_examples: dict[tuple[int, str, str], Path] = {}
    for item in valid_items:
        expected = EXPECTED_PREFIX_BY_VOLUME.get(item.volume)
        if expected is not None and item.prefix != expected:
            key = (item.volume, item.prefix, expected)
            wrong_volume_groups[key] += 1
            wrong_volume_examples.setdefault(key, item.path)

    wrong_volumes = [
        (
            f"vol{volume}: actual={actual}, expected={expected}, "
            f"count={count}, example={relative(wrong_volume_examples[(volume, actual, expected)])}"
        )
        for (volume, actual, expected), count in sorted(wrong_volume_groups.items())
    ]
    print_list("Prefix / Volume Mismatches", wrong_volumes)

    multi_volume = [
        f"{prefix}: {', '.join(sorted(volumes))}"
        for prefix, volumes in sorted(prefix_volumes.items())
        if len(volumes) > 1
    ]
    print_list("Prefixes Used in Multiple Volumes", multi_volume)

    reserved_items = [
        item
        for item in valid_items
        if item.prefix in RESERVED_PREFIXES
        and EXPECTED_PREFIX_BY_VOLUME.get(item.volume) != item.prefix
    ]
    reserved_groups: Counter[tuple[str, str]] = Counter(
        (item.prefix, item.path.relative_to(DATA_ROOT).parts[0]) for item in reserved_items
    )
    reserved_collisions = [
        f"{prefix} is reserved for {RESERVED_PREFIXES[prefix]} but has {count} item(s) in {volume}"
        for (prefix, volume), count in sorted(reserved_groups.items())
    ]
    print_list("Reserved Future Prefix Collisions", reserved_collisions)

    emo_violations = [
        f"{item.item_id}: {relative(item.path)}"
        for item in reserved_items
        if item.prefix == "EMO" and item.volume == 2
    ]
    print_list("EMO Prefix Violations in Vol2 Personality", emo_violations)

    duplicate_ids = [
        f"{item_id}: {', '.join(relative(path) for path in paths)}"
        for item_id, paths in sorted(ids.items())
        if len(paths) > 1
    ]
    print_list(f"Duplicate IDs Within Vol1-Vol{AUDIT_MAX_VOLUME}", duplicate_ids)

    external_ids: dict[str, list[Path]] = defaultdict(list)
    for item in external_items:
        external_ids[item.item_id].append(item.path)
    external_collisions = [
        f"{item_id}: target={', '.join(relative(path) for path in target_paths_for_id)}; "
        f"later={', '.join(relative(path) for path in external_ids[item_id])}"
        for item_id, target_paths_for_id in sorted(ids.items())
        if item_id in external_ids
    ]
    print_list(f"ID Collisions with Vol{AUDIT_MAX_VOLUME + 1}+", external_collisions)

    issue_count = (
        len(read_errors)
        + len(missing_ids)
        + len(invalid_items)
        + len(unregistered)
        + sum(wrong_volume_groups.values())
        + len(multi_volume)
        + len(reserved_items)
        + len(duplicate_ids)
        + len(external_collisions)
    )
    print("\n=== Audit Summary ===")
    print(f"Findings: {issue_count}")
    print("Mode: report only (no files were modified)")


if __name__ == "__main__":
    main()
