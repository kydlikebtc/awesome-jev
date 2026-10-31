#!/usr/bin/env python3
"""Keep the hand-written docs from quietly going stale.

scripts/lint.py validates the data. This validates the prose around it, where
every staleness bug in this repository has actually lived: a status page stuck
at 148 entries, a licence warning that said fourteen when the answer was 171, a
link-preview sentence nobody regenerated. Each rule below exists because the
failure it catches already happened once.

Stdlib only, like the rest of scripts/.

Run: python3 scripts/lint_docs.py
     python3 scripts/lint_docs.py --simulate-model jev-1.14.0
         # release rehearsal: what would go red if compat.json moved to that
         # version today; writes nothing
"""

from __future__ import annotations

import argparse
import copy
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from _github import VERSION, version_parts, version_stem  # noqa: E402

# Fully generated: their numbers are checked by the generator that wrote them.
# docs/by-pattern/ is build_readme.py's output too, one page per pattern, and so
# are docs/measured.md and docs/measured.zh-CN.md, every independent report;
# docs/review-queue.md is build_review_queue.py's and docs/zh-queue.md zh_audit.py's;
# docs/benchmarks.md and docs/benchmarks.zh-CN.md are build_benchmarks.py's, every
# benchmark row's measurement; examples/index.json is build_examples_index.py's,
# a copy of the examples' code; docs/shape.md and docs/shape.zh-CN.md are
# build_shape.py's, the catalogue's shape as a dataset.
GENERATED = {
    "README.md", "README.zh-CN.md", "docs/measured.md", "docs/measured.zh-CN.md", "docs/review-queue.md",
    "docs/benchmarks.md", "docs/benchmarks.zh-CN.md", "docs/zh-queue.md", "examples/index.json",
    "docs/shape.md", "docs/shape.zh-CN.md",
}
# docs/monthly/ is build_monthly.py's: each month's report, its figures taken
# from history/ snapshots and written once, so they stay that month's.
GENERATED_DIRS = ("docs/by-pattern/", "docs/monthly/")
# Generated pages that quote other people's files verbatim: the review queue
# prints each row's `evidence.matched`, which is whatever text a project's code
# contains (`jev-1.13` inside a `jev-1.13.0`, say). Those are quotations, not
# this repository stating a model string, so vendor facts are not checked there.
QUOTES_UPSTREAM = {"docs/review-queue.md"}


def generated(rel: str) -> bool:
    return rel in GENERATED or rel.startswith(GENERATED_DIRS)
# Dated logs. "The first build had 148 entries" is true forever, and rewriting it
# to today's number would falsify the history rather than update it.
HISTORY = {"docs/method.md"}

BLOCK = re.compile(r"<!-- ([a-z-]+):start -->.*?<!-- \1:end -->", re.S)
INLINE = re.compile(r"<!--n:[a-z_]+-->.*?<!--/n-->", re.S)

# A number followed by a noun that only ever describes this catalogue. Kept
# deliberately narrow: "the top 40", "2–10 levels" or "52 of its files" are not
# catalogue counts, and a rule that cries wolf is a rule people learn to bypass.
WORDS = (
    "one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|"
    "fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|"
    "fifty|sixty|seventy|eighty|ninety|hundred"
)
NOUNS = r"(?:verified\s+)?(?:entries|examples|rows|linked\s+projects|repositories|call\s+sites)\b"
BARE_COUNT = re.compile(
    # 805 entries · 1,887 repositories · Fourteen linked projects
    rf"(?<![\w.#/-])(?:\d{{1,3}}(?:,\d{{3}})+|\d+|(?:{WORDS})(?:[- ](?:{WORDS}))*)\s+{NOUNS}"
    # 805 条目
    r"|(?<![\w.#/-])\d+\s*(?:条目|个条目|个例子|个项目|个仓库)",
    re.I,
)
# `document-triage` (1) — a per-pattern count written by hand.
PATTERN_COUNT = re.compile(r"`[a-z]+(?:-[a-z]+)*`\s*\(\d+\)")
# Coverage prose can freeze even when the figure beside it is generated. The
# original README kept "Two patterns have no examples" after every pattern was
# populated. Keep such catalogue claims inside generated coverage blocks.
PATTERN_GAP_COUNT = re.compile(
    rf"\b(?:\d+|{WORDS})\s+patterns?\s+(?:have|has)\s+no\s+(?:examples|entries)\b"
    r"|(?:\d+|[零一二两三四五六七八九十]+)\s*个模式(?:目前|尚)?(?:没有|未收录|无)(?:例子|条目)?",
    re.I,
)
# A table whose header announces counts, or whose first column is a stat label.
COUNT_HEADER = re.compile(r"^(rows|repositories|entries|count|examples|条目)$", re.I)
STAT_LABEL = re.compile(
    r"^(entries|carrying code|with code|official.*|patterns covered|retired.*|link.*verified.*)$",
    re.I,
)


