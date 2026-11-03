#!/usr/bin/env python3
"""The launch board's plain pages (docs/launches.md; P1 of the 2026-11-03 plan):
one page per product, one per maker, and the board itself.

  products/<slug>.html       a catalogued product: what Jev decides in it, the
                             evidence the catalogue records and who read it,
                             its launches, its makers, other products filed
                             under the same pattern. English and Chinese on one
                             page, as patterns/index.html is.
  makers/index.html          every maker with a product
  makers/<login>.html        one maker's products and launches (login in lower case)
  launches.html, .zh.html    the board: the week running, the last week closed,
                             next week's launches, the past weeks, and the
                             products new this week
  weeks/<week>.html, .zh.html  a closed week's ranking, and the launches
                             removed from it with their reasons (L15)
  badges/<slug>.svg          a product's latest badge, for its README (L13)

A product is a row scripts/launches.py is_product() admits: a project, plugin,
SDK or integration with code that is an example of deciding with Jev. Every
rule the pages show (evidence tier, quiet rows, who a maker is, how a week is
ranked) is read from launches.py, so a page cannot say something the rules do
not.

site_pages.py writes these beside its own pages and holds them to the same
promises: no script, nothing loaded from another host, every word of a row's
escaped, and no date but the data's own, so two builds of the same files write
the same bytes.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import launches  # noqa: E402
import site_pages as sp  # noqa: E402
from evidence_url import evidence_url  # noqa: E402
from site_api import query  # noqa: E402

PRODUCT_DIR = "products"
MAKER_DIR = "makers"
WEEK_DIR = "weeks"
BADGE_DIR = "badges"
HOW_TO_LAUNCH = f"{sp.REPOSITORY}/blob/main/docs/launches.md"
LAUNCH_ISSUE = f"{sp.REPOSITORY}/issues/new?template=launch.yml"
DISCUSSION = f"{sp.REPOSITORY}/discussions/{{n}}"
# How many products a "same pattern" list shows, and a maker list per maker.
SAME_PATTERN = 5
# How many hunters the board lists (L21).
HUNTERS = 10

# Both languages: a product or maker page carries the two side by side.
WORDS = {
    "decides": ("What Jev decides here", "Jev 在这里做什么决定"),
    "patterns": ("Decision patterns", "决策模式"),
    "primitives": ("Primitives", "原语"),
    "evidence": ("Evidence", "证据"),
    "summary": ("Summary", "摘要"),
    "notes": ("Notes", "备注"),
    "launches": ("Launches", "发布记录"),
    "makers": ("Makers", "Maker"),
    "same": ("Also under this pattern", "同一模式的其他产品"),
    "links": ("Links", "链接"),
    "project": ("Project", "项目"),
    "demo": ("Try it", "在线试用"),
    "in_app": ("In the catalogue", "在目录中查看"),
    "cited": ("Cited file", "引用的文件"),
    "not_launched": ("Not launched yet.", "还没有发布过。"),
    "how": ("How a product launches", "怎样发布一个产品"),
    "launch_it": ("Launch it", "发布它"),
    "none_read": ("No reading of its primitives is recorded.", "没有记录原语的阅读结果。"),
    "seen": ("text signal only: the cited file contains their request or answer shape",
             "仅文本信号：引用的文件里出现了它们的请求或回答格式"),
    "read_person": ("read in the code by a person", "由人在代码里读到"),
    "read_model": ("read in the code by a model, not yet by a person", "由模型在代码里读到，尚无人复核"),
    "rank": ("#{rank} of the week · {votes} votes, {counted} counted", "当周第 {rank} 名 · {votes} 票，计 {counted} 票"),
    "open_week": ("on the board this week; counts are shown when the week closes",
                  "本周在榜；票数在收榜后公布"),
    "next_week": ("on the board next week", "下周上榜"),
    "products_by": ("Products", "产品"),
    "no_profile": ("Built from the catalogue; this maker has not added a profile.",
                   "根据目录生成；这位 Maker 还没有添加自我介绍。"),
    "makers_title": ("Makers · awesome-jev", "Maker · awesome-jev"),
    "makers_lede": ("Everyone with a Jev product in the catalogue, by GitHub login. A page lists what the catalogue "
                    "records; a maker can add a line about themselves with a pull request.",
                    "目录里每位有 Jev 产品的 Maker，按 GitHub 登录名排列。页面只列目录记录的内容；"
                    "Maker 可以提一个 pull request 加上自我介绍。"),
}

TIER_WORDS = {
    "person": ("a person read the call site", "有人读过调用点"),
    "model": ("a model read the call site; no person yet", "模型读过调用点，尚无人复核"),
    "file": ("a script found Jev's request or answer in the cited file; nobody has read it",
             "脚本在引用的文件里找到了 Jev 的请求或回答，还没有人读过"),
    "none": ("no file cited", "没有引用文件"),
}

# The board, per language.
BOARD = {
    "en": {
        "title": "Launches · awesome-jev",
        "h1": "Launches",
        "lede": "Products built on Jev, launched by their makers once a week. People vote with a thumbs-up on "
                "each launch's GitHub Discussion; the week closes on Sunday at 23:59 UTC. Votes say how many "
                "people cared. The evidence next to each launch says whether the product calls Jev and who read "
                "the code. The two are never added together, and a rank is not this catalogue's recommendation.",
        "how": "How to launch a product",
        "running": "This week: {week}",
        "running_note": "In a shuffled order, without counts, until the week closes.",
        "closed": "Last week: {week}",
        "votes": "{votes} votes, {counted} counted",
        "no_launch": "No launch has opened yet. The first week opens once launch posts can be voted on.",
        "new": "New in the catalogue: {week}",
        "new_note": "Products that entered the catalogue this week, in the order of what it records: who read the "
                    "call site, then stars. An order, not a ranking. Their makers can launch them.",
        "nothing_new": "Nothing new this week.",
        "vote": "Vote",
        "page": "Product page",
        "evidence": "Evidence",
        "next": "Next week: {week}",
        "next_note": "Launches accepted for next week, in no particular order. Their vote posts open on Monday {monday}.",
        "past": "Past weeks",
        "past_item": "{week}: {n} launches, closed {closed}",
        "week_title": "Launches of {week} · awesome-jev",
        "week_h1": "Launches of {week}",
        "week_lede": "Monday {monday} to Sunday {sunday} (UTC), closed on {closed} and counted under rules {rules}. "
                     "A rank is a count of votes, not this catalogue's recommendation; the evidence beside each "
                     "launch is the catalogue's own record.",
        "removed": "Removed from this week",
        "removed_note": "Taken off the board, with the reason kept in the week's file.",
        "board": "The board",
        "badge": "Badge for a README",
        "hunters": "Hunters",
        "hunters_note": "People who put someone else's product on the board, by how many of those launches ran a "
                        "closed week, then how many placed in its top three. Thanks, not a score.",
        "hunter_item": "{n} launched, {top} in a top three",
    },
    "zh": {
        "title": "发布榜 · awesome-jev",
        "h1": "发布榜",
        "lede": "基于 Jev 做出来的产品，由 Maker 每周发布一次。大家在每个 Launch 的 GitHub Discussion 上点赞投票，"
                "每周日 23:59 UTC 收榜。票数说明有多少人关心；每个 Launch 旁边的证据说明产品是否真的调用 Jev、"
                "谁读过代码。两者从不相加，名次也不是本目录的推荐。",
        "how": "怎样发布一个产品",
        "running": "本周：{week}",
        "running_note": "收榜前按随机顺序展示，不显示票数。",
        "closed": "上周：{week}",
        "votes": "{votes} 票，计 {counted} 票",
        "no_launch": "还没有开榜。Launch 的投票帖可以投票之后，第一周就会开榜。",
        "new": "本周新收录：{week}",
        "new_note": "本周进入目录的产品，按目录记录的内容排序：先看谁读过调用点，再看星标。这是排序，不是排名。"
                    "它们的 Maker 可以发布它们。",
        "nothing_new": "本周没有新产品。",
        "vote": "投票",
        "page": "产品页",
        "evidence": "证据",
        "next": "下周：{week}",
        "next_note": "已接受、下周上榜的 Launch，不分先后。投票帖在 {monday}（周一）开放。",
        "past": "往期",
        "past_item": "{week}：{n} 个 Launch，{closed} 收榜",
        "week_title": "{week} 发布榜 · awesome-jev",
        "week_h1": "{week} 发布榜",
        "week_lede": "{monday}（周一）至 {sunday}（周日，UTC），{closed} 收榜，按规则 {rules} 计票。"
                     "名次只是票数的排序，不是本目录的推荐；每个 Launch 旁的证据来自目录自己的记录。",
        "removed": "本周下榜",
        "removed_note": "从榜上撤下的 Launch，原因留在当周的文件里。",
        "board": "发布榜",
        "badge": "README 徽章",
        "hunters": "Hunter",
        "hunters_note": "把别人的产品带上榜的人，按他们发布、并跑完一周的 Launch 数排序，再看其中进过前三的数。"
                        "这是致谢，不是评分。",
        "hunter_item": "发布 {n} 个，{top} 个进过前三",
    },
}


def esc(text: object) -> str:
    return sp.esc(text)


def product_path(slug: str) -> str:
    return f"{PRODUCT_DIR}/{slug}.html"


def maker_path(login: str) -> str:
    return f"{MAKER_DIR}/{launches.login_key(login)}.html"


def launches_path(lang: str) -> str:
    return sp.launches_path(lang)


def week_path(week: str, lang: str) -> str:
    return f"{WEEK_DIR}/{week}.html" if lang == "en" else f"{WEEK_DIR}/{week}.zh.html"


def badge_path(slug: str) -> str:
    return f"{BADGE_DIR}/{slug}.svg"


def both(key: str, sep: str = " · ") -> str:
    """A heading in both languages, the Chinese marked as such."""
    en, zh = WORDS[key]
    return f'{esc(en)}{sep}<span lang="zh-CN">{esc(zh)}</span>'


def pair(en: str, zh: str, tag: str = "p", cls: str = "") -> list[str]:
    """The same text in English and in Chinese, as two elements."""
    attr = f' class="{cls}"' if cls else ""
    out = [f"      <{tag}{attr}>{esc(en)}</{tag}>"]
    if zh:
        out.append(f'      <{tag}{attr} lang="zh-CN">{esc(zh)}</{tag}>')
    return out


def tier_html(row: dict, lang: str | None = None) -> str:
    """The evidence tier as a short marked span; both languages unless `lang`."""
    name = launches.tier(row)
    en, zh = TIER_WORDS[name]
    cls = "caveat" if name in ("none",) else "mark"
    if lang == "en":
        return f'<span class="{cls}">{esc(en)}</span>'
    if lang == "zh":
        return f'<span class="{cls}">{esc(zh)}</span>'
    return f'<span class="{cls}">{esc(en)}</span> <span class="{cls}" lang="zh-CN">{esc(zh)}</span>'


def meta_line(row: dict, labels: sp.Labels, lang: str) -> str:
    s = sp.STRINGS[lang]
    meta = [esc(labels.name("kinds", row.get("kind", ""), lang))]
    if row.get("official"):
        meta.append(esc(s["official"]))
    if isinstance(row.get("stars"), int):
        meta.append(esc(s["stars"].format(n=f"{row['stars']:,}")))
    if row.get("languages"):
        meta.append(esc(s["list_sep"].join(str(x) for x in row["languages"])))
    if row.get("repo_license"):
        meta.append(esc(row["repo_license"]))
    for flag in row.get("flags") or []:
        css = ' class="caveat"' if flag in query.DISQUALIFYING else ""
        meta.append(f"<span{css}>{esc(labels.name('flags', flag, lang))}</span>")
    return s["sep"].join(meta)


def marks(row: dict, labels: sp.Labels, lang: str) -> str:
    found = []
    if row.get("summary_source") in sp.MARKED_SOURCES:
        found.append(labels.name("summary_sources", row["summary_source"], lang))
    if lang == "zh" and row.get("zh_machine") is True:
        found.append("机翻")
    return "".join(f'<span class="mark">{esc(m)}</span>' for m in found)


def launch_line(week: str, launch: dict, weeks_by_id: dict[str, dict]) -> str:
    """One launch of a product: its week and, once closed, its rank and votes."""
    status = (weeks_by_id.get(week) or {}).get("status")
    result = launch.get("result")
    label = esc(week)
    if status == "closed" and result:
        en = WORDS["rank"][0].format(rank=result["rank"], votes=result["votes"], counted=result["counted"])
        zh = WORDS["rank"][1].format(rank=result["rank"], votes=result["votes"], counted=result["counted"])
        label = f'<a href="../{esc(week_path(week, "en"))}">{esc(week)}</a>'
    elif status == "scheduled":
        en, zh = WORDS["next_week"]
    else:
        en, zh = WORDS["open_week"]
    link = (f' · <a href="{esc(DISCUSSION.format(n=launch["discussion"]))}" rel="noopener">GitHub</a>'
            if isinstance(launch.get("discussion"), int) else "")
    return f'{label}: {esc(en)} <span lang="zh-CN">{esc(zh)}</span>{link}'


def same_pattern(row: dict, products: list[dict]) -> list[dict]:
    """Up to SAME_PATTERN other products under the row's first pattern that is
    not overview, in the catalogue's order."""
    key = next((p for p in row.get("patterns") or [] if p != "overview"), None)
    if key is None:
        return []
    others = [r for r in products if r["slug"] != row["slug"] and key in (r.get("patterns") or [])]
    return sorted(others, key=query.sort_key)[:SAME_PATTERN]


