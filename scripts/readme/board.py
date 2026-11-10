"""The two sections the READMEs open with (since 2026-11-05): the launch board
as it stands, and how a product gets on it; and the cards the README cover
draws from the same files.

The README used to open with the catalogue and mention the board once, inside
a collapsed preview. The board is what changes every week and what a maker
comes for, so it leads, laid out as a launch feed (a vote mark, the product,
its one line, then who launched it and who read its code), and the catalogue
it is built on follows.

Everything here is read from files, never from the clock, so two builds of the
same tree write the same bytes: the weeks in launches/ (written by
launch-collect.yml on Fridays and launch-week.yml on Mondays, both of which
regenerate the READMEs in the same commit) and the two star readings the
rising list compares (launches.readings: the daily readings in history/daily/
from board-daily.yml and the weekly refreshes in history/ from metadata.yml,
both of which regenerate too). Which week is running,
which is filed next and which closed last is decided as the board page on the
site decides it (site_products.board_page), from each week's `status`.

The rules themselves (who counts, how a week ranks, when a product can launch
again) live in scripts/launches.py; this module only prints what they decide.
The rows printed here are not on front_page()'s list, which names the rows a
person picked or the pattern order keeps in the README: these change weekly.
"""

from __future__ import annotations

from dataclasses import dataclass
from html import escape

import launches
from _github import repo_of

from .rows import REPO_URL, SITE, esc, marked, summary_of
from .strings import ZH_MACHINE

# How many rising products the README lists; the board on the site lists
# launches.RISING_SHOWN.
README_RISING = 5
# How many cards the README cover draws.
HERO_CARDS = 3
DISCUSSIONS = f"{REPO_URL}/discussions/categories/launches"
LAUNCH_FORM = launches.query.LAUNCH_FORM
NEW_ENTRY_FORM = f"{REPO_URL}/issues/new?template=new-entry.yml"
MEDALS = {1: "🥇", 2: "🥈", 3: "🥉"}
VOTE, STAR = "▲", "★"
# The feed's picture of a product, in CSS pixels: its GitHub owner's avatar,
# fetched at twice the size for sharp screens. A product with no GitHub
# repository shows the awesome-jev mark instead.
THUMB = 48
NO_THUMB = "site/favicon.svg"
# The right-hand box's width: without one, a table squeezes the column to its
# narrowest unbreakable piece, and Chinese breaks between any two characters,
# so 投票 would stand one character a line.
BOX = 80

# The cover's feed, per language: the heading over the cards for each state
# the board can be in, the footer under them, and the three cards drawn when
# nothing is on the board and nothing is rising (the three steps, as cards).
HERO = {
    "en": {
        "running": "THIS WEEK · {week} · VOTES OPEN",
        "next": "NEXT WEEK · {week} · FILED",
        "closed": "LAST WEEK · {week} · RESULTS",
        "rising": "RISING · STARS GAINED THIS WEEK",
        "steps": "LAUNCH · VOTE · READ THE EVIDENCE",
        "footer": "VOTES AND EVIDENCE SIDE BY SIDE · NEVER ADDED",
        "cards": [
            ("Launch a product", "by Thursday; on the board on Monday"),
            ("Vote with a thumbs-up", "one per account, inside the week"),
            ("Read the evidence", "who read the call site, beside every rank"),
        ],
    },
    "zh": {
        "running": "本周 · {week} · 投票中",
        "next": "下周 · {week} · 已登记",
        "closed": "上周 · {week} · 结果",
        "rising": "上升最快 · 本周星标",
        "steps": "发布 · 投票 · 看证据",
        "footer": "票数与证据并列 · 从不相加",
        "cards": [
            ("发布一个产品", "周四前提交，周一上榜"),
            ("点赞投票", "每个账号一票，当周有效"),
            ("看证据", "每个名次旁边都写着谁读过调用点"),
        ],
    },
}


def board_url(lang: str) -> str:
    return f"{SITE}launches.html" if lang == "en" else f"{SITE}launches.zh.html"


