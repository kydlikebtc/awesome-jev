"""check_links.py: bare GitHub repositories go through _github's API call (so a
rate limit is a refusal, not a dead link), refusals are counted for GitHub and
for other hosts apart, and every count reaches the job summary. No network."""

from __future__ import annotations

import contextlib
import datetime as dt
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
import check_links  # noqa: E402


class GithubRepoStatusTest(unittest.TestCase):
    def setUp(self):
        _github.reset_usage()
        self.addCleanup(_github.reset_usage)
        env = mock.patch.dict(os.environ, {"GITHUB_TOKEN": "t"})
        env.start()
        self.addCleanup(env.stop)

    def status(self, answer) -> object:
        side = answer if isinstance(answer, BaseException) else None
        with mock.patch.object(_github, "api_fetch", return_value=answer, side_effect=side) as fetch:
            result = check_links.github_repo_status("https://github.com/a/b")
        fetch.assert_called_once_with("/repos/a/b")
        return result

    def test_answers(self):
        self.assertEqual(self.status((200, {})), (200, ""))
        self.assertEqual(self.status((404, None)), (404, "repository not found via API"))
        # Blocked, or no answer at all: about us or GitHub, not the page, so
        # the HTML request decides.
        self.assertIsNone(self.status((403, {"message": "Repository access blocked"})))
        self.assertIsNone(self.status((0, None)))

    def test_a_rate_limit_is_a_refusal_not_a_fallback(self):
        status, note = self.status(_github.RateLimited("core", "HTTP 403 again after the wait"))
        self.assertEqual(status, 429)
        self.assertIn(status, check_links.REFUSED)
        self.assertEqual(note, "not checked: GitHub core rate limit: HTTP 403 again after the wait")

    def test_only_bare_roots_with_a_token(self):
        with mock.patch.object(_github, "api_fetch") as fetch:
            self.assertIsNone(check_links.github_repo_status("https://github.com/a/b/blob/main/x.py"))
            with mock.patch.dict(os.environ, {"GITHUB_TOKEN": "", "GH_TOKEN": ""}):
                self.assertIsNone(check_links.github_repo_status("https://github.com/a/b"))
        fetch.assert_not_called()


def rows(github: int, other: int) -> list[dict]:
    out = [{"slug": f"gh-{i:02}", "url": f"https://github.com/o/r{i}"} for i in range(github)]
    out += [{"slug": f"web-{i:02}", "url": f"https://example{i}.org/page"} for i in range(other)]
    return out