def product_page(row: dict, *, products: list[dict], patterns: dict[str, dict], labels: sp.Labels,
                 history: dict[str, list[tuple[str, dict]]], weeks_by_id: dict[str, dict]) -> str:
    path = product_path(row["slug"])
    base = sp.base_of(path)
    title = row["title"]
    body = [f"      <h1>{esc(title)}</h1>"]
    if row.get("tagline"):
        body += pair(row["tagline"], row.get("tagline_zh", ""), cls="lede")
    body.append(f'      <p class="meta">{meta_line(row, labels, "en")}</p>')

    links = []
    url = sp.href(row.get("url"))
    if url:
        links.append(f'<a href="{url}" rel="noopener">{both("project", " / ")}</a>')
    demo = sp.href(row.get("demo_url"))
    if demo:
        links.append(f'<a href="{demo}" rel="noopener">{both("demo", " / ")}</a>')
    links.append(f'<a href="{base}{esc(sp.app_link("en"))}#{esc(row["slug"])}">{both("in_app", " / ")}</a>')
    body.append(f'      <p>{" · ".join(links)}</p>')

    body.append(f"      <h2>{both('decides')}</h2>")
    names = []
    for key in row.get("patterns") or []:
        pattern = patterns.get(key)
        if pattern:
            names.append(
                f'<a href="{base}{sp.pattern_path(key, "en")}">{esc(pattern["en"])}</a> '
                f'(<a href="{base}{sp.pattern_path(key, "zh")}" lang="zh-CN" hreflang="zh-CN">{esc(pattern["zh"])}</a>)'
            )
    body.append(f'      <p><span class="meta">{both("patterns", " / ")}</span><br />{", ".join(names) or "—"}</p>')
    if row.get("question_types"):
        who = query.primitives_read_by(row)
        en, zh = WORDS["read_person"] if who == query.PERSON else WORDS["read_model"]
        prims = ", ".join(esc(x) for x in row["question_types"])
        body.append(f'      <p><span class="meta">{both("primitives", " / ")}</span><br />{prims}: '
                    f'{esc(en)} <span lang="zh-CN">{esc(zh)}</span></p>')
    elif row.get("primitives_seen"):
        en, zh = WORDS["seen"]
        prims = ", ".join(esc(x) for x in row["primitives_seen"])
        body.append(f'      <p><span class="meta">{both("primitives", " / ")}</span><br />{prims}: '
                    f'{esc(en)} <span lang="zh-CN">{esc(zh)}</span></p>')
    else:
        en, zh = WORDS["none_read"]
        body.append(f'      <p><span class="meta">{both("primitives", " / ")}</span><br />{esc(en)} '
                    f'<span lang="zh-CN">{esc(zh)}</span></p>')
    evidence = [tier_html(row)]
    reading = query.reading(row.get("evidence"))
    if reading:
        evidence.append(f'<span class="meta">{esc(reading[1])}</span>')
    cited = sp.href(evidence_url(row))
    if cited:
        path_text = (row.get("evidence") or {}).get("path", "")
        evidence.append(f'<a href="{cited}" rel="noopener">{both("cited", " / ")}: <code>{esc(path_text)}</code></a>')
    body.append(f'      <p><span class="meta">{both("evidence", " / ")}</span><br />{" · ".join(evidence)}</p>')

    body.append(f"      <h2>{both('summary')}</h2>")
    body.append(f'      <p>{esc(row.get("summary", ""))}{marks(row, labels, "en")}</p>')
    if row.get("summary_zh"):
        body.append(f'      <p lang="zh-CN">{esc(row["summary_zh"])}{marks(row, labels, "zh")}</p>')
    if row.get("notes"):
        body.append(f"      <h2>{both('notes')}</h2>")
        body += pair(row["notes"], row.get("notes_zh", ""), cls="note")

    body.append(f"      <h2>{both('launches')}</h2>")
    mine = history.get(row["slug"], [])
    if mine:
        body.append('      <ul class="rows">')
        body += [f"        <li>{launch_line(week, launch, weeks_by_id)}</li>" for week, launch in reversed(mine)]
        body.append("      </ul>")
    else:
        en, zh = WORDS["not_launched"]
        body.append(f'      <p>{esc(en)} <span lang="zh-CN">{esc(zh)}</span> '
                    f'<a href="{esc(HOW_TO_LAUNCH)}" rel="noopener">{both("how", " / ")}</a></p>')

    logins = launches.makers_of(row)
    if logins:
        body.append(f"      <h2>{both('makers')}</h2>")
        body.append("      <p>" + ", ".join(
            f'<a href="{base}{esc(maker_path(login))}">{esc(login)}</a>' for login in logins) + "</p>")

    others = same_pattern(row, products)
    if others:
        body.append(f"      <h2>{both('same')}</h2>")
        body.append('      <ul class="rows">')
        for other in others:
            body.append(
                f'        <li><h3><a href="{esc(other["slug"])}.html">{esc(other["title"])}</a></h3>'
                f'<p>{esc(other.get("summary", ""))}</p></li>'
            )
        body.append("      </ul>")

    description = row.get("tagline") or row.get("summary", "")
    return sp.shell("en", path=path, title=f"{title} · awesome-jev", description=description, body="\n".join(body))