# A range of probabilities or confidences typed into prose: "0.3 to 0.9",
# "0.55–0.8", "0.3 到 0.9". SKILL.md and examples/README.md once said a
# catalogued system's thresholds ranged "from 0.3 to 0.9", copied by hand from
# one row's notes, and nothing would have noticed the row change. The ranges
# come from observed_thresholds now, as build_docs.py inline values. Narrow:
# two decimals at most 1 with a range word between them, a full stop after
# the second allowed. A version (1.13) or a level scale (2–10) does not match.
DECIMAL_RANGE = re.compile(
    r"(?<![\w.])(?:0?\.\d+|1\.0+)\s*(?:to|–|—|-|~|到|至)\s*(?:0?\.\d+|1(?:\.0+)?)(?!\w|\.\d)",
    re.I,
)


def check_decimal_ranges(rel: str, text: str) -> list[str]:
    """A typed range of thresholds outside a generated marker is a number nothing re-derives."""
    masked = BLOCK.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)
    masked = INLINE.sub(lambda m: " " * len(m.group(0)), masked)
    return [
        f"{rel}:{line_of(masked, m.start())}: typed decimal range {m.group(0)!r} — state the thresholds "
        "catalogued files use as <!--n:threshold_…--> inline values (scripts/build_docs.py), or reword it"
        for m in DECIMAL_RANGE.finditer(masked)
    ]


def tracked(*patterns: str) -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", *patterns],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return [line for line in out.stdout.splitlines() if line]


def line_of(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def check_bare_counts(rel: str, text: str) -> list[str]:
    """A catalogue count outside a generated marker is a number nothing updates."""
    # Blank the generated regions but keep their newlines, so line numbers in
    # the report still point at the real line.
    masked = BLOCK.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)
    masked = INLINE.sub(lambda m: " " * len(m.group(0)), masked)
    hint = "wrap it in <!--n:key-->…<!--/n--> (see scripts/build_docs.py) or reword it"
    found = [
        f"{rel}:{line_of(masked, m.start())}: bare catalogue count {m.group(0).strip()!r} — {hint}"
        for rx in (BARE_COUNT, PATTERN_COUNT, PATTERN_GAP_COUNT)
        for m in rx.finditer(masked)
    ]
    return found + check_count_tables(rel, masked)


def check_count_tables(rel: str, masked: str) -> list[str]:
    """Hand-written tables are where status.md and sources.md froze: `| Entries |
    148 |` puts the number after the noun, so the prose rule never sees it."""
    found = []
    header: list[str] | None = None
    for n, line in enumerate(masked.splitlines(), 1):
        row = line.strip()
        if not (row.startswith("|") and row.endswith("|")):
            header = None
            continue
        cells = [c.strip() for c in row.strip("|").split("|")]
        if all(set(c) <= set("-: ") for c in cells):
            continue  # separator row
        if header is None:
            header = cells
            continue
        numeric = [i for i, c in enumerate(cells) if re.fullmatch(r"[\d,]+( of \d+)?", c)]
        counted = any(COUNT_HEADER.match(header[i]) for i in numeric if i < len(header))
        labelled = numeric and STAT_LABEL.match(cells[0])
        if counted or labelled:
            found.append(
                f"{rel}:{n}: hand-written count in a table — generate the table "
                "between <!-- name:start --> / <!-- name:end --> markers instead"
            )
    return found


