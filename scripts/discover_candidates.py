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
import urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from _github import CODE_EXT, SELF, api_get, default_branch, raw_get, repo_of  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
SIBLINGS = ROOT / "docs" / "sibling-lists.txt"
# Candidates a person read and chose not to add, one `owner/name  # reason` per
# line. Without it the weekly run would re-propose the same rejects forever.
DECLINED = ROOT / "docs" / "declined.txt"
# A repository judged not to call Jev is re-read after this long: projects add
# integrations, and a verdict from two months ago is not a verdict about today.
RECHECK_DAYS = 60
WORKERS = 8

GH = re.compile(r"https://github\.com/([A-Za-z0-9][\w.-]*)/([\w.-]+)")

# GitHub's own paths, not repositories.
SKIP_OWNERS = {
    "sponsors",
    "topics",
    "features",
    "about",
    "pricing",
    "login",
    "apps",
    "marketplace",
    "orgs",
    "settings",
    "notifications",
    "explore",
    "collections",
    "readme",
    "search",
    "users",
    "site",
    "github",
}

# Same signals verify_claims.py uses: an import or an endpoint is proof, a bare
# primitive name is not, because "choice" and "score" are ordinary words.
STRONG = [
    "api.typesafe.ai",
    "typesafe_sdk",
    "@typesafe-ai/sdk",
    # The Vercel AI SDK provider: evaluate() calls, where noul is spelled boolean.
    "@ai-sdk/typesafe-ai",
    "typesafe-ai/jev",
    "typesafe/jev",
    "jev-latest",
    "jev-1.13",
    "/v1/systemone",
    "systemOne",
    "system_one",
    "langchain_typesafe",
    "TypeSafeClient",
    "AsyncTypeSafeClient",
]


# ---------------------------------------------------------------------------
# Suggested classification
#
# Keyword rules over the project's own description. They are a starting point
# and nothing more: on the first bulk run of 223 rows they needed eight manual
# corrections, most of them an SDK picking up a behavioural pattern from words
# describing its own API ("typed noul, choice and score" is not content
# scoring, and "observable retries" is the HTTP client, not a retry decision).
# Read the suggestion, then decide.
# ---------------------------------------------------------------------------


def classify(desc, name, lang):
    d = (desc or "").lower()
    n = name.lower()
    t = f"{d} {n}"

    def has(p):
        return bool(re.search(p, t))

    if has(
        r"\b(alternative|jev-?like|jev-?style|reimplement|open-?jev|clone of|drop-?in replacement|"
        r"turn any .{0,24}llm into|local (take on|jev)|own decision model|fine-?tuned from|"
        r"without generating a single to|self-?hosted drop-?in)"
    ):
        kind = "alternative"
    elif has(
        r"\b(benchmark|bench\b|audit|leaderboard|capability (atlas|study)|head-?to-?head|"
        r"reproducible .{0,20}evaluation|measures how well|evaluation of jev)"
    ):
        kind = "benchmark"
    elif has(
        r"\b(sdk|client library|client for|idiomatic .{0,14}(client|sdk)|port of the|"
        r"bindings?\b|dependency-?free cli|small cli)"
    ):
        kind = "sdk"
    elif has(
        r"\b(mcp|skill\b|hook\b|plugin|extension|\.nvim|claude code|codex|neovim|vscode|cursor|"
        r"pytest|pre-?commit|starter\b)"
    ):
        kind = "plugin"
    elif has(
        r"\b(provider|integration|adapter|middleware|for (hono|django|rails|spring|langchain|duckdb))"
    ):
        kind = "integration"
    else:
        kind = "project"

    P = []

    def add(p):
        if p not in P:
            P.append(p)

    # Tightened: a circuit breaker genuinely decides whether to retry; a
    # benchmark about failure *attribution* does not, and matched before.
    if has(r"\bcircuit breaker|retry|retries|back-?off|resilien"):
        add("retry-control")
    if has(
        r"\brerank|re-?rank|relevance|retriev|\brag\b|semantic (search|find|sql|grep)|"
        r"\bgrep|ranking|rank(s|ing)? |select(or|ion) .{0,20}(context|evidence)|shortlist"
    ):
        add("search-ranking")
    if has(
        r"\b(which|cheapest|pick a) (model|llm)|model (routing|selection)|tier\b|"
        r"route .{0,16}model|route accordingly|when to use"
    ):
        add("model-routing")
    if has(
        r"\bclassif|categor|\btag\b|label(s|ling)?\b|taxonom|detect(s|ing|ion)?\b|identif|"
        r"sort(s|ing)?\b|triage"
    ):
        add("classification")
    if has(
        r"\bbrowser|computer use|\bclick|\bgui\b|screen|next action|tool call|agent step|"
        r"control|robot|drive[sn]?\b|navigat|autonomous|tool routing|chains? .{0,14}primitive|"
        r"reflex|harness|which tool|picks? each action"
    ):
        add("tool-selection")
    if has(
        r"\bguard|block(s|ing)?\b|gate|safety|risk|secret|injection|moderat|spam|harmful|"
        r"malicio|permission|censor|sponsor|adblock|\bads?\b"
    ):
        add("safety-gating")
    if has(
        r"\bverif|validat|assert|lint(er|ing)?\b|review|quality|hallucinat|stop hook|"
        r"diagnostic|check(s|ing)?\b|claim|correctness"
    ):
        add("output-validation")
    if has(r"\bscore|rate[sd]?\b|grade|meter|judg"):
        add("content-scoring")
    if has(
        r"\bcompact|prune|trim|context (window|garbage|select)|token budget|history"
    ):
        add("context-compaction")
    if has(r"\bcalibrat|threshold|confidence|uncertain|human review|escalat"):
        add("human-escalation")
    if has(r"\bextract|parse|structured data|field"):
        add("data-extraction")
    if has(r"\bintent|support ticket|inbox|\bmail|email|customer"):
        add("intent-routing")
    if has(r"\bparallel|batch|fan-?out|many questions|more than 255|beyond 255"):
        add("fan-out")
    # Tightened: "suggest" alone matched a skill router, which is tool-selection.
    if has(r"\brecommend(s|ation|er)?\b|what to (watch|read|buy)|next-?best"):
        add("recommendation")
    if has(r"\bfeature (extraction|engineering)|training data|curation|dataset"):
        add("feature-extraction")
    if has(r"\bdocument|\binvoice|\breceipt|\bpdf\b|\bform\b"):
        add("document-triage")

    if not P:
        P = ["overview"]
    return kind, P[:3]