def maker_page(login: str, rows: list[dict], *, profile: dict | None, labels: sp.Labels,
               history: dict[str, list[tuple[str, dict]]], weeks_by_id: dict[str, dict]) -> str:
    path = maker_path(login)
    base = sp.base_of(path)
    name = (profile or {}).get("name") or login
    body = [f"      <h1>{esc(name)}</h1>"]
    body.append(f'      <p class="meta"><a href="https://github.com/{esc(login)}" rel="noopener">github.com/{esc(login)}</a>'
                + (f' · <a href="{sp.href(profile["url"])}" rel="noopener">{esc(profile["url"])}</a>'
                   if profile and sp.href(profile.get("url")) else "") + "</p>")
    if profile and profile.get("bio"):
        body += pair(profile["bio"], profile.get("bio_zh", ""), cls="lede")
    else:
        en, zh = WORDS["no_profile"]
        body += pair(en, zh, cls="note")
    body.append(f"      <h2>{both('products_by')}</h2>")
    body.append('      <ul class="rows">')
    for row in sorted(rows, key=query.sort_key):
        body.append(f'        <li id="{esc(row["slug"])}">')
        body.append(f'          <h3><a href="{base}{esc(product_path(row["slug"]))}">{esc(row["title"])}</a></h3>')
        body.append(f'          <p class="meta">{meta_line(row, labels, "en")} · {tier_html(row, "en")}</p>')
        body.append(f'          <p>{esc(row.get("tagline") or row.get("summary", ""))}</p>')
        for week, launch in reversed(history.get(row["slug"], [])):
            body.append(f'          <p class="meta">{launch_line(week, launch, weeks_by_id)}</p>')
        body.append("        </li>")
    body.append("      </ul>")
    return sp.shell("en", path=path, title=f"{name} · awesome-jev", description=f"{name}: Jev products", body="\n".join(body))