# ---- vendor facts ------------------------------------------------------------
#
# Model strings and limits change when the vendor ships, not when the catalogue
# grows. compat.json is their one source; everything else that states them is a
# copy, and is held to it here. When jev-1.13.0 is superseded and compat.json is
# updated, every doc still naming the old version goes red on the same push.

# Narrow on purpose. A bare version must carry a dot — `jev-1.13.0` is how a
# real version drift looks — because `jev-2048` is a catalogued project's name,
# not a model. And `typesafe/jev…` preceded by a slash is a URL path
# (github.com/typesafe-ai/jev-…), not a model string.
#
# ASCII classes on purpose, not \w: Python's \w matches Chinese characters, so
# `模型jev-1.13` would have hidden the model string behind its neighbour and
# `typesafe/jev模型` would have swallowed the neighbour into it. Chinese prose
# needs no space before a model string, and the Chinese pages are held to
# compat.json like the English ones.
MODEL = re.compile(
    r"(?<![A-Za-z0-9_/.-])~?typesafe(?:-ai)?[/:]jev[-A-Za-z0-9_.]*"
    r"|(?<![A-Za-z0-9_/.-])jev-(?:latest|preview|\d+\.\d+(?:\.\d+)*)"
)
LIMIT_RULES = (
    # (what, pattern, how to read the captured numbers)
    ("choice options", re.compile(r"\b(?:max(?:imum)?|up to)\s+(\d{2,})\b|\b(\d{2,})\s+options\b", re.I)),
    ("score levels", re.compile(r"\b(\d+)\s*(?:–|-|to)\s*(\d+)\s+(?:ordered\s+)?levels\b", re.I)),
    ("context", re.compile(r"\b(\d+)k\b(?=\s+(?:tokens|for\b|context))", re.I)),
    # The same limits as the Chinese pages write them: 最多 255 个选项,
    # 2–10 级 (or 个有序级别), 64k token / 64k 上下文. Narrow like the English
    # rules: a bare 最多 16 (a project's own batch size) is not a choice limit.
    ("choice options", re.compile(r"(?<![\d.])(\d{2,})\s*个选项")),
    ("score levels", re.compile(r"(?<![\d.])(\d+)\s*(?:–|-|到|至)\s*(\d+)\s*个?(?:有序)?(?:等级|级)")),
    ("context", re.compile(r"(?<![\d.])(\d+)k(?=\s*(?:token\b|上下文|的上下文))", re.I)),
)


def load_compat() -> dict:
    return json.loads((ROOT / "compat.json").read_text())


def vendor_facts(compat: dict | None = None) -> tuple[set[str], set[str], dict]:
    compat = load_compat() if compat is None else compat
    canonical = {
        re.sub(r"\s*\(.*\)$", "", part.strip())
        for platform in compat["platforms"]
        for part in platform["model"].split("·")
        if part.strip() not in ("", "—")
    }
    refuted = {item["s"] for item in compat.get("not_model_strings", [])}
    limits = {item["k"]: item["n"] for item in compat["limits"] if "n" in item}
    return canonical, refuted, limits


def check_vendor_facts(rel: str, text: str, facts: tuple) -> list[str]:
    canonical, refuted, limits = facts
    found = []
    for m in MODEL.finditer(text):
        token = m.group(0).rstrip(".")
        if token not in canonical and token not in refuted:
            found.append(
                f"{rel}:{line_of(text, m.start())}: model string {token!r} is not in "
                "compat.json — fix the doc, or add it there (or to not_model_strings "
                "if the doc is refuting it)"
            )
    choice_max = limits["choice options"]["max"]
    levels = (limits["score levels"]["min"], limits["score levels"]["max"])
    context = {limits["context"]["request_k"], limits["context"]["state_k"]}
    for what, rx in LIMIT_RULES:
        for m in rx.finditer(text):
            nums = tuple(int(g) for g in m.groups() if g)
            ok = (
                (what == "choice options" and nums == (choice_max,))
                or (what == "score levels" and nums == levels)
                or (what == "context" and set(nums) <= context)
            )
            if not ok:
                found.append(
                    f"{rel}:{line_of(text, m.start())}: {m.group(0)!r} disagrees with "
                    f"compat.json's {what} limit"
                )
    return found


