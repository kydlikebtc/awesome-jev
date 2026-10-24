#!/usr/bin/env python3
"""Plain pages the Pages deploy writes beside the app: one per decision
pattern, what's new, two feeds and a sitemap.

site/index.html is an app. It fetches catalog.json and draws every view with
script, under addresses like ?p=tool-selection, and search engines index such
views poorly when at all. A reader coming back had no page saying what changed
either. Since 2026-10-24 the deploy also writes, from the files it publishes:

  patterns/index.html          every decision pattern, in both languages
  patterns/<key>.html          the rows filed under one pattern, in English
  patterns/<key>.zh.html       the same rows in Chinese
  new.html, new.zh.html        rows added and retired, week by week
  feed.xml, feed.zh.xml        the same weeks as Atom feeds
  sitemap.xml                  the app and every page above

Rows come in the order the API and the MCP server give them
(query.sort_key()), and every word of theirs is escaped: titles, summaries and
notes are other people's words (query.TEXT_NOTE). A row's week is the Monday
of its `first_seen`. A retired row's is the date its notes open with
("Retired YYYY-MM-DD: ..."), which retired.json keeps in no field of its own.
The week the catalogue opened is counted, not listed. No date but the
catalogue's own appears, so two deploys of the same data write the same
bytes. The pages carry no script and load nothing from another host; their
fonts are site/fonts/ (tests/test_site_pages.py holds them to lint_docs'
rules for site pages).

assemble_site.py writes them (gitignored, like every copy under site/), and
check_site_data.py holds them to a rebuild before Pages publishes anything.
"""

from __future__ import annotations

import datetime as dt
import html
import pathlib
import re
import shutil
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _stats  # noqa: E402
from site_api import query  # noqa: E402

SITE_URL = "https://kydlikebtc.github.io/awesome-jev/"
REPOSITORY = "https://github.com/kydlikebtc/awesome-jev"
LANGS = ("en", "zh")
# The most weeks the what's-new page and the feeds list, newest first.
WEEKS_SHOWN = 26
RETIRED_ON = re.compile(r"^Retired (\d{4}-\d{2}-\d{2})\b")
# The summary sources a line marks, as the site and the READMEs do
# (site/catalog-core.mjs MARKED_SOURCES).
MARKED_SOURCES = ("upstream-description", "upstream-description-stale")
PATTERN_DIR = "patterns"