def slug_of(owner: str, name: str) -> str:
    return f"{owner.lower()}/{re.sub(r'\\.git$', '', name).lower()}"


def fetch_readme(repo_url: str) -> tuple[str, str]:
    match = GH.match(repo_url)
    if not match:
        return repo_url, ""
    slug = f"{match.group(1)}/{match.group(2)}"
    for branch in ("main", "master"):
        for name in ("README.md", "readme.md"):
            try:
                req = urllib.request.Request(
                    f"https://raw.githubusercontent.com/{slug}/{branch}/{name}",
                    headers={"User-Agent": "awesome-jev"},
                )
                with urllib.request.urlopen(req, timeout=20) as response:
                    return repo_url, response.read().decode("utf-8", "replace")
            except Exception:  # noqa: BLE001
                continue
    return repo_url, ""


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
    # Same preference verify_claims.py applies. A fixture called fake_jev.py
    # proves the request shape, not that anything ever calls the API — and a
    # fake is exactly the evidence that would embarrass this catalog later.
    testy = re.compile(
        r"(^|/)(tests?|spec|__tests__|fixtures?)/|\.(test|spec)\.[a-z]+$"
        r"|_test\.[a-z]+$|test_[^/]*$|fake[_-]|mock[_-]",
        re.I,
    )
    best: tuple[int, str, list[str]] | None = None

    def scan(candidates: list[str]) -> None:
        nonlocal best
        for path in candidates:
            body = raw_get(slug, branch, path)
            if not body:
                continue
            found = [s for s in STRONG if s in body]
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
    mentions = any(s in readme for s in STRONG) or bool(
        re.search(r"\bjev\b", readme, re.I)
    )
    return {**out, "verdict": "mentions-only" if mentions else "no-signal"}


def read_declined() -> dict[str, str]:
    if not DECLINED.exists():
        return {}
    out = {}
    for line in DECLINED.read_text().splitlines():
        body, _, reason = line.partition("#")
        if body.strip():
            out[body.strip().lower()] = reason.strip()
    return out


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


