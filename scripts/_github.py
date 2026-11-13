"""Shared GitHub plumbing for the scripts that read upstream repositories.

Extracted because verify_claims.py and refresh_metadata.py both need the same
four things — a token, an API call, a raw file, and the owner/name out of a row
— and two copies of that would drift. Dependency-free like the rest of the repo:
urllib only, so CI stays `setup-python` with no install step.

Rate limits and blocked repositories are told apart (since 2026-09-27). GitHub
answers an exhausted budget with 403 or 429 and says so — `x-ratelimit-remaining:
0`, a `retry-after` header, or "rate limit" in the message — and answers a
repository it will not serve (a DMCA or terms-of-service block) with 403 or 451
and none of that. The first is about this run; the second is about one row.
Both used to be the same SystemExit, so one blocked repository ended a weekly
refresh before it had written anything, while a 429 passed for a missing row.

  * blocked      -> api_get returns {"blocked": True, "status", "message"}
  * rate limited -> wait what GitHub asks (at most RATE_WAIT_CAP seconds), retry
                    once, then raise RateLimited and send nothing more on that
                    budget for the rest of the run
  * nearly spent -> below the reserve, RateLimited without sending, until the
                    budget resets

RateLimited is a SystemExit(2), so a caller that does not handle it stops the
way every caller always did. The weekly jobs catch it per row, count the row as
skipped and keep what they already read. Every response's x-ratelimit-* headers
are recorded; usage_lines() says what a run spent and what is left.
"""

from __future__ import annotations

import functools
import http.client
import json
import os
import pathlib
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from dataclasses import dataclass

API = "https://api.github.com"
RAW = "https://raw.githubusercontent.com"
# Characters a URL path may carry as they are (RFC 3986 pchar and "/"):
# raw_get percent-encodes everything else in a file's path.
RAW_PATH_SAFE = "/!$&'()*+,;=:@"
TIMEOUT = 25

# The longest a rate-limited request waits before its one retry. A weekly job
# that sleeps out an hour-long reset would only fail later; one that stops
# keeps what it has.
RATE_WAIT_CAP = 90
# A secondary limit may name no time at all; GitHub's guidance is then to wait
# at least a minute.
SECONDARY_WAIT = 60
# Stop spending a budget this close to empty (a tenth of it, for a small one):
# the job's own later steps — filing an issue, dispatching the site rebuild —
# run on the same token.
RESERVE = 50

# This repository's own owner/name. Lives here because three scripts need it for
# three different reasons — building links, excluding self-referencing rows from
# the star refresh, and reading the published description — and three string
# literals would be three chances to drift after a rename.
SELF = "kydlikebtc/awesome-jev"

# File extensions per language, keyed by the `languages` enum in
# schema/entry.schema.json; lint.py checks the two keep the same keys. Both
# discover_candidates.py and verify_claims.py scan by these. They used to keep
# separate lists with no C or C++ at all, so a SQLite, DuckDB or MySQL extension
# calling Jev from C could never be discovered, only guessed at from its tests.
LANG_EXT: dict[str, tuple[str, ...]] = {
    "python": (".py",),
    "typescript": (".ts", ".tsx", ".mts", ".cts"),
    "javascript": (".js", ".mjs", ".cjs", ".jsx", ".gs"),  # .gs: Google Apps Script
    "go": (".go",),
    "rust": (".rs",),
    "shell": (".sh", ".bash"),
    "java": (".java",),
    "ruby": (".rb",),
    "php": (".php",),
    "csharp": (".cs",),
    "elixir": (".ex", ".exs"),
    "lua": (".lua",),
    "swift": (".swift",),
    "kotlin": (".kt", ".kts"),
    "haskell": (".hs",),
    "c": (".c", ".h"),
    "cpp": (".cc", ".cpp", ".cxx", ".hpp", ".hh"),
}
# SQL is not a catalogue language, but a query calling Jev is still a call site.
CODE_EXT: tuple[str, ...] = tuple(e for exts in LANG_EXT.values() for e in exts) + (".sql",)

# ---- What says a file calls Jev -------------------------------------------
#
# An import, the endpoint, a client class or a model name is a strong signal
# that a file calls Jev; a bare primitive name is not, because "choice" and
# "score" are ordinary words. verify_claims.py (proposing evidence) and
# discover_candidates.py (judging a candidate) read files by these signals.
# Until 2026-09-27 each kept its own copy of the list with the model version
# typed in, so a release would have left both looking for the old one. The
# model names now come from compat.json (version_signals), and a pinned version
# compat.json does not list yet still counts (VERSION), so a mistake in
# compat.json cannot hide a file that pins a real version.
COMPAT = pathlib.Path(__file__).resolve().parent.parent / "compat.json"

