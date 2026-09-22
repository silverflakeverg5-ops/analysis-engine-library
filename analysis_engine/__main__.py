"""Command-line inspection interface for the read-only Knowledge Library."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .library import KnowledgeLibrary


def _stroke_sequence(value: str) -> list[int]:
    try:
        strokes = [int(entry.strip()) for entry in value.split(",")]
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "stroke counts must be comma-separated integers"
        ) from exc
    if not strokes or any(stroke < 1 for stroke in strokes):
        raise argparse.ArgumentTypeError("stroke counts must be positive integers")
    return strokes


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Search the read-only Analysis Engine Knowledge Library.",
    )
    parser.add_argument("--id", dest="item_id", help="Return one exact Knowledge Item ID")
    parser.add_argument("--query", help="Case-insensitive text search")
    parser.add_argument("--category", help="Exact category filter")
    parser.add_argument("--knowledge-type", help="Exact knowledge_type filter")
    parser.add_argument("--tag", action="append", default=[], help="Required exact tag; repeatable")
    parser.add_argument("--status", default="active", help="Exact status filter; default: active")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--sort", choices=("id", "name_ja", "name_en"), default="id")
    parser.add_argument(
        "--match-signal",
        action="append",
        default=[],
        help="Observation Signal ID or free-text Signal; repeatable",
    )
    parser.add_argument("--match-mode", choices=("any", "all"), default="any")
    parser.add_argument(
        "--target-knowledge-type",
        action="append",
        default=[],
        help="Limit Signal matches to a knowledge_type; repeatable",
    )
    parser.add_argument(
        "--include-operational",
        action="store_true",
        help="Include API, audit, Observation Signal, and other operational items",
    )
    parser.add_argument(
        "--bundle-id",
        help="Return modifier, evidence, and safety materials for one Knowledge Item ID",
    )
    parser.add_argument(
        "--pipeline-signal",
        action="append",
        default=[],
        help="Match a Signal and return candidate material bundles; repeatable",
    )
    parser.add_argument(
        "--app-use-case-id",
        help="Attach one App Use Case guidance bundle to a Signal pipeline",
    )
    parser.add_argument(
        "--app-guidance-id",
        help="Return display and safety guidance for one App Use Case ID",
    )
    parser.add_argument(
        "--safety-audit",
        action="store_true",
        help="Run the executable runtime safety-contract audit",
    )
    parser.add_argument(
        "--contract-audit",
        action="store_true",
        help="Compare public response shapes with the reviewed API snapshot",
    )
    parser.add_argument(
        "--divination-registry",
        action="store_true",
        help="Return supported divination traditions and required inputs",
    )
    parser.add_argument(
        "--numerology-birth-date",
        help="Calculate numerology values from a YYYY-MM-DD birth date",
    )
    parser.add_argument(
        "--numerology-name",
        help="Optional Latin-script name for Pythagorean name calculations",
    )
    parser.add_argument(
        "--numerology-target-year",
        type=int,
        help="Optional year for a personal-year calculation",
    )
    parser.add_argument(
        "--reduce-master-numbers",
        action="store_true",
        help="Reduce 11, 22, and 33 instead of preserving them",
    )
    parser.add_argument("--japanese-surname", help="Japanese family name")
    parser.add_argument("--japanese-given-name", help="Japanese given name")
    parser.add_argument(
        "--japanese-surname-strokes",
        type=_stroke_sequence,
        help="Comma-separated declared stroke counts for the family name",
    )
    parser.add_argument(
        "--japanese-given-strokes",
        type=_stroke_sequence,
        help="Comma-separated declared stroke counts for the given name",
    )
    parser.add_argument(
        "--stroke-dictionary",
        help="Declared glyph dictionary or stroke-count source",
    )
    parser.add_argument(
        "--stroke-dictionary-file",
        help="Optional UTF-8 JSON object mapping exact characters to stroke counts",
    )
    parser.add_argument(
        "--single-character-adjustment",
        choices=("virtual_one", "none"),
        default="virtual_one",
        help="Treatment of one-character family or given names",
    )
    parser.add_argument("--metadata", action="store_true", help="Return catalog metadata")
    return parser


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = build_parser()
    args = parser.parse_args()
    library = KnowledgeLibrary()
    if args.metadata:
        response = library.metadata()
    elif args.divination_registry:
        response = library.divination_registry().to_dict()
    elif args.numerology_birth_date:
        response = library.calculate_numerology(
            args.numerology_birth_date,
            name=args.numerology_name,
            target_year=args.numerology_target_year,
            preserve_master_numbers=not args.reduce_master_numbers,
        ).to_dict()
    elif args.japanese_surname is not None or args.japanese_given_name is not None:
        required = {
            "--japanese-surname": args.japanese_surname,
            "--japanese-given-name": args.japanese_given_name,
            "--stroke-dictionary": args.stroke_dictionary,
        }
        if args.stroke_dictionary_file is None:
            required.update(
                {
                    "--japanese-surname-strokes": args.japanese_surname_strokes,
                    "--japanese-given-strokes": args.japanese_given_strokes,
                }
            )
        missing = [flag for flag, value in required.items() if value is None]
        if missing:
            parser.error("Japanese name calculation also requires: " + ", ".join(missing))
        if args.stroke_dictionary_file is not None:
            dictionary_path = Path(args.stroke_dictionary_file)
            try:
                if dictionary_path.stat().st_size > 5_000_000:
                    parser.error("stroke dictionary file cannot exceed 5 MB")
                stroke_dictionary = json.loads(
                    dictionary_path.read_text(encoding="utf-8")
                )
            except (OSError, json.JSONDecodeError) as exc:
                parser.error(f"cannot read stroke dictionary JSON: {exc}")
            if not isinstance(stroke_dictionary, dict):
                parser.error("stroke dictionary JSON root must be an object")
            response = library.calculate_japanese_name_from_dictionary(
                args.japanese_surname,
                args.japanese_given_name,
                stroke_dictionary=stroke_dictionary,
                stroke_dictionary_id=args.stroke_dictionary,
                single_character_adjustment=args.single_character_adjustment,
            ).to_dict()
        else:
            response = library.calculate_japanese_name(
                args.japanese_surname,
                args.japanese_given_name,
                surname_strokes=args.japanese_surname_strokes,
                given_strokes=args.japanese_given_strokes,
                stroke_dictionary=args.stroke_dictionary,
                single_character_adjustment=args.single_character_adjustment,
            ).to_dict()
    elif args.safety_audit:
        response = library.safety_contract_report().to_dict()
    elif args.contract_audit:
        response = library.runtime_contract_report().to_dict()
    elif args.app_guidance_id:
        response = library.application_guidance(args.app_guidance_id).to_dict()
    elif args.pipeline_signal:
        response = library.application_pipeline(
            args.pipeline_signal,
            mode=args.match_mode,
            target_knowledge_types=args.target_knowledge_type,
            status=args.status,
            offset=args.offset,
            limit=args.limit if args.limit is not None else 10,
            application_id=args.app_use_case_id,
        ).to_dict()
    elif args.bundle_id:
        response = library.interpretation_bundle(args.bundle_id).to_dict()
    elif args.item_id:
        response = {
            "api_version": "1.0",
            "item": library.require(args.item_id),
            "safety": {
                "inference_performed": False,
                "scoring_performed": False,
            },
        }
    elif args.match_signal:
        response = library.match_signals(
            args.match_signal,
            mode=args.match_mode,
            target_knowledge_types=args.target_knowledge_type,
            include_operational=args.include_operational,
            status=args.status,
            offset=args.offset,
            limit=args.limit if args.limit is not None else 20,
        ).to_dict()
    else:
        response = library.search(
            args.query,
            category=args.category,
            knowledge_type=args.knowledge_type,
            tags=args.tag,
            status=args.status,
            offset=args.offset,
            limit=args.limit if args.limit is not None else 20,
            sort=args.sort,
        ).to_dict()
    print(json.dumps(response, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
