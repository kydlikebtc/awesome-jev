"""The site's per-pattern JSON files for agents, site/api/v1/ (I36).

catalog.json is over a megabyte; an agent without the MCP server gets one small
file per decision pattern instead, served by Pages beside the site. These tests
build the files in memory from made-up rows (and from the real catalogue, whose
source files they read), and run assemble_site.py and check_site_data.py
against a scratch copy of the tree. Nothing here reads a generated file.
"""

from __future__ import annotations

import contextlib
import io
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))

import _stats  # noqa: E402
import assemble_site  # noqa: E402
import build_docs  # noqa: E402
import check_site_data  # noqa: E402
import site_api  # noqa: E402
from awesome_jev_mcp import query as package_query  # noqa: E402

SITE_URL = "https://example.test/awesome-jev/"
PUBLISHED = ("catalog.json", "retired.json", "llms.txt", "stats.json")

PATTERNS = [
    {"key": "tool-selection", "en": "Tool selection", "zh": "工具选择", "blurb_en": "Which tool next.", "blurb_zh": "下一步用哪个工具。"},
    {"key": "safety-gating", "en": "Safety gating", "zh": "安全闸门", "blurb_en": "Let an action through?", "blurb_zh": "是否放行。"},
    {"key": "fan-out", "en": "Fan-out", "zh": "扇出", "blurb_en": "Many questions at once.", "blurb_zh": "一次问多个问题。"},
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
        "sources": [{"catalog": "somewhere", "url": "https://example.test/list"}],
        "license": "CC0-1.0",
    }
    return {**base, **fields}


ROWS = [
    row("router", has_code=True, stars=40, languages=["python"], question_types=["choice"],
        flags=["vendor-reported", "single-commit"], notes="Routes by cost.", checked="2026-09-20"),
    row("gate", title="gate", has_code=True, stars=400, patterns=["tool-selection", "safety-gating"],
        repo_created_at="2026-09-01T00:00:00Z", summary_source="upstream-description"),
    row("vendor-docs", kind="official-docs", official=True, patterns=["overview"]),
    row("clone", kind="alternative", has_code=True, stars=4000, flags=["not-jev"]),
    row("dry-run", has_code=True, stars=90, flags=["shadow-mode-only"], primitives_seen=["noul"],
        patterns=["safety-gating"]),
]
STATS = {"last_sweep": "2001-02-03", "entries": len(ROWS), "retired": 2,
         "by_pattern": {"tool-selection": 3, "safety-gating": 2, "fan-out": 0, "overview": 1}}


def build(rows=ROWS, patterns=PATTERNS, stats=STATS) -> dict[str, str]:
    return site_api.api_files(rows, patterns, stats, site_url=SITE_URL, published=PUBLISHED)


def parsed(files: dict[str, str]) -> dict[str, dict]:
    return {rel: json.loads(text) for rel, text in files.items()}