# The Chinese is model-written, like the site's own strings.
STRINGS = {
    "en": {
        "html_lang": "en",
        "brand": "awesome-jev",
        "app": "Search the catalogue",
        "other": "中文",
        "patterns": "Decision patterns",
        "new": "What's new",
        "feed": "Feed",
        "github": "GitHub",
        "pattern_title": "{name}: public Jev examples · awesome-jev",
        "pattern_lede": "{n} rows are filed under this pattern, {code} of them with code. "
                        "Rows are listed as the catalogue orders them: official first, then rows with code, then by stars.",
        "open_in_app": "Filter and search them in the catalogue",
        "in_app": "In the catalogue",
        "caveat_note": "Rows marked {flags} stay listed, but they are not examples of deciding with Jev.",
        "unindexed": "Not yet indexed by pattern",
        "unindexed_note": "Projects and plugins with code that nobody has yet read against the patterns: "
                          "overview is also what the keyword rules suggest when nothing matches.",
        "official": "official",
        "stars": "★{n}",
        "sep": " · ",
        "list_sep": ", ",
        "quote": "“{}”",
        "or": " or ",
        "index_title": "Decision patterns · awesome-jev",
        "index_lede": "Every decision pattern the catalogue files public Jev examples under, as plain pages "
                      "in English and Chinese. The searchable catalogue has the same rows with filters.",
        "rows": "{n} rows",
        "new_title": "What's new · awesome-jev",
        "new_lede": "Rows added to the catalogue and rows retired from it, week by week (weeks start on Monday, UTC). "
                    "Also as an Atom feed.",
        "week": "Week of {date}",
        "colon": ": ",
        "week_counts": "{added} added, {retired} retired",
        "opened": "the catalogue opened with {n} rows",
        "added": "Added",
        "retired": "Retired",
        "nothing": "Nothing yet.",
        "feed_title": "awesome-jev: what's new",
        "feed_subtitle": "Rows added to and retired from the catalogue of public Jev examples, week by week.",
        "more": "…and {n} more on the page.",
        "disclaimer": "An unaffiliated community index of TypeSafe AI's Jev. Its rows' titles and summaries are "
                      "mostly the projects' own words; the catalogue has not run the listed code.",
    },
    "zh": {
        "html_lang": "zh-CN",
        "brand": "awesome-jev",
        "app": "搜索目录",
        "other": "English",
        "patterns": "决策模式",
        "new": "新增与退役",
        "feed": "订阅",
        "github": "GitHub",
        "pattern_title": "{name}：Jev 公开示例 · awesome-jev",
        "pattern_lede": "共有 {n} 行归在这个模式下，其中 {code} 行带代码。顺序与目录相同：官方的在前，然后是带代码的，再按星标排。",
        "open_in_app": "在目录中筛选和搜索这些条目",
        "in_app": "在目录中查看",
        "caveat_note": "标有{flags}的条目照样列出，但它们不是用 Jev 做决策的示例。",
        "unindexed": "尚未按模式归类",
        "unindexed_note": "带代码、但还没有人对照各模式读过的项目和插件：关键词规则匹配不到时也会给出 overview。",
        "official": "官方",
        "stars": "★{n}",
        "sep": " · ",
        "list_sep": "、",
        "quote": "「{}」",
        "or": "或",
        "index_title": "决策模式 · awesome-jev",
        "index_lede": "目录收录的 Jev 公开示例按决策模式归类，这里是每个模式的静态页面，有中英两版。可搜索的目录里是同样的条目，另有筛选。",
        "rows": "{n} 行",
        "new_title": "新增与退役 · awesome-jev",
        "new_lede": "每周新收录和退役的条目（每周从周一开始，按 UTC 计）。也可以用 Atom 订阅。",
        "week": "{date} 这一周",
        "colon": "：",
        "week_counts": "新增 {added} 行，退役 {retired} 行",
        "opened": "目录开张，收录了 {n} 行",
        "added": "新增",
        "retired": "退役",
        "nothing": "暂时没有。",
        "feed_title": "awesome-jev：新增与退役",
        "feed_subtitle": "Jev 公开示例目录每周新收录和退役的条目。",
        "more": "……另有 {n} 行，见页面。",
        "disclaimer": "TypeSafe AI Jev 的非官方社区目录。条目的标题和摘要多是项目自己的话；本目录没有运行过收录的代码。",
    },
}

CSS = """
      :root {
        --ink: #0b0d10; --ink-2: #12151a; --rule: #242b34; --fg: #e8eaed; --fg-2: #a9b3c0;
        --fg-3: #8a95a3; --amber: #f5a524; --signal: #4ec97a; --alert: #ff9287;
        --mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, "PingFang SC", "Hiragino Sans GB",
          "Microsoft YaHei", "Noto Sans CJK SC", "Noto Sans SC", monospace;
        --sans: "IBM Plex Sans", system-ui, -apple-system, "PingFang SC", "Hiragino Sans GB",
          "Microsoft YaHei", "Noto Sans CJK SC", "Noto Sans SC", sans-serif;
      }
      * { box-sizing: border-box; }
      body { margin: 0; background: var(--ink); color: var(--fg); font: 16px/1.6 var(--sans); }
      a { color: var(--amber); text-underline-offset: 3px; }
      a:focus-visible { outline: 2px solid var(--amber); outline-offset: 3px; }
      header, main, footer { max-width: 920px; margin: 0 auto; padding: 0 16px; }
      header { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between;
        gap: 8px 20px; padding-top: 20px; padding-bottom: 16px; border-bottom: 1px solid var(--rule); }
      .brand { font: 500 17px var(--mono); color: var(--fg); text-decoration: none; }
      nav { display: flex; flex-wrap: wrap; gap: 6px 18px; font-size: 14px; }
      h1 { font-size: clamp(28px, 5vw, 40px); line-height: 1.15; margin: 28px 0 8px; }
      h2 { font-size: 22px; margin: 36px 0 8px; }
      h3 { font-size: 17px; margin: 0; overflow-wrap: anywhere; }
      .lede { color: var(--fg-2); max-width: 70ch; }
      .note { color: var(--fg-3); font-size: 14px; max-width: 70ch; }
      ol.rows, ul.rows { list-style: none; padding: 0; margin: 16px 0 0; }
      .rows li { padding: 14px 0; border-top: 1px solid var(--rule); }
      .rows p { margin: 4px 0 0; overflow-wrap: anywhere; }
      .meta { font: 13px var(--mono); color: var(--fg-3); }
      .caveat { color: var(--alert); }
      .mark { font: 12px var(--mono); color: var(--fg-3); margin-left: 6px; }
      .more { font-size: 14px; }
      footer { margin-top: 48px; padding-top: 16px; padding-bottom: 40px; border-top: 1px solid var(--rule);
        color: var(--fg-3); font-size: 14px; }
"""


