"""Reference implementation of the notification-profile analysis rules.

This package is separate from the read-only ``analysis_engine`` runtime. It
turns questionnaire answers and behavior aggregates into transient tendencies
and immediately converts them into notification parameters. Tendencies are
never serialized, logged, or returned to callers outside the secretary step.
Applications port this logic and verify it against these functions.
"""

from .analysis import (
    AnalysisInputError,
    TendencySnapshot,
    analyze,
    load_rules,
)
from .secretary import (
    NotificationParameters,
    StreakDecision,
    StreakState,
    apply_streak_event,
    derive_parameters,
    recommend_presets,
    to_parameters,
    undo_decision,
)

__all__ = [
    "AnalysisInputError",
    "NotificationParameters",
    "StreakDecision",
    "StreakState",
    "TendencySnapshot",
    "analyze",
    "apply_streak_event",
    "derive_parameters",
    "load_rules",
    "recommend_presets",
    "to_parameters",
    "undo_decision",
]