class ShapeTest(unittest.TestCase):
    def setUp(self):
        self.files = parsed(build())
        self.index = self.files["api/v1/index.json"]

    def test_one_file_per_pattern_and_an_index(self):
        expected = {"api/v1/index.json"} | {f"api/v1/patterns/{p['key']}.json" for p in PATTERNS}
        self.assertEqual(set(self.files), expected)

    def test_the_index_lists_the_patterns_in_the_taxonomy_order(self):
        self.assertEqual(self.index["api_version"], 1)
        self.assertEqual([p["key"] for p in self.index["patterns"]], [p["key"] for p in PATTERNS])
        for item in self.index["patterns"]:
            self.assertEqual(item["url"], f"{SITE_URL}api/v1/patterns/{item['key']}.json")

    def test_the_index_reuses_list_patterns_shape(self):
        # key, name, description and the row count are exactly the MCP
        # server's list_patterns answer; the index adds where the file is.
        listed = package_query.pattern_counts(ROWS, PATTERNS)["patterns"]
        self.assertEqual([{k: v for k, v in p.items() if k not in ("url", "bytes")} for p in self.index["patterns"]], listed)
        self.assertEqual(self.index["note"], package_query.PATTERNS_NOTE)

    def test_every_row_is_the_mcp_compact_shape_in_the_mcp_order(self):
        for p in PATTERNS:
            body = self.files[f"api/v1/patterns/{p['key']}.json"]
            rows = sorted((e for e in ROWS if p["key"] in e["patterns"]), key=package_query.sort_key)
            self.assertEqual(body["entries"], [package_query.compact(e) for e in rows], p["key"])
            self.assertEqual(body["examples"], len(rows))
            self.assertEqual(body["pattern"], p["key"])
            self.assertEqual((body["name"], body["description"]), (p["en"], p["blurb_en"]), p["key"])
            self.assertEqual(body["note"], package_query.SEARCH_NOTE)
            # The rows' text is data, as every MCP answer holding rows says.
            self.assertEqual(body["text_note"], package_query.TEXT_NOTE)

    def test_caveated_rows_stay_with_their_caveats(self):
        # Counts match the catalogue, so nothing is left out; the index and
        # every file say which caveats mean "not an example of calling Jev".
        gating = self.files["api/v1/patterns/safety-gating.json"]
        self.assertIn({"slug": "dry-run", "caveats": ["shadow-mode-only"]},
                      [{"slug": e["slug"], "caveats": e.get("caveats")} for e in gating["entries"]])
        tools = self.files["api/v1/patterns/tool-selection.json"]
        self.assertEqual([e["slug"] for e in tools["entries"]], ["clone", "gate", "router"])
        self.assertEqual(tools["entries"][0]["caveats"], ["not-jev"])
        for body in self.files.values():
            self.assertEqual(body["not_examples"], sorted(package_query.DISQUALIFYING))

    def test_counts_match_a_count_over_the_rows(self):
        counts = Counter(p for e in ROWS for p in e["patterns"])
        for item in self.index["patterns"]:
            self.assertEqual(item["examples"], counts[item["key"]])
        self.assertEqual(self.files["api/v1/patterns/fan-out.json"]["entries"], [])

    def test_bytes_is_the_size_of_the_file_served(self):
        text = build()
        for item in self.index["patterns"]:
            self.assertEqual(item["bytes"], len(text[f"api/v1/patterns/{item['key']}.json"].encode("utf-8")))

    def test_the_only_date_in_the_index_is_the_catalogue_s(self):
        # Never a build time: two deploys of the same data serve the same bytes.
        index = build()["api/v1/index.json"]
        self.assertEqual(re.findall(r"\d{4}-\d{2}-\d{2}", index), ["2001-02-03"])
        self.assertEqual(self.index["last_sweep"], "2001-02-03")
        self.assertEqual(build(), build())

    def test_file_order_does_not_matter(self):
        self.assertEqual(build(list(reversed(ROWS))), build())

    def test_the_index_links_the_published_files(self):
        self.assertEqual(self.index["files"], {name: SITE_URL + name for name in PUBLISHED})
        self.assertEqual(self.index["entries"], STATS["entries"])
        self.assertEqual(self.index["retired"], STATS["retired"])

    def test_query_is_the_package_s_own_file(self):
        # Loaded by path, so the MCP server and the site cannot shape a row two ways.
        self.assertEqual(pathlib.Path(site_api.query.__file__).resolve(), ROOT / site_api.BY_PATH[0])
        self.assertEqual(
            (ROOT / site_api.BY_PATH[0]).read_text(), pathlib.Path(package_query.__file__).read_text()
        )


