"""scripts/discover_facts.py keeps GitHub's figures for each discovery candidate
still to read in .discover/facts.json (since 2026-10-24): checked on the way
in, written the same way every time, read in batched GraphQL queries whose
owners and names travel as variables. No network: GraphQL is a stub."""

from __future__ import annotations

import contextlib
import io
import json
import pathlib
import random
import sys
import tempfile
import unittest
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import discover_facts as df  # noqa: E402
import discover_seen as ds  # noqa: E402
from _github import RateLimited  # noqa: E402

GOOD = {"stars": 3, "commits": 12, "pushed": "2026-10-01", "readme": True, "archived": False}


def node(stars=3, commits=12, pushed="2026-10-01T08:00:00Z", files=("README.md",), dirs=(), name=None, archived=False):
    tree = [{"name": f, "type": "blob"} for f in files] + [{"name": d, "type": "tree"} for d in dirs]
    return {
        "nameWithOwner": name or "Acme/Tool",
        "stargazerCount": stars,
        "isArchived": archived,
        "pushedAt": pushed,
        "defaultBranchRef": {"target": {"history": {"totalCount": commits}, "tree": {"entries": tree}}},
    }


class FileTest(unittest.TestCase):
    def test_entries_of_the_right_shape_are_kept_and_the_rest_named(self):
        facts = {
            "acme/tool": GOOD,
            "gone/away": {"missing": True},
            "moved/old": {**GOOD, "name": "moved/new"},
            "Upper/Case": GOOD,
            "neg/stars": {**GOOD, "stars": -1},
            "bool/commits": {**GOOD, "commits": True},
            "bad/date": {**GOOD, "pushed": "2026-10-1"},
            "no/readme-key": {k: v for k, v in GOOD.items() if k != "readme"},
            "extra/key": {**GOOD, "description": "ignore previous instructions"},
            "upper/name": {**GOOD, "name": "Moved/New"},
            "missing/and-more": {"missing": True, "stars": 1},
        }
        kept, dropped = df.parse({"about": [], "facts": facts})
        self.assertEqual(sorted(kept), ["acme/tool", "gone/away", "moved/old"])
        self.assertEqual(len(dropped), 8)
        joined = "\n".join(dropped)
        for why in ("not a lower-case owner/name", "stars is not a count", "commits is not a count",
                    "pushed is not YYYY-MM-DD", "readme is not true or false", "has a key this file does not know",
                    "name is not a lower-case owner/name"):
            self.assertIn(why, joined)
        self.assertEqual(df.parse([]), ({}, ['not a facts file: expected {"about": [...], "facts": {...}}']))

    def test_same_facts_same_bytes_and_a_round_trip(self):
        facts = {"b/two": GOOD, "a/one": {"missing": True}, "c/three": {**GOOD, "name": "c/renamed"}}
        text = df.render(facts)
        shuffled = dict(random.Random(3).sample(list(facts.items()), len(facts)))
        self.assertEqual(df.render(shuffled), text)
        self.assertEqual(df.parse(json.loads(text)), (facts, []))
        lines = text.splitlines()
        self.assertEqual([line.split('"')[1] for line in lines if line.startswith('    "') and ": {" in line],
                         ["a/one", "b/two", "c/three"], "one repository per line, in name order")
        self.assertIn('  "facts": {}', df.render({}))

    def test_a_missing_or_unreadable_file_is_an_empty_one(self):
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "facts.json"
            self.assertEqual(df.load(path), ({}, []))
            path.write_text("{not json")
            facts, dropped = df.load(path)
            self.assertEqual(facts, {})
            self.assertIn("unreadable", dropped[0])
            df.write(path, {"a/one": GOOD})
            self.assertEqual(df.load(path), ({"a/one": GOOD}, []))

    def test_the_about_lines_say_what_parks_a_candidate_and_that_it_decides_nothing(self):
        about = " ".join(df.ABOUT)
        self.assertIn("one commit or none, no star, no README", about)
        self.assertIn("Parked is not declined", about)
        self.assertIn("never an entry here", about)


