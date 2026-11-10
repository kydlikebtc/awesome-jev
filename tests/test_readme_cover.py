"""Regression checks for the README hero and header; no network access."""

from __future__ import annotations

import pathlib
import re
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from unittest.mock import patch

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

import _stats
import build_readme
import build_readme_cover as cover
from readme import sections

STATS = {"products": 12_345, "makers": 12_001, "call_site_rows": 9_876}
SVG_NS = "{http://www.w3.org/2000/svg}"
# A feed as readme.board.hero hands one over, with words nobody here chose:
# a title and a line far too long for any card, and Chinese ones.
FEED = {
    "heading": "THIS WEEK · 2026-W46 · VOTES OPEN",
    "footer": "VOTES AND EVIDENCE SIDE BY SIDE · NEVER ADDED",
    "cards": [
        {"mark": "▲", "count": None, "rank": None, "title": "agent-desktop",
         "line": "Reads the accessibility tree and decides the next click", "tier": "person"},
        {"mark": "▲", "count": "1,234", "rank": "#1", "title": "x" * 200, "line": "y " * 200, "tier": "model"},
        {"mark": "★", "count": "+56", "rank": None, "title": "星标涨得最快的产品，名字很长很长很长很长很长很长",
         "line": "一句话", "tier": None},
    ],
}
FEEDS = {"en": FEED, "zh": FEED}


def github_pick(
    sources: list[tuple[str, str]], fallback: str, mode: str, os_scheme: str, width: int
) -> str:
    """Replay how github.com chooses a README <picture> source.

    With a fixed theme ("light" or "dark"), GitHub's <themed-picture> replaces
    the whole media query of every source that names a colour scheme, width
    condition included: sources of the reader's theme always match, the other
    theme's never do. With "auto" nothing is rewritten, and a query that is not
    rewritten sees the operating system's scheme. The first match wins. Media
    syntax this replay does not model fails loudly rather than guessing.
    """

    def theme_of(media: str) -> str | None:
        for theme in ("light", "dark"):  # GitHub checks light first
            if f"prefers-color-scheme: {theme}" in media:
                return theme
        return None

    def matches(media: str) -> bool:
        if re.sub(r"\([^)]*\)", "", media).replace("and", "").strip():
            raise AssertionError(f"github_pick models only (…) and (…) queries: {media!r}")
        for condition in re.findall(r"\(([^)]*)\)", media):
            feature, value = (part.strip() for part in condition.split(":"))
            if feature == "prefers-color-scheme":
                ok = value == os_scheme
            elif feature == "max-width":
                ok = width <= int(value.removesuffix("px"))
            elif feature == "min-width":
                ok = width >= int(value.removesuffix("px"))
            else:
                raise AssertionError(f"github_pick does not model {feature!r}")
            if not ok:
                return False
        return True

    for media, srcset in sources:
        theme = theme_of(media)
        if mode != "auto" and theme is not None:
            if theme == mode:
                return srcset
            continue
        if matches(media):
            return srcset
    return fallback