# A link to a page whose address names a model version — the vendor's known
# limitations page, docs.typesafe.ai/model-jaggedness/ and then the version —
# states a vendor fact too: that this is the current model's page. MODEL
# cannot see it (a model string after a slash is a URL path), so it went stale
# unchecked. compat.json records such pages in a platform's `docs_url`, and a
# hand-written file may link only those. The generated READMEs and pattern
# pages are not held to it: their links are catalogue rows, each the record of
# one document, which is lint.py's business, and a row about one version's
# page stays true after the next ships.
VERSIONED_URL = re.compile(r"""https?://[^\s<>()\[\]{}"'`|]*?(?<![\w.-])jev-\d+\.\d+[^\s<>()\[\]{}"'`|]*""")


def docs_urls(compat: dict) -> set[str]:
    """Every versioned page compat.json records (`docs_url`, a string or a list)."""
    out: set[str] = set()
    for platform in compat.get("platforms", []):
        urls = platform.get("docs_url") or []
        out.update([urls] if isinstance(urls, str) else urls)
    return out


# Marker blocks whose links cite files in catalogued projects' repositories,
# as a README row does: docs/compatibility.md's `alternatives` table, generated
# from catalog.json's `wire` records (scripts/wire.py). A path there that names
# a model version is a project's own file, not a vendor page.
CATALOGUE_BLOCKS = ("alternatives",)


def without_catalogue_blocks(text: str) -> str:
    """`text` with the CATALOGUE_BLOCKS blanked, newlines kept for line numbers."""
    for name in CATALOGUE_BLOCKS:
        block = re.compile(rf"<!-- {name}:start -->.*?<!-- {name}:end -->", re.S)
        text = block.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)
    return text


def check_versioned_urls(rel: str, text: str, allowed: set[str]) -> list[str]:
    found = []
    text = without_catalogue_blocks(text)
    for m in VERSIONED_URL.finditer(text):
        url = m.group(0).rstrip(".,;:")
        # A heading on a recorded page (picker.json cites #generation) is that page.
        if url.split("#", 1)[0].rstrip("/") not in {u.rstrip("/") for u in allowed}:
            found.append(
                f"{rel}:{line_of(text, m.start())}: links {url!r}, a page for one model version "
                "that no docs_url in compat.json records — link the current version's page, or "
                "record the page there"
            )
    return found


# compat.json's own prose restates model strings too (a `why` names
# OpenRouter's versioned string), and the MCP server hands its `why` lines to
# agents. A release edits the model cells; these are held to them like any
# other copy.
COMPAT_PROSE = ("notes", "notes_zh", "why", "why_zh")


def check_compat_prose(compat: dict, facts: tuple, raw: str) -> list[str]:
    found = []
    for section in ("platforms", "limits", "not_model_strings"):
        for item in compat.get(section, []):
            name = item.get("id") or item.get("k") or item.get("s") or "?"
            for key in COMPAT_PROSE:
                text = item.get(key)
                if not isinstance(text, str):
                    continue
                at = raw.find(json.dumps(text, ensure_ascii=False)[1:-1])
                where = f"compat.json:{line_of(raw, at) if at >= 0 else 1}: {section} {name!r} {key}:"
                # check_vendor_facts numbers lines inside the string; the
                # string's own line in compat.json is the useful one.
                found += [
                    re.sub(r"^compat\.json:\d+:", where, problem)
                    for problem in check_vendor_facts("compat.json", text, facts)
                ]
    return found


# The pages that define each pattern: the English page, and its Chinese
# rendering, which a model wrote from it and which says the English governs.
# Both are held to every pattern in patterns.json.
PATTERN_DOCS = ("docs/patterns.md", "docs/patterns.zh-CN.md")
PATTERN_HEAD = re.compile(r"^## ([a-z]+(?:-[a-z]+)*)\s*$", re.M)


