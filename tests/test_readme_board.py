"""The README's launch board as a feed, its week figure, and the folded
catalogue lists (2026-11-06); no network access."""

from __future__ import annotations

import pathlib
import re
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from unittest.mock import patch

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _stats
import build_readme
import build_readme_cover as cover
import build_readme_week as week
from readme import board, sections
from test_readme_cover import STATS, github_pick

SVG_NS = "{http://www.w3.org/2000/svg}"


def product(slug: str, url: str | None = None, **fields) -> dict:
    return {
        "slug": slug, "title": slug.title(), "summary": "Decides with Jev.", "summary_zh": "用 Jev 决定。",
        "url": url or f"https://github.com/owner-{slug}/{slug}", "kind": "project", "patterns": ["safety-gating"],
        "has_code": True, **fields,
    }


def launch(slug: str, **fields) -> dict:
    return {"product": slug, "status": "scheduled", "tagline": f"{slug} in one line", "issue": 1,
            "submitted_by": "someone", "role": "hunter", "submitted_on": "2026-11-05", **fields}


ROWS = [product("alpha"), product("beta", url="https://example.com/beta")]
RUNNING = {"week": "2026-W46", "status": "open", "launches": [launch("alpha", discussion=7), launch("beta", discussion=8)]}
FILED = {**RUNNING, "status": "scheduled"}
CLOSED = {"week": "2026-W45", "status": "closed", "launches": [
    launch("alpha", result={"votes": 42, "counted": 40, "discounted": 2, "rank": 1}),
    launch("beta", result={"votes": 1_234, "counted": 1_200, "discounted": 34, "rank": 2}),
]}
BEFORE = {"date": "2026-10-28", "rows": [{"slug": "alpha", "stars": 10}]}
AFTER = {"date": "2026-11-04", "rows": [{"slug": "alpha", "stars": 60}]}


def section(weeks: list[dict], snapshots: list[dict] = (), strings: dict = build_readme.EN) -> str:
    page = type("Page", (), {"strings": strings, "lang": strings["lang_code"], "catalog": ROWS})()
    with patch.object(board.launches, "weeks", return_value=weeks), \
            patch.object(board.launches, "readings", return_value=list(snapshots)):
        return "\n".join(board.this_weeks_launches(page))