# In the order a proposal quotes them: verify_claims.py takes the first two it
# finds, discover_candidates.py the first three. compat.json's model names go
# between the two halves, where the typed-in ones stood.
STRONG_BEFORE_MODELS: tuple[str, ...] = (
    "api.typesafe.ai",
    "typesafe_sdk",
    "@typesafe-ai/sdk",
    # The Vercel AI SDK provider: evaluate() calls, where noul is spelled boolean.
    "@ai-sdk/typesafe-ai",
    # The gateways' model ids that name no version.
    "typesafe-ai/jev",
    "typesafe/jev",
)
STRONG_AFTER_MODELS: tuple[str, ...] = (
    "/v1/systemone",
    "systemOne",
    "system_one",
    "langchain_typesafe",
    "TypeSafeClient",
    "AsyncTypeSafeClient",
)

# A Jev model name as a file or a compat.json cell writes it: an alias
# (`jev-latest`) or a version (`jev-1.2`, `jev-1.2.0`). Not after a word
# character, a dot or a hyphen, so `my-jev-1.2` is another project's version;
# and a version needs its dot, because `jev-2048` is a catalogued project.
MODEL_NAME = re.compile(r"(?<![\w.-])jev-(?:\d+(?:\.\d+)+|[a-z]+)")
VERSION = re.compile(r"(?<![\w.-])jev-\d+(?:\.\d+)+")


def version_parts(token: str) -> tuple[int, ...]:
    """(1, 2, 0) for `jev-1.2.0`: the order versions sort in."""
    return tuple(int(part) for part in token.split("-", 1)[1].split("."))


def version_stem(token: str, parts: int = 2) -> str:
    """`jev-1.2` for `jev-1.2.0`: a version cut to its first `parts` numbers."""
    return "jev-" + ".".join(str(n) for n in version_parts(token)[:parts])


def version_signals(compat: dict | None = None) -> tuple[str, ...]:
    """The Jev model names compat.json records, as a file using them contains
    them: each alias whole (`jev-latest`), each version cut to major.minor
    (`jev-1.2`, which `jev-1.2.0` and `typesafe/jev-1.2` both contain).
    In compat.json's order, first mention first."""
    data = json.loads(COMPAT.read_text()) if compat is None else compat
    names: list[str] = []
    for platform in data.get("platforms", []):
        for name in MODEL_NAME.findall(platform.get("model") or ""):
            name = version_stem(name) if VERSION.fullmatch(name) else name
            if name not in names:
                names.append(name)
    return tuple(names)


@functools.lru_cache(maxsize=1)
def _listed_models() -> tuple[str, ...]:
    return version_signals()


def strong(models: tuple[str, ...] | None = None) -> tuple[str, ...]:
    """Every literal strong signal, compat.json's model names in their place."""
    models = _listed_models() if models is None else models
    return (*STRONG_BEFORE_MODELS, *models, *STRONG_AFTER_MODELS)


def strong_signals(body: str, models: tuple[str, ...] | None = None) -> list[str]:
    """The strong signals a file contains, in strong()'s order. A pinned
    version compat.json does not list (a release it has not caught up with)
    counts too, cut to major.minor, right after the model names it does list."""
    models = _listed_models() if models is None else models
    pinned: list[str] = []
    for token in VERSION.findall(body):
        stem = version_stem(token)
        if stem not in models and stem not in pinned:
            pinned.append(stem)
    return (
        [s for s in STRONG_BEFORE_MODELS if s in body]
        + [s for s in models if s in body]
        + pinned
        + [s for s in STRONG_AFTER_MODELS if s in body]
    )

_branches: dict[str, str] = {}

# 451 is GitHub's answer for a repository taken down on a legal notice; 403
# without any rate-limit signal is its answer for a terms-of-service block.
BLOCKED = (403, 451)


class RateLimited(SystemExit):
    """GitHub will not answer on this budget for a while — the run's problem,
    not a row's. Exit code 2, so an unhandled one ends the run as before."""

    def __init__(self, resource: str, detail: str):
        super().__init__(2)
        self.resource = resource
        self.detail = detail

    def __str__(self) -> str:
        return f"GitHub {self.resource} rate limit: {self.detail}"


@dataclass
class Window:
    limit: int
    remaining: int
    reset: float  # epoch seconds, as x-ratelimit-reset gives it


