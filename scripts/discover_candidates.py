#!/usr/bin/env python3
"""Find catalog candidates by aggregating sibling lists, then verifying them.

There are dozens of Jev directories. Each is a different person's sweep of the
same ecosystem, so the union of them is a far better discovery surface than any
one — including this one. A repository cited by twenty lists is worth looking
at.

But citation frequency is not verification. These lists copy from each other,
so a repository miscatalogued once propagates everywhere: the most-starred
"Jev visual inference tool" in this ecosystem turned out to contain zero
references to the API, and it is listed as a Jev project almost universally.
Crowd agreement is a discovery signal and nothing more.

So this does both halves. It harvests every sibling list, ranks by how many
cite each repository, then reads the candidate's actual code looking for a call
site. What it emits is a shortlist for a person, never a catalog row — the whole
point of this catalog is that someone read the source.

Usage:
  python3 scripts/discover_candidates.py                 # top 40 candidates
  python3 scripts/discover_candidates.py --top 100
  python3 scripts/discover_candidates.py --json > out.json
  python3 scripts/discover_candidates.py --only owner/name   # re-read one candidate
  python3 scripts/discover_candidates.py --only owner/name --drafts drafts
      # ...and write drafts/<slug>.json, a draft row to complete (discover_drafts.py)
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import pathlib
import re
import sys
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from _github import CODE_EXT, SELF, api_get, default_branch, raw_get, repo_of, strong_signals  # noqa: E402
# The keyword rules behind each candidate's suggested kind and patterns live in
# classify.py; re-exported, so `from discover_candidates import classify` works.
from classify import classify  # noqa: E402,F401
from discover_seen import (  # noqa: E402
    PROPOSED,
    RECHECK_DAYS,
    VERDICTS,
    load as load_seen,
    merge as merge_seen,
    parse as parse_seen,
    report_dropped,
    write as write_seen,
)
import discover_drafts  # noqa: E402
# Reading the sibling lists and counting their citations lives in
# sibling_lists.py, shared with attribute_sources.py; re-exported here.
from sibling_lists import (  # noqa: E402,F401
    GH,
    SIBLINGS,
    SKIP_OWNERS,
    fetch_readme,
    harvest,
    read_lists,
    slug_of,
)

# The weekly issue: at most this many new boxes (the rest are saved with their
# verdict and listed among the earlier candidates from the next run on), and at
# most this many earlier candidates, so a comment stays well under GitHub's
# 65,536-character limit.
NEW_SHOWN = 60
WAITING_SHOWN = 100
# Printed under every box. It re-reads that one repository with the code below
# and prints the same verdict, call site and matched strings. Not
# verify_claims.py --discover: that one proposes evidence only for rows already
# in catalog.json, and says "0 row(s)" for a candidate.
COMMAND = "python3 scripts/discover_candidates.py --only {slug}"
CONTRIBUTING_URL = f"https://github.com/{SELF}/blob/main/CONTRIBUTING.md#adding-an-entry"
DECLINED_URL = f"https://github.com/{SELF}/blob/main/docs/declined.txt"
CLAIM_EN = (
    "Each box is a repository whose code a script found calling Jev: a reason to "
    "read it, not a catalog row. To take one, comment `claim owner/name` on this "
    "issue so two people do not read the same code, then read the call site and "
    f"open a pull request adding its row ([Adding an entry]({CONTRIBUTING_URL})). "
    "If it does not belong, open a pull request adding it to "
    f"[`docs/declined.txt`]({DECLINED_URL}) with the reason instead. The command "
    "with each box re-reads that repository now and prints the verdict, the call "
    "site and the strings it matched. Add `--drafts drafts` to it and it also "
    "writes `drafts/<slug>.json`: the row with what the script found filled in, "
    "for you to complete. lint refuses it until its `_draft` field is gone."
)
# Model-written, so marked the way the README marks machine Chinese.
CLAIM_ZH = (
    "每个复选框是一个仓库：脚本在它的代码里找到了 Jev 调用——这是去读代码的理由，"
    "不是一条目录记录。想认领一条，先在本 issue 评论 `claim owner/name`，免得两个人读同一份代码；"
    f"然后阅读调用点，提交添加该行的 pull request（[添加条目]({CONTRIBUTING_URL})）。"
    f"若它不该收录，就提交 pull request 把它加进 [`docs/declined.txt`]({DECLINED_URL}) 并写明理由。"
    "每个复选框附带的命令会立即重读该仓库，打印判定、调用点和匹配到的字符串；"
    "加上 `--drafts drafts` 还会写出 `drafts/<slug>.json`：已填好脚本所知信息的草稿行，由你补全。"
    "在删掉其中的 `_draft` 字段之前，lint 会拒绝它。 <sub>(机翻)</sub>"
)

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
# Candidates a person read and chose not to add, one `owner/name  # reason` per
# line. Without it the weekly run would re-propose the same rejects forever.
DECLINED = ROOT / "docs" / "declined.txt"
# RECHECK_DAYS and VERDICTS live in discover_seen.py, beside the verdict file
# they describe.
WORKERS = 8

# Same preference verify_claims.py applies. A fixture called fake_jev.py
# proves the request shape, not that anything ever calls the API — and a
# fake is exactly the evidence that would embarrass this catalog later.
# scripts/model_draft.py asks the same of the file a model cites.
TEST_PATH = re.compile(
    r"(^|/)(tests?|spec|__tests__|fixtures?)/|\.(test|spec)\.[a-z]+$"
    r"|_test\.[a-z]+$|test_[^/]*$|fake[_-]|mock[_-]",
    re.I,
)

# A candidate is judged by the signals verify_claims.py proposes evidence by,
# _github.strong_signals(): an import, the endpoint or a model name is proof, a
# bare primitive name is not, because "choice" and "score" are ordinary words.
# The model names come from compat.json, so a release changes one file.


def only_slug(text: str) -> str | None:
    """owner/name, or a github.com URL of one, as a slug; None otherwise."""
    match = re.fullmatch(
        r"(?:https://github\.com/)?([A-Za-z0-9][\w.-]*)/([\w.-]+?)/?", text.strip()
    )
    if not match or match.group(2) in (".", ".."):
        return None
    return slug_of(*match.groups())


def inspect(slug: str) -> dict:
    """Read a candidate's code and decide whether it genuinely calls Jev."""
    meta = api_get(f"/repos/{slug}")
    if not isinstance(meta, dict) or "stargazers_count" not in meta:
        return {"slug": slug, "verdict": "repo-gone"}

    out = {
        "slug": slug,
        "url": meta["html_url"],
        "stars": meta["stargazers_count"],
        "license": ((meta.get("license") or {}).get("spdx_id") or "unknown"),
        "language": meta.get("language") or "-",
        "archived": bool(meta.get("archived")),
        "created": (meta.get("created_at") or "")[:10],
        "pushed": (meta.get("pushed_at") or "")[:10],
        "description": meta.get("description") or "",
    }

    branch = default_branch(slug)
    tree = api_get(f"/repos/{slug}/git/trees/{branch}?recursive=1") if branch else None
    if not isinstance(tree, dict) or "tree" not in tree:
        return {**out, "verdict": "tree-unavailable"}

    # An extensionless file named after Jev is almost always a CLI script with a
    # shebang (okooo5km/jev's lives at jev/scripts/jev); read those too.
    paths = [
        n["path"]
        for n in tree["tree"]
        if n.get("type") == "blob"
        and (
            n["path"].endswith(CODE_EXT)
            or (
                "." not in n["path"].rsplit("/", 1)[-1]
                and re.search(r"jev|typesafe", n["path"].rsplit("/", 1)[-1], re.I)
            )
        )
    ]
    hinted = [p for p in paths if re.search(r"jev|typesafe", p, re.I)]
    testy = TEST_PATH
    best: tuple[int, str, list[str]] | None = None

    def scan(candidates: list[str]) -> None:
        nonlocal best
        for path in candidates:
            body = raw_get(slug, branch, path)
            if not body:
                continue
            found = strong_signals(body)
            if not found:
                continue
            score = len(found) - (5 if testy.search(path) else 0)
            if best is None or score > best[0]:
                best = (score, path, found[:3])

    scan((hinted or paths)[:30])
    # Files named after Jev are the likeliest call sites, but not the only ones:
    # belay.mjs, src/model.ts and a DuckDB extension's jev_client.cpp were all
    # missed this way, and each looked test-only because its test file had the
    # hinted name. If nothing but a test matched, read the rest of the source.
    if best is None or testy.search(best[1]):
        rest = [p for p in paths if p not in hinted and not testy.search(p)]
        scan(rest[:60])
    if best:
        kind, patterns = classify(
            out["description"], slug.split("/")[1], out["language"]
        )
        return {
            **out,
            "verdict": "calls-jev",
            "suggested_kind": kind,
            "suggested_patterns": patterns,
            "evidence_path": best[1],
            "matched": best[2],
            "evidence_is_test": bool(testy.search(best[1])),
        }

    # A README may claim Jev while the code never calls it. That gap is exactly
    # what propagates through these lists, so name it rather than guessing.
    _, readme = fetch_readme(out["url"])
    mentions = bool(strong_signals(readme)) or bool(
        re.search(r"\bjev\b", readme, re.I)
    )
    return {**out, "verdict": "mentions-only" if mentions else "no-signal"}