def feed_url(lang: str) -> str:
    return f"{SITE}launches.xml" if lang == "en" else f"{SITE}launches.zh.xml"


def week_url(week: str, lang: str) -> str:
    return f"{SITE}weeks/{week}.html" if lang == "en" else f"{SITE}weeks/{week}.zh.html"


def product_url(slug: str) -> str:
    return f"{SITE}products/{slug}.html"


@dataclass(frozen=True)
class Board:
    """The weeks on file and what they say, as the site's board reads them."""

    rows: dict[str, dict]
    weeks: list[dict]
    running: dict | None
    closed: dict | None
    coming: dict | None
    snapshots: list[dict]

    @property
    def weeks_by_id(self) -> dict[str, dict]:
        return {w["week"]: w for w in self.weeks}

    def on(self, week: dict | None) -> list[dict]:
        """A week's launches on the board whose product is catalogued."""
        if not week:
            return []
        return [x for x in launches.on_board(week) if x.get("product") in self.rows]

    def shuffled(self, week: dict) -> list[dict]:
        return launches.shuffled(self.on(week), week["week"])

    def ranked(self, week: dict) -> list[dict]:
        return sorted(self.on(week), key=lambda x: (x.get("result") or {}).get("rank", 10**6))

    def rising(self, catalog: list[dict], limit: int) -> list[dict]:
        if len(self.snapshots) < 2:
            return []
        return launches.rising(catalog, self.snapshots[-2], self.snapshots[-1], limit=limit)


def read_board(catalog: list[dict]) -> Board:
    weeks = launches.weeks()
    running = next((w for w in reversed(weeks) if w.get("status") == "open"), None)
    closed = next((w for w in reversed(weeks) if w.get("status") == "closed"), None)
    coming = next(
        (w for w in weeks if w.get("status") == "scheduled" and (not running or w["week"] > running["week"])), None
    )
    return Board({r["slug"]: r for r in catalog}, weeks, running, closed, coming, launches.readings())


def tagline(launch: dict, lang: str) -> str:
    if lang == "zh" and launch.get("tagline_zh"):
        return launch["tagline_zh"]
    return launch.get("tagline", "")


def one_line(row: dict, lang: str) -> str:
    """A product's own line (tagline, a maker's words) or its summary with
    the summary's marks."""
    if lang == "zh" and row.get("tagline_zh"):
        return esc(row["tagline_zh"])
    if lang == "en" and row.get("tagline"):
        return esc(row["tagline"])
    return summary_of(row, lang)


def who(launch: dict, strings: dict) -> str:
    login = launch.get("submitted_by", "")
    key = "board_maker" if launch.get("role") == "maker" else "board_hunter"
    return strings[key].format(who=f"[{esc(login)}](https://github.com/{login})")


def thumb(row: dict) -> str:
    """A product's picture on the feed, linked to its page: the avatar of the
    GitHub account that owns its repository (an organisation's logo or a
    maker's own picture, as GitHub serves it), or the awesome-jev mark."""
    repo = repo_of(row)
    src = f"https://github.com/{repo.split('/')[0]}.png?size={THUMB * 2}" if repo else NO_THUMB
    return (
        f'<a href="{product_url(row["slug"])}"><img src="{escape(src)}" width="{THUMB}" height="{THUMB}" '
        f'alt="{escape(row["title"])}"></a>'
    )


def box(lead: str, under: str = "", href: str | None = None) -> str:
    """The feed's right-hand box: a mark or a number over a small word, the
    whole box a link where there is something to do (vote)."""
    inner = f"<b>{lead}</b>" + (f"<br><sub>{under}</sub>" if under else "")
    return f'<a href="{escape(href)}">{inner}</a>' if href else inner


