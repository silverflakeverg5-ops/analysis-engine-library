"""Compose Signal matching and interpretation materials for applications."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence, TYPE_CHECKING

from .bundles import BUNDLE_MESSAGE_JA, InterpretationBundle
from .library import API_VERSION, RUNTIME_VERSION, SAFETY_MESSAGE_JA, QueryValidationError
from .matching import MATCHING_MESSAGE_JA, SignalMatch, SignalReference
from .guidance import ApplicationGuidanceBundle

if TYPE_CHECKING:
    from .library import KnowledgeLibrary


DEFAULT_PIPELINE_LIMIT = 10
MAX_PIPELINE_LIMIT = 20
PIPELINE_MESSAGE_JA = (
    "候補はSignalの文字列照合結果であり、各バンドルは解釈前の確認材料です。"
    "候補間の優先順位、人物特性、結論は生成していません。"
)


class PipelineValidationError(QueryValidationError):
    """Raised when an application-pipeline request violates its contract."""


@dataclass(frozen=True)
class PipelineCandidate:
    """One deterministic match paired with its interpretation materials."""

    match: SignalMatch
    materials: InterpretationBundle

    def to_dict(self) -> dict[str, Any]:
        return {
            "match": {
                "knowledge_id": self.match.item["id"],
                "matched_inputs": list(self.match.matched_inputs),
                "evidence": [dict(entry) for entry in self.match.evidence],
                "evidence_truncated": self.match.evidence_truncated,
            },
            "interpretation_materials": self.materials.to_dict()["bundle"],
        }


@dataclass(frozen=True)
class ApplicationPipelineResult:
    """Paginated application handoff that performs no inference or ranking."""

    inputs: tuple[SignalReference, ...]
    candidates: tuple[PipelineCandidate, ...]
    total: int
    offset: int
    limit: int
    mode: str
    target_knowledge_types: tuple[str, ...]
    status: str | None
    application_guidance: ApplicationGuidanceBundle | None

    @property
    def returned(self) -> int:
        return len(self.candidates)

    @property
    def has_more(self) -> bool:
        return self.offset + self.returned < self.total

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable response with explicit safety boundaries."""
        return {
            "api_version": API_VERSION,
            "runtime_version": RUNTIME_VERSION,
            "pipeline": {
                "method": "signal_match_then_material_bundle",
                "mapping_method": "deterministic_text_containment",
                "application_id": (
                    self.application_guidance.application["id"]
                    if self.application_guidance is not None
                    else None
                ),
                "mode": self.mode,
                "inputs": [reference.to_dict() for reference in self.inputs],
                "target_knowledge_types": list(self.target_knowledge_types),
                "status": self.status,
            },
            "pagination": {
                "offset": self.offset,
                "limit": self.limit,
                "total": self.total,
                "returned": self.returned,
                "has_more": self.has_more,
            },
            "candidates": [candidate.to_dict() for candidate in self.candidates],
            "application_guidance": (
                self.application_guidance.to_dict()["guidance"]
                if self.application_guidance is not None
                else None
            ),
            "safety": {
                "mapping_only": True,
                "materials_only": True,
                "inference_performed": False,
                "scoring_performed": False,
                "ranking_performed": False,
                "evidence_strength_assessed": False,
                "applicability_assessed": False,
                "display_suitability_assessed": False,
                "message_ja": (
                    f"{SAFETY_MESSAGE_JA}{MATCHING_MESSAGE_JA}"
                    f"{BUNDLE_MESSAGE_JA}{PIPELINE_MESSAGE_JA}"
                ),
            },
        }


def run_application_pipeline(
    library: "KnowledgeLibrary",
    signals: Sequence[str],
    *,
    mode: str = "any",
    target_knowledge_types: Sequence[str] | None = None,
    status: str | None = "active",
    offset: int = 0,
    limit: int = DEFAULT_PIPELINE_LIMIT,
    application_id: str | None = None,
) -> ApplicationPipelineResult:
    """Match Signals and attach auditable materials to the returned page."""
    if (
        not isinstance(limit, int)
        or isinstance(limit, bool)
        or not 1 <= limit <= MAX_PIPELINE_LIMIT
    ):
        raise PipelineValidationError(
            f"limit must be an integer from 1 to {MAX_PIPELINE_LIMIT}"
        )

    application_guidance = (
        library.application_guidance(application_id)
        if application_id is not None
        else None
    )

    matches = library.match_signals(
        signals,
        mode=mode,
        target_knowledge_types=target_knowledge_types,
        include_operational=False,
        status=status,
        offset=offset,
        limit=limit,
    )
    candidates = tuple(
        PipelineCandidate(
            match=match,
            materials=library.interpretation_bundle(str(match.item["id"])),
        )
        for match in matches.matches
    )
    return ApplicationPipelineResult(
        inputs=matches.inputs,
        candidates=candidates,
        total=matches.total,
        offset=matches.offset,
        limit=matches.limit,
        mode=matches.mode,
        target_knowledge_types=matches.target_knowledge_types,
        status=matches.status,
        application_guidance=application_guidance,
    )
