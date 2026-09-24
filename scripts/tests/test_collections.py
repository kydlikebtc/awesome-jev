"""Protect curated navigation from catalog retirement and incomplete edits."""

import copy
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from check_collections import ROOT, validate_collections


class CollectionsTest(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "collections.json").read_text())
        self.catalog = json.loads((ROOT / "catalog.json").read_text())

    def test_live_collections_are_valid(self):
        self.assertEqual(validate_collections(self.data, self.catalog), [])

    def test_retiring_selected_entry_requires_replacement(self):
        slug = self.data["collections"][0]["entries"][0]["slug"]
        self.catalog = [entry for entry in self.catalog if entry["slug"] != slug]
        self.assertTrue(any("not in catalog.json" in e for e in validate_collections(self.data, self.catalog)))

    def test_duplicate_does_not_inflate_curated_count(self):
        entries = self.data["collections"][0]["entries"]
        entries[1] = copy.deepcopy(entries[0])
        self.assertTrue(any("duplicate slug" in e for e in validate_collections(self.data, self.catalog)))

    def test_missing_translation_is_rejected(self):
        entry = self.data["collections"][0]["entries"][0]
        for value in ("", "English placeholder", None):
            with self.subTest(value=value):
                entry["caution_zh"] = value
                self.assertTrue(any("caution_zh" in e for e in validate_collections(self.data, self.catalog)))

    def test_vendor_benchmark_cannot_become_independent_measurement(self):
        slug = self.data["collections"][2]["entries"][0]["slug"]
        next(e for e in self.catalog if e["slug"] == slug)["official"] = True
        self.assertTrue(any("third-party benchmarks" in e for e in validate_collections(self.data, self.catalog)))

    def test_each_navigation_destination_must_exist(self):
        self.data["collections"][2]["id"] = "first-call"
        self.assertTrue(any("require exactly one" in e for e in validate_collections(self.data, self.catalog)))

    def test_malformed_editorial_data_reports_errors(self):
        for value in (None, [], {"collections": None}, {"collections": [None]}):
            with self.subTest(value=value):
                self.assertTrue(validate_collections(value, self.catalog))


if __name__ == "__main__":
    unittest.main()
