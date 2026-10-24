"""An alternative row's `wire` (I48): what its own files show about the
interface it offers, the rules scripts/wire.py keeps on it, the table
docs/compatibility.md and the site draw from it, the review-queue section for
rows no person has read, and the weekly re-read of every cited file.

No network: verify_claims' raw reads are replaced. Tables are rendered in
memory from made-up rows, never read from the committed page.
"""

from __future__ import annotations

import contextlib
import copy
import datetime as dt
import io
import json
import os
import pathlib
import re
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import build_compat  # noqa: E402
import build_review_queue  # noqa: E402
import lint_docs  # noqa: E402
import verify_claims as vc  # noqa: E402
import wire  # noqa: E402
from _github import RateLimited  # noqa: E402
from platform_values import load_query  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCHEMA = json.loads((ROOT / "schema" / "entry.schema.json").read_text())
TAXONOMY = json.loads((ROOT / "taxonomy.json").read_text())
CASES = json.loads((HERE / "wire_cases.json").read_text())["cases"]
NOT_JEV = next(flag for flag in TAXONOMY["flags"] if flag["key"] == wire.NOT_JEV)

SERVER = {"path": "server.py", "matched": ['@app.post("/v1/systemone")', '{"type": "noul", "noul": p}']}


def alt(slug: str, stars: int | None = None, record: dict | None = None, **extra) -> dict:
    """An alternative row on GitHub with the not-jev flag, `record` as its wire."""
    entry = {
        "slug": slug, "title": extra.pop("title", slug), "kind": "alternative",
        "url": f"https://github.com/o/{slug}", "flags": [wire.NOT_JEV], **extra,
    }
    if stars is not None:
        entry["stars"] = stars
    if record is not None:
        entry["wire"] = record
    return entry


def block(catalog: list[dict]) -> str:
    return build_compat.alternatives_block(catalog, TAXONOMY)


class DefinitionTest(unittest.TestCase):
    def test_the_constants_are_the_schemas(self):
        props = SCHEMA["properties"]["wire"]["properties"]
        self.assertEqual(tuple(props["weights"]["enum"]), wire.WEIGHTS)
        self.assertEqual(tuple(props["envelope"]["enum"]), wire.ENVELOPES)
        for field in (*wire.COPIED, wire.ENDPOINT, wire.BASELINE, wire.COMPARISON, wire.SOURCE):
            self.assertIn(field, props)
        self.assertEqual(props[wire.BASELINE]["enum"], [True], "only true is recorded")

    def test_the_site_table_prints_weights_caveats_and_the_repository_on_every_row(self):
        page = (ROOT / "site" / "index.html").read_text()
        start = page.index("function wireTable()")
        table = page[start:page.index("\n      }\n", start)]
        cols = re.search(r"const cols = \[([^\]]*)\]", table).group(1)
        self.assertEqual(len(cols.split(",")), len(build_compat.WIRE_COLUMNS))
        self.assertIn('"w_weights"', cols)
        row = table[table.index("return `<tr>"):]
        for text in ("${caveats(e)}", "wireRepository(e)", "<sub>${esc(repo)}</sub>"):
            self.assertIn(text, table)
        caveats = table[table.index("const caveats"):table.index("const cols")]
        for text in ('lbl(FLAG, "not-jev")', "S().w_calibration", "isNegativeResult(e)", "S().w_negative"):
            self.assertIn(text, caveats)
        self.assertIn("${caveats(e)}", row)

    def test_the_calibration_sentence_is_taxonomys_in_both_languages(self):
        self.assertIn(wire.CALIBRATION_NOTE, NOT_JEV["blurb_en"])
        self.assertIn(wire.CALIBRATION_NOTE_ZH, NOT_JEV["blurb_zh"])
        page = (ROOT / "site" / "index.html").read_text()
        self.assertEqual(re.findall(r'w_calibration: "([^"]*)"', page), [wire.CALIBRATION_NOTE, wire.CALIBRATION_NOTE_ZH])

    def test_selection_agrees_with_the_site_on_the_shared_cases(self):
        entries = [case["entry"] for case in CASES]
        wired = {e["slug"] for e in wire.wired(entries)}
        unwired = {e["slug"] for e in wire.unwired(entries)}
        for case in CASES:
            with self.subTest(case=case["name"]):
                self.assertEqual(case["entry"]["slug"] in wired, case["wired"])
                self.assertEqual(case["entry"]["slug"] in unwired, case["unwired"])
                self.assertEqual(wire.person_read(wire.wire_of(case["entry"]) or {}), case["person_read"])
                self.assertEqual(wire.every_file_read(wire.wire_of(case["entry"]) or {}), case["every_file_read"])
                self.assertEqual(build_compat.row_repository(case["entry"]), case["repository"])

    def test_claims_are_the_well_formed_cited_files(self):
        record = {"weights": "open", "source": [SERVER, {"path": "x.py"}, "text", {"path": "y.py", "matched": ["a1"], "read_on": "2026-09-01"}]}
        self.assertEqual(wire.claims(alt("a", record=record)), [SERVER, {"path": "y.py", "matched": ["a1"]}])
        self.assertEqual(wire.claims(alt("b")), [])
        self.assertEqual(wire.endpoint_path("POST /v1/systemone"), "/v1/systemone")


