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

STATS = {"entries": 12_345, "link_ok": 12_001, "evidence_rows": 9_876}
SVG_NS = "{http://www.w3.org/2000/svg}"


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
            patch.object(build_readme, "START_HERE", []),
        ):
            readme = build_readme.render([self.ENTRY], [], strings, "2026-09-25")
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
        self.assertIn("12,345 public resources", cover.description("en", STATS))
        self.assertIn("not current link availability", cover.description("en", STATS))


if __name__ == "__main__":
    unittest.main()
