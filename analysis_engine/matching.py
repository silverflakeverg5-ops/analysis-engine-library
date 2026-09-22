"""Deterministic Signal-to-Knowledge matching without inference or scoring."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Any, Mapping, Sequence, TYPE_CHECKING
import re
import unicodedata

from .library import (
    API_VERSION,
    ITEM_ID_PATTERN,
    MAX_LIMIT,
    RUNTIME_VERSION,
    SAFETY_MESSAGE_JA,
    QueryValidationError,
    _public_copy,
)

if TYPE_CHECKING:
    from .library import KnowledgeLibrary, _Record


MAX_SIGNALS = 20
MAX_SIGNAL_LENGTH = 200
MAX_EVIDENCE_PER_MATCH = 20
OBSERVATION_ID_PATTERN = re.compile(r"^OBS-[0-9]{6}$")
MATCH_FIELDS = (
    "name_ja",
    "name_en",
    "definition_ja",
    "observable_data",
    "signal_candidates",
)
DEFAULT_OPERATIONAL_TYPES = frozenset(
    {
        "api_contract",
        "app_use_case",
        "display_design",
        "documentation",
        "evidence_source",
        "library_governance",
        "mapping_rule",
        "modifier",
        "observation_signal",
        "roadmap",
        "safety_ethics",
        "test_case",
    }
)
MATCHING_MESSAGE_JA = (
    "一致は入力語とKnowledge Item内の記述を機械的に照合した結果です。"
    "関連性、因果関係、人物特性、確信度を推論したものではありません。"
)


class SignalValidationError(QueryValidationError):
    """Raised when Signal matching input violates the public contract."""


@dataclass(frozen=True)
class SignalReference:
    """One normalized matching input and its auditable expansion terms."""

    input_value: str
    resolved_signal_id: str | None
    terms: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "input": self.input_value,
            "resolved_signal_id": self.resolved_signal_id,
            "terms": list(self.terms),
        }


@dataclass(frozen=True)
class SignalMatch:
    """One candidate item with exact field-level match evidence."""

    item: Mapping[str, Any]
    matched_inputs: tuple[str, ...]
    evidence: tuple[Mapping[str, str], ...]
    evidence_truncated: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "item": _public_copy(self.item),
            "matched_inputs": list(self.matched_inputs),
            "evidence": [dict(entry) for entry in self.evidence],
            "evidence_truncated": self.evidence_truncated,
        }


@dataclass(frozen=True)
class SignalMatchResult:
    """Immutable, paginated Signal matching result envelope."""

    inputs: tuple[SignalReference, ...]
    matches: tuple[SignalMatch, ...]
    total: int
    offset: int
    limit: int
    mode: str
    target_knowledge_types: tuple[str, ...]
    include_operational: bool
    status: str | None

    @property
    def returned(self) -> int:
        return len(self.matches)

    @property
    def has_more(self) -> bool:
        return self.offset + self.returned < self.total

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable mapping response with safety boundaries."""
        return {
            "api_version": API_VERSION,
            "runtime_version": RUNTIME_VERSION,
            "mapping": {
                "method": "deterministic_text_containment",
                "mode": self.mode,
                "inputs": [reference.to_dict() for reference in self.inputs],
                "target_knowledge_types": list(self.target_knowledge_types),
                "include_operational": self.include_operational,
                "status": self.status,
            },
            "pagination": {
                "offset": self.offset,
                "limit": self.limit,
                "total": self.total,
                "returned": self.returned,
                "has_more": self.has_more,
            },
            "matches": [match.to_dict() for match in self.matches],
            "safety": {
                "mapping_only": True,
                "inference_performed": False,
                "scoring_performed": False,
                "ranking_performed": False,
                "message_ja": f"{SAFETY_MESSAGE_JA}{MATCHING_MESSAGE_JA}",
            },
        }


def _normalize_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value)
    return " ".join(normalized.casefold().split())


def _field_values(data: Mapping[str, Any], field: str) -> tuple[str, ...]:
    value = data.get(field)
    if isinstance(value, (tuple, list)):
        return tuple(str(entry) for entry in value)
    if value is None:
        return ()
    return (str(value),)


def _unique_terms(values: Sequence[str]) -> tuple[str, ...]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        stripped = value.strip()
        normalized = _normalize_text(stripped)
        if len(normalized) < 2 or normalized in seen:
            continue
        seen.add(normalized)
        result.append(stripped)
    return tuple(result)


