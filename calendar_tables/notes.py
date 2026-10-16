"""Daily calendar notes: 六曜, 日干支, 十二直, 選日, 雑節, 九星日盤."""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from functools import lru_cache

from .astronomy import from_julian_day, julian_day, solar_longitude_instant, tt_to_ut
from .lunisolar import JST, LunarDate, lunar_date, solar_term_dates, term_date


STEMS = "甲乙丙丁戊己庚辛壬癸"
BRANCHES = "子丑寅卯辰巳午未申酉戌亥"
ROKUYO = ("大安", "赤口", "先勝", "友引", "先負", "仏滅")  # index = (month + day) % 6
TWELVE_DIRECTIVES = "建除満平定執破危成納開閉"
NINE_STARS = ("一白水星", "二黒土星", "三碧木星", "四緑木星", "五黄土星", "六白金星", "七赤金星", "八白土星", "九紫火星")

# 節 (sectional term) longitude -> solar-term month number (寅月 = 1).
SECTIONAL_TERM_MONTH = {
    315: 1, 345: 2, 15: 3, 45: 4, 75: 5, 105: 6,
    135: 7, 165: 8, 195: 9, 225: 10, 255: 11, 285: 12,
}
ICHIRYU_MANBAI = {
    1: "丑午", 2: "酉寅", 3: "子卯", 4: "卯辰", 5: "巳午", 6: "酉午",
    7: "子未", 8: "卯申", 9: "酉午", 10: "酉戌", 11: "亥子", 12: "卯子",
}
TENSHA = {1: "戊寅", 2: "戊寅", 3: "戊寅", 4: "甲午", 5: "甲午", 6: "甲午",
          7: "戊申", 8: "戊申", 9: "戊申", 10: "甲子", 11: "甲子", 12: "甲子"}
SANRINBO = {1: "亥", 4: "亥", 7: "亥", 10: "亥", 2: "寅", 5: "寅", 8: "寅", 11: "寅",
            3: "午", 6: "午", 9: "午", 12: "午"}
FUJOJU = {
    1: (3, 11, 19, 27), 7: (3, 11, 19, 27), 2: (2, 10, 18, 26), 8: (2, 10, 18, 26),
    3: (1, 9, 17, 25), 9: (1, 9, 17, 25), 4: (4, 12, 20, 28), 10: (4, 12, 20, 28),
    5: (5, 13, 21, 29), 11: (5, 13, 21, 29), 6: (6, 14, 22, 30), 12: (6, 14, 22, 30),
}
HAPPEN_EXCLUDED = {"癸丑", "丙辰", "戊午", "壬戌"}

NINE_STAR_METHOD = "nearest_kinoe_ne_to_solstice_no_leap_adjustment_v1"
SHANICHI_METHOD = "nearest_tsuchinoe_to_equinox_noon_tiebreak_v1"


def sexagenary_index(day: date) -> int:
    """0 = 甲子. Uses JDN - 11 (2000-01-01 is 戊午 = 54)."""
    jdn = day.toordinal() + 1721425
    return (jdn - 11) % 60


def sexagenary_name(index: int) -> str:
    return STEMS[index % 10] + BRANCHES[index % 12]


def sexagenary_day(day: date) -> str:
    return sexagenary_name(sexagenary_index(day))


@lru_cache(maxsize=1)
def _sectional_starts() -> tuple[tuple[date, int], ...]:
    return tuple(sorted(
        (day, SECTIONAL_TERM_MONTH[lon])
        for day, (lon, _, _) in solar_term_dates().items()
        if lon in SECTIONAL_TERM_MONTH
    ))


def solar_term_month(day: date) -> int:
    """Solar-term month number (寅月 = 1 ... 丑月 = 12)."""
    current = None
    for start, number in _sectional_starts():
        if start > day:
            break
        current = number
    if current is None:
        raise ValueError(f"no sectional term before {day.isoformat()}")
    return current


def rokuyo(lunar: LunarDate) -> str:
    return ROKUYO[(lunar.month + lunar.day) % 6]


def twelve_directive(day: date) -> str:
    month_branch = (solar_term_month(day) + 1) % 12
    day_branch = sexagenary_index(day) % 12
    return TWELVE_DIRECTIVES[(day_branch - month_branch) % 12]


def selected_days(day: date, lunar: LunarDate) -> list[str]:
    index = sexagenary_index(day)
    name = sexagenary_name(index)
    branch = BRANCHES[index % 12]
    month = solar_term_month(day)
    notes = []
    if branch in ICHIRYU_MANBAI[month]:
        notes.append("一粒万倍日")
    if name == TENSHA[month]:
        notes.append("天赦日")
    if branch == "寅":
        notes.append("寅の日")
    if branch == "巳":
        notes.append("巳の日")
    if name == "己巳":
        notes.append("己巳の日")
    if name == "甲子":
        notes.append("甲子の日")
    if lunar.day in FUJOJU[lunar.month]:
        notes.append("不成就日")
    if branch == SANRINBO[month]:
        notes.append("三隣亡")
    if 20 <= index <= 29:
        notes.append("十方暮")
    if 48 <= index <= 59 and name not in HAPPEN_EXCLUDED:
        notes.append("八専")
    if 29 <= index <= 44:
        notes.append("天一天上")
    return notes


