"""Dependency-free, read-only access to Knowledge Item YAML files.

This module intentionally performs no scoring, weighting, diagnosis, or
person-level inference.  Applications can retrieve neutral Knowledge Items and
remain responsible for their own separately governed inference logic.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence, TYPE_CHECKING
import json
import re


API_VERSION = "1.0"
RUNTIME_VERSION = "1.4.0"
DEFAULT_LIMIT = 20
MAX_LIMIT = 100
ITEM_ID_PATTERN = re.compile(r"^[A-Z]+-[0-9]{6}$")
TOP_LEVEL_KEY_PATTERN = re.compile(r"^(?P<key>[A-Za-z_][A-Za-z0-9_]*):(?P<value>.*)$")
INDEX_FILENAMES = {"core_index.yml", "personality_index.yml", "domains_index.yml"}
SEARCH_FIELDS = (
    "id",
    "knowledge_type",
    "name_ja",
    "name_en",
    "category",
    "attribute",
    "definition_ja",
    "tags",
    "parent",
    "related",
    "observable_data",
    "signal_candidates",
    "modifiers",
    "evidence",
    "tradition",
    "source_type",
    "evidence_class",
    "required_inputs",
    "calculation_basis",
    "trait_links",
    "interpretive_scope",
    "safe_expression",
    "provenance",
)
SAFETY_MESSAGE_JA = (
    "このレスポンスは知識項目の検索結果であり、人物の性格・能力・状態を"
    "推論、採点、診断したものではありません。"
)

if TYPE_CHECKING:
    from .bundles import InterpretationBundle
    from .guidance import ApplicationGuidanceBundle
    from .matching import SignalMatchResult
    from .pipeline import ApplicationPipelineResult
    from .safety import SafetyContractReport
    from .contracts import RuntimeContractReport
    from .divination import DivinationRegistry
    from .numerology import NumerologyCalculation
    from .japanese_name import JapaneseNameCalculation


class CatalogError(RuntimeError):
    """Base error for catalog loading and access."""


class DuplicateItemIdError(CatalogError):
    """Raised when two item files declare the same Knowledge Item ID."""


class ItemNotFoundError(CatalogError):
    """Raised by ``require`` when a Knowledge Item ID does not exist."""


class QueryValidationError(ValueError):
    """Raised when a search request violates the public query contract."""


@dataclass(frozen=True)
class _Record:
    data: Mapping[str, Any]
    source_path: str
    search_text: str


@dataclass(frozen=True)
class SearchResult:
    """Immutable result envelope for a read-only catalog search."""

    items: tuple[Mapping[str, Any], ...]
    total: int
    offset: int
    limit: int
    query: str | None
    filters: Mapping[str, Any]

    @property
    def returned(self) -> int:
        return len(self.items)

    @property
    def has_more(self) -> bool:
        return self.offset + self.returned < self.total

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable API response without inference output."""
        return {
            "api_version": API_VERSION,
            "runtime_version": RUNTIME_VERSION,
            "query": {
                "text": self.query,
                "filters": dict(self.filters),
            },
            "pagination": {
                "offset": self.offset,
                "limit": self.limit,
                "total": self.total,
                "returned": self.returned,
                "has_more": self.has_more,
            },
            "items": [dict(item) for item in self.items],
            "safety": {
                "inference_performed": False,
                "scoring_performed": False,
                "message_ja": SAFETY_MESSAGE_JA,
            },
        }


def _is_item_file(path: Path) -> bool:
    if path.suffix.lower() != ".yml":
        return False
    if path.name.endswith("_index.yml") or path.name in INDEX_FILENAMES:
        return False
    return True


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "[]":
        return []
    if value == "{}":
        return {}
    if value.startswith("[") or value.startswith("{"):
        try:
            return json.loads(value)
        except json.JSONDecodeError as exc:
            raise CatalogError(f"Unsupported inline YAML value: {value}") from exc
    if len(value) >= 2 and value[0] == value[-1] == '"':
        try:
            return json.loads(value)
        except json.JSONDecodeError as exc:
            raise CatalogError(f"Invalid quoted YAML scalar: {value}") from exc
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1].replace("''", "'")
    if value in {"|", ">", "|-", ">-", "|+", ">+"}:
        raise CatalogError("Block scalar YAML is not supported by the item runtime")
    return value


