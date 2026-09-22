"""Deterministic response-shape fingerprints for runtime compatibility audits."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Any, Mapping, Sequence, TYPE_CHECKING
import json

from .library import API_VERSION, RUNTIME_VERSION, SAFETY_MESSAGE_JA

if TYPE_CHECKING:
    from .library import KnowledgeLibrary


CONTRACT_VERSION = "1.0"
DEFAULT_SNAPSHOT_PATH = (
    Path(__file__).resolve().parents[1] / "docs" / "08_runtime_api_contract_v1.json"
)
CONTRACT_AUDIT_MESSAGE_JA = (
    "この監査は公開レスポンスのキー構造と値型の互換性だけを検証します。"
    "人物データの分析、推論、評価は行いません。"
)


@dataclass(frozen=True)
class ContractEndpointCheck:
    """Compatibility result for one public response envelope."""

    endpoint: str
    expected_fingerprint: str | None
    actual_fingerprint: str | None

    @property
    def passed(self) -> bool:
        return (
            self.expected_fingerprint is not None
            and self.expected_fingerprint == self.actual_fingerprint
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "endpoint": self.endpoint,
            "passed": self.passed,
            "expected_fingerprint": self.expected_fingerprint,
            "actual_fingerprint": self.actual_fingerprint,
        }


@dataclass(frozen=True)
class RuntimeContractReport:
    """Aggregate API compatibility result against an independent snapshot."""

    snapshot_path: str
    snapshot_api_version: str | None
    checks: tuple[ContractEndpointCheck, ...]
    errors: tuple[str, ...]

    @property
    def api_version_compatible(self) -> bool:
        return self.snapshot_api_version == API_VERSION

    @property
    def passed(self) -> bool:
        return (
            not self.errors
            and self.api_version_compatible
            and bool(self.checks)
            and all(check.passed for check in self.checks)
        )

    @property
    def failed(self) -> int:
        return sum(not check.passed for check in self.checks)

    def to_dict(self) -> dict[str, Any]:
        return {
            "api_version": API_VERSION,
            "runtime_version": RUNTIME_VERSION,
            "contract": {
                "name": "runtime_api_compatibility",
                "contract_version": CONTRACT_VERSION,
                "snapshot_path": self.snapshot_path,
                "snapshot_api_version": self.snapshot_api_version,
                "api_version_compatible": self.api_version_compatible,
                "passed": self.passed,
                "total_endpoints": len(self.checks),
                "passed_endpoints": len(self.checks) - self.failed,
                "failed_endpoints": self.failed,
                "errors": list(self.errors),
                "checks": [check.to_dict() for check in self.checks],
            },
            "safety": {
                "audit_only": True,
                "inference_performed": False,
                "scoring_performed": False,
                "ranking_performed": False,
                "message_ja": f"{SAFETY_MESSAGE_JA}{CONTRACT_AUDIT_MESSAGE_JA}",
            },
        }


def _value_type(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    raise TypeError(f"Unsupported public response value type: {type(value).__name__}")


def _schema_shape(value: Any) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return {
            "type": "object",
            "properties": {
                str(key): _schema_shape(entry)
                for key, entry in sorted(value.items(), key=lambda item: str(item[0]))
            },
        }
    if isinstance(value, (list, tuple)):
        item_shapes: dict[str, Mapping[str, Any]] = {}
        for entry in value:
            shape = _schema_shape(entry)
            encoded = json.dumps(shape, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            item_shapes[encoded] = shape
        ordered_shapes = [item_shapes[key] for key in sorted(item_shapes)]
        if not ordered_shapes:
            items: Any = None
        elif len(ordered_shapes) == 1:
            items = ordered_shapes[0]
        else:
            items = {"one_of": ordered_shapes}
        return {"type": "array", "items": items}
    return {"type": _value_type(value)}


def _fingerprint(value: Any) -> str:
    encoded = json.dumps(
        _schema_shape(value),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return f"sha256:{sha256(encoded).hexdigest()}"


def _representative_responses(library: "KnowledgeLibrary") -> Mapping[str, Any]:
    return {
        "metadata": library.metadata(),
        "search": library.search("判断潜時", limit=1).to_dict(),
        "signal_matching": library.match_signals(
            ["OBS-000014"],
            target_knowledge_types=["decision_strategy"],
            limit=1,
        ).to_dict(),
        "interpretation_bundle": library.interpretation_bundle("DEC-000091").to_dict(),
        "application_guidance": library.application_guidance("APP-000001").to_dict(),
        "application_pipeline": library.application_pipeline(
            ["OBS-000014"],
            target_knowledge_types=["decision_strategy"],
            application_id="APP-000001",
            limit=1,
        ).to_dict(),
        "divination_registry": library.divination_registry().to_dict(),
        "numerology_calculation": library.calculate_numerology(
            "1990-01-01",
            name="Jane Doe",
            target_year=2026,
        ).to_dict(),
        "japanese_name_calculation": library.calculate_japanese_name_from_dictionary(
            "山田",
            "太郎",
            stroke_dictionary={"山": 3, "田": 5, "太": 4, "郎": 9},
            stroke_dictionary_id="modern_glyph_declared_v1",
        ).to_dict(),
        "safety_contract": library.safety_contract_report().to_dict(),
    }


def current_contract_fingerprints(
    library: "KnowledgeLibrary",
) -> dict[str, str]:
    """Return stable response-shape hashes for all versioned endpoints."""
    cached = getattr(library, "_contract_fingerprint_cache", None)
    if isinstance(cached, dict):
        return dict(cached)
    fingerprints = {
        endpoint: _fingerprint(response)
        for endpoint, response in _representative_responses(library).items()
    }
    library._contract_fingerprint_cache = dict(fingerprints)
    return fingerprints


def build_runtime_contract_snapshot(
    library: "KnowledgeLibrary",
) -> dict[str, Any]:
    """Build snapshot content for explicit review and controlled updates."""
    return {
        "contract_version": CONTRACT_VERSION,
        "api_version": API_VERSION,
        "description": (
            "Public response-shape fingerprints. Update only after an intentional "
            "API contract review."
        ),
        "schema_fingerprints": current_contract_fingerprints(library),
    }


def run_runtime_contract_audit(
    library: "KnowledgeLibrary",
    snapshot_path: str | Path | None = None,
) -> RuntimeContractReport:
    """Compare current response shapes with the reviewed v1 snapshot."""
    path = Path(snapshot_path).resolve() if snapshot_path else DEFAULT_SNAPSHOT_PATH
    display_path = (
        path.relative_to(Path(__file__).resolve().parents[1]).as_posix()
        if path.is_relative_to(Path(__file__).resolve().parents[1])
        else str(path)
    )
    errors: list[str] = []
    snapshot_api_version: str | None = None
    expected: Mapping[str, Any] = {}
    try:
        snapshot = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(snapshot, dict):
            raise ValueError("snapshot root must be an object")
        snapshot_api_version = snapshot.get("api_version")
        if snapshot.get("contract_version") != CONTRACT_VERSION:
            errors.append("contract_version does not match the runtime auditor")
        raw_expected = snapshot.get("schema_fingerprints")
        if not isinstance(raw_expected, dict):
            errors.append("schema_fingerprints must be an object")
        else:
            expected = raw_expected
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors.append(f"{type(exc).__name__}: {exc}")

    try:
        actual = current_contract_fingerprints(library)
    except Exception as exc:
        errors.append(f"runtime fingerprint generation failed: {type(exc).__name__}: {exc}")
        actual = {}

    endpoint_names = sorted(set(expected) | set(actual))
    checks = tuple(
        ContractEndpointCheck(
            endpoint=endpoint,
            expected_fingerprint=(
                str(expected[endpoint]) if endpoint in expected else None
            ),
            actual_fingerprint=(str(actual[endpoint]) if endpoint in actual else None),
        )
        for endpoint in endpoint_names
    )
    return RuntimeContractReport(
        snapshot_path=display_path,
        snapshot_api_version=(
            str(snapshot_api_version) if snapshot_api_version is not None else None
        ),
        checks=checks,
        errors=tuple(errors),
    )
