"""refresh_metadata.py: GraphQL batches agree with REST, a blocked repository or
a spent budget costs one row rather than the run, and what was read is written.
No network: the _github calls are replaced."""

from __future__ import annotations

import contextlib
import io
import json
import os
import pathlib
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import _github  # noqa: E402
import refresh_metadata as rm  # noqa: E402


def row(slug: str, repo: str, **extra: object) -> dict:
    return {"slug": slug, "url": f"https://github.com/{repo}", **extra}


# The same four repositories as REST and GraphQL describe them.
REST = {
    "a/mit": {"stargazers_count": 10, "license": {"spdx_id": "MIT"}, "archived": False,
              "full_name": "a/mit", "html_url": "https://github.com/a/mit",
              "description": "Routes support tickets with a choice.",
              "created_at": "2026-09-16T08:00:00Z", "pushed_at": "2026-09-20T10:30:00Z"},
    "a/none": {"stargazers_count": 0, "license": None, "archived": False,
               "full_name": "a/none", "html_url": "https://github.com/a/none",
               "created_at": "2026-09-17T07:03:00Z", "pushed_at": "2026-09-17T07:06:04Z"},
    "a/other": {"stargazers_count": 5, "license": {"spdx_id": "NOASSERTION"}, "archived": True,
                "full_name": "a/other", "html_url": "https://github.com/a/other",
                "created_at": "2019-02-01T00:00:00Z", "pushed_at": "2025-12-31T23:59:59Z"},
    "a/old": {"stargazers_count": 7, "license": {"spdx_id": "Apache-2.0"}, "archived": False,
              "full_name": "b/new", "html_url": "https://github.com/b/new",
              "created_at": "2024-05-05T05:05:05Z", "pushed_at": "2026-09-21T00:00:00Z"},
}
# Commits on each default branch, as the REST Link header and GraphQL's
# history.totalCount both give them (I15). a/none has exactly one.
COMMITS = {"a/mit": 12, "a/none": 1, "a/other": 3, "b/new": 40}


def history(count: int | None) -> dict | None:
    return {"target": {"history": {"totalCount": count}}} if count is not None else None


GRAPHQL = {
    "a/mit": {"nameWithOwner": "a/mit", "url": "https://github.com/a/mit", "stargazerCount": 10,
              "isArchived": False, "licenseInfo": {"spdxId": "MIT"},
              "description": "Routes support tickets with a choice.",
              "createdAt": "2026-09-16T08:00:00Z", "pushedAt": "2026-09-20T10:30:00Z",
              "defaultBranchRef": history(12)},
    "a/none": {"nameWithOwner": "a/none", "url": "https://github.com/a/none", "stargazerCount": 0,
               "isArchived": False, "licenseInfo": None,
               "createdAt": "2026-09-17T07:03:00Z", "pushedAt": "2026-09-17T07:06:04Z",
               "defaultBranchRef": history(1)},
    "a/other": {"nameWithOwner": "a/other", "url": "https://github.com/a/other", "stargazerCount": 5,
                "isArchived": True, "licenseInfo": {"spdxId": "NOASSERTION"},
                "createdAt": "2019-02-01T00:00:00Z", "pushedAt": "2025-12-31T23:59:59Z",
                "defaultBranchRef": history(3)},
    "a/old": {"nameWithOwner": "b/new", "url": "https://github.com/b/new", "stargazerCount": 7,
              "isArchived": False, "licenseInfo": {"spdxId": "Apache-2.0"},
              "createdAt": "2024-05-05T05:05:05Z", "pushedAt": "2026-09-21T00:00:00Z",
              "defaultBranchRef": history(40)},
}


def link_to_page(count: int) -> dict:
    """The headers GitHub sends with `/commits?per_page=1`: a rel="last" link to
    page `count`. For one commit GitHub was seen sending a rel="last" link to
    page 1 as well; none at all is the other case rest_commits() must count."""
    if count <= 1:
        return {}
    base = "https://api.github.com/repositories/1/commits?per_page=1"
    return {"Link": f'<{base}&page=2>; rel="next", <{base}&page={count}>; rel="last"'}


def commits_answer(path: str):
    """A fake _github.api_response for `/repos/{repo}/commits?per_page=1`."""
    repo = path.removeprefix("/repos/").removesuffix("/commits?per_page=1")
    count = COMMITS.get(repo)
    if count is None:
        return 409, {"message": "Git Repository is empty."}, {}
    return 200, [{"sha": "0" * 40}], link_to_page(count)