def esc(text: object) -> str:
    return html.escape(str(text), quote=True)


def href(url: object) -> str | None:
    """A row's link, escaped, when it is a web address; None otherwise, so
    nothing but http(s) ever lands in an href."""
    return esc(url) if isinstance(url, str) and re.match(r"https?://", url) else None


def week_of(day: str) -> str:
    """The Monday (UTC) of the week holding `day`, YYYY-MM-DD."""
    date = dt.date.fromisoformat(day)
    return (date - dt.timedelta(days=date.weekday())).isoformat()


def retired_on(row: dict) -> str | None:
    """The day a retired row's notes say it was retired, or None."""
    match = RETIRED_ON.match(str(row.get("notes") or ""))
    if not match:
        return None
    try:
        return dt.date.fromisoformat(match.group(1)).isoformat()
    except ValueError:
        return None


def weeks(catalog: list[dict], retired: list[dict]) -> list[dict]:
    """Every week since the catalogue opened, newest first: the rows first
    seen that week and the rows retired that week, each in sort_key() order,
    and the latest day either records. Rows with no date sit in no week."""
    added: dict[str, list[dict]] = {}
    gone: dict[str, list[dict]] = {}
    days: dict[str, str] = {}
    for row in catalog:
        day = row.get("first_seen")
        if isinstance(day, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", day):
            added.setdefault(week_of(day), []).append(row)
            days[week_of(day)] = max(days.get(week_of(day), day), day)
    for row in retired:
        day = retired_on(row)
        if day:
            gone.setdefault(week_of(day), []).append(row)
            days[week_of(day)] = max(days.get(week_of(day), day), day)
    if not days:
        return []
    opening = min(added) if added else None
    out = []
    for week in sorted(days, reverse=True):
        out.append({
            "week": week,
            "updated": days[week],
            "added": sorted(added.get(week, []), key=query.sort_key),
            "retired": sorted(gone.get(week, []), key=query.sort_key),
            "opening": week == opening,
        })
    return out


def base_of(path: str) -> str:
    """The relative way from a page at `path` back to the site's root."""
    return "../" * path.count("/")


def shell(lang: str, *, path: str, title: str, description: str, body: str,
          alternates: dict[str, str] | None = None) -> str:
    """A whole page: head, header, `body`, footer. `alternates` maps each
    language to the path of this page in it."""
    s = STRINGS[lang]
    base = base_of(path)
    other = LANGS[1 - LANGS.index(lang)]
    head = [
        '<meta charset="utf-8" />',
        '<meta name="viewport" content="width=device-width, initial-scale=1" />',
        f"<title>{esc(title)}</title>",
        f'<meta name="description" content="{esc(description)}" />',
        f'<link rel="canonical" href="{SITE_URL}{path}" />',
    ]
    for code, alt in (alternates or {}).items():
        head.append(f'<link rel="alternate" hreflang="{STRINGS[code]["html_lang"]}" href="{SITE_URL}{alt}" />')
    head += [
        f'<link rel="alternate" type="application/atom+xml" title="{esc(s["feed_title"])}" '
        f'href="{base}{feed_path(lang)}" />',
        '<meta name="color-scheme" content="dark" />',
        '<meta name="theme-color" content="#0b0d10" />',
        f'<link rel="icon" href="{base}favicon.svg" type="image/svg+xml" />',
        f'<link rel="stylesheet" href="{base}fonts/fonts.css" />',
        f"<style>{CSS}    </style>",
    ]
    switch = (
        f'<a href="{base}{(alternates or {})[other]}" hreflang="{STRINGS[other]["html_lang"]}" '
        f'lang="{STRINGS[other]["html_lang"]}">{esc(s["other"])}</a>'
        if alternates and other in alternates else ""
    )
    nav = [
        f'<a href="{base}{app_link(lang)}">{esc(s["app"])}</a>',
        f'<a href="{base}{PATTERN_DIR}/">{esc(s["patterns"])}</a>',
        f'<a href="{base}{new_path(lang)}">{esc(s["new"])}</a>',
        f'<a href="{base}{feed_path(lang)}">{esc(s["feed"])}</a>',
        f'<a href="{REPOSITORY}">{esc(s["github"])} ↗</a>',
    ] + ([switch] if switch else [])
    return "\n".join([
        "<!doctype html>",
        f'<html lang="{s["html_lang"]}">',
        "  <head>",
        *(f"    {line}" for line in head),
        "  </head>",
        "  <body>",
        "    <header>",
        f'      <a class="brand" href="{base}{app_link(lang)}">{esc(s["brand"])}</a>',
        f'      <nav aria-label="awesome-jev">{" ".join(nav)}</nav>',
        "    </header>",
        "    <main>",
        body,
        "    </main>",
        f"    <footer><p>{esc(s['disclaimer'])}</p></footer>",
        "  </body>",
        "</html>",
        "",
    ])


def app_link(lang: str, query_string: str = "") -> str:
    """The app, in `lang`, with filters (relative to the site's root)."""
    params = "&".join(p for p in (query_string, f"lang={lang}") if p)
    return f"?{params}"


def pattern_path(key: str, lang: str) -> str:
    return f"{PATTERN_DIR}/{key}.html" if lang == "en" else f"{PATTERN_DIR}/{key}.zh.html"


def new_path(lang: str) -> str:
    return "new.html" if lang == "en" else "new.zh.html"


def feed_path(lang: str) -> str:
    return "feed.xml" if lang == "en" else "feed.zh.xml"


class Labels:
    """taxonomy.json's names for kinds, flags and summary sources."""

    def __init__(self, taxonomy: dict):
        self.by = {
            group: {item["key"]: item for item in taxonomy.get(group, [])}
            for group in ("kinds", "flags", "summary_sources")
        }

    def name(self, group: str, key: str, lang: str) -> str:
        item = self.by[group].get(key)
        return item[lang] if item and item.get(lang) else key


def row_html(row: dict, lang: str, labels: Labels, base: str, *, depth: str = "      ") -> str:
    """One row as a list item: its link, what the catalogue records about it,
    its summary in `lang` with the marks the site gives it, and its permalink."""
    s = STRINGS[lang]
    slug = esc(row["slug"])
    link = href(row.get("url"))
    title = esc(row["title"])
    heading = f'<a href="{link}" rel="noopener">{title}</a>' if link else title
    meta = [esc(labels.name("kinds", row.get("kind", ""), lang))]
    if row.get("official"):
        meta.append(esc(s["official"]))
    if isinstance(row.get("stars"), int):
        meta.append(esc(s["stars"].format(n=f"{row['stars']:,}")))
    if row.get("languages"):
        meta.append(esc(s["list_sep"].join(str(x) for x in row["languages"])))
    for flag in row.get("flags") or []:
        css = ' class="caveat"' if flag in query.DISQUALIFYING else ""
        meta.append(f"<span{css}>{esc(labels.name('flags', flag, lang))}</span>")
    summary = row.get("summary_zh") if lang == "zh" and row.get("summary_zh") else row.get("summary", "")
    marks = []
    if row.get("summary_source") in MARKED_SOURCES:
        marks.append(labels.name("summary_sources", row["summary_source"], lang))
    if lang == "zh" and row.get("zh_machine") is True:
        marks.append("机翻")
    marked = "".join(f'<span class="mark">{esc(m)}</span>' for m in marks)
    return "\n".join([
        f'{depth}<li id="{slug}">',
        f"{depth}  <h3>{heading}</h3>",
        f'{depth}  <p class="meta">{s["sep"].join(meta)}</p>',
        f"{depth}  <p>{esc(summary)}{marked}</p>",
        f'{depth}  <p class="more"><a href="{base}{app_link(lang)}#{slug}">{esc(s["in_app"])}</a></p>',
        f"{depth}</li>",
    ])


def pattern_page(pattern: dict, catalog: list[dict], lang: str, labels: Labels) -> str:
    key = pattern["key"]
    s = STRINGS[lang]
    path = pattern_path(key, lang)
    base = base_of(path)
    rows = sorted((e for e in catalog if key in e.get("patterns", [])), key=query.sort_key)
    indexed = [e for e in rows if not _stats.not_indexed_by_pattern(e)]
    later = [e for e in rows if _stats.not_indexed_by_pattern(e)]
    name = pattern[lang]
    flags = s["or"].join(s["quote"].format(labels.name("flags", f, lang)) for f in sorted(query.DISQUALIFYING))
    body = [
        f"      <h1>{esc(name)}</h1>",
        f'      <p class="lede">{esc(pattern["blurb_" + lang])}</p>',
        "      <p>" + esc(s["pattern_lede"].format(n=len(rows), code=sum(1 for e in rows if e.get("has_code")))) + "</p>",
        f'      <p><a href="{base}{esc(app_link(lang, "p=" + key))}">{esc(s["open_in_app"])} →</a></p>',
        f'      <p class="note">{esc(s["caveat_note"].format(flags=flags))}</p>',
        '      <ol class="rows">',
        *(row_html(e, lang, labels, base) for e in indexed),
        "      </ol>",
    ]
    if later:
        body += [
            f"      <h2>{esc(s['unindexed'])}</h2>",
            f'      <p class="note">{esc(s["unindexed_note"])}</p>',
            '      <ol class="rows">',
            *(row_html(e, lang, labels, base) for e in later),
            "      </ol>",
        ]
    return shell(
        lang, path=path, title=s["pattern_title"].format(name=name),
        description=pattern["blurb_" + lang], body="\n".join(body),
        alternates={code: pattern_path(key, code) for code in LANGS},
    )


def patterns_index(patterns: list[dict], catalog: list[dict]) -> str:
    """Both languages on one page: the pages it links are per language."""
    path = f"{PATTERN_DIR}/index.html"
    en, zh = STRINGS["en"], STRINGS["zh"]
    items = []
    for p in patterns:
        n = sum(1 for e in catalog if p["key"] in e.get("patterns", []))
        items += [
            "        <li>",
            f'          <h3><a href="{p["key"]}.html">{esc(p["en"])}</a> · '
            f'<a href="{p["key"]}.zh.html" lang="zh-CN" hreflang="zh-CN">{esc(p["zh"])}</a></h3>',
            f'          <p class="meta">{esc(en["rows"].format(n=n))}</p>',
            f'          <p>{esc(p["blurb_en"])}</p>',
            f'          <p lang="zh-CN">{esc(p["blurb_zh"])}</p>',
            "        </li>",
        ]
    body = [
        f"      <h1>{esc(en['patterns'])} · <span lang=\"zh-CN\">{esc(zh['patterns'])}</span></h1>",
        f'      <p class="lede">{esc(en["index_lede"])}</p>',
        f'      <p class="lede" lang="zh-CN">{esc(zh["index_lede"])}</p>',
        '      <ul class="rows">',
        *items,
        "      </ul>",
    ]
    return shell("en", path=path, title=en["index_title"], description=en["index_lede"], body="\n".join(body))


def week_counts(week: dict, lang: str) -> str:
    """What a week holds, in a line: the week the catalogue opened is counted
    as its opening, its rows not listed."""
    s = STRINGS[lang]
    if week["opening"]:
        opened = s["opened"].format(n=len(week["added"]))
        return opened + (s["list_sep"] + s["week_counts"].format(added=0, retired=len(week["retired"]))
                         if week["retired"] else "")
    return s["week_counts"].format(added=len(week["added"]), retired=len(week["retired"]))


def week_html(week: dict, lang: str, labels: Labels, base: str) -> list[str]:
    s = STRINGS[lang]
    lines = [
        f'      <h2 id="w{week["week"]}">{esc(s["week"].format(date=week["week"]))}</h2>',
        f'      <p class="meta">{esc(week_counts(week, lang))}</p>',
    ]
    if week["added"] and not week["opening"]:
        lines += [f"      <h3>{esc(s['added'])}</h3>", '      <ol class="rows">']
        lines += [row_html(e, lang, labels, base) for e in week["added"]]
        lines.append("      </ol>")
    if week["retired"]:
        lines += [f"      <h3>{esc(s['retired'])}</h3>", '      <ul class="rows">']
        for row in week["retired"]:
            notes = row.get("notes_zh") if lang == "zh" and row.get("notes_zh") else row.get("notes", "")
            lines += [
                f'        <li id="{esc(row["slug"])}">',
                f"          <h3>{esc(row['title'])}</h3>",
                f"          <p>{esc(notes)}</p>",
                "        </li>",
            ]
        lines.append("      </ul>")
    return lines


def new_page(all_weeks: list[dict], lang: str, labels: Labels) -> str:
    s = STRINGS[lang]
    path = new_path(lang)
    body = [
        f"      <h1>{esc(s['new'])}</h1>",
        f'      <p class="lede">{esc(s["new_lede"])} <a href="{feed_path(lang)}">{esc(s["feed"])}</a></p>',
    ]
    for week in all_weeks[:WEEKS_SHOWN]:
        body += week_html(week, lang, labels, "")
    if not all_weeks:
        body.append(f"      <p>{esc(s['nothing'])}</p>")
    return shell(
        lang, path=path, title=s["new_title"], description=s["new_lede"], body="\n".join(body),
        alternates={code: new_path(code) for code in LANGS},
    )


def stamp(day: str) -> str:
    return f"{day}T00:00:00Z"


def feed(all_weeks: list[dict], lang: str, labels: Labels, *, entry_rows: int = 100) -> str:
    """An Atom feed: one entry per week, linking that week on the page. An
    entry lists at most `entry_rows` added rows; the page lists them all."""
    s = STRINGS[lang]
    page = SITE_URL + new_path(lang)
    shown = all_weeks[:WEEKS_SHOWN]
    lines = [
        '<?xml version="1.0" encoding="utf-8"?>',
        f'<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="{s["html_lang"]}">',
        f"  <title>{esc(s['feed_title'])}</title>",
        f"  <subtitle>{esc(s['feed_subtitle'])}</subtitle>",
        f"  <id>{SITE_URL}{feed_path(lang)}</id>",
        f'  <link rel="self" type="application/atom+xml" href="{SITE_URL}{feed_path(lang)}" />',
        f'  <link rel="alternate" type="text/html" href="{page}" />',
        # An empty catalogue (tests only) has no date of its own.
        f"  <updated>{stamp(max((w['updated'] for w in shown), default='1970-01-01'))}</updated>",
        f"  <author><name>awesome-jev</name><uri>{REPOSITORY}</uri></author>",
    ]
    for week in shown:
        title = s["week"].format(date=week["week"]) + s["colon"] + week_counts(week, lang)
        if week["opening"]:
            content = []
        else:
            content = [f"<h3>{esc(s['added'])}</h3><ul>"] if week["added"] else []
            for row in week["added"][:entry_rows]:
                link = href(row.get("url"))
                summary = row.get("summary_zh") if lang == "zh" and row.get("summary_zh") else row.get("summary", "")
                name = f'<a href="{link}">{esc(row["title"])}</a>' if link else esc(row["title"])
                content.append(f"<li>{name}: {esc(summary)}</li>")
            if week["added"]:
                content.append("</ul>")
                if len(week["added"]) > entry_rows:
                    content.append(f"<p>{esc(s['more'].format(n=len(week['added']) - entry_rows))}</p>")
        if week["retired"]:
            content.append(f"<h3>{esc(s['retired'])}</h3><ul>")
            content += [f"<li>{esc(row['title'])}</li>" for row in week["retired"]]
            content.append("</ul>")
        anchor = f"{page}#w{week['week']}"
        lines += [
            "  <entry>",
            f"    <title>{esc(title)}</title>",
            f"    <id>{anchor}</id>",
            f'    <link rel="alternate" type="text/html" href="{anchor}" />',
            f"    <updated>{stamp(week['updated'])}</updated>",
            f'    <content type="html">{esc("".join(content))}</content>',
            "  </entry>",
        ]
    return "\n".join(lines + ["</feed>", ""])


def sitemap(paths: list[str]) -> str:
    urls = "\n".join(f"  <url><loc>{esc(SITE_URL + path)}</loc></url>" for path in paths)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n</urlset>\n"
    )


