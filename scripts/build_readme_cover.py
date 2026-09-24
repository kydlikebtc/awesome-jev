#!/usr/bin/env python3
"""Build compact, theme-aware README covers without external image services.

The cover identifies the catalogue rather than duplicating the site's interface.
It contains no mutable counts, sample confidence values, or claims of testing.
GitHub can render these self-contained SVG files through a README <picture>.

Run: python3 scripts/build_readme_cover.py [--check]
"""

from __future__ import annotations

import argparse
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "assets"
WIDTH, HEIGHT = 1200, 300
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,'Noto Sans CJK SC',sans-serif"
MONO = "ui-monospace,SFMono-Regular,Consolas,'Liberation Mono',monospace"

THEMES = {
    "light": {
        "bg": "#f7f8fa", "fg": "#18212b", "muted": "#586675",
        "line": "#d5dde5", "panel": "#ffffff", "amber": "#ad6500", "green": "#21834a",
    },
    "dark": {
        "bg": "#10161d", "fg": "#eef2f6", "muted": "#a2afbd",
        "line": "#33404e", "panel": "#17212b", "amber": "#f5a524", "green": "#4ec97a",
    },
}

COPY = {
    "en": {
        "tagline": "Examples by task. Evidence in view.",
        "foot": "PUBLIC RESOURCES  /  DECISION PATTERNS  /  SOURCE NOTES",
        "diagram": "STRUCTURED DECISIONS",
        "state": "state",
        "types": ("category", "ordinal", "probability"),
        "desc": "Jev Decision Atlas: a catalogue of public Jev examples organised by task, with source evidence. A small diagram connects state to the choice, score and noul primitives.",
    },
    "zh": {
        "tagline": "按场景找案例，沿证据做判断。",
        "foot": "公开资源  /  决策模式  /  来源记录",
        "diagram": "结构化决策",
        "state": "状态",
        "types": ("类别", "级别", "概率"),
        "desc": "Jev 决策图谱：按场景整理公开案例，保留来源与证据。右侧示意图连接状态与 choice、score、noul 三种原语。",
    },
}


def cover(lang: str, theme: str) -> str:
    c, s = THEMES[theme], COPY[lang]
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title description">',
        '<title id="title">awesome-jev · Jev Decision Atlas</title>',
        f'<desc id="description">{escape(s["desc"])}</desc>',
        '<style>',
        f'text{{font-family:{SANS};fill:{c["fg"]}}}',
        f'.mono{{font-family:{MONO}}}',
        f'.muted{{fill:{c["muted"]}}}',
        '</style>',
        f'<rect x=".5" y=".5" width="1199" height="299" rx="16" fill="{c["bg"]}" stroke="{c["line"]}"/>',
        # Shared three-bar brand mark, drawn inline for portable image rendering.
        '<rect x="44" y="35" width="36" height="36" rx="8" fill="#0b0d10"/>',
        '<rect x="52" y="57" width="5" height="7" rx="1.5" fill="#4ec97a"/>',
        '<rect x="59.5" y="50" width="5" height="14" rx="1.5" fill="#a9b3c0"/>',
        '<rect x="67" y="43" width="5" height="21" rx="1.5" fill="#f5a524"/>',
        '<text x="95" y="59" font-size="15" font-weight="600" letter-spacing="2.1" class="muted">JEV DECISION ATLAS</text>',
        '<text x="42" y="145" font-size="72" font-weight="750" letter-spacing="-3">awesome<tspan fill="' + c["amber"] + '">-</tspan>jev</text>',
        f'<text x="45" y="190" font-size="25">{escape(s["tagline"])}</text>',
        f'<path d="M44 228H675" stroke="{c["line"]}"/>',
        f'<text x="45" y="260" font-size="12.5" letter-spacing="1.1" class="muted">{escape(s["foot"])}</text>',
        f'<path d="M719 35V265" stroke="{c["line"]}"/>',
        f'<text x="766" y="59" font-size="12.5" letter-spacing="1.3" class="muted">{escape(s["diagram"])}</text>',
        # Branches carry no numeric values; this is a topology, not example output.
        f'<path d="M843 163H881M881 109V217M881 109H916M881 163H916M881 217H916" fill="none" stroke="{c["line"]}" stroke-width="2"/>',
        f'<rect x="766" y="144" width="77" height="38" rx="7" fill="{c["panel"]}" stroke="{c["line"]}"/>',
        f'<text x="804.5" y="168" text-anchor="middle" class="mono" font-size="15">{escape(s["state"])}</text>',
        f'<circle cx="881" cy="163" r="4" fill="{c["amber"]}"/>',
    ]
    for index, primitive in enumerate(("choice", "score", "noul")):
        y = 87 + index * 54
        accent = (c["amber"], c["muted"], c["green"])[index]
        out.extend([
            f'<rect x="916" y="{y}" width="240" height="44" rx="7" fill="{c["panel"]}" stroke="{c["line"]}"/>',
            f'<rect x="929" y="{y + 17}" width="4" height="10" rx="2" fill="{accent}"/>',
            f'<text x="945" y="{y + 28}" font-size="19" font-weight="600" class="mono">{primitive}</text>',
            f'<text x="1141" y="{y + 27}" text-anchor="end" font-size="12.5" class="muted">{escape(s["types"][index])}</text>',
        ])
    out.append('</svg>\n')
    return '\n'.join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report stale generated covers without modifying files")
    args = parser.parse_args()
    stale = []
    if not args.check:
        OUT.mkdir(parents=True, exist_ok=True)
    for lang in COPY:
        for theme in THEMES:
            path = OUT / f"readme-cover-{lang}-{theme}.svg"
            content = cover(lang, theme)
            if args.check:
                if not path.exists() or path.read_text(encoding="utf-8") != content:
                    stale.append(str(path.relative_to(ROOT)))
            else:
                path.write_text(content, encoding="utf-8")
    if stale:
        print("Stale README covers; run python3 scripts/build_readme_cover.py:")
        print("\n".join(stale))
        return 1
    print("README covers are current" if args.check else "Wrote 4 README covers (1200 × 300) to docs/assets/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