def makers_index(by_login: dict[str, list[dict]], profiles: dict[str, dict]) -> str:
    path = f"{MAKER_DIR}/index.html"
    en, zh = WORDS["makers_lede"]
    body = [f"      <h1>{both('makers')}</h1>", *pair(en, zh, cls="lede"), '      <ul class="rows">']
    for key in sorted(by_login):
        rows = by_login[key]
        login = launches.makers_of(rows[0])
        shown = next((x for x in login if launches.login_key(x) == key), key)
        name = (profiles.get(key) or {}).get("name") or shown
        titles = ", ".join(esc(r["title"]) for r in sorted(rows, key=query.sort_key))
        body.append(f'        <li><h3><a href="{esc(launches.login_key(key))}.html">{esc(name)}</a></h3>'
                    f'<p class="meta">{titles}</p></li>')
    body.append("      </ul>")
    return sp.shell("en", path=path, title=WORDS["makers_title"][0], description=en, body="\n".join(body))


def board_item(launch: dict, row: dict, lang: str, *, result: dict | None, base: str = "") -> list[str]:
    """One launch on a board list. `base` leads every link to the site's root
    ("../" from a week page)."""
    b = BOARD[lang]
    tagline = launch.get("tagline_zh") if lang == "zh" and launch.get("tagline_zh") else launch.get("tagline", "")
    meta = []
    if result:
        meta.append(f"#{result['rank']}")
        meta.append(esc(b["votes"].format(votes=result["votes"], counted=result["counted"])))
    meta.append(f'{esc(b["evidence"])}: {tier_html(row, lang)}')
    links = [f'<a href="{esc(base + product_path(row["slug"]))}">{esc(b["page"])}</a>']
    if result and result.get("badges"):
        links.append(f'<a href="{esc(base + badge_path(row["slug"]))}">{esc(b["badge"])}</a>')
    if isinstance(launch.get("discussion"), int) and not result:
        links.append(f'<a href="{esc(DISCUSSION.format(n=launch["discussion"]))}" rel="noopener">{esc(b["vote"])} ↗</a>')
    return [
        f'        <li id="{esc(row["slug"])}">',
        f'          <h3><a href="{esc(base + product_path(row["slug"]))}">{esc(row["title"])}</a></h3>',
        f"          <p>{esc(tagline)}</p>",
        f'          <p class="meta">{" · ".join(meta)}</p>',
        f'          <p class="more">{" · ".join(links)}</p>',
        "        </li>",
    ]


