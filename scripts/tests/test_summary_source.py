"""Whose words a summary is: summary_source on every surface (I21).

Most summaries were copied from the linked repository's own GitHub description
by the bulk passes, while the generated licence statement said no descriptive
text had been inherited. summary_source records the fact per row; the weekly
refresh sets the upstream values by comparing the texts (its rules are pinned
in test_refresh_metadata.py). Here: the READMEs and pattern pages mark those
summaries next to the machine-translation mark, docs/sources.md counts them
apart, and the labels exist once, in taxonomy.json.
"""

from __future__ import annotations

import copy
import json
import pathlib
import sys
import unittest
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import _stats  # noqa: E402
import build_docs  # noqa: E402
import build_readme  # noqa: E402
import refresh_metadata  # noqa: E402
from readme import rows, strings  # noqa: E402

SCHEMA = json.loads((ROOT / "schema" / "entry.schema.json").read_text(encoding="utf-8"))
TAXONOMY = json.loads((ROOT / "taxonomy.json").read_text(encoding="utf-8"))

EN_UP, EN_STALE = " <sub>(upstream description)</sub>", " <sub>(earlier upstream description)</sub>"
ZH_UP, ZH_STALE, ZH_MACHINE = " <sub>(项目自述)</sub>", " <sub>(项目旧自述)</sub>", " <sub>(机翻)</sub>"
EN_MODEL, ZH_MODEL = " <sub>(written by a model)</sub>", " <sub>(模型撰写)</sub>"


def entry(**extra) -> dict:
    return {"summary": "Routes tickets.", "summary_zh": "路由工单。", **extra}


class OneDefinitionTest(unittest.TestCase):
    def test_values_labels_and_writer_agree(self):
        enum = SCHEMA["properties"]["summary_source"]["enum"]
        self.assertEqual(list(_stats.SUMMARY_SOURCES), enum)
        self.assertEqual([item["key"] for item in TAXONOMY["summary_sources"]], enum)
        self.assertEqual(set(rows.SUMMARY_SOURCE_LABELS), set(enum))
        self.assertEqual(
            rows.MARKED_SOURCES,
            (refresh_metadata.UPSTREAM, refresh_metadata.UPSTREAM_STALE, refresh_metadata.MODEL_WRITTEN),
        )
        self.assertEqual(refresh_metadata.CURATED, enum[0])
        self.assertEqual(refresh_metadata.MODEL_WRITTEN, enum[-1])

    def test_model_written_labels_say_so(self):
        for item in TAXONOMY["summary_sources"]:
            with self.subTest(key=item["key"]):
                self.assertIs(item.get("zh_machine"), True)


class RowMarkTest(unittest.TestCase):
    def test_marks_by_source_and_language(self):
        cases = [
            # summary_source,              zh_machine, English suffix, Chinese suffix
            ("upstream-description",       True,  EN_UP,    ZH_UP + ZH_MACHINE),
            ("upstream-description",       False, EN_UP,    ZH_UP),
            ("upstream-description-stale", True,  EN_STALE, ZH_STALE + ZH_MACHINE),
            ("model-written",              True,  EN_MODEL, ZH_MODEL + ZH_MACHINE),
            ("model-written",              False, EN_MODEL, ZH_MODEL),
            ("curated",                    True,  "",       ZH_MACHINE),
            ("curated",                    False, "",       ""),
            (None,                         True,  "",       ZH_MACHINE),
            (None,                         False, "",       ""),
        ]
        for source, machine, en, zh in cases:
            with self.subTest(source=source, zh_machine=machine):
                row = entry(zh_machine=machine)
                if source:
                    row["summary_source"] = source
                self.assertEqual(rows.summary_of(row, "en"), "Routes tickets." + en)
                self.assertEqual(rows.summary_of(row, "zh"), "路由工单。" + zh)

    def test_every_labelled_row_is_marked_on_every_pattern_page(self):
        catalog = json.loads(build_readme.CATALOG.read_text(encoding="utf-8"))
        labelled = [e for e in catalog if e.get("summary_source") in rows.MARKED_SOURCES]
        self.assertGreater(len(labelled), 500, "the backfill labelled the bulk-pass summaries")
        expected = sum(len(e["patterns"]) for e in labelled)
        for pack, marks in ((strings.EN, (EN_UP, EN_STALE, EN_MODEL)), (strings.ZH, (ZH_UP, ZH_STALE, ZH_MODEL))):
            with self.subTest(lang=pack["lang_code"]):
                found = 0
                for key, members in build_readme.group_by_pattern(catalog).items():
                    if members:
                        page = build_readme.render_page(key, members, pack)
                        found += sum(page.count(mark) for mark in marks)
                self.assertEqual(found, expected)