class Quiet(unittest.TestCase):
    def setUp(self):
        _github.reset_usage()
        self.addCleanup(_github.reset_usage)
        self.env = mock.patch.dict(os.environ, {"GITHUB_TOKEN": "t"})
        self.env.start()
        self.addCleanup(self.env.stop)
        os.environ.pop("GITHUB_STEP_SUMMARY", None)
        # fetch() counts commits with a second REST request; never the network.
        counts = mock.patch.object(rm, "api_response", side_effect=commits_answer)
        self.commit_requests = counts.start()
        self.addCleanup(counts.stop)
        self.err = io.StringIO()
        redirect = contextlib.redirect_stderr(self.err)
        redirect.__enter__()
        self.addCleanup(redirect.__exit__, None, None, None)


class FactsTest(Quiet):
    def test_graphql_and_rest_give_the_same_facts(self):
        for repo in REST:
            with self.subTest(repo=repo):
                entry = row("x", repo)
                self.assertEqual(
                    rm.from_graphql(entry, repo, GRAPHQL[repo]),
                    rm.from_rest(entry, repo, REST[repo], COMMITS[REST[repo]["full_name"]]),
                )

    def test_licence_mapping(self):
        self.assertEqual(rm.from_rest(row("x", "a/none"), "a/none", REST["a/none"])["repo_license"], "unknown")
        self.assertEqual(rm.from_graphql(row("x", "a/other"), "a/other", GRAPHQL["a/other"])["repo_license"], "NOASSERTION")

    def test_the_description_is_kept_both_ways(self):
        # I21: summary_source compares the summary with it, so both paths keep it.
        want = "Routes support tickets with a choice."
        self.assertEqual(rm.from_rest(row("x", "a/mit"), "a/mit", REST["a/mit"])["description"], want)
        self.assertEqual(rm.from_graphql(row("x", "a/mit"), "a/mit", GRAPHQL["a/mit"])["description"], want)
        self.assertIsNone(rm.from_rest(row("x", "a/none"), "a/none", {**REST["a/none"], "description": ""})["description"])
        self.assertIsNone(rm.from_graphql(row("x", "a/none"), "a/none", GRAPHQL["a/none"])["description"])
        self.assertIn("description", rm.FIELDS.split())
        self.assertIn("description", rm.COMPARED)