class FeedTests(unittest.TestCase):
    """Each launch is one row of a table: its picture, its name and line, and
    a box with what counts in the board's state."""

    def test_a_running_week_is_a_table_with_a_vote_box_per_launch(self):
        text = section([RUNNING])
        self.assertEqual(text.count("<table>"), 1)
        self.assertEqual(text.count("<tr>"), 2)
        for number in (7, 8):
            self.assertIn(f'<a href="{board.launches.query.DISCUSSION}{number}"><b>▲</b><br><sub>VOTE</sub></a>', text)
        self.assertNotIn("votes", text.split("</table>")[0].split("<table>")[1])

    def test_the_picture_is_the_repository_owners_avatar_or_the_mark(self):
        text = section([RUNNING])
        self.assertIn(f'<img src="https://github.com/owner-alpha.png?size={board.THUMB * 2}" '
                      f'width="{board.THUMB}" height="{board.THUMB}" alt="Alpha">', text)
        self.assertIn(f'<img src="{board.NO_THUMB}"', text)
        self.assertTrue((cover.ROOT / board.NO_THUMB).is_file())

    def test_the_words_cell_is_fenced_so_github_renders_its_markdown(self):
        lines = section([RUNNING]).splitlines()
        for index, line in enumerate(lines):
            if line.startswith("**[") and "](" in line:
                self.assertEqual(lines[index - 2:index], ["<td>", ""])
                self.assertEqual(lines[index + 2:index + 4], ["", "</td>"])
                self.assertTrue(lines[index + 1].startswith("<sub>hunted by [someone](https://github.com/someone)"))

    def test_a_filed_week_says_the_monday_it_opens(self):
        text = section([FILED])
        self.assertEqual(text.count("<b>▲</b><br><sub>opens<br>11-09</sub>"), 2)
        self.assertNotIn("discussions/7", text)
        self.assertIn("<b>▲</b><br><sub>11-09<br>开榜</sub>", section([FILED], strings=build_readme.ZH))

    def test_a_closed_week_shows_medals_and_counted_votes(self):
        text = section([CLOSED])
        self.assertIn("<b>🥇&nbsp;40</b><br><sub>votes</sub>", text)
        self.assertIn("<b>🥈&nbsp;1,200</b><br><sub>votes</sub>", text)
        self.assertIn("▲ 42 votes, 40 counted", text)
        self.assertLess(text.index("🥇"), text.index("🥈"))

    def test_a_rank_nobody_voted_for_gets_no_medal(self):
        # 2026-W46 closed with no vote: its order was only the tie order.
        nobody = {**CLOSED, "launches": [
            launch("alpha", result={"votes": 0, "counted": 0, "discounted": 0, "rank": 1}),
            launch("beta", result={"votes": 1, "counted": 0.5, "discounted": 1, "rank": 2}),
        ]}
        text = section([nobody])
        self.assertNotIn("🥇", text)
        self.assertIn("<b>▲&nbsp;0</b><br><sub>votes</sub>", text)
        self.assertIn("<b>🥈&nbsp;0.5</b><br><sub>votes</sub>", text)

    def test_with_nothing_running_an_old_week_is_the_latest_results_not_last_week(self):
        text = section([CLOSED])
        self.assertIn("No launch is on the board this week.", text)
        self.assertIn("### 🏆 Last week: 2026-W45", text)
        self.assertLess(text.index("No launch is on the board this week."), text.index("<table>"))
        # The files' today in 2026-W47: no week was filed after 2026-W45.
        later = [{**ROWS[0], "first_seen": "2026-11-17"}, ROWS[1]]
        for strings, heading in ((build_readme.EN, "### Latest results: 2026-W45"),
                                 (build_readme.ZH, "### 最近一期结果：2026-W45")):
            page = type("Page", (), {"strings": strings, "lang": strings["lang_code"], "catalog": later})()
            with patch.object(board.launches, "weeks", return_value=[CLOSED]), \
                    patch.object(board.launches, "readings", return_value=[]):
                text = "\n".join(board.this_weeks_launches(page))
            self.assertIn(heading, text)
            self.assertNotIn("🏆", text)
        # A running week says nothing about a quiet week.
        self.assertNotIn("No launch is on the board this week.", section([CLOSED, {**RUNNING, "week": "2026-W46"}]))

    def test_rising_products_show_the_stars_they_gained(self):
        text = section([], [BEFORE, AFTER])
        self.assertIn("<b>★&nbsp;+50</b><br><sub>stars</sub>", text)
        self.assertIn("10 → 60 stars (+500%)", text)

    def test_products_come_first_then_how_the_board_works(self):
        for weeks in ([RUNNING], [FILED], [CLOSED], []):
            text = section(weeks, [BEFORE, AFTER])
            self.assertLess(text.index("<table>"), text.index("People vote with a thumbs-up"))
        self.assertLess(section([], [BEFORE, AFTER]).index("No launch is on the board yet"),
                        section([], [BEFORE, AFTER]).index("<table>"))

    def test_with_a_week_on_the_board_it_leads_and_rising_follows(self):
        for weeks in ([RUNNING], [FILED], [CLOSED, RUNNING]):
            text = section(weeks, [BEFORE, AFTER])
            self.assertLess(text.index("People vote with a thumbs-up"), text.index("★ Rising"))
            self.assertNotIn("New in the catalogue", text)

    def test_with_no_week_on_the_board_what_moves_daily_leads(self):
        # 2026-11-18: no launch was filed after 2026-W46. Rising, then the
        # catalogue's new products, then the old week, then how the board works.
        fresh = [product("gamma", first_seen="2026-11-17", stars=7, evidence={"path": "a.py", "read_on": "2026-11-17"}),
                 product("delta", first_seen="2026-11-16", stars=90),
                 product("old", first_seen="2026-11-02", stars=500)]
        catalog = ROWS + fresh
        for strings, new_h in ((build_readme.EN, "### New in the catalogue: 2026-W47"),
                               (build_readme.ZH, "### 本周新收录：2026-W47")):
            page = type("Page", (), {"strings": strings, "lang": strings["lang_code"], "catalog": catalog})()
            with patch.object(board.launches, "weeks", return_value=[CLOSED]), \
                    patch.object(board.launches, "readings", return_value=[BEFORE, AFTER]):
                text = "\n".join(board.this_weeks_launches(page))
            order = [text.index(strings["board_quiet"].split(".")[0].split("。")[0]),
                     text.index(strings["board_rising_h"].split(":")[0].split("：")[0]),
                     text.index(new_h), text.index("2026-W45"), text.index(strings["board_intro"][:12])]
            self.assertEqual(order, sorted(order), strings["lang_code"])
            new = text.split(new_h, 1)[1].split("###", 1)[0]
            # The person-read row first, then by stars; last week's rows are not this week's.
            self.assertLess(new.index("[Gamma]"), new.index("[Delta]"))
            self.assertNotIn("[Old]", new)
            self.assertIn("<b>11-16</b><br><sub>%s</sub>" % strings["box_new"], new)
            self.assertIn(strings["board_new_stars"].format(stars="90"), new)
            self.assertIn("template=launch.yml&product=delta", new)
            self.assertIn("2026-W45", text.split(new_h, 1)[1])
        # No week has ever opened: the same order, without results.
        page = type("Page", (), {"strings": build_readme.EN, "lang": "en", "catalog": catalog})()
        with patch.object(board.launches, "weeks", return_value=[]), \
                patch.object(board.launches, "readings", return_value=[BEFORE, AFTER]):
            text = "\n".join(board.this_weeks_launches(page))
        self.assertLess(text.index("No launch is on the board yet"), text.index("★ Rising"))
        self.assertLess(text.index("★ Rising"), text.index("New in the catalogue"))
        self.assertLess(text.index("New in the catalogue"), text.index("People vote with a thumbs-up"))