def pages(catalog: list[dict], retired: list[dict], patterns: list[dict], taxonomy: dict) -> dict[str, str]:
    """Every file this module writes: path relative to site/ → text."""
    labels = Labels(taxonomy)
    all_weeks = weeks(catalog, retired)
    files: dict[str, str] = {f"{PATTERN_DIR}/index.html": patterns_index(patterns, catalog)}
    for pattern in patterns:
        for lang in LANGS:
            files[pattern_path(pattern["key"], lang)] = pattern_page(pattern, catalog, lang, labels)
    for lang in LANGS:
        files[new_path(lang)] = new_page(all_weeks, lang, labels)
        files[feed_path(lang)] = feed(all_weeks, lang, labels)
    listed = [""] + [f"{PATTERN_DIR}/"] + [
        path for path in files if path.endswith(".html") and path != f"{PATTERN_DIR}/index.html"
    ]
    files["sitemap.xml"] = sitemap(listed)
    return files


# The files and the one directory pages() writes, so a rewrite can clear them.
TOP_FILES = ("new.html", "new.zh.html", "feed.xml", "feed.zh.xml", "sitemap.xml")


def write_pages(site: pathlib.Path, files: dict[str, str]) -> None:
    """Replace site/patterns/ and the top-level files with `files`, so a
    pattern that left patterns.json leaves no page behind."""
    shutil.rmtree(site / PATTERN_DIR, ignore_errors=True)
    for name in TOP_FILES:
        (site / name).unlink(missing_ok=True)
    for rel, text in files.items():
        path = site / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def page_problems(site: pathlib.Path, files: dict[str, str]) -> list[str]:
    """Why the pages under site/ are not what a rebuild writes, or []."""
    problems = []
    found = {p.relative_to(site).as_posix() for p in (site / PATTERN_DIR).rglob("*") if p.is_file()} \
        if (site / PATTERN_DIR).is_dir() else set()
    found |= {name for name in TOP_FILES if (site / name).is_file()}
    for rel in sorted(set(files) - found):
        problems.append(f"site/{rel} is missing; run assemble_site.py")
    for rel in sorted(found - set(files)):
        problems.append(f"site/{rel} is no page a rebuild writes; run assemble_site.py, which rewrites them whole")
    for rel in sorted(set(files) & found):
        if (site / rel).read_text(encoding="utf-8") != files[rel]:
            problems.append(f"site/{rel} is stale: a rebuild from the published files differs; run assemble_site.py")
    return problems