def board_page(lang: str, *, catalog: list[dict], rows: dict[str, dict], all_weeks: list[dict],
               labels: sp.Labels) -> str:
    b = BOARD[lang]
    path = launches_path(lang)
    body = [
        f"      <h1>{esc(b['h1'])}</h1>",
        f'      <p class="lede">{esc(b["lede"])}</p>',
        f'      <p><a href="{esc(HOW_TO_LAUNCH)}" rel="noopener">{esc(b["how"])} ↗</a></p>',
    ]
    running = next((w for w in reversed(all_weeks) if w.get("status") == "open"), None)
    closed = next((w for w in reversed(all_weeks) if w.get("status") == "closed"), None)
    if running:
        on = [x for x in running.get("launches") or [] if x.get("status") == "scheduled" and x["product"] in rows]
        body += [f"      <h2>{esc(b['running'].format(week=running['week']))}</h2>",
                 f'      <p class="note">{esc(b["running_note"])}</p>', '      <ol class="rows">']
        for launch in launches.shuffled(on, running["week"]):
            body += board_item(launch, rows[launch["product"]], lang, result=None)
        body.append("      </ol>")
    if closed:
        on = [x for x in closed.get("launches") or [] if x.get("status") == "scheduled" and x["product"] in rows]
        body += [f'      <h2><a href="{esc(week_path(closed["week"], lang))}">'
                 f"{esc(b['closed'].format(week=closed['week']))}</a></h2>", '      <ol class="rows">']
        for launch in sorted(on, key=lambda x: x["result"]["rank"]):
            body += board_item(launch, rows[launch["product"]], lang, result=launch["result"])
        body.append("      </ol>")
    coming = next((w for w in all_weeks if w.get("status") == "scheduled"
                   and (not running or w["week"] > running["week"])), None)
    if coming:
        on = [x for x in coming.get("launches") or [] if x.get("status") == "scheduled" and x["product"] in rows]
        if on:
            monday, _ = launches.week_days(coming["week"])
            body += [f"      <h2>{esc(b['next'].format(week=coming['week']))}</h2>",
                     f'      <p class="note">{esc(b["next_note"].format(monday=monday))}</p>', '      <ol class="rows">']
            for launch in launches.shuffled(on, coming["week"]):
                body += board_item(launch, rows[launch["product"]], lang, result=None)
            body.append("      </ol>")
    if not running and not closed:
        body.append(f'      <p class="note">{esc(b["no_launch"])}</p>')
    past = [w for w in reversed(all_weeks) if w.get("status") == "closed"]
    if past:
        body += [f"      <h2>{esc(b['past'])}</h2>", "      <ul>"]
        for w in past:
            n = sum(1 for x in w.get("launches") or [] if x.get("status") == "scheduled")
            text = b["past_item"].format(week=w["week"], n=n, closed=w.get("closed_on", ""))
            body.append(f'        <li><a href="{esc(week_path(w["week"], lang))}">{esc(text)}</a></li>')
        body.append("      </ul>")
    hunted = launches.hunters(all_weeks)
    if hunted:
        body += [f"      <h2>{esc(b['hunters'])}</h2>", f'      <p class="note">{esc(b["hunters_note"])}</p>',
                 "      <ol>"]
        for login, n, top in hunted[:HUNTERS]:
            body.append(f'        <li><a href="https://github.com/{esc(login)}" rel="noopener">{esc(login)}</a>: '
                        f'{esc(b["hunter_item"].format(n=n, top=top))}</li>')
        body.append("      </ol>")
    week, fresh = launches.new_this_week(catalog)
    if week:
        body += [f"      <h2>{esc(b['new'].format(week=week))}</h2>", f'      <p class="note">{esc(b["new_note"])}</p>']
    if fresh:
        body.append('      <ol class="rows">')
        for row in fresh:
            summary = row.get("summary_zh") if lang == "zh" and row.get("summary_zh") else row.get("summary", "")
            body += [
                f'        <li id="new-{esc(row["slug"])}">',
                f'          <h3><a href="{esc(product_path(row["slug"]))}">{esc(row["title"])}</a></h3>',
                f'          <p class="meta">{meta_line(row, labels, lang)} · {tier_html(row, lang)}</p>',
                f"          <p>{esc(row.get('tagline') if lang == 'en' and row.get('tagline') else summary)}"
                f"{marks(row, labels, lang) if not (lang == 'en' and row.get('tagline')) else ''}</p>",
                "        </li>",
            ]
        body.append("      </ol>")
    elif week is not None:
        body.append(f"      <p>{esc(b['nothing_new'])}</p>")
    return sp.shell(lang, path=path, title=b["title"], description=b["lede"], body="\n".join(body),
                    alternates={code: launches_path(code) for code in sp.LANGS})


