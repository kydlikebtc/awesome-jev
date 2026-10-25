"""The rows the README prints by name, and what a person has yet to give them (C1).

Most readers see the README and nothing else, and of the catalogue only the
rows it prints: *Start here*, the first reports under *Measured, not
claimed* and the first rows of each pattern. readme.sections.front_page()
names them with the README's own selection; _stats.front_page_gaps() says
what each still lacks from a person (a summary written for the catalogue,
Chinese a person wrote, a person's reading of the cited file);
docs/review-queue.md lists them in the order the README prints them, and
docs/status.md counts them.
"""

from __future__ import annotations

import copy
import json
import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import _stats  # noqa: E402
import build_docs  # noqa: E402
import build_readme  # noqa: E402
import build_review_queue as queue  # noqa: E402
from readme import rows, sections, strings  # noqa: E402

CATALOG = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
CITED = {"path": "app.py", "matched": ["system_one"]}


def row(slug: str, **fields) -> dict:
    return {
        "slug": slug, "title": slug, "summary": "Asks Jev whether to ship.", "summary_zh": "问 Jev 是否发布。",
        "url": f"https://github.com/o/{slug}", "kind": "project", "patterns": ["safety-gating"],
        "has_code": True, **fields,
    }


def listed(catalog: list[dict]) -> list[str]:
    return [cells[0].split("]")[0].lstrip("[") for cells in queue.front_page(catalog).rows]


def place(key: str, position: int) -> str:
    name = rows.label(rows.PATTERN_LABELS, key, "en")
    return f"[{name}](../README.md#{rows.anchor(name)}) {position}"


class GapsTest(unittest.TestCase):
    def test_a_persons_work_lacks_nothing(self):
        done = row("done", summary_source="curated", evidence={**CITED, "read_on": "2026-09-01"})
        self.assertEqual(_stats.front_page_gaps(done), {})
        # A summary nobody labelled that names Jev, and no cited file: nothing to give.
        self.assertEqual(_stats.front_page_gaps(row("plain")), {})

    def test_a_summary_not_in_a_persons_words(self):
        for source in _stats.NOT_A_PERSONS_SUMMARY:
            with self.subTest(source=source):
                self.assertEqual(_stats.front_page_gaps(row("a", summary_source=source)), {"summary": source})
        generic = row("a", summary="An AI Hedge Fund Team")
        self.assertEqual(_stats.front_page_gaps(generic), {"summary": "generic-summary"})
        self.assertEqual(_stats.front_page_gaps({**generic, "summary_source": "curated"}), {"summary": "generic-summary"})
        # Whose words they are comes first.
        upstream = {**generic, "summary_source": "upstream-description"}
        self.assertEqual(_stats.front_page_gaps(upstream), {"summary": "upstream-description"})

    def test_machine_chinese(self):
        self.assertEqual(_stats.front_page_gaps(row("a", zh_machine=True)), {"summary_zh": "zh_machine"})
        self.assertEqual(_stats.front_page_gaps(row("a", zh_machine=False)), {})

    def test_a_cited_file_lacks_a_persons_reading_until_one_is_recorded(self):
        self.assertEqual(_stats.front_page_gaps(row("a", evidence=CITED)), {"evidence": "unread"})
        by_model = {**CITED, "model_read_on": "2026-10-24"}
        self.assertEqual(_stats.front_page_gaps(row("a", evidence=by_model)), {"evidence": "model_read_on"})
        self.assertEqual(_stats.front_page_gaps(row("a", evidence={**by_model, "read_on": "2026-10-25"})), {})


