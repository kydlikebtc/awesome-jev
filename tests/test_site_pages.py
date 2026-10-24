"""The plain pages the Pages deploy writes beside the app (P4, P5; since
2026-10-24): one per decision pattern in each language, what's new week by
week with an Atom feed in each language, and sitemap.xml (scripts/site_pages.py).

These tests build the pages in memory from made-up rows and from the real
catalogue's source files. lint_docs' rules for site pages read only tracked
files, so they never see these; here the pages are written to a scratch
directory and held to the same rules. Nothing here reads a generated file.
"""

from __future__ import annotations

import datetime as dt
import html
import json
import pathlib
import posixpath
import random
import re
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import _stats  # noqa: E402
import lint_docs  # noqa: E402
import site_pages  # noqa: E402

ATOM = "{http://www.w3.org/2005/Atom}"
SITEMAP = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
TAXONOMY = json.loads((ROOT / "taxonomy.json").read_text())
LABELS = site_pages.Labels(TAXONOMY)

PATTERNS = [
    {"key": "tool-selection", "en": "Tool selection", "zh": "工具选择", "blurb_en": "Which tool next.", "blurb_zh": "下一步用哪个工具。"},
    {"key": "safety-gating", "en": "Safety gating", "zh": "安全闸门", "blurb_en": "Let an action through?", "blurb_zh": "是否放行。"},
    {"key": "overview", "en": "Overview", "zh": "概览", "blurb_en": "Surveys the space.", "blurb_zh": "综述。"},
]


def row(slug: str, **fields) -> dict:
    base = {
        "slug": slug,
        "title": slug.title(),
        "summary": f"{slug} summary",
        "summary_zh": f"{slug} 摘要",
        "url": f"https://github.com/o/{slug}",
        "kind": "project",
        "patterns": ["tool-selection"],
        "first_seen": "2025-03-04",
    }
    return {key: value for key, value in {**base, **fields}.items() if value is not None}


# The catalogue opens in the week of Monday 2025-03-03; two rows come in the
# week of 2025-03-10 (one on its Sunday) and one is retired in the week after.
CATALOG = [
    row("alpha", official=True, has_code=True, stars=5),
    row("beta", first_seen="2025-03-05", has_code=True, stars=1200),
    row("gamma", first_seen="2025-03-12", has_code=True, stars=40),
    row("delta", first_seen="2025-03-16", patterns=["safety-gating"], flags=["not-jev"]),
    row("overview-unread", first_seen="2025-03-05", patterns=["overview"], has_code=True),
    row("overview-article", first_seen="2025-03-05", patterns=["overview"], kind="article"),
    row("undated", first_seen=None),
]
RETIRED = [
    row("gone", first_seen="2025-03-04", notes="Retired 2025-03-18: the repository was deleted.",
        notes_zh="2025-03-18 退役：仓库已删除。"),
]


def build(catalog=CATALOG, retired=RETIRED, patterns=PATTERNS) -> dict[str, str]:
    return site_pages.pages(catalog, retired, patterns, TAXONOMY)


def ids(text: str) -> list[str]:
    return re.findall(r'<li id="([^"]+)"', text)


class PagesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = build()

    def test_one_page_per_pattern_and_language_then_what_s_new_the_feeds_and_the_sitemap(self):
        expected = {"patterns/index.html", "new.html", "new.zh.html", "feed.xml", "feed.zh.xml", "sitemap.xml"}
        expected |= {f"patterns/{p['key']}{suffix}.html" for p in PATTERNS for suffix in ("", ".zh")}
        self.assertEqual(set(self.files), expected)
        self.assertEqual(
            {rel for rel in self.files if "/" not in rel and rel != "sitemap.xml"} | {"sitemap.xml"},
            set(site_pages.TOP_FILES),
        )

    def test_two_builds_from_the_same_rows_in_any_order_write_the_same_bytes(self):
        shuffled = CATALOG[:]
        random.Random(7).shuffle(shuffled)
        self.assertEqual(build(catalog=shuffled), self.files)

    def test_no_date_appears_but_the_catalogue_s(self):
        today = dt.date.today().isoformat()
        for rel, text in self.files.items():
            self.assertNotIn(today, text, rel)
            for day in re.findall(r"\d{4}-\d{2}-\d{2}", text):
                self.assertTrue(day.startswith("2025-03-"), f"{rel}: {day}")

    def test_rows_come_in_the_catalogue_s_order(self):
        # Official first, then rows with code by stars, then the rest.
        self.assertEqual(ids(self.files["patterns/tool-selection.html"]), ["alpha", "beta", "gamma", "undated"])

    def test_rows_nobody_has_read_against_the_patterns_come_last_under_their_own_heading(self):
        text = self.files["patterns/overview.html"]
        self.assertEqual(ids(text), ["overview-article", "overview-unread"])
        self.assertLess(text.index('id="overview-article"'), text.index(site_pages.STRINGS["en"]["unindexed"]))
        self.assertLess(text.index(site_pages.STRINGS["en"]["unindexed"]), text.index('id="overview-unread"'))
        self.assertNotIn(site_pages.STRINGS["en"]["unindexed"], self.files["patterns/tool-selection.html"])

    def test_each_pattern_page_counts_the_rows_the_stats_count(self):
        for key, n in _stats.pattern_tally(CATALOG, PATTERNS).items():
            code = sum(1 for e in CATALOG if key in e["patterns"] and e.get("has_code"))
            lede = site_pages.STRINGS["en"]["pattern_lede"].format(n=n, code=code)
            self.assertIn(html.escape(lede), self.files[f"patterns/{key}.html"], key)
            self.assertEqual(len(ids(self.files[f"patterns/{key}.zh.html"])), n, key)

    def test_a_row_that_is_no_example_is_marked_and_the_note_names_its_flags(self):
        text = self.files["patterns/safety-gating.html"]
        self.assertIn(f'<span class="caveat">{LABELS.name("flags", "not-jev", "en")}</span>', text)
        for flag in site_pages.query.DISQUALIFYING:
            self.assertIn(f"“{LABELS.name('flags', flag, 'en')}”", text)
            self.assertIn(f"「{LABELS.name('flags', flag, 'zh')}」", self.files["patterns/safety-gating.zh.html"])

    def test_stars_are_grouped_in_thousands(self):
        self.assertIn("★1,200", self.files["patterns/tool-selection.html"])
        self.assertNotIn("★1200", self.files["patterns/tool-selection.html"])

    def test_the_chinese_page_gives_the_chinese_summary_and_marks_what_the_site_marks(self):
        rows = [
            row("copied", summary_source="upstream-description", summary_zh="抄来的摘要", zh_machine=True),
            row("english-only", summary_zh=None),
        ]
        files = build(catalog=rows, retired=[])
        zh, en = files["patterns/tool-selection.zh.html"], files["patterns/tool-selection.html"]
        mark = LABELS.name("summary_sources", "upstream-description", "zh")
        self.assertIn(f'抄来的摘要<span class="mark">{mark}</span><span class="mark">机翻</span>', zh)
        self.assertIn("english-only summary", zh)
        self.assertNotIn("机翻", en)
        self.assertIn(f'<span class="mark">{LABELS.name("summary_sources", "upstream-description", "en")}</span>', en)

    def test_each_language_links_the_other(self):
        en, zh = self.files["patterns/safety-gating.html"], self.files["patterns/safety-gating.zh.html"]
        self.assertIn(f'<link rel="alternate" hreflang="zh-CN" href="{site_pages.SITE_URL}patterns/safety-gating.zh.html" />', en)
        self.assertIn('<a href="../patterns/safety-gating.zh.html" hreflang="zh-CN" lang="zh-CN">中文</a>', en)
        self.assertIn('<a href="../patterns/safety-gating.html" hreflang="en" lang="en">English</a>', zh)
        self.assertIn('<html lang="zh-CN">', zh)
        self.assertIn(f'<link rel="canonical" href="{site_pages.SITE_URL}new.zh.html" />', self.files["new.zh.html"])


