"""scripts/_github.py against a fake urlopen: rate limits, blocked repositories,
budget, timeouts. No network.

GitHub answers an exhausted budget with 403 or 429 and says so in its headers
or body; it answers a repository it will not serve (a DMCA or terms-of-service
block) with 403 or 451 and says nothing about limits. Until 2026-09-27 every 403
stopped the run with SystemExit(2), so one blocked repository ended a weekly
refresh before it had written anything, and a 429 was treated as a missing row.
"""

from __future__ import annotations

import contextlib
import email.message
import io
import json
import os
import pathlib
import socket
import sys
import tempfile
import unittest
import urllib.error
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import _github  # noqa: E402

NOW = 1_790_000_000.0


def headers(**values: object) -> email.message.Message:
    message = email.message.Message()
    for key, value in values.items():
        message[key.replace("_", "-")] = str(value)
    return message


def budget(remaining: int, *, limit: int = 5000, reset: float = NOW + 1800, resource: str = "core") -> dict:
    return {
        "X_RateLimit_Limit": limit,
        "X_RateLimit_Remaining": remaining,
        "X_RateLimit_Reset": int(reset),
        "X_RateLimit_Resource": resource,
    }


class Ok:
    def __init__(self, body: object, **head: object):
        self.status = 200
        self.headers = headers(**head)
        self._body = body if isinstance(body, bytes) else json.dumps(body).encode()

    def read(self) -> bytes:
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def error(code: int, body: object = b"", **head: object) -> urllib.error.HTTPError:
    raw = body if isinstance(body, bytes) else json.dumps(body).encode()
    return urllib.error.HTTPError("https://api.github.com/x", code, "err", headers(**head), io.BytesIO(raw))


class FakeNet:
    """Plays a scripted sequence of answers and records every request."""

    def __init__(self, *answers: object):
        self.answers = list(answers)
        self.requests: list[str] = []

    def __call__(self, request, timeout=None):
        self.requests.append(request.full_url)
        answer = self.answers.pop(0)
        if isinstance(answer, BaseException):
            raise answer
        return answer


class Base(unittest.TestCase):
    def setUp(self):
        _github.reset_usage()
        self.addCleanup(_github.reset_usage)
        self.slept: list[float] = []
        self.now = NOW
        patches = [
            mock.patch.object(_github, "_sleep", self.sleep),
            mock.patch.object(_github, "_now", lambda: self.now),
            mock.patch.dict(os.environ, {"GITHUB_TOKEN": "test-token"}),
        ]
        for patch in patches:
            patch.start()
            self.addCleanup(patch.stop)
        os.environ.pop("GITHUB_STEP_SUMMARY", None)
        self.stderr = io.StringIO()
        redirect = contextlib.redirect_stderr(self.stderr)
        redirect.__enter__()
        self.addCleanup(redirect.__exit__, None, None, None)

    def sleep(self, seconds: float) -> None:
        self.slept.append(seconds)
        self.now += seconds

    def net(self, *answers: object) -> FakeNet:
        fake = FakeNet(*answers)
        patch = mock.patch.object(_github.urllib.request, "urlopen", fake)
        patch.start()
        self.addCleanup(patch.stop)
        return fake


