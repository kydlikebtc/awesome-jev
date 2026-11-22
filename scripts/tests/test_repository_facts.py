"""GitHub's creation date, last push and commit count per row (I15).

method.md said creation dates and last pushes came from the API at the first
build, but no field held them, and `single-commit` sat on two rows while
nothing counted commits. The weekly refresh now records `repo_created_at`,
`repo_pushed_at` and `repo_commits` as GitHub states them and keeps
`single-commit` in step with the count (test_refresh_metadata.py covers the
reading and writing; test_lint.py the rules). Here: one definition of the
three fields, and where they are published. They move every week, so the
READMEs and pattern pages must not depend on them at all, docs/status.md only
through the calendar month of the last push, and nothing anywhere turns them
into an age or a verdict.

One exception came later, on purpose. Since 2026-11-03 the launch board, which
the README has fronted since 2026-11-05, leaves out a quiet product: one whose
repository has had no push for launches.QUIET_DAYS before the newest day the
catalogue records (launches.quiet, docs/launches.md "Rising",
docs/launch-engine.md). That reads the day of the last push and prints nothing
about it. So the README may depend on `repo_pushed_at` through that check and
nothing else: the tests below hold each row's quiet answer fixed while the
facts move, and pin the check itself on a fixture. Until 2026-11-22 no product
the README lists sat on the quiet line, so the older assertion held by chance.
"""

from __future__ import annotations

import copy
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import _stats  # noqa: E402
import build_docs  # noqa: E402
import build_readme  # noqa: E402
import launches  # noqa: E402
import lint  # noqa: E402
import refresh_metadata  # noqa: E402
from readme import strings  # noqa: E402

FIELDS = ("repo_created_at", "repo_pushed_at", "repo_commits")
SCHEMA = json.loads((ROOT / "schema" / "entry.schema.json").read_text(encoding="utf-8"))
# Words that would turn a date into an age or a verdict.
AGE_OR_VERDICT = re.compile(r"\b(?:days? (?:ago|since)|ago\b|stale|abandoned|unmaintained|inactive)", re.I)


def shifted(catalog: list[dict], *, month: str | None = None) -> list[dict]:
    """A copy of the catalogue whose repository facts all moved: every last
    push to another second of its own month (or into `month`), every creation
    date one second on, every count above one up by seven. A count of one stays
    one, so `single-commit` still agrees with it.

    A move inside its own month never carries a push across the board's quiet
    line (launches.quiet, the one deliberate use of the last push: see the
    module docstring). A push the move would carry across it stays on its day
    and moves to another second of that day, which launches.quiet cannot see."""
    out = copy.deepcopy(catalog)
    today = launches.as_of(catalog)
    for entry in out:
        pushed = entry.get("repo_pushed_at")
        if pushed:
            moved = f"{month or pushed[:7]}-{'28' if pushed[8:10] != '28' else '27'}T23:59:59Z"
            if month is None and launches.quiet({"repo_pushed_at": moved}, today) != launches.quiet(entry, today):
                moved = f"{pushed[:10]}T{'00:00:00' if pushed[11:19] != '00:00:00' else '00:00:01'}Z"
            entry["repo_pushed_at"] = moved
        created = entry.get("repo_created_at")
        if created:
            entry["repo_created_at"] = created[:-3] + ("01Z" if created[-3:] != "01Z" else "02Z")
        if isinstance(entry.get("repo_commits"), int) and entry["repo_commits"] > 1:
            entry["repo_commits"] += 7
    return out


class DefinitionTest(unittest.TestCase):
    def test_one_list_of_fields(self):
        self.assertEqual(_stats.REPO_FACTS, FIELDS)
        self.assertEqual(tuple(refresh_metadata.REPO_FACTS), FIELDS)
        self.assertEqual((*lint.REPO_TIMESTAMPS, lint.REPO_COMMITS), FIELDS)

    def test_the_schema_calls_them_githubs_facts_not_a_judgement(self):
        names = list(SCHEMA["properties"])
        at = names.index("repo_license")
        self.assertEqual(names[at + 1 : at + 4], list(FIELDS), "they follow repo_license, as in the rows")
        for field in FIELDS:
            with self.subTest(field=field):
                text = SCHEMA["properties"][field]["description"]
                self.assertIn("A GitHub fact, not a judgement", text)
                self.assertIn("refresh_metadata.py", text)
                self.assertNotIn("verified", text.lower())
        self.assertIn("single-commit", SCHEMA["properties"]["repo_commits"]["description"])

    def test_the_flag_states_the_count_instead_of_guessing(self):
        taxonomy = json.loads((ROOT / "taxonomy.json").read_text(encoding="utf-8"))
        flag = next(item for item in taxonomy["flags"] if item["key"] == "single-commit")
        self.assertNotIn("unlikely", flag["blurb_en"])
        self.assertIn("one commit", flag["blurb_en"])
        self.assertIn("weekly refresh", flag["blurb_en"])
        self.assertTrue(flag["zh_machine"], "the new Chinese is model-written")
        self.assertNotIn("single-commit", lint.FLAGS_NEEDING_NOTES, "a machine-set flag needs no notes line")

    def test_only_the_refresh_writes_them(self):
        write = re.compile(r"""\[\s*["'](?:repo_created_at|repo_pushed_at|repo_commits)["']\s*\]\s*=""")
        for path in sorted(SCRIPTS.rglob("*.py")):
            if "tests" in path.parts:
                continue
            with self.subTest(path=path.name):
                self.assertIsNone(write.search(path.read_text(encoding="utf-8")))


class RealCatalogueTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog, cls.retired, *_ = _stats.load()

    def test_every_recorded_count_agrees_with_the_flag(self):
        counted = [e for e in self.catalog if "repo_commits" in e]
        self.assertGreater(len(counted), 1000, "the backfill recorded them")
        for entry in counted:
            with self.subTest(slug=entry["slug"]):
                self.assertEqual(entry["repo_commits"] == 1, "single-commit" in (entry.get("flags") or []))
                self.assertLessEqual(set(FIELDS), set(entry))

    def test_status_counts_what_the_rows_record(self):
        stats = _stats.compute()
        self.assertEqual(stats["repo_facts_rows"], sum(1 for e in self.catalog if set(FIELDS) <= set(e)))
        self.assertEqual(sum(stats["pushed_by_month"].values()), sum(1 for e in self.catalog if e.get("repo_pushed_at")))
        self.assertEqual(list(stats["pushed_by_month"]), sorted(stats["pushed_by_month"], reverse=True))
        for month in stats["pushed_by_month"]:
            self.assertRegex(month, r"^[0-9]{4}-[0-9]{2}$")

    def test_readmes_and_pattern_pages_do_not_depend_on_them(self):
        moved = shifted(self.catalog, month="2031-01")
        removed = copy.deepcopy(self.catalog)
        for entry in removed:
            for field in FIELDS:
                entry.pop(field, None)
        # The board's quiet check is the README's one allowed reading of the
        # last push (module docstring): each row keeps the answer it has on the
        # real catalogue, and everything else must come out the same.
        today = launches.as_of(self.catalog)
        quiet_now = {e["slug"]: launches.quiet(e, today) for e in self.catalog}

        def as_today(row: dict, _today) -> bool:
            return quiet_now.get(row.get("slug"), False)

        for pack in (strings.EN, strings.ZH):
            base = build_readme.render(copy.deepcopy(self.catalog), copy.deepcopy(self.retired), pack)
            for name, variant in (("moved", moved), ("removed", removed)):
                with self.subTest(lang=pack["lang_code"], variant=name), mock.patch.object(launches, "quiet", as_today):
                    self.assertEqual(base, build_readme.render(copy.deepcopy(variant), copy.deepcopy(self.retired), pack))
        before = build_readme.group_by_pattern(copy.deepcopy(self.catalog))
        after = build_readme.group_by_pattern(copy.deepcopy(moved))
        for key, members in before.items():
            for pack in (strings.EN, strings.ZH):
                with self.subTest(pattern=key, lang=pack["lang_code"]):
                    self.assertEqual(build_readme.render_page(key, members, pack), build_readme.render_page(key, after[key], pack))


class QuietLineTest(unittest.TestCase):
    """The board's quiet check, the one place a last push changes the README."""

    def test_a_product_is_quiet_only_after_its_quiet_days(self):
        today = launches.day("2026-11-22")
        line = today - launches.dt.timedelta(days=launches.QUIET_DAYS)
        self.assertFalse(launches.quiet({"repo_pushed_at": f"{line.isoformat()}T00:45:41Z"}, today))
        before = line - launches.dt.timedelta(days=1)
        self.assertTrue(launches.quiet({"repo_pushed_at": f"{before.isoformat()}T23:59:59Z"}, today))
        self.assertFalse(launches.quiet({}, today), "a row with no recorded push is not called quiet")
        self.assertFalse(launches.quiet({"repo_pushed_at": "2026-01-01T00:00:00Z"}, None))

    def test_rising_leaves_a_quiet_product_out(self):
        def product(slug: str, pushed: str) -> dict:
            return {"slug": slug, "kind": "project", "has_code": True, "first_seen": "2026-11-22",
                    "repo_pushed_at": pushed}

        catalog = [product("busy", "2026-11-20T00:00:00Z"), product("quiet", "2026-09-01T00:00:00Z")]
        before = {"rows": [{"slug": "busy", "stars": 10}, {"slug": "quiet", "stars": 10}]}
        after = {"rows": [{"slug": "busy", "stars": 40}, {"slug": "quiet", "stars": 40}]}
        self.assertEqual([x["row"]["slug"] for x in launches.rising(catalog, before, after)], ["busy"])

    def test_a_move_inside_the_month_keeps_every_quiet_answer(self):
        catalog, *_ = _stats.load()
        today = launches.as_of(catalog)
        moved = shifted(catalog)
        self.assertEqual(launches.as_of(moved), today)
        self.assertEqual([launches.quiet(e, today) for e in moved], [launches.quiet(e, today) for e in catalog])
        pushed = [(a["repo_pushed_at"], b["repo_pushed_at"]) for a, b in zip(catalog, moved) if a.get("repo_pushed_at")]
        self.assertTrue(all(old != new and old[:7] == new[:7] for old, new in pushed), "every push still moves, inside its month")