class EscapingTest(unittest.TestCase):
    """Titles, summaries and notes are other people's words."""

    HOSTILE = '<script>alert(1)</script>"><img src=x onerror=alert(2)>&'

    def setUp(self):
        self.files = build(
            catalog=[
                row("hostile", title=self.HOSTILE, summary=self.HOSTILE, summary_zh=self.HOSTILE,
                    first_seen="2025-03-12"),
                row("scheme", url="javascript:alert(3)", first_seen="2025-03-12"),
                row("opener"),
            ],
            retired=[row("gone", title=self.HOSTILE, notes=f"Retired 2025-03-12: {self.HOSTILE}")],
        )

    def test_no_row_text_becomes_markup(self):
        for rel, text in self.files.items():
            self.assertNotIn("<script", text, rel)
            self.assertNotIn("<img", text, rel)
        page = self.files["patterns/tool-selection.html"]
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;&quot;&gt;&lt;img src=x onerror=alert(2)&gt;&amp;", page)

    def test_the_feeds_parse_with_the_hostile_text_inside(self):
        for name in ("feed.xml", "feed.zh.xml"):
            feed = ET.fromstring(self.files[name])
            content = "".join(e.findtext(f"{ATOM}content") or "" for e in feed.iter(f"{ATOM}entry"))
            self.assertIn("&lt;script&gt;", content, name)

    def test_only_a_web_address_becomes_a_link(self):
        self.assertNotIn("javascript:", "".join(self.files.values()))
        self.assertIn("<h3>Scheme</h3>", self.files["patterns/tool-selection.html"])
        for url in ("javascript:alert(1)", "data:text/html,x", " https://x.test/", None, 3):
            self.assertIsNone(site_pages.href(url), url)
        self.assertEqual(site_pages.href('https://x.test/?a=1&b="2"'), "https://x.test/?a=1&amp;b=&quot;2&quot;")


class WeeksTest(unittest.TestCase):
    def test_a_week_starts_on_monday(self):
        self.assertEqual(site_pages.week_of("2025-03-10"), "2025-03-10")
        self.assertEqual(site_pages.week_of("2025-03-16"), "2025-03-10")
        self.assertEqual(site_pages.week_of("2025-03-17"), "2025-03-17")

    def test_a_retired_row_s_day_is_the_one_its_notes_open_with(self):
        self.assertEqual(site_pages.retired_on({"notes": "Retired 2025-03-18: gone."}), "2025-03-18")
        self.assertIsNone(site_pages.retired_on({"notes": "Gone. Retired 2025-03-18."}))
        self.assertIsNone(site_pages.retired_on({"notes": "Retired 2025-02-30: no such day."}))
        self.assertIsNone(site_pages.retired_on({}))

    def test_weeks_run_newest_first_with_their_last_day(self):
        weeks = site_pages.weeks(CATALOG, RETIRED)
        self.assertEqual([w["week"] for w in weeks], ["2025-03-17", "2025-03-10", "2025-03-03"])
        self.assertEqual([w["updated"] for w in weeks], ["2025-03-18", "2025-03-16", "2025-03-05"])
        self.assertEqual([w["opening"] for w in weeks], [False, False, True])
        self.assertEqual([e["slug"] for e in weeks[1]["added"]], ["gamma", "delta"])
        self.assertEqual([e["slug"] for e in weeks[0]["retired"]], ["gone"])
        self.assertNotIn("undated", [e["slug"] for w in weeks for e in w["added"]])

    def test_the_opening_week_is_counted_not_listed(self):
        text = build()["new.html"]
        self.assertIn(site_pages.STRINGS["en"]["opened"].format(n=4), text)
        self.assertEqual(ids(text), ["gone", "gamma", "delta"])
        self.assertIn(site_pages.STRINGS["en"]["week_counts"].format(added=2, retired=0), text)

    def test_what_s_new_shows_the_latest_weeks_only(self):
        rows = [row(f"r{i}", first_seen=(dt.date(2025, 1, 6) + dt.timedelta(weeks=i)).isoformat())
                for i in range(site_pages.WEEKS_SHOWN + 3)]
        files = build(catalog=rows, retired=[])
        self.assertEqual(files["new.html"].count('<h2 id="w'), site_pages.WEEKS_SHOWN)
        self.assertEqual(len(ET.fromstring(files["feed.xml"]).findall(f"{ATOM}entry")), site_pages.WEEKS_SHOWN)
        self.assertIn('id="r28"', files["new.html"])
        self.assertNotIn('id="r2"', files["new.html"])

    def test_an_empty_catalogue_says_so(self):
        files = build(catalog=[], retired=[])
        self.assertIn(site_pages.STRINGS["en"]["nothing"], files["new.html"])
        self.assertIn("<updated>1970-01-01T00:00:00Z</updated>", files["feed.xml"])


