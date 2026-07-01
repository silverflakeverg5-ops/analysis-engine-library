from pathlib import Path
import subprocess
import sys

ROOT = Path(".")

REQUIRED_DIRS = [
    "data",
    "data/master_packs",
    "scripts",
]

REQUIRED_SCRIPTS = [
    "scripts/generate_from_master.py",
    "scripts/audit_all_data.py",
    "scripts/run_all_audits.py",
    "scripts/run_quality_checks.py",
]

def check_paths():
    errors = []

    for d in REQUIRED_DIRS:
        if not Path(d).is_dir():
            errors.append(f"[MISSING DIRECTORY] {d}")

    for s in REQUIRED_SCRIPTS:
        if not Path(s).is_file():
            errors.append(f"[MISSING SCRIPT] {s}")

    return errors


def git_status():
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.stdout.strip().splitlines()
    except Exception:
        return ["Git not available"]


def main():
    print("=== Repository Validation ===")

    errors = check_paths()

    print(f"Directory / Script Errors : {len(errors)}")

    if errors:
        print("\n--- Missing ---")
        for e in errors:
            print(e)

    git_changes = git_status()

    print(f"\nGit Pending Changes : {len(git_changes)}")

    if git_changes:
        print("\n--- Git Status ---")
        for line in git_changes:
            print(line)

    if not errors and not git_changes:
        print("\nRepository is clean.")

    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()