def report_markdown(
    results: list[dict],
    new_hits: list[dict],
    waiting: list[str],
    new_lists: list[dict],
    reached: int,
    total_lists: int,
) -> str:
    """The weekly discovery issue. A shortlist for a person, never a row: each
    candidate still has to be read and summarised before it enters the catalog."""
    counts = collections.Counter(r["verdict"] for r in results)
    lines = [
        f"Harvested {reached}/{total_lists} sibling lists and read the code of "
        f"{len(results)} cited repositories not yet in the catalog: "
        + ", ".join(f"{n} {v}" for v, n in counts.most_common())
        + ".",
        "",
    ]
    if new_hits:
        lines += [
            f"### {len(new_hits)} new candidate{'s' if len(new_hits) != 1 else ''} with a call site",
            "",
            "| Repository | Cited by | ★ | Call site | Suggested |",
            "| --- | --- | --- | --- | --- |",
        ]
        for r in sorted(new_hits, key=lambda r: (-r["cited_by"], -r.get("stars", 0)))[:60]:
            branch_path = f"{r['url']}/blob/HEAD/{r['evidence_path']}"
            warn = " ⚠ test file" if r.get("evidence_is_test") else ""
            lines.append(
                f"| [{r['slug']}]({r['url']}) | {r['cited_by']} | {r.get('stars', 0)} "
                f"| [`{r['evidence_path']}`]({branch_path}){warn} "
                f"| {r['suggested_kind']} · {', '.join(r['suggested_patterns'])} |"
            )
        lines.append("")
    else:
        lines += ["No new candidate with a call site this week.", ""]
    if waiting:
        lines += [
            f"{len(waiting)} candidates proposed in earlier weeks are still neither "
            "catalogued nor declined. Add each, or decline it in "
            "`docs/declined.txt` with a reason.",
            "",
        ]
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--top", type=int, default=40, help="candidates to verify")
    parser.add_argument("--json", action="store_true")
    parser.add_argument(
        "--seen",
        default="",
        help="JSON cache of past verdicts; skips fresh ones and records this run's",
    )
    parser.add_argument(
        "--markdown", default="", help="write a Markdown report here, for an issue body"
    )
    parser.add_argument(
        "--find-lists",
        action="store_true",
        help="also search GitHub for sibling directories not yet in sibling-lists.txt",
    )
    args = parser.parse_args()
    today = dt.date.today()
    seen: dict[str, dict] = {}
    if args.seen and pathlib.Path(args.seen).exists():
        seen = json.loads(pathlib.Path(args.seen).read_text())

    if not SIBLINGS.exists():
        print(f"error: {SIBLINGS.relative_to(ROOT)} is missing", file=sys.stderr)
        return 1
    lists = [
        line.strip()
        for line in SIBLINGS.read_text().splitlines()
        if line.strip() and not line.startswith("#")
    ]

    print(f"harvesting {len(lists)} sibling list(s)", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        fetched = list(pool.map(fetch_readme, lists))

    cites: collections.Counter[str] = collections.Counter()
    reached = 0
    for _, body in fetched:
        if not body:
            continue
        reached += 1
        for owner, name in set(GH.findall(body)):
            if owner.lower() in SKIP_OWNERS:
                continue
            cites[slug_of(owner, name)] += 1

    catalog = json.loads(CATALOG.read_text())
    have = {repo_of(e) for e in catalog}
    have |= {(repo_of(e) or "").lower() for e in catalog}
    have = {h.lower() for h in have if h}
    # Sibling lists themselves are already catalogued or deliberately excluded.
    have |= {slug_of(*GH.match(u).groups()) for u in lists if GH.match(u)}
    declined = read_declined()
    have |= set(declined)

    def fresh(slug: str) -> bool:
        """Read recently enough that reading it again would only repeat the
        verdict. A candidate already proposed is counted as waiting instead —
        re-reading it every week spent a third of each run's budget on
        repositories that were already on a person's list."""
        past = seen.get(slug)
        return bool(past) and (
            today - dt.date.fromisoformat(past["on"])
        ).days < RECHECK_DAYS

    candidates = [
        (slug, n) for slug, n in cites.most_common() if slug not in have and not fresh(slug)
    ]
    print(
        f"reached {reached}/{len(lists)} lists, {len(cites)} repos cited, "
        f"{len(candidates)} not in the catalog",
        file=sys.stderr,
    )

    shortlist = [slug for slug, _ in candidates[: args.top]]
    print(f"verifying the top {len(shortlist)} by citation count\n", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        results = list(pool.map(inspect, shortlist))
    for result, (slug, n) in zip(results, candidates[: args.top]):
        result["cited_by"] = n

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

    # Proposed before, still neither catalogued nor declined: counted, not
    # re-listed, so the weekly issue shows what is new rather than a wall.
    waiting = [
        slug
        for slug, past in seen.items()
        if past["verdict"] == "calls-jev" and slug not in have
    ]
    new_hits = [
        r for r in results if r["verdict"] == "calls-jev" and r["slug"] not in seen
    ]
    for r in results:
        seen[r["slug"]] = {"verdict": r["verdict"], "on": today.isoformat()}
    if args.seen:
        pathlib.Path(args.seen).parent.mkdir(parents=True, exist_ok=True)
        pathlib.Path(args.seen).write_text(json.dumps(seen, indent=1, sort_keys=True))

    new_lists = find_new_lists(lists) if args.find_lists else []
    if args.markdown:
        pathlib.Path(args.markdown).write_text(
            report_markdown(results, new_hits, waiting, new_lists, reached, len(lists))
        )

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return 0

    by_verdict = collections.Counter(r["verdict"] for r in results)
    for verdict in (
        "calls-jev",
        "mentions-only",
        "no-signal",
        "repo-gone",
        "tree-unavailable",
    ):
        rows = [r for r in results if r["verdict"] == verdict]
        if not rows:
            continue
        print(f"\n=== {verdict} ({len(rows)}) ===")
        for r in rows:
            head = f"  {r['cited_by']:>2} lists  ★{r.get('stars', 0):<7} {r['slug']}"
            print(head)
            if verdict == "calls-jev":
                print(f"          {r['evidence_path']}  -> {r['matched']}")
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