def pattern_sections(text: str) -> dict[str, str]:
    """Each `## key` heading's section: its text up to the next `## ` heading."""
    heads = list(PATTERN_HEAD.finditer(text))
    out = {}
    for m in heads:
        rest = text[m.end():]
        following = re.search(r"^## ", rest, re.M)
        out[m.group(1)] = rest[: following.start()] if following else rest
    return out


def check_pattern_docs(texts: dict[str, str] | None = None, keys: list[str] | None = None) -> list[str]:
    """docs/patterns.md has one `## key` section per pattern, carrying the
    "when NOT to use this" that no generator can write. A pattern added to
    patterns.json without one would ship with its most important caveat
    missing, and nothing else would notice. Each section ends with its
    `catalogued-<key>` markers, which build_docs.py fills with the count and
    the links to the pattern's page and the site: markers moved into another
    section would put one pattern's count under another's heading.

    `texts` stands in for the pages' contents and `keys` for patterns.json's
    (tests)."""
    if keys is None:
        keys = [p["key"] for p in json.loads((ROOT / "patterns.json").read_text())["patterns"]]
    problems = []
    for rel in PATTERN_DOCS:
        text = (texts or {}).get(rel)
        if text is None:
            path = ROOT / rel
            if not path.exists():
                problems.append(f"{rel}: missing; it defines every pattern in patterns.json")
                continue
            text = path.read_text()
        sections = pattern_sections(text)
        problems += [f"{rel}: no `## {k}` section for a pattern in patterns.json" for k in keys if k not in sections]
        problems += [f"{rel}: `## {h}` is not a pattern in patterns.json" for h in sorted(set(sections) - set(keys))]
        problems += [
            f"{rel}: the `## {k}` section has no <!-- catalogued-{k}:start --> / <!-- catalogued-{k}:end --> "
            "markers for build_docs.py to fill"
            for k in keys
            if k in sections
            and not (f"<!-- catalogued-{k}:start -->" in sections[k] and f"<!-- catalogued-{k}:end -->" in sections[k])
        ]
    return problems


CJK = re.compile(r"[\u3400-\u9fff]")
FONT_STACK = re.compile(r"--(mono|sans):\s*([^;]+);")
# The system CJK fonts every stack on a page that shows Chinese names: Apple's
# two, Windows', and Noto Sans CJK SC for Linux and Android, which the Pages
# deploy installs (fonts-noto-cjk) before it renders the README screenshots.
# The site loads no Chinese web font (site/fonts/fonts.css says why), and the
# README cover's SVGs name the same four (build_readme_cover.py).
CJK_FAMILIES = ("PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC")


def check_cjk_fallback() -> list[str]:
    """A page that shows Chinese needs a CJK font in every stack it draws text
    with. IBM Plex has no CJK glyphs; a Mac falls back to a system font
    silently, while a machine with none — stock Linux, and the CI runner that
    renders the README screenshots — draws empty boxes. The screenshots shipped
    that way once, which is how this was found."""
    problems = []
    for rel in tracked("site/*.html"):
        text = (ROOT / rel).read_text()
        if not CJK.search(text):
            continue
        for m in FONT_STACK.finditer(text):
            missing = [family for family in CJK_FAMILIES if f'"{family}"' not in m.group(2)]
            if missing:
                problems.append(
                    f"{rel}:{line_of(text, m.start())}: --{m.group(1)} has no CJK fallback for "
                    f"{', '.join(missing)}; name every system font in lint_docs.CJK_FAMILIES"
                )
    return problems


# A tag or rule that loads something from another host. Since 2026-10-24 the
# site loads nothing from one: its fonts came from fonts.googleapis.com until
# then, a render-blocking stylesheet on a host most readers in mainland China
# cannot reach, so a page could stay blank until the request timed out. A link
# a reader follows to another site is fine; a stylesheet, script, font, image,
# frame, preconnect or fetch from one is not.
LOADS = "stylesheet|preload|modulepreload|preconnect|dns-prefetch|icon"
FOREIGN_LOAD = re.compile(
    rf'<link\b[^>]*\brel="(?:{LOADS})"[^>]*\bhref="(?:https?:)?//'
    rf'|<link\b[^>]*\bhref="(?:https?:)?//[^"]*"[^>]*\brel="(?:{LOADS})"'
    r'|<(?:script|img|iframe|source|video|audio|embed)\b[^>]*\bsrc="(?:https?:)?//'
    r"|@import\s+(?:url\()?[\"']?(?:https?:)?//"
    r"|url\(\s*[\"']?(?:https?:)?//"
    r"|\bfetch\(\s*[\"'`](?:https?:)?//",
    re.I,
)


