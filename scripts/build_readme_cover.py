#!/usr/bin/env python3
"""Generate the README hero: a theme-aware launch-board card and its phone layout.

GitHub picks the light or dark file through the README <picture>, so each
theme is drawn for its own canvas rather than one poster serving both. Counts
come from _stats.compute() and describe saved records, never runtime test
passes. The feed on the right is the board as it stands (readme.board.hero:
the week running, the week filed next, last week's top three, or the rising
products), read from the files the README's first section reads, so the cover
and the section change together. The SVGs are portable: system fonts only,
and no external fonts, images, scripts or foreign objects, none of which an
SVG shown as <img> may load anyway.

Text is placed from conservative advance-width estimates. Copy and counts
fail the build when they would overrun their column; a product's title or
line, which nobody here chose, is clipped to its card instead, so a long name
can never stop the Monday run that regenerates this cover. Fonts differ by
platform, so a layout that merely fits on the author's machine proves nothing.

Run: python3 scripts/build_readme_cover.py [--check]
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import unicodedata
from html import escape
from pathlib import Path

from _stats import compute

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "assets"
WIDTH, HEIGHT = 1200, 440
MOBILE_WIDTH, MOBILE_HEIGHT = 600, 560
# GitHub's own md breakpoint; below it the desktop card's labels drop under 11px.
HERO_BREAKPOINT = 768
SANS = (
    "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,"
    "'PingFang SC','Hiragino Sans GB','Microsoft YaHei','Noto Sans CJK SC',sans-serif"
)
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"
# The favicon: source evidence, context and a decision as three bars on ink.
MARK_INK = "#0b0d10"
MARK_BARS = ((7, 20, 6, "#4ec97a"), (13.5, 14, 12, "#a9b3c0"), (20, 8, 18, "#f5a524"))
# Primer colours, as in the other README figures, under the brand accents.
# `tiers` colours a card's evidence bar: a person read the call site, a model
# did, or only a script matched text (or nothing is cited).
THEMES = {
    "light": {
        "canvas": "#f6f8fa", "panel": "#ffffff", "fg": "#1f2328", "muted": "#59636e",
        "faint": "#656d76", "rule": "#d1d9e0", "grid": "#1f2328", "grid_opacity": ".05",
        "accent": "#a15c00", "joint": "#e59a1a", "tiers": {"person": "#1a7f37", "model": "#6e7781", "file": "#a15c00"},
        "mark_edge": MARK_INK,
    },
    "dark": {
        "canvas": "#0b0d10", "panel": "#121821", "fg": "#e6edf3", "muted": "#9198a1",
        "faint": "#8b949e", "rule": "#30363d", "grid": "#ffffff", "grid_opacity": ".045",
        "accent": "#f5a524", "joint": "#f5a524", "tiers": {"person": "#4ec97a", "model": "#a9b3c0", "file": "#f5a524"},
        # The ink tile would vanish into an ink canvas without an edge.
        "mark_edge": "#3d444d",
    },
}
COPY = {
    "en": {
        "eyebrow": "weekly launch board",
        "title": "Jev Launches",
        "lede": ("Products built on Jev, launched weekly.", "Vote, then read the evidence."),
        "labels": ("products", "makers", "call-site records"),
    },
    "zh": {
        "eyebrow": "每周发布榜",
        "title": "Jev 发布榜",
        "lede": ("用 Jev 做的产品，每周发布一次。", "投票之后，再看证据。"),
        "labels": ("产品", "Maker", "调用点记录"),
    },
}
METRICS = ("products", "makers", "call_site_rows")
# How many cards the feed draws (readme.board.HERO_CARDS hands over as many).
CARDS = 3
VOTE, STAR = "▲", "★"
# Advance widths in em. Measured against SF, Helvetica, Arial and Menlo, and
# against Verdana standing in for DejaVu Sans, the widest common Linux
# fallback: every line on the current covers fits under all of them. BOLD
# widens sans text drawn at weight 600 or more.
NARROW = frozenset(" .,:;!'|·ijlt-()/")
WIDE = frozenset("mwMW@%&")
BOLD = 1.08


class CoverLayoutError(ValueError):
    """Copy or a count no longer fits its column on the cover."""


def asset_path(lang: str, theme: str, *, mobile: bool = False) -> str:
    """Repository-relative path, as the README <picture> references it."""
    name = f"readme-cover-{lang}-{theme}{'-mobile' if mobile else ''}.svg"
    return (OUT / name).relative_to(ROOT).as_posix()


def picture_sources(lang: str) -> list[tuple[str, str]]:
    """<source> media and files for the README <picture>, fallback excluded.

    When a reader fixes their GitHub theme, GitHub's <themed-picture> replaces
    the whole media query of any source naming a colour scheme, width condition
    included. No single order is then right for everyone; this one is exact for
    "sync with system" and fixed-dark readers, and sends fixed-light readers on
    a phone the desktop light card, scaled. PR #16's order stretched the phone
    layout across fixed-dark desktops. tests/test_readme_cover.py replays
    GitHub's rewrite over every mode, scheme and width.
    """
    narrow, wide = f"(max-width: {HERO_BREAKPOINT - 1}px)", f"(min-width: {HERO_BREAKPOINT}px)"
    return [
        (f"{wide} and (prefers-color-scheme: light)", asset_path(lang, "light")),
        (f"{narrow} and (prefers-color-scheme: light)", asset_path(lang, "light", mobile=True)),
        (narrow, asset_path(lang, "dark", mobile=True)),
        ("(prefers-color-scheme: dark)", asset_path(lang, "dark")),
    ]


def description(lang: str, stats: dict) -> str:
    """Keep the record/verification distinction available to screen readers."""
    if lang == "zh":
        return (
            f"Jev 发布榜：{stats['products']:,} 个用 Jev 做的产品、"
            f"{stats['makers']:,} 位 Maker、"
            f"{stats['call_site_rows']:,} 条调用点引用记录。"
            "数字来自保存的记录，不代表当前链接可用或运行与性能测试通过。"
        )
    return (
        f"Jev Launches: {stats['products']:,} products built on Jev by "
        f"{stats['makers']:,} makers, with "
        f"{stats['call_site_rows']:,} call-site citation records. "
        "Counts describe saved records, not current link availability or passed runtime and performance tests."
    )


def text_width(text: str, size: float, *, mono: bool = False, bold: bool = False, tracking: float = 0.0) -> float:
    def advance(ch: str) -> float:
        if unicodedata.east_asian_width(ch) in ("W", "F"):
            return 1.0
        if mono:
            return 0.62
        if ch in WIDE:
            em = 0.92
        elif ch in NARROW:
            em = 0.34
        else:
            em = 0.72 if ch.isupper() else 0.58
        return em * BOLD if bold else em

    return sum(advance(ch) for ch in text) * size + tracking * len(text)


def check(what: str, text: str, x: float, needed: float, limit: float) -> None:
    """Fail the build, naming the culprit, instead of letting text collide."""
    if x + needed > limit:
        raise CoverLayoutError(
            f"README cover: {what} {text!r} needs about {needed:.0f}px from x={x:.0f}, "
            f"but its column ends at x={limit:.0f}. Shorten it in COPY or widen the layout."
        )


def fit(what: str, text: str, x: float, limit: float, size: float, *, mono: bool = False, bold: bool = False, tracking: float = 0.0) -> None:
    check(what, text, x, text_width(text, size, mono=mono, bold=bold, tracking=tracking), limit)


def clip(text: str, size: float, limit: float, *, mono: bool = False, bold: bool = False, tracking: float = 0.0) -> str:
    """`text` cut to `limit` pixels at `size`, with an ellipsis where cut: for
    the words nobody here chose (a product's title and line), which must never
    fail the build. Whitespace runs become one space, as SVG draws them."""
    text = " ".join(text.split())
    if text_width(text, size, mono=mono, bold=bold, tracking=tracking) <= limit:
        return text
    for end in range(len(text) - 1, 0, -1):
        cut = text[:end].rstrip() + "…"
        if text_width(cut, size, mono=mono, bold=bold, tracking=tracking) <= limit:
            return cut
    return "…"


def text(x: float, y: float, content: str, size: float, cls: str = "", **attrs: object) -> str:
    extra = "".join(f' {name.replace("_", "-")}="{escape(str(value))}"' for name, value in attrs.items())
    css = f' class="{cls}"' if cls else ""
    return f'<text x="{x}" y="{y}" font-size="{size}"{css}{extra}>{escape(content)}</text>'


def opening(lang: str, stats: dict, c: dict, width: int, height: int, fade: tuple[int, int, int, int]) -> list[str]:
    """Card, styles and a brand grid that fades in along `fade` (x1, y1, x2, y2)."""
    x1, y1, x2, y2 = fade
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
        '<title id="title">awesome-jev · Jev Launches</title>',
        f'<desc id="description">{escape(description(lang, stats))}</desc>',
        f'<style>text{{font-family:{SANS};fill:{c["fg"]}}}.mono{{font-family:{MONO}}}'
        f'.muted{{fill:{c["muted"]}}}.faint{{fill:{c["faint"]}}}.accent{{fill:{c["accent"]}}}</style>',
        '<defs>',
        f'<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="{c["grid"]}" stroke-opacity="{c["grid_opacity"]}"/></pattern>',
        f'<linearGradient id="fade" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"><stop offset=".4" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff"/></linearGradient>',
        f'<mask id="reveal"><rect width="{width}" height="{height}" fill="url(#fade)"/></mask>',
        f'<clipPath id="card"><rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="15"/></clipPath>',
        '</defs>',
        f'<rect x=".5" y=".5" width="{width - 1}" height="{height - 1}" rx="16" fill="{c["canvas"]}" stroke="{c["rule"]}"/>',
        f'<g clip-path="url(#card)"><rect width="{width}" height="{height}" fill="url(#grid)" mask="url(#reveal)"/></g>',
    ]


def brand(x: int, y: int, s: dict, c: dict, limit: int) -> list[str]:
    """Favicon mark and wordmark; tspans flow, so no font can make them overlap."""
    needed = text_width("awesome-jev", 22, mono=True) + 12 + text_width("·", 18) + 10 + text_width(s["eyebrow"], 18)
    check("brand line", f"awesome-jev · {s['eyebrow']}", x + 46, needed, limit)
    bars = "".join(f'<rect x="{bx}" y="{by}" width="5" height="{h}" rx="1.5" fill="{fill}"/>' for bx, by, h, fill in MARK_BARS)
    return [
        f'<g transform="translate({x} {y})"><rect x=".5" y=".5" width="31" height="31" rx="7" fill="{MARK_INK}" stroke="{c["mark_edge"]}"/>{bars}</g>',
        f'<text x="{x + 46}" y="{y + 23}" font-size="18"><tspan class="mono" font-size="22" font-weight="600">awesome-jev</tspan>'
        f'<tspan class="faint" dx="12">·</tspan><tspan class="muted" dx="10">{escape(s["eyebrow"])}</tspan></text>',
    ]


def headline(x: int, limit: int, s: dict, *, title: tuple[int, float, int], lede: tuple[int, int, int]) -> list[str]:
    """Title (size, tracking, baseline) and the two-line lede (size, first baseline, leading)."""
    size, tracking, baseline = title
    lede_size, lede_y, leading = lede
    fit("title", s["title"], x - 3, limit, size, bold=True, tracking=tracking)
    for line in s["lede"]:
        fit("lede", line, x, limit, lede_size)
    return [
        text(x - 3, baseline, s["title"], size, font_weight=600, letter_spacing=tracking),
        text(x, lede_y, s["lede"][0], lede_size, "muted"),
        text(x, lede_y + leading, s["lede"][1], lede_size, "accent", font_weight=500),
    ]


def counts(x0: int, y: int, pitch: int, limit: int, stats: dict, s: dict, *, number: int, label: int) -> list[str]:
    """Three counts on an even pitch; each must fit its column, the last the card."""
    out = []
    for index, key in enumerate(METRICS):
        x = x0 + index * pitch
        end = limit if index == len(METRICS) - 1 else x + pitch - 12
        value = f"{stats[key]:,}"
        fit(f"count {key}", value, x, end, number, mono=True, tracking=-1)
        fit(f"label {key}", s["labels"][index], x, end, label)
        out.append(text(x, y, value, number, "mono accent" if index == 0 else "mono", font_weight=600, letter_spacing=-1))
        out.append(text(x, y + label + 14, s["labels"][index], label, "muted"))
    return out


def mark(kind: str, cx: float, cy: float, color: str, scale: float = 1.0) -> str:
    """The vote mark (a triangle: a thumbs-up counts as one) or the star mark
    (a rising product), drawn, so no font decides what a reader sees."""
    if kind == STAR:
        points = []
        for index in range(10):
            radius = (7.5 if index % 2 == 0 else 3.2) * scale
            angle = math.radians(-90 + index * 36)
            points.append(f"{cx + radius * math.cos(angle):.1f},{cy + radius * math.sin(angle):.1f}")
        return f'<polygon points="{" ".join(points)}" fill="{color}"/>'
    half, tall = 7.5 * scale, 12 * scale
    return f'<path d="M{cx} {cy - tall / 2}l{half} {tall}h-{2 * half}z" fill="{color}"/>'


def tier_color(tier: str | None, c: dict) -> str | None:
    """The evidence bar's colour: who read the call site (readme.board hands
    launches.tier over), or none for a card that is not a product."""
    if tier is None:
        return None
    return c["tiers"].get(tier, c["tiers"]["file"])


def card(x: float, y: float, width: float, height: float, item: dict, c: dict) -> list[str]:
    """One card of the feed: a vote box (the mark, and the count where the
    board shows one), the product's title and line, its rank once the week
    closed, and a bar in the colour of its evidence tier."""
    box, pad = 60, 16
    out = [f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="10" fill="{c["panel"]}" stroke="{c["rule"]}"/>']
    color = tier_color(item.get("tier"), c)
    if color:
        out.append(f'<rect x="{x}" y="{y + 18}" width="3" height="{height - 36}" rx="1.5" fill="{color}"/>')
    bx, by, bh = x + pad, y + 10, height - 20
    out.append(f'<rect x="{bx}" y="{by}" width="{box}" height="{bh}" rx="8" fill="{c["canvas"]}" stroke="{c["rule"]}"/>')
    cx = bx + box / 2
    if item.get("count") is None:
        out.append(mark(item["mark"], cx, by + bh / 2, c["accent"]))
    else:
        out.append(mark(item["mark"], cx, by + 15, c["accent"]))
        count = clip(str(item["count"]), 13, box - 6, mono=True, bold=True, tracking=-0.5)
        out.append(text(cx, by + bh - 9, count, 13, "mono accent", font_weight=600, text_anchor="middle", letter_spacing=-0.5))
    tx, limit = bx + box + 14, x + width - pad
    title_limit = limit
    if item.get("rank"):
        out.append(text(limit, y + 30, item["rank"], 14, "mono accent", font_weight=600, text_anchor="end"))
        title_limit = limit - text_width(item["rank"], 14, mono=True, bold=True) - 10
    out.append(text(tx, y + 30, clip(item["title"], 18, title_limit - tx, mono=True, bold=True), 18, "mono", font_weight=600))
    out.append(text(tx, y + 52, clip(item["line"], 14, limit - tx), 14, "muted"))
    return out


def feed(x: int, right: int, c: dict, cards: dict) -> list[str]:
    """The board's feed: its heading, CARDS cards and a footer."""
    width, top, pitch, height = right - x, 96, 86, 72
    out = [text(x, 73, clip(cards["heading"], 16, width, mono=True, tracking=1.6), 16, "mono faint", letter_spacing=1.6)]
    for index, item in enumerate(cards["cards"][:CARDS]):
        out += card(x, top + index * pitch, width, height, item, c)
    out.append(text(x, 383, clip(cards["footer"], 12, width, mono=True, tracking=1), 12, "mono faint", letter_spacing=1))
    return out


