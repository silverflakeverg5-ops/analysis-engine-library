"""Read-only runtime access to the Analysis Engine Knowledge Library."""

from .library import (
    CatalogError,
    DuplicateItemIdError,
    ItemNotFoundError,
    KnowledgeLibrary,
    QueryValidationError,
    SearchResult,
)
from .matching import (
    SignalMatch,
    SignalMatchResult,
    SignalReference,
    SignalValidationError,
)
from .bundles import (
    BundleValidationError,
    InterpretationBundle,
    MaterialLink,
    MaterialSection,
)
from .pipeline import (
    ApplicationPipelineResult,
    PipelineCandidate,
    PipelineValidationError,
)
from .guidance import (
    ApplicationGuidanceBundle,
    GuidanceValidationError,
)
from .safety import (
    SafetyContractCheck,
    SafetyContractReport,
)
from .contracts import (
    ContractEndpointCheck,
    RuntimeContractReport,
)
from .divination import (
    DivinationRegistry,
    DivinationRegistryError,
    DivinationTradition,
)
from .numerology import (
    NumberCalculation,
    NumerologyCalculation,
    NumerologyValidationError,
    calculate_numerology,
)
from .japanese_name import (
    GridCalculation,
    JapaneseNameCalculation,
    JapaneseNameValidationError,
    calculate_japanese_name,
    calculate_japanese_name_from_dictionary,
)

__all__ = [
    "CatalogError",
    "DuplicateItemIdError",
    "ItemNotFoundError",
    "KnowledgeLibrary",
    "QueryValidationError",
    "SearchResult",
    "SignalMatch",
    "SignalMatchResult",
    "SignalReference",
    "SignalValidationError",
    "BundleValidationError",
    "InterpretationBundle",
    "MaterialLink",
    "MaterialSection",
    "ApplicationPipelineResult",
    "PipelineCandidate",
    "PipelineValidationError",
    "ApplicationGuidanceBundle",
    "GuidanceValidationError",
    "SafetyContractCheck",
    "SafetyContractReport",
    "ContractEndpointCheck",
    "RuntimeContractReport",
    "DivinationRegistry",
    "DivinationRegistryError",
    "DivinationTradition",
    "NumberCalculation",
    "NumerologyCalculation",
    "NumerologyValidationError",
    "calculate_numerology",
    "GridCalculation",
    "JapaneseNameCalculation",
    "JapaneseNameValidationError",
    "calculate_japanese_name",
    "calculate_japanese_name_from_dictionary",
]

__version__ = "1.4.0"