class StatusBlockTest(unittest.TestCase):
    def test_months_newest_first_and_only_rows_that_record_one(self):
        rows = [
            {"repo_pushed_at": "2026-09-17T07:06:04Z"},
            {"repo_pushed_at": "2026-11-01T00:00:00Z"},
            {"repo_pushed_at": "2026-09-30T23:59:59Z"},
            {},
            {"repo_pushed_at": None},
        ]
        self.assertEqual(_stats.pushed_by_month(rows), {"2026-11": 1, "2026-09": 2})
        block = build_docs.pushed_block({"pushed_by_month": _stats.pushed_by_month(rows)})
        self.assertEqual(
            block,
            "| Month of the last push (UTC) | Rows |\n| --- | --- |\n| 2026-11 | 1 |\n| 2026-09 | 2 |",
        )
        self.assertEqual(build_docs.pushed_block({"pushed_by_month": {}}), "No row records a last push yet.")

    def test_a_push_inside_its_month_changes_nothing_and_no_line_is_an_age(self):
        catalog, *_ = _stats.load()
        same = build_docs.pushed_block({"pushed_by_month": _stats.pushed_by_month(shifted(catalog))})
        self.assertEqual(build_docs.pushed_block({"pushed_by_month": _stats.pushed_by_month(catalog)}), same)
        later = build_docs.pushed_block({"pushed_by_month": _stats.pushed_by_month(shifted(catalog, month="2031-01"))})
        self.assertNotEqual(same, later, "a new month is a new line: the test is not vacuous")
        shape = "\n".join(
            line for line in build_docs.shape_block(_stats.compute()).splitlines()
            if "repo_" in line or "single-commit" in line
        )
        self.assertEqual(len(shape.splitlines()), 2)
        page = build_docs.render()[ROOT / "docs" / "status.md"]
        section = page.split("### When each repository was last pushed", 1)[1].split("### Coverage gaps", 1)[0]
        for text in (same, section, shape):
            self.assertIsNone(AGE_OR_VERDICT.search(text.replace("not whether a project is maintained", "")), text[:200])
        self.assertIn("<!-- pushed:start -->", section)


class SiteAndServerTest(unittest.TestCase):
    def test_the_site_shows_them_in_both_languages(self):
        page = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
        self.assertIn("repositoryFacts(e)", page)
        for key in ("repo_created", "repo_pushed", "repo_commits", "repo_facts_about"):
            with self.subTest(key=key):
                self.assertEqual(len(re.findall(rf"\b{key}:", page)), 2, "one string per language")
        self.assertIn("repository-fact strings below is model-written", page)
        for about in re.findall(r'repo_facts_about: "([^"]+)"', page):
            self.assertIsNone(AGE_OR_VERDICT.search(about), about)


class RegenerateTest(unittest.TestCase):
    """Every generator on a scratch copy: facts that move inside their month
    change no generated file but the README screenshot's cache-buster."""

    CACHE_BUSTER = re.compile(r"\?v=[0-9a-f]+")

    def test_only_the_screenshot_cache_buster_moves(self):
        sys.path.insert(0, str(SCRIPTS / "tests"))
        from test_star_bands import copy_tree, outputs  # noqa: E402

        with tempfile.TemporaryDirectory() as tmp:
            tree = pathlib.Path(tmp)
            copy_tree(tree)

            def run() -> dict[str, str]:
                subprocess.run(
                    [sys.executable, "scripts/regenerate.py"], cwd=tree, check=True, capture_output=True, text=True
                )
                return outputs(tree)

            before = run()
            catalog = json.loads((tree / "catalog.json").read_text(encoding="utf-8"))
            (tree / "catalog.json").write_text(
                json.dumps(shifted(catalog), indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )
            after = run()

        changed = sorted(rel for rel in before if before[rel] != after[rel])
        self.assertEqual(changed, ["README.md", "README.zh-CN.md"])
        for rel in changed:
            with self.subTest(file=rel):
                differing = [(a, b) for a, b in zip(before[rel].splitlines(), after[rel].splitlines()) if a != b]
                self.assertEqual(len(differing), 1, differing[:3])
                a, b = differing[0]
                self.assertEqual(self.CACHE_BUSTER.sub("?v=", a), self.CACHE_BUSTER.sub("?v=", b))


if __name__ == "__main__":
    unittest.main()