def feed_strip(top: int, left: int, right: int, c: dict, cards: dict) -> list[str]:
    """The feed folded into one panel for phones: the heading, then one line
    per card (mark, count, rank, title, line), clipped at the panel's edge."""
    width, edge = right - left, right - 20
    out = [
        f'<rect x="{left}" y="{top}" width="{width}" height="132" rx="12" fill="{c["panel"]}" stroke="{c["rule"]}"/>',
        text(left + 20, top + 32, clip(cards["heading"], 13, width - 40, mono=True, tracking=1.2), 13, "mono faint", letter_spacing=1.2),
    ]
    for index, item in enumerate(cards["cards"][:CARDS]):
        x, y = left + 20, top + 60 + index * 26
        out.append(mark(item["mark"], x + 6, y - 5, c["accent"], scale=0.7))
        x += 22
        lead = " ".join(str(part) for part in (item.get("count"), item.get("rank")) if part)
        if lead:
            lead = clip(lead, 14, 90, mono=True, bold=True)
            out.append(text(x, y, lead, 14, "mono accent", font_weight=600))
            x += text_width(lead, 14, mono=True, bold=True) + 10
        title = clip(item["title"], 15, min(220, edge - x), mono=True, bold=True)
        out.append(text(x, y, title, 15, "mono", font_weight=600))
        x += text_width(title, 15, mono=True, bold=True) + 10
        if edge - x > 40:
            out.append(text(x, y, clip(item["line"], 13, edge - x), 13, "muted"))
    return out