class RepositoryFactsTest(Quiet):
    """I15: GitHub's creation date, last push and default-branch commit count
    are recorded as GitHub states them, over GraphQL and over REST alike, and
    `single-commit` follows the count both ways, as `archived` follows GitHub's
    flag."""

    def test_both_paths_read_the_dates_and_the_count(self):
        fresh = rm.from_graphql(row("x", "a/mit"), "a/mit", GRAPHQL["a/mit"])
        self.assertEqual(
            (fresh["created_at"], fresh["pushed_at"], fresh["commits"]),
            ("2026-09-16T08:00:00Z", "2026-09-20T10:30:00Z", 12),
        )
        for field in ("createdAt", "pushedAt", "defaultBranchRef"):
            self.assertIn(field, rm.FIELDS)
        self.assertIn("history { totalCount }", rm.FIELDS)
        for key in ("created_at", "pushed_at", "commits"):
            self.assertIn(key, rm.COMPARED)

    def test_rest_counts_commits_from_the_link_header(self):
        with mock.patch.object(rm, "api_get", side_effect=lambda path: REST[path.removeprefix("/repos/")]):
            fresh = rm.fetch(row("x", "a/mit"))
        self.assertEqual(fresh["commits"], 12)
        self.assertEqual(self.commit_requests.call_args.args, ("/repos/a/mit/commits?per_page=1",))

    def test_rest_counts_a_one_page_list_without_a_link(self):
        self.assertEqual(rm.rest_commits("a/none"), 1)

    def test_a_renamed_repository_is_counted_under_its_new_name(self):
        with mock.patch.object(rm, "api_get", side_effect=lambda path: REST[path.removeprefix("/repos/")]):
            fresh = rm.fetch(row("x", "a/old"))
        self.assertEqual(fresh["commits"], 40)
        self.assertEqual(self.commit_requests.call_args.args, ("/repos/b/new/commits?per_page=1",))

    def test_an_uncounted_repository_has_no_count(self):
        # Empty (409), blocked (403), no answer (0) and a spent budget all
        # leave the count unknown, and never cost the row its other facts.
        for answer in ((409, {"message": "Git Repository is empty."}, {}), (403, {}, {}), (0, None, None)):
            with self.subTest(status=answer[0]), mock.patch.object(rm, "api_response", return_value=answer):
                self.assertIsNone(rm.rest_commits("a/b"))
        with mock.patch.object(rm, "api_response", side_effect=_github.RateLimited("core", "spent")):
            self.assertIsNone(rm.rest_commits("a/b"))
        with mock.patch.object(rm, "api_get", side_effect=lambda path: REST[path.removeprefix("/repos/")]), \
             mock.patch.object(rm, "api_response", side_effect=_github.RateLimited("core", "spent")):
            fresh = rm.fetch(row("x", "a/mit"))
        self.assertEqual((fresh["state"], fresh["stars"], fresh["commits"]), ("ok", 10, None))
        # GraphQL: an empty repository has no default branch.
        empty = {**GRAPHQL["a/mit"], "defaultBranchRef": None}
        self.assertIsNone(rm.from_graphql(row("x", "a/mit"), "a/mit", empty)["commits"])

    def test_a_count_below_one_is_no_count(self):
        # The schema's minimum is 1: a zero (or a non-number) from either path
        # must leave the row's count and flag alone, not write a row lint fails.
        for bad in (0, -3, "12", None):
            with self.subTest(count=bad):
                node = {**GRAPHQL["a/none"], "defaultBranchRef": {"target": {"history": {"totalCount": bad}}}}
                fresh = rm.from_graphql(row("x", "a/none"), "a/none", node)
                self.assertIsNone(fresh["commits"])
                self.assertIsNone(rm.from_rest(row("x", "a/none"), "a/none", REST["a/none"], bad)["commits"])
                entry = {"slug": "x", "stars": 0, "repo_license": "unknown", "flags": ["no-license"],
                         "repo_created_at": "2026-09-17T07:03:00Z", "repo_pushed_at": "2026-09-17T07:06:04Z",
                         "repo_commits": 4}
                self.assertEqual(rm.diff_for(entry, fresh), [])

    def test_a_date_not_in_githubs_form_is_not_recorded(self):
        for value in (None, "", "2026-09-16", "2026-09-16T08:00:00+00:00", 20260916):
            with self.subTest(value=value):
                self.assertIsNone(rm.timestamp(value))
        self.assertEqual(rm.timestamp("2026-09-16T08:00:00Z"), "2026-09-16T08:00:00Z")

    def fresh(self, repo: str, **overrides) -> dict:
        return {**rm.from_graphql(row("x", repo), repo, GRAPHQL[repo]), **overrides}

    def test_diff_records_the_three_facts_and_apply_places_them_after_the_licence(self):
        entry = {"slug": "x", "stars": 10, "repo_license": "MIT", "evidence": {"path": "a.py", "matched": ["jev"]}}
        fresh = self.fresh("a/mit")
        changes = rm.diff_for(entry, fresh)
        self.assertEqual(changes, [
            ("repo_created_at", None, "2026-09-16T08:00:00Z"),
            ("repo_pushed_at", None, "2026-09-20T10:30:00Z"),
            ("repo_commits", None, 12),
        ])
        rm.apply(entry, fresh, changes)
        self.assertEqual(
            list(entry),
            ["slug", "stars", "repo_license", "repo_created_at", "repo_pushed_at", "repo_commits", "evidence"],
        )
        self.assertEqual(rm.diff_for(entry, fresh), [], "a second run changes nothing")
        # A later push moves only the last push, in place.
        later = self.fresh("a/mit", pushed_at="2026-10-02T09:00:00Z", commits=15)
        changes = rm.diff_for(entry, later)
        self.assertEqual(changes, [
            ("repo_pushed_at", "2026-09-20T10:30:00Z", "2026-10-02T09:00:00Z"),
            ("repo_commits", 12, 15),
        ])
        rm.apply(entry, later, changes)
        self.assertEqual(list(entry)[3:6], ["repo_created_at", "repo_pushed_at", "repo_commits"])
        self.assertEqual((entry["repo_pushed_at"], entry["repo_commits"]), ("2026-10-02T09:00:00Z", 15))

    def test_a_fact_github_did_not_give_leaves_the_row_alone(self):
        entry = {"slug": "x", "stars": 10, "repo_license": "MIT", "repo_created_at": "2026-09-16T08:00:00Z",
                 "repo_pushed_at": "2026-09-20T10:30:00Z", "repo_commits": 1, "flags": ["single-commit"]}
        fresh = self.fresh("a/mit", created_at=None, pushed_at=None, commits=None)
        self.assertEqual(rm.diff_for(entry, fresh), [])

    def test_single_commit_follows_the_count_both_ways(self):
        entry = {"slug": "x", "stars": 0, "repo_license": "unknown", "flags": ["no-license"],
                 "repo_created_at": "2026-09-17T07:03:00Z", "repo_pushed_at": "2026-09-17T07:06:04Z"}
        fresh = self.fresh("a/none")
        changes = rm.diff_for(entry, fresh)
        self.assertEqual(changes, [("repo_commits", None, 1), ("flags", "single-commit", "add")])
        rm.apply(entry, fresh, changes)
        self.assertEqual(entry["flags"], ["no-license", "single-commit"])
        second = self.fresh("a/none", commits=2)
        changes = rm.diff_for(entry, second)
        self.assertEqual(changes, [("repo_commits", 1, 2), ("flags", "single-commit", "remove")])
        rm.apply(entry, second, changes)
        self.assertEqual(entry["flags"], ["no-license"])
        # More than one commit and no flag: nothing, or only the count, moves.
        self.assertEqual(rm.diff_for(entry, second), [])
        self.assertEqual(rm.diff_for(entry, self.fresh("a/none", commits=3)), [("repo_commits", 2, 3)])
        # The flag is the only one: removing it removes the key, as for `archived`.
        alone = {"slug": "x", "repo_commits": 1, "flags": ["single-commit"]}
        rm.apply(alone, second, rm.diff_for(alone, self.fresh("a/mit", commits=2, stars=None, repo_license=None,
                                                                   created_at=None, pushed_at=None)))
        self.assertNotIn("flags", alone)

    def test_the_flag_goes_with_the_count_under_only_field(self):
        self.assertEqual(rm.change_kind(("flags", "single-commit", "add")), "repo_commits")
        self.assertEqual(rm.change_kind(("flags", "archived", "add")), "flags")
        self.assertEqual(rm.change_kind(("flags", "no-license", "remove")), "flags")
        self.assertEqual(rm.change_kind(("repo_pushed_at", None, "x")), "repo_pushed_at")
        for field in rm.REPO_FACTS:
            self.assertIn(field, rm.CHANGE_FIELDS)

    def test_the_digest_counts_repository_activity_and_lists_a_new_creation_date(self):
        def change(field, a, b):
            return {"field": field, "from": a, "to": b}

        report = [
            {"slug": "a", "repo": "o/a", "changes": [change("repo_pushed_at", "2026-09-20T10:30:00Z", "2026-10-02T09:00:00Z"),
                                                    change("repo_commits", 12, 15), change("stars", 1, 2)]},
            {"slug": "b", "repo": "o/b", "changes": [change("repo_created_at", None, "2026-09-16T08:00:00Z")]},
            {"slug": "c", "repo": "o/c", "changes": [change("repo_created_at", "2026-09-16T08:00:00Z", "2026-10-01T00:00:00Z")]},
            {"slug": "d", "repo": "o/d", "changes": [change("repo_commits", None, 1), change("flags", "single-commit", "add")]},
        ]
        text = rm.digest(report, [], 4)
        self.assertIn("3 rows record a new last push, commit count or first creation date", text)
        self.assertIn("**Worth a look before merging:**", text)
        self.assertIn("- `c` (o/c): repo_created_at 2026-09-16T08:00:00Z → 2026-10-01T00:00:00Z\n", text)
        self.assertIn("- `d` (o/d): flag `single-commit` add\n", text)
        self.assertNotIn("`a`", text, "a push and a commit count are counted, not listed")
        self.assertNotIn("`b`", text, "a creation date recorded for the first time is counted, not listed")
        self.assertNotIn("Nothing but star counts moved", text)
        quiet = rm.digest(report[:1], [], 1)
        self.assertNotIn("Worth a look", quiet)
        self.assertNotIn("Nothing but star counts moved", quiet)


