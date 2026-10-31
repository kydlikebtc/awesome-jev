#!/usr/bin/env python3
"""Refill the generated blocks in the practice reviews: docs/practice/ (K1).

docs/patterns.md says what each decision is for and when not to use a decision
model, from the vendor's guidance. A practice review says how the projects in
this catalogue actually do it: how they phrase the questions, which primitive
they pick, which thresholds their files compare answers with, what their
authors measured, and a few call sites worth reading in full.

The prose is written by a model and says so at the top; no person has
reviewed it until the page says otherwise. Every count and list in a page sits
in a generated block this script refills from catalog.json, so the prose never
states a number that drifts:

  readings     the pattern's rows, and who read their cited files
  primitives   per primitive, rows a person or a model read calling it, and
               rows where only the text signal (`primitives_seen`) shows it
  thresholds   every `observed_thresholds` item on the pattern's rows
  measured     the pattern's benchmark measurements and negative results
  read         the rows PAGES names as worth reading, with their cited files

and docs/practice/README.md's `pages` block lists the reviews. A row PAGES
names must stay in the catalogue, filed under the pattern, citing a file
someone has read; otherwise this fails, and the page's prose about it needs a
new pick.

Run: python3 scripts/build_practice.py
     python3 scripts/build_practice.py --check    # CI: fail if anything is stale
"""

from __future__ import annotations

import argparse
import pathlib
import sys
import urllib.parse
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _stats  # noqa: E402
import thresholds  # noqa: E402
from _markers import normalise, replace_block  # noqa: E402
from evidence_url import evidence_url  # noqa: E402
from measurements import measured, negative  # noqa: E402
from platform_values import load_query  # noqa: E402

ROOT = _stats.ROOT
DIR = ROOT / "docs" / "practice"
SITE = "https://kydlikebtc.github.io/awesome-jev/"
PRIMITIVES = _stats.PRIMITIVES

# The reviews written so far, in the order the index lists them, and for each
# the rows whose cited file its prose recommends reading, in the prose's order.
PAGES = {
    "safety-gating": ("jev-engineering", "omp-jevens-classifier", "sub2api-moderation"),
    "tool-selection": ("fastmcp-jev-search", "cua-jev-use", "composio-typesafe-provider"),
    "content-scoring": ("gptcache", "worldmonitor-shadow-mode", "autogpt-typesafe-blocks"),
}


def row_link(entry: dict) -> str:
    return f"[{entry['slug']}]({SITE}?lang=en#{urllib.parse.quote(entry['slug'])})"


def cell(text: object) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def table(header: list[str], rows: list[list[object]], align: str | None = None) -> str:
    out = ["| " + " | ".join(header) + " |", align or "| " + " | ".join("---" for _ in header) + " |"]
    return "\n".join(out + ["| " + " | ".join(cell(c) for c in row) + " |" for row in rows])


def who_read(record: object) -> str:
    found = load_query().reading(record)
    if not found:
        return "nobody yet"
    who, date = found
    return f"a person, {date}" if who == "person" else f"a model, {date}"


def readings_block(rows: list[dict]) -> str:
    query = load_query()
    cited = [e for e in rows if e.get("evidence")]
    by = Counter(query.read_by(e["evidence"]) for e in cited)
    return table(
        ["", "Rows"],
        [
            ["Filed under this pattern", len(rows)],
            ["Citing one file in their repository (`evidence`)", len(cited)],
            ["Of those, the file read by a person (`evidence.read_on`)", by["person"]],
            ["Of those, read only by a model (`evidence.model_read_on`)", by["model"]],
            ["Of those, no reading recorded (a script's match only)", by[None]],
        ],
        "| --- | ---: |",
    )


def primitives_block(rows: list[dict]) -> str:
    layers = _stats.primitive_layers(rows)
    model = [e for e in rows if _stats.primitives_by_model(e)]
    lines = table(
        ["Primitive", "A person read the code calling it", "A model read the code calling it", "Only the text signal shows it"],
        [
            [f"`{name}`", layers[name]["read"], sum(1 for e in model if name in e["question_types"]),
             layers[name]["signal_only"]]
            for name in PRIMITIVES
        ],
        "| --- | ---: | ---: | ---: |",
    )
    combos = Counter(
        " + ".join(f"`{n}`" for n in PRIMITIVES if n in e["question_types"]) for e in rows if e.get("question_types")
    )
    if combos:
        lines += "\n\nPrimitives recorded together on one row (`question_types`, a person's or a model's reading): " + (
            " · ".join(f"{combo} {n}" for combo, n in sorted(combos.items(), key=lambda kv: (-kv[1], kv[0])))
        ) + "."
    return lines


