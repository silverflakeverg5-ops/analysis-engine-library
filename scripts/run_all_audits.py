import subprocess
import sys
from pathlib import Path

AUDIT_SCRIPTS = [
    "scripts/audit_all_data.py",
    "scripts/audit_required_fields.py",
    "scripts/audit_id_filename.py",
    "scripts/audit_index_references.py",
    "scripts/audit_orphan_items.py",
    "scripts/audit_tag_consistency.py",
    "scripts/audit_status_values.py",
]

def main():
    failed = []

    print("=== Run All Audits ===")

    for script in AUDIT_SCRIPTS:
        path = Path(script)

        if not path.exists():
            print(f"\n[SKIP] Missing: {script}")
            failed.append(script)
            continue

        print(f"\n--- Running: {script} ---")
        result = subprocess.run([sys.executable, script])

        if result.returncode != 0:
            failed.append(script)

    print("\n=== Audit Summary ===")
    print(f"Audit scripts: {len(AUDIT_SCRIPTS)}")
    print(f"Failed: {len(failed)}")

    if failed:
        print("\n--- Failed Scripts ---")
        for script in failed:
            print(script)
        sys.exit(1)

    print("\nOK: All audits completed.")

if __name__ == "__main__":
    main()