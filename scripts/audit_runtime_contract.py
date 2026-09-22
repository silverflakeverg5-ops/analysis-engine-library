"""Run or inspect the versioned runtime API compatibility contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from analysis_engine import KnowledgeLibrary
from analysis_engine.contracts import build_runtime_contract_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit the runtime API response-shape contract.",
    )
    parser.add_argument(
        "--print-current",
        action="store_true",
        help="Print a proposed snapshot for explicit review; do not write files",
    )
    parser.add_argument("--snapshot", help="Optional snapshot JSON path")
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    library = KnowledgeLibrary()
    if args.print_current:
        response = build_runtime_contract_snapshot(library)
        passed = True
    else:
        report = library.runtime_contract_report(args.snapshot)
        response = report.to_dict()
        passed = report.passed
    print(json.dumps(response, ensure_ascii=False, indent=2))
    if not passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
