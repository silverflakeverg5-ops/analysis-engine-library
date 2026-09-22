"""Run the read-only runtime safety contract as a repository quality gate."""

from __future__ import annotations

import json
from pathlib import Path
import sys

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from analysis_engine import KnowledgeLibrary


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    report = KnowledgeLibrary().safety_contract_report()
    print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
    if not report.passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
