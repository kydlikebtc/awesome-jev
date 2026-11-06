#!/usr/bin/env python3
"""Draw the README's "how a launch week runs" figure, with where the board is now.

Four stations on one track: launch by Thursday, filed on Friday, vote Monday
to Sunday, results the next Monday. The station the board is at is filled in
and tagged NOW, and the line over the track says which week and until when:
votes open (a week is running), filed (next week's launches are in, nothing
runs yet), or taking launches (neither). That state is read from the week
files in launches/ the way the README's first section reads them
(readme.board), never from the clock, so two builds of the same tree write
the same bytes, and the Friday and Monday runs that change the files
regenerate this figure in the same commit (they run regenerate.py, whose
build_readme.py draws it).

Like the cover (build_readme_cover.py, whose palette, text measures and
layout checks this reuses): a light and a dark file per language, each with a
phone layout, chosen by the README <picture> exactly as the cover's are;
system fonts only, nothing external. All of the copy is ours, so copy that
would overrun its column fails the build rather than collide.

Run: python3 scripts/build_readme_week.py [--check]
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import dataclass
from html import escape
from pathlib import Path

import build_readme_cover as cover

ROOT = cover.ROOT
OUT = cover.OUT
STEM = "launch-week"
WIDTH, HEIGHT = 1200, 300
MOBILE_WIDTH, MOBILE_HEIGHT = 600, 670
PHASES = ("launch", "filed", "vote", "results")

COPY = {
    "en": {
        "title": "How a launch week runs",
        "eyebrow": "HOW A LAUNCH WEEK RUNS",
        "now": "NOW",
        "steps": (
            ("Launch", "by Thursday 23:59 UTC", "the launch form, checked at once"),
            ("Filed", "Friday", "on next week's board"),
            ("Vote", "Monday to Sunday", "a thumbs-up on each post"),
            ("Results", "the next Monday", "ranked; the top three on their badge"),
        ),
        "status": {
            "launch": "TAKING LAUNCHES FOR NEXT WEEK",
            "filed": "{week} FILED · OPENS MONDAY {monday}",
            "vote": "{week} · VOTES OPEN UNTIL SUNDAY {sunday}",
        },
        "alt": (
            "How a launch week runs: launch by Thursday 23:59 UTC, filed on Friday, vote from Monday to "
            "Sunday, results the next Monday. Now: {status}."
        ),
    },
    "zh": {
        "title": "一周发布流程",
        "eyebrow": "一周发布流程",
        "now": "现在",
        "steps": (
            ("发布", "周四 23:59 UTC 前", "填发布表单，立即检查"),
            ("登记", "周五", "排进下周的榜"),
            ("投票", "周一到周日", "在每个帖子上点赞"),
            ("结果", "下周一", "排名，前三名上徽章"),
        ),
        "status": {
            "launch": "正在接受下周的 Launch",
            "filed": "{week} 已登记 · {monday}（周一）开榜",
            "vote": "{week} · 投票中，{sunday}（周日）收榜",
        },
        "alt": "一周发布流程：周四 23:59 UTC 前发布，周五登记，周一到周日投票，下周一出结果。现在：{status}。",
    },
}


@dataclass(frozen=True)
class Now:
    """Where the board is: a phase (one of PHASES) and the week it is about."""

    phase: str
    week: str | None = None

    def status(self, lang: str) -> str:
        words = COPY[lang]["status"][self.phase]
        if self.week is None:
            return words
        monday, sunday = week_days(self.week)
        return words.format(week=self.week, monday=monday.isoformat(), sunday=sunday.isoformat())


def week_days(week: str) -> tuple[dt.date, dt.date]:
    from launches import week_days as days

    return days(week)


def now_of(catalog: list[dict]) -> Now:
    """The board's phase from the week files, as the README's first section
    reads them: a running week with launches on it means votes are open;
    else a filed week with launches means it opens next Monday; else the
    board is taking launches. Results never stay the phase: the Monday run
    that writes them opens the next week in the same commit."""
    from readme.board import read_board

    board = read_board(catalog)
    if board.on(board.running):
        return Now("vote", board.running["week"])
    if board.on(board.coming):
        return Now("filed", board.coming["week"])
    return Now("launch")


def alt_text(lang: str, now: Now) -> str:
    """The figure's description, as the README <img> alt and the SVG <desc>."""
    return COPY[lang]["alt"].format(status=now.status(lang))


