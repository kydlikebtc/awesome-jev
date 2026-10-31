#!/usr/bin/env python3
"""Re-check that the primitive claims in catalog.json are still true upstream.

A row carrying `question_types` asserts which Jev primitives a project's code
actually calls. That assertion was true when a person read the call site, and
nothing stopped it going stale afterwards — an upstream refactor could remove
the integration entirely and this catalog would keep claiming it.

This script closes that gap. For every row with `evidence`, it fetches that file
from the repository's default branch and asserts every string in
`evidence.matched` still appears.

The file is read first at `HEAD` on raw.githubusercontent.com, which resolves
to the default branch without the API call per repository that asking for the
branch name costs. That resolution is observed behaviour, not documented, so
only a pass is taken from it: a file missing or changed at HEAD is read again at
the default branch the API names, and that read is what gets reported. A GitHub
rate limit leaves a claim unchecked (`skipped`), never failed.

Deliberately not pinned to a commit. Pinning would verify a historical snapshot
forever and never notice a removal, which defeats the purpose. The cost is that
an upstream rename reports `path-gone`; that is a false positive a person
resolves, not a reason to check the wrong thing.

Exit code is 0 when every claim holds and 1 when any fails, so the scheduled
workflow can open an issue.

A `path-gone` file has usually been moved or renamed rather than deleted with
its integration. In the weekly report each one's repository tree is searched
(one API call, then a bounded number of reads on the raw host) for a file that
still holds every string in `evidence.matched`, and the line names it: a
proposed `evidence.path` (or wire.source path) for the person resolving the
failure, who opens it first. The claim still fails, and nothing is written.

A claim that lost only a pinned model version (`jev-1.2`, say) from a file that
now names another is reported as `version-moved` rather than `claim-gone`, and
the report counts those rows per version ("N rows now pin X"): when the vendor
ships a model, projects move their pin one by one, and each move is not a
removed integration. It still fails, since its strings are gone.
`--propose-version-rewrite` prints the rewritten `evidence.matched` for each
such row and writes nothing; a person applies it and leaves `read_on` alone.

A file whose claim holds is also searched for the primitives' request and
answer shapes — `"type": "choice"`, `Noul(`, `.noul` and the like
(PRIMITIVE_SHAPES), and a call to the TypeScript SDK's `choice()`, `score()`
or `noul()` imported from `@typesafe-ai/sdk` (ts_sdk_helpers) — never the bare
words. What it finds is a machine text
signal about that one file: it does not say the code calls the primitive, and
it is not `question_types`, which records what a person read the code calling.
`--write-signals` records it in each row's `primitives_seen`, the only field
this script ever writes; the weekly metadata run calls it and commits the
result with the other mechanical facts. Nothing reads `primitives_seen` in place
of `question_types`.

The same read records, in `experimental_seen` (since 2026-10-31), which of
Jev's experimental features the file's text shows (EXPERIMENTAL_SHAPES): a
Box question (Jev 1.14), and the images and long-context opt-in headers. Box
is not one of the three primitives the catalogue counts, filters and picks
between, so it is kept apart from primitives_seen rather than added to it;
docs/review-queue.md#experimental lists the rows that show one, for a person
to read when Box leaves the experimental tier.

An `alternative` row's `wire` record cites the files its interface was read in
(wire.source: path and matched strings, as evidence does; scripts/wire.py).
Each of those files is re-read the same way and reported on its own line,
marked `wire.source`. A file there that lost only a model version is reported
`claim-gone`, not `version-moved`: the fields were read in it, so a person
re-reads it rather than rewriting strings.

Usage:
  python3 scripts/verify_claims.py                  # check every row with evidence, and every wire.source file
  python3 scripts/verify_claims.py --only slug      # check one row
  python3 scripts/verify_claims.py --discover       # propose evidence for rows lacking it
  python3 scripts/verify_claims.py --json           # machine-readable report
  python3 scripts/verify_claims.py --write-signals  # record primitives_seen in catalog.json
  python3 scripts/verify_claims.py --propose-version-rewrite [--json]
      # dry run: evidence.matched rewritten for each version-moved row
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

from _github import (
    CODE_EXT,
    VERSION,
    RateLimited,
    api_get,
    default_branch,
    log_usage,
    raw_get,
    repo_of,
    step_summary,
    strong_signals,
    usage_lines,
    version_parts,
    version_stem,
)

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from wire import claims as wire_claims  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"

# Signals that a file is a genuine Jev call site rather than a mention — an
# import, the endpoint, a model name — are _github.strong_signals(), shared with
# discover_candidates.py; the model names come from compat.json. A bare
# primitive name is only meaningful alongside one, because "choice" and
# "score" are ordinary English words.
WEAK = ["noul", "Noul", "choice", "Choice", "score", "Score"]

# The Jev primitives, in the order schema/entry.schema.json lists them for
# question_types and primitives_seen.
PRIMITIVES = ("choice", "score", "noul")

# A primitive's request or answer shape written out, as opposed to its name.
# WEAK's bare words say nothing about a primitive ("choice" and "score" are
# English, and a README names all three); these are the forms Jev's request and
# answer take in code. Each pattern's one group is the primitive. Left out on
# purpose: `.choice` and `.score` (random.choice, model.score), `type="noul"`
# as a keyword argument (the test doubles that build fake answers), and
# Vercel's `boolean`, which is how its SDK spells noul and how everything else
# spells a boolean.
_QUOTE = r"""\\?["']"""  # also inside an escaped JSON string: {\"type\":\"noul\"}
PRIMITIVE_SHAPES = (
    # The request's `type` field: JSON, a Python dict, a JS object, a TS type.
    re.compile(rf"""(?<![\w$.])(?:{_QUOTE}type{_QUOTE}|type)\s*:\s*{_QUOTE}(choice|score|noul){_QUOTE}"""),
    # The same field in Ruby, PHP or Elixir.
    re.compile(rf"""(?:{_QUOTE}type{_QUOTE}|:type)\s*=>\s*{_QUOTE}(choice|score|noul){_QUOTE}"""),
    # Question constructors with a capital, as the Python SDK spells them (the
    # TypeScript SDK's lower-case ones are ts_sdk_helpers). click.Choice( is a
    # CLI option, not Jev.
    re.compile(r"""(?<!click\.)\b(Choice|Score|Noul)\("""),
    # Reading a noul answer.
    re.compile(r"""\.(noul)\b"""),
)

WORKERS = 6

# A test file's path. discover() ranks one below an implementation, and
# relocation_candidates() reads one last.
TEST_PATH = re.compile(r"(^|/)(tests?|spec|__tests__)/|\.(test|spec)\.[a-z]+$|_test\.[a-z]+$|test_[^/]*$", re.I)


def weak_words(body: str) -> list[str]:
    """The WEAK words the file contains as whole words, in WEAK's order."""
    return [w for w in WEAK if re.search(rf"\b{re.escape(w)}\b", body)]


# The TypeScript SDK builds a question with choice(), score() or noul(), which
# @typesafe-ai/sdk exports (its README: `category: choice("What is this ticket
# about?", {...})`). Lower-case, those names are also random.choice, a local
# score() and plain words, so one counts only when the file imports it from the
# SDK by name — `import { choice }`, `import { noul as yes }`, never
# `import type` — and calls it, not as a method.
TS_SDK_IMPORT = re.compile(r"""\bimport\s+(?!type\b)(?:[\w$]+\s*,\s*)?\{([^}]*)\}\s*from\s*["']@typesafe-ai/sdk["']""")


def ts_sdk_helpers(body: str) -> set[str]:
    """The primitives whose @typesafe-ai/sdk helper the file imports by name and calls."""
    found = set()
    for match in TS_SDK_IMPORT.finditer(body):
        for part in match.group(1).split(","):
            words = part.split()
            if len(words) not in (1, 3) or words[0] not in PRIMITIVES:
                continue  # empty, `type choice`, or another export
            local = words[-1]  # `choice`, or `pick` in `choice as pick`
            if re.search(rf"(?<![\w$.]){re.escape(local)}\s*\(", body):
                found.add(words[0])
    return found


# Jev's experimental features (K3, 2026-10-31), as the official SDKs spell
# them: typesafe-ai/typesafe-sdk-js src/types.ts (`BoxQuestion { type: "box" }`,
# `BoxResponse.box.{top,bottom,left,right}`) and the Python SDK's `Box`. Each
# pattern's match names its feature by the dictionary key. Bare `Box(` is
# Jetpack Compose and gym.spaces too, so the Python constructor counts only
# when the file imports Box from typesafe_sdk; `.box` alone is a property of
# half the UI code on GitHub, so only a box answer's edges count.
EXPERIMENTAL = ("box", "images", "long-context")
EXPERIMENTAL_SHAPES = {
    "box": (
        re.compile(rf"""(?<![\w$.])(?:{_QUOTE}type{_QUOTE}|type)\s*:\s*{_QUOTE}box{_QUOTE}"""),
        re.compile(rf"""(?:{_QUOTE}type{_QUOTE}|:type)\s*=>\s*{_QUOTE}box{_QUOTE}"""),
        re.compile(r"""\.box\.(?:top|bottom|left|right)\b"""),
    ),
    "images": (re.compile(r"TypeSafe-Danger-Zone-Images", re.IGNORECASE),),
    "long-context": (re.compile(r"TypeSafe-Danger-Zone-Long-Context", re.IGNORECASE),),
}
PY_SDK_IMPORT = re.compile(r"""\bfrom\s+typesafe_sdk(?:\.[\w.]+)?\s+import\s+(\([^)]*\)|[^\n;]+)""")


def sdk_box(body: str) -> bool:
    """The file builds a Box question with an SDK: box() imported from
    @typesafe-ai/sdk and called, or Box imported from typesafe_sdk and called."""
    for match in TS_SDK_IMPORT.finditer(body):
        for part in match.group(1).split(","):
            words = part.split()
            if len(words) in (1, 3) and words[0] == "box" and re.search(
                rf"(?<![\w$.]){re.escape(words[-1])}\s*\(", body
            ):
                return True
    for match in PY_SDK_IMPORT.finditer(body):
        for part in match.group(1).strip("()").split(","):
            words = part.split()
            if len(words) in (1, 3) and words[0] == "Box" and re.search(
                rf"(?<![\w.]){re.escape(words[-1])}\(", body
            ):
                return True
    return False


def experimental_signals(body: str) -> list[str]:
    """The experimental features whose shape (EXPERIMENTAL_SHAPES, sdk_box) the
    text contains, in EXPERIMENTAL order. A text signal about this one file."""
    found = {name for name, patterns in EXPERIMENTAL_SHAPES.items() if any(p.search(body) for p in patterns)}
    if sdk_box(body):
        found.add("box")
    return [name for name in EXPERIMENTAL if name in found]


def primitive_signals(body: str) -> list[str]:
    """The primitives whose shape (PRIMITIVE_SHAPES, ts_sdk_helpers) the text
    contains, in PRIMITIVES order. A text signal about this one file, not a reading."""
    found = {match.group(1).lower() for pattern in PRIMITIVE_SHAPES for match in pattern.finditer(body)}
    found |= ts_sdk_helpers(body)
    return [name for name in PRIMITIVES if name in found]


def check(entry: dict) -> dict:
    slug = entry["slug"]
    repo = repo_of(entry)
    if not repo:
        return {
            "slug": slug,
            "status": "no-repo",
            "detail": "row has no GitHub repository",
        }
    try:
        return read_claim(slug, repo, entry["evidence"])
    except RateLimited as exc:
        return {"slug": slug, "status": "skipped", "detail": f"not checked: {exc}"}


# A result about a file wire.source cites carries claim=WIRE.
WIRE = "wire"


def check_wire(item: tuple[dict, dict]) -> dict:
    """Re-read one file an alternative row's wire.source cites, as check()
    re-reads evidence. A lost model version counts as claim-gone here: the
    fields were read in that file, so it is a person's to re-read."""
    entry, source = item
    slug = entry["slug"]
    repo = repo_of(entry)
    if not repo:
        result = {"status": "no-repo", "detail": "row has no GitHub repository"}
    else:
        try:
            result = read_claim(slug, repo, source)
        except RateLimited as exc:
            result = {"status": "skipped", "detail": f"not checked: {exc}"}
    status = "claim-gone" if result["status"] == VERSION_MOVED else result["status"]
    out = {"slug": slug, "status": status, "claim": WIRE, "detail": f"wire.source {result['detail']}"}
    if status == "path-gone":
        out.update({key: result[key] for key in WHERE})
    return out


def read_claim(slug: str, repo: str, evidence: dict) -> dict:
    # A pass at HEAD is a pass; anything else is judged at the named branch.
    body = raw_get(repo, "HEAD", evidence["path"])
    if body is not None and all(needle in body for needle in evidence["matched"]):
        return {
            "slug": slug,
            "status": "ok",
            "detail": f"{repo}@HEAD:{evidence['path']}",
            "primitive_signals": primitive_signals(body),
            "experimental_signals": experimental_signals(body),
        }

    branch = default_branch(repo)
    if not branch:
        return {
            "slug": slug,
            "status": "repo-gone",
            "detail": f"{repo} did not resolve",
        }

    body = raw_get(repo, branch, evidence["path"])
    if body is None:
        return {
            "slug": slug,
            "status": "path-gone",
            "detail": f"{repo}@{branch}:{evidence['path']} not found — renamed, moved or deleted",
            # Where it looked, for propose_paths(): the file may only have moved.
            "repo": repo,
            "branch": branch,
            "path": evidence["path"],
            "matched": list(evidence["matched"]),
        }

    missing = [needle for needle in evidence["matched"] if needle not in body]
    pins = moved_to(missing, body)
    if pins:
        # Only a model version is gone and the file names another: the
        # integration is most likely still there, pinned to a newer model.
        # A classification for the person reading the report, not a verdict.
        return {
            "slug": slug,
            "status": VERSION_MOVED,
            "detail": (
                f"{repo}@{branch}:{evidence['path']} no longer contains {missing}; "
                f"it names {', '.join(pins)} instead"
            ),
            "pins": pins,
            "path": evidence["path"],
            "matched": list(evidence["matched"]),
            "proposed": rewrite(evidence["matched"], body, pins[-1]),
            "primitive_signals": primitive_signals(body),
            "experimental_signals": experimental_signals(body),
        }
    if missing:
        return {
            "slug": slug,
            "status": "claim-gone",
            "detail": f"{repo}@{branch}:{evidence['path']} no longer contains {missing}",
        }
    return {
        "slug": slug,
        "status": "ok",
        "detail": f"{repo}@{branch}:{evidence['path']}",
        "primitive_signals": primitive_signals(body),
        "experimental_signals": experimental_signals(body),
    }


# --- version-moved -------------------------------------------------------------
#
# About one cited row in six quotes a pinned model version in evidence.matched.
# When the vendor ships the next one, those projects move their pin one by
# one, and each move would read as claim-gone — mixed in with real removals,
# and each worth a person's re-read. A claim that lost only model
# versions, from a file that names another version, is `version-moved`
# instead: reported together ("N rows now pin X") with the rewritten strings
# proposed (--propose-version-rewrite), never written. A person applies them;
# `read_on` stays as it is, because a string rewrite is not a reading.
VERSION_MOVED = "version-moved"


def moved_to(missing: list[str], body: str) -> list[str]:
    """The model versions (major.minor) a file names in place of those its
    claim lost, oldest first; [] when the claim lost anything but a model
    version, or the file names no other version."""
    if not missing:
        return []
    lost = set()
    for needle in missing:
        token = VERSION.search(needle)
        if not token:
            return []
        lost.add(version_stem(token.group(0)))
    found = {version_stem(token) for token in VERSION.findall(body)} - lost
    return sorted(found, key=version_parts)


def rewrite(matched: list[str], body: str, target: str) -> list[str] | None:
    """evidence.matched with each version the file no longer names moved to
    `target`, written as precisely as before (`jev-1.2.0` becomes the file's
    `jev-1.3.x`, `jev-1.2` becomes `jev-1.3`). None when a rewritten string
    is still not in the file: then a person reads it."""
    out = []
    for needle in matched:
        if needle in body:
            out.append(needle)
            continue
        token = VERSION.search(needle)
        if not token:
            return None
        precision = len(version_parts(token.group(0)))
        written = sorted(
            (t for t in VERSION.findall(body) if version_stem(t) == target and len(version_parts(t)) >= precision),
            key=version_parts,
        )
        new = version_stem(written[-1], precision) if written else target
        candidate = needle[: token.start()] + new + needle[token.end() :]
        if candidate not in body:
            return None
        out.append(candidate)
    return out


def version_moves(results: list[dict]) -> dict[str, list[str]]:
    """Slugs by the newest version their file now names, for the report."""
    moves: dict[str, list[str]] = {}
    for result in results:
        if result["status"] == VERSION_MOVED:
            moves.setdefault(result["pins"][-1], []).append(result["slug"])
    return dict(sorted(moves.items(), key=lambda item: version_parts(item[0])))


def move_lines(moves: dict[str, list[str]]) -> list[str]:
    """One line per version, the form claims.yml's issue quotes."""
    return [
        f"version-moved: {len(slugs)} row(s) now pin {target} — their cited file names it in place of the "
        "version in evidence.matched; `python3 scripts/verify_claims.py --propose-version-rewrite` "
        "lists the strings to review (read_on stays as it is)"
        for target, slugs in moves.items()
    ]


# --- path-gone -----------------------------------------------------------------
#
# A cited file missing from the default branch has often been moved or renamed
# with the integration intact. 24 of the 66 failures in the claims run of
# 2026-10-20 were path-gone, and each was a person's search through someone
# else's tree. The weekly report now does the search: one API call for the
# repository's file tree, then at most RELOCATE_READS files read on the raw
# host, in relocation_candidates' order, until one holds every string in
# `matched`. A hit is a proposal, never written, and the claim still fails:
# the strings being elsewhere does not say that file is where the integration
# lives now, so a person opens it first.
WHERE = ("repo", "branch", "path", "matched")
RELOCATE_READS = 20
# A name that hints at the integration, the way discover() narrows a tree.
HINT = re.compile(r"jev|typesafe|system_?one", re.I)


def relocation_candidates(paths: list[str], old: str) -> list[str]:
    """The files worth reading in place of `old`, best first: the same file name
    anywhere in the tree, then paths that hint at the integration, then files
    with its extension. Within each group a test file comes last (the claim was
    read in an implementation), then the paths sharing the longest leading
    directories with `old`, then the shallowest. At most RELOCATE_READS of them."""
    gone = pathlib.PurePosixPath(old)

    def rank(path: str) -> tuple[bool, int, int, str]:
        parts = pathlib.PurePosixPath(path).parts
        shared = 0
        for mine, theirs in zip(gone.parent.parts, parts[:-1]):
            if mine != theirs:
                break
            shared += 1
        return (bool(TEST_PATH.search(path)), -shared, len(parts), path)

    groups: list[list[str]] = [[], [], []]
    for path in paths:
        if path == old:
            continue
        here = pathlib.PurePosixPath(path)
        if here.name == gone.name:
            groups[0].append(path)
        elif HINT.search(path):
            groups[1].append(path)
        elif gone.suffix and here.suffix == gone.suffix:
            groups[2].append(path)
    return [path for group in groups for path in sorted(group, key=rank)][:RELOCATE_READS]


def relocate(result: dict) -> str | None:
    """A file on the result's branch holding every string its claim matched, or
    None: none of the candidates does, the tree is unavailable, or the GitHub
    budget ran out (which leaves the failure as it was, not unchecked)."""
    repo, branch = result["repo"], result["branch"]
    try:
        tree = api_get(f"/repos/{repo}/git/trees/{urllib.parse.quote(branch, safe='')}?recursive=1")
        if not isinstance(tree, dict) or not isinstance(tree.get("tree"), list):
            return None
        paths = [
            node["path"]
            for node in tree["tree"]
            if node.get("type") == "blob" and isinstance(node.get("path"), str)
        ]
        for path in relocation_candidates(paths, result["path"]):
            body = raw_get(repo, branch, urllib.parse.quote(path, safe="/"))
            if body is not None and all(needle in body for needle in result["matched"]):
                return path
    except RateLimited:
        return None
    return None


def propose_paths(results: list[dict]) -> int:
    """Give each path-gone result whose matched strings all sit in another file
    of its repository that file's path, as `proposed_path` and at the end of
    its detail. Returns how many got one."""
    gone = [r for r in results if r["status"] == "path-gone" and all(key in r for key in WHERE)]
    if not gone:
        return 0
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        found = list(pool.map(relocate, gone))
    for result, path in zip(gone, found):
        if path:
            result["proposed_path"] = path
            result["detail"] += f"; every matched string is in {path} — open it, then update the path"
    return sum(1 for path in found if path)


def path_line(proposed: int, gone: int) -> str:
    """The report's one line about path-gone proposals, the form claims.yml's issue quotes."""
    return (
        f"path-gone: {proposed} of {gone} missing file(s) have a proposed new path — a file in the same "
        "repository holding every matched string, named on its line; open it before changing the row's "
        "path, and move read_on only if you read the call there"
    )


def propose_rewrites(todo: list[dict], as_json: bool) -> int:
    """--propose-version-rewrite: a dry run. Reads every cited file and prints,
    for each version-moved row, evidence.matched as it is and as the file now
    reads. Writes nothing; read_on is never part of it."""
    print(f"reading {len(todo)} cited file(s) for moved model versions\n", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(check, todo))
    moved = [r for r in results if r["status"] == VERSION_MOVED]
    unread = [r for r in results if r["status"] == "skipped"]
    if as_json:
        print(json.dumps(
            [{key: r[key] for key in ("slug", "path", "matched", "proposed", "pins")} for r in moved],
            indent=2, ensure_ascii=False,
        ))
    else:
        for r in moved:
            print(f"  {r['slug']}  {r['path']}")
            print(f"    matched:  {json.dumps(r['matched'], ensure_ascii=False)}")
            if r["proposed"] is None:
                print(f"    proposed: none — the file names {', '.join(r['pins'])}, but not in a form "
                      "the old strings can be rewritten to; read it")
            else:
                print(f"    proposed: {json.dumps(r['proposed'], ensure_ascii=False)}")
        for line in move_lines(version_moves(results)):
            print(line)
    rewritable = sum(1 for r in moved if r["proposed"] is not None)
    tail = f"; {len(unread)} not read (GitHub rate limit)" if unread else ""
    print(
        f"version rewrites: {len(moved)} of {len(results)} cited row(s) version-moved, "
        f"{rewritable} with a proposed evidence.matched{tail}. Nothing written; "
        "apply by hand and leave read_on as it is.",
        file=sys.stderr if as_json else sys.stdout,
    )
    log_usage()
    return 0


def needs_discovery(entry: dict) -> bool:
    """A row lint requires evidence or evidence_none of, that carries neither.

    That is a row claiming primitives, and since 2026-09-27 every row with code
    in a GitHub repository; --discover can only help where there is a
    repository to read.
    """
    return (
        bool(entry.get("question_types") or entry.get("has_code"))
        and "evidence" not in entry
        and "evidence_none" not in entry
        and repo_of(entry) is not None
    )


def discover(entry: dict) -> dict:
    """Propose evidence for a row that has none, by reading the repository.

    Proposals are a starting point for a person, never written automatically —
    the whole point of this catalog is that a human read the call site. For an
    alternative the proposal says `wire-shape`, the only evidence.kind lint
    accepts there: whatever file it cites, the project is not built on Jev.
    """
    slug = entry["slug"]
    repo = repo_of(entry)
    if not repo:
        return {"slug": slug, "status": "no-repo"}
    branch = default_branch(repo)
    if not branch:
        return {"slug": slug, "status": "repo-gone"}

    tree = api_get(f"/repos/{repo}/git/trees/{branch}?recursive=1")
    if not isinstance(tree, dict) or "tree" not in tree:
        return {"slug": slug, "status": "tree-unavailable"}

    # Prefer paths whose name already hints at the integration; it keeps the
    # candidate list short on repositories with thousands of files.
    paths = [
        node["path"]
        for node in tree["tree"]
        if node.get("type") == "blob" and node["path"].endswith(CODE_EXT)
    ]
    hinted = [p for p in paths if re.search(r"jev|typesafe", p, re.I)]
    candidates = (hinted or paths)[:40]

    best = None
    for path in candidates:
        body = raw_get(repo, branch, path)
        if not body:
            continue
        strong = strong_signals(body)
        if not strong:
            continue
        weak = weak_words(body)
        score = len(strong) * 2 + len(weak)
        # A test file proves the integration exists, but the implementation is
        # the better witness: tests get deleted while features stay, and a
        # mocked string is weaker proof than a real call site.
        if TEST_PATH.search(path):
            score -= 5
        # Config and fixture files mention endpoints without calling them.
        if re.search(r"(^|/)(fixtures?|config|constants|prefs)[./]", path, re.I):
            score -= 3
        if best is None or score > best["score"]:
            best = {
                "score": score,
                "path": path,
                "matched": (strong[:2] + weak[:2])[:4],
                "signals": primitive_signals(body),
            }
    if not best:
        return {"slug": slug, "status": "no-call-site", "repo": repo}
    proposal = {
        "slug": slug,
        "status": "proposed",
        "repo": repo,
        "path": best["path"],
        "matched": best["matched"],
        # A hint for the person reading the file, never a value for question_types.
        "primitive_signals": best["signals"],
    }
    if entry.get("kind") == "alternative":
        proposal["kind"] = "wire-shape"
    return proposal


# --- primitives_seen ---------------------------------------------------------

SEEN = "primitives_seen"
# A read that found the cited file without the claim, or no file or repository
# at all: that file shows nothing now, so the row carries no signal. A read the
# rate limit stopped is no read, and changes nothing. A file whose claim lost
# only its model version (version-moved) was read and still holds the rest, so
# its signals count like a pass.
UNSEEN = ("claim-gone", "path-gone", "repo-gone")
READ = ("ok", VERSION_MOVED)


EXPERIMENTAL_SEEN = "experimental_seen"


def seen_after(result: dict, signals: str = "primitive_signals") -> list[str] | None:
    """What a row's primitives_seen (or, with signals="experimental_signals",
    its experimental_seen) should be after this read; None to leave it."""
    if result["status"] in READ:
        return list(result.get(signals) or [])
    if result["status"] in UNSEEN:
        return []
    return None


def with_seen(entry: dict, seen: list[str], field: str = SEEN) -> dict:
    """A copy of the row carrying `seen` in `field`, or no `field` when `seen`
    is empty. primitives_seen goes right after `evidence`; experimental_seen
    after the last of `evidence`, primitives_seen and observed_thresholds the
    row has, the schema's order. Every other key keeps its place and value."""
    after = "evidence"
    if field != SEEN:
        after = next((key for key in ("observed_thresholds", SEEN) if key in entry), "evidence")
    out: dict = {}
    for key, value in entry.items():
        if key == field:
            continue
        out[key] = value
        if key == after and seen:
            out[field] = list(seen)
    return out


def apply_experimental(catalog: list[dict], results: list[dict]) -> tuple[list[dict], list[str]]:
    """The catalogue with each read row's experimental_seen brought up to
    date, and one log line per row whose value changed."""
    by_slug = {r["slug"]: r for r in results}
    rows, lines = [], []
    for entry in catalog:
        result = by_slug.get(entry.get("slug"))
        seen = seen_after(result, "experimental_signals") if result else None
        old = list(entry.get(EXPERIMENTAL_SEEN) or [])
        if seen is None or seen == old:
            rows.append(entry)
            continue
        lines.append(f"  {'+' if seen else '-'} {entry['slug']}: experimental {', '.join(seen or old)}")
        rows.append(with_seen(entry, seen, EXPERIMENTAL_SEEN))
    return rows, lines


def apply_signals(catalog: list[dict], results: list[dict]) -> tuple[list[dict], dict[str, list[str]]]:
    """The catalogue with each read row's primitives_seen brought up to date,
    and one log line per row by outcome. question_types is never read or written."""
    by_slug = {r["slug"]: r for r in results}
    outcome: dict[str, list[str]] = {"added": [], "changed": [], "removed": [], "unchanged": [], "unread": []}
    rows = []
    for entry in catalog:
        result = by_slug.get(entry.get("slug"))
        seen = seen_after(result) if result else None
        old = list(entry.get(SEEN) or [])
        if result is None:
            rows.append(entry)
            continue
        slug = entry["slug"]
        if seen is None:
            outcome["unread"].append(f"  ? {slug}: {result['status']}, left as it was")
        elif seen == old:
            outcome["unchanged"].append(slug)
        elif not old:
            outcome["added"].append(f"  + {slug}: {', '.join(seen)}")
        elif not seen:
            why = "no shape in the file" if result["status"] in READ else result["status"]
            outcome["removed"].append(f"  - {slug}: {', '.join(old)} ({why})")
        else:
            outcome["changed"].append(f"  ~ {slug}: {', '.join(old)} -> {', '.join(seen)}")
        rows.append(entry if seen is None or seen == old else with_seen(entry, seen))
    return rows, outcome


def write_signals(catalog: list[dict], todo: list[dict]) -> int:
    """--write-signals: read every cited file and record primitives_seen.

    Exit 0 whatever the claims show: a claim that stopped holding is the
    claims job's alarm, and this run only records what each file shows. The
    last line printed is always the counts, for the workflow log."""
    print(f"reading {len(todo)} cited file(s) for primitive text signals\n", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(check, todo))
    rows, outcome = apply_signals(catalog, results)
    rows, experimental = apply_experimental(rows, results)
    for kind in ("added", "changed", "removed", "unread"):
        for line in outcome[kind]:
            print(line)
    for line in experimental:
        print(line)
    counts = (
        f"primitive text signals: {len(results)} row(s) with evidence; "
        f"{len(outcome['added'])} added, {len(outcome['changed'])} changed, "
        f"{len(outcome['removed'])} removed, {len(outcome['unchanged'])} unchanged; "
        f"{len(outcome['unread'])} not read (GitHub rate limit or no repository); "
        f"experimental features: {len(experimental)} row(s) changed"
    )
    step_summary(
        "## Primitive text signals\n\n"
        "`primitives_seen`: primitives whose request or answer shape each row's cited file "
        "contains. A machine text signal, not a person's reading, and not `question_types`.\n\n"
        f"- {counts}\n"
        + "".join(f"- {line}\n" for line in usage_lines())
    )
    if rows != catalog:
        CATALOG.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n")
        print(f"wrote {CATALOG.name}")
    else:
        print("nothing to write")
    log_usage()
    print(counts)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", default="", help="check a single slug")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--discover", action="store_true", help="propose evidence for rows lacking it"
    )
    mode.add_argument(
        "--write-signals",
        action="store_true",
        help="record in catalog.json the primitives whose shape each cited file contains (primitives_seen)",
    )
    mode.add_argument(
        "--propose-version-rewrite",
        action="store_true",
        help="dry run: for each version-moved row, print evidence.matched rewritten to the version its "
        "file now names; writes nothing and never touches read_on",
    )
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()

    catalog = json.loads(CATALOG.read_text())

    if args.write_signals:
        todo = [e for e in catalog if "evidence" in e and (not args.only or e["slug"] == args.only)]
        return write_signals(catalog, todo)

    if args.propose_version_rewrite:
        todo = [e for e in catalog if "evidence" in e and (not args.only or e["slug"] == args.only)]
        return propose_rewrites(todo, args.json)

    if args.discover:
        todo = [e for e in catalog if needs_discovery(e) and (not args.only or e["slug"] == args.only)]
        print(f"discovering evidence for {len(todo)} row(s)\n", file=sys.stderr)
        if args.only and not todo:
            print(
                f"{args.only}: not a row that needs one: it already carries evidence or "
                "evidence_none, has no code, has no GitHub repository, or is not in catalog.json",
                file=sys.stderr,
            )
        with ThreadPoolExecutor(max_workers=WORKERS) as pool:
            results = list(pool.map(discover, todo))
        if args.json:
            print(json.dumps(results, indent=2, ensure_ascii=False))
        else:
            for r in results:
                if r["status"] == "proposed":
                    print(
                        f"  {r['slug']}\n    path: {r['path']}\n    matched: {r['matched']}"
                    )
                    if r.get("primitive_signals"):
                        print(
                            f"    primitive shapes in that file: {', '.join(r['primitive_signals'])} "
                            "(a text signal: read the call before setting question_types)"
                        )
                    if r.get("kind"):
                        print(f"    kind: {r['kind']} (the row is an alternative, so the file is not where it builds on Jev)")
                else:
                    print(f"  {r['slug']}  [{r['status']}]")
        return 0

    todo = [
        e
        for e in catalog
        if "evidence" in e and (not args.only or e["slug"] == args.only)
    ]
    # Each file an alternative row's wire record cites is a claim of its own.
    wire_todo = [
        (e, source) for e in catalog if not args.only or e["slug"] == args.only for source in wire_claims(e)
    ]
    if not todo and not wire_todo:
        print("no rows carry evidence yet")
        return 0

    print(f"re-checking {len(todo)} claim(s) and {len(wire_todo)} wire source file(s)\n", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(check, todo)) + list(pool.map(check_wire, wire_todo))
    # Only once every claim is read, so the search spends what the reads left.
    proposed = propose_paths(results)
    gone = sum(1 for r in results if r["status"] == "path-gone")

    # A claim the rate limit kept us from reading is neither a pass nor a
    # failure. Counting it as either would be the false report this avoids.
    skipped = [r for r in results if r["status"] == "skipped"]
    # A version-moved claim still fails: its strings are gone, and only a
    # person may rewrite them. It is reported apart, grouped by version.
    failed = [r for r in results if r["status"] not in ("ok", "skipped")]
    moves = version_moves(results)
    moved = sum(len(slugs) for slugs in moves.values())
    step_summary(
        "## Cited call sites\n\n"
        + f"- checked {len(results) - len(skipped)} of {len(results)} claim(s): "
        + f"{len(failed)} failed, {len(skipped)} skipped (GitHub rate limit)\n"
        + f"- {len(wire_todo)} of them are files an `alternative` row's `wire` record cites (wire.source)\n"
        + (f"- {moved} of the failures only moved to another model version:\n" if moved else "")
        + "".join(f"  - {line}\n" for line in move_lines(moves))
        + (f"- {path_line(proposed, gone)}\n" if gone else "")
        + "".join(f"- {line}\n" for line in usage_lines())
    )
    if skipped:
        print(
            f"::warning title=Claims not checked::{len(skipped)} of {len(results)} "
            "cited call sites were not read: GitHub rate limit. They are not failures.",
            file=sys.stderr,
        )
    if args.json:
        print(
            json.dumps(
                {
                    "checked": len(results),
                    "failed": failed,
                    "skipped": skipped,
                    # Slugs by the version their cited file now names; each is also in `failed`.
                    "version_moved": moves,
                    # A file holding every matched string, for each path-gone claim that has one;
                    # each is also in `failed`.
                    "proposed_paths": [
                        {key: r[key] for key in ("slug", "claim", "path", "proposed_path") if key in r}
                        for r in results
                        if r.get("proposed_path")
                    ],
                    # A text signal per file whose claim held; see --write-signals.
                    "primitive_signals": {
                        r["slug"]: r["primitive_signals"]
                        for r in results
                        if r["status"] == "ok" and r.get("primitive_signals")
                    },
                },
                indent=2,
                ensure_ascii=False,
            )
        )
    else:
        for r in results:
            mark = "ok  " if r["status"] == "ok" else r["status"].upper()
            shapes = r.get("primitive_signals")
            tail = f"  · primitive shapes: {', '.join(shapes)}" if shapes else ""
            print(f"  {mark:<12} {r['slug']}  {r['detail']}{tail}")
        lines = move_lines(moves) + ([path_line(proposed, gone)] if gone else [])
        if lines:
            print()
            for line in lines:
                print(line)
        held = len(results) - len(failed) - len(skipped)
        tail = f"; {len(skipped)} not checked (GitHub rate limit)" if skipped else ""
        print(f"\n{held}/{len(results)} claims still hold{tail}")
        if failed:
            print("\nFailures need a person: an upstream rename is a false positive,")
            print("a removed integration means the row's question_types is now wrong.")
            if any(r.get("claim") == WIRE for r in failed):
                print("A wire.source failure: the file behind a row's wire record changed; re-read it and correct wire.")
    log_usage()

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
