#!/usr/bin/env python3
"""Refill every generated number and table inside the hand-written docs.

The README was always generated. The docs around it were not, and every one of
them froze at the first build: status.md said 148 entries and listed
`retry-control` as a pattern nobody had published, sources.md warned that
fourteen linked projects had no licence when the real number was 171, and the
site's link-preview text still said 148. None of that was ever wrong on the day
it was written. It became wrong silently, which is worse.

The rule this enforces: a number describing the catalogue may appear only where
something re-derives it. Here that means one of

  * a block — `<!-- name:start -->` … `<!-- name:end -->` — whose whole body is
    generated (a table, a list, a group of meta tags), or
  * an inline value — `<!--n:key-->805<!--/n-->` — inside a hand-written sentence.

Both are invisible once rendered. The prose around them stays hand-written.
lint.py rejects a bare catalogue count anywhere else, so a new stale number
cannot creep back in. Dated history (docs/method.md) is exempt by design: a log
entry saying the first build had 148 entries is true forever.

Run: python3 scripts/build_docs.py
     python3 scripts/build_docs.py --check    # CI: fail if anything is stale
"""

from __future__ import annotations

import argparse
import html
import pathlib
import re
import sys
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _stats  # noqa: E402
from _markers import normalise, replace_block, replace_inline  # noqa: E402

ROOT = _stats.ROOT
SITE = "https://kydlikebtc.github.io/awesome-jev/"
OG_IMAGE = f"{SITE}img/og.png"

LICENCE_LABEL = {
    "unknown": "None declared",
    "NOASSERTION": "NOASSERTION (non-standard terms)",
}


def table(header: list[str], rows: list[list[str]]) -> str:
    out = [
        "| " + " | ".join(header) + " |",
        "|" + "|".join(" --- " for _ in header) + "|",
    ]
    out += [
        "| " + " | ".join(str(c).replace("|", "\\|") for c in row) + " |"
        for row in rows
    ]
    return "\n".join(out)


# ---- status.md -------------------------------------------------------------


def shape_block(s: dict) -> str:
    return table(
        ["", ""],
        [
            ["Entries", s["entries"]],
            ["Carrying code", s["with_code"]],
            ["Official (TypeSafe AI's own)", s["official"]],
            ["Links with a dated 2xx response record", s["link_ok"]],
            ["Most recent successful link-check date (dates vary by row)", s["last_sweep"]],
            ["Rows with call-site text evidence recorded (not a CI pass count)", s["evidence_rows"]],
            ["Patterns covered", f"{s['patterns_covered']} of {s['patterns_total']}"],
            ["Chinese summaries hand-written", f"{s['zh_hand']} of {s['entries']}"],
            ["Retired links", s["retired"]],
        ],
    )


# Editorial commentary on a gap, keyed by the state it describes. A note is
# emitted only while that state holds: "nobody has published one" belongs to
# `empty` and must vanish the day the first example lands. Keying notes by
# pattern alone let that sentence survive into the `thin` list the day
# recommendation got its first entry, contradicting the count printed beside it.
GAP_NOTES = {
    ("recommendation", "empty"): (
        "The vendor lists it as a use case, and nothing has surfaced across every "
        "sibling directory harvested so far. This is a gap in this catalogue, "
        "not proof that no example has been published."
    ),
    ("recommendation", "thin"): (
        "The first example is a movie recommender: retrieval narrows the field, and "
        "Jev parses the request and chooses from the shortlist."
    ),
    ("retry-control", "thin"): (
        "Most apparent matches are false positives: an HTTP client advertising "
        "\"observable retries\" is not a retry decision. The first real one was a "
        "semantic circuit breaker asking whether an HTTP 200 is a silent failure."
    ),
    ("case-study", "empty"): (
        "The catalogue has no case study documenting both cost and observed outcomes."
    ),
}


def gaps_block(s: dict, patterns: list[dict]) -> str:
    counts = s["by_pattern"]
    # Thin is a share, not a count: ten rows meant something at 148 entries and
    # means much less at 800.
    thin_below = s["entries"] * _stats.THIN_SHARE
    empty = [p for p in patterns if counts[p["key"]] == 0]
    thin = sorted(
        (p for p in patterns if 0 < counts[p["key"]] < thin_below and p["key"] != "overview"),
        key=lambda p: counts[p["key"]],
    )
    def note(key: str, state: str, lead: str = " ") -> str:
        text = GAP_NOTES.get((key, state))
        return f"{lead}{text}" if text else ""

    lines = []
    if empty:
        lines += ["No entries yet:", ""]
        lines += [f"- **`{p['key']}`** — {p['blurb_en']}{note(p['key'], 'empty')}" for p in empty]
    else:
        lines.append("Every pattern has at least one entry.")
    if s["empty_kinds"]:
        lines += ["", "Empty kinds:", ""]
        lines += [f"- **`{k}`**.{note(k, 'empty')}" for k in s["empty_kinds"]]
    if thin:
        pct = f"{_stats.THIN_SHARE:.1%}".replace(".0%", "%")
        lines += [
            "",
            f"Thin — under {pct} of the catalogue:",
            "",
        ]
        lines += [
            f"- `{p['key']}` ({counts[p['key']]} of {s['entries']})"
            + note(p["key"], "thin", " — ")
            for p in thin
        ]
    return "\n".join(lines)


# ---- sources.md ------------------------------------------------------------