class RowProblemsTest(unittest.TestCase):
    TODAY = dt.date(2026, 9, 28)

    def test_a_clean_record_has_no_problem(self):
        self.assertEqual(wire.row_problems(alt("a", record={"endpoint": "POST /v1/systemone", "source": [SERVER]}), self.TODAY, on_github=True), [])

    def test_a_row_without_wire_is_not_judged(self):
        self.assertEqual(wire.row_problems({"slug": "a", "kind": "project"}, self.TODAY, on_github=False), [])

    def test_a_record_needs_a_repository_to_read_its_files_in(self):
        found = wire.row_problems(alt("a", record={"weights": "open", "source": [SERVER]}), self.TODAY, on_github=False)
        self.assertEqual(found, ["has a wire record but no GitHub repository to read wire.source in"])

    def test_a_malformed_record_is_left_to_the_schema(self):
        self.assertEqual(wire.row_problems(alt("a", record=None, wire=["x"]), self.TODAY, on_github=True), [])


class TableTest(unittest.TestCase):
    FULL = {
        "endpoint": "POST /v1/systemone", "yesno_spelling": "noul", "answer_field": "noul",
        "confidence_field": "confidence", "envelope": "top-level", "weights": "open", "base_model": "o/m-4b",
        "calls_real_jev_as_baseline": True, "comparison_url": "https://github.com/o/big/blob/HEAD/RESULTS.md",
        "source": [SERVER],
    }

    def catalogue(self) -> list[dict]:
        return [
            alt("small", 150, {"weights": "proxy", "base_model": "gpt-4o-mini", "source": [{"path": "a.ts", "matched": ['"gpt-4o-mini"']}]}),
            alt("big", 12000, self.FULL, title="Big"),
            alt("unread-one", 3),
            alt("unread-two", None),
            {"slug": "proj", "title": "proj", "kind": "project", "url": "https://github.com/o/proj"},
        ]

    def lines(self, catalog: list[dict]) -> list[str]:
        return [line for line in block(catalog).splitlines() if line.startswith("| [")]

    def test_every_row_carries_the_not_jev_caveat_and_the_calibration_sentence(self):
        rows = self.lines(self.catalogue())
        self.assertEqual(len(rows), 2)
        for line in rows:
            self.assertIn(f"**{NOT_JEV['en']}**: {wire.CALIBRATION_NOTE}", line)
        # Not the blurb's first sentence: some of these projects do call Jev.
        self.assertNotIn("Does not call Jev at all", block(self.catalogue()))

    def test_the_weights_column_is_always_there_and_an_unread_field_is_a_dash(self):
        text = block([alt("bare", 20, {"endpoint": "POST /v1/systemone", "source": [SERVER]})])
        header = text.splitlines()[0]
        self.assertIn("| Weights |", header)
        cells = [cell.strip() for cell in text.splitlines()[2].strip("|").split(" | ")]
        self.assertEqual(len(cells), len(build_compat.WIRE_COLUMNS))
        self.assertEqual(cells[1], "—")  # weights not recorded
        self.assertEqual(cells[3], "`POST /v1/systemone`")
        self.assertEqual(cells[8], "—")  # no baseline call shown

    def test_a_full_record_prints_every_field(self):
        line = self.lines(self.catalogue())[0]
        for text in ("open weights", "`o/m-4b`", "`POST /v1/systemone`", "top level", "`noul`", "`confidence`",
                     "| yes |", "[link](https://github.com/o/big/blob/HEAD/RESULTS.md)",
                     "[`server.py`](https://github.com/o/big/blob/HEAD/server.py) (not yet read by a person)",
                     "<sub>o/big</sub> ★10k+"):
            self.assertIn(text, line)
        self.assertIn("proxy: another provider's hosted model", self.lines(self.catalogue())[1])

    def test_rows_follow_the_star_band_then_the_title_whatever_the_file_order(self):
        catalog = self.catalogue()
        self.assertTrue(self.lines(catalog)[0].startswith("| [Big]"))
        self.assertEqual(block(catalog), block(catalog[::-1]))
        # Stars that stay in their band change nothing.
        moved = copy.deepcopy(catalog)
        moved[0]["stars"], moved[1]["stars"] = 999, 99999
        self.assertEqual(block(moved), block(catalog))

    def test_the_rows_without_a_record_are_counted_not_listed(self):
        text = block(self.catalogue())
        self.assertIn("2 more `alternative` rows carry no `wire` record", text)
        self.assertNotIn("unread-one", text)
        one = block(self.catalogue()[:3])
        self.assertIn("1 more `alternative` row carries no `wire` record", one)
        self.assertIn("No row records its interface yet.", block([alt("x")]))

    def test_other_caveats_and_a_negative_result_travel_with_the_row(self):
        catalog = [alt("a", 10, {"weights": "open", "source": [SERVER]}, flags=["no-license", wire.NOT_JEV, "negative-result"],
                       notes="Measured: recall fell, https://example.com/r")]
        line = self.lines(catalog)[0]
        labels = {flag["key"]: flag["en"] for flag in TAXONOMY["flags"]}
        self.assertTrue(line.endswith(f"{wire.CALIBRATION_NOTE} · {labels['no-license']} · {labels['negative-result']} · "
                                      "negative result, author-stated, not reproduced here |"), line)

    def test_a_person_reading_is_dated_and_outside_text_cannot_break_the_table(self):
        record = {"weights": "open", "source": [{"path": "a|b`c.py", "matched": ["x1"], "read_on": "2026-09-20"}]}
        line = self.lines([alt("a", 10, record)])[0]
        self.assertIn("(read by a person on 2026-09-20)", line)
        self.assertIn("`a\\|b'c.py`", line)
        self.assertEqual(line.count(" | "), len(build_compat.WIRE_COLUMNS) - 1)

    def test_the_page_fills_its_markers_from_the_catalogue(self):
        text = build_compat.build(catalog=self.catalogue())
        section = text.split("<!-- alternatives:start -->\n", 1)[1].split("\n<!-- alternatives:end -->", 1)[0]
        self.assertEqual(section, block(self.catalogue()))
        # A page without the markers (lint_docs' rehearsal text, other tests) is left alone.
        bare = "<!-- models:start -->\n<!-- models:end -->\n"
        self.assertNotIn("alternatives", build_compat.build(text=bare + "".join(
            f"<!-- {name}:start -->\n<!-- {name}:end -->\n" for name in build_compat.BLOCKS if name != "models")))