class ApiTest(Base):
    def test_success_returns_the_body_and_records_the_budget(self):
        net = self.net(Ok({"stargazers_count": 3}, **budget(4321)))
        self.assertEqual(_github.api_get("/repos/a/b"), {"stargazers_count": 3})
        self.assertEqual(net.requests, ["https://api.github.com/repos/a/b"])
        window = _github.USAGE.windows["core"]
        self.assertEqual((window.limit, window.remaining), (5000, 4321))
        self.assertEqual(_github.USAGE.requests["core"], 1)

    def test_not_found_is_none_and_is_not_retried(self):
        net = self.net(error(404, {"message": "Not Found"}, **budget(4000)))
        self.assertIsNone(_github.api_get("/repos/a/gone"))
        self.assertEqual(len(net.requests), 1)
        self.assertEqual(self.slept, [])
        self.assertEqual(_github.api_fetch.__name__, "api_fetch")

    def test_a_403_that_names_no_limit_is_a_blocked_repository(self):
        body = {"message": "Repository access blocked", "block": {"reason": "tos"}}
        net = self.net(error(403, body, **budget(4000)))
        self.assertEqual(
            _github.api_get("/repos/a/blocked"),
            {"blocked": True, "status": 403, "message": "Repository access blocked"},
        )
        self.assertEqual(len(net.requests), 1)
        self.assertEqual(self.slept, [])
        self.assertEqual(_github.USAGE.blocked, 1)

    def test_451_is_blocked_too(self):
        self.net(error(451, {"message": "Repository access blocked"}))
        self.assertTrue(_github.api_get("/repos/a/dmca")["blocked"])

    def test_an_empty_budget_waits_for_the_reset_then_retries_once(self):
        net = self.net(
            error(403, {"message": "API rate limit exceeded"}, **budget(0, reset=NOW + 30)),
            Ok({"ok": 1}, **budget(4999, reset=NOW + 3600)),
        )
        self.assertEqual(_github.api_get("/repos/a/b"), {"ok": 1})
        self.assertEqual(len(net.requests), 2)
        self.assertEqual(self.slept, [31])
        self.assertEqual(_github.USAGE.limited, 1)

    def test_an_empty_budget_is_a_limit_whatever_the_message_says(self):
        # The headers alone decide: a 403 with nothing left is not a blocked
        # repository, even when its message does not say "rate limit".
        net = self.net(
            error(403, {"message": "Forbidden"}, **budget(0, reset=NOW + 30)),
            Ok({"ok": 1}, **budget(4999, reset=NOW + 3600)),
        )
        self.assertEqual(_github.api_get("/repos/a/b"), {"ok": 1})
        self.assertEqual(len(net.requests), 2)
        self.assertEqual(self.slept, [31])
        self.assertEqual(_github.USAGE.blocked, 0)

    def test_429_waits_as_long_as_retry_after_says(self):
        net = self.net(error(429, b"", Retry_After=7), Ok({"ok": 1}))
        self.assertEqual(_github.api_get("/repos/a/b"), {"ok": 1})
        self.assertEqual(self.slept, [7])
        self.assertEqual(len(net.requests), 2)

    def test_a_secondary_limit_named_only_in_the_body_waits_a_minute(self):
        body = {"message": "You have exceeded a secondary rate limit. Please wait a few minutes."}
        self.net(error(403, body, **budget(4000)), Ok({"ok": 1}))
        self.assertEqual(_github.api_get("/repos/a/b"), {"ok": 1})
        self.assertEqual(self.slept, [_github.SECONDARY_WAIT])

    def test_a_wait_past_the_cap_is_not_slept_and_later_calls_send_nothing(self):
        net = self.net(error(403, {"message": "API rate limit exceeded"}, **budget(0, reset=NOW + 3000)))
        with self.assertRaises(_github.RateLimited) as caught:
            _github.api_get("/repos/a/b")
        self.assertEqual(self.slept, [])
        self.assertEqual(caught.exception.code, 2, "uncaught, it still stops a run as exit 2")
        self.assertIsInstance(caught.exception, SystemExit)
        with self.assertRaises(_github.RateLimited):
            _github.api_get("/repos/a/c")
        self.assertEqual(len(net.requests), 1)
        self.assertEqual(_github.USAGE.unsent["core"], 1)

    def test_still_limited_after_the_retry_closes_the_budget_for_the_run(self):
        net = self.net(error(429, b"", Retry_After=5), error(429, b"", Retry_After=5))
        with self.assertRaises(_github.RateLimited):
            _github.api_get("/repos/a/b")
        self.assertEqual(self.slept, [5])
        self.assertEqual(len(net.requests), 2)
        self.now += 10_000
        with self.assertRaises(_github.RateLimited):
            _github.api_get("/repos/a/c")
        self.assertEqual(len(net.requests), 2)
        self.assertEqual(self.stderr.getvalue().count("sending nothing more"), 1, self.stderr.getvalue())

    def test_below_the_reserve_nothing_is_sent_until_the_reset(self):
        net = self.net(Ok({"n": 1}, **budget(49, reset=NOW + 600)), Ok({"n": 2}, **budget(4999, reset=NOW + 4200)))
        self.assertEqual(_github.api_get("/repos/a/b"), {"n": 1})
        with self.assertRaises(_github.RateLimited):
            _github.api_get("/repos/a/c")
        self.assertEqual(len(net.requests), 1)
        self.now = NOW + 601
        self.assertEqual(_github.api_get("/repos/a/c"), {"n": 2})

    def test_the_reserve_scales_down_for_a_small_budget(self):
        # Unauthenticated is 60 an hour: a reserve of 50 would stop after ten.
        self.net(Ok({}, **budget(7, limit=60)), Ok({}, **budget(5, limit=60)), Ok({}))
        _github.api_get("/a")
        _github.api_get("/b")
        with self.assertRaises(_github.RateLimited):
            _github.api_get("/c")

    def test_out_of_order_answers_keep_the_lowest_remaining(self):
        self.net(Ok({}, **budget(900)), Ok({}, **budget(950)))
        _github.api_get("/a")
        _github.api_get("/b")
        self.assertEqual(_github.USAGE.windows["core"].remaining, 900)

    def test_servers_that_disagree_on_the_window_count_as_the_lower(self):
        # Seen live: one answer said 4997 left with a later reset, the next
        # eleven said 4965 and falling with an earlier one.
        self.net(Ok({}, **budget(4997, reset=NOW + 1860)), Ok({}, **budget(4965, reset=NOW + 1800)))
        _github.api_get("/a")
        _github.api_get("/b")
        self.assertEqual(_github.USAGE.windows["core"].remaining, 4965)

    def test_a_timeout_is_no_answer(self):
        net = self.net(socket.timeout("timed out"))
        self.assertEqual(_github.api_fetch("/repos/a/b"), (0, None))
        self.assertEqual(len(net.requests), 1)
        self.net(urllib.error.URLError("reset"))
        self.assertIsNone(_github.api_get("/repos/a/b"))

    def test_search_is_its_own_budget(self):
        self.net(Ok({}, **budget(0, limit=30, resource="search")), Ok({"ok": 1}, **budget(4000)))
        _github.api_get("/search/repositories?q=x")
        self.assertEqual(_github.api_get("/repos/a/b"), {"ok": 1})
        with self.assertRaises(_github.RateLimited):
            _github.api_get("/search/repositories?q=y")


