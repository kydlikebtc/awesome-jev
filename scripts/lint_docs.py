#!/usr/bin/env python3
"""Keep the hand-written docs from quietly going stale.

scripts/lint.py validates the data. This validates the prose around it, where
every staleness bug in this repository has actually lived: a status page stuck
at 148 entries, a licence warning that said fourteen when the answer was 171, a
link-preview sentence nobody regenerated. Each rule below exists because the
failure it catches already happened once.

Stdlib only, like the rest of scripts/.

Run: python3 scripts/lint_docs.py
"""

from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Fully generated: their numbers are checked by the generator that wrote them.
# docs/by-pattern/ is build_readme.py's output too, one page per pattern.
GENERATED = {"README.md", "README.zh-CN.md"}
GENERATED_DIRS = ("docs/by-pattern/",)


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
MODEL = re.compile(
    r"(?<![\w/.-])~?typesafe(?:-ai)?[/:]jev[-\w.]*"
    r"|(?<![\w/.-])jev-(?:latest|preview|\d+\.\d+(?:\.\d+)*)"
)
LIMIT_RULES = (
    # (what, pattern, how to read the captured numbers)
    ("choice options", re.compile(r"\b(?:max(?:imum)?|up to)\s+(\d{2,})\b|\b(\d{2,})\s+options\b", re.I)),
    ("score levels", re.compile(r"\b(\d+)\s*(?:–|-|to)\s*(\d+)\s+(?:ordered\s+)?levels\b", re.I)),
    ("context", re.compile(r"\b(\d+)k\b(?=\s+(?:tokens|for\b|context))", re.I)),
)


def vendor_facts() -> tuple[set[str], set[str], dict]:
    compat = json.loads((ROOT / "compat.json").read_text())
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


def check_pattern_docs() -> list[str]:
    """docs/patterns.md has one `## key` section per pattern, carrying the
    "when NOT to use this" that no generator can write. A pattern added to
    patterns.json without one would ship with its most important caveat
    missing, and nothing else would notice."""
    keys = [p["key"] for p in json.loads((ROOT / "patterns.json").read_text())["patterns"]]
    heads = set(
        re.findall(r"^## ([a-z]+(?:-[a-z]+)*)\s*$", (ROOT / "docs" / "patterns.md").read_text(), re.M)
    )
    return [
        f"docs/patterns.md: no `## {k}` section for a pattern in patterns.json" for k in keys if k not in heads
    ] + [
        f"docs/patterns.md: `## {h}` is not a pattern in patterns.json" for h in sorted(heads - set(keys))
    ]


CJK = re.compile(r"[\u3400-\u9fff]")
FONT_STACK = re.compile(r"--(mono|sans):\s*([^;]+);")


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
            if "Noto Sans SC" not in m.group(2):
                problems.append(
                    f"{rel}:{line_of(text, m.start())}: --{m.group(1)} has no CJK "
                    "fallback; add \"Noto Sans SC\" (already loaded) to the stack"
                )
    return problems


def check_leading_markers(rel: str, text: str) -> list[str]:
    """CommonMark opens a raw HTML block on any line beginning with `<!--`, so an
    inline value at the start of a line splits its sentence into two
    paragraphs. Prettier then inserts the blank line and makes it visible."""
    return [
        f"{rel}:{n}: line starts with an inline value; put a word before it"
        for n, line in enumerate(text.splitlines(), 1)
        if line.lstrip().startswith("<!--n:")
    ]


def main() -> int:
    problems: list[str] = []
    files = [
        f
        for f in tracked("*.md", "*.txt", "*.html")
        if not generated(f) and not f.startswith(("LICENSE",))
    ]

    for rel in files:
        text = (ROOT / rel).read_text()
        if rel not in HISTORY:
            problems += check_bare_counts(rel, text)
        if rel.endswith((".md", ".txt")):
            problems += check_leading_markers(rel, text)

    # Vendor facts are checked everywhere they are stated, including generated
    # output: the README's primitive table and the SVG figures carry facts that
    # live as constants inside build_readme.py and build_assets.py, so checking
    # what they emit is how those constants get checked.
    facts = vendor_facts()
    fact_files = sorted(
        set(files)
        | {f for f in tracked("*.md") if generated(f)}
        | set(tracked("examples/*.py", "docs/assets/*.svg"))
    )
    for rel in fact_files:
        problems += check_vendor_facts(rel, (ROOT / rel).read_text(), facts)

    problems += check_pattern_docs()
    problems += check_cjk_fallback()

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