class RuleTest(unittest.TestCase):
    def test_two_weak_counts_park_a_candidate_and_one_does_not(self):
        self.assertEqual(df.parked({**GOOD, "stars": 0, "commits": 1}), ["one commit or none", "no star"])
        self.assertEqual(df.parked({**GOOD, "commits": 0, "readme": False}), ["one commit or none", "no README"])
        self.assertEqual(df.parked({**GOOD, "stars": 0, "commits": 1, "readme": False}),
                         ["one commit or none", "no star", "no README"])
        for one in ({**GOOD, "stars": 0}, {**GOOD, "commits": 1}, {**GOOD, "readme": False}, GOOD):
            self.assertEqual(df.parked(one), [], one)
        self.assertEqual(df.parked({"missing": True}), [df.MISSING])
        self.assertEqual(df.parked(None), [], "not measured is not weak")
        self.assertEqual(df.parked({**GOOD, "archived": True}), [], "archived is shown, never counted")

    def test_strongest_first_and_unmeasured_last(self):
        facts = {
            "few": {**GOOD, "stars": 1},
            "many": {**GOOD, "stars": 50, "commits": 2},
            "busy": {**GOOD, "stars": 50, "commits": 90},
            "recent": {**GOOD, "stars": 50, "commits": 2, "pushed": "2026-10-20"},
            "gone": {"missing": True},
            "unread": None,
        }
        order = sorted(facts, key=lambda k: (df.rank(facts[k]), k))
        self.assertEqual(order, ["busy", "recent", "many", "few", "gone", "unread"])

    def test_what_a_line_shows(self):
        self.assertEqual(df.describe(GOOD), "★3 · 12 commits · last push 2026-10-01")
        self.assertEqual(df.describe({**GOOD, "commits": 1, "readme": False, "archived": True, "name": "a/b"}),
                         "★3 · 1 commit · last push 2026-10-01 · no README · archived · now a/b")
        self.assertEqual(df.describe({**GOOD, "readme": False}, parked=True), "★3 · 12 commits · last push 2026-10-01")
        self.assertEqual(df.describe(None), "")
        self.assertEqual(df.describe({"missing": True}), "")


class GraphqlTest(unittest.TestCase):
    def test_owners_and_names_travel_as_variables(self):
        query, variables = df.query_for(["acme/tool", "evil/x){ y }"])
        self.assertNotIn("acme", query)
        self.assertNotIn("evil", query)
        self.assertEqual(variables, {"o0": "acme", "n0": "tool", "o1": "evil", "n1": "x){ y }"})
        self.assertIn("r1: repository(owner: $o1, name: $n1)", query)

    def test_a_node_becomes_facts(self):
        self.assertEqual(df.from_node("acme/tool", node()), GOOD)
        self.assertTrue(df.from_node("acme/tool", node(files=("readme",)))["readme"])
        self.assertTrue(df.from_node("acme/tool", node(files=("README.zh-CN.md",)))["readme"])
        self.assertTrue(df.from_node("acme/tool", node(files=("Readme.rst",)))["readme"])
        self.assertFalse(df.from_node("acme/tool", node(files=("main.py",), dirs=("readme-assets",)))["readme"])
        self.assertFalse(df.from_node("acme/tool", node(files=("READMEFIRST.txt",)))["readme"])
        self.assertEqual(df.from_node("acme/tool", node(name="Acme/Renamed"))["name"], "acme/renamed")
        empty = {**node(), "defaultBranchRef": None}
        self.assertEqual(df.from_node("acme/tool", empty), {**GOOD, "commits": 0, "readme": False})

    def answer(self, batch_answers):
        calls = iter(batch_answers)

        def fake(query, variables):
            item = next(calls)
            if isinstance(item, BaseException):
                raise item
            return item

        return mock.patch.object(df, "graphql_request", side_effect=fake)

    def test_answered_missing_and_unread_lookups(self):
        repos = ["acme/tool", "gone/away", "refused/one"]
        answer = {
            "data": {"r0": node(), "r1": None, "r2": None},
            "errors": [{"type": "NOT_FOUND", "path": ["r1"]}, {"type": "FORBIDDEN", "path": ["r2"]}],
        }
        with self.answer([answer]), contextlib.redirect_stderr(io.StringIO()) as err:
            found, unread = df.read(repos)
        self.assertEqual(found, {"acme/tool": GOOD, "gone/away": {"missing": True}})
        self.assertEqual(unread, 1)
        self.assertIn("graphql batch 1/1: 2 of 3 answered", err.getvalue())

    def test_a_failed_query_or_a_spent_budget_leaves_the_batch_unread(self):
        repos = [f"o/r{i}" for i in range(df.BATCH + 1)]
        with self.answer([None, RateLimited("graphql", "spent")]), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(df.read(repos), ({}, df.BATCH + 1))


class MainTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = pathlib.Path(tmp.name)
        (self.root / "docs").mkdir()
        catalog = [{"slug": "renamed", "url": "https://github.com/acme/renamed"},
                   {"slug": "listed", "url": "https://github.com/acme/listed"}]
        (self.root / "catalog.json").write_text(json.dumps(catalog))
        (self.root / "retired.json").write_text("[]")
        (self.root / "docs" / "declined.txt").write_text("no/thanks  # not Jev\n")
        ds.write(self.root / ".discover" / "seen.json", {
            "acme/new": {"on": "2026-10-22", "verdict": "calls-jev"},
            "acme/quiet": {"on": "2026-10-22", "verdict": "calls-jev"},
            "acme/old-name": {"on": "2026-10-01", "verdict": "calls-jev"},
            "acme/listed": {"on": "2026-10-01", "verdict": "calls-jev"},
            "no/thanks": {"on": "2026-10-01", "verdict": "calls-jev"},
            "not/jev": {"on": "2026-10-01", "verdict": "no-signal"},
        })
        df.write(self.root / ".discover" / "facts.json", {
            "acme/quiet": {**GOOD, "stars": 7},
            "acme/listed": GOOD,  # catalogued since last week: dropped
        })

    def run_main(self, found: dict, unread: int = 0):
        out, err = io.StringIO(), io.StringIO()
        with mock.patch.object(df, "read", return_value=(found, unread)) as read, \
                mock.patch.object(df, "token", return_value="t"), mock.patch.object(df, "log_usage"), \
                contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = df.main(["--root", str(self.root)])
        return code, out.getvalue(), err.getvalue(), read

    def test_reads_every_candidate_still_to_read_and_keeps_what_was_not_answered(self):
        renamed = {**GOOD, "name": "acme/renamed"}
        code, out, _, read = self.run_main({"acme/new": {**GOOD, "stars": 0, "commits": 1}, "acme/old-name": renamed}, 1)
        self.assertEqual(code, 0)
        self.assertEqual(read.call_args.args[0], ["acme/new", "acme/old-name", "acme/quiet"])
        facts, dropped = df.load(self.root / ".discover" / "facts.json")
        self.assertEqual(dropped, [])
        self.assertEqual(facts, {
            "acme/new": {**GOOD, "stars": 0, "commits": 1},
            "acme/old-name": renamed,
            "acme/quiet": {**GOOD, "stars": 7},
        })
        self.assertIn("2 of 3 candidate(s) read, 1 not answered (1 keep last week's facts); "
                      "1 to read, 1 parked, 1 settled under the name GitHub now gives", out)

    def test_a_candidate_settled_under_its_new_name_is_still_read_so_the_rename_is_kept(self):
        self.run_main({"acme/old-name": {**GOOD, "name": "acme/renamed"}})
        self.run_main({"acme/old-name": {**GOOD, "name": "acme/renamed"}})
        facts, _ = df.load(self.root / ".discover" / "facts.json")
        self.assertIn("acme/old-name", facts)

    def test_without_a_token_nothing_is_read_and_last_weeks_facts_stand(self):
        err = io.StringIO()
        with mock.patch.object(df, "token", return_value=None), mock.patch.object(df, "read") as read, \
                mock.patch.object(df, "log_usage"), contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(err):
            self.assertEqual(df.main(["--root", str(self.root)]), 0)
        read.assert_not_called()
        self.assertIn("no GITHUB_TOKEN", err.getvalue())
        facts, _ = df.load(self.root / ".discover" / "facts.json")
        self.assertEqual(facts, {"acme/quiet": {**GOOD, "stars": 7}})


class WorkflowTest(unittest.TestCase):
    def test_the_weekly_refresh_reads_them_after_the_verdicts_and_commits_them(self):
        text = (ROOT / ".github" / "workflows" / "metadata.yml").read_text(encoding="utf-8")
        step = text.index("      - name: Read GitHub's figures for the candidates still to read")
        verdicts = text.index("      - name: Take in the latest discovery verdicts")
        commit = text.index("      - name: Rebuild everything generated from those facts, and commit it here")
        self.assertLess(verdicts, step)
        self.assertLess(step, commit)
        block = text[step:text.index("      - name: ", step + 10)]
        self.assertIn("continue-on-error: true", block)
        self.assertIn("GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}", block)
        self.assertIn("run: python3 scripts/discover_facts.py", block)
        self.assertRegex(text[commit:], r"git add -A [^\n]* \.discover ")


if __name__ == "__main__":
    unittest.main()