def _longitude_date(year: int, longitude: float) -> date:
    guess = julian_day(datetime(year, 1, 1, tzinfo=timezone.utc)) + ((longitude - 280) % 360) * 365.2422 / 360
    jde = solar_longitude_instant(longitude, guess)
    return from_julian_day(tt_to_ut(jde)).astimezone(JST).date()


def _equinox_instant(year: int, longitude: int) -> datetime:
    for day, (lon, _, instant) in solar_term_dates().items():
        if lon == longitude and day.year == year:
            return instant
    raise ValueError(f"equinox {longitude} missing in {year}")


def _shanichi(year: int, longitude: int) -> date:
    instant = _equinox_instant(year, longitude)
    equinox = instant.date()
    offset = (4 - sexagenary_index(equinox) % 10) % 10  # days to next 戊
    if offset == 0:
        return equinox
    if offset < 5:
        return equinox + timedelta(days=offset)
    if offset > 5:
        return equinox - timedelta(days=10 - offset)
    # Equidistant (equinox on 癸): before noon -> earlier 戊, otherwise later.
    return equinox - timedelta(days=5) if instant.hour < 12 else equinox + timedelta(days=5)


@lru_cache(maxsize=32)
def seasonal_days(year: int) -> dict[date, list[str]]:
    """雑節 for one calendar year, keyed by JST date."""
    risshun = term_date(year, 315)
    shunbun = term_date(year, 0)
    shubun = term_date(year, 180)
    entries: dict[date, list[str]] = {}

    def add(day: date, label: str) -> None:
        entries.setdefault(day, []).append(label)

    add(risshun - timedelta(days=1), "節分")
    for equinox, name in ((shunbun, "春の彼岸"), (shubun, "秋の彼岸")):
        add(equinox - timedelta(days=3), f"{name}入り")
        add(equinox, f"{name}中日")
        add(equinox + timedelta(days=3), f"{name}明け")
    add(_shanichi(year, 0), "春社日")
    add(_shanichi(year, 180), "秋社日")
    add(risshun + timedelta(days=87), "八十八夜")
    add(_longitude_date(year, 80), "入梅")
    add(_longitude_date(year, 100), "半夏生")
    for longitude, season in ((297, "冬"), (27, "春"), (117, "夏"), (207, "秋")):
        add(_longitude_date(year, longitude), f"{season}の土用入り")
    add(risshun + timedelta(days=209), "二百十日")
    add(risshun + timedelta(days=219), "二百二十日")
    return entries


def seasonal_day_labels(day: date) -> list[str]:
    return list(seasonal_days(day.year).get(day, []))


@lru_cache(maxsize=1)
def _nine_star_switches() -> tuple[tuple[date, str], ...]:
    switches = []
    for year in range(2018, 2043):
        for longitude, flight in ((270, "yang"), (90, "yin")):
            solstice = term_date(year, longitude)
            offset = sexagenary_index(solstice)  # days since the previous 甲子
            if offset <= 30:
                start = solstice - timedelta(days=offset)
            else:
                start = solstice + timedelta(days=60 - offset)
            switches.append((start, flight))
    return tuple(sorted(switches))


def nine_star_day(day: date) -> tuple[str, str]:
    """(day star name, flight) by the declared switch method."""
    current = None
    for start, flight in _nine_star_switches():
        if start > day:
            break
        current = (start, flight)
    if current is None:
        raise ValueError(f"no nine-star switch before {day.isoformat()}")
    start, flight = current
    steps = (day - start).days % 9
    number = 1 + steps if flight == "yang" else 9 - steps
    return NINE_STARS[number - 1], flight


def daily_notes(day: date) -> dict:
    lunar = lunar_date(day)
    term = solar_term_dates().get(day)
    star, flight = nine_star_day(day)
    return {
        "date": day.isoformat(),
        "lunar": {"year": lunar.year, "month": lunar.month, "day": lunar.day, "leap": lunar.leap},
        "rokuyo": rokuyo(lunar),
        "sexagenaryDay": sexagenary_day(day),
        "solarTermMonth": solar_term_month(day),
        "twelveDirective": twelve_directive(day),
        "solarTerm": None if term is None else {"name": term[1], "longitude": term[0], "instantJst": term[2].isoformat(timespec="minutes")},
        "selectedDays": selected_days(day, lunar),
        "seasonalDays": seasonal_day_labels(day),
        "nineStarDay": {"star": star, "flight": flight},
    }
