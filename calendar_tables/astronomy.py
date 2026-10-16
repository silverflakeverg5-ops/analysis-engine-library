"""Solar longitude and new-moon instants for calendar-table precomputation.

Algorithms follow Meeus, *Astronomical Algorithms* (2nd ed.): the Sun from the
truncated VSOP87 Earth series (Appendix III, ch. 32 and 25), the Moon from the
ELP-2000/82 truncation of ch. 47, nutation in longitude from ch. 22, and
Delta T from the Espenak-Meeus polynomial for 2005-2050. Accuracy is about one
arcsecond for the Sun and ten arcseconds for the Moon, i.e. well under a
minute for solar-term and new-moon instants in 2019-2041.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from math import cos, fmod, radians, sin
from typing import Iterator


J2000 = 2451545.0

# (A, B, C) terms of VSOP87D Earth heliocentric longitude, radians * 1e8.
_EARTH_L = (
    (
        (175347046, 0.0, 0.0), (3341656, 4.6692568, 6283.0758500), (34894, 4.62610, 12566.15170),
        (3497, 2.7441, 5753.3849), (3418, 2.8289, 3.5231), (3136, 3.6277, 77713.7715),
        (2676, 4.4181, 7860.4194), (2343, 6.1352, 3930.2097), (1324, 0.7425, 11506.7698),
        (1273, 2.0371, 529.6910), (1199, 1.1096, 1577.3435), (990, 5.233, 5884.927),
        (902, 2.045, 26.298), (857, 3.508, 398.149), (780, 1.179, 5223.694),
        (753, 2.533, 5507.553), (505, 4.583, 18849.228), (492, 4.205, 775.523),
        (357, 2.920, 0.067), (317, 5.849, 11790.629), (284, 1.899, 796.298),
        (271, 0.315, 10977.079), (243, 0.345, 5486.778), (206, 4.806, 2544.314),
        (205, 1.869, 5573.143), (202, 2.458, 6069.777), (156, 0.833, 213.299),
        (132, 3.411, 2942.463), (126, 1.083, 20.775), (115, 0.645, 0.980),
        (103, 0.636, 4694.003), (102, 0.976, 15720.839), (102, 4.267, 7.114),
        (99, 6.21, 2146.17), (98, 0.68, 155.42), (86, 5.98, 161000.69),
        (85, 1.30, 6275.96), (85, 3.67, 71430.70), (80, 1.81, 17260.15),
        (79, 3.04, 12036.46), (75, 1.76, 5088.63), (74, 3.50, 3154.69),
        (74, 4.68, 801.82), (70, 0.83, 9437.76), (62, 3.98, 8827.39),
        (61, 1.82, 7084.90), (57, 2.78, 6286.60), (56, 4.39, 14143.50),
        (56, 3.47, 6279.55), (52, 0.19, 12139.55), (52, 1.33, 1748.02),
        (51, 0.28, 5856.48), (49, 0.49, 1194.45), (41, 5.37, 8429.24),
        (41, 2.40, 19651.05), (39, 6.17, 10447.39), (37, 6.04, 10213.29),
        (37, 2.57, 1059.38), (36, 1.71, 2352.87), (36, 1.78, 6812.77),
        (33, 0.59, 17789.85), (30, 0.44, 83996.85), (30, 2.74, 1349.87),
        (25, 3.16, 4690.48),
    ),
    (
        (628331966747, 0.0, 0.0), (206059, 2.678235, 6283.07585), (4303, 2.6351, 12566.1517),
        (425, 1.590, 3.523), (119, 5.796, 26.298), (109, 2.966, 1577.344),
        (93, 2.59, 18849.23), (72, 1.14, 529.69), (68, 1.87, 398.15),
        (67, 4.41, 5507.55), (59, 2.89, 5223.69), (56, 2.17, 155.42),
        (45, 0.40, 796.30), (36, 0.47, 775.52), (29, 2.65, 7.11),
        (21, 5.34, 0.98), (19, 1.85, 5486.78), (19, 4.97, 213.30),
        (17, 2.99, 6275.96), (16, 0.03, 2544.31), (16, 1.43, 2146.17),
        (15, 1.21, 10977.08), (12, 2.83, 1748.02), (12, 3.26, 5088.63),
        (12, 5.27, 1194.45), (12, 2.08, 4694.00), (11, 0.77, 553.57),
        (10, 1.30, 6286.60), (10, 4.24, 1349.87), (9, 2.70, 242.73),
        (9, 5.64, 951.72), (8, 5.30, 2352.87), (6, 2.65, 9437.76),
        (6, 4.67, 4690.48),
    ),
    (
        (52919, 0.0, 0.0), (8720, 1.0721, 6283.0758), (309, 0.867, 12566.152),
        (27, 0.05, 3.52), (16, 5.19, 26.30), (16, 3.68, 155.42),
        (10, 0.76, 18849.23), (9, 2.06, 77713.77), (7, 0.83, 775.52),
        (5, 4.66, 1577.34), (4, 1.03, 7.11), (4, 3.44, 5573.14),
        (3, 5.14, 796.30), (3, 6.05, 5507.55), (3, 1.19, 242.73),
        (3, 6.12, 529.69), (3, 0.31, 398.15), (3, 2.28, 553.57),
        (2, 4.38, 5223.69), (2, 3.75, 0.98),
    ),
    (
        (289, 5.844, 6283.076), (35, 0.0, 0.0), (17, 5.49, 12566.15),
        (3, 5.20, 155.42), (1, 4.72, 3.52), (1, 5.30, 18849.23),
        (1, 5.97, 242.73),
    ),
    ((114, 3.142, 0.0), (8, 4.13, 6283.08), (1, 3.84, 12566.15)),
    ((1, 3.14, 0.0),),
)

# Moon longitude terms (D, M, M', F, coefficient in 1e-6 degrees), Meeus 47.A.
_MOON_L = (
    (0, 0, 1, 0, 6288774), (2, 0, -1, 0, 1274027), (2, 0, 0, 0, 658314),
    (0, 0, 2, 0, 213618), (0, 1, 0, 0, -185116), (0, 0, 0, 2, -114332),
    (2, 0, -2, 0, 58793), (2, -1, -1, 0, 57066), (2, 0, 1, 0, 53322),
    (2, -1, 0, 0, 45758), (0, 1, -1, 0, -40923), (1, 0, 0, 0, -34720),
    (0, 1, 1, 0, -30383), (2, 0, 0, -2, 15327), (0, 0, 1, 2, -12528),
    (0, 0, 1, -2, 10980), (4, 0, -1, 0, 10675), (0, 0, 3, 0, 10034),
    (4, 0, -2, 0, 8548), (2, 1, -1, 0, -7888), (2, 1, 0, 0, -6766),
    (1, 0, -1, 0, -5163), (1, 1, 0, 0, 4987), (2, -1, 1, 0, 4036),
    (2, 0, 2, 0, 3994), (4, 0, 0, 0, 3861), (2, 0, -3, 0, 3665),
    (0, 1, -2, 0, -2689), (2, 0, -1, 2, -2602), (2, -1, -2, 0, 2390),
    (1, 0, 1, 0, -2348), (2, -2, 0, 0, 2236), (0, 1, 2, 0, -2120),
    (0, 2, 0, 0, -2069), (2, -2, -1, 0, 2048), (2, 0, 1, -2, -1773),
    (2, 0, 0, 2, -1595), (4, -1, -1, 0, 1215), (0, 0, 2, 2, -1110),
    (3, 0, -1, 0, -892), (2, 1, 1, 0, -810), (4, -1, -2, 0, 759),
    (0, 2, -1, 0, -713), (2, 2, -1, 0, -700), (2, 1, -2, 0, 691),
    (2, -1, 0, -2, 596), (4, 0, 1, 0, 549), (0, 0, 4, 0, 537),
    (4, -1, 0, 0, 520), (1, 0, -2, 0, -487), (2, 1, 0, -2, -399),
    (0, 0, 2, -2, -381), (1, 1, 1, 0, 351), (3, 0, -2, 0, -340),
    (4, 0, -3, 0, 330), (2, -1, 2, 0, 327), (0, 2, 1, 0, -323),
    (1, 1, -1, 0, 299), (2, 0, 3, 0, 294),
)

SYNODIC_MONTH = 29.530588861


def _norm(degrees: float) -> float:
    value = fmod(degrees, 360.0)
    return value + 360.0 if value < 0 else value


def julian_day(moment: datetime) -> float:
    """Julian Day of an aware datetime, on its own time scale."""
    moment = moment.astimezone(timezone.utc).replace(tzinfo=None)
    year, month = moment.year, moment.month
    day = moment.day + (moment.hour + (moment.minute + (moment.second + moment.microsecond / 1e6) / 60) / 60) / 24
    if month <= 2:
        year -= 1
        month += 12
    a = year // 100
    b = 2 - a + a // 4
    return int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + b - 1524.5


def from_julian_day(jd: float) -> datetime:
    """UTC datetime for a Julian Day."""
    return datetime(2000, 1, 1, 12, tzinfo=timezone.utc) + timedelta(days=jd - J2000)


def delta_t_seconds(jd: float) -> float:
    """TT - UT, Espenak & Meeus polynomial valid for 2005-2050."""
    year = 2000 + (jd - J2000) / 365.25
    t = year - 2000
    return 62.92 + 0.32217 * t + 0.005589 * t * t


def tt_to_ut(jde: float) -> float:
    return jde - delta_t_seconds(jde) / 86400.0


def ut_to_tt(jd: float) -> float:
    return jd + delta_t_seconds(jd) / 86400.0


def nutation_longitude(jde: float) -> float:
    """Nutation in longitude, degrees (Meeus ch. 22, 0.5" accuracy)."""
    t = (jde - J2000) / 36525.0
    omega = radians(125.04452 - 1934.136261 * t)
    sun = radians(280.4665 + 36000.7698 * t)
    moon = radians(218.3165 + 481267.8813 * t)
    arcsec = -17.20 * sin(omega) - 1.32 * sin(2 * sun) - 0.23 * sin(2 * moon) + 0.21 * sin(2 * omega)
    return arcsec / 3600.0


def sun_apparent_longitude(jde: float) -> float:
    """Apparent geocentric ecliptic longitude of the Sun, degrees."""
    tau = (jde - J2000) / 365250.0
    total = 0.0
    for power, series in enumerate(_EARTH_L):
        total += sum(a * cos(b + c * tau) for a, b, c in series) * tau ** power
    heliocentric = total / 1e8
    geometric = _norm(heliocentric * 57.29577951308232 + 180.0)
    fk5 = -0.09033 / 3600.0
    aberration = -20.4898 / 3600.0
    return _norm(geometric + fk5 + nutation_longitude(jde) + aberration)


def moon_geocentric_longitude(jde: float) -> float:
    """Geocentric ecliptic longitude of the Moon without nutation, degrees."""
    t = (jde - J2000) / 36525.0
    lp = 218.3164477 + 481267.88123421 * t - 0.0015786 * t * t + t ** 3 / 538841 - t ** 4 / 65194000
    d = 297.8501921 + 445267.1114034 * t - 0.0018819 * t * t + t ** 3 / 545868 - t ** 4 / 113065000
    m = 357.5291092 + 35999.0502909 * t - 0.0001536 * t * t + t ** 3 / 24490000
    mp = 134.9633964 + 477198.8675055 * t + 0.0087414 * t * t + t ** 3 / 69699 - t ** 4 / 14712000
    f = 93.2720950 + 483202.0175233 * t - 0.0036539 * t * t - t ** 3 / 3526000 + t ** 4 / 863310000
    a1 = 119.75 + 131.849 * t
    a2 = 53.09 + 479264.290 * t
    e = 1 - 0.002516 * t - 0.0000074 * t * t
    total = 0.0
    for cd, cm, cmp_, cf, coefficient in _MOON_L:
        term = coefficient * sin(radians(cd * d + cm * m + cmp_ * mp + cf * f))
        if abs(cm) == 1:
            term *= e
        elif abs(cm) == 2:
            term *= e * e
        total += term
    total += 3958 * sin(radians(a1)) + 1962 * sin(radians(lp - f)) + 318 * sin(radians(a2))
    return _norm(lp + total / 1e6)


def moon_apparent_longitude(jde: float) -> float:
    return _norm(moon_geocentric_longitude(jde) + nutation_longitude(jde))


def _signed_difference(a: float, b: float) -> float:
    return (a - b + 180.0) % 360.0 - 180.0


def solar_longitude_instant(target: float, jde_guess: float) -> float:
    """JDE (TT) when the Sun's apparent longitude equals ``target`` degrees."""
    jde = jde_guess
    for _ in range(50):
        step = _signed_difference(target, sun_apparent_longitude(jde)) * 365.2422 / 360.0
        jde += step
        if abs(step) < 1e-7:
            break
    return jde


def new_moon_instant(jde_guess: float) -> float:
    """JDE (TT) of the new moon nearest ``jde_guess``."""
    jde = jde_guess
    for _ in range(50):
        elongation = _signed_difference(moon_apparent_longitude(jde), sun_apparent_longitude(jde))
        step = -elongation * SYNODIC_MONTH / 360.0
        jde += step
        if abs(step) < 1e-7:
            break
    return jde


def new_moons_between(start: date, end: date) -> Iterator[float]:
    """JDE (TT) of every new moon from ``start`` to ``end`` inclusive, in order."""
    start_jd = julian_day(datetime(start.year, start.month, start.day, tzinfo=timezone.utc))
    end_jd = julian_day(datetime(end.year, end.month, end.day, tzinfo=timezone.utc)) + 1
    k = int((start_jd - 2451550.09766) / SYNODIC_MONTH) - 1
    previous = None
    while True:
        guess = 2451550.09766 + SYNODIC_MONTH * k
        jde = new_moon_instant(guess)
        k += 1
        if jde < start_jd - 1:
            continue
        if jde > end_jd + 1:
            return
        if previous is not None and abs(jde - previous) < 1:
            continue
        previous = jde
        yield jde


def solar_term_instants(year: int) -> list[tuple[int, float]]:
    """(longitude, JDE) for all 24 solar terms whose instant falls in ``year`` (UT)."""
    results = []
    start = julian_day(datetime(year, 1, 1, tzinfo=timezone.utc)) - 20
    for index in range(26):
        longitude = (285 + 15 * index) % 360
        guess = start + index * 365.2422 / 24
        jde = solar_longitude_instant(longitude, guess)
        moment = from_julian_day(tt_to_ut(jde))
        if moment.year == year:
            results.append((longitude, jde))
    return sorted(results, key=lambda pair: pair[1])