class MainTest(unittest.TestCase):
    def run_main(self, catalog: list[dict], answers: dict[str, tuple[int, str]], *argv: str):
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "catalog.json"
            path.write_text(json.dumps(catalog))
            summary = pathlib.Path(tmp) / "summary.md"
            out, err = io.StringIO(), io.StringIO()
            with mock.patch.object(check_links, "CATALOG", path), \
                 mock.patch.object(check_links, "fetch_status", lambda url: answers.get(url, (200, ""))), \
                 mock.patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": str(summary)}), \
                 contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                code = check_links.main(list(argv))
            return code, out.getvalue(), summary.read_text(), json.loads(path.read_text())

    def refuse(self, catalog: list[dict], prefix: str, count: int, status: int = 429) -> dict:
        urls = [e["url"] for e in catalog if e["slug"].startswith(prefix)][:count]
        return {url: (status, "Too Many Requests") for url in urls}

    def test_refusals_are_split_by_host_and_summarised(self):
        catalog = rows(25, 30)
        answers = {**self.refuse(catalog, "gh-", 2), **self.refuse(catalog, "web-", 3, 403)}
        code, out, summary, _ = self.run_main(catalog, answers)
        self.assertEqual(code, 0)
        self.assertIn("refused: 2 of 25 GitHub URLs (8%), 3 of 30 on other hosts (10%)", out)
        self.assertEqual(
            out.rstrip().splitlines()[-1],
            "links: 55 checked: 50 answered 2xx, 0 redirected, 5 refused, 0 dead",
        )
        self.assertIn("## Link sweep", summary)
        self.assertIn("| Refused (401/403/429) | 2 (8%) | 3 (10%) | 5 |", summary)
        self.assertIn("GitHub", summary)

    def test_a_share_over_the_alarm_fails_the_sweep_as_rate_limiting(self):
        catalog = rows(25, 30)
        code, out, summary, _ = self.run_main(catalog, self.refuse(catalog, "gh-", 6))
        self.assertEqual(code, 3)
        self.assertIn("6 of 25 GitHub URLs refused this checker (24% > 20%)", out)
        self.assertIn("rate limiting or blocking of this runner, not dead links", out)
        self.assertIn("rate limiting or blocking of this runner, not dead links", summary)

    def test_exactly_at_the_alarm_is_not_over_it(self):
        catalog = rows(25, 0)
        code, _, _, _ = self.run_main(catalog, self.refuse(catalog, "gh-", 5))
        self.assertEqual(code, 0)

    def test_other_hosts_are_judged_alone(self):
        catalog = rows(25, 30)
        code, out, _, _ = self.run_main(catalog, self.refuse(catalog, "web-", 7, 403))
        self.assertEqual(code, 3)
        self.assertIn("7 of 30 URLs on other hosts refused this checker (23% > 20%)", out)

    def test_a_small_group_raises_no_alarm(self):
        catalog = rows(0, 5)
        code, out, _, _ = self.run_main(catalog, self.refuse(catalog, "web-", 5, 403))
        self.assertEqual(code, 0)
        self.assertIn("5 of 5 on other hosts (100%)", out)

    def test_dead_links_keep_exit_1(self):
        catalog = rows(25, 0)
        answers = {**self.refuse(catalog, "gh-", 6), catalog[-1]["url"]: (404, "repository not found via API")}
        code, out, _, _ = self.run_main(catalog, answers)
        self.assertEqual(code, 1)
        self.assertIn("1 dead link(s)", out)
        self.assertIn("not dead links", out, "the alarm is still said")

    def test_write_stamps_only_what_answered(self):
        catalog = rows(2, 1)
        answers = {catalog[0]["url"]: (429, ""), catalog[2]["url"]: (301, "")}
        code, out, _, written = self.run_main(catalog, answers, "--write")
        self.assertEqual(code, 0)
        today = dt.date.today().isoformat()
        self.assertEqual([e.get("checked") for e in written], [None, today, None])
        self.assertEqual(
            out.rstrip().splitlines()[-1],
            "links: 3 checked: 1 answered 2xx (stamped), 1 redirected, 1 refused, 0 dead",
        )

    def test_nothing_to_check_still_reports(self):
        code, out, _, _ = self.run_main(rows(1, 0), {}, "--only", "no-such-host")
        self.assertEqual(code, 0)
        self.assertIn("links: 0 checked", out)


class IssueBodyTest(unittest.TestCase):
    """--markdown: the body links.yml keeps its issue with (since 2026-10-24)."""

    run_main = MainTest.run_main
    refuse = MainTest.refuse

    def body(self, catalog: list[dict], answers: dict) -> tuple[int, str]:
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "body.md"
            code, _, _, _ = self.run_main(catalog, answers, "--markdown", str(path))
            return code, path.read_text(encoding="utf-8")

    def test_dead_links_and_redirects_are_listed_with_what_to_do(self):
        catalog = rows(25, 3)
        answers = {
            catalog[0]["url"]: (404, "repository not found via API"),
            catalog[-1]["url"]: (0, "timed out"),
            catalog[-2]["url"]: (301, ""),
        }
        code, body = self.body(catalog, answers)
        self.assertEqual(code, 1)
        self.assertIn("### Dead links (2)", body)
        self.assertIn("| `gh-00` | 404 | <https://github.com/o/r0> (repository not found via API) |", body)
        self.assertIn("| `web-02` | --- | <https://example2.org/page> (timed out) |", body)
        self.assertIn("`retired.json` with a `notes` line", body)
        self.assertIn("### Redirects (1)", body)
        self.assertNotIn("### Refused", body, "a few refusals are every week's noise")
        self.assertTrue(body.rstrip().endswith("2 dead\n```"), body[-200:])

    def test_refusals_are_listed_only_past_the_alarm(self):
        catalog = rows(25, 0)
        code, body = self.body(catalog, self.refuse(catalog, "gh-", 6))
        self.assertEqual(code, 3)
        self.assertIn("**6 of 25 GitHub URLs refused this checker", body)
        self.assertIn("### Refused (6)", body)
        self.assertNotIn("### Dead links", body)

    def test_a_cell_cannot_break_the_table(self):
        self.assertEqual(check_links.cell("a | b\nc"), "a \\| b c")

    def test_a_long_list_is_cut_to_fit_one_comment(self):
        catalog = rows(0, check_links.ISSUE_ROWS + 3)
        answers = {e["url"]: (404, "Not Found") for e in catalog}
        _, body = self.body(catalog, answers)
        self.assertEqual(body.count("| 404 |"), check_links.ISSUE_ROWS)
        self.assertIn("…and 3 more, in the run's log.", body)
        self.assertLess(len(body), 65_536)


if __name__ == "__main__":
    unittest.main()