class CoverAssetTests(unittest.TestCase):
    def test_every_language_theme_and_width_is_rendered(self):
        expected = {
            f"readme-cover-{lang}-{theme}{suffix}.svg"
            for lang in ("en", "zh")
            for theme in ("light", "dark")
            for suffix in ("", "-mobile")
        }
        self.assertEqual(set(cover.rendered_covers(STATS)), expected)

    def test_counts_come_from_the_stats_snapshot(self):
        for name, svg in cover.rendered_covers(STATS).items():
            for number in ("12,345", "12,001", "9,876"):
                self.assertIn(number, svg, name)

    def test_each_theme_is_drawn_for_its_own_canvas(self):
        for lang in ("en", "zh"):
            for render in (cover.cover, cover.mobile_cover):
                light, dark = render(lang, "light", STATS), render(lang, "dark", STATS)
                self.assertIn(f'fill="{cover.THEMES["light"]["canvas"]}"', light)
                self.assertIn(f'fill="{cover.THEMES["dark"]["canvas"]}"', dark)
                self.assertNotIn(cover.THEMES["dark"]["fg"], light)
                self.assertNotIn(cover.THEMES["light"]["fg"], dark)

    def test_unknown_theme_is_rejected(self):
        with self.assertRaises(ValueError):
            cover.cover("en", "sepia", STATS)

    def test_covers_are_self_contained_and_well_formed(self):
        # An SVG shown through <img> cannot fetch fonts, images or scripts, and
        # anything that tries fails silently on some platforms and not others.
        for name, svg in cover.rendered_covers(STATS).items():
            root = ET.fromstring(svg)
            self.assertEqual(root.tag, f"{SVG_NS}svg", name)
            for banned in (
                "<image",
                "<script",
                "foreignObject",
                "@import",
                "@font-face",
                "href=",
                "url(http",
            ):
                self.assertNotIn(banned, svg, f"{name} contains {banned}")
            ids = [element.get("id") for element in root.iter() if element.get("id")]
            self.assertEqual(len(ids), len(set(ids)), f"{name} repeats an id")

    def test_accessible_description_keeps_the_record_caveat(self):
        self.assertIn(
            "not current link availability", cover.cover("en", "light", STATS)
        )
        self.assertIn("不代表当前链接可用", cover.mobile_cover("zh", "dark", STATS))

    def test_copy_that_would_overrun_its_column_fails_the_build(self):
        longer = dict(
            cover.COPY["en"], title="Jev Decision Atlas and Field Guide to Everything"
        )
        with patch.dict(cover.COPY, {"en": longer}):
            with self.assertRaisesRegex(cover.CoverLayoutError, "title"):
                cover.cover("en", "light", STATS)

    def test_counts_can_grow_tenfold_without_overrunning(self):
        grown = {key: 123_456 for key in cover.METRICS}
        for lang in ("en", "zh"):
            for theme in cover.THEMES:
                cover.cover(lang, theme, grown)
                cover.mobile_cover(lang, theme, grown)

    def test_check_mode_names_exactly_the_stale_files(self):
        with tempfile.TemporaryDirectory() as directory:
            out = pathlib.Path(directory)
            cover.write_covers(STATS, out)
            self.assertEqual(cover.stale_covers(STATS, out), [])
            (out / "readme-cover-en-dark.svg").write_text("<svg/>", encoding="utf-8")
            (out / "readme-cover-zh-light-mobile.svg").unlink()
            self.assertEqual(
                cover.stale_covers(STATS, out),
                ["readme-cover-en-dark.svg", "readme-cover-zh-light-mobile.svg"],
            )


