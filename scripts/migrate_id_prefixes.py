"""Migrate legacy Knowledge Item prefixes to the project-guide prefixes.

The command is a dry-run by default. Pass ``--apply`` only after reviewing the
reported file and reference counts. The migration changes ID prefixes without
changing their six-digit numbers or Knowledge Item contents.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = REPOSITORY_ROOT / "data"
THIS_FILE = Path(__file__).resolve()
TEXT_SUFFIXES = {".json", ".md", ".py", ".yaml", ".yml"}


@dataclass(frozen=True)
class Migration:
    volume: int
    old_prefix: str
    new_prefix: str


MIGRATIONS = (
    Migration(4, "BIAS", "COG"),
    Migration(5, "COGSCI", "CSC"),
    Migration(6, "NEURO", "NEU"),
    Migration(8, "PHYS", "PHY"),
    Migration(9, "SOCPSY", "SOC"),
    Migration(10, "LEARN", "LEA"),
    Migration(11, "SIGNAL", "OBS"),
    Migration(13, "EVID", "EVD"),
    Migration(15, "DISPLAY", "DSP"),
    Migration(16, "SAFE", "SAF"),
    Migration(17, "GOV", "LIB"),
    Migration(18, "ROAD", "RDM"),
    Migration(21, "TEST", "TST"),
)


def read_exact(path: Path) -> str:
    with path.open("r", encoding="utf-8", newline="") as stream:
        return stream.read()


def write_exact(path: Path, content: str) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        stream.write(content)


def text_files() -> list[Path]:
    files: list[Path] = []
    for path in REPOSITORY_ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if path.resolve() == THIS_FILE or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        files.append(path)
    return sorted(files)


def volume_directory(volume: int) -> Path:
    matches = sorted(path for path in DATA_ROOT.glob(f"vol{volume}_*") if path.is_dir())
    if len(matches) != 1:
        names = ", ".join(str(path) for path in matches) or "none"
        raise RuntimeError(f"Expected one directory for vol{volume}, found: {names}")
    return matches[0]


def planned_renames(migration: Migration) -> list[tuple[Path, Path]]:
    directory = volume_directory(migration.volume)
    renames: list[tuple[Path, Path]] = []
    old_start = f"{migration.old_prefix}-"
    new_start = f"{migration.new_prefix}-"
    for source in sorted(directory.rglob(f"{migration.old_prefix}-*")):
        if not source.is_file() or not source.name.startswith(old_start):
            continue
        destination = source.with_name(new_start + source.name[len(old_start) :])
        if destination.exists():
            raise RuntimeError(f"Rename target already exists: {destination}")
        renames.append((source, destination))
    return renames


def relative(path: Path) -> str:
    return path.relative_to(REPOSITORY_ROOT).as_posix()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply the reported prefix replacements and file renames.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    files = text_files()
    replacements: dict[Path, str] = {}
    renames: list[tuple[Path, Path]] = []

    print("=== Canonical ID Prefix Migration ===")
    print(f"Mode: {'apply' if args.apply else 'dry-run'}")

    for migration in MIGRATIONS:
        old_token = f"{migration.old_prefix}-"
        new_token = f"{migration.new_prefix}-"
        changed_files = 0
        occurrences = 0

        for path in files:
            current = replacements.get(path)
            if current is None:
                current = read_exact(path)
            count = current.count(old_token)
            if count:
                replacements[path] = current.replace(old_token, new_token)
                changed_files += 1
                occurrences += count

        migration_renames = planned_renames(migration)
        renames.extend(migration_renames)
        print(
            f"- vol{migration.volume}: {migration.old_prefix} -> {migration.new_prefix}; "
            f"text_files={changed_files}, references={occurrences}, renames={len(migration_renames)}"
        )

    destinations = [destination for _, destination in renames]
    if len(destinations) != len(set(destinations)):
        raise RuntimeError("Multiple source files resolve to the same rename target")

    print("\n--- Summary ---")
    print(f"Text files: {len(replacements)}")
    print(f"File renames: {len(renames)}")

    if not args.apply:
        print("No files changed. Re-run with --apply after reviewing this report.")
        return

    for path, content in replacements.items():
        write_exact(path, content)
    for source, destination in renames:
        source.rename(destination)

    print("Migration applied.")
    if renames:
        print("\n--- Renamed Items ---")
        for source, destination in renames:
            print(f"- {relative(source)} -> {relative(destination)}")


if __name__ == "__main__":
    main()
