import subprocess
import sys
from pathlib import Path

SCRIPTS = [
    "scripts/run_all_audits.py",
    "scripts/library_stats.py",
]

def run(script):
    print(f"\n{'=' * 70}")
    print(f"Running: {script}")
    print(f"{'=' * 70}")

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"\nFAILED: {script}")
        return False

    return True


def main():
    failed = []

    for script in SCRIPTS:
        if not Path(script).exists():
            print(f"Missing: {script}")
            failed.append(script)
            continue

        if not run(script):
            failed.append(script)

    print("\n")
    print("=" * 70)
    print("QUALITY CHECK SUMMARY")
    print("=" * 70)

    print(f"Scripts : {len(SCRIPTS)}")
    print(f"Failed  : {len(failed)}")

    if failed:
        print("\nFailed Scripts")
        for script in failed:
            print(f" - {script}")
        sys.exit(1)

    print("\nAll quality checks passed.")


if __name__ == "__main__":
    main()