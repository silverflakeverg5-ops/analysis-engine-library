"""Executable safety-contract audit for every public runtime response."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Mapping, TYPE_CHECKING

from .bundles import BASELINE_SAFETY_IDS
from .guidance import BASELINE_DISPLAY_IDS, DISPLAY_MAPPING_RULE_IDS
from .library import API_VERSION, RUNTIME_VERSION, SAFETY_MESSAGE_JA

if TYPE_CHECKING:
    from .library import KnowledgeLibrary


SAFETY_AUDIT_MESSAGE_JA = (
    "この監査は公開レスポンスの安全契約と固定基底を検証するもので、"
    "人物データの分析や表示内容の適合性評価は行いません。"
)


@dataclass(frozen=True)
class SafetyContractCheck:
    """One deterministic runtime safety-contract check."""

    name: str
    passed: bool
    detail: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "passed": self.passed,
            "detail": self.detail,
        }


@dataclass(frozen=True)
class SafetyContractReport:
    """Aggregate result of the executable runtime safety review."""

    checks: tuple[SafetyContractCheck, ...]

    @property
    def passed(self) -> bool:
        return all(check.passed for check in self.checks)

    @property
    def failed(self) -> int:
        return sum(not check.passed for check in self.checks)

    def to_dict(self) -> dict[str, Any]:
        return {
            "api_version": API_VERSION,
            "runtime_version": RUNTIME_VERSION,
            "audit": {
                "name": "runtime_safety_contract",
                "passed": self.passed,
                "total_checks": len(self.checks),
                "passed_checks": len(self.checks) - self.failed,
                "failed_checks": self.failed,
                "checks": [check.to_dict() for check in self.checks],
            },
            "safety": {
                "audit_only": True,
                "inference_performed": False,
                "scoring_performed": False,
                "ranking_performed": False,
                "display_suitability_assessed": False,
                "message_ja": f"{SAFETY_MESSAGE_JA}{SAFETY_AUDIT_MESSAGE_JA}",
            },
        }


def _false_flags(safety: Mapping[str, Any], *names: str) -> bool:
    return all(safety.get(name) is False for name in names)


def _run_check(
    checks: list[SafetyContractCheck],
    name: str,
    operation: Callable[[], tuple[bool, str]],
) -> None:
    try:
        passed, detail = operation()
    except Exception as exc:  # The audit must report failures instead of aborting.
        checks.append(
            SafetyContractCheck(
                name=name,
                passed=False,
                detail=f"{type(exc).__name__}: {exc}",
            )
        )
        return
    checks.append(SafetyContractCheck(name=name, passed=passed, detail=detail))


def run_safety_contract_audit(
    library: "KnowledgeLibrary",
) -> SafetyContractReport:
    """Exercise representative public responses and verify safety invariants."""
    checks: list[SafetyContractCheck] = []

    def metadata_check() -> tuple[bool, str]:
        response = library.metadata()
        passed = (
            response.get("read_only") is True
            and response.get("inference_performed") is False
            and response.get("scoring_performed") is False
        )
        return passed, "read-only and non-inference metadata boundary"

    def search_check() -> tuple[bool, str]:
        response = library.search("判断潜時", limit=1).to_dict()
        passed = _false_flags(
            response["safety"], "inference_performed", "scoring_performed"
        )
        return passed, "search response disables inference and scoring"

    def matching_check() -> tuple[bool, str]:
        response = library.match_signals(
            ["OBS-000014"],
            target_knowledge_types=["decision_strategy"],
            limit=1,
        ).to_dict()
        ids = [match["item"]["id"] for match in response["matches"]]
        passed = (
            response["safety"].get("mapping_only") is True
            and _false_flags(
                response["safety"],
                "inference_performed",
                "scoring_performed",
                "ranking_performed",
            )
            and ids == ["DEC-000091"]
            and bool(response["matches"][0]["evidence"])
        )
        return passed, "Signal matching is evidence-bearing mapping only"

    def bundle_check() -> tuple[bool, str]:
        response = library.interpretation_bundle("DEC-000091").to_dict()
        safety_ids = tuple(
            entry["item"]["id"]
            for entry in response["bundle"]["safety_constraints"]
        )
        passed = (
            response["bundle"]["knowledge"]["id"] == "DEC-000091"
            and safety_ids == BASELINE_SAFETY_IDS
            and response["safety"].get("materials_only") is True
            and _false_flags(
                response["safety"],
                "inference_performed",
                "scoring_performed",
                "ranking_performed",
                "evidence_strength_assessed",
                "applicability_assessed",
            )
        )
        return passed, "interpretation bundle preserves the fixed safety baseline"

    def guidance_check() -> tuple[bool, str]:
        response = library.application_guidance("APP-000001").to_dict()
        guidance = response["guidance"]
        display_ids = tuple(
            entry["item"]["id"] for entry in guidance["display_baseline"]
        )
        mapping_ids = tuple(
            entry["item"]["id"] for entry in guidance["mapping_rules"]
        )
        safety_ids = tuple(
            entry["item"]["id"] for entry in guidance["safety_constraints"]
        )
        mapping_status = guidance["mapping_status"]
        passed = (
            guidance["application"]["id"] == "APP-000001"
            and display_ids == BASELINE_DISPLAY_IDS
            and mapping_ids == DISPLAY_MAPPING_RULE_IDS
            and safety_ids == BASELINE_SAFETY_IDS
            and mapping_status.get("baseline_only") is True
            and mapping_status.get("app_specific_mapping_resolved") is False
            and _false_flags(
                response["safety"],
                "inference_performed",
                "scoring_performed",
                "ranking_performed",
                "display_suitability_assessed",
            )
        )
        return passed, "application guidance exposes baseline-only limitations"

    def pipeline_check() -> tuple[bool, str]:
        response = library.application_pipeline(
            ["OBS-000014"],
            target_knowledge_types=["decision_strategy"],
            application_id="APP-000001",
            limit=1,
        ).to_dict()
        candidate = response["candidates"][0]
        passed = (
            response["pipeline"]["application_id"] == "APP-000001"
            and candidate["match"]["knowledge_id"]
            == candidate["interpretation_materials"]["knowledge"]["id"]
            == "DEC-000091"
            and response["application_guidance"]["application"]["id"]
            == "APP-000001"
            and response["safety"].get("mapping_only") is True
            and response["safety"].get("materials_only") is True
            and _false_flags(
                response["safety"],
                "inference_performed",
                "scoring_performed",
                "ranking_performed",
                "evidence_strength_assessed",
                "applicability_assessed",
                "display_suitability_assessed",
            )
        )
        return passed, "pipeline keeps match, materials, and app context aligned"

    def divination_registry_check() -> tuple[bool, str]:
        response = library.divination_registry().to_dict()
        registry = response["registry"]
        safety = response["safety"]
        passed = (
            registry["tradition_count"] == 10
            and registry["total_items"] == 1000
            and all(
                entry["evidence_class"]
                == "traditional_cultural_interpretation"
                for entry in registry["traditions"]
            )
            and safety.get("reference_only") is True
            and safety.get("cultural_interpretation_only") is True
            and _false_flags(
                safety,
                "inference_performed",
                "scoring_performed",
                "ranking_performed",
                "diagnosis_performed",
                "prediction_performed",
            )
        )
        return passed, "divination registry remains cultural reference only"

    def numerology_calculation_check() -> tuple[bool, str]:
        response = library.calculate_numerology(
            "1990-01-01",
            name="Jane Doe",
            target_year=2026,
        ).to_dict()
        calculation = response["calculation"]
        safety = response["safety"]
        passed = (
            calculation["knowledge_type"] == "numerology"
            and calculation["input_summary"]["raw_inputs_returned"] is False
            and calculation["input_summary"]["inputs_stored"] is False
            and calculation["results"]["life_path"]["value"] == 3
            and safety.get("calculation_only") is True
            and safety.get("mathematical_validity_implies_symbolic_validity") is False
            and _false_flags(
                safety,
                "interpretation_performed",
                "inference_performed",
                "scoring_performed",
                "ranking_performed",
                "diagnosis_performed",
                "prediction_performed",
            )
        )
        return passed, "numerology returns traceable arithmetic without interpretation"

    def japanese_name_calculation_check() -> tuple[bool, str]:
        response = library.calculate_japanese_name_from_dictionary(
            "山田",
            "太郎",
            stroke_dictionary={"山": 3, "田": 5, "太": 4, "郎": 9},
            stroke_dictionary_id="modern_glyph_declared_v1",
        ).to_dict()
        calculation = response["calculation"]
        safety = response["safety"]
        passed = (
            calculation["knowledge_type"] == "name_divination"
            and calculation["stroke_resolution"] == "dictionary_lookup"
            and calculation["input_summary"]["raw_names_returned"] is False
            and calculation["input_summary"]["names_stored"] is False
            and calculation["grids"]["total"]["value"] == 21
            and safety.get("calculation_only") is True
            and safety.get("name_quality_assessed") is False
            and _false_flags(
                safety,
                "interpretation_performed",
                "inference_performed",
                "scoring_performed",
                "ranking_performed",
                "diagnosis_performed",
                "prediction_performed",
            )
        )
        return passed, "Japanese name grids preserve provenance without judgment"

    for name, operation in (
        ("metadata_boundary", metadata_check),
        ("search_boundary", search_check),
        ("signal_matching_boundary", matching_check),
        ("interpretation_bundle_boundary", bundle_check),
        ("application_guidance_boundary", guidance_check),
        ("application_pipeline_boundary", pipeline_check),
        ("divination_registry_boundary", divination_registry_check),
        ("numerology_calculation_boundary", numerology_calculation_check),
        ("japanese_name_calculation_boundary", japanese_name_calculation_check),
    ):
        _run_check(checks, name, operation)

    return SafetyContractReport(checks=tuple(checks))
