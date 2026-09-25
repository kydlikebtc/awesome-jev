#!/usr/bin/env python3
"""Generate the README hero: a theme-aware atlas card and its phone layout.

GitHub picks the light or dark file through the README <picture>, so each
theme is drawn for its own canvas rather than one poster serving both. Counts
come from _stats.compute() and describe saved records, never runtime test
passes. The SVGs are portable: system fonts only, and no external fonts,
images, scripts or foreign objects, none of which an SVG shown as <img> may
load anyway.

Text is placed from conservative advance-width estimates, and the build fails
when copy or a grown count would overrun its column. Fonts differ by platform,
so a layout that merely fits on the author's machine proves nothing.

Run: python3 scripts/build_readme_cover.py [--check]
"""

from __future__ import annotations

import argparse
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
THEMES = {
    "light": {
        "canvas": "#f6f8fa", "panel": "#ffffff", "fg": "#1f2328", "muted": "#59636e",
        "faint": "#656d76", "rule": "#d1d9e0", "grid": "#1f2328", "grid_opacity": ".05",
        "accent": "#a15c00", "joint": "#e59a1a", "answers": ("#a15c00", "#6e7781", "#1a7f37"),
        "mark_edge": MARK_INK,
    },
    "dark": {
        "canvas": "#0b0d10", "panel": "#121821", "fg": "#e6edf3", "muted": "#9198a1",
        "faint": "#8b949e", "rule": "#30363d", "grid": "#ffffff", "grid_opacity": ".045",
        "accent": "#f5a524", "joint": "#f5a524", "answers": ("#f5a524", "#a9b3c0", "#4ec97a"),
        # The ink tile would vanish into an ink canvas without an edge.
        "mark_edge": "#3d444d",
    },
}
COPY = {
    "en": {
        "eyebrow": "community index",
        "title": "Jev Decision Atlas",
        "lede": ("Find Jev examples by task.", "Inspect the evidence before you build."),
        "labels": ("public resources", "dated 2xx links", "call-site records"),
        "diagram": "ONE STATE · TYPED QUESTIONS",
        "state_note": "text · JSON",
        "answers": ("category", "ordinal", "probability"),
    },
    "zh": {
        "eyebrow": "社区目录",
        "title": "Jev 决策图谱",
        "lede": ("按场景发现 Jev 用法，", "沿证据判断是否适合你的项目。"),
        "labels": ("公开资源", "带日期的 2xx 链接", "调用点记录"),
        "diagram": "一个状态 · 多个类型化问题",
        "state_note": "文本 · JSON",
        "answers": ("类别", "等级", "概率"),
    },
}
METRICS = ("entries", "link_ok", "evidence_rows")
PRIMITIVES = ("choice", "score", "noul")
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
            f"Jev 决策图谱：{stats['entries']:,} 条公开资源、"
            f"{stats['link_ok']:,} 条带日期的 HTTP 2xx 链接记录、"
            f"{stats['evidence_rows']:,} 条调用点引用记录。"
            "数字来自保存的记录，不代表当前链接可用或运行与性能测试通过。"
        )
    return (
        f"Jev Decision Atlas: {stats['entries']:,} public resources, "
        f"{stats['link_ok']:,} dated HTTP 2xx link records, and "
        f"{stats['evidence_rows']:,} call-site citation records. "
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


def text(x: float, y: float, content: str, size: float, cls: str = "", **attrs: object) -> str:
    extra = "".join(f' {name.replace("_", "-")}="{escape(str(value))}"' for name, value in attrs.items())
    css = f' class="{cls}"' if cls else ""
    return f'<text x="{x}" y="{y}" font-size="{size}"{css}{extra}>{escape(content)}</text>'


def opening(lang: str, stats: dict, c: dict, width: int, height: int, fade: tuple[int, int, int, int]) -> list[str]:
    """Card, styles and a brand grid that fades in along `fade` (x1, y1, x2, y2)."""
    x1, y1, x2, y2 = fade
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
        '<title id="title">awesome-jev · Jev Decision Atlas</title>',
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


def icon(name: str, x: float, y: float, c: dict, color: str) -> str:
    """What each answer looks like: one of several, a level, a point on 0–1."""
    if name == "choice":
        return "".join(
            f'<circle cx="{x + i * 15}" cy="{y}" r="4.5" fill="{color if i == 1 else "none"}" '
            f'stroke="{color if i == 1 else c["faint"]}" stroke-width="1.5"/>'
            for i in range(4)
        )
    if name == "score":
        return "".join(
            f'<rect x="{x - 4 + i * 11}" y="{y + 3 - i * 3}" width="7" height="{4 + i * 3}" rx="1.5" '
            + (f'fill="{color}"/>' if i < 3 else f'fill="none" stroke="{c["faint"]}" stroke-width="1.2"/>')
            for i in range(5)
        )
    return (
        f'<rect x="{x - 4}" y="{y - 2.5}" width="52" height="5" rx="2.5" fill="{c["rule"]}"/>'
        f'<rect x="{x - 4}" y="{y - 2.5}" width="34" height="5" rx="2.5" fill="{color}"/>'
        f'<circle cx="{x + 30}" cy="{y}" r="5.5" fill="{c["panel"]}" stroke="{color}" stroke-width="2"/>'
    )


def diagram(x: int, right: int, s: dict, c: dict) -> list[str]:
    """One state fanning out to the three typed answers: shapes, never sample values."""
    rows, mid, trunk, left = (148, 232, 316), 232, x + 150, x + 184
    fit("diagram heading", s["diagram"], x, right, 16, mono=True, tracking=1.6)
    fit("state label", "state", x + 8, x + 108, 20, mono=True)
    fit("state note", s["state_note"], x + 8, x + 108, 15)
    out = [
        text(x, 73, s["diagram"], 16, "mono faint", letter_spacing=1.6),
        f'<path d="M{x + 116} {mid}H{trunk}M{trunk} {rows[0] + 12}V{rows[2] - 12}M{trunk} {rows[0] + 12}q0 -12 12 -12H{left}'
        f'M{trunk} {mid}H{left}M{trunk} {rows[2] - 12}q0 12 12 12H{left}" fill="none" stroke="{c["rule"]}" stroke-width="2"/>',
        f'<circle cx="{trunk}" cy="{mid}" r="4" fill="{c["joint"]}"/>',
        f'<rect x="{x}" y="{mid - 34}" width="116" height="68" rx="10" fill="{c["panel"]}" stroke="{c["rule"]}"/>',
        text(x + 58, mid - 2, "state", 20, "mono", font_weight=600, text_anchor="middle"),
        text(x + 58, mid + 21, s["state_note"], 15, "faint", text_anchor="middle"),
    ]
    for name, kind, y, color in zip(PRIMITIVES, s["answers"], rows, c["answers"]):
        fit(f"{name} name", name, left + 22, right - 90, 20, mono=True)
        fit(f"{name} type", kind, left + 22, right - 90, 16)
        out += [
            f'<rect x="{left}" y="{y - 30}" width="{right - left}" height="60" rx="10" fill="{c["panel"]}" stroke="{c["rule"]}"/>',
            f'<rect x="{left}" y="{y - 14}" width="3" height="28" rx="1.5" fill="{color}"/>',
            text(left + 22, y - 3, name, 20, "mono", font_weight=600),
            text(left + 22, y + 19, kind, 16, "muted"),
            icon(name, right - 78, y, c, color),
        ]
    return out


def strip(top: int, left: int, right: int, s: dict, c: dict) -> list[str]:
    """The diagram folded into one row for phones."""
    fit("diagram heading", s["diagram"], left + 20, right - 20, 16, mono=True, tracking=1.4)
    out = [
        f'<rect x="{left}" y="{top}" width="{right - left}" height="132" rx="12" fill="{c["panel"]}" stroke="{c["rule"]}"/>',
        text(left + 20, top + 34, s["diagram"], 16, "mono faint", letter_spacing=1.4),
    ]
    for index, (name, kind, color) in enumerate(zip(PRIMITIVES, s["answers"], c["answers"])):
        x = left + 20 + index * 172
        fit(f"{name} name", name, x + 16, min(x + 164, right - 20), 22, mono=True)
        fit(f"{name} type", kind, x + 16, min(x + 164, right - 20), 18)
        out += [
            f'<rect x="{x}" y="{top + 58}" width="3" height="48" rx="1.5" fill="{color}"/>',
            text(x + 16, top + 78, name, 22, "mono", font_weight=600),
            text(x + 16, top + 104, kind, 18, "muted"),
        ]
    return out


def palette(theme: str) -> dict:
    if theme not in THEMES:
        raise ValueError(f"Unknown theme: {theme}")
    return THEMES[theme]


def cover(lang: str, theme: str, stats: dict | None = None) -> str:
    """Desktop card: identity and counts on the left, the decision diagram right."""
    c, s = palette(theme), COPY[lang]
    stats = compute() if stats is None else stats
    left, limit = 60, 680
    out = opening(lang, stats, c, WIDTH, HEIGHT, (0, 0, 1, 0))
    out += brand(left, 50, s, c, limit)
    out += headline(left, limit, s, title=(64, -1.6, 172), lede=(27, 225, 37))
    out.append(f'<path d="M{left} 306H{limit - 40}" stroke="{c["rule"]}"/>')
    out += counts(left, 362, 202, limit, stats, s, number=36, label=19)
    out += diagram(712, WIDTH - 60, s, c)
    out.append("</svg>\n")
    return "\n".join(out)


def mobile_cover(lang: str, theme: str, stats: dict | None = None) -> str:
    """Phone layout: recomposed and stacked rather than shrunk to unreadable type."""
    c, s = palette(theme), COPY[lang]
    stats = compute() if stats is None else stats
    left, limit = 36, MOBILE_WIDTH - 36
    out = opening(lang, stats, c, MOBILE_WIDTH, MOBILE_HEIGHT, (0, 1, 1, 0))
    out += brand(left, 36, s, c, limit)
    out += headline(left, limit, s, title=(54, -1.4, 146), lede=(26, 196, 36))
    out.append(f'<path d="M{left} 272H{limit}" stroke="{c["rule"]}"/>')
    out += counts(left, 322, 180, limit, stats, s, number=34, label=19)
    out += strip(392, left, limit, s, c)
    out.append("</svg>\n")
    return "\n".join(out)


def rendered_covers(stats: dict | None = None) -> dict[str, str]:
    """Return deterministic asset contents with a single consistent stats read."""
    stats = compute() if stats is None else stats
    return {
        Path(asset_path(lang, theme, mobile=mobile)).name: render(lang, theme, stats)
        for lang in COPY
        for theme in THEMES
        for mobile, render in ((False, cover), (True, mobile_cover))
    }


def write_covers(stats: dict | None = None, out_dir: Path = OUT) -> list[Path]:
    """Write all cover assets; build_readme.main can share its own stats snapshot."""
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for filename, content in rendered_covers(stats).items():
        path = out_dir / filename
        path.write_text(content, encoding="utf-8")
        paths.append(path)
    return paths


def stale_covers(stats: dict | None = None, out_dir: Path = OUT) -> list[str]:
    """Names of cover files that are missing or differ from a fresh render."""
    return sorted(
        filename
        for filename, content in rendered_covers(stats).items()
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