class LinkHeaderTest(Base):
    """I15: over REST a branch's commit count is the page number of the
    rel="last" link when asking for one commit per page."""

    LINK = (
        '<https://api.github.com/repositories/70107786/commits?per_page=1&page=2>; rel="next", '
        '<https://api.github.com/repositories/70107786/commits?per_page=1&page=35895>; rel="last"'
    )

    def test_last_page_is_the_count(self):
        self.assertEqual(_github.last_page(self.LINK), 35895)
        self.assertEqual(_github.last_page('<https://x/y?page=1&per_page=1>; rel="last"'), 1)

    def test_no_last_link_is_none(self):
        for link in (None, "", '<https://x/y?per_page=1&page=2>; rel="next"', '<https://x/y>; rel="last"',
                     '<https://x/y?page=0>; rel="last"', '<https://x/y?page=abc>; rel="last"'):
            with self.subTest(link=link):
                self.assertIsNone(_github.last_page(link))

    def test_api_response_returns_the_headers(self):
        self.net(Ok([{"sha": "a"}], Link=self.LINK, **budget(4000)))
        status, data, head = _github.api_response("/repos/vercel/next.js/commits?per_page=1")
        self.assertEqual((status, data), (200, [{"sha": "a"}]))
        self.assertEqual(_github.last_page(head.get("Link")), 35895)
        self.assertEqual(_github.USAGE.requests["core"], 1)

    def test_api_response_on_an_error_keeps_status_and_body(self):
        self.net(error(409, {"message": "Git Repository is empty."}, **budget(4000)))
        status, data, _ = _github.api_response("/repos/a/empty/commits?per_page=1")
        self.assertEqual((status, data), (409, {"message": "Git Repository is empty."}))
        self.net(socket.timeout("timed out"))
        self.assertEqual(_github.api_response("/repos/a/b/commits?per_page=1"), (0, None, None))


class GraphqlTest(Base):
    def test_returns_errors_beside_the_data_and_counts_points(self):
        body = {
            "data": {"r0": {"nameWithOwner": "a/b"}, "r1": None},
            "errors": [{"type": "NOT_FOUND", "path": ["r1"], "message": "Could not resolve"}],
        }
        self.net(Ok(body, **budget(4990, resource="graphql")))
        self.assertEqual(_github.graphql_request("query { x }", {"o0": "a"}), body)
        self.assertEqual(_github.USAGE.windows["graphql"].remaining, 4990)
        self.assertEqual(_github.USAGE.requests["graphql"], 1)

    def test_no_token_sends_nothing(self):
        net = self.net()
        with mock.patch.dict(os.environ, {"GITHUB_TOKEN": "", "GH_TOKEN": ""}):
            self.assertIsNone(_github.graphql_request("query { x }"))
        self.assertEqual(net.requests, [])

    def test_a_server_error_is_retried_once_then_none(self):
        net = self.net(error(502), error(502))
        self.assertIsNone(_github.graphql_request("query { x }"))
        self.assertEqual(len(net.requests), 2)

    def test_a_refusal_is_not_retried(self):
        # A bad token or a refused query will not change on a second try; only
        # a server error or no answer is worth one.
        net = self.net(error(401, {"message": "Bad credentials"}))
        self.assertIsNone(_github.graphql_request("query { x }"))
        self.assertEqual(len(net.requests), 1)
        self.assertEqual(self.slept, [])

    def test_a_200_whose_only_error_is_rate_limited_is_a_rate_limit(self):
        body = {"data": None, "errors": [{"type": "RATE_LIMITED", "message": "API rate limit exceeded"}]}
        net = self.net(Ok(body, **budget(0, resource="graphql")))
        with self.assertRaises(_github.RateLimited) as caught:
            _github.graphql_request("query { x }")
        self.assertEqual(caught.exception.resource, "graphql")
        with self.assertRaises(_github.RateLimited):
            _github.graphql_request("query { y }")
        self.assertEqual(len(net.requests), 1)

    def test_the_informational_wrapper_degrades_a_rate_limit_to_none(self):
        self.net(error(403, {"message": "API rate limit exceeded"}, **budget(0, reset=NOW + 3000, resource="graphql")))
        self.assertIsNone(_github.graphql("{ viewer { login } }"))