def feed(items: list[tuple[dict, str, list[str], str]]) -> list[str]:
    """Launches laid out as a launch feed: one table row per product with its
    picture, its name and one line over a dim line of who launched it and
    who read its code, and a box on the right with what counts this week (a
    vote, the votes, the stars). `items` are (row, line, meta, box) tuples.

    The middle cell is markdown, fenced by blank lines inside the <td> so
    GitHub renders it as markdown (links, <sub>) within the HTML table; the
    two outer cells are plain HTML, each with a width: GitHub's
    `max-width: 100%` on images would otherwise let a table squeeze the
    picture to a sliver, and the box's words to a character a line (BOX)."""
    out = ["<table>"]
    for row, line, meta, right in items:
        out += [
            "<tr>",
            f'<td align="center" width="{THUMB + 8}">{thumb(row)}</td>',
            "<td>",
            "",
            f"**[{esc(row['title'])}]({product_url(row['slug'])})** — {line}<br>",
            f"<sub>{' · '.join(meta)}</sub>",
            "",
            "</td>",
            f'<td align="center" width="{BOX}">{right}</td>',
            "</tr>",
        ]
    return out + ["</table>", ""]


def launch_list(board: Board, week: dict, strings: dict, *, vote: bool) -> list[str]:
    """A running or filed week's launches, shuffled as the board shows them:
    while the week runs the box is the vote link (counts stay hidden until it
    closes); for a filed week it says the Monday it opens."""
    lang, items = strings["lang_code"], []
    monday, _ = launches.week_days(week["week"])
    for launch in board.shuffled(week):
        row = board.rows[launch["product"]]
        meta = [who(launch, strings), strings["tiers"][launches.tier(row)]]
        number = launch.get("discussion")
        if vote and isinstance(number, int):
            right = box(VOTE, strings["box_vote"], f"{launches.query.DISCUSSION}{number}")
        else:
            right = box(VOTE, strings["box_opens"].format(day=monday.strftime("%m-%d")))
        items.append((row, esc(tagline(launch, lang)), meta, right))
    return feed(items)


def closed_list(board: Board, strings: dict) -> list[str]:
    """Last week's top three by rank, their votes beside their evidence, and
    the link to the whole week."""
    lang, week, items = strings["lang_code"], board.closed, []
    for launch in board.ranked(week)[:3]:
        row, result = board.rows[launch["product"]], launch.get("result") or {}
        rank = result.get("rank")
        votes = strings["board_votes"].format(votes=result.get("votes", 0), counted=result.get("counted", 0))
        meta = [f"{VOTE} {votes}"] + ([strings["board_ring"]] if result.get("ring") else [])
        meta += [who(launch, strings), strings["tiers"][launches.tier(row)]]
        right = box(f"{MEDALS.get(rank, f'#{rank}')}&nbsp;{result.get('counted', 0):,}", strings["box_votes"])
        items.append((row, esc(tagline(launch, lang)), meta, right))
    more = marked(strings, "board_closed_more", week=week["week"], page=week_url(week["week"], lang), feed=feed_url(lang))
    return feed(items) + [more, ""]


def rising_state(board: Board, row: dict, strings: dict, today) -> str:
    """What a rising product can do next: launch now, wait, or be voted on."""
    mine = launches.launched(board.weeks).get(row["slug"], [])
    state, again = launches.launch_again(mine, board.weeks_by_id, today)
    if state == "now":
        return f"[{strings['board_launch_it']}]({launches.query.launch_form(row['slug'], row['title'])})"
    if state == "from":
        return strings["board_again"].format(day=again)
    week, launch = mine[-1]
    if isinstance(launch.get("discussion"), int):
        return f"[{strings['board_vote']}]({launches.query.DISCUSSION}{launch['discussion']})"
    return strings["board_on"].format(week=week)


