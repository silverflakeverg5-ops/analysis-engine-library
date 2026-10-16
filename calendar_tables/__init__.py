"""Precomputed daily calendar tables for applications (旧暦・六曜・選日・九星日盤).

Applications ship the generated table instead of running lunisolar or
astronomical calculations on the device. Every value is reproducible from the
declared methods in ``lunisolar.METHOD`` and ``notes.*_METHOD``.
"""

from .lunisolar import (
    METHOD as LUNISOLAR_METHOD,
    SUPPORTED_END,
    SUPPORTED_START,
    CalendarRangeError,
    LunarDate,
    lunar_date,
)
from .notes import (
    NINE_STAR_METHOD,
    SHANICHI_METHOD,
    daily_notes,
    nine_star_day,
    rokuyo,
    selected_days,
    sexagenary_day,
)

__all__ = [
    "CalendarRangeError",
    "LUNISOLAR_METHOD",
    "LunarDate",
    "NINE_STAR_METHOD",
    "SHANICHI_METHOD",
    "SUPPORTED_END",
    "SUPPORTED_START",
    "daily_notes",
    "lunar_date",
    "nine_star_day",
    "rokuyo",
    "selected_days",
    "sexagenary_day",
]