def check_site_origin() -> list[str]:
    """Every page, stylesheet and script under site/ loads only from the site."""
    return [
        f"{rel}:{line_of(text, m.start())}: loads from another host ({' '.join(m.group(0).split())[:70]}); "
        "serve the file from site/ instead"
        for rel in tracked("site/*.html", "site/*.css", "site/*.mjs", "site/*.js")
        for text in [(ROOT / rel).read_text()]
        for m in FOREIGN_LOAD.finditer(text)
    ]


def check_leading_markers(rel: str, text: str) -> list[str]:
    """CommonMark opens a raw HTML block on any line beginning with `<!--`, so an
    inline value at the start of a line splits its sentence into two
    paragraphs. Prettier then inserts the blank line and makes it visible."""
    return [
        f"{rel}:{n}: line starts with an inline value; put a word before it"
        for n, line in enumerate(text.splitlines(), 1)
        # A blockquote's lines count too: `> <!--n:` opens the block there.
        if line.lstrip(" \t>").startswith("<!--n:")
    ]


# Vendor facts are checked everywhere they are stated, including generated
# output: the READMEs and the SVG figures carry facts that live as strings and
# constants in scripts/readme/ and build_assets.py, so checking what they emit
# is how those constants get checked. Since 2026-09-27 also the MCP server's
# source, whose strings reach every agent that asks it, the Claude Code plugin
# manifests, and the issue forms, which link the vendor's pages. Since
# 2026-09-28 also the hand-written prose the site and the MCP server serve
# from JSON — the curated collections' reasons and cautions, the pattern and
# label blurbs, the entry schema's field descriptions — and the site's
# script module; none states a vendor fact today, and this keeps it so. Also
# watch.json, whose dated readings of the vendor's pages the status page shows.
EXTRA_FACT_FILES = (
    "examples/*.py", "docs/assets/*.svg", "src/**/*.py", ".claude-plugin/**", ".github/ISSUE_TEMPLATE/*",
    "collections.json", "patterns.json", "taxonomy.json", "schema/*.json", "site/*.mjs", "watch.json",
    "picker.json",
)


def hand_written_files() -> list[str]:
    return [
        f
        for f in tracked("*.md", "*.txt", "*.html")
        # A licence is not prose this repository wrote, at the root or beside
        # the fonts it covers (site/fonts/LICENSE.txt).
        if not generated(f) and not pathlib.PurePosixPath(f).name.startswith("LICENSE")
    ]


def fact_file_list(files: list[str]) -> list[str]:
    return sorted(
        (set(files) | {f for f in tracked("*.md") if generated(f)} | set(tracked(*EXTRA_FACT_FILES)))
        - QUOTES_UPSTREAM
    )


def vendor_problems(compat: dict, fact_files: list[str], texts: dict[str, str] | None = None) -> list[str]:
    """Every copy of a vendor fact that disagrees with `compat`. `texts`
    stands in for a file's contents (the rehearsal's regenerated page)."""
    facts, allowed = vendor_facts(compat), docs_urls(compat)
    problems: list[str] = []
    for rel in fact_files:
        text = (texts or {}).get(rel)
        text = (ROOT / rel).read_text() if text is None else text
        problems += check_vendor_facts(rel, text, facts)
        if not generated(rel):
            problems += check_versioned_urls(rel, text, allowed)
    return problems + check_compat_prose(compat, facts, (ROOT / "compat.json").read_text())


# ---- release rehearsal ----------------------------------------------------
#
# `--simulate-model jev-1.14.0` answers "what does a release cost us?" before
# the day: it builds the compat.json a maintainer would write — every model
# name and docs_url naming the newest version recorded now names the new one,
# at the precision it was written in — and runs this file's checks against it,
# with docs/compatibility.md regenerated from it. Nothing is written. What it
# prints is the list of places to change, what follows compat.json on its own,
# and what the catalogue and the weekly claims run will do afterwards.