class WeekFigureTests(unittest.TestCase):
    def now(self, weeks: list[dict]) -> week.Now:
        with patch.object(board.launches, "weeks", return_value=weeks), \
                patch.object(board.launches, "readings", return_value=[]):
            return week.now_of(ROWS)

    def test_the_phase_comes_from_the_week_files(self):
        self.assertEqual(self.now([RUNNING]), week.Now("vote", "2026-W46"))
        self.assertEqual(self.now([FILED]), week.Now("filed", "2026-W46"))
        self.assertEqual(self.now([CLOSED]), week.Now("launch"))
        self.assertEqual(self.now([]), week.Now("launch"))
        # A running week and the week filed after it: votes are what is open.
        self.assertEqual(self.now([{**RUNNING, "week": "2026-W45"}, FILED]), week.Now("vote", "2026-W45"))

    def test_the_status_names_the_week_and_its_days(self):
        self.assertEqual(week.Now("vote", "2026-W46").status("en"), "2026-W46 · VOTES OPEN UNTIL SUNDAY 2026-11-15")
        self.assertEqual(week.Now("filed", "2026-W46").status("zh"), "2026-W46 已登记 · 2026-11-09（周一）开榜")
        self.assertIn("Now: TAKING LAUNCHES FOR NEXT WEEK.", week.alt_text("en", week.Now("launch")))

    def test_every_language_theme_and_width_is_drawn_and_self_contained(self):
        for now in (week.Now("launch"), week.Now("filed", "2026-W46"), week.Now("vote", "2026-W46")):
            drawn = week.rendered(now)
            self.assertEqual(set(drawn), {
                f"launch-week-{lang}-{theme}{suffix}.svg"
                for lang in ("en", "zh") for theme in ("light", "dark") for suffix in ("", "-mobile")
            })
            for name, svg in drawn.items():
                root = ET.fromstring(svg)
                self.assertEqual(root.tag, f"{SVG_NS}svg", name)
                for banned in ("<image", "<script", "foreignObject", "@import", "@font-face", "href=", "url(http"):
                    self.assertNotIn(banned, svg, f"{name} contains {banned}")
                lang = "zh" if "-zh-" in name else "en"
                self.assertEqual(svg.count(f">{week.COPY[lang]['now']}</text>"), 1, name)
                self.assertIn(escape_xml(now.status(lang)), svg, name)
                theme = "dark" if "-dark" in name else "light"
                other = "light" if theme == "dark" else "dark"
                self.assertNotIn(cover.THEMES[other]["fg"], svg, name)

    def test_copy_that_would_overrun_fails_the_build(self):
        steps = list(week.COPY["en"]["steps"])
        steps[0] = ("Launch", "by Thursday 23:59 UTC, or whenever you like really", steps[0][2])
        with patch.dict(week.COPY, {"en": {**week.COPY["en"], "steps": tuple(steps)}}):
            with self.assertRaisesRegex(cover.CoverLayoutError, "when of launch"):
                week.figure("en", "light", week.Now("launch"))

    def test_the_picture_picks_as_the_covers_does(self):
        for lang in ("en", "zh"):
            sources = cover.picture_sources(lang, stem=week.STEM)
            fallback = cover.asset_path(lang, "light", stem=week.STEM)
            for mode, os_scheme, width in (("auto", "dark", 390), ("dark", "light", 1280), ("auto", "light", 1280)):
                theme = os_scheme if mode == "auto" else mode
                want = cover.asset_path(lang, theme, mobile=width < cover.HERO_BREAKPOINT, stem=week.STEM)
                self.assertEqual(github_pick(sources, fallback, mode, os_scheme, width), want)
            drawn = week.rendered(week.Now("launch"))
            for _, path in sources:
                self.assertIn(pathlib.Path(path).name, drawn)

    def test_check_mode_names_exactly_the_stale_files(self):
        now = week.Now("vote", "2026-W46")
        with tempfile.TemporaryDirectory() as directory:
            out = pathlib.Path(directory)
            week.write_figures(now, out)
            self.assertEqual(week.stale(now, out), [])
            (out / "launch-week-en-dark.svg").write_text("<svg/>", encoding="utf-8")
            self.assertEqual(week.stale(now, out), ["launch-week-en-dark.svg"])
            self.assertEqual(len(week.stale(week.Now("launch"), out)), 8)