def thresholds_block(rows: list[dict]) -> str:
    found = [
        (item, e)
        for e in thresholds.rows(rows)
        for item in e[thresholds.FIELD]
    ]
    if not found:
        return "None recorded on this pattern's rows."
    found.sort(key=lambda pair: (PRIMITIVES.index(pair[0]["question_type"]), pair[0]["compares"],
                                 -float(pair[0]["value"]), pair[1]["slug"]))
    return table(
        ["Row", "Primitive", "Compares", "Value", "What the file does", "Read by"],
        [
            [row_link(e), f"`{item['question_type']}`", item["compares"], thresholds.number(item["value"]),
             item["decision"], who_read(item)]
            for item, e in found
        ],
    )


def measured_block(rows: list[dict]) -> str:
    shown = {e["slug"]: e for e in measured(rows) + negative(rows)}
    if not shown:
        return "None recorded on this pattern's rows."
    out = []
    negatives = {e["slug"] for e in negative(rows)}
    for slug in sorted(shown):
        e = shown[slug]
        m = e.get("measurement") or {}
        parts = [row_link(e), f"`{e['kind']}`"]
        if m.get("direction"):
            parts.append(f"author's conclusion: {m['direction']}")
        if slug in negatives:
            parts.append("negative result")
        what = m.get("task") or e.get("summary", "")
        out.append(f"- {' · '.join(parts)}: {what.strip()}")
    return "\n".join(out)


def read_block(key: str, picks: tuple[str, ...], catalog: list[dict]) -> str:
    by_slug = {e["slug"]: e for e in catalog}
    out = []
    for n, slug in enumerate(picks, 1):
        e = by_slug.get(slug)
        if e is None:
            raise SystemExit(f"error: docs/practice/{key}.md recommends {slug}, which is not in catalog.json")
        if key not in e["patterns"]:
            raise SystemExit(f"error: docs/practice/{key}.md recommends {slug}, which is not filed under {key}")
        url, path = evidence_url(e), (e.get("evidence") or {}).get("path")
        if not url or not load_query().reading(e["evidence"]):
            raise SystemExit(f"error: docs/practice/{key}.md recommends {slug}, which cites no file anyone has read")
        primitives = ", ".join(f"`{q}`" for q in e.get("question_types") or []) or "none recorded"
        out.append(
            f"{n}. **{row_link(e)}** · `{e['kind']}` · cited file [`{path}`]({url}), read by "
            f"{who_read(e['evidence'])} · primitives: {primitives}"
        )
    return "\n".join(out)


def index_block(patterns: list[dict]) -> str:
    names = {p["key"]: p for p in patterns}
    return "\n".join(
        f"- [{names[key]['en']} · {names[key]['zh']}]({key}.md): {names[key]['blurb_en']} · {names[key]['blurb_zh']}"
        for key in PAGES
    )


def render() -> dict[pathlib.Path, str]:
    catalog, _retired, patterns, _compat, _schema = _stats.load()
    keys = {p["key"] for p in patterns}
    unknown = [key for key in PAGES if key not in keys]
    if unknown:
        raise SystemExit(f"error: PAGES names patterns not in patterns.json: {', '.join(unknown)}")
    pages = {p.stem for p in DIR.glob("*.md") if p.name != "README.md"}
    if pages != set(PAGES):
        raise SystemExit(
            "error: docs/practice/ and build_practice.PAGES disagree: "
            f"pages {sorted(pages)}, PAGES {sorted(PAGES)}"
        )
    out = {}
    for key, picks in PAGES.items():
        rows = [e for e in catalog if key in e["patterns"]]
        path = DIR / f"{key}.md"
        rel = str(path.relative_to(ROOT))
        text = path.read_text(encoding="utf-8")
        for name, body in (
            ("readings", readings_block(rows)),
            ("primitives", primitives_block(rows)),
            ("thresholds", thresholds_block(rows)),
            ("measured", measured_block(rows)),
            ("read", read_block(key, picks, catalog)),
        ):
            text = replace_block(text, name, body, where=rel)
        out[path] = text
    index = DIR / "README.md"
    out[index] = replace_block(index.read_text(encoding="utf-8"), "pages", index_block(patterns),
                               where="docs/practice/README.md")
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true", help="fail instead of writing")
    args = parser.parse_args(argv)
    stale = []
    for path, text in render().items():
        current = path.read_text(encoding="utf-8")
        if text == current or normalise(text) == normalise(current):
            continue
        stale.append(str(path.relative_to(ROOT)))
        if not args.check:
            path.write_text(text, encoding="utf-8")
    if args.check:
        if stale:
            print("error: generated blocks are stale in: " + ", ".join(stale) + "\n"
                  "Run 'python3 scripts/build_practice.py' and commit the result.", file=sys.stderr)
            return 1
        print("the practice reviews' generated blocks are up to date")
        return 0
    print(("rewrote " + ", ".join(stale)) if stale else "nothing to update")
    return 0


if __name__ == "__main__":
    sys.exit(main())
