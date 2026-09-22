"""Read-only registry for culturally framed divination reference catalogs."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, TYPE_CHECKING

from .library import API_VERSION, RUNTIME_VERSION

if TYPE_CHECKING:
    from .library import KnowledgeLibrary


DIVINATION_CATALOGS: tuple[tuple[str, str, str], ...] = (
    ("western_astrology", "AST", "西洋占星術"),
    ("yin_yang_wuxing", "WUX", "陰陽五行"),
    ("four_pillars", "BAZ", "四柱推命"),
    ("indian_astrology", "JYO", "インド占星術"),
    ("zi_wei_dou_shu", "ZWD", "紫微斗数"),
    ("nine_star_ki", "NSK", "九星気学"),
    ("sukuyo", "SUK", "宿曜"),
    ("numerology", "NUM", "数秘術"),
    ("name_divination", "NAM", "姓名判断"),
    ("feng_shui", "FSH", "風水"),
)

DIVINATION_SAFETY_MESSAGE_JA = (
    "占術情報は伝統文化上の象徴的な参照材料です。心理学的な性格分析、"
    "医療・心理診断、能力評価、未来の確定的予測、高影響判断には使用できません。"
)


class DivinationRegistryError(RuntimeError):
    """Raised when a detailed divination catalog violates registry invariants."""


@dataclass(frozen=True)
class DivinationTradition:
    """Stable application-facing metadata for one detailed tradition catalog."""

    knowledge_type: str
    prefix: str
    label_ja: str
    item_count: int
    tradition: str
    source_type: str
    required_inputs: tuple[str, ...]
    calculation_basis: str
    interpretive_scope: str
    evidence_class: str
    provenance: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "knowledge_type": self.knowledge_type,
            "prefix": self.prefix,
            "label_ja": self.label_ja,
            "item_count": self.item_count,
            "tradition": self.tradition,
            "source_type": self.source_type,
            "required_inputs": list(self.required_inputs),
            "calculation_basis": self.calculation_basis,
            "interpretive_scope": self.interpretive_scope,
            "evidence_class": self.evidence_class,
            "provenance": self.provenance,
        }


@dataclass(frozen=True)
class DivinationRegistry:
    """Immutable registry response for all supported detailed traditions."""

    traditions: tuple[DivinationTradition, ...]

    @property
    def total_items(self) -> int:
        return sum(entry.item_count for entry in self.traditions)

    def to_dict(self) -> dict[str, Any]:
        return {
            "api_version": API_VERSION,
            "runtime_version": RUNTIME_VERSION,
            "registry": {
                "tradition_count": len(self.traditions),
                "total_items": self.total_items,
                "traditions": [entry.to_dict() for entry in self.traditions],
            },
            "safety": {
                "reference_only": True,
                "cultural_interpretation_only": True,
                "inference_performed": False,
                "scoring_performed": False,
                "ranking_performed": False,
                "diagnosis_performed": False,
                "prediction_performed": False,
                "message_ja": DIVINATION_SAFETY_MESSAGE_JA,
            },
        }


def _shared_value(
    items: tuple[Mapping[str, Any], ...],
    field: str,
    knowledge_type: str,
) -> Any:
    values = {repr(item.get(field)) for item in items}
    if len(values) != 1:
        raise DivinationRegistryError(
            f"{knowledge_type}: catalog field is not consistent: {field}"
        )
    return items[0].get(field)


def build_divination_registry(library: "KnowledgeLibrary") -> DivinationRegistry:
    """Build a deterministic registry from audited catalog metadata."""
    traditions: list[DivinationTradition] = []
    for knowledge_type, prefix, label_ja in DIVINATION_CATALOGS:
        result = library.search(knowledge_type=knowledge_type, limit=100)
        items = result.items
        if result.total != 100 or len(items) != 100:
            raise DivinationRegistryError(
                f"{knowledge_type}: expected 100 active items, found {result.total}"
            )
        if any(not str(item.get("id", "")).startswith(f"{prefix}-") for item in items):
            raise DivinationRegistryError(
                f"{knowledge_type}: item ID does not use the registered {prefix} prefix"
            )
        evidence_class = _shared_value(items, "evidence_class", knowledge_type)
        if evidence_class != "traditional_cultural_interpretation":
            raise DivinationRegistryError(
                f"{knowledge_type}: unsupported evidence class: {evidence_class}"
            )
        required_inputs = _shared_value(items, "required_inputs", knowledge_type)
        if not isinstance(required_inputs, list) or not required_inputs:
            raise DivinationRegistryError(
                f"{knowledge_type}: required_inputs must be a non-empty list"
            )
        traditions.append(
            DivinationTradition(
                knowledge_type=knowledge_type,
                prefix=prefix,
                label_ja=label_ja,
                item_count=result.total,
                tradition=str(_shared_value(items, "tradition", knowledge_type)),
                source_type=str(_shared_value(items, "source_type", knowledge_type)),
                required_inputs=tuple(str(value) for value in required_inputs),
                calculation_basis=str(
                    _shared_value(items, "calculation_basis", knowledge_type)
                ),
                interpretive_scope=str(
                    _shared_value(items, "interpretive_scope", knowledge_type)
                ),
                evidence_class=str(evidence_class),
                provenance=str(_shared_value(items, "provenance", knowledge_type)),
            )
        )
    return DivinationRegistry(traditions=tuple(traditions))