class FeedTest(unittest.TestCase):
    def test_each_feed_is_atom_with_one_entry_a_week(self):
        files = build()
        for lang in site_pages.LANGS:
            feed = ET.fromstring(files[site_pages.feed_path(lang)])
            self.assertEqual(feed.tag, f"{ATOM}feed")
            self.assertEqual(feed.findtext(f"{ATOM}updated"), "2025-03-18T00:00:00Z")
            self.assertEqual(feed.findtext(f"{ATOM}id"), site_pages.SITE_URL + site_pages.feed_path(lang))
            entries = feed.findall(f"{ATOM}entry")
            self.assertEqual(len(entries), 3)
            page = site_pages.SITE_URL + site_pages.new_path(lang)
            self.assertEqual([e.findtext(f"{ATOM}id") for e in entries],
                             [f"{page}#w2025-03-17", f"{page}#w2025-03-10", f"{page}#w2025-03-03"])
            for entry in entries:
                self.assertEqual(entry.find(f"{ATOM}content").get("type"), "html")
                self.assertTrue(entry.findtext(f"{ATOM}title"))
            self.assertIn("Gamma", entries[1].findtext(f"{ATOM}content"))
            # The opening week names no row.
            self.assertNotIn("Alpha", entries[2].findtext(f"{ATOM}content"))

    def test_a_long_week_lists_the_first_rows_and_points_at_the_page(self):
        all_weeks = site_pages.weeks(CATALOG, RETIRED)
        feed = ET.fromstring(site_pages.feed(all_weeks, "en", LABELS, entry_rows=1))
        content = feed.findall(f"{ATOM}entry")[1].findtext(f"{ATOM}content")
        self.assertIn("Gamma", content)
        self.assertNotIn("Delta", content)
        self.assertIn(site_pages.STRINGS["en"]["more"].format(n=1), content)


class SitemapTest(unittest.TestCase):
    def test_the_sitemap_lists_the_app_and_every_page(self):
        files = build()
        urls = [loc.text for loc in ET.fromstring(files["sitemap.xml"]).iter(f"{SITEMAP}loc")]
        pages = {rel for rel in files if rel.endswith(".html") and rel != "patterns/index.html"}
        self.assertEqual(sorted(urls), sorted({site_pages.SITE_URL, site_pages.SITE_URL + "patterns/"}
                                              | {site_pages.SITE_URL + rel for rel in pages}))
        self.assertEqual(len(urls), len(set(urls)))


class SiteRulesTest(unittest.TestCase):
    """The rules lint_docs holds the committed site pages to."""

    @classmethod
    def setUpClass(cls):
        cls.files = build()

    def lint(self, check) -> list[str]:
        pages = {rel: text for rel, text in self.files.items() if rel.endswith(".html")}
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            for rel, text in pages.items():
                (root / "site" / rel).parent.mkdir(parents=True, exist_ok=True)
                (root / "site" / rel).write_text(text, encoding="utf-8")
            listed = [f"site/{rel}" for rel in pages]
            with patch.object(lint_docs, "ROOT", root), patch.object(lint_docs, "tracked", return_value=listed):
                return check()

    def test_no_page_loads_from_another_host(self):
        self.assertEqual(self.lint(lint_docs.check_site_origin), [])

    def test_every_font_stack_names_the_system_cjk_fonts(self):
        self.assertTrue(lint_docs.CJK.search(self.files["patterns/index.html"]))
        self.assertEqual(self.lint(lint_docs.check_cjk_fallback), [])

    def test_no_page_runs_script(self):
        for rel, text in self.files.items():
            self.assertNotIn("<script", text, rel)

    def test_every_link_within_the_site_lands_on_a_file_it_serves(self):
        served = set(self.files) | {"index.html", "favicon.svg", "fonts/fonts.css"}
        for rel in ("favicon.svg", "fonts/fonts.css", "index.html"):
            self.assertTrue((ROOT / "site" / rel).is_file(), rel)
        for rel, text in self.files.items():
            if not rel.endswith(".html"):
                continue
            for link in re.findall(r'href="([^"]*)"', text):
                if link.startswith(("https://", "http://", "#")):
                    continue
                target = posixpath.join(posixpath.dirname(rel), link.split("#")[0].split("?")[0])
                if target == "" or target.endswith("/"):
                    target = posixpath.join(target, "index.html")
                self.assertIn(posixpath.normpath(target), served, f"{rel} links {link}")


class WriteTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.site = pathlib.Path(tmp.name) / "site"
        self.site.mkdir()
        (self.site / "index.html").write_text("app")
        self.files = build()
        site_pages.write_pages(self.site, self.files)

    def test_a_fresh_build_has_no_problems(self):
        self.assertEqual(site_pages.page_problems(self.site, self.files), [])

    def test_the_writer_clears_old_pages_and_leaves_the_app(self):
        (self.site / "patterns" / "retired-pattern.html").write_text("old")
        site_pages.write_pages(self.site, self.files)
        self.assertFalse((self.site / "patterns" / "retired-pattern.html").exists())
        self.assertEqual((self.site / "index.html").read_text(), "app")

    def test_a_missing_page(self):
        (self.site / "new.zh.html").unlink()
        self.assertEqual(site_pages.page_problems(self.site, self.files),
                         ["site/new.zh.html is missing; run assemble_site.py"])

    def test_a_page_for_no_pattern(self):
        (self.site / "patterns" / "retired-pattern.html").write_text("old")
        found = site_pages.page_problems(self.site, self.files)
        self.assertEqual(len(found), 1)
        self.assertIn("site/patterns/retired-pattern.html is no page a rebuild writes", found[0])

    def test_a_stale_page(self):
        (self.site / "feed.xml").write_text(self.files["feed.xml"].replace("Gamma", "Gammon"))
        found = site_pages.page_problems(self.site, self.files)
        self.assertEqual(len(found), 1)
        self.assertIn("site/feed.xml is stale", found[0])


class RealCatalogueTest(unittest.TestCase):
    """The pages built from the catalogue's own source files."""

    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "catalog.json").read_text())
        cls.retired = json.loads((ROOT / "retired.json").read_text())
        cls.patterns = json.loads((ROOT / "patterns.json").read_text())["patterns"]
        cls.files = site_pages.pages(cls.catalog, cls.retired, cls.patterns, TAXONOMY)

    def test_every_pattern_has_a_page_in_each_language_holding_its_rows(self):
        tally = _stats.pattern_tally(self.catalog, self.patterns)
        for pattern in self.patterns:
            for lang in site_pages.LANGS:
                rows = ids(self.files[site_pages.pattern_path(pattern["key"], lang)])
                self.assertEqual(len(rows), tally[pattern["key"]], pattern["key"])
                self.assertEqual(len(rows), len(set(rows)), pattern["key"])

    def test_every_retired_row_names_the_day_it_was_retired(self):
        # A row with no such day would never reach what's new.
        self.assertEqual([e["slug"] for e in self.retired if not site_pages.retired_on(e)], [])

    def test_the_feeds_parse(self):
        for lang in site_pages.LANGS:
            ET.fromstring(self.files[site_pages.feed_path(lang)])
        ET.fromstring(self.files["sitemap.xml"])


class WiringTest(unittest.TestCase):
    def test_every_page_is_ignored_by_git(self):
        for rel in (*site_pages.TOP_FILES, "patterns/index.html", "patterns/overview.zh.html"):
            done = subprocess.run(["git", "check-ignore", "-q", f"site/{rel}"], cwd=ROOT)
            self.assertEqual(done.returncode, 0, f"site/{rel} is built at deploy and must never be committed")

    def test_pages_redeploys_when_the_page_writer_changes(self):
        text = (ROOT / ".github" / "workflows" / "pages.yml").read_text()
        paths = text.split("    paths:\n", 1)[1].split("\n  workflow_dispatch:", 1)[0]
        self.assertIn('      - "scripts/site_pages.py"\n', paths)

    def test_the_app_links_the_pages_and_offers_the_feeds(self):
        text = (ROOT / "site" / "index.html").read_text()
        for lang in site_pages.LANGS:
            title = site_pages.STRINGS[lang]["feed_title"]
            self.assertRegex(
                text, rf'<link rel="alternate" type="application/atom\+xml"[^>]*title="{re.escape(title)}" '
                      rf'href="{re.escape(site_pages.feed_path(lang))}" />'
            )
        self.assertIn('href="patterns/"', text)
        self.assertIn(f'data-href-en="{site_pages.new_path("en")}" data-href-zh="{site_pages.new_path("zh")}"', text)
        self.assertIn(f'data-href-zh="{site_pages.feed_path("zh")}"', text)


if __name__ == "__main__":
    unittest.main()