class FeedTests(unittest.TestCase):
    """The feed on the cover is the board as it stands, and nothing in it can
    stop the Monday run that regenerates the cover."""

    def test_a_products_words_are_clipped_never_failed(self):
        for lang in ("en", "zh"):
            for render in (cover.cover, cover.mobile_cover):
                svg = render(lang, "light", STATS, FEED)
                self.assertIn("agent-desktop", svg)
                self.assertIn("…", svg)
                self.assertNotIn("x" * 60, svg)
                self.assertIn("1,234", svg)
                self.assertIn("#1", svg)
                self.assertIn(FEED["heading"], svg)

    def test_clip_keeps_what_fits_and_cuts_the_rest(self):
        self.assertEqual(cover.clip("short", 14, 500), "short")
        self.assertEqual(cover.clip("two  words\nhere", 14, 500), "two words here")
        cut = cover.clip("a sentence that goes on for far too long to fit", 14, 120)
        self.assertTrue(cut.endswith("…"))
        self.assertLessEqual(cover.text_width(cut, 14), 120)
        self.assertEqual(cover.clip("wide", 14, 1), "…")

    def test_the_feed_comes_from_the_board_files(self):
        from readme import board

        feeds = cover.hero_feed()
        for lang in ("en", "zh"):
            with self.subTest(lang=lang):
                self.assertEqual(set(feeds[lang]), {"heading", "cards", "footer"})
                self.assertLessEqual(len(feeds[lang]["cards"]), board.HERO_CARDS)
                self.assertEqual(board.HERO_CARDS, cover.CARDS)
                for item in feeds[lang]["cards"]:
                    self.assertEqual(set(item), {"mark", "count", "rank", "title", "line", "tier"})
                self.assertIn(feeds[lang]["heading"], cover.cover(lang, "dark", STATS, feeds[lang]))

    def test_the_states_of_the_board(self):
        from readme import board

        row = {"slug": "alpha", "title": "Alpha", "summary": "Decides with Jev.", "summary_zh": "用 Jev 决定。",
               "url": "https://github.com/o/alpha", "kind": "project", "patterns": ["safety-gating"], "has_code": True}
        launch = {"product": "alpha", "status": "scheduled", "tagline": "One line", "issue": 1,
                  "submitted_by": "someone", "role": "hunter", "submitted_on": "2026-11-05"}
        running = {"week": "2026-W46", "status": "open", "launches": [{**launch, "discussion": 7}]}
        closed = {"week": "2026-W45", "status": "closed", "launches": [
            {**launch, "result": {"votes": 42, "counted": 40, "discounted": 2, "rank": 1}}]}
        cases = [
            ([running], "THIS WEEK · 2026-W46 · VOTES OPEN", {"mark": "▲", "count": None, "rank": None}),
            ([closed], "LAST WEEK · 2026-W45 · RESULTS", {"mark": "▲", "count": "40", "rank": "#1"}),
            ([{**running, "status": "scheduled"}], "NEXT WEEK · 2026-W46 · FILED", {"mark": "▲", "count": None, "rank": None}),
        ]
        for weeks, heading, expected in cases:
            with self.subTest(heading=heading), patch.object(board.launches, "weeks", return_value=weeks), \
                    patch.object(board.launches, "readings", return_value=[]):
                feed = board.hero([row], "en")
                self.assertEqual(feed["heading"], heading)
                self.assertEqual(len(feed["cards"]), 1)
                self.assertEqual({k: feed["cards"][0][k] for k in expected}, expected)
                self.assertEqual((feed["cards"][0]["title"], feed["cards"][0]["line"]), ("Alpha", "One line"))
        with patch.object(board.launches, "weeks", return_value=[]), \
                patch.object(board.launches, "readings", return_value=[]):
            feed = board.hero([row], "zh")
            self.assertEqual(feed["heading"], board.HERO["zh"]["steps"])
            self.assertEqual([c["tier"] for c in feed["cards"]], [None, None, None])
        before = {"date": "2026-10-28", "rows": [{"slug": "alpha", "stars": 10}]}
        after = {"date": "2026-11-04", "rows": [{"slug": "alpha", "stars": 60}]}
        with patch.object(board.launches, "weeks", return_value=[]), \
                patch.object(board.launches, "readings", return_value=[before, after]):
            feed = board.hero([row], "en")
            self.assertEqual(feed["heading"], board.HERO["en"]["rising"])
            self.assertEqual(feed["cards"][0]["count"], "+50")
            self.assertEqual(feed["cards"][0]["mark"], "★")


class HeroSelectionTests(unittest.TestCase):
    MODES = ("auto", "light", "dark")

    def test_each_reader_gets_the_cover_for_their_theme_and_width(self):
        for lang in ("en", "zh"):
            sources, fallback = (
                cover.picture_sources(lang),
                cover.asset_path(lang, "light"),
            )
            for mode in self.MODES:
                for os_scheme in ("light", "dark"):
                    for width in (390, 767, 768, 1280):
                        theme = os_scheme if mode == "auto" else mode
                        narrow = width < cover.HERO_BREAKPOINT
                        want = cover.asset_path(lang, theme, mobile=narrow)
                        if mode == "light" and narrow:
                            # The one case one <picture> cannot serve (see
                            # picture_sources): the desktop light cover, scaled.
                            want = cover.asset_path(lang, "light")
                        got = github_pick(sources, fallback, mode, os_scheme, width)
                        self.assertEqual(
                            got,
                            want,
                            f"{lang} mode={mode} os={os_scheme} width={width}",
                        )

    def test_a_desktop_reader_never_gets_the_phone_layout(self):
        # PR #16's order sent fixed-dark desktop readers the tall phone cover
        # stretched across the page.
        sources, fallback = cover.picture_sources("en"), cover.asset_path("en", "light")
        for mode in self.MODES:
            for os_scheme in ("light", "dark"):
                got = github_pick(sources, fallback, mode, os_scheme, 1280)
                self.assertNotIn("-mobile", got, f"mode={mode} os={os_scheme}")

    def test_colour_scheme_conditions_are_spelled_as_github_detects_them(self):
        # GitHub finds themed sources by substring; "(prefers-color-scheme:dark)"
        # would escape the rewrite and follow the operating system instead.
        for lang in ("en", "zh"):
            for media, _ in cover.picture_sources(lang):
                for condition in re.findall(r"\([^)]*color-scheme[^)]*\)", media):
                    self.assertRegex(condition, r"^\(prefers-color-scheme: (light|dark)\)$")

    def test_every_referenced_cover_is_a_rendered_asset(self):
        # A <source> whose file is missing shows a broken image; the <picture>
        # does not fall back to its <img>.
        rendered = cover.rendered_covers(STATS)
        for lang in ("en", "zh"):
            paths = [path for _, path in cover.picture_sources(lang)]
            for path in paths + [cover.asset_path(lang, "light")]:
                self.assertEqual((cover.ROOT / path).parent, cover.OUT, path)
                self.assertIn(pathlib.Path(path).name, rendered, path)


