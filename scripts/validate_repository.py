from pathlib import Path
import subprocess
import sys

ROOT = Path(".")

REQUIRED_DIRS = [
    "analysis_engine",
    "data",
    "data/master_packs",
    "scripts",
    "tests",
]

REQUIRED_SCRIPTS = [
    "scripts/generate_from_master.py",
    "scripts/audit_all_data.py",
    "scripts/audit_runtime_safety.py",
    "scripts/audit_runtime_contract.py",
    "scripts/run_all_audits.py",
    "scripts/run_quality_checks.py",
]

REQUIRED_RUNTIME_FILES = [
    "analysis_engine/__init__.py",
    "analysis_engine/__main__.py",
    "analysis_engine/bundles.py",
    "analysis_engine/contracts.py",
    "analysis_engine/guidance.py",
    "analysis_engine/library.py",
    "analysis_engine/matching.py",
    "analysis_engine/pipeline.py",
    "analysis_engine/safety.py",
    "tests/test_knowledge_library.py",
    "tests/test_interpretation_bundles.py",
    "tests/test_application_guidance.py",
    "tests/test_signal_matching.py",
    "tests/test_application_pipeline.py",
    "tests/test_runtime_contract.py",
    "tests/test_safety_contract.py",
    "docs/08_runtime_api_contract_v1.json",
]

def check_paths():
    errors = []

    for d in REQUIRED_DIRS:
        if not Path(d).is_dir():
            errors.append(f"[MISSING DIRECTORY] {d}")

    for s in REQUIRED_SCRIPTS:
        if not Path(s).is_file():
            errors.append(f"[MISSING SCRIPT] {s}")

    for runtime_file in REQUIRED_RUNTIME_FILES:
        if not Path(runtime_file).is_file():
            errors.append(f"[MISSING RUNTIME FILE] {runtime_file}")

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