def icon(phase: str, cx: float, cy: float, color: str) -> str:
    """Each station's mark, drawn, so no font decides what a reader sees: an
    arrow going up (launch), a tick (filed), the vote mark, a podium."""
    if phase == "launch":
        return (f'<path d="M{cx} {cy - 10}l8 9h-5v10h-6v-10h-5z" fill="{color}"/>')
    if phase == "filed":
        return (f'<path d="M{cx - 9} {cy + 1}l6 6l12 -13" fill="none" stroke="{color}" stroke-width="3.2" '
                f'stroke-linecap="round" stroke-linejoin="round"/>')
    if phase == "vote":
        return cover.mark(cover.VOTE, cx, cy + 1, color)
    return (f'<rect x="{cx - 11}" y="{cy - 2}" width="6" height="10" rx="1" fill="{color}"/>'
            f'<rect x="{cx - 3}" y="{cy - 9}" width="6" height="17" rx="1" fill="{color}"/>'
            f'<rect x="{cx + 5}" y="{cy + 1}" width="6" height="7" rx="1" fill="{color}"/>')


def station(phase: str, index: int, here: int, cx: float, cy: float, c: dict, radius: int) -> list[str]:
    """One station's disc: filled in the accent where the board is now,
    ringed in the accent where it has been this week, plain ahead of it."""
    if index == here:
        disc = f'<circle cx="{cx}" cy="{cy}" r="{radius + 8}" fill="{c["accent"]}" fill-opacity=".14"/>'
        disc += f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="{c["accent"]}"/>'
        return [disc, icon(phase, cx, cy, c["canvas"])]
    ring = c["accent"] if index < here else c["rule"]
    color = c["accent"] if index < here else c["faint"]
    return [f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="{c["panel"]}" stroke="{ring}" stroke-width="2"/>',
            icon(phase, cx, cy, color)]


def now_tag(x: float, y: float, words: str, c: dict, *, anchor: str = "middle") -> list[str]:
    """The NOW tag: a small accent pill. `x` is its centre, or its left edge
    with anchor="start"."""
    size = 12
    width = cover.text_width(words, size, mono=True, bold=True, tracking=1.2) + 18
    left = x - width / 2 if anchor == "middle" else x
    return [
        f'<rect x="{left:.1f}" y="{y - 15}" width="{width:.1f}" height="22" rx="11" fill="{c["accent"]}"/>',
        cover.text(left + width / 2, y + 1, words, size, "mono inv", font_weight=700, text_anchor="middle",
                   letter_spacing=1.2),
    ]


def opening(lang: str, now: Now, c: dict, width: int, height: int) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        'role="img" aria-labelledby="title description">',
        f'<title id="title">{escape(COPY[lang]["title"])}</title>',
        f'<desc id="description">{escape(alt_text(lang, now))}</desc>',
        f'<style>text{{font-family:{cover.SANS};fill:{c["fg"]}}}.mono{{font-family:{cover.MONO}}}'
        f'.muted{{fill:{c["muted"]}}}.faint{{fill:{c["faint"]}}}.accent{{fill:{c["accent"]}}}'
        f'.inv{{fill:{c["canvas"]}}}</style>',
        f'<rect x=".5" y=".5" width="{width - 1}" height="{height - 1}" rx="16" fill="{c["canvas"]}" stroke="{c["rule"]}"/>',
    ]


def figure(lang: str, theme: str, now: Now) -> str:
    """Desktop: the eyebrow and the status line, then the four stations in a
    row on one track, each with its name, when, and what happens."""
    c, s = cover.palette(theme), COPY[lang]
    here = PHASES.index(now.phase)
    left, right = 60, WIDTH - 60
    out = opening(lang, now, c, WIDTH, HEIGHT)
    cover.fit("eyebrow", s["eyebrow"], left, WIDTH / 2, 16, mono=True, tracking=1.6)
    out.append(cover.text(left, 62, s["eyebrow"], 16, "mono faint", letter_spacing=1.6))
    status = now.status(lang)
    cover.fit("status", status, WIDTH / 2 - 40, right, 16, mono=True, bold=True, tracking=1.2)
    out.append(cover.text(right, 62, status, 16, "mono accent", font_weight=600, text_anchor="end",
                          letter_spacing=1.2))
    pitch = (right - left) / len(PHASES)
    xs = [left + pitch * (i + 0.5) for i in range(len(PHASES))]
    track = 140
    out.append(f'<path d="M{xs[0]} {track}H{xs[-1]}" stroke="{c["rule"]}" stroke-width="3" stroke-linecap="round"/>')
    if here:
        out.append(f'<path d="M{xs[0]} {track}H{xs[here]}" stroke="{c["accent"]}" stroke-width="3" '
                   'stroke-linecap="round"/>')
    for index, (phase, (name, when, what)) in enumerate(zip(PHASES, s["steps"])):
        x = xs[index]
        out += station(phase, index, here, x, track, c, 26)
        if index == here:
            out += now_tag(x, 94, s["now"], c)
        for label, text, size, kw in (
            ("step", name, 22, {"bold": True}), ("when", when, 15, {"mono": True}), ("what", what, 14, {}),
        ):
            cover.check(f"{label} of {phase}", text, x - pitch / 2 + 8, cover.text_width(text, size, **kw),
                        x + pitch / 2 - 8)
        out.append(cover.text(x, 204, name, 22, "accent" if index == here else "", font_weight=600,
                              text_anchor="middle"))
        out.append(cover.text(x, 232, when, 15, "mono muted", text_anchor="middle"))
        out.append(cover.text(x, 258, what, 14, "faint", text_anchor="middle"))
    out.append("</svg>\n")
    return "\n".join(out)


