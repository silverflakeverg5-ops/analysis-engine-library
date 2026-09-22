"""Application-use guidance assembled from audited catalog materials."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, TYPE_CHECKING

from .bundles import BASELINE_SAFETY_IDS, MaterialLink, MaterialSection, build_interpretation_bundle
from .library import (
    API_VERSION,
    ITEM_ID_PATTERN,
    RUNTIME_VERSION,
    SAFETY_MESSAGE_JA,
    ItemNotFoundError,
    QueryValidationError,
    _public_copy,
)

if TYPE_CHECKING:
    from .library import KnowledgeLibrary


BASELINE_DISPLAY_IDS = (
    "DSP-000001",  # Tendency expression
    "DSP-000002",  # Possibility expression
    "DSP-000003",  # Non-diagnostic expression
    "DSP-000006",  # Contextualized result display
    "DSP-000013",  # Non-evaluative expression
    "DSP-000021",  # Result-reason explanation
    "DSP-000022",  # Used-Signal display
    "DSP-000023",  # Modifier display
    "DSP-000024",  # Evidence display
    "DSP-000025",  # Uncertainty-reason display
    "DSP-000027",  # Data-limitation display
    "DSP-000030",  # User-correction prompt
)
DISPLAY_MAPPING_RULE_IDS = (
    "MAP-000024",  # Safety to display mapping
    "MAP-000025",  # App use case display mapping
)
GUIDANCE_MESSAGE_JA = (
    "表示項目と安全項目は全用途に適用する固定基底です。"
    "現行スキーマには用途別の明示的ID対応がないため、用途固有の表示適合性を"
    "推測していません。各アプリは文脈とリスクを確認して採否を決定してください。"
)


class GuidanceValidationError(QueryValidationError):
    """Raised when an application-guidance request is invalid."""


@dataclass(frozen=True)
class ApplicationGuidanceBundle:
    """Neutral app definition plus baseline display and safety materials."""

    application: Mapping[str, Any]
    application_source: str
    application_modifiers: MaterialSection
    application_evidence: MaterialSection
    display_baseline: tuple[MaterialLink, ...]
    mapping_rules: tuple[MaterialLink, ...]
    safety_constraints: tuple[MaterialLink, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "api_version": API_VERSION,
            "runtime_version": RUNTIME_VERSION,
            "guidance": {
                "application": _public_copy(self.application),
                "application_source": self.application_source,
                "application_modifiers": self.application_modifiers.to_dict(),
                "application_evidence": self.application_evidence.to_dict(),
                "display_baseline": [link.to_dict() for link in self.display_baseline],
                "mapping_rules": [link.to_dict() for link in self.mapping_rules],
                "safety_constraints": [
                    link.to_dict() for link in self.safety_constraints
                ],
                "mapping_status": {
                    "baseline_only": True,
                    "app_specific_mapping_resolved": False,
                    "reason_ja": (
                        "App Use CaseからDisplay Designへの明示的ID参照が"
                        "現行スキーマに存在しないため"
                    ),
                },
            },
            "safety": {
                "materials_only": True,
                "inference_performed": False,
                "scoring_performed": False,
                "ranking_performed": False,
                "display_suitability_assessed": False,
                "message_ja": f"{SAFETY_MESSAGE_JA}{GUIDANCE_MESSAGE_JA}",
            },
        }


def _catalog_links(
    library: "KnowledgeLibrary",
    item_ids: tuple[str, ...],
    *,
    expected_type: str,
    method: str,
) -> tuple[MaterialLink, ...]:
    links: list[MaterialLink] = []
    for item_id in item_ids:
        record = library._records.get(item_id)
        if (
            record is None
            or record.data.get("knowledge_type") != expected_type
            or record.data.get("status") != "active"
        ):
            raise GuidanceValidationError(
                f"Required {expected_type} item is unavailable: {item_id}"
            )
        links.append(
            MaterialLink(
                item=record.data,
                method=method,
                source_value=None,
                matched_field=None,
                matched_value=None,
            )
        )
    return tuple(links)


def build_application_guidance(
    library: "KnowledgeLibrary",
    application_id: str,
) -> ApplicationGuidanceBundle:
    """Collect application, display, mapping, and safety reference materials."""
    if not isinstance(application_id, str) or not ITEM_ID_PATTERN.fullmatch(application_id):
        raise GuidanceValidationError(
            "application_id must use the canonical PREFIX-000000 form"
        )
    record = library._records.get(application_id)
    if record is None:
        raise ItemNotFoundError(f"Knowledge Item not found: {application_id}")
    if record.data.get("knowledge_type") != "app_use_case":
        raise GuidanceValidationError("application_id must identify an App Use Case")
    if record.data.get("status") != "active":
        raise GuidanceValidationError(f"App Use Case is not active: {application_id}")

    materials = build_interpretation_bundle(library, application_id)
    return ApplicationGuidanceBundle(
        application=record.data,
        application_source=record.source_path,
        application_modifiers=materials.modifiers,
        application_evidence=materials.evidence,
        display_baseline=_catalog_links(
            library,
            BASELINE_DISPLAY_IDS,
            expected_type="display_design",
            method="runtime_baseline_policy",
        ),
        mapping_rules=_catalog_links(
            library,
            DISPLAY_MAPPING_RULE_IDS,
            expected_type="mapping_rule",
            method="runtime_contract_reference",
        ),
        safety_constraints=_catalog_links(
            library,
            BASELINE_SAFETY_IDS,
            expected_type="safety_ethics",
            method="runtime_baseline_policy",
        ),
    )