def week_page(week: dict, lang: str, *, rows: dict[str, dict]) -> str:
    """A closed week: its ranking, and what was removed from it and why."""
    b = BOARD[lang]
    monday, sunday = launches.week_days(week["week"])
    lede = b["week_lede"].format(monday=monday, sunday=sunday, closed=week.get("closed_on", ""),
                                 rules=week.get("rules", ""))
    body = [
        f'      <p><a href="../{esc(launches_path(lang))}">{esc(b["board"])}</a></p>',
        f"      <h1>{esc(b['week_h1'].format(week=week['week']))}</h1>",
        f'      <p class="lede">{esc(lede)}</p>',
        '      <ol class="rows">',
    ]
    on = [x for x in week.get("launches") or [] if x.get("status") == "scheduled" and x["product"] in rows]
    for launch in sorted(on, key=lambda x: x["result"]["rank"]):
        body += board_item(launch, rows[launch["product"]], lang, result=launch["result"], base="../")
    body.append("      </ol>")
    removed = [x for x in week.get("launches") or [] if x.get("status") == "removed"]
    if removed:
        body += [f"      <h2>{esc(b['removed'])}</h2>", f'      <p class="note">{esc(b["removed_note"])}</p>', "      <ul>"]
        for launch in removed:
            body.append(f"        <li>{esc(launch['product'])}: {esc(launch.get('reason', ''))}</li>")
        body.append("      </ul>")
    path = week_path(week["week"], lang)
    return sp.shell(lang, path=path, title=b["week_title"].format(week=week["week"]), description=lede,
                    body="\n".join(body), alternates={code: week_path(week["week"], code) for code in sp.LANGS})