def rising_list(board: Board, catalog: list[dict], strings: dict) -> list[str]:
    """The products rising fastest between the two star readings
    launches.readings() picks: the newest, and the one closest to a week before."""
    if len(board.snapshots) < 2:
        return []
    lang = strings["lang_code"]
    before, after = board.snapshots[-2], board.snapshots[-1]
    risen = board.rising(catalog, README_RISING)
    out = [f"### {strings['board_rising_h'].format(start=before.get('date', ''), end=after.get('date', ''))}", ""]
    if not risen:
        return out + [marked(strings, "board_rising_none", n=launches.RISING_MIN), ""]
    today = launches.as_of(catalog)
    items = []
    for item in risen:
        row = item["row"]
        share = launches.share(item["gained"], item["before"])
        stars = strings["board_stars"].format(before=f"{item['before']:,}", after=f"{item['after']:,}", share=share)
        meta = [stars, strings["tiers"][launches.tier(row)], rising_state(board, row, strings, today)]
        items.append((row, one_line(row, lang), meta, box(f"{STAR}&nbsp;+{item['gained']:,}", strings["box_stars"])))
    note = marked(
        strings, "board_rising_note", n=launches.RISING_MIN, shown=launches.RISING_SHOWN, listed=README_RISING,
        board=board_url(lang),
    )
    return out + feed(items) + [f"<sub>{note}</sub>", ""]


def this_weeks_launches(page) -> list[str]:
    """The board as it stands, products first: the running week, the week
    filed next, last week's top three, or a line saying no week has opened;
    then how the board works, then what is rising."""
    strings, lang = page.strings, page.lang
    board = read_board(page.catalog)
    out = [f"## {strings['board_h']}", ""]
    shown = False
    if board.on(board.running):
        shown = True
        out += [f"### {strings['board_running_h'].format(week=board.running['week'])}", ""]
        out += [marked(strings, "board_running_note"), ""]
        out += launch_list(board, board.running, strings, vote=True)
    if board.on(board.coming):
        shown = True
        monday, _ = launches.week_days(board.coming["week"])
        out += [f"### {strings['board_next_h'].format(week=board.coming['week'])}", ""]
        out += [marked(strings, "board_next_note", monday=monday), ""]
        out += launch_list(board, board.coming, strings, vote=False)
    if board.on(board.closed):
        shown = True
        out += [f"### {strings['board_closed_h'].format(week=board.closed['week'])}", ""]
        out += closed_list(board, strings)
    if not shown:
        out += [marked(strings, "board_empty", form=LAUNCH_FORM), ""]
    out += [marked(strings, "board_intro", discussions=DISCUSSIONS, board=board_url(lang)), ""]
    out += rising_list(board, page.catalog, strings)
    return out


def example_product(board: Board, catalog: list[dict]) -> str | None:
    """The product whose badge the README shows live: the first launch on the
    board or filed next, else the fastest riser; None before either."""
    for week in (board.running, board.coming):
        if week and board.on(week):
            return board.shuffled(week)[0]["product"]
    risen = board.rising(catalog, 1)
    return risen[0]["row"]["slug"] if risen else None


def week_figure(catalog: list[dict], lang: str) -> list[str]:
    """The "how a launch week runs" figure (build_readme_week.py), with where
    the board is now in its alt text as in the image, picked by theme and
    width as the cover is."""
    import build_readme_cover as cover
    import build_readme_week as week

    alt = escape(week.alt_text(lang, week.now_of(catalog)))
    out = ["<picture>"]
    for media, srcset in cover.picture_sources(lang, stem=week.STEM):
        out.append(f'  <source media="{media}" srcset="{srcset}">')
    out += [f'  <img src="{cover.asset_path(lang, "light", stem=week.STEM)}" alt="{alt}" width="100%">', "</picture>", ""]
    return out