def escape_xml(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class ReadmeLayoutTests(unittest.TestCase):
    def render(self, catalog: list[dict], strings: dict) -> str:
        with patch.object(_stats, "compute", return_value={**_stats.compute(), **STATS}), \
                patch.object(sections, "START_HERE", []):
            return build_readme.render(catalog, [], strings)

    def test_the_board_chips_sit_on_their_own_row(self):
        for strings in (build_readme.EN, build_readme.ZH):
            head = self.render(ROWS, strings).split("\n## ", 1)[0]
            chips = head.split('<p align="center">', 1)[1].split("</p>", 1)[0].strip().splitlines()
            self.assertEqual(chips.index("<br>"), sections.BOARD_CHIPS)
            self.assertIn(strings["chip_board"].replace(" ", "&nbsp;"), chips[0])
            self.assertIn(strings["chip_launch"].replace(" ", "&nbsp;"), chips[1])

    def test_the_week_figure_leads_the_launch_steps(self):
        text = self.render(ROWS, build_readme.EN)
        launch = text.split("## Launch your product", 1)[1].split("\n## ", 1)[0]
        found = re.findall(r'<source media="([^"]+)" srcset="([^"]+)">', launch)
        self.assertEqual(found, cover.picture_sources("en", stem=week.STEM))
        self.assertLess(launch.index("<picture>"), launch.index("| Step |"))
        self.assertIn('alt="How a launch week runs: ', launch)

    def test_a_patterns_rows_past_the_first_few_fold(self):
        catalog = [product(f"r{index:02}") for index in range(sections.INLINE_PER_PATTERN + 2)]
        for strings in (build_readme.EN, build_readme.ZH):
            text = self.render(catalog, strings)
            name = build_readme.label(build_readme.PATTERN_LABELS, "safety-gating", strings["lang_code"])
            part = re.split(r"\n##+ ", text.split(f"### {name}\n", 1)[1], maxsplit=1)[0]
            shown, folded = part.split("<details>", 1)
            folded = folded.split("</details>", 1)[0]
            self.assertEqual(len(re.findall(r"^- \*\*\[", shown, re.M)), sections.INLINE_OPEN)
            self.assertEqual(len(re.findall(r"^- \*\*\[", folded, re.M)),
                             sections.INLINE_PER_PATTERN - sections.INLINE_OPEN)
            n = sections.INLINE_PER_PATTERN - sections.INLINE_OPEN
            self.assertIn(f"<summary>{strings['pattern_fold'].format(n=n)}</summary>\n\n", folded)
            titles = re.findall(r"^- \*\*\[([^\]]+)\]", part, re.M)
            self.assertEqual(titles, sorted(titles))

    def test_a_short_pattern_has_nothing_to_fold(self):
        catalog = [product(f"r{index}") for index in range(sections.INLINE_OPEN)]
        text = self.render(catalog, build_readme.EN)
        part = re.split(r"\n##+ ", text.split("### Safety gating\n", 1)[1], maxsplit=1)[0]
        self.assertIn("- **[R2]", part)
        self.assertNotIn("<details>", part)


if __name__ == "__main__":
    unittest.main()