def simulated_compat(compat: dict, model: str) -> tuple[dict, str]:
    """(compat.json as it would read with `model` in place of the newest
    version it records, that version's major.minor)."""
    if not VERSION.fullmatch(model):
        raise SystemExit(f"error: --simulate-model wants a versioned model id such as jev-1.14.0, not {model!r}")
    recorded = {
        version_stem(token) for platform in compat["platforms"] for token in VERSION.findall(platform.get("model") or "")
    }
    if not recorded:
        raise SystemExit("error: compat.json records no versioned model id to move from")
    old = max(recorded, key=version_parts)
    new = version_parts(model)
    if version_parts(version_stem(model)) <= version_parts(old):
        raise SystemExit(f"error: {model} is not newer than {old}, the newest version compat.json records")

    def move(text: str) -> str:
        def one(match: re.Match) -> str:
            token = match.group(0)
            if version_stem(token) != old:
                return token
            width = len(version_parts(token))
            return "jev-" + ".".join(str(n) for n in (new + (0,) * width)[:width])

        return VERSION.sub(one, text)

    out = copy.deepcopy(compat)
    for platform in out["platforms"]:
        platform["model"] = move(platform["model"])
        urls = platform.get("docs_url")
        if isinstance(urls, str):
            platform["docs_url"] = move(urls)
        elif urls:
            platform["docs_url"] = [move(url) for url in urls]
    return out, old


def catalogue_rehearsal(catalog: list[dict], old: str, now: tuple, then: tuple) -> list[str]:
    """What the catalogue does when the version moves: nothing turns red from
    evidence, but text that reaches the generated pages does."""
    def pins(entry: dict) -> bool:
        matched = (entry.get("evidence") or {}).get("matched") or []
        return any(version_stem(t) == old for s in matched for t in VERSION.findall(s))

    pinned = [e["slug"] for e in catalog if pins(e)]
    worded = sorted(
        e["slug"]
        for e in catalog
        for key in ("title", "summary", "summary_zh")
        if isinstance(e.get(key), str) and check_vendor_facts(key, e[key], then) and not check_vendor_facts(key, e[key], now)
    )
    linked = [e["slug"] for e in catalog if any(version_stem(t) == old for t in VERSION.findall(e.get("url") or ""))]
    lines = [
        f"- {len(pinned)} row(s) quote {old} in evidence.matched. None turns red: as each project moves "
        "its pin, the weekly claims run reports the row as version-moved, counted per version, and "
        "`python3 scripts/verify_claims.py --propose-version-rewrite` prints the rewritten strings "
        "for a person to apply, read_on unchanged.",
    ]
    if worded:
        lines.append(
            f"- {len(set(worded))} row(s) name {old} in a title or summary, which the READMEs and "
            f"pattern pages print, so those pages are among the red files above: {', '.join(sorted(set(worded)))}. "
            "Either compat.json keeps the old version while the vendor still serves it, or each row is reworded "
            "by a person (a measurement made on the old version stays true; say so in words)."
        )
    if linked:
        lines.append(
            f"- {len(linked)} row(s) link a page for {old}: {', '.join(linked)}. A row about that page stays true; "
            "decide whether the README's Start here list should point at the new version's page instead."
        )
    return lines


def unchecked_copies(old: str, checked: set[str]) -> list[str]:
    """Tracked text files naming the old version that no rule here reads.
    Tests are left out (their fixtures are literal on purpose, and check.py
    runs them), and so are the data files the rehearsal already covers."""
    skip = checked | {"catalog.json", "retired.json", "compat.json"} | HISTORY
    out = []
    for rel in tracked():
        if rel in skip or generated(rel) or rel.startswith(("tests/", "scripts/tests/")):
            continue
        try:
            text = (ROOT / rel).read_text()
        except (UnicodeDecodeError, IsADirectoryError, FileNotFoundError):
            continue
        hits = [n for n, line in enumerate(text.splitlines(), 1) if any(version_stem(t) == old for t in VERSION.findall(line))]
        if hits:
            out.append(f"  {rel}: line {', '.join(map(str, hits))}")
    return out