def parse_declined(text: str) -> dict[str, str]:
    """owner/name, lower-cased, to the reason given, from docs/declined.txt's lines."""
    out = {}
    for line in text.splitlines():
        body, _, reason = line.partition("#")
        if body.strip():
            out[body.strip().lower()] = reason.strip()
    return out


def read_declined() -> dict[str, str]:
    if not DECLINED.exists():
        return {}
    return parse_declined(DECLINED.read_text())


def find_new_lists(lists: list[str]) -> list[dict]:
    """Sibling directories GitHub search can see that sibling-lists.txt cannot.
    The discovery surface should grow on its own, not stay at the lists that
    happened to exist the week this repository was built."""
    known = {slug_of(*GH.match(u).groups()) for u in lists if GH.match(u)}
    found: dict[str, dict] = {}
    for query in ("awesome-jev in:name", "jev awesome in:name,description"):
        data = api_get(
            "/search/repositories?per_page=50&sort=updated&q="
            + urllib.parse.quote(query)
        )
        for repo in (data or {}).get("items", []):
            slug = repo["full_name"].lower()
            if slug in known or slug == SELF.lower() or repo.get("fork"):
                continue
            found[slug] = {
                "slug": repo["full_name"],
                "url": repo["html_url"],
                "stars": repo.get("stargazers_count", 0),
                "description": repo.get("description") or "",
            }
    return sorted(found.values(), key=lambda r: -r["stars"])