class Usage:
    """What this process spent, per budget: "core" and "search" (REST),
    "graphql", and "raw" (raw.githubusercontent.com, which sends no budget
    headers). Worker threads share it, hence the lock."""

    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.requests: Counter = Counter()
        self.unsent: Counter = Counter()
        self.windows: dict[str, Window] = {}
        self.closed: dict[str, tuple[float, str]] = {}
        self.limited = 0
        self.blocked = 0
        self.waited = 0.0


USAGE = Usage()


def reset_usage() -> None:
    """Forget what was spent. A script is one run; tests start each case clean."""
    global USAGE
    USAGE = Usage()
    _branches.clear()


def _sleep(seconds: float) -> None:
    time.sleep(seconds)


def _now() -> float:
    return time.time()


def _clock(epoch: float) -> str:
    return time.strftime("%H:%M UTC", time.gmtime(epoch))


def _int(value: object) -> int | None:
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return None


def token() -> str | None:
    return os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")


def _reserve(limit: int) -> int:
    return min(RESERVE, limit // 10)


def _note(resource: str, head) -> None:
    """Record a response's budget. Answers arrive out of order — worker threads,
    and GitHub's own servers, which do not always agree on the window — so
    until the recorded window has reset, the lowest remaining count wins."""
    if not head:
        return
    limit, remaining, reset = (
        _int(head.get(f"X-RateLimit-{name}")) for name in ("Limit", "Remaining", "Reset")
    )
    if limit is None or remaining is None or reset is None:
        return
    with USAGE.lock:
        old = USAGE.windows.get(resource)
        if old is None or _now() >= old.reset or remaining < old.remaining:
            USAGE.windows[resource] = Window(limit, remaining, float(reset))


def _close(resource: str, until: float, detail: str) -> None:
    """Send nothing more on this budget until `until`; say so once."""
    with USAGE.lock:
        if resource in USAGE.closed:
            return
        USAGE.closed[resource] = (until, detail)
    when = "this run" if until == float("inf") else f"until {_clock(until)}"
    print(f"GitHub {resource}: {detail}; sending nothing more on it {when}", file=sys.stderr)


def _check_open(resource: str) -> None:
    """Raise RateLimited, sending nothing, while this budget is closed — for the
    rest of the run after a limit that outlasted its retry, or until the reset
    once it is under the reserve."""
    now = _now()
    with USAGE.lock:
        closed = USAGE.closed.get(resource)
        if closed is not None and now >= closed[0]:
            del USAGE.closed[resource]
            closed = None
        window = USAGE.windows.get(resource)
    if (
        closed is None
        and window is not None
        and now < window.reset
        and window.remaining < _reserve(window.limit)
    ):
        _close(
            resource,
            window.reset,
            f"{window.remaining} of {window.limit} left, under the reserve of {_reserve(window.limit)}",
        )
    with USAGE.lock:
        closed = USAGE.closed.get(resource)
        if closed is not None:
            USAGE.unsent[resource] += 1
    if closed is not None:
        raise RateLimited(resource, closed[1])


def _limit_wait(code: int, head, body: bytes) -> float | None:
    """Seconds GitHub asks for when this answer is a rate limit; None when it is
    anything else — a blocked repository, a missing one, a server error."""
    if code not in (403, 429):
        return None
    head = head or {}
    retry_after = _int(head.get("Retry-After"))
    remaining = _int(head.get("X-RateLimit-Remaining"))
    reset = _int(head.get("X-RateLimit-Reset"))
    said = "rate limit" in body.decode("utf-8", "replace").lower()
    if code == 403 and retry_after is None and remaining != 0 and not said:
        return None
    if retry_after is not None:
        return float(max(retry_after, 0))
    if remaining == 0 and reset is not None:
        return max(reset - _now(), 0) + 1
    return float(SECONDARY_WAIT)


def _request(req: urllib.request.Request, resource: str) -> tuple[int, bytes, object]:
    """(status, body, headers) for one request. Status 0 means no answer.

    A rate limit is waited out once, when GitHub names a wait no longer than
    RATE_WAIT_CAP; a longer one, or one still there after the retry, closes the
    budget and raises RateLimited."""
    for attempt in (1, 2):
        _check_open(resource)
        with USAGE.lock:
            USAGE.requests[resource] += 1
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
                body = response.read()
                _note(resource, response.headers)
                return response.status, body, response.headers
        except urllib.error.HTTPError as exc:
            try:
                body = exc.read() or b""
            except Exception:  # noqa: BLE001 - the status is what matters
                body = b""
            _note(resource, exc.headers)
            wait = _limit_wait(exc.code, exc.headers, body)
            if wait is None:
                if exc.code in BLOCKED and resource != "raw":
                    with USAGE.lock:
                        USAGE.blocked += 1
                return exc.code, body, exc.headers
            with USAGE.lock:
                USAGE.limited += 1
            if attempt == 1 and wait <= RATE_WAIT_CAP:
                print(
                    f"GitHub {resource}: HTTP {exc.code}, waiting {wait:.0f} s before one retry",
                    file=sys.stderr,
                )
                with USAGE.lock:
                    USAGE.waited += wait
                _sleep(wait)
                continue
            if attempt == 1:
                until = _now() + wait
                detail = f"HTTP {exc.code}, asked to wait {wait:.0f} s (this run waits at most {RATE_WAIT_CAP} s)"
            else:
                until = float("inf")
                detail = f"HTTP {exc.code} again after the wait"
            _close(resource, until, detail)
            raise RateLimited(resource, detail) from exc
        except (urllib.error.URLError, http.client.HTTPException, OSError, ValueError):
            return 0, b"", None
    raise AssertionError("unreachable: the second attempt returns or raises")


def _headers(accept: str | None = "application/vnd.github+json") -> dict[str, str]:
    return {
        **({"Accept": accept} if accept else {}),
        "User-Agent": "awesome-jev",
        **({"Authorization": f"Bearer {token()}"} if token() else {}),
    }


def api_response(path: str) -> tuple[int, dict | list | None, object]:
    """(HTTP status, parsed JSON body, response headers) for a GET on an API
    path; status 0 means no answer (timeout, reset connection) and headers are
    then None. Raises RateLimited. For a caller that needs a header, such as
    the `Link` header that says how many pages a list has."""
    req = urllib.request.Request(f"{API}{path}", headers=_headers())
    status, body, head = _request(req, "search" if path.startswith("/search/") else "core")
    try:
        data = json.loads(body) if body else None
    except ValueError:
        data = None
    return status, data, head


def api_fetch(path: str) -> tuple[int, dict | list | None]:
    """(HTTP status, parsed JSON body) for a GET on an API path; status 0 means
    no answer (timeout, reset connection). Raises RateLimited."""
    status, data, _ = api_response(path)
    return status, data


LAST_PAGE = re.compile(r'<([^>]*)>\s*;\s*rel="last"')


def last_page(link: str | None) -> int | None:
    """The page number of the `rel="last"` link in a `Link` header, or None
    when there is none (the whole list fitted on one page) or it names no
    page. With `per_page=1` that is the number of items in the list: how
    GitHub's REST API says how many commits a branch has without listing them."""
    match = LAST_PAGE.search(link or "")
    if not match:
        return None
    query = urllib.parse.urlsplit(match.group(1)).query
    pages = urllib.parse.parse_qs(query).get("page") or []
    number = _int(pages[-1]) if pages else None
    return number if number is not None and number > 0 else None


def api_get(path: str) -> dict | list | None:
    """The body of a successful GET; {"blocked": True, "status", "message"} for
    a repository GitHub refuses to serve; None for anything else (missing, no
    answer). A rate limit raises RateLimited rather than returning None —
    continuing would silently turn every remaining row into a false negative."""
    status, data = api_fetch(path)
    if 200 <= status < 300:
        return data
    if status in BLOCKED:
        message = data.get("message", "") if isinstance(data, dict) else ""
        return {"blocked": True, "status": status, "message": message}
    return None


def graphql_request(query: str, variables: dict | None = None) -> dict | None:
    """POST a read-only GraphQL query and return the whole answer, `errors`
    beside `data`: a batch of aliased lookups fails one alias at a time. None
    without a token, or without a usable answer after one retry. Raises
    RateLimited, including for a 200 whose only error is RATE_LIMITED."""
    if not token():
        return None
    payload = json.dumps({"query": query, **({"variables": variables} if variables else {})}).encode()
    for attempt in (1, 2):
        req = urllib.request.Request(
            f"{API}/graphql", data=payload, headers=_headers(None), method="POST"
        )
        status, body, _ = _request(req, "graphql")
        if 200 <= status < 300:
            try:
                answer = json.loads(body)
            except ValueError:
                answer = None
            if isinstance(answer, dict):
                errors = answer.get("errors") or []
                if not answer.get("data") and any(e.get("type") == "RATE_LIMITED" for e in errors):
                    detail = "a GraphQL answer of RATE_LIMITED"
                    _close("graphql", float("inf"), detail)
                    raise RateLimited("graphql", detail)
                return answer
        elif 0 < status < 500:
            return None  # refused for a reason a retry will not change
        if attempt == 1:
            _sleep(1.5)
    return None


def graphql_mutation(query: str, variables: dict | None = None) -> dict | None:
    """POST a GraphQL mutation once and return the whole answer, or None
    without a token or a usable answer. Never retried: a mutation that timed
    out may still have happened, and a second try could do it twice (two vote
    posts for one launch). A caller that must be sure looks first, as
    launch_week.py does, and runs again later. Raises RateLimited."""
    if not token():
        return None
    payload = json.dumps({"query": query, **({"variables": variables} if variables else {})}).encode()
    req = urllib.request.Request(f"{API}/graphql", data=payload, headers=_headers(None), method="POST")
    status, body, _ = _request(req, "graphql")
    if not 200 <= status < 300:
        return None
    try:
        answer = json.loads(body)
    except ValueError:
        return None
    return answer if isinstance(answer, dict) else None


def graphql(query: str) -> dict | None:
    """The `data` of a read-only GraphQL query, or None. For informational
    callers — whether a custom social preview is uploaded is not exposed over
    REST — which degrade to "unknown", a rate limit included."""
    try:
        answer = graphql_request(query)
    except RateLimited:
        return None
    return (answer or {}).get("data")


def raw_get(repo: str, branch: str, path: str, *, retries: int = 1) -> str | None:
    """Fetch a file, retrying once before giving up.

    Without the retry a transient hiccup from the raw host is indistinguishable
    from a deleted file, and verify_claims.py reports `path-gone`. Two of the
    first three failures on an 805-row sweep were exactly that — the path was
    still there on the next request — which would have opened a weekly issue
    for nothing and taught everyone to ignore it.

    A 429 is not a miss either: it is waited out once like an API rate limit,
    and one that persists raises RateLimited instead of calling the file gone.
    `branch` may be "HEAD", which the raw host resolves to the default branch.

    The path is percent-encoded, so a file under a folder named in Korean or
    holding a space can be read: unencoded, such a URL cannot be sent at all
    (jkf87/jev-handson's call sites, 2026-11-12). A path of letters, digits
    and the punctuation a path may carry is sent unchanged.
    """
    req = urllib.request.Request(
        f"{RAW}/{repo}/{branch}/{urllib.parse.quote(path, safe=RAW_PATH_SAFE)}",
        headers={"User-Agent": "awesome-jev"},
    )
    for attempt in range(retries + 1):
        status, body, _ = _request(req, "raw")
        if 200 <= status < 300:
            return body.decode("utf-8", "replace")
        # A real 404 will not become a 200 on a retry.
        if status == 404:
            return None
        if attempt < retries:
            _sleep(1.5)
    return None


def usage_lines() -> list[str]:
    """What this run spent and what is left, one line per budget, for the log
    and the job summary. Clock times are absolute (UTC)."""
    with USAGE.lock:
        names = sorted(set(USAGE.requests) | set(USAGE.unsent))
        if not names:
            return ["GitHub: no requests made"]
        lines = []
        for name in names:
            line = f"GitHub {name}: {USAGE.requests[name]} request(s)"
            window = USAGE.windows.get(name)
            if window is not None:
                line += f"; {window.remaining} of {window.limit} left, resets {_clock(window.reset)}"
            if USAGE.unsent[name]:
                line += f"; {USAGE.unsent[name]} not sent (budget closed)"
            lines.append(line)
        lines.append(
            f"GitHub answers: {USAGE.limited} rate-limited, {USAGE.blocked} blocked; "
            f"waited {USAGE.waited:.0f} s"
        )
    return lines


def log_usage() -> None:
    for line in usage_lines():
        print(line, file=sys.stderr)


def step_summary(markdown: str) -> None:
    """Append to the job summary when running in GitHub Actions; else nothing."""
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as handle:
            handle.write(markdown + "\n")


def repo_of(entry: dict) -> str | None:
    """owner/name from a catalog row's repo or url, when it is a GitHub repo."""
    for candidate in (entry.get("repo"), entry.get("url")):
        if not candidate:
            continue
        match = re.match(r"https://github\.com/([^/]+)/([^/#?]+)", candidate)
        if match:
            return f"{match.group(1)}/{match.group(2)}"
    return None


def default_branch(repo: str) -> str | None:
    """Cached, because several rows point at the same repository."""
    if repo not in _branches:
        data = api_get(f"/repos/{repo}")
        _branches[repo] = (data or {}).get("default_branch") or ""
    return _branches[repo] or None
