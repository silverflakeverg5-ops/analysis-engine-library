import subprocess
import sys

CHECKS = [
    ("all data audits", [sys.executable, "scripts/run_all_audits.py"]),
    ("library statistics", [sys.executable, "scripts/library_stats.py"]),
    (
        "runtime safety contract",
        [sys.executable, "-B", "scripts/audit_runtime_safety.py"],
    ),
    (
        "runtime API compatibility contract",
        [sys.executable, "-B", "scripts/audit_runtime_contract.py"],
    ),
    (
        "read-only runtime tests",
        [sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-v"],
    ),
]


def run(label, command):
    print(f"\n{'=' * 70}")
    print(f"Running: {label}")
    print(f"{'=' * 70}")

    result = subprocess.run(command)

    if result.returncode != 0:
        print(f"\nFAILED: {label}")
        return False

    return True


def main():
    failed = []

    for label, command in CHECKS:
        if not run(label, command):
            failed.append(label)

    print("\n")
    print("=" * 70)
    print("QUALITY CHECK SUMMARY")
    print("=" * 70)

    print(f"Checks  : {len(CHECKS)}")
    print(f"Failed  : {len(failed)}")

    if failed:
        print("\nFailed Scripts")
        for script in failed:
            print(f" - {script}")
        sys.exit(1)

    print("\nAll quality checks passed.")


if __name__ == "__main__":
    main()