def inert(text: str, limit: int = 100) -> str:
    """A repository description is text a stranger chose, and it lands in an
    issue this repository posts. Neutralise the three things it could do there:
    @-mention someone (a zero-width joiner after @ stops the ping), break out of
    a table cell, or start a new Markdown block."""
    text = " ".join(text.split())[:limit]
    return text.replace("@", "@\u2060").replace("|", "\\|").replace("<", "&lt;")


def code_span(text: str, limit: int = 120) -> str:
    """A path from a stranger's repository, shown as inline code in the issue.
    Without a backtick it cannot end the span early, and inside the span an @
    pings nobody and brackets cannot close the link around it."""
    return " ".join(str(text).split())[:limit].replace("`", "'")


def blob_url(repo_url: str, path: str) -> str:
    """The file on the default branch. Percent-encoded, so a space or a
    parenthesis in the path cannot end the Markdown link."""
    return f"{repo_url}/blob/HEAD/{urllib.parse.quote(path, safe='/')}"


def task_lines(r: dict) -> list[str]:
    """One new candidate: a box to tick, and the command that re-reads it."""
    warn = " ⚠ test file" if r.get("evidence_is_test") else ""
    call_site = f"[`{code_span(r['evidence_path'])}`]({blob_url(r['url'], r['evidence_path'])})"
    return [
        f"- [ ] [{r['slug']}]({r['url']}) · cited by {r['cited_by']} · ★{r.get('stars', 0)}"
        f" · call site {call_site}{warn}"
        f" · suggested {r['suggested_kind']} / {', '.join(r['suggested_patterns'])}",
        f"  `{COMMAND.format(slug=r['slug'])}`",
    ]