def launch_your_product(page) -> list[str]:
    """How a product launches, as three steps, the badge it gets, and where
    the rules and the data are."""
    strings, lang = page.strings, page.lang
    out = [f"## {strings['launch_h']}", "", marked(strings, "launch_intro", entry=NEW_ENTRY_FORM), ""]
    out += week_figure(page.catalog, lang)
    out += [f"| {strings['th_step']} | {strings['th_when']} | {strings['th_what_happens']} |", "| --- | --- | --- |"]
    for step, when, what in strings["launch_steps"]:
        out.append(f"| **{step}** | {when} | {what.format(form=LAUNCH_FORM, discussions=DISCUSSIONS)} |")
    if lang == "zh" and "launch_steps" in ZH_MACHINE:
        out.append("<sub>(机翻)</sub>")
    out += ["", marked(strings, "launch_badge"), ""]
    slug = example_product(read_board(page.catalog), page.catalog)
    if slug:
        live = strings["launch_badge_live"].format(slug=slug)
        out += [f"[![awesome-jev]({SITE}badges/{slug}.svg)]({product_url(slug)}) <sub>← {live}</sub>", ""]
    out += ["```markdown", launches.badge_line("your-slug"), "```", ""]
    docs = "docs/launches.zh-CN.md" if lang == "zh" else "docs/launches.md"
    engine = "docs/launch-engine.zh-CN.md" if lang == "zh" else "docs/launch-engine.md"
    out += [
        marked(
            strings, "launch_more", rules=f"{docs}#{strings['launch_rules_anchor']}", board=board_url(lang),
            feed=feed_url(lang), api=f"{SITE}api/v1/launches.json", engine=engine,
        ),
        "",
    ]
    return out


def compact(n: int) -> str:
    """A count as the cover's vote box has room for: 999, 1.2k, 12.4k, 123k."""
    if n < 1_000:
        return str(n)
    if n < 100_000:
        return f"{n / 1_000:.1f}k"
    return f"{n // 1_000}k"


def hero_card(row: dict, line: str, *, mark: str, count: str | None = None, rank: str | None = None) -> dict:
    return {"mark": mark, "count": count, "rank": rank, "title": row["title"], "line": line,
            "tier": launches.tier(row)}


def hero(catalog: list[dict], lang: str) -> dict:
    """What the README cover's feed shows in `lang`, from the files the
    section reads: a heading, HERO_CARDS cards (a vote or star mark, a count
    where the board shows one, a rank once a week closed, the product, its
    line and its evidence tier) and a footer. The running week first, then
    the week filed next, then the last closed week, then the rising products;
    with none of those, the three steps as cards."""
    words, board = HERO[lang], read_board(catalog)
    for week, key in ((board.running, "running"), (board.coming, "next")):
        if week and board.on(week):
            cards = [hero_card(board.rows[x["product"]], tagline(x, lang), mark=VOTE) for x in board.shuffled(week)]
            return {"heading": words[key].format(week=week["week"]), "cards": cards[:HERO_CARDS], "footer": words["footer"]}
    if board.closed and board.on(board.closed):
        cards = []
        for x in board.ranked(board.closed)[:HERO_CARDS]:
            result = x.get("result") or {}
            cards.append(hero_card(board.rows[x["product"]], tagline(x, lang), mark=VOTE,
                                   count=compact(int(result.get("counted", 0))), rank=f"#{result.get('rank', '')}"))
        return {"heading": words["closed"].format(week=board.closed["week"]), "cards": cards, "footer": words["footer"]}
    risen = board.rising(catalog, HERO_CARDS)
    if risen:
        cards = [hero_card(x["row"], plain_line(x["row"], lang), mark=STAR, count=f"+{compact(x['gained'])}") for x in risen]
        return {"heading": words["rising"], "cards": cards, "footer": words["footer"]}
    cards = [{"mark": VOTE, "count": None, "rank": None, "title": t, "line": l, "tier": None} for t, l in words["cards"]]
    return {"heading": words["steps"], "cards": cards, "footer": words["footer"]}


def plain_line(row: dict, lang: str) -> str:
    """A product's line for the cover: its tagline, else its summary, with no
    marks, since an image carries no footnote."""
    if lang == "zh" and row.get("tagline_zh"):
        return row["tagline_zh"]
    if lang == "en" and row.get("tagline"):
        return row["tagline"]
    return row.get("summary_zh" if lang == "zh" else "summary") or ""