BADGE_TEXT = {"week-1": "#1", "week-2": "#2", "week-3": "#3"}


def badge_svg(badge: str, week: str) -> str:
    """A small plain badge: no script, no font or image from anywhere."""
    left, right = "awesome-jev launches", f"{BADGE_TEXT[badge]} of {week}"
    lw, rw = 7 * len(left) + 12, 7 * len(right) + 12
    width = lw + rw
    label = f"{left}: {right}"
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="20" role="img" aria-label="{esc(label)}">'
        f"<title>{esc(label)}</title>"
        f'<rect width="{lw}" height="20" fill="#20252c"/>'
        f'<rect x="{lw}" width="{rw}" height="20" fill="#b8892e"/>'
        '<g fill="#fff" font-family="Verdana,DejaVu Sans,sans-serif" font-size="11">'
        f'<text x="6" y="14">{esc(left)}</text>'
        f'<text x="{lw + 6}" y="14">{esc(right)}</text>'
        "</g></svg>\n"
    )


def badges(launch_weeks: list[dict]) -> dict[str, tuple[str, str]]:
    """Each product's latest badge, as (badge, week)."""
    out: dict[str, tuple[str, str]] = {}
    for week in sorted(launch_weeks, key=lambda w: str(w.get("week"))):
        if week.get("status") != "closed":
            continue
        for launch in week.get("launches") or []:
            got = (launch.get("result") or {}).get("badges") or []
            if launch.get("status") == "scheduled" and got:
                out[launch["product"]] = (got[0], week["week"])
    return out