def _parse_item_yaml(text: str, source: Path) -> dict[str, Any]:
    """Parse the repository's audited flat item-schema YAML subset."""
    result: dict[str, Any] = {}
    current_list: str | None = None

    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        stripped = raw_line.strip()
        if stripped.startswith("- ") or stripped == "-":
            if current_list is None:
                raise CatalogError(f"{source}:{line_number}: list value without a field")
            value = stripped[1:].strip()
            result[current_list].append(_parse_scalar(value))
            continue

        if raw_line[0].isspace():
            raise CatalogError(f"{source}:{line_number}: nested mappings are not supported")

        match = TOP_LEVEL_KEY_PATTERN.match(raw_line)
        if not match:
            raise CatalogError(f"{source}:{line_number}: invalid top-level YAML field")

        key = match.group("key")
        raw_value = match.group("value").strip()
        if key in result:
            raise CatalogError(f"{source}:{line_number}: duplicate field {key}")
        if raw_value:
            result[key] = _parse_scalar(raw_value)
            current_list = None
        else:
            result[key] = []
            current_list = key

    if not result:
        raise CatalogError(f"{source}: empty item file")
    return result


def _freeze_value(value: Any) -> Any:
    if isinstance(value, list):
        return tuple(_freeze_value(entry) for entry in value)
    if isinstance(value, dict):
        return MappingProxyType({key: _freeze_value(entry) for key, entry in value.items()})
    return value


