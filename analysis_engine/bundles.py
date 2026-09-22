"""Build auditable interpretation-material bundles without inference."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Any, Mapping, Sequence, TYPE_CHECKING
import re

from .library import (
    API_VERSION,
    ITEM_ID_PATTERN,
    RUNTIME_VERSION,
    SAFETY_MESSAGE_JA,
    ItemNotFoundError,
    QueryValidationError,
    _public_copy,
)
from .matching import _field_values, _normalize_text

if TYPE_CHECKING:
    from .library import KnowledgeLibrary, _Record


BASELINE_SAFETY_IDS = (
    "SAF-000001",  # Non-diagnostic principle
    "SAF-000006",  # Context-sensitive principle
    "SAF-000007",  # Uncertainty disclosure principle
    "SAF-000008",  # No-ranking principle
    "SAF-000009",  # Human-review principle
    "SAF-000010",  # Knowledge DB boundary principle
)
LINK_FIELDS = ("name_ja", "name_en", "definition_ja")
EVIDENCE_SPLIT_PATTERN = re.compile(r"[・,/、;；]+")
EVIDENCE_SUFFIX_PATTERN = re.compile(
    r"(?:研究|科学|心理学|設計|方法論|測定|評価|倫理|工学|HCI)*(?:を参照|で使用)$"
)
BUNDLE_MESSAGE_JA = (
    "このバンドルは解釈前に確認すべき材料を収集したものです。"
    "リンクは文字列一致または固定された安全基底によるもので、"
    "関連性、根拠強度、適用可能性、結論を保証しません。"
)


class BundleValidationError(QueryValidationError):
    """Raised when an interpretation-bundle request is invalid."""


@dataclass(frozen=True)
class MaterialLink:
    """One catalog material plus the exact reason it was linked."""

    item: Mapping[str, Any]
    method: str
    source_value: str | None
    matched_field: str | None
    matched_value: str | None

    def to_dict(self) -> dict[str, Any]:
        return {
            "item": _public_copy(self.item),
            "link": {
                "method": self.method,
                "source_value": self.source_value,
                "matched_field": self.matched_field,
                "matched_value": self.matched_value,
            },
        }


@dataclass(frozen=True)
class MaterialSection:
    """Raw source values and any exact catalog links derived from them."""

    source_field: str
    source_values: tuple[str, ...]
    links: tuple[MaterialLink, ...]
    unresolved_values: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "source_field": self.source_field,
            "source_values": list(self.source_values),
            "links": [link.to_dict() for link in self.links],
            "unresolved_values": list(self.unresolved_values),
        }


@dataclass(frozen=True)
class InterpretationBundle:
    """Read-only materials for one Knowledge Item; never an interpretation."""

    knowledge: Mapping[str, Any]
    knowledge_source: str
    modifiers: MaterialSection
    evidence: MaterialSection
    safety_constraints: tuple[MaterialLink, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "api_version": API_VERSION,
            "runtime_version": RUNTIME_VERSION,
            "bundle": {
                "knowledge": _public_copy(self.knowledge),
                "knowledge_source": self.knowledge_source,
                "modifiers": self.modifiers.to_dict(),
                "evidence": self.evidence.to_dict(),
                "safety_constraints": [
                    link.to_dict() for link in self.safety_constraints
                ],
            },
            "safety": {
                "materials_only": True,
                "inference_performed": False,
                "scoring_performed": False,
                "ranking_performed": False,
                "evidence_strength_assessed": False,
                "applicability_assessed": False,
                "message_ja": f"{SAFETY_MESSAGE_JA}{BUNDLE_MESSAGE_JA}",
            },
        }


def _unique_strings(values: Sequence[str]) -> tuple[str, ...]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        text = str(value).strip()
        normalized = _normalize_text(text)
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        result.append(text)
    return tuple(result)


def _evidence_terms(value: str) -> tuple[str, ...]:
    terms: list[str] = []
    for part in EVIDENCE_SPLIT_PATTERN.split(value):
        term = EVIDENCE_SUFFIX_PATTERN.sub("", part.strip()).strip()
        if len(_normalize_text(term)) >= 2:
            terms.append(term)
    return _unique_strings(terms)


def _find_text_links(
    library: "KnowledgeLibrary",
    source_values: tuple[str, ...],
    *,
    target_type: str,
) -> tuple[tuple[MaterialLink, ...], tuple[str, ...]]:
    links: list[MaterialLink] = []
    resolved_sources: set[str] = set()
    seen_items: set[str] = set()

    candidates = sorted(
        (
            record
            for record in library._records.values()
            if record.data.get("knowledge_type") == target_type
            and record.data.get("status") == "active"
        ),
        key=lambda record: str(record.data["id"]),
    )
    for source_value in source_values:
        normalized_source = _normalize_text(source_value)
        if len(normalized_source) < 2:
            continue
        for record in candidates:
            matched_field: str | None = None
            matched_value: str | None = None
            for field in LINK_FIELDS:
                for value in _field_values(record.data, field):
                    normalized_value = _normalize_text(value)
                    if normalized_source in normalized_value:
                        matched_field = field
                        matched_value = value
                        break
                if matched_field is not None:
                    break
            if matched_field is None:
                continue
            resolved_sources.add(source_value)
            item_id = str(record.data["id"])
            if item_id in seen_items:
                continue
            seen_items.add(item_id)
            links.append(
                MaterialLink(
                    item=record.data,
                    method="deterministic_text_containment",
                    source_value=source_value,
                    matched_field=matched_field,
                    matched_value=matched_value,
                )
            )

    unresolved = tuple(
        source for source in source_values if source not in resolved_sources
    )
    return tuple(links), unresolved


def _safety_links(library: "KnowledgeLibrary") -> tuple[MaterialLink, ...]:
    links: list[MaterialLink] = []
    for item_id in BASELINE_SAFETY_IDS:
        record = library._records.get(item_id)
        if record is None or record.data.get("knowledge_type") != "safety_ethics":
            raise BundleValidationError(
                f"Required baseline safety item is unavailable: {item_id}"
            )
        links.append(
            MaterialLink(
                item=record.data,
                method="runtime_baseline_policy",
                source_value=None,
                matched_field=None,
                matched_value=None,
            )
        )
    return tuple(links)


def build_interpretation_bundle(
    library: "KnowledgeLibrary",
    knowledge_id: str,
) -> InterpretationBundle:
    """Collect modifier, evidence, and safety materials for one item."""
    if not isinstance(knowledge_id, str) or not ITEM_ID_PATTERN.fullmatch(knowledge_id):
        raise BundleValidationError("knowledge_id must use the canonical PREFIX-000000 form")
    record = library._records.get(knowledge_id)
    if record is None:
        raise ItemNotFoundError(f"Knowledge Item not found: {knowledge_id}")
    if record.data.get("status") != "active":
        raise BundleValidationError(f"Knowledge Item is not active: {knowledge_id}")
    if record.data.get("knowledge_type") in {
        "modifier",
        "evidence_source",
        "safety_ethics",
    }:
        raise BundleValidationError(
            "interpretation bundles require a primary Knowledge Item, not a material item"
        )

    modifier_values = _unique_strings(_field_values(record.data, "modifiers"))
    modifier_links, unresolved_modifiers = _find_text_links(
        library,
        modifier_values,
        target_type="modifier",
    )
    evidence_source_values = _unique_strings(_field_values(record.data, "evidence"))
    evidence_terms = _unique_strings(
        [term for value in evidence_source_values for term in _evidence_terms(value)]
    )
    evidence_links, unresolved_evidence = _find_text_links(
        library,
        evidence_terms,
        target_type="evidence_source",
    )

    return InterpretationBundle(
        knowledge=record.data,
        knowledge_source=record.source_path,
        modifiers=MaterialSection(
            source_field="modifiers",
            source_values=modifier_values,
            links=modifier_links,
            unresolved_values=unresolved_modifiers,
        ),
        evidence=MaterialSection(
            source_field="evidence",
            source_values=evidence_source_values,
            links=evidence_links,
            unresolved_values=unresolved_evidence,
        ),
        safety_constraints=_safety_links(library),
    )
