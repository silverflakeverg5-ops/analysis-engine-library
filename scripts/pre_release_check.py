from pathlib import Path
import subprocess
import sys

CHECK_COMMANDS = [
    ["python", "scripts/run_quality_checks.py"],
    ["python", "scripts/validate_repository.py"],
]

def run_command(command):
    print("\n" + "=" * 70)
    print("Running:", " ".join(command))
    print("=" * 70)

    result = subprocess.run(command)

    return result.returncode == 0


def git_clean():
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True,
    )

    return result.stdout.strip() == ""


def main():
    failed = []

    for command in CHECK_COMMANDS:
        if not run_command(command):
            failed.append(" ".join(command))

    print("\n" + "=" * 70)
    print("Git Status")
    print("=" * 70)

    if git_clean():
        print("Working tree clean")
    else:
        print("Working tree is NOT clean")
        failed.append("git status")

    print("\n" + "=" * 70)
    print("PRE RELEASE SUMMARY")
    print("=" * 70)

    print(f"Checks : {len(CHECK_COMMANDS)+1}")
    print(f"Failed : {len(failed)}")

    if failed:
        print("\nFailed")
        for f in failed:
            print("-", f)
        sys.exit(1)

    print("\nRepository is ready for release.")

if __name__ == "__main__":
    main()