class SummarySourceTest(unittest.TestCase):
    """I21: summary_source records whether the summary is the repository's own
    description. Identical labels it; a labelled summary that stops matching is
    stale; `curated` is a person's, `model-written` a model's, and neither is
    ever written or overwritten here."""

    SAME = "Routes support tickets with a choice."

    def source(self, current, summary, description):
        entry = {"slug": "x", "summary": summary}
        if current is not None:
            entry["summary_source"] = current
        return rm.summary_source_for(entry, description)

    def test_the_rules(self):
        up, stale, curated, model = rm.UPSTREAM, rm.UPSTREAM_STALE, rm.CURATED, rm.MODEL_WRITTEN
        other = "A different sentence someone wrote."
        cases = [
            # current, description,          expected
            (None,    self.SAME,               up),
            (None,    other,                   None),
            (None,    None,                    None),
            (None,    "",                      None),
            (up,      self.SAME,               None),
            (up,      other,                   stale),
            (up,      None,                    stale),
            (stale,   self.SAME,               up),
            (stale,   other,                   None),
            (curated, self.SAME,               None),
            (curated, other,                   None),
            (curated, None,                    None),
            (model,   self.SAME,               None),
            (model,   other,                   None),
            (model,   None,                    None),
        ]
        for current, description, expected in cases:
            with self.subTest(current=current, description=description):
                self.assertEqual(self.source(current, self.SAME, description), expected)

    def test_case_whitespace_and_one_final_full_stop_do_not_count(self):
        for description in (
            "routes SUPPORT tickets with a choice",
            "Routes  support\ttickets with a choice.",
            "  Routes support tickets with a choice . ",
        ):
            with self.subTest(description=description):
                self.assertEqual(self.source(None, self.SAME, description), rm.UPSTREAM)
        self.assertEqual(self.source(None, "按意图路由工单。", "按意图路由工单"), rm.UPSTREAM)

    def test_nothing_else_is_forgiven(self):
        for description in (
            "Routes support tickets with a choice and a score.",  # the summary was cut short
            "Routes support tickets with a choice..",            # two full stops
            "Routes support tickets - with a choice.",           # one character changed
        ):
            with self.subTest(description=description):
                self.assertIsNone(self.source(None, self.SAME, description))

    def test_curated_and_model_written_are_never_produced(self):
        for current in (None, rm.CURATED, rm.UPSTREAM, rm.UPSTREAM_STALE, rm.MODEL_WRITTEN):
            for description in (self.SAME, "Other.", None):
                with self.subTest(current=current, description=description):
                    self.assertNotIn(self.source(current, self.SAME, description), rm.WRITTEN_HERE)

    def test_a_row_without_a_summary_is_left_alone(self):
        self.assertIsNone(rm.summary_source_for({"slug": "x"}, self.SAME))

    def test_diff_and_apply_place_the_field_after_summary(self):
        entry = {"slug": "x", "summary": self.SAME, "summary_zh": "路由工单", "stars": 10, "repo_license": "MIT"}
        # GitHub gives no dates or count here (I15), so only the label moves.
        fresh = rm.from_rest(entry, "a/mit", {**REST["a/mit"], "created_at": None, "pushed_at": None})
        changes = rm.diff_for(entry, fresh)
        self.assertEqual(changes, [("summary_source", None, rm.UPSTREAM)])
        rm.apply(entry, fresh, changes)
        self.assertEqual(list(entry), ["slug", "summary", "summary_source", "summary_zh", "stars", "repo_license"])
        self.assertEqual(entry["summary_source"], rm.UPSTREAM)
        # A value already present keeps its place.
        entry["summary"] = "Rewritten by hand."
        changes = rm.diff_for(entry, fresh)
        self.assertEqual(changes, [("summary_source", rm.UPSTREAM, rm.UPSTREAM_STALE)])
        rm.apply(entry, fresh, changes)
        self.assertEqual(list(entry)[2], "summary_source")
        self.assertEqual(entry["summary_source"], rm.UPSTREAM_STALE)