def palette(theme: str) -> dict:
    if theme not in THEMES:
        raise ValueError(f"Unknown theme: {theme}")
    return THEMES[theme]


def hero_feed() -> dict[str, dict]:
    """The feed in both languages, from the catalogue and the board's files
    (readme.board.hero). Imported here, not at the top: readme.sections
    imports this module."""
    from readme.board import hero

    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    return {lang: hero(catalog, lang) for lang in COPY}


def cover(lang: str, theme: str, stats: dict | None = None, cards: dict | None = None) -> str:
    """Desktop card: identity and counts on the left, the launch feed right."""
    c, s = palette(theme), COPY[lang]
    stats = compute() if stats is None else stats
    cards = hero_feed()[lang] if cards is None else cards
    left, limit = 60, 680
    out = opening(lang, stats, c, WIDTH, HEIGHT, (0, 0, 1, 0))
    out += brand(left, 50, s, c, limit)
    out += headline(left, limit, s, title=(64, -1.6, 172), lede=(27, 225, 37))
    out.append(f'<path d="M{left} 306H{limit - 40}" stroke="{c["rule"]}"/>')
    out += counts(left, 362, 202, limit, stats, s, number=36, label=19)
    out += feed(712, WIDTH - 60, c, cards)
    out.append("</svg>\n")
    return "\n".join(out)


