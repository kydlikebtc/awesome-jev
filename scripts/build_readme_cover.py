#!/usr/bin/env python3
"""Generate the README's dark brand hero and narrow-screen composition.

Both GitHub themes intentionally use the same dark poster. All numbers come
from _stats.compute(); they describe saved records, never runtime test passes.
The SVGs are portable: no external fonts, images, scripts or foreign objects.

Run: python3 scripts/build_readme_cover.py [--check]
"""

from __future__ import annotations

import argparse
from html import escape
from pathlib import Path

from _stats import compute

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "assets"
WIDTH, HEIGHT = 1200, 430
MOBILE_WIDTH, MOBILE_HEIGHT = 600, 420
SANS = "Arial,Helvetica,'Noto Sans CJK SC',sans-serif"
BG = "#131412"
FG = "#f4f2e9"
MUTED = "#b9bbb2"
AMBER = "#f5a524"
RULE = "#393b34"
THEMES = ("light", "dark")

COPY = {
    "en": {
        "purpose": "Public resources for Jev, TypeSafe AI’s decision model.",
        "mobile_purpose": ("Public resources for Jev,", "TypeSafe AI’s decision model."),
        "labels": ("Public resources", "Dated 2xx links", "Call-site records"),
        "mobile_labels": (("Public", "resources"), ("Dated 2xx", "links"), ("Call-site", "records")),
    },
    "zh": {
        "purpose": "按决策场景索引 TypeSafe AI 决策模型 Jev 的公开资源。",
        "mobile_purpose": ("TypeSafe AI 决策模型 Jev", "公开资源，按决策场景索引。"),
        "labels": ("公开资源", "带日期的 2xx 链接", "调用点记录"),
        "mobile_labels": (("公开", "资源"), ("有日期 2xx", "链接"), ("调用点", "记录")),
    },
}
METRICS = ("entries", "link_ok", "evidence_rows")


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


def opening(lang: str, stats: dict, width: int, height: int) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
        '<title id="title">awesome-jev · Jev Decision Atlas</title>',
        f'<desc id="description">{escape(description(lang, stats))}</desc>',
        '<style>',
        f'text{{font-family:{SANS};fill:{FG}}}',
        f'.muted{{fill:{MUTED}}}.amber{{fill:{AMBER}}}',
        '.wordmark{font-weight:800}.number{font-weight:700;font-variant-numeric:tabular-nums}',
        '</style>',
        f'<rect width="{width}" height="{height}" fill="{BG}"/>',
    ]


def brand(x: int, y: int, font_size: int) -> list[str]:
    """The only graphic: the shared three-bar mark beside the atlas name."""
    return [
        f'<rect x="{x}" y="{y + 19}" width="7" height="9" rx="1.5" fill="#4ec97a"/>',
        f'<rect x="{x + 11}" y="{y + 10}" width="7" height="18" rx="1.5" fill="#a9b3c0"/>',
        f'<rect x="{x + 22}" y="{y}" width="7" height="28" rx="1.5" fill="{AMBER}"/>',
        f'<text x="{x + 48}" y="{y + 23}" font-size="{font_size}" letter-spacing="1.6" class="muted">JEV DECISION ATLAS</text>',
    ]


def cover(lang: str, theme: str, stats: dict | None = None) -> str:
    """Render the desktop poster; theme is retained for stable asset names."""
    if theme not in THEMES:
        raise ValueError(f"Unknown theme: {theme}")
    stats = compute() if stats is None else stats
    s = COPY[lang]
    out = opening(lang, stats, WIDTH, HEIGHT)
    out.extend(brand(58, 38, 21))
    out.extend([
        '<text x="51" y="219" font-size="136" letter-spacing="-7.2" class="wordmark">awesome<tspan class="amber">-jev</tspan></text>',
        f'<text x="59" y="274" font-size="29">{escape(s["purpose"])}</text>',
        f'<path d="M58 315H1142" stroke="{RULE}"/>',
    ])
    for index, (key, x) in enumerate(zip(METRICS, (58, 437, 816))):
        accent = " amber" if index == 0 else ""
        out.extend([
            f'<text x="{x}" y="368" font-size="41" letter-spacing="-1.3" class="number{accent}">{stats[key]:,}</text>',
            f'<text x="{x}" y="401" font-size="21" class="muted">{escape(s["labels"][index])}</text>',
        ])
    out.append('</svg>\n')
    return '\n'.join(out)


def mobile_cover(lang: str, theme: str, stats: dict | None = None) -> str:
    """Recompose rather than shrink the desktop poster into unreadable type."""
    if theme not in THEMES:
        raise ValueError(f"Unknown theme: {theme}")
    stats = compute() if stats is None else stats
    s = COPY[lang]
    out = opening(lang, stats, MOBILE_WIDTH, MOBILE_HEIGHT)
    out.extend(brand(32, 29, 21))
    out.extend([
        '<text x="27" y="158" font-size="82" letter-spacing="-4.4" class="wordmark">awesome<tspan class="amber">-jev</tspan></text>',
        f'<text x="33" y="211" font-size="28">{escape(s["mobile_purpose"][0])}</text>',
        f'<text x="33" y="248" font-size="28">{escape(s["mobile_purpose"][1])}</text>',
        f'<path d="M32 285H568" stroke="{RULE}"/>',
    ])
    for index, (key, x) in enumerate(zip(METRICS, (32, 220, 408))):
        accent = " amber" if index == 0 else ""
        labels = s["mobile_labels"][index]
        out.extend([
            f'<text x="{x}" y="338" font-size="39" letter-spacing="-1.3" class="number{accent}">{stats[key]:,}</text>',
            f'<text x="{x}" y="372" font-size="22" class="muted">{escape(labels[0])}</text>',
            f'<text x="{x}" y="399" font-size="22" class="muted">{escape(labels[1])}</text>',
        ])
    out.append('</svg>\n')
    return '\n'.join(out)


def rendered_covers(stats: dict | None = None) -> dict[str, str]:
    """Return deterministic asset contents with a single consistent stats read."""
    stats = compute() if stats is None else stats
    return {
        f"readme-cover-{lang}-{theme}{suffix}.svg": render(lang, theme, stats)
        for lang in COPY
        for theme in THEMES
        for suffix, render in (("", cover), ("-mobile", mobile_cover))
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report stale generated covers without modifying files")
    args = parser.parse_args()
    if args.check:
        stale = [
            f"docs/assets/{filename}"
            for filename, content in rendered_covers().items()
            if not (OUT / filename).exists() or (OUT / filename).read_text(encoding="utf-8") != content
        ]
        if stale:
            print("Stale README covers; run python3 scripts/build_readme_cover.py:")
            print("\n".join(stale))
            return 1
        print("README covers are current")
    else:
        write_covers()
        print("Wrote 8 README covers (desktop 1200 × 430; mobile 600 × 420) to docs/assets/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