def waiting_lines(waiting: list[tuple[str, dict]]) -> list[str]:
    """Candidates proposed in earlier weeks, by name, oldest verdict first."""
    shown = sorted(waiting, key=lambda item: (item[1]["on"], item[0]))[:WAITING_SHOWN]
    n = len(waiting)
    lines = [
        "<details>",
        f"<summary>{n} candidate{'s' if n != 1 else ''} from earlier weeks "
        f"{'are' if n != 1 else 'is'} still neither catalogued nor declined</summary>",
        "",
    ]
    lines += [
        f"- [ ] [{slug}](https://github.com/{slug}) · read by script {entry['on']}"
        f" · `{COMMAND.format(slug=slug)}`"
        for slug, entry in shown
    ]
    if n > len(shown):
        lines.append(f"- …and {n - len(shown)} more, not shown to keep this comment short.")
    return lines + ["", "</details>", ""]


def report_markdown(
    results: list[dict],
    new_hits: list[dict],
    waiting: list[tuple[str, dict]],
    new_lists: list[dict],
    reached: int,
    total_lists: int,
) -> str:
    """The weekly discovery issue. A shortlist for a person, never a row: each
    candidate still has to be read and summarised before it enters the catalog.

    A GitHub task list, so a person can say which one they are reading, with
    the command that re-reads each candidate. `waiting` is (slug, verdict) for
    candidates proposed in earlier weeks, printed by name; they alone never add
    a `### ` heading, which is what discover.yml posts on."""
    counts = collections.Counter(r["verdict"] for r in results)
    lines = [
        f"Harvested {reached}/{total_lists} sibling lists and read the code of "
        f"{len(results)} cited repositories not yet in the catalog: "
        + ", ".join(f"{n} {v}" for v, n in counts.most_common())
        + ".",
        "",
    ]
    if new_hits or waiting:
        lines += [CLAIM_EN, "", CLAIM_ZH, ""]
    if new_hits:
        ranked = sorted(new_hits, key=lambda r: (-r["cited_by"], -r.get("stars", 0), r["slug"]))
        lines += [
            f"### {len(new_hits)} new candidate{'s' if len(new_hits) != 1 else ''} with a call site",
            "",
        ]
        for r in ranked[:NEW_SHOWN]:
            lines += task_lines(r)
        if len(ranked) > NEW_SHOWN:
            lines += [
                "",
                f"Showing {NEW_SHOWN} of {len(ranked)}; the rest are listed among "
                "the earlier candidates from the next run on.",
            ]
        lines.append("")
    else:
        lines += ["No new candidate with a call site this week.", ""]
    if waiting:
        lines += waiting_lines(waiting)
    if new_lists:
        lines += [
            f"### {len(new_lists)} possible sibling director{'ies' if len(new_lists) != 1 else 'y'}",
            "",
            "Not in `docs/sibling-lists.txt`. Adding a real one widens next week's harvest.",
            "",
        ]
        lines += [
            f"- [{r['slug']}]({r['url']}) ★{r['stars']} — {inert(r['description'])}"
            for r in new_lists[:20]
        ]
        lines.append("")
    lines.append(
        "A call site found by a script is a reason to read the code, not a catalog "
        "row. Suggested kinds and patterns come from keyword rules with a known "
        "error rate; check both."
    )
    return "\n".join(lines)


def print_results(results: list[dict]) -> None:
    """The console report, grouped by verdict. A harvest shows how many lists
    cite each repository; a single --only read has no such count."""
    by_verdict = collections.Counter(r["verdict"] for r in results)
    for verdict in VERDICTS:
        rows = [r for r in results if r["verdict"] == verdict]
        if not rows:
            continue
        print(f"\n=== {verdict} ({len(rows)}) ===")
        for r in rows:
            cited = f"{r['cited_by']:>2} lists  " if "cited_by" in r else ""
            print(f"  {cited}★{r.get('stars', 0):<7} {r['slug']}")
            if verdict == "calls-jev":
                print(f"          {r['evidence_path']}  -> {r['matched']}")
                print(f"          {blob_url(r['url'], r['evidence_path'])}")
                print(
                    f"          suggested: {r['suggested_kind']} / "
                    f"{', '.join(r['suggested_patterns'])}  (check it)"
                )
            if r.get("description"):
                print(f"          {r['description'][:96]}")

    print(f"\n{dict(by_verdict)}")
    print(
        "\nA `calls-jev` verdict means a call site was found, not that the row is "
        "ready.\nSomeone still has to read it and write the summary — that is the "
        "whole point."
    )