def rehearse(model: str, fact_files: list[str]) -> int:
    import build_compat  # noqa: PLC0415 - only the rehearsal regenerates a page

    compat = load_compat()
    then, old = simulated_compat(compat, model)
    new = version_stem(model)
    texts = {"docs/compatibility.md": build_compat.build(then)}
    before = set(vendor_problems(compat, fact_files))
    red = [p for p in vendor_problems(then, fact_files, texts) if p not in before]
    files = sorted({p.split(":", 1)[0] for p in red})
    catalog = json.loads((ROOT / "catalog.json").read_text())
    print(f"Release rehearsal: compat.json with {model} in place of {old} (nothing is written).\n")
    moved = [f"{p['id']}: {p['model']}" for p in then["platforms"] if p["model"] != next(
        q["model"] for q in compat["platforms"] if q["id"] == p["id"])]
    print("compat.json would read:")
    for line in moved:
        print(f"  {line}")
    for platform in then["platforms"]:
        if platform.get("docs_url"):
            print(f"  {platform['id']} docs_url: {platform['docs_url']}")
    print(f"\nWould fail lint_docs: {len(red)} problem(s) in {len(files)} file(s). Each is a copy to edit:")
    for rel in files:
        # A generated page is never edited: its text comes from catalogue rows
        # (named under "The catalogue" below) or from its generator.
        source = "  (generated: fix its source, not this file)" if generated(rel) else ""
        print(f"  {rel}{source}")
        for problem in red:
            where, _, what = problem.partition(": ")
            if where.split(":", 1)[0] == rel:
                # The finding without its how-to-fix tail, which the real run prints.
                print(f"    line {where.split(':', 1)[1]}: {what.split(' — ', 1)[0]}")
    print(
        "\nThese follow compat.json, nothing to edit: the model names verify_claims.py and "
        f"discover_candidates.py look for (then {', '.join(_listed(then))}; {old} still counts as a "
        "pinned version), the MCP server's check_model_string hint, docs/compatibility.md's tables "
        "and its as_of line (regenerated), and the site's compatibility view."
    )
    print("\nThe catalogue:")
    for line in catalogue_rehearsal(catalog, old, vendor_facts(compat), vendor_facts(then)):
        print(line)
    others = unchecked_copies(old, set(fact_files))
    if others:
        print(f"\nNo rule reads these tracked files, which name {old} (mostly examples in comments; a value "
              "a script uses belongs in compat.json):")
        for line in others:
            print(line)
    print(
        f"\nOn the day: read each platform's page, edit compat.json (model cells, docs_url, the prose "
        f"above, as_of to that day), fix the files listed, run python3 scripts/check.py. {new} is then current."
    )
    return 0


def _listed(compat: dict) -> tuple[str, ...]:
    from _github import version_signals  # noqa: PLC0415

    return version_signals(compat)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--simulate-model",
        metavar="MODEL",
        help="release rehearsal: report what would go red if compat.json moved to MODEL (e.g. jev-1.14.0); writes nothing",
    )
    args = parser.parse_args(argv)
    files = hand_written_files()
    fact_files = fact_file_list(files)
    if args.simulate_model:
        return rehearse(args.simulate_model, fact_files)

    problems: list[str] = []
    for rel in files:
        text = (ROOT / rel).read_text()
        if rel not in HISTORY:
            problems += check_bare_counts(rel, text)
            if rel.endswith((".md", ".txt")):
                problems += check_decimal_ranges(rel, text)
        if rel.endswith((".md", ".txt")):
            problems += check_leading_markers(rel, text)

    problems += vendor_problems(load_compat(), fact_files)
    problems += check_pattern_docs()
    problems += check_cjk_fallback()
    problems += check_site_origin()

    for problem in problems:
        print(f"error: {problem}", file=sys.stderr)
    if problems:
        print(f"\n{len(problems)} problem(s) in hand-written docs", file=sys.stderr)
        return 1
    print(
        f"checked {len(files)} hand-written files for stale numbers and "
        f"{len(fact_files)} files for vendor facts against compat.json"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
