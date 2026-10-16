from __future__ import annotations

from datetime import date
from pathlib import Path
import hashlib
import json
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from export_app_bundle import export_bundle  # noqa: E402
from analysis_profile import load_rules  # noqa: E402


class AppBundleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name)
        cls.manifest = export_bundle(cls.out, date(2026, 1, 1), date(2026, 12, 31))

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tmp.cleanup()

    def test_manifest_hashes_match_files(self) -> None:
        self.assertEqual(self.manifest["format"], "secretary-app-bundle-v1")
        for entry in self.manifest["files"]:
            data = (self.out / entry["path"]).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(), entry["sha256"])

    def test_calendar_days_link_to_library_items(self) -> None:
        calendar = json.loads((self.out / "calendar_2026_2026.json").read_text(encoding="utf-8"))
        self.assertEqual(len(calendar["days"]), 365)
        knowledge = json.loads((self.out / "knowledge.json").read_text(encoding="utf-8"))
        ids = {item["id"] for item in knowledge["items"]}
        for day in calendar["days"]:
            self.assertTrue(set(day["noteIds"]) <= ids)
            self.assertIn(day["nineStarDay"]["starId"], ids)

    def test_rule_references_ship_without_display_text(self) -> None:
        knowledge = json.loads((self.out / "knowledge.json").read_text(encoding="utf-8"))
        text = json.dumps(knowledge, ensure_ascii=False)
        for term in load_rules()["forbidden_output_terms"]:
            if term in ("診断", "障害"):
                continue  # safety boundaries of divination items mention these words
            self.assertNotIn(term, text)
        references = [item for item in knowledge["items"] if item.get("rule_reference_only")]
        self.assertTrue(references)
        self.assertTrue(all(set(item) == {"id", "rule_reference_only"} for item in references))

    def test_rejects_range_outside_supported_table(self) -> None:
        with self.assertRaises(ValueError):
            export_bundle(self.out, date(2019, 1, 1), date(2019, 12, 31))


if __name__ == "__main__":
    unittest.main()