def catalogued(catalog: list[dict]) -> set[str]:
    """owner/name of every catalogued GitHub repository, lower-cased."""
    return {repo.lower() for repo in (repo_of(e) for e in catalog) if repo}


def inspect_only(text: str, *, as_json: bool, drafts: str = "") -> int:
    """`--only owner/name`: the command the discovery issue prints under each
    box. Reads that one repository now, as the weekly run did, and prints the
    same verdict. No harvest, and no verdict file is read or written: a
    person's run proposes nothing to anyone. With `drafts`, a candidate that
    calls Jev and is neither catalogued nor declined also gets a draft row."""
    slug = only_slug(text)
    if not slug:
        print(f"error: --only takes owner/name or its GitHub URL, not {text!r}", file=sys.stderr)
        return 2
    catalog = json.loads(CATALOG.read_text())
    # With --json the notes go to stderr, so stdout stays one JSON document.
    notes = sys.stderr if as_json else sys.stdout
    known = ""
    if slug in catalogued(catalog):
        known = "already in catalog.json"
        print(f"note: {slug} is {known}", file=notes)
    declined = read_declined()
    if slug in declined:
        known = "declined in docs/declined.txt"
        print(
            f"note: {slug} was declined in docs/declined.txt: {declined[slug] or '(no reason given)'}",
            file=notes,
        )
    print(f"reading {slug}", file=sys.stderr)
    result = inspect(slug)
    if as_json:
        print(json.dumps([result], indent=2, ensure_ascii=False))
    else:
        print_results([result])
    if drafts:
        # Not a harvest, so nothing says which list cited it: sources is left to the person.
        discover_drafts.report([result], drafts, sourced=False, skip=known)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--top", type=int, default=40, help="candidates to verify")
    parser.add_argument("--json", action="store_true")
    parser.add_argument(
        "--seen",
        action="append",
        default=[],
        metavar="FILE",
        help="verdict file (repeatable): all are read and merged, newest verdict per "
        "repository winning; fresh ones are not read again; the merged verdicts, "
        "this run's included, are written back to each (see discover_seen.py)",
    )
    parser.add_argument(
        "--markdown", default="", help="write a Markdown report here, for an issue body"
    )
    parser.add_argument(
        "--find-lists",
        action="store_true",
        help="also search GitHub for sibling directories not yet in sibling-lists.txt",
    )
    parser.add_argument(
        "--only",
        default="",
        metavar="OWNER/NAME",
        help="read just this repository now and print its verdict (no harvest, no verdict file)",
    )
    parser.add_argument(
        "--drafts",
        default="",
        metavar="DIR",
        help="also write DIR/<slug>.json, a draft catalog row, for each repository found "
        "calling Jev (never over an existing file); lint refuses a draft until a person "
        "completes it (see discover_drafts.py)",
    )
    args = parser.parse_args(argv)
    if args.only:
        return inspect_only(args.only, as_json=args.json, drafts=args.drafts)
    today = dt.date.today()
    # The committed .discover/seen.json and the Actions cache copy: whichever
    # holds the newer verdict for a repository wins.
    loaded = []
    for path in args.seen:
        verdicts, dropped = load_seen(path, today=today)
        report_dropped(path, dropped)
        print(f"{path}: {len(verdicts)} verdict(s)", file=sys.stderr)
        loaded.append(verdicts)
    seen: dict[str, dict] = merge_seen(*loaded)

    if not SIBLINGS.exists():
        print(f"error: {SIBLINGS.relative_to(ROOT)} is missing", file=sys.stderr)
        return 1
    lists = read_lists(SIBLINGS)

    print(f"harvesting {len(lists)} sibling list(s)", file=sys.stderr)
    # fetch_readme is looked up here, so a test can patch it on this module.
    found = harvest(lists, fetch=fetch_readme, workers=WORKERS)
    cites = found.counts()
    reached = len(found.reached)

    catalog = json.loads(CATALOG.read_text())
    have = catalogued(catalog)
    # Sibling lists themselves are already catalogued or deliberately excluded.
    have |= {slug_of(*GH.match(u).groups()) for u in lists if GH.match(u)}
    declined = read_declined()
    have |= set(declined)

    def fresh(slug: str) -> bool:
        """Read recently enough that reading it again would only repeat the
        verdict. A candidate already proposed is listed as waiting instead —
        re-reading it every week spent a third of each run's budget on
        repositories that were already on a person's list."""
        past = seen.get(slug)
        return bool(past) and (
            today - dt.date.fromisoformat(past["on"])
        ).days < RECHECK_DAYS

    candidates = [
        (slug, n) for slug, n in cites.most_common() if slug not in have and not fresh(slug)
    ]
    recent = sum(1 for slug in cites if slug not in have and fresh(slug))
    print(
        f"reached {reached}/{len(lists)} lists, {len(cites)} repos cited, "
        f"{len(candidates)} not in the catalog and due a read "
        f"({recent} read in the last {RECHECK_DAYS} days, not read again)",
        file=sys.stderr,
    )

    shortlist = [slug for slug, _ in candidates[: args.top]]
    print(f"verifying the top {len(shortlist)} by citation count\n", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(inspect, shortlist))
    for result, (slug, n) in zip(results, candidates[: args.top]):
        result["cited_by"] = n
        # Which lists, not only how many: the URLs, never their descriptions.
        result["cited_lists"] = sorted(found.cited[slug])

    # GitHub redirects a renamed repository, so two cited names can resolve to
    # one canonical html_url. Without this the same project is proposed twice
    # under different slugs, and only the catalog linter catches it.
    # A candidate is cited under whatever name the citing list used; inspect()
    # reports GitHub's canonical URL. Compare that against the catalogue too,
    # or a renamed or transferred project comes back as "new" — four of the
    # first eighty did (hermes-jev renamed to hermes-nerve, among them).
    seen_urls: set[str] = {
        u.rstrip("/").lower() for e in catalog for u in (e.get("url"), e.get("repo")) if u
    }
    deduped = []
    for r in results:
        key = (r.get("url") or r["slug"]).rstrip("/").lower()
        if key in seen_urls:
            continue
        seen_urls.add(key)
        deduped.append(r)
    results = deduped
    if args.drafts:
        # Every one of these was cited by a sibling list, and none is catalogued or declined.
        hits = [r for r in results if r["verdict"] == PROPOSED]
        discover_drafts.report(hits, args.drafts, sourced=True)

    # New = calls Jev now and was not proposed before. A repository read before
    # and found quiet, then read again after RECHECK_DAYS and found calling Jev,
    # is new: it was never put to anyone, and it is the case the re-read exists
    # for. Listing it among the earlier candidates would also leave the issue
    # without a `### ` heading, so the workflow would not post it at all.
    new_hits = [
        r
        for r in results
        if r["verdict"] == PROPOSED
        and (seen.get(r["slug"]) or {}).get("verdict") != PROPOSED
    ]
    for r in results:
        seen[r["slug"]] = {"verdict": r["verdict"], "on": today.isoformat()}
    # Proposed before, still neither catalogued nor declined: listed by name
    # under the new ones, with this run's re-reads already applied, so one that
    # stopped calling Jev drops out.
    fresh_hits = {r["slug"] for r in new_hits}
    waiting = [
        (slug, past)
        for slug, past in seen.items()
        if past["verdict"] == PROPOSED and slug not in have and slug not in fresh_hits
    ]
    # Only the verdict shape reaches a file that metadata.yml commits: a slug a
    # sibling list spelled oddly is reported here and left out.
    kept, dropped = parse_seen({"verdicts": seen}, today=today)
    report_dropped("this run's verdicts", dropped)
    for path in args.seen:
        write_seen(path, kept)
    if args.seen:
        print(f"wrote {len(kept)} verdict(s) to {', '.join(args.seen)}", file=sys.stderr)

    new_lists = find_new_lists(lists) if args.find_lists else []
    if args.markdown:
        pathlib.Path(args.markdown).write_text(
            report_markdown(results, new_hits, waiting, new_lists, reached, len(lists))
        )

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return 0

    print_results(results)
    return 0


if __name__ == "__main__":
    sys.exit(main())