def _resolve_inputs(
    library: "KnowledgeLibrary",
    signals: Sequence[str],
) -> tuple[SignalReference, ...]:
    if isinstance(signals, str):
        raise SignalValidationError("signals must be a sequence of strings, not one string")
    if not signals:
        raise SignalValidationError("at least one Signal input is required")
    if len(signals) > MAX_SIGNALS:
        raise SignalValidationError(f"at most {MAX_SIGNALS} Signal inputs are allowed")

    references: list[SignalReference] = []
    seen_inputs: set[str] = set()
    for raw_signal in signals:
        if not isinstance(raw_signal, str):
            raise SignalValidationError("every Signal input must be a string")
        signal = raw_signal.strip()
        if not signal:
            raise SignalValidationError("Signal input cannot be empty")
        if len(signal) > MAX_SIGNAL_LENGTH:
            raise SignalValidationError(
                f"Signal input cannot exceed {MAX_SIGNAL_LENGTH} characters"
            )

        normalized_input = _normalize_text(signal)
        if normalized_input in seen_inputs:
            continue
        seen_inputs.add(normalized_input)

        if OBSERVATION_ID_PATTERN.fullmatch(signal):
            record = library._records.get(signal)
            if record is None:
                raise SignalValidationError(f"Observation Signal not found: {signal}")
            if record.data.get("knowledge_type") != "observation_signal":
                raise SignalValidationError(f"Item is not an Observation Signal: {signal}")
            terms = _unique_terms(
                [
                    *_field_values(record.data, "name_ja"),
                    *_field_values(record.data, "name_en"),
                    *_field_values(record.data, "observable_data"),
                ]
            )
            references.append(SignalReference(signal, signal, terms))
            continue

        if ITEM_ID_PATTERN.fullmatch(signal):
            raise SignalValidationError(
                f"Knowledge Item ID is not an Observation Signal ID: {signal}"
            )
        if len(normalized_input) < 2:
            raise SignalValidationError("free-text Signal input must contain at least 2 characters")
        references.append(SignalReference(signal, None, (signal,)))

    if not references:
        raise SignalValidationError("at least one unique Signal input is required")
    return tuple(references)


def _normalize_target_types(values: Sequence[str] | None) -> tuple[str, ...]:
    if values is None:
        return ()
    if isinstance(values, str):
        raise SignalValidationError(
            "target_knowledge_types must be a sequence of strings, not one string"
        )
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        if not isinstance(value, str) or not value.strip():
            raise SignalValidationError(
                "target_knowledge_types cannot contain empty or non-string values"
            )
        normalized = value.strip().casefold()
        if normalized not in seen:
            seen.add(normalized)
            result.append(value.strip())
    return tuple(result)


def _match_record(
    record: "_Record",
    references: tuple[SignalReference, ...],
) -> tuple[tuple[str, ...], tuple[Mapping[str, str], ...], bool]:
    matched_inputs: list[str] = []
    evidence: list[Mapping[str, str]] = []
    seen_evidence: set[tuple[str, str, str, str]] = set()
    truncated = False

    for reference in references:
        input_matched = False
        for term in reference.terms:
            normalized_term = _normalize_text(term)
            for field in MATCH_FIELDS:
                for value in _field_values(record.data, field):
                    normalized_value = _normalize_text(value)
                    if normalized_term not in normalized_value:
                        continue
                    input_matched = True
                    key = (reference.input_value, term, field, value)
                    if key in seen_evidence:
                        continue
                    seen_evidence.add(key)
                    if len(evidence) < MAX_EVIDENCE_PER_MATCH:
                        evidence.append(
                            MappingProxyType(
                                {
                                    "input": reference.input_value,
                                    "matched_term": term,
                                    "field": field,
                                    "value": value,
                                }
                            )
                        )
                    else:
                        truncated = True
        if input_matched:
            matched_inputs.append(reference.input_value)

    return tuple(matched_inputs), tuple(evidence), truncated


def match_signals(
    library: "KnowledgeLibrary",
    signals: Sequence[str],
    *,
    mode: str = "any",
    target_knowledge_types: Sequence[str] | None = None,
    include_operational: bool = False,
    status: str | None = "active",
    offset: int = 0,
    limit: int = 20,
) -> SignalMatchResult:
    """Match Signal terms to item text without weights, scores, or inference."""
    if mode not in {"any", "all"}:
        raise SignalValidationError("mode must be one of: any, all")
    if not isinstance(include_operational, bool):
        raise SignalValidationError("include_operational must be a boolean")
    if not isinstance(offset, int) or isinstance(offset, bool) or offset < 0:
        raise SignalValidationError("offset must be a non-negative integer")
    if not isinstance(limit, int) or isinstance(limit, bool) or not 1 <= limit <= MAX_LIMIT:
        raise SignalValidationError(f"limit must be an integer from 1 to {MAX_LIMIT}")

    references = _resolve_inputs(library, signals)
    requested_types = _normalize_target_types(target_knowledge_types)
    requested_type_set = {value.casefold() for value in requested_types}

    matches: list[SignalMatch] = []
    for record in library._records.values():
        knowledge_type = str(record.data.get("knowledge_type", ""))
        if status is not None and str(record.data.get("status", "")).casefold() != status.casefold():
            continue
        if requested_type_set and knowledge_type.casefold() not in requested_type_set:
            continue
        if not include_operational and knowledge_type in DEFAULT_OPERATIONAL_TYPES:
            continue

        matched_inputs, evidence, truncated = _match_record(record, references)
        if mode == "any" and not matched_inputs:
            continue
        if mode == "all" and len(matched_inputs) != len(references):
            continue
        matches.append(
            SignalMatch(
                item=record.data,
                matched_inputs=matched_inputs,
                evidence=evidence,
                evidence_truncated=truncated,
            )
        )

    matches.sort(key=lambda match: str(match.item["id"]))
    page = tuple(matches[offset : offset + limit])
    return SignalMatchResult(
        inputs=references,
        matches=page,
        total=len(matches),
        offset=offset,
        limit=limit,
        mode=mode,
        target_knowledge_types=requested_types,
        include_operational=include_operational,
        status=status,
    )