def sources_block(catalog: list[dict]) -> str:
    counts: Counter = Counter()
    urls: dict[str, set] = {}
    for entry in catalog:
        # A row citing one source twice still counts once for that source.
        for source in {s["catalog"]: s for s in entry["sources"]}.values():
            counts[source["catalog"]] += 1
            urls.setdefault(source["catalog"], set()).add(source["url"])
    rows = [
        [name, f"<{next(iter(urls[name]))}>" if len(urls[name]) == 1 else "various", n]
        for name, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0].lower()))
    ]
    return table(["Source", "URL", "Rows"], rows)


def licences_block(catalog: list[dict]) -> str:
    counts = Counter(e["repo_license"] for e in catalog if e.get("repo_license"))
    rows = [
        [LICENCE_LABEL.get(lic, lic), n]
        for lic, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    ]
    return table(["Licence", "Repositories"], rows)


def row_licences_block(catalog: list[dict]) -> str:
    by = Counter(e["license"] for e in catalog)
    if set(by) == {"CC0-1.0"}:
        return (
            "Every row in the current build is `CC0-1.0`, meaning no descriptive "
            "text was inherited from a source that requires attribution."
        )
    return (
        f"{by.get('CC0-1.0', 0)} rows are `CC0-1.0`; {by.get('CC-BY-4.0', 0)} are "
        "`CC-BY-4.0` because their descriptive text was inherited from a CC BY 4.0 "
        "source, and the attribution is that row's `sources` array."
    )


# ---- site/index.html -------------------------------------------------------


def meta_block(s: dict) -> str:
    """Link-preview tags. og:description is the same sentence as the GitHub
    repository description — both come from _stats.pitch — so a link to the
    site and a link to the repo can no longer describe different catalogues."""
    text = html.escape(_stats.pitch(s), quote=True)
    alt = html.escape(
        "awesome-jev — "
        f"{s['entries']} public resources for TypeSafe AI's Jev, indexed by the "
        "decision each one makes.",
        quote=True,
    )
    tags = [
        f'<meta name="description" content="{text}" />',
        '<meta property="og:title" content="awesome-jev" />',
        f'<meta property="og:description" content="{text}" />',
        '<meta property="og:type" content="website" />',
        f'<meta property="og:url" content="{SITE}" />',
        # Rendered from site/card.html with live data on every deploy, never
        # committed — so the preview image is exactly as current as the site.
        f'<meta property="og:image" content="{OG_IMAGE}" />',
        '<meta property="og:image:width" content="1280" />',
        '<meta property="og:image:height" content="640" />',
        f'<meta property="og:image:alt" content="{alt}" />',
        '<meta name="twitter:card" content="summary_large_image" />',
    ]
    return "\n".join("    " + tag for tag in tags)


# ---- driver ----------------------------------------------------------------


def inline_values(s: dict) -> dict[str, object]:
    return {
        "entries": s["entries"],
        "with_code": s["with_code"],
        "official": s["official"],
        "link_ok": s["link_ok"],
        "link_unstamped": s["link_unstamped"],
        "last_sweep": s["last_sweep"],
        "evidence_rows": s["evidence_rows"],
        "primitive_rows": s["primitive_rows"],
        "primitive_rows_cited": s["primitive_rows_cited"],
        "no_licence": s["no_licence"],
        "platforms": s["platforms"],
        "sibling_lists": s["sibling_lists"],
        "patterns_total": s["patterns_total"],
        "kinds": ", ".join(s["kinds"]),
        "pattern_keys": ", ".join(s["pattern_keys"]),
        "fields": ", ".join(s["fields"]),
    }


def render() -> dict[pathlib.Path, str]:
    catalog, _, patterns, _, _ = _stats.load()
    s = _stats.compute()
    values = inline_values(s)

    blocks = {
        "docs/status.md": {"shape": shape_block(s), "gaps": gaps_block(s, patterns)},
        "docs/sources.md": {
            "sources": sources_block(catalog),
            "licences": licences_block(catalog),
            "row-licences": row_licences_block(catalog),
        },
        "site/index.html": {"meta": meta_block(s)},
        "llms.txt": {},
    }

    out = {}
    for rel, regions in blocks.items():
        path = ROOT / rel
        text = path.read_text()
        for name, body in regions.items():
            text = replace_block(text, name, body, where=rel)
        out[path] = replace_inline(text, values, where=rel)
    return out


def squash(text: str) -> str:
    """Whitespace-insensitive form. A formatter that re-wraps a long HTML
    attribute changes bytes, not data, and must not turn CI red."""
    return re.sub(r"\s+", " ", normalise(text)).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail instead of writing")
    args = parser.parse_args()

    stale = []
    for path, rendered in render().items():
        current = path.read_text()
        if rendered == current or squash(rendered) == squash(current):
            continue
        stale.append(path)
        if not args.check:
            path.write_text(rendered)

    rel = [str(p.relative_to(ROOT)) for p in stale]
    if args.check:
        if stale:
            print(
                "error: generated values are stale in: " + ", ".join(rel) + "\n"
                "Run 'python3 scripts/build_docs.py' and commit the result.",
                file=sys.stderr,
            )
            return 1
        print("generated values in docs, llms.txt and site meta are up to date")
        return 0

    print(("rewrote " + ", ".join(rel)) if stale else "nothing to update")
    return 0


if __name__ == "__main__":
    sys.exit(main())