class ReadmeAgreesTest(unittest.TestCase):
    """front_page() is the README's own selection: what it prints by name, in order."""

    @classmethod
    def setUpClass(cls):
        retired = json.loads(build_readme.RETIRED.read_text(encoding="utf-8"))
        cls.readme = build_readme.render(copy.deepcopy(CATALOG), retired, strings.EN)
        cls.shown = sections.front_page(CATALOG)

    def printed(self, heading: str) -> list[tuple[str, str]]:
        """(title, url) of each row printed by name under a `## ` heading."""
        body = self.readme.split(f"\n## {heading}\n", 1)[1].split("\n## ", 1)[0]
        return re.findall(r"^(?:- |\d+\. )\*\*\[(.+?)\]\((\S+?)\)\*\*", body, flags=re.M)

    def selected(self, keep) -> list[tuple[str, str]]:
        return [(rows.esc(entry["title"]), entry["url"]) for where, _, entry in self.shown if keep(where)]

    def test_start_here(self):
        self.assertEqual(self.printed(strings.EN["start_h"]), self.selected(lambda where: where == sections.START_PLACE))

    def test_measured_not_claimed(self):
        measured = self.selected(lambda where: where == sections.MEASURED_PLACE)
        self.assertEqual(self.printed(strings.EN["measured_h"]), measured)
        self.assertEqual(len(measured), sections.INLINE_MEASURED)

    def test_by_decision_pattern(self):
        patterns = self.selected(lambda where: where not in (sections.START_PLACE, sections.MEASURED_PLACE))
        self.assertEqual(self.printed(strings.EN["patterns_h"]), patterns)

    def test_positions_count_from_one_in_each_place(self):
        seen: dict[str, int] = {}
        for where, position, _ in self.shown:
            seen[where] = seen.get(where, 0) + 1
            self.assertEqual(position, seen[where], where)
        self.assertLessEqual(max(seen.values()), max(sections.INLINE_PER_PATTERN, len(sections.START_HERE)))


class QueueTest(unittest.TestCase):
    def test_the_page_opens_with_it(self):
        self.assertIs(queue.SECTIONS[0], queue.front_page)
        self.assertEqual(queue.front_page([]).key, "front-page")

    def test_rows_in_readme_order_once_each_with_every_place_they_are_printed(self):
        catalog = [
            row("gated-twice", patterns=["safety-gating", "tool-selection"], zh_machine=True),
            row("done", summary_source="curated", evidence={**CITED, "read_on": "2026-09-01"}),
            row("by-model", stars=5000, evidence={**CITED, "model_read_on": "2026-10-24"}),
            row("generic", summary="An AI Hedge Fund Team", patterns=["tool-selection"]),
        ]
        section = queue.front_page(catalog)
        # The README prints tool-selection before safety-gating (PATTERN_ORDER),
        # and a pattern's rows by star band, then title: done, which lacks
        # nothing, is second under safety-gating and listed nowhere.
        self.assertEqual([cells[0].split("]")[0].lstrip("[") for cells in section.rows], ["gated-twice", "generic", "by-model"])
        self.assertEqual(
            section.rows[0][1:], (f"{place('tool-selection', 1)} · {place('safety-gating', 3)}", "—", "`zh_machine`", "—")
        )
        self.assertEqual(section.rows[1][1:], (place("tool-selection", 2), "[`generic-summary`](#generic-summary)", "—", "—"))
        self.assertEqual(
            section.rows[2][1:], (place("safety-gating", 1), "—", "—", "[`model_read_on`](#model-read) 2026-10-24")
        )
        self.assertIn(", 4 rows in all.", section.about_en)

    def test_a_row_the_readme_does_not_print_is_not_listed(self):
        catalog = [row(f"r{index:02}", zh_machine=True) for index in range(sections.INLINE_PER_PATTERN + 1)]
        self.assertEqual(listed(catalog), [f"r{index:02}" for index in range(sections.INLINE_PER_PATTERN)])

    def test_a_persons_work_takes_a_row_off_and_a_models_does_not(self):
        upstream = row("up", summary_source="upstream-description")
        self.assertEqual(listed([upstream]), ["up"])
        self.assertEqual(listed([{**upstream, "summary_source": "model-written"}]), ["up"])
        self.assertEqual(listed([{**upstream, "summary_source": "curated"}]), [])
        cited = row("cited", evidence={**CITED, "model_read_on": "2026-10-24"})
        self.assertEqual(listed([cited]), ["cited"])
        self.assertEqual(listed([{**cited, "evidence": {**cited["evidence"], "read_on": "2026-10-25"}}]), [])

    def test_counted_where_status_publishes_it(self):
        # Rendered, not read from the committed pages: a pull request that
        # adds rows leaves those to the bot, and CI runs the unit tests first.
        s = _stats.compute()
        self.assertEqual(len(queue.front_page(CATALOG).rows), s["review_front_page"])
        self.assertEqual(len(_stats.front_page(CATALOG)), s["front_page_rows"])
        self.assertGreater(s["review_front_page"], 0)
        self.assertIn(f"](#front-page) | {s['review_front_page']} |", queue.render(CATALOG))
        status = build_docs.render()[ROOT / "docs" / "status.md"]
        self.assertIn(f"(review-queue.md#front-page)) | {s['review_front_page']} of {s['front_page_rows']} |", status)


if __name__ == "__main__":
    unittest.main()