def _public_copy(data: Mapping[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in data.items():
        if isinstance(value, tuple):
            result[key] = list(value)
        elif isinstance(value, Mapping):
            result[key] = dict(value)
        else:
            result[key] = value
    return result


def _searchable_text(data: Mapping[str, Any]) -> str:
    parts: list[str] = []
    for field in SEARCH_FIELDS:
        value = data.get(field)
        if isinstance(value, (list, tuple)):
            parts.extend(str(entry) for entry in value)
        elif value is not None:
            parts.append(str(value))
    return "\n".join(parts).casefold()


def _normalized_tags(tags: Sequence[str] | None) -> tuple[str, ...]:
    if tags is None:
        return ()
    if isinstance(tags, str):
        raise QueryValidationError("tags must be a sequence of strings, not one string")
    normalized = tuple(tag.strip() for tag in tags)
    if any(not tag for tag in normalized):
        raise QueryValidationError("tags cannot contain empty values")
    return normalized


class KnowledgeLibrary:
    """In-memory, read-only index over audited Knowledge Item YAML files."""

    def __init__(self, data_root: str | Path | None = None) -> None:
        repository_root = Path(__file__).resolve().parents[1]
        self._data_root = Path(data_root).resolve() if data_root else repository_root / "data"
        if not self._data_root.is_dir():
            raise CatalogError(f"Knowledge data directory does not exist: {self._data_root}")

        records: dict[str, _Record] = {}
        for path in sorted(self._data_root.rglob("*.yml")):
            if not _is_item_file(path):
                continue
            parsed = _parse_item_yaml(path.read_text(encoding="utf-8"), path)
            item_id = parsed.get("id")
            if not isinstance(item_id, str) or not ITEM_ID_PATTERN.fullmatch(item_id):
                raise CatalogError(f"{path}: missing or invalid Knowledge Item ID")
            if item_id in records:
                previous = records[item_id].source_path
                current = path.relative_to(self._data_root).as_posix()
                raise DuplicateItemIdError(f"Duplicate Knowledge Item ID {item_id}: {previous} / {current}")

            frozen = MappingProxyType(
                {key: _freeze_value(value) for key, value in parsed.items()}
            )
            source_path = path.relative_to(self._data_root).as_posix()
            records[item_id] = _Record(
                data=frozen,
                source_path=source_path,
                search_text=_searchable_text(parsed),
            )

        if not records:
            raise CatalogError(f"No Knowledge Items found under: {self._data_root}")
        self._records = MappingProxyType(records)

    def __len__(self) -> int:
        return len(self._records)

    @property
    def data_root(self) -> Path:
        return self._data_root

    def metadata(self) -> dict[str, Any]:
        """Return catalog metadata and the enforced inference boundary."""
        return {
            "api_version": API_VERSION,
            "runtime_version": RUNTIME_VERSION,
            "item_count": len(self),
            "read_only": True,
            "inference_performed": False,
            "scoring_performed": False,
            "safety_message_ja": SAFETY_MESSAGE_JA,
        }

    def get(self, item_id: str) -> dict[str, Any] | None:
        """Return one item by exact ID, or ``None`` when it does not exist."""
        record = self._records.get(item_id)
        return _public_copy(record.data) if record else None

    def require(self, item_id: str) -> dict[str, Any]:
        """Return one item by exact ID or raise ``ItemNotFoundError``."""
        item = self.get(item_id)
        if item is None:
            raise ItemNotFoundError(f"Knowledge Item not found: {item_id}")
        return item

    def source_for(self, item_id: str) -> str:
        """Return the data-root-relative source path for an item."""
        record = self._records.get(item_id)
        if record is None:
            raise ItemNotFoundError(f"Knowledge Item not found: {item_id}")
        return record.source_path

    def search(
        self,
        query: str | None = None,
        *,
        category: str | None = None,
        knowledge_type: str | None = None,
        tags: Sequence[str] | None = None,
        status: str | None = "active",
        offset: int = 0,
        limit: int = DEFAULT_LIMIT,
        sort: str = "id",
    ) -> SearchResult:
        """Search neutral item content using exact filters and stable pagination."""
        if not isinstance(offset, int) or isinstance(offset, bool) or offset < 0:
            raise QueryValidationError("offset must be a non-negative integer")
        if not isinstance(limit, int) or isinstance(limit, bool) or not 1 <= limit <= MAX_LIMIT:
            raise QueryValidationError(f"limit must be an integer from 1 to {MAX_LIMIT}")
        if sort not in {"id", "name_ja", "name_en"}:
            raise QueryValidationError("sort must be one of: id, name_ja, name_en")

        normalized_query = query.strip() if query and query.strip() else None
        query_token = normalized_query.casefold() if normalized_query else None
        required_tags = _normalized_tags(tags)
        normalized_filters = {
            "category": category,
            "knowledge_type": knowledge_type,
            "tags": list(required_tags),
            "status": status,
            "sort": sort,
        }

        matches: list[_Record] = []
        for record in self._records.values():
            data = record.data
            if category is not None and str(data.get("category", "")).casefold() != category.casefold():
                continue
            if knowledge_type is not None and str(data.get("knowledge_type", "")).casefold() != knowledge_type.casefold():
                continue
            if status is not None and str(data.get("status", "")).casefold() != status.casefold():
                continue
            item_tags = {str(tag).casefold() for tag in data.get("tags", ())}
            if any(tag.casefold() not in item_tags for tag in required_tags):
                continue
            if query_token is not None and query_token not in record.search_text:
                continue
            matches.append(record)

        matches.sort(
            key=lambda record: (
                str(record.data.get(sort, "")).casefold(),
                str(record.data["id"]),
            )
        )
        page = matches[offset : offset + limit]
        public_items = tuple(MappingProxyType(_public_copy(record.data)) for record in page)
        return SearchResult(
            items=public_items,
            total=len(matches),
            offset=offset,
            limit=limit,
            query=normalized_query,
            filters=MappingProxyType(normalized_filters),
        )

    def match_signals(
        self,
        signals: Sequence[str],
        *,
        mode: str = "any",
        target_knowledge_types: Sequence[str] | None = None,
        include_operational: bool = False,
        status: str | None = "active",
        offset: int = 0,
        limit: int = DEFAULT_LIMIT,
    ) -> "SignalMatchResult":
        """Return deterministic text matches without scoring or inference."""
        from .matching import match_signals

        return match_signals(
            self,
            signals,
            mode=mode,
            target_knowledge_types=target_knowledge_types,
            include_operational=include_operational,
            status=status,
            offset=offset,
            limit=limit,
        )

    def interpretation_bundle(self, knowledge_id: str) -> "InterpretationBundle":
        """Collect auditable materials without interpreting the Knowledge Item."""
        from .bundles import build_interpretation_bundle

        return build_interpretation_bundle(self, knowledge_id)

    def application_pipeline(
        self,
        signals: Sequence[str],
        *,
        mode: str = "any",
        target_knowledge_types: Sequence[str] | None = None,
        status: str | None = "active",
        offset: int = 0,
        limit: int = 10,
        application_id: str | None = None,
    ) -> "ApplicationPipelineResult":
        """Match Signals and return candidate interpretation materials."""
        from .pipeline import run_application_pipeline

        return run_application_pipeline(
            self,
            signals,
            mode=mode,
            target_knowledge_types=target_knowledge_types,
            status=status,
            offset=offset,
            limit=limit,
            application_id=application_id,
        )

    def application_guidance(
        self,
        application_id: str,
    ) -> "ApplicationGuidanceBundle":
        """Collect neutral display and safety guidance for one App Use Case."""
        from .guidance import build_application_guidance

        return build_application_guidance(self, application_id)

    def divination_registry(self) -> "DivinationRegistry":
        """Return supported traditions and their shared application metadata."""
        from .divination import build_divination_registry

        return build_divination_registry(self)

    def calculate_numerology(
        self,
        birth_date: str,
        *,
        name: str | None = None,
        target_year: int | None = None,
        preserve_master_numbers: bool = True,
    ) -> "NumerologyCalculation":
        """Calculate disclosed numerology arithmetic without interpretation."""
        from .numerology import calculate_numerology

        return calculate_numerology(
            birth_date,
            name=name,
            target_year=target_year,
            preserve_master_numbers=preserve_master_numbers,
        )

    def calculate_japanese_name(
        self,
        surname: str,
        given_name: str,
        *,
        surname_strokes: Sequence[int],
        given_strokes: Sequence[int],
        stroke_dictionary: str,
        single_character_adjustment: str = "virtual_one",
    ) -> "JapaneseNameCalculation":
        """Calculate Japanese five-grid arithmetic without judging the name."""
        from .japanese_name import calculate_japanese_name

        return calculate_japanese_name(
            surname,
            given_name,
            surname_strokes=surname_strokes,
            given_strokes=given_strokes,
            stroke_dictionary=stroke_dictionary,
            single_character_adjustment=single_character_adjustment,
        )

    def calculate_japanese_name_from_dictionary(
        self,
        surname: str,
        given_name: str,
        *,
        stroke_dictionary: Mapping[str, int],
        stroke_dictionary_id: str,
        single_character_adjustment: str = "virtual_one",
    ) -> "JapaneseNameCalculation":
        """Resolve Japanese-name strokes from an exact versioned mapping."""
        from .japanese_name import calculate_japanese_name_from_dictionary

        return calculate_japanese_name_from_dictionary(
            surname,
            given_name,
            stroke_dictionary=stroke_dictionary,
            stroke_dictionary_id=stroke_dictionary_id,
            single_character_adjustment=single_character_adjustment,
        )

    def safety_contract_report(self) -> "SafetyContractReport":
        """Run the executable, read-only safety review for public responses."""
        from .safety import run_safety_contract_audit

        return run_safety_contract_audit(self)

    def runtime_contract_report(
        self,
        snapshot_path: str | Path | None = None,
    ) -> "RuntimeContractReport":
        """Compare public response shapes with the reviewed API snapshot."""
        from .contracts import run_runtime_contract_audit

        return run_runtime_contract_audit(self, snapshot_path)