class RawTest(Base):
    def test_404_is_none_at_once(self):
        net = self.net(error(404))
        self.assertIsNone(_github.raw_get("a/b", "HEAD", "x.py"))
        self.assertEqual(len(net.requests), 1)
        self.assertEqual(net.requests[0], "https://raw.githubusercontent.com/a/b/HEAD/x.py")

    def test_a_path_outside_ascii_is_percent_encoded(self):
        # jkf87/jev-handson keeps every call site under folders named in
        # Korean; sent unencoded, such a URL cannot leave the machine.
        net = self.net(Ok(b"body"))
        self.assertEqual(_github.raw_get("a/b", "HEAD", "02_라우터/code/mini router.mjs"), "body")
        self.assertEqual(
            net.requests[0],
            "https://raw.githubusercontent.com/a/b/HEAD/02_%EB%9D%BC%EC%9A%B0%ED%84%B0/code/mini%20router.mjs",
        )

    def test_an_ordinary_path_is_sent_unchanged(self):
        net = self.net(Ok(b"body"))
        _github.raw_get("a/b", "main", "packages/@scope/x-y_z.v1~/a+b,c=d.ts")
        self.assertEqual(net.requests[0], "https://raw.githubusercontent.com/a/b/main/packages/@scope/x-y_z.v1~/a+b,c=d.ts")

    def test_a_timeout_is_retried_once(self):
        net = self.net(socket.timeout(), Ok(b"print('hi')"))
        self.assertEqual(_github.raw_get("a/b", "main", "x.py"), "print('hi')")
        self.assertEqual(len(net.requests), 2)
        self.assertEqual(self.slept, [1.5])
        self.net(socket.timeout(), socket.timeout())
        self.assertIsNone(_github.raw_get("a/b", "main", "x.py"))

    def test_429_waits_for_retry_after(self):
        self.net(error(429, b"", Retry_After=3), Ok(b"body"))
        self.assertEqual(_github.raw_get("a/b", "main", "x.py"), "body")
        self.assertEqual(self.slept, [3])

    def test_a_429_that_persists_is_a_rate_limit_not_a_missing_file(self):
        self.net(error(429, b"", Retry_After=3), error(429, b"", Retry_After=3))
        with self.assertRaises(_github.RateLimited) as caught:
            _github.raw_get("a/b", "main", "x.py")
        self.assertEqual(caught.exception.resource, "raw")
        self.assertEqual(_github.USAGE.requests["raw"], 2)


class ReportTest(Base):
    def test_usage_lines_say_what_was_spent_and_what_is_left(self):
        self.net(Ok({}, **budget(4321, reset=NOW + 60)), error(403, {"message": "blocked"}), error(404))
        _github.api_get("/a")
        _github.api_get("/b")
        _github.api_get("/c")
        text = "\n".join(_github.usage_lines())
        self.assertIn("core: 3 request(s)", text)
        self.assertIn("4321 of 5000 left", text)
        self.assertIn("1 blocked", text)
        self.assertRegex(text, r"resets \d\d:\d\d UTC")

    def test_nothing_spent_says_so(self):
        self.assertEqual(_github.usage_lines(), ["GitHub: no requests made"])

    def test_step_summary_appends_only_inside_actions(self):
        _github.step_summary("## Hello")
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "summary.md"
            with mock.patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": str(path)}):
                _github.step_summary("## Hello")
                _github.step_summary("again")
            self.assertEqual(path.read_text(), "## Hello\nagain\n")


if __name__ == "__main__":
    unittest.main()