class RestTest(Quiet):
    def test_blocked_is_its_own_state(self):
        blocked = {"blocked": True, "status": 403, "message": "Repository access blocked"}
        with mock.patch.object(rm, "api_get", return_value=blocked):
            fresh = rm.fetch(row("x", "a/b"))
        self.assertEqual(fresh["state"], "blocked")
        self.assertEqual(fresh["detail"], "HTTP 403: Repository access blocked")

    def test_a_rate_limit_skips_the_row_instead_of_ending_the_run(self):
        with mock.patch.object(rm, "api_get", side_effect=_github.RateLimited("core", "spent")):
            self.assertEqual(rm.fetch(row("x", "a/b"))["state"], "skipped")

    def test_missing_is_gone(self):
        with mock.patch.object(rm, "api_get", return_value=None):
            self.assertEqual(rm.fetch(row("x", "a/b"))["state"], "gone")


class GraphqlBatchTest(Quiet):
    def answer(self, found: dict[str, dict]):
        """A fake graphql_request answering each alias from `found`."""
        calls = []

        def fake(query, variables):
            calls.append(variables)
            data = {"rateLimit": {"cost": 1, "remaining": 4999}}
            errors = []
            for key, owner in variables.items():
                if not key.startswith("o"):
                    continue
                alias = "r" + key[1:]
                repo = f"{owner}/{variables['n' + key[1:]]}"
                data[alias] = found.get(repo)
                if repo not in found:
                    errors.append({"type": "NOT_FOUND", "path": [alias]})
            return {"data": data, "errors": errors}

        return fake, calls

    def test_batches_of_fifty_with_variables_not_interpolation(self):
        # Fifty since the commit count joined the query (I15): a hundred took
        # 9-10 s, at GitHub's 10-second limit.
        self.assertEqual(rm.BATCH, 50)
        rows = [row(f"r{i}", f"o/n{i}") for i in range(125)]
        found = {f"o/n{i}": {**GRAPHQL["a/mit"], "nameWithOwner": f"o/n{i}"} for i in range(125)}
        fake, calls = self.answer(found)
        with mock.patch.object(rm, "graphql_request", side_effect=fake), \
             mock.patch.object(rm, "api_get") as rest:
            results = rm.fetch_all(rows, via="graphql")
        self.assertEqual([len(c) // 2 for c in calls], [50, 50, 25])
        self.assertEqual(rest.call_count, 0)
        self.assertTrue(all(r["state"] == "ok" for r in results))
        query = rm.query_for([("o/n0", 0)])[0]
        self.assertIn("repository(owner: $o0, name: $n0)", query)
        self.assertNotIn('"o"', query)

    def test_an_alias_graphql_could_not_answer_is_read_over_rest(self):
        rows = [row("mit", "a/mit"), row("gone", "a/gone"), row("blocked", "a/blocked")]
        fake, _ = self.answer({"a/mit": GRAPHQL["a/mit"]})
        rest = {"a/gone": None, "a/blocked": {"blocked": True, "status": 451, "message": "DMCA"}}
        with mock.patch.object(rm, "graphql_request", side_effect=fake), \
             mock.patch.object(rm, "api_get", side_effect=lambda path: rest[path.removeprefix("/repos/")]):
            results = rm.fetch_all(rows, via="graphql")
        self.assertEqual([r["state"] for r in results], ["ok", "gone", "blocked"])

    def test_an_answer_without_the_facts_is_read_over_rest(self):
        rows = [row("mit", "a/mit")]
        fake, _ = self.answer({"a/mit": {"nameWithOwner": "a/mit"}})
        with mock.patch.object(rm, "graphql_request", side_effect=fake), \
             mock.patch.object(rm, "api_get", side_effect=lambda path: REST[path.removeprefix("/repos/")]) as rest:
            results = rm.fetch_all(rows, via="graphql")
        self.assertEqual(rest.call_count, 1)
        self.assertEqual(results, [rm.from_rest(rows[0], "a/mit", REST["a/mit"], COMMITS["a/mit"])])

    def test_a_failed_or_rate_limited_query_falls_back_to_rest(self):
        rows = [row("mit", "a/mit"), row("other", "a/other")]
        for failure in (None, _github.RateLimited("graphql", "spent")):
            with self.subTest(failure=failure):
                side = [failure] if isinstance(failure, BaseException) else None
                with mock.patch.object(rm, "graphql_request", return_value=failure, side_effect=side), \
                     mock.patch.object(rm, "api_get", side_effect=lambda path: REST[path.removeprefix("/repos/")]):
                    results = rm.fetch_all(rows, via="graphql")
                self.assertEqual(results, [rm.from_rest(rows[0], "a/mit", REST["a/mit"], COMMITS["a/mit"]),
                                           rm.from_rest(rows[1], "a/other", REST["a/other"], COMMITS["a/other"])])

    def test_rest_only_when_asked(self):
        with mock.patch.object(rm, "graphql_request") as gql, \
             mock.patch.object(rm, "api_get", side_effect=lambda path: REST[path.removeprefix("/repos/")]):
            rm.fetch_all([row("mit", "a/mit")], via="rest")
        gql.assert_not_called()

    def test_compare_reports_any_field_that_differs(self):
        rows = [row("mit", "a/mit"), row("other", "a/other")]
        fake, _ = self.answer({"a/mit": GRAPHQL["a/mit"], "a/other": {**GRAPHQL["a/other"], "stargazerCount": 6}})
        with mock.patch.object(rm, "graphql_request", side_effect=fake), \
             mock.patch.object(rm, "api_get", side_effect=lambda path: REST[path.removeprefix("/repos/")]):
            differences = rm.compare(rows)
        self.assertEqual(differences, ["other (a/other): stars rest=5 graphql=6"])


class MainTest(Quiet):
    """The whole script against a temporary catalogue."""

    def run_main(self, catalog: list[dict], answers: dict, *argv: str) -> tuple[int, str, list[dict], str]:
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "catalog.json"
            path.write_text(json.dumps(catalog, indent=2) + "\n")
            digest = pathlib.Path(tmp) / "digest.md"

            def api(path_: str):
                value = answers[path_.removeprefix("/repos/")]
                if isinstance(value, BaseException):
                    raise value
                return value

            out = io.StringIO()
            with mock.patch.object(rm, "CATALOG", path), mock.patch.object(rm, "api_get", side_effect=api), \
                 mock.patch.object(sys, "argv", ["refresh_metadata.py", "--via", "rest", "--digest", str(digest), *argv]), \
                 contextlib.redirect_stdout(out):
                code = rm.main()
            return code, out.getvalue(), json.loads(path.read_text()), digest.read_text()

    def test_a_spent_budget_still_writes_what_was_read(self):
        catalog = [
            row("a-mit", "a/mit", stars=1, repo_license="MIT"),
            row("b-late", "a/late", stars=3, repo_license="MIT"),
            row("c-blocked", "a/blocked", stars=4, repo_license="MIT"),
        ]
        answers = {
            "a/mit": REST["a/mit"],
            "a/late": _github.RateLimited("core", "0 of 1000 left"),
            "a/blocked": {"blocked": True, "status": 403, "message": "Repository access blocked"},
        }
        code, out, written, digest = self.run_main(catalog, answers, "--write")
        self.assertEqual(code, 0)
        self.assertEqual(written[0]["stars"], 10, "the row that was read is written")
        self.assertEqual(written[1]["stars"], 3, "the skipped row keeps its facts")
        self.assertEqual(written[2]["stars"], 4)
        self.assertIn("checked 2 of 3 row(s): 1 skipped (GitHub API budget), 1 blocked, 0 did not resolve", out)
        self.assertIn("Re-read 2 of 3 repositories", digest.splitlines()[0])
        self.assertIn("**Worth a look before merging:**", digest)
        self.assertIn("`c-blocked` (a/blocked): GitHub refuses to serve it (HTTP 403: Repository access blocked)", digest)
        self.assertIn("**1 repositories were not re-read**", digest)
        self.assertNotIn("Nothing but star counts moved", digest)

    def test_writes_the_counts_to_the_job_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            summary = pathlib.Path(tmp) / "summary.md"
            with mock.patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": str(summary)}):
                self.run_main([row("a-mit", "a/mit", stars=10, repo_license="MIT")], {"a/mit": REST["a/mit"]})
            text = summary.read_text()
        self.assertIn("## Repository facts", text)
        self.assertIn("checked 1 of 1 row(s): 0 skipped (GitHub API budget), 0 blocked, 0 did not resolve", text)
        self.assertIn("GitHub", text)

    def test_only_field_writes_that_field_and_nothing_else(self):
        # I21's backfill: `--only-field summary_source --write` labels summaries
        # and leaves stars, licences, flags and names exactly as they were.
        catalog = [
            row("a-mit", "a/mit", summary="Routes support tickets with a choice", stars=1, repo_license="GPL-3.0"),
            row("b-old", "a/old", summary="Something else", stars=1, repo_license="MIT", flags=["archived"]),
        ]
        answers = {"a/mit": REST["a/mit"], "a/old": REST["a/old"]}
        code, out, written, digest = self.run_main(catalog, answers, "--write", "--only-field", "summary_source")
        self.assertEqual(code, 0)
        expected = [dict(catalog[0]), dict(catalog[1])]
        rm.put_after(expected[0], "summary_source", rm.UPSTREAM, "summary")
        self.assertEqual(written, expected)
        self.assertEqual(list(written[0])[:4], ["slug", "url", "summary", "summary_source"])
        self.assertIn("summary_source: None -> upstream-description", out)
        self.assertNotIn("stars:", out)
        self.assertIn("applied 1 row(s) of 2", out)
        self.assertIn("only these changes: summary_source", self.err.getvalue())

    def test_only_field_backfills_the_repository_facts_and_nothing_else(self):
        # I15's backfill: the three facts and the single-commit flag, with
        # stars, licences, other flags, names and summaries left as they were.
        catalog = [
            row("a-mit", "a/mit", summary="Routes support tickets with a choice", stars=1, repo_license="GPL-3.0"),
            row("b-none", "a/none", stars=0, repo_license="MIT", flags=["archived"]),
            row("c-old", "a/old", stars=7, repo_license="Apache-2.0", flags=["single-commit"]),
        ]
        answers = {"a/mit": REST["a/mit"], "a/none": REST["a/none"], "a/old": REST["a/old"]}
        argv = ["--write", "--only-field", "repo_created_at", "--only-field", "repo_pushed_at",
                "--only-field", "repo_commits"]
        code, out, written, _ = self.run_main(catalog, answers, *argv)
        self.assertEqual(code, 0)
        for before, after, repo in zip(catalog, written, ("a/mit", "a/none", "b/new")):
            with self.subTest(slug=before["slug"]):
                rest = {k: v for k, v in after.items() if not k.startswith("repo_") or k == "repo_license"}
                expected = dict(before)
                if "flags" in expected:
                    expected["flags"] = [f for f in expected["flags"] if f != "single-commit"]
                    if not expected["flags"]:
                        del expected["flags"]
                self.assertEqual({k: v for k, v in rest.items() if k != "flags"}, {k: v for k, v in expected.items() if k != "flags"})
                self.assertEqual(after["repo_commits"], COMMITS[repo])
                self.assertEqual(after["repo_created_at"], REST[{"b/new": "a/old"}.get(repo, repo)]["created_at"])
        self.assertEqual(written[1]["flags"], ["archived", "single-commit"], "one commit gains the flag, archived kept")
        self.assertNotIn("flags", written[2], "forty commits lose it")
        self.assertEqual(written[0]["stars"], 1)
        self.assertEqual(written[0]["repo_license"], "GPL-3.0")
        self.assertNotIn("summary_source", written[0])
        self.assertIn("url", written[2])
        self.assertEqual(written[2]["url"], "https://github.com/a/old", "a rename is not applied")
        self.assertIn("applied 3 row(s) of 3", out)

    def test_the_digest_counts_labels_and_lists_stale_summaries(self):
        catalog = [
            row("a-mit", "a/mit", summary="Routes support tickets with a choice", stars=1, repo_license="MIT"),
            row("b-other", "a/other", summary="Was the description once.", summary_source=rm.UPSTREAM,
                stars=5, repo_license="NOASSERTION", flags=["archived"]),
        ]
        answers = {"a/mit": REST["a/mit"], "a/other": {**REST["a/other"], "description": "Says something new now."}}
        _, _, written, digest = self.run_main(catalog, answers, "--write")
        self.assertEqual([r.get("summary_source") for r in written], [rm.UPSTREAM, rm.UPSTREAM_STALE])
        self.assertIn("1 summaries are now labelled `upstream-description`", digest)
        self.assertIn("**Worth a look before merging:**", digest)
        self.assertIn("- `b-other` (a/other): summary_source upstream-description → upstream-description-stale", digest)
        self.assertNotIn("`a-mit`", digest, "a label that only records a match is counted, not listed")
        self.assertNotIn("Nothing but star counts moved", digest)

    def test_a_week_of_labels_only_is_not_called_star_counts(self):
        change = {"field": "summary_source", "from": None, "to": rm.UPSTREAM}
        stars = {"field": "stars", "from": 1, "to": 2}
        text = rm.digest([{"slug": "a", "repo": "o/a", "changes": [change, stars]}], [], 1)
        self.assertIn("1 summaries are now labelled `upstream-description`", text)
        self.assertNotIn("Nothing but star counts moved", text)
        self.assertNotIn("Worth a look", text)

    def test_a_listed_row_does_not_list_its_label(self):
        # A licence change is worth a look; the label that came with it is only counted.
        report = [{"slug": "a", "repo": "o/a", "changes": [
            {"field": "repo_license", "from": "MIT", "to": "Apache-2.0"},
            {"field": "summary_source", "from": None, "to": rm.UPSTREAM},
        ]}]
        text = rm.digest(report, [], 1)
        self.assertIn("- `a` (o/a): repo_license MIT → Apache-2.0\n", text)
        self.assertNotIn("summary_source None", text)

    def test_a_quiet_week_digest_is_unchanged(self):
        # The row already records GitHub's dates and count (I15), so only its stars move.
        facts = {"repo_created_at": "2026-09-16T08:00:00Z", "repo_pushed_at": "2026-09-20T10:30:00Z", "repo_commits": 12}
        code, out, _, digest = self.run_main(
            [row("a-mit", "a/mit", stars=9, repo_license="MIT", **facts)], {"a/mit": REST["a/mit"]}
        )
        self.assertEqual(digest.splitlines()[0], "Re-read 1 repositories: 1 rows changed, 1 of them stars only.")
        self.assertIn("Nothing but star counts moved.", digest)


if __name__ == "__main__":
    unittest.main()