class ReviewQueueTest(unittest.TestCase):
    def test_rows_no_person_has_read_are_listed_by_band(self):
        read = {"weights": "open", "source": [{**SERVER, "read_on": "2026-09-20"}]}
        half = {"weights": "proxy", "source": [{**SERVER, "read_on": "2026-09-20"}, {"path": "b.py", "matched": ["b1"]}]}
        catalog = [alt("low", 20, {"weights": "open", "source": [SERVER]}), alt("high", 5000, half), alt("done", 900, read), alt("none", 800)]
        section = build_review_queue.wire_unread(catalog)
        self.assertEqual([row[0].split("]")[0] for row in section.rows], ["[high", "[low"])
        self.assertEqual(section.rows[0][2], "`proxy`")
        self.assertIn(build_review_queue.wire_unread, build_review_queue.SECTIONS)
        self.assertEqual(section.key, "wire-unread")


class VersionedLinkTest(unittest.TestCase):
    URL = "https://github.com/o/a/blob/HEAD/eval/jev-1.13/RUN.md"

    def test_a_projects_file_in_the_table_is_not_a_vendor_page(self):
        inside = f"a\n<!-- alternatives:start -->\n| [x]({self.URL}) |\n<!-- alternatives:end -->\n"
        self.assertEqual(lint_docs.check_versioned_urls("docs/compatibility.md", inside, set()), [])
        outside = inside + f"see {self.URL}\n"
        found = lint_docs.check_versioned_urls("docs/compatibility.md", outside, set())
        self.assertEqual(len(found), 1)
        self.assertTrue(found[0].startswith("docs/compatibility.md:5: "), found)