class ContractTest(unittest.TestCase):
    """What api_version 1 promises (site_api.ABOUT, docs/method.md): fields
    may be added, none removed or renamed, and no file carries the time it was
    built. A change that fails here belongs at api/v2, a new path, rather than
    in these lists."""

    INDEX = {"api_version", "last_sweep", "entries", "retired", "about", "not_examples", "note", "patterns",
             "files", "repository"}
    INDEX_PATTERN = {"key", "name", "description", "examples", "url", "bytes"}
    PATTERN_FILE = {"api_version", "pattern", "name", "description", "last_sweep", "examples", "not_examples",
                    "note", "entries"}
    ROW = {"slug", "title", "url", "summary", "kind", "patterns", "summary_source", "patterns_reviewed",
           "question_types", "languages", "platforms", "stars", "repo_license", "repo_created_at",
           "repo_pushed_at", "repo_commits", "official", "caveats", "note"}

    def test_no_v1_field_is_dropped(self):
        full = row("full", has_code=True, official=True, stars=7, summary_source="curated",
                   patterns_reviewed="2001-01-01", question_types=["choice"], languages=["python"],
                   platforms=["typesafe-api"], repo_license="MIT", repo_created_at="2001-01-01T00:00:00Z",
                   repo_pushed_at="2001-01-02T00:00:00Z", repo_commits=3, flags=["vendor-reported"], notes="n")
        files = parsed(build([*ROWS, full]))
        index = files[site_api.INDEX]
        self.assertLessEqual(self.INDEX, set(index))
        for item in index["patterns"]:
            self.assertLessEqual(self.INDEX_PATTERN, set(item), item["key"])
        tools = files["api/v1/patterns/tool-selection.json"]
        for rel, body in files.items():
            if rel != site_api.INDEX:
                self.assertLessEqual(self.PATTERN_FILE, set(body), rel)
        (served,) = [e for e in tools["entries"] if e["slug"] == "full"]
        self.assertLessEqual(self.ROW, set(served))

    def test_the_index_says_what_the_evidence_counts_are(self):
        # Every pattern in the index carries list_patterns' `evidence` counts;
        # the note saying they are reports counted, not a verdict, travels with them.
        index = parsed(build())[site_api.INDEX]
        self.assertEqual(index["evidence_note"], site_api.query.EVIDENCE_NOTE)
        self.assertIn("not a verdict", index["evidence_note"])
        for item in index["patterns"]:
            self.assertIn("evidence", item, item["key"])

    def test_no_pattern_file_carries_a_build_date(self):
        # Row dates are the catalogue's; outside the rows the only date is
        # last_sweep, so two deploys of the same data serve the same bytes.
        for rel, text in build().items():
            if rel == site_api.INDEX:
                continue
            head = {k: v for k, v in json.loads(text).items() if k != "entries"}
            self.assertEqual(re.findall(r"\d{4}-\d{2}-\d{2}", json.dumps(head)), ["2001-02-03"], rel)

    def test_pattern_files_are_compact(self):
        # An agent pays for every byte of a pattern file; only the index is
        # indented for a person.
        for rel, text in build().items():
            if rel != site_api.INDEX:
                self.assertEqual(text, json.dumps(json.loads(text), ensure_ascii=False, separators=(",", ":")) + "\n", rel)


class RealCatalogueTest(unittest.TestCase):
    """The real catalogue, built in memory from the source files."""

    @classmethod
    def setUpClass(cls):
        catalog, _, patterns, _, _ = _stats.load()
        cls.stats = _stats.compute()
        cls.patterns = patterns
        cls.files = parsed(site_api.api_files(
            catalog, patterns, cls.stats, site_url=assemble_site.SITE_URL, published=assemble_site.RUNTIME_FILES
        ))
        cls.fields = {key for e in catalog for key in package_query.compact(e)}

    def test_each_pattern_file_holds_as_many_rows_as_the_stats_count(self):
        for p in self.patterns:
            body = self.files[f"api/v1/patterns/{p['key']}.json"]
            self.assertEqual(len(body["entries"]), self.stats["by_pattern"][p["key"]], p["key"])

    def test_the_rows_carry_the_compact_fields_and_no_others(self):
        seen = {key for rel, body in self.files.items() if rel != site_api.INDEX for e in body["entries"] for key in e}
        self.assertEqual(seen, self.fields)

    def test_the_index_points_at_pages(self):
        index = self.files["api/v1/index.json"]
        self.assertTrue(all(u.startswith("https://kydlikebtc.github.io/awesome-jev/") for u in index["files"].values()))
        self.assertIn("https://kydlikebtc.github.io/awesome-jev/llms.txt", index["files"].values())
        self.assertIn("https://kydlikebtc.github.io/awesome-jev/schema/entry.schema.json", index["files"].values())
        self.assertIn("https://kydlikebtc.github.io/awesome-jev/retired.json", index["files"].values())


class LlmsTextTest(unittest.TestCase):
    def test_the_published_copy_is_what_build_docs_writes(self):
        # The committed llms.txt can trail a merge by one bot commit, and that
        # commit starts no Pages run, so the site refills its values itself.
        stats = _stats.compute()
        self.assertEqual(
            site_api.llms_text((ROOT / "llms.txt").read_text(), stats),
            build_docs.render()[ROOT / "llms.txt"],
        )

    def test_a_stale_value_is_refilled(self):
        text = "It contains <!--n:entries-->3<!--/n--> entries."
        self.assertEqual(
            site_api.llms_text(text, _stats.compute()),
            f"It contains <!--n:entries-->{_stats.compute()['entries']}<!--/n--> entries.",
        )