def mobile_cover(lang: str, theme: str, stats: dict | None = None, cards: dict | None = None) -> str:
    """Phone layout: recomposed and stacked rather than shrunk to unreadable type."""
    c, s = palette(theme), COPY[lang]
    stats = compute() if stats is None else stats
    cards = hero_feed()[lang] if cards is None else cards
    left, limit = 36, MOBILE_WIDTH - 36
    out = opening(lang, stats, c, MOBILE_WIDTH, MOBILE_HEIGHT, (0, 1, 1, 0))
    out += brand(left, 36, s, c, limit)
    out += headline(left, limit, s, title=(54, -1.4, 146), lede=(26, 196, 36))
    out.append(f'<path d="M{left} 272H{limit}" stroke="{c["rule"]}"/>')
    out += counts(left, 322, 180, limit, stats, s, number=34, label=19)
    out += feed_strip(392, left, limit, c, cards)
    out.append("</svg>\n")
    return "\n".join(out)


def rendered_covers(stats: dict | None = None, feeds: dict[str, dict] | None = None) -> dict[str, str]:
    """Return deterministic asset contents with a single consistent stats read."""
    stats = compute() if stats is None else stats
    feeds = hero_feed() if feeds is None else feeds
    return {
        Path(asset_path(lang, theme, mobile=mobile)).name: render(lang, theme, stats, feeds[lang])
        for lang in COPY
        for theme in THEMES
        for mobile, render in ((False, cover), (True, mobile_cover))
    }