class Raw:
    """A fake raw host for one repository: {(branch, path): body}."""

    def __init__(self, files: dict):
        self.files = files
        self.reads: list[tuple[str, str]] = []

    def raw_get(self, repo, branch, path, **_):
        self.reads.append((branch, path))
        return self.files.get((branch, path))

    def default_branch(self, repo):
        return "main"


class WeeklyReadTest(unittest.TestCase):
    ROW = alt("a", 10, {"endpoint": "POST /v1/systemone", "source": [SERVER, {"path": "cfg.py", "matched": ['MODEL = "jev-1.13"']}]})

    def check(self, files: dict, source: dict = SERVER) -> dict:
        raw = Raw(files)
        with mock.patch.object(vc, "raw_get", raw.raw_get), mock.patch.object(vc, "default_branch", raw.default_branch):
            return vc.check_wire((self.ROW, source))

    def test_each_cited_file_is_read_like_evidence(self):
        body = "\n".join(SERVER["matched"])
        self.assertEqual(self.check({("HEAD", "server.py"): body}),
                         {"slug": "a", "status": "ok", "claim": "wire", "detail": "wire.source o/a@HEAD:server.py"})
        gone = self.check({("main", "server.py"): "nothing here"})
        self.assertEqual(gone["status"], "claim-gone")
        self.assertIn("wire.source o/a@main:server.py no longer contains", gone["detail"])
        self.assertEqual(self.check({})["status"], "path-gone")

    def test_a_moved_model_version_is_a_file_to_re_read_not_a_rewrite(self):
        cfg = self.ROW["wire"]["source"][1]
        result = self.check({("main", "cfg.py"): 'MODEL = "jev-1.14"'}, cfg)
        self.assertEqual(result["status"], "claim-gone")
        self.assertNotIn("pins", result)

    def test_a_rate_limit_leaves_the_file_unchecked(self):
        def limited(*_, **__):
            raise RateLimited("raw", "closed")
        with mock.patch.object(vc, "raw_get", limited):
            self.assertEqual(vc.check_wire((self.ROW, SERVER))["status"], "skipped")
        self.assertEqual(vc.check_wire(({"slug": "b", "wire": {}}, SERVER))["status"], "no-repo")

    def run_main(self, rows: list[dict], files: dict, *argv: str) -> tuple[int, str, Raw]:
        raw = Raw(files)
        with tempfile.TemporaryDirectory() as tmp:
            catalog = pathlib.Path(tmp) / "catalog.json"
            catalog.write_text(json.dumps(rows))
            out = io.StringIO()
            with mock.patch.object(vc, "CATALOG", catalog), mock.patch.object(sys, "argv", ["verify_claims.py", *argv]), \
                 mock.patch.object(vc, "raw_get", raw.raw_get), mock.patch.object(vc, "default_branch", raw.default_branch), \
                 mock.patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": ""}), \
                 contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
                code = vc.main()
            return code, out.getvalue(), raw

    def test_the_weekly_run_reads_wire_sources_beside_evidence(self):
        row = {**self.ROW, "evidence": {"path": "bench.py", "matched": ['"type": "noul"']}}
        files = {("HEAD", "bench.py"): '{"type": "noul"}', ("HEAD", "server.py"): "\n".join(SERVER["matched"])}
        code, out, raw = self.run_main([row], files, "--json")
        self.assertEqual(code, 1)
        report = json.loads(out)
        self.assertEqual(report["checked"], 3)
        self.assertEqual([(r["slug"], r.get("claim"), r["status"]) for r in report["failed"]], [("a", "wire", "path-gone")])
        # Only evidence gives a file's primitive text signal.
        self.assertEqual(report["primitive_signals"], {"a": ["noul"]})
        code, text, _ = self.run_main([row], files)
        self.assertIn("A wire.source failure", text)
        self.assertIn("2/3 claims still hold", text)

    def test_a_row_with_only_a_wire_record_is_still_read(self):
        code, out, raw = self.run_main([self.ROW], {("HEAD", "server.py"): "\n".join(SERVER["matched"]),
                                                     ("HEAD", "cfg.py"): 'MODEL = "jev-1.13"'})
        self.assertEqual(code, 0, out)
        self.assertIn("2/2 claims still hold", out)

    def test_recording_primitive_signals_never_reads_wire_sources(self):
        row = {**self.ROW, "evidence": {"path": "bench.py", "matched": ["x1"]}}
        with tempfile.TemporaryDirectory() as tmp:
            catalog = pathlib.Path(tmp) / "catalog.json"
            catalog.write_text(json.dumps([row]))
            raw = Raw({("HEAD", "bench.py"): "x1"})
            with mock.patch.object(vc, "CATALOG", catalog), mock.patch.object(sys, "argv", ["verify_claims.py", "--write-signals"]), \
                 mock.patch.object(vc, "raw_get", raw.raw_get), mock.patch.object(vc, "default_branch", raw.default_branch), \
                 mock.patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": ""}), \
                 contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(vc.main(), 0)
        self.assertEqual({path for _, path in raw.reads}, {"bench.py"})


class ServerTest(unittest.TestCase):
    def test_get_example_returns_wire_and_search_leaves_it_out(self):
        query = load_query()
        row = {**alt("a", 10, {"weights": "open", "source": [SERVER]}), "summary": "s", "patterns": ["overview"]}
        self.assertEqual(query.find_example([row], "a")["wire"], row["wire"])
        self.assertNotIn("wire", query.compact(row))


class RealCatalogueTest(unittest.TestCase):
    def test_every_record_is_on_an_alternative_that_says_it_is_not_jev(self):
        catalog = json.loads((ROOT / "catalog.json").read_text())
        recorded = [e for e in catalog if wire.FIELD in e]
        self.assertEqual(recorded, wire.wired(catalog))
        for entry in recorded:
            with self.subTest(slug=entry["slug"]):
                self.assertIn(wire.NOT_JEV, entry["flags"])
                # The real clock, as lint uses it: a person may date a reading later.
                self.assertEqual(wire.row_problems(entry, dt.date.today(), on_github=True), [])


if __name__ == "__main__":
    unittest.main()
