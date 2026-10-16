from __future__ import annotations

from collections import Counter
from datetime import date, timedelta, timezone
import unittest

from calendar_tables import CalendarRangeError, daily_notes, lunar_date, sexagenary_day
from calendar_tables.astronomy import (
    from_julian_day,
    moon_geocentric_longitude,
    sun_apparent_longitude,
    tt_to_ut,
)
from calendar_tables import lunisolar
from calendar_tables.lunisolar import lunar_month_starts, term_date


# Lunar new year in China (UTC+8), used to validate the month algorithm itself.
CHINESE_NEW_YEAR = (
    "2020-01-25 2021-02-12 2022-02-01 2023-01-22 2024-02-10 2025-01-29 2026-02-17 "
    "2027-02-06 2028-01-26 2029-02-13 2030-02-03 2031-01-23 2032-02-11 2033-01-31 "
    "2034-02-19 2035-02-08 2036-01-28 2037-02-15 2038-02-04 2039-01-24 2040-02-12"
).split()
LEAP_MONTHS = {2020: 4, 2023: 2, 2025: 6, 2028: 5, 2031: 3, 2033: 11, 2036: 6, 2039: 5}


def _all_days():
    day = lunisolar.SUPPORTED_START
    while day <= lunisolar.SUPPORTED_END:
        yield day
        day += timedelta(days=1)


class AstronomyTests(unittest.TestCase):
    def test_sun_matches_meeus_example_25b(self) -> None:
        # 1992-10-13 0h TD, apparent longitude 199 deg 54' 21.818".
        self.assertAlmostEqual(sun_apparent_longitude(2448908.5), 199.906060, delta=0.0003)

    def test_moon_matches_meeus_example_47a(self) -> None:
        # 1992-04-12 0h TD, geocentric longitude 133.162655 deg.
        self.assertAlmostEqual(moon_geocentric_longitude(2448724.5), 133.162655, delta=0.0003)

    def test_equinox_and_solstice_dates(self) -> None:
        expected = {
            (2024, 0): date(2024, 3, 20), (2025, 0): date(2025, 3, 20),
            (2026, 0): date(2026, 3, 20), (2027, 0): date(2027, 3, 21),
            (2026, 90): date(2026, 6, 21), (2026, 180): date(2026, 9, 23),
            (2025, 270): date(2025, 12, 22), (2026, 270): date(2026, 12, 22),
        }
        for (year, longitude), day in expected.items():
            with self.subTest(year=year, longitude=longitude):
                self.assertEqual(term_date(year, longitude), day)


class LunisolarTests(unittest.TestCase):
    def test_algorithm_reproduces_chinese_new_year_in_utc8(self) -> None:
        original = lunisolar.JST
        try:
            lunisolar.JST = timezone(timedelta(hours=8))
            lunisolar._months.cache_clear()
            lunisolar.solar_term_dates.cache_clear()
            starts = sorted(
                begin.isoformat()
                for begin, number, leap, _ in lunar_month_starts()
                if number == 1 and not leap and 2020 <= begin.year <= 2040
            )
        finally:
            lunisolar.JST = original
            lunisolar._months.cache_clear()
            lunisolar.solar_term_dates.cache_clear()
        self.assertEqual(starts, CHINESE_NEW_YEAR)

    def test_japanese_new_year_differs_only_where_the_new_moon_is_after_midnight_jst(self) -> None:
        japan = {
            begin.year: begin.isoformat()
            for begin, number, leap, _ in lunar_month_starts()
            if number == 1 and not leap and 2020 <= begin.year <= 2040
        }
        differences = {year for year, day in japan.items() if day not in CHINESE_NEW_YEAR}
        self.assertEqual(differences, {2027, 2028})
        self.assertEqual(japan[2027], "2027-02-07")
        self.assertEqual(japan[2028], "2028-01-27")

    def test_leap_months_including_2033_problem(self) -> None:
        leaps = {
            begin.year: number
            for begin, number, leap, _ in lunar_month_starts()
            if leap and 2020 <= begin.year <= 2040
        }
        self.assertEqual(leaps, LEAP_MONTHS)
        self.assertEqual(lunar_date(date(2033, 12, 22)).leap, True)

    def test_known_lunar_dates(self) -> None:
        self.assertEqual(lunar_date(date(2026, 2, 17)), lunisolar.LunarDate(2026, 1, 1, False))
        self.assertEqual(lunar_date(date(2020, 1, 1)), lunisolar.LunarDate(2019, 12, 7, False))

    def test_out_of_range_dates_fail_closed(self) -> None:
        with self.assertRaises(CalendarRangeError):
            daily_notes(date(2019, 12, 31))
        with self.assertRaises(CalendarRangeError):
            daily_notes(date(2041, 1, 1))


class DailyNoteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.days = [daily_notes(day) for day in _all_days()]

    def test_sexagenary_anchor(self) -> None:
        self.assertEqual(sexagenary_day(date(2000, 1, 1)), "戊午")
        self.assertEqual(sexagenary_day(date(2026, 10, 17)), "甲子")

    def test_lunar_new_year_is_always_sensho(self) -> None:
        for notes in self.days:
            if notes["lunar"]["month"] == 1 and notes["lunar"]["day"] == 1 and not notes["lunar"]["leap"]:
                self.assertEqual(notes["rokuyo"], "先勝")

    def test_rokuyo_cycles_within_a_month(self) -> None:
        order = ["先勝", "友引", "先負", "仏滅", "大安", "赤口"]
        for previous, current in zip(self.days, self.days[1:]):
            if current["lunar"]["day"] != 1:
                self.assertEqual(order.index(current["rokuyo"]), (order.index(previous["rokuyo"]) + 1) % 6)

    def test_twelve_directive_repeats_on_sectional_term_days(self) -> None:
        sectional = {"立春", "啓蟄", "清明", "立夏", "芒種", "小暑", "立秋", "白露", "寒露", "立冬", "大雪", "小寒"}
        repeats = 0
        for previous, current in zip(self.days, self.days[1:]):
            term = current["solarTerm"]
            if term and term["name"] in sectional:
                self.assertEqual(previous["twelveDirective"], current["twelveDirective"])
                repeats += 1
            else:
                self.assertNotEqual(previous["twelveDirective"], current["twelveDirective"])
        self.assertGreater(repeats, 240)

    def test_selected_day_frequencies(self) -> None:
        counts = Counter(label for notes in self.days for label in notes["selectedDays"])
        years = 21
        self.assertTrue(5 * years <= counts["天赦日"] <= 7 * years)
        self.assertTrue(55 * years <= counts["一粒万倍日"] <= 66 * years)
        self.assertTrue(46 * years <= counts["不成就日"] <= 50 * years)
        self.assertAlmostEqual(counts["十方暮"] / len(self.days), 10 / 60, delta=0.005)
        self.assertAlmostEqual(counts["八専"] / len(self.days), 8 / 60, delta=0.005)
        self.assertAlmostEqual(counts["天一天上"] / len(self.days), 16 / 60, delta=0.005)
        self.assertAlmostEqual(counts["寅の日"] / len(self.days), 1 / 12, delta=0.002)

    def test_nine_star_moves_one_step_per_day(self) -> None:
        stars = ["一白水星", "二黒土星", "三碧木星", "四緑木星", "五黄土星", "六白金星", "七赤金星", "八白土星", "九紫火星"]
        switches = 0
        for previous, current in zip(self.days, self.days[1:]):
            a = stars.index(previous["nineStarDay"]["star"])
            b = stars.index(current["nineStarDay"]["star"])
            if previous["nineStarDay"]["flight"] != current["nineStarDay"]["flight"]:
                switches += 1
                self.assertEqual(sexagenary_day(date.fromisoformat(current["date"])), "甲子")
                continue
            step = 1 if current["nineStarDay"]["flight"] == "yang" else -1
            self.assertEqual(b, (a + step) % 9)
        self.assertEqual(switches, 42)

    def test_seasonal_days_once_per_year(self) -> None:
        counts = Counter(label for notes in self.days for label in notes["seasonalDays"])
        for label in ("節分", "八十八夜", "入梅", "半夏生", "二百十日", "春の彼岸中日", "夏の土用入り", "春社日"):
            self.assertEqual(counts[label], 21, label)
        setsubun = [notes["date"] for notes in self.days if "節分" in notes["seasonalDays"] and notes["date"].startswith("2026")]
        self.assertEqual(setsubun, ["2026-02-03"])


if __name__ == "__main__":
    unittest.main()