class ReadmeTextTest(unittest.TestCase):
    STATS = {"summary_upstream": 7, "summary_upstream_stale": 2, "summary_curated": 3, "summary_model_written": 5,
             "summary_unlabelled": 11}

    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads(build_readme.CATALOG.read_text(encoding="utf-8"))
        cls.retired = json.loads(build_readme.RETIRED.read_text(encoding="utf-8"))
        real = _stats.compute()
        with mock.patch.object(_stats, "compute", return_value={**real, **cls.STATS}):
            cls.readmes = {
                pack["lang_code"]: build_readme.render(copy.deepcopy(cls.catalog), copy.deepcopy(cls.retired), pack)
                for pack in (strings.EN, strings.ZH)
            }

    def test_the_counts_and_both_marks_are_explained(self):
        en = self.readmes["en"]
        self.assertIn("**Whose words the summaries are** — 7 summaries are the linked project's own GitHub", en)
        self.assertIn("marked *(upstream description)*; 2 are marked *(earlier upstream description)*", en)
        self.assertIn("3 summaries are marked as written for this catalogue by a person, 5 were written for it by a "
                      "model and are marked *(written by a model)*, and 11 carry no record", en)
        zh = self.readmes["zh"]
        self.assertIn("**摘要是谁的文字** —— 7 条摘要的英文原文", zh)
        self.assertIn("标为 *(项目自述)*；2 条标为 *(项目旧自述)*", zh)
        self.assertIn("3 条摘要标明由人为本目录撰写，5 条由模型为本目录撰写并标为 *(模型撰写)*，11 条未作记录", zh)

    def test_the_licence_paragraph_says_the_dedication_does_not_cover_them(self):
        self.assertIn(
            "Summaries marked *(upstream description)* or *(earlier upstream description)* are the linked "
            "projects' own words, which that dedication does not cover",
            self.readmes["en"],
        )
        self.assertIn("记录了各自声明的内容。标有 *(项目自述)* 或 *(项目旧自述)* 的摘要", self.readmes["zh"])

    def test_model_written_chinese_is_marked(self):
        for key in ("verified_summaries", "license_summaries"):
            with self.subTest(key=key):
                self.assertIn(key, strings.ZH_MACHINE)
        zh = self.readmes["zh"]
        for fragment in ("只有人才能把摘要标为人写的。 <sub>(机翻)</sub>", "（见[来源与许可](docs/sources.md#licences)）。 <sub>(机翻)</sub>"):
            self.assertIn(fragment, zh)
        self.assertNotIn("机翻", "\n".join(l for l in self.readmes["en"].splitlines() if "Whose words" in l or "dedication" in l))


class LicenceStatementTest(unittest.TestCase):
    """docs/sources.md's row-licences block, from counts."""

    def stats(self, **changes):
        return {
            "entries": 20, "summary_upstream": 12, "summary_upstream_stale": 1, "summary_curated": 2,
            "summary_model_written": 1, "summary_unlabelled": 4, "summary_upstream_zh_machine": 13, **changes,
        }

    def test_it_counts_whose_words_they_are(self):
        text = build_docs.row_licences_block(self.stats(), [{"license": "CC0-1.0"}] * 20)
        self.assertIn("12 of the 20 summaries in `catalog.json` are the linked project's own GitHub description", text)
        self.assertIn("1 more were taken from such a description and no longer match it", text)
        self.assertIn("the copyright in them is theirs: this repository does not dedicate them under `CC0-1.0`", text)
        self.assertIn("13 of their Chinese counterparts are machine translations", text)
        # The Chinese README says the translations are outside the dedication
        # too; the licence statement says the same.
        self.assertIn("this repository does not dedicate it under `CC0-1.0` either", text)
        self.assertIn("not a summary labelled as the project's own description or the Chinese translation of one", text)
        self.assertIn("*(upstream description)* or *(earlier upstream description)*", text)
        self.assertIn("2 summaries are marked `curated`: written for this catalogue by a person", text)
        self.assertIn("1 are marked `model-written`: written for it by a model, and marked *(written by a model)*", text)
        self.assertIn("The other 4 carry no `summary_source`", text)
        self.assertIn("Every row's `license` field is `CC0-1.0`. It covers the row's structured metadata", text)
        # The sentence I21 exists to remove.
        self.assertNotIn("no descriptive text was inherited", text)

    def test_nothing_quoted_says_nothing_about_quoting(self):
        text = build_docs.row_licences_block(
            self.stats(summary_upstream=0, summary_upstream_stale=0, summary_unlabelled=17), [{"license": "CC0-1.0"}] * 20
        )
        self.assertNotIn("copyright", text)
        self.assertIn("The other 17 carry no `summary_source`", text)

    def test_a_cc_by_row_is_still_counted(self):
        text = build_docs.row_licences_block(self.stats(), [{"license": "CC0-1.0"}] * 19 + [{"license": "CC-BY-4.0"}])
        self.assertIn("19 rows are `CC0-1.0`; 1 are `CC-BY-4.0`", text)
        self.assertIn("Either way the field covers the row's structured metadata", text)

    def test_the_real_counts_add_up(self):
        s = _stats.compute()
        total = (s["summary_upstream"] + s["summary_upstream_stale"] + s["summary_curated"]
                 + s["summary_model_written"] + s["summary_unlabelled"])
        self.assertEqual(total, s["entries"])
        self.assertLessEqual(s["summary_upstream_zh_machine"], s["summary_upstream"] + s["summary_upstream_stale"])

    def test_the_published_page_is_the_generated_one(self):
        page = (ROOT / "docs" / "sources.md").read_text(encoding="utf-8")
        self.assertNotIn("no descriptive text was inherited", page)


if __name__ == "__main__":
    unittest.main()