class ReadmeHeaderTests(unittest.TestCase):
    ENTRY = {
        "slug": "example",
        "title": "Example",
        "url": "https://example.com/repo",
        "summary": "A cited implementation, not a runtime test.",
        "summary_zh": "有调用点记录，未经运行测试。",
        "kind": "project",
        "patterns": ["tool-selection"],
        "license": "CC0-1.0",
    }

    def header(self, strings: dict) -> str:
        patterns = [{"key": "tool-selection"}]
        schema = {"properties": {"kind": {"enum": ["project"]}}}
        loaded = ([self.ENTRY], [], patterns, {"platforms": []}, schema)
        with patch.object(_stats, "load", return_value=loaded):
            stats = {**_stats.compute(), **STATS}
        with (
            patch.object(_stats, "compute", return_value=stats),
            patch.object(sections, "START_HERE", []),
        ):
            readme = build_readme.render([self.ENTRY], [], strings)
        return readme.split("\n## ", 1)[0]

    def test_hero_markup_uses_the_tested_source_order(self):
        for strings in (build_readme.EN, build_readme.ZH):
            lang = strings["lang_code"]
            head = self.header(strings)
            found = re.findall(r'<source media="([^"]+)" srcset="([^"]+)">', head)
            self.assertEqual(found, cover.picture_sources(lang))
            self.assertIn(f'<img src="{cover.asset_path(lang, "light")}"', head)
            self.assertIn('width="100%"', head)

    def test_entry_points_are_chips_that_never_wrap_inside(self):
        head = self.header(build_readme.EN)
        chips = re.findall(r'<a href="([^"]+)"><kbd>(.*?)</kbd></a>', head)
        self.assertEqual(
            [href for href, _ in chips],
            [
                f"{build_readme.SITE}launches.html",
                "https://github.com/kydlikebtc/awesome-jev/issues/new?template=launch.yml",
                f"{build_readme.SITE}?lang=en",
                f"{build_readme.SITE}?collection=first-call&amp;lang=en",
                f"{build_readme.SITE}?collection=build&amp;lang=en",
                f"{build_readme.SITE}?collection=measured&amp;lang=en",
                "README.zh-CN.md",
            ],
        )
        for _, label in chips:
            self.assertNotIn(" ", label, f"chip {label!r} can wrap inside")

    def test_counts_caveat_sits_under_the_chips_and_links_to_its_section(self):
        for strings in (build_readme.EN, build_readme.ZH):
            head = self.header(strings)
            caveat = f'<p align="center"><sub>{strings["badge_note"]}'
            self.assertIn(caveat, head)
            self.assertLess(head.index("<kbd>"), head.index(caveat))
            self.assertIn(f'href="#{build_readme.anchor(strings["verified_h"])}"', head)

    def test_alt_text_is_the_covers_own_description(self):
        for strings in (build_readme.EN, build_readme.ZH):
            head = self.header(strings)
            described = cover.description(strings["lang_code"], STATS)
            self.assertIn(f'alt="awesome-jev — {described}"', head)
        self.assertIn("12,345 products", cover.description("en", STATS))
        self.assertIn("not current link availability", cover.description("en", STATS))


if __name__ == "__main__":
    unittest.main()
