"""Shared GitHub plumbing for the scripts that read upstream repositories.

Extracted because verify_claims.py and refresh_metadata.py both need the same
four things — a token, an API call, a raw file, and the owner/name out of a row
— and two copies of that would drift. Dependency-free like the rest of the repo:
urllib only, so CI stays `setup-python` with no install step.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

API = "https://api.github.com"
RAW = "https://raw.githubusercontent.com"
TIMEOUT = 25

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

_branches: dict[str, str] = {}


def token() -> str | None:
    return os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")


def api_get(path: str) -> dict | list | None:
    """GET an API path. Returns None on anything but success, except a rate
    limit, which stops the run — continuing would silently produce a report
    full of false negatives."""
    req = urllib.request.Request(
        f"{API}{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "awesome-jev",
            **({"Authorization": f"Bearer {token()}"} if token() else {}),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as exc:
        if exc.code == 403:
            print(
                "error: GitHub rate limit. Set GITHUB_TOKEN; unauthenticated is 60/hour.",
                file=sys.stderr,
            )
            raise SystemExit(2) from exc
        return None
    except Exception:  # noqa: BLE001 - a sweep must not die on one row
        return None


def graphql(query: str) -> dict | None:
    """POST a read-only GraphQL query. Some repository facts — whether a custom
    social preview is uploaded, for one — are not exposed over REST."""
    if not token():
        return None
    req = urllib.request.Request(
        f"{API}/graphql",
        data=json.dumps({"query": query}).encode(),
        headers={"Authorization": f"Bearer {token()}", "User-Agent": "awesome-jev"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            return json.loads(response.read()).get("data")
    except Exception:  # noqa: BLE001 - informational callers degrade to "unknown"
        return None


def raw_get(repo: str, branch: str, path: str, *, retries: int = 1) -> str | None:
    """Fetch a file, retrying once before giving up.

    Without the retry a transient hiccup from the raw host is indistinguishable
    from a deleted file, and verify_claims.py reports `path-gone`. Two of the
    first three failures on an 805-row sweep were exactly that — the path was
    still there on the next request — which would have opened a weekly issue
    for nothing and taught everyone to ignore it.
    """
    req = urllib.request.Request(
        f"{RAW}/{repo}/{branch}/{path}", headers={"User-Agent": "awesome-jev"}
    )
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
                return response.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as exc:
            # A real 404 will not become a 200 on a retry.
            if exc.code == 404:
                return None
        except Exception:  # noqa: BLE001
            pass
        if attempt < retries:
            time.sleep(1.5)
    return None


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