def mobile_figure(lang: str, theme: str, now: Now) -> str:
    """Phone: the same four stations stacked down one track, the words to
    the right of each, so nothing shrinks to unreadable type."""
    c, s = cover.palette(theme), COPY[lang]
    here = PHASES.index(now.phase)
    left, right = 36, MOBILE_WIDTH - 36
    out = opening(lang, now, c, MOBILE_WIDTH, MOBILE_HEIGHT)
    cover.fit("eyebrow", s["eyebrow"], left, right, 18, mono=True, tracking=1.6)
    out.append(cover.text(left, 58, s["eyebrow"], 18, "mono faint", letter_spacing=1.6))
    status = now.status(lang)
    cover.fit("status", status, left, right, 17, mono=True, bold=True, tracking=0.6)
    out.append(cover.text(left, 94, status, 17, "mono accent", font_weight=600, letter_spacing=0.6))
    cx, top, pitch, tx = left + 34, 168, 128, left + 84
    ys = [top + pitch * i for i in range(len(PHASES))]
    out.append(f'<path d="M{cx} {ys[0]}V{ys[-1]}" stroke="{c["rule"]}" stroke-width="3" stroke-linecap="round"/>')
    if here:
        out.append(f'<path d="M{cx} {ys[0]}V{ys[here]}" stroke="{c["accent"]}" stroke-width="3" '
                   'stroke-linecap="round"/>')
    for index, (phase, (name, when, what)) in enumerate(zip(PHASES, s["steps"])):
        y = ys[index]
        out += station(phase, index, here, cx, y, c, 26)
        cover.fit(f"step of {phase}", name, tx, right, 28, bold=True)
        cover.fit(f"when of {phase}", when, tx, right, 18, mono=True)
        cover.fit(f"what of {phase}", what, tx, right, 18)
        out.append(cover.text(tx, y - 10, name, 28, "accent" if index == here else "", font_weight=600))
        if index == here:
            tag_x = tx + cover.text_width(name, 28, bold=True) + 14
            cover.fit("now tag", s["now"], tag_x, right, 12, mono=True, bold=True, tracking=1.2)
            out += now_tag(tag_x, y - 16, s["now"], c, anchor="start")
        out.append(cover.text(tx, y + 19, when, 18, "mono muted"))
        out.append(cover.text(tx, y + 46, what, 18, "faint"))
    out.append("</svg>\n")
    return "\n".join(out)


def read_now() -> Now:
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    return now_of(catalog)


def rendered(now: Now | None = None) -> dict[str, str]:
    """Every file of the figure by name, from one reading of the board."""
    now = read_now() if now is None else now
    return {
        Path(cover.asset_path(lang, theme, mobile=mobile, stem=STEM)).name: draw(lang, theme, now)
        for lang in COPY
        for theme in cover.THEMES
        for mobile, draw in ((False, figure), (True, mobile_figure))
    }


def write_figures(now: Now | None = None, out_dir: Path = OUT) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for name, content in rendered(now).items():
        path = out_dir / name
        path.write_text(content, encoding="utf-8")
        paths.append(path)
    return paths


def stale(now: Now | None = None, out_dir: Path = OUT) -> list[str]:
    return sorted(
        name for name, content in rendered(now).items()
        if not (out_dir / name).exists() or (out_dir / name).read_text(encoding="utf-8") != content
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="report stale figures without modifying files")
    args = parser.parse_args()
    try:
        if args.check:
            names = stale()
            if names:
                print("Stale launch-week figures; run python3 scripts/build_readme_week.py:")
                print("\n".join(f"docs/assets/{name}" for name in names))
                return 1
            print("Launch-week figures are current")
            return 0
        paths = write_figures()
    except cover.CoverLayoutError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"Wrote {len(paths)} launch-week figures to docs/assets/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