def write_covers(stats: dict | None = None, out_dir: Path = OUT, feeds: dict[str, dict] | None = None) -> list[Path]:
    """Write all cover assets; build_readme.main can share its own stats snapshot."""
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for filename, content in rendered_covers(stats, feeds).items():
        path = out_dir / filename
        path.write_text(content, encoding="utf-8")
        paths.append(path)
    return paths


def stale_covers(stats: dict | None = None, out_dir: Path = OUT, feeds: dict[str, dict] | None = None) -> list[str]:
    """Names of cover files that are missing or differ from a fresh render."""
    return sorted(
        filename
        for filename, content in rendered_covers(stats, feeds).items()
        if not (out_dir / filename).exists() or (out_dir / filename).read_text(encoding="utf-8") != content
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="report stale generated covers without modifying files")
    args = parser.parse_args()
    try:
        if args.check:
            stale = stale_covers()
            if stale:
                print("Stale README covers; run python3 scripts/build_readme_cover.py:")
                print("\n".join(f"docs/assets/{name}" for name in stale))
                return 1
            print("README covers are current")
            return 0
        paths = write_covers()
    except CoverLayoutError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"Wrote {len(paths)} README covers (desktop {WIDTH} × {HEIGHT}; mobile {MOBILE_WIDTH} × {MOBILE_HEIGHT}) to docs/assets/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