def pages(catalog: list[dict], patterns: list[dict], labels: sp.Labels, *,
          launch_weeks: list[dict], maker_profiles: dict[str, dict]) -> dict[str, str]:
    """Every file this module writes: path relative to site/ → text."""
    products = sorted((r for r in catalog if launches.is_product(r)), key=lambda r: r["slug"])
    rows = {r["slug"]: r for r in products}
    by_key = {p["key"]: p for p in patterns}
    history = launches.launched(launch_weeks)
    weeks_by_id = {w["week"]: w for w in launch_weeks}
    files: dict[str, str] = {}
    for row in products:
        files[product_path(row["slug"])] = product_page(
            row, products=products, patterns=by_key, labels=labels, history=history, weeks_by_id=weeks_by_id)
    by_login: dict[str, list[dict]] = {}
    for row in products:
        for login in launches.makers_of(row):
            by_login.setdefault(launches.login_key(login), []).append(row)
    for key, made in by_login.items():
        shown = next(x for x in launches.makers_of(made[0]) if launches.login_key(x) == key)
        files[maker_path(key)] = maker_page(
            shown, made, profile=maker_profiles.get(key), labels=labels, history=history, weeks_by_id=weeks_by_id)
    files[f"{MAKER_DIR}/index.html"] = makers_index(by_login, maker_profiles)
    for lang in sp.LANGS:
        files[launches_path(lang)] = board_page(lang, catalog=catalog, rows=rows, all_weeks=launch_weeks, labels=labels)
        for week in launch_weeks:
            if week.get("status") == "closed":
                files[week_path(week["week"], lang)] = week_page(week, lang, rows=rows)
    for slug, (badge, week) in badges(launch_weeks).items():
        if slug in rows:
            files[badge_path(slug)] = badge_svg(badge, week)
    return files