class ProblemsTest(unittest.TestCase):
    """site_api.api_problems() on a site directory written from build()."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.site = pathlib.Path(tmp.name)
        site_api.write_api(self.site, build())

    def problems(self, stats=STATS):
        return site_api.api_problems(self.site, ROWS, PATTERNS, stats, site_url=SITE_URL, published=PUBLISHED)

    def test_a_fresh_build_has_none(self):
        self.assertEqual(self.problems(), [])

    def test_a_missing_file(self):
        (self.site / "api/v1/patterns/fan-out.json").unlink()
        self.assertEqual(self.problems(), ["site/api/v1/patterns/fan-out.json is missing; run assemble_site.py"])

    def test_a_file_for_no_pattern(self):
        (self.site / "api/v1/patterns/retired-pattern.json").write_text("{}")
        (found,) = self.problems()
        self.assertIn("site/api/v1/patterns/retired-pattern.json", found)
        self.assertIn("patterns.json", found)

    def test_the_writer_clears_old_files(self):
        (self.site / "api/v1/patterns/retired-pattern.json").write_text("{}")
        site_api.write_api(self.site, build())
        self.assertEqual(self.problems(), [])

    def test_a_row_count_that_disagrees_with_the_stats(self):
        stats = {**STATS, "by_pattern": {**STATS["by_pattern"], "tool-selection": 4}}
        (found,) = self.problems(stats)
        self.assertIn("tool-selection", found)
        self.assertIn("3 row(s)", found)
        self.assertIn("4", found)

    def test_a_stale_row(self):
        path = self.site / "api/v1/patterns/overview.json"
        body = json.loads(path.read_text())
        body["entries"][0]["title"] = "Old title"
        path.write_text(site_api.dump(body))
        found = self.problems()
        self.assertTrue(any("overview.json" in f and "stale" in f for f in found), found)

    def test_a_dropped_row_is_both_stale_and_miscounted(self):
        path = self.site / "api/v1/patterns/safety-gating.json"
        body = json.loads(path.read_text())
        body["entries"] = body["entries"][:1]
        path.write_text(site_api.dump(body))
        found = self.problems()
        self.assertTrue(any("stale" in f for f in found), found)
        self.assertTrue(any("1 row(s)" in f and "by_pattern" in f for f in found), found)

    def test_an_index_whose_keys_are_not_the_taxonomy(self):
        path = self.site / "api/v1/index.json"
        body = json.loads(path.read_text())
        body["patterns"] = body["patterns"][:-1]
        path.write_text(site_api.dump(body, pretty=True))
        found = self.problems()
        self.assertTrue(any("index.json" in f and "patterns.json" in f for f in found), found)

    def test_a_size_that_is_not_the_file_s(self):
        # The same JSON re-serialised: equal when parsed, but the index's
        # byte count no longer describes what Pages serves.
        path = self.site / "api/v1/patterns/tool-selection.json"
        path.write_text(json.dumps(json.loads(path.read_text()), ensure_ascii=False, indent=2))
        found = self.problems()
        self.assertTrue(any("tool-selection.json" in f and "bytes" in f for f in found), found)

    def test_a_file_that_is_not_json(self):
        (self.site / "api/v1/patterns/overview.json").write_text("<html>")
        found = self.problems()
        self.assertTrue(any("overview.json is not JSON" in f for f in found), found)


class AssembleTest(unittest.TestCase):
    """assemble_site.main() and check_site_data.main() on a scratch copy."""

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = pathlib.Path(tmp.name)
        (self.root / "site").mkdir()
        for name in assemble_site.RUNTIME_FILES:
            (self.root / name).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, self.root / name)
        shutil.copyfile(ROOT / "site" / "index.html", self.root / "site" / "index.html")
        for module in (assemble_site, check_site_data):
            for name, value in (("ROOT", self.root), ("SITE", self.root / "site")):
                if hasattr(module, name):
                    patcher = patch.object(module, name, value)
                    patcher.start()
                    self.addCleanup(patcher.stop)

    def run_main(self, main, argv=()):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = main(list(argv))
        return code, out.getvalue() + err.getvalue()

    def test_assemble_publishes_the_agent_files_and_the_check_accepts_them(self):
        code, out = self.run_main(assemble_site.main)
        self.assertEqual(code, 0, out)
        site = self.root / "site"
        for name in ("retired.json", "schema/entry.schema.json", "llms.txt", "api/v1/index.json"):
            self.assertTrue((site / name).is_file(), name)
        self.assertIn("api/v1", out)
        self.assertEqual(
            (site / "llms.txt").read_text(), site_api.llms_text((ROOT / "llms.txt").read_text(), _stats.compute())
        )
        code, out = self.run_main(check_site_data.main)
        self.assertEqual(code, 0, out)
        self.assertIn("by_pattern", out)

    def test_a_committed_llms_txt_that_trails_the_data_is_published_current(self):
        # The regenerate job's commit after a merge starts no Pages run, so the
        # deploy of the merge itself must not publish the old counts.
        llms = self.root / "llms.txt"
        # Source-only PRs may already carry stale generated counts. Build the
        # fixture from the marker, independent of the committed number.
        stale, replaced = re.subn(
            r"<!--n:entries-->.*?<!--/n-->", "<!--n:entries-->3<!--/n-->", llms.read_text(), flags=re.S
        )
        self.assertGreater(replaced, 0)
        llms.write_text(stale)
        code, out = self.run_main(assemble_site.main)
        self.assertEqual(code, 0, out)
        published = (self.root / "site" / "llms.txt").read_text()
        self.assertNotIn("<!--n:entries-->3<!--/n-->", published)
        entries = len(json.loads((self.root / "catalog.json").read_text()))
        self.assertIn(f"<!--n:entries-->{entries}<!--/n-->", published)
        self.assertEqual(published, site_api.llms_text(stale, _stats.compute()))
        code, out = self.run_main(check_site_data.main)
        self.assertEqual(code, 0, out)

    def test_the_check_refuses_a_broken_api_file(self):
        self.run_main(assemble_site.main)
        (self.root / "site" / "api" / "v1" / "patterns" / "overview.json").unlink()
        code, out = self.run_main(check_site_data.main)
        self.assertEqual(code, 1)
        self.assertIn("site/api/v1/patterns/overview.json is missing", out)

    def test_the_check_refuses_a_stale_llms_txt(self):
        self.run_main(assemble_site.main)
        llms = self.root / "site" / "llms.txt"
        llms.write_text(llms.read_text().replace("## For agents", "## For robots"))
        code, out = self.run_main(check_site_data.main)
        self.assertEqual(code, 1)
        self.assertIn("site/llms.txt", out)


class WiringTest(unittest.TestCase):
    def test_every_published_file_is_ignored_by_git(self):
        for name in (*assemble_site.RUNTIME_FILES, "stats.json", "api/v1/index.json", "api/v1/patterns/overview.json"):
            done = subprocess.run(["git", "check-ignore", "-q", f"site/{name}"], cwd=ROOT)
            self.assertEqual(done.returncode, 0, f"site/{name} is built at deploy and must never be committed")

    def test_pages_redeploys_when_a_published_source_changes(self):
        text = (ROOT / ".github" / "workflows" / "pages.yml").read_text()
        paths = text.split("    paths:\n", 1)[1].split("\n  workflow_dispatch:", 1)[0]
        for name in assemble_site.RUNTIME_FILES:
            source = "schema/**" if name.startswith("schema/") else name
            self.assertIn(f'      - "{source}"\n', paths, name)
        for rel in site_api.BY_PATH:
            self.assertIn(f'      - "{rel}"\n', paths, rel)

    def test_llms_txt_gives_the_pages_urls_before_the_raw_ones(self):
        section = (ROOT / "llms.txt").read_text().split("## Machine-readable data", 1)[1].split("\n## ", 1)[0]
        pages = section.index("https://kydlikebtc.github.io/awesome-jev/api/v1/index.json")
        self.assertIn("https://kydlikebtc.github.io/awesome-jev/api/v1/patterns/", section)
        self.assertIn("https://kydlikebtc.github.io/awesome-jev/retired.json", section)
        self.assertIn("https://kydlikebtc.github.io/awesome-jev/schema/entry.schema.json", section)
        self.assertLess(pages, section.index("https://raw.githubusercontent.com/"))

    def test_the_skill_falls_back_to_pages_before_raw_github(self):
        text = (ROOT / "skills" / "awesome-jev" / "SKILL.md").read_text()
        fallback = text.split("Without it", 1)[1].split("\n## ", 1)[0]
        pages = fallback.index("https://kydlikebtc.github.io/awesome-jev/api/v1/index.json")
        self.assertLess(pages, fallback.index("https://raw.githubusercontent.com/"))


if __name__ == "__main__":
    unittest.main()
