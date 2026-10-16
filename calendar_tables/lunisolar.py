"""Japanese lunisolar (旧暦) dates and solar-term dates in JST.

Method ``jst_chuki_first_missing_v1``:

- Days are civil dates in Japan Standard Time (UTC+9), switching at midnight.
- A month starts on the JST date of a new moon.
- Each month is numbered by the principal term (中気) it contains. The month
  containing the winter solstice is month 11.
- When the span between two winter-solstice months holds 13 months, the first
  month without a principal term is a leap month carrying the previous number.

This rule resolves the 2033 problem with a leap 11th month (閏十一月), as
recommended by the Japan Calendar Culture Promotion Association. It differs
from the strict Tenpo rule only where that rule breaks down.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from functools import lru_cache

from .astronomy import from_julian_day, new_moons_between, solar_term_instants, tt_to_ut


METHOD = "jst_chuki_first_missing_v1"
JST = timezone(timedelta(hours=9))
SUPPORTED_START = date(2020, 1, 1)
SUPPORTED_END = date(2040, 12, 31)

SOLAR_TERMS = {
    315: "立春", 330: "雨水", 345: "啓蟄", 0: "春分", 15: "清明", 30: "穀雨",
    45: "立夏", 60: "小満", 75: "芒種", 90: "夏至", 105: "小暑", 120: "大暑",
    135: "立秋", 150: "処暑", 165: "白露", 180: "秋分", 195: "寒露", 210: "霜降",
    225: "立冬", 240: "小雪", 255: "大雪", 270: "冬至", 285: "小寒", 300: "大寒",
}
# Principal term longitude -> lunisolar month number.
PRINCIPAL_TERM_MONTH = {
    330: 1, 0: 2, 30: 3, 60: 4, 90: 5, 120: 6,
    150: 7, 180: 8, 210: 9, 240: 10, 270: 11, 300: 12,
}


class CalendarRangeError(ValueError):
    """Raised for dates outside the supported precomputed range."""


@dataclass(frozen=True)
class LunarDate:
    year: int
    month: int
    day: int
    leap: bool


def _jst_date(jde: float) -> date:
    return from_julian_day(tt_to_ut(jde)).astimezone(JST).date()


@lru_cache(maxsize=1)
def solar_term_dates() -> dict[date, tuple[int, str, datetime]]:
    """JST date -> (longitude, name, JST instant) for 2018-2042."""
    result = {}
    for year in range(2018, 2043):
        for longitude, jde in solar_term_instants(year):
            instant = from_julian_day(tt_to_ut(jde)).astimezone(JST)
            result[instant.date()] = (longitude, SOLAR_TERMS[longitude], instant)
    return result


@lru_cache(maxsize=1)
def _months() -> tuple[tuple[date, int, bool, int], ...]:
    """(start date, month number, leap, lunar year) for every month in range."""
    starts = [_jst_date(jde) for jde in new_moons_between(date(2018, 10, 1), date(2042, 3, 1))]
    terms = solar_term_dates()
    principal = sorted(
        (day, longitude) for day, (longitude, _, _) in terms.items() if longitude in PRINCIPAL_TERM_MONTH
    )
    months = []
    for index in range(len(starts) - 1):
        begin, end = starts[index], starts[index + 1]
        inside = [lon for day, lon in principal if begin <= day < end]
        months.append([begin, inside])

    solstice_months = [i for i, (_, inside) in enumerate(months) if 270 in inside]
    numbered: list[tuple[date, int, bool]] = []
    for a, b in zip(solstice_months, solstice_months[1:]):
        span = months[a:b]
        leap_index = None
        if len(span) == 13:
            leap_index = next(i for i, (_, inside) in enumerate(span) if not inside)
        number = 11
        for i, (begin, inside) in enumerate(span):
            if i == leap_index:
                numbered.append((begin, numbered[-1][1], True))
                continue
            if i > 0:
                number = number % 12 + 1
            numbered.append((begin, number, False))

    result = []
    year = None
    for begin, number, leap in numbered:
        if number == 1 and not leap:
            year = begin.year
        elif year is None:
            # Months 11-12 before the first new year in range: a month starting
            # in Jan/Feb still belongs to the previous lunar year.
            year = begin.year if begin.month >= 6 else begin.year - 1
        result.append((begin, number, leap, year))
    return tuple(result)


def _check_range(day: date) -> None:
    if not SUPPORTED_START <= day <= SUPPORTED_END:
        raise CalendarRangeError(f"date outside supported range: {day.isoformat()}")


def lunar_date(day: date) -> LunarDate:
    _check_range(day)
    months = _months()
    for (begin, number, leap, year), following in zip(months, months[1:]):
        if begin <= day < following[0]:
            return LunarDate(year, number, (day - begin).days + 1, leap)
    raise CalendarRangeError(f"no lunar month covers {day.isoformat()}")


def lunar_month_starts() -> tuple[tuple[date, int, bool, int], ...]:
    return _months()


def solar_term_on(day: date) -> tuple[int, str, datetime] | None:
    _check_range(day)
    return solar_term_dates().get(day)


def term_date(year: int, longitude: int) -> date:
    """JST date of the solar term with ``longitude`` in calendar year ``year``."""
    for day, (lon, _, _) in solar_term_dates().items():
        if lon == longitude and day.year == year:
            return day
    raise CalendarRangeError(f"term {longitude} not found in {year}")
