"""README.md and README.zh-CN.md, one function per section.

render() used to be one 310-line function. Each section is now a function of
the same Page, in SECTIONS order; the reading map at the top (section_nav) and
the ## headings they write are checked against each other by a test.
"""

from __future__ import annotations

import hashlib
import html
from dataclasses import dataclass

import _stats
import build_assets
import build_readme_cover
import picker as picker_rules

from .rows import (
    FLAG_LABELS,
    FLAG_ORDER,
    KIND_LABELS,
    KIND_ORDER,
    PATTERN_LABELS,
    PATTERN_ORDER,
    RAW,
    REPO_URL,
    ROOT,
    SITE,
    anchor,
    collection_link,
    is_negative,
    negatives_link,
    direction_bit,
    direction_note,
    collection_slugs,
    entry_list,
    esc,
    group_by_pattern,
    is_measured,
    label,
    marked,
    measured_page,
    page_name,
    reports_link,
    site_link,
    sort_key,
    source_marks,
    split_unindexed,
    stars_note,
    summary_of,
    unindexed_note,
)
from .strings import DATA_FILES, REPO_FILES, REPO_FILES_ZH, ZH_MACHINE

# The handful of rows a newcomer should open, in reading order. Curated by hand
# because "most starred" is not the same as "read this first" — the limitations
# page has no stars at all and is the most useful page in the docs.
START_HERE = [
    "typesafe-quickstart",
    "typesafe-jaggedness",
    "example-three-primitives",
    "fast-jev-compaction",
    "ai-cookbook-jev-track",
    "hermes-agent-jev-evaluation",
]

# The README shows this many rows per pattern and links to a page with the rest.
#
# It used to show every row, collapsing long sections behind <details>. That
# kept the scroll short but not the file: at 805 entries the README was 323 KB,
# 92% of it this one section, with every multi-pattern row printed once per
# pattern. Collapsing hides rows from the eye, not from the download, the
# renderer or anyone reading the raw file.
#
# Ten is enough to show what a pattern looks like in practice, in nearly the
# order the site and the MCP server use — official first, then code, then
# stars — so the surfaces agree on what comes first. The README compares stars
# by band (rows.STAR_BANDS) and then goes by title, where the site and the MCP
# server compare the exact count. Each pattern also gets its own generated
# page, which is a URL worth having for its own sake: "every safety-gating
# example" can now be linked to.
INLINE_PER_PATTERN = 10

# "Measured, not claimed" shows this many independent reports and links
# docs/measured.md, which lists every one, with every note.
#
# Until 2026-09-27 it printed them all, each with its note: 70 reports, 350 of
# the README's 1,442 lines, all of them before "By decision pattern", the
# section the README calls its primary index. The rows shown are the curated
# `measured` path of collections.json first, in its order, since a person
# picked them to read first, then the first of the others by sort_key, as a
# pattern's rows are chosen. The number lives here, beside INLINE_PER_PATTERN,
# not in collections.json: that file is editorial data and
# check_collections.py holds it to its fields.
#
# Since 2026-09-28 the negative results come first, under their own heading
# (rows.is_negative: a benchmark whose author's direction is unfavourable, or
# the negative-result flag on another row, which is how a plugin that measured
# and dropped a use of Jev reaches this section at all), by sort_key, and they
# count towards the ten.
INLINE_MEASURED = 10


def coverage_note(stats: dict, lang: str) -> str:
    """Describe current catalogue coverage without inferring ecosystem absence."""
    missing = [key for key, count in stats["by_pattern"].items() if count == 0]
    total = len(stats["by_pattern"])
    if lang == "zh":
        if missing:
            statement = (
                f"本目录有 {len(missing)} 个模式尚未收录条目："
                + "、".join(f"`{key}`" for key in missing)
                + "。未收录不代表其他地方没有公开案例。"
            )
        elif total:
            statement = f"全部 {total} 个模式均已收录条目。覆盖不代表已运行验证或各模式成熟度相同。"
        else:
            statement = "尚未配置决策模式，因此暂不报告覆盖率。"
        return statement + " 详见 [`docs/status.md`](docs/status.md)。"
    if missing:
        statement = (
            f"{len(missing)} patterns have no entries in this catalogue: "
            + ", ".join(f"`{key}`" for key in missing)
            + ". Absence here does not establish absence elsewhere."
        )
    elif total:
        statement = f"All {total} patterns have at least one catalogue entry. Coverage does not imply runtime testing or equal maturity."
    else:
        statement = "No decision patterns are configured, so coverage is not reported yet."
    return statement + " See [`docs/status.md`](docs/status.md)."


def preview_version() -> str:
    """Invalidate GitHub's image proxy when a rendered preview can change."""
    paths = [
        "site/index.html", "site/catalog.css", "site/catalog-core.mjs",
        "site/favicon.svg", "scripts/render_images.py", "scripts/_stats.py",
        "catalog.json", "collections.json", "compat.json", "patterns.json", "taxonomy.json",
    ]
    digest = hashlib.sha256()
    for path in paths:
        digest.update(path.encode())
        digest.update((ROOT / path).read_bytes())
    return digest.hexdigest()[:16]


def section_nav(strings: dict, *, has_measured: bool = True) -> list[str]:
    keys = ["about_h", "prims_h", "start_h", "coverage_h", "measured_h", "patterns_h", "kinds_h", "repo_h", "verified_h", "data_h", "contrib_h"]
    if not has_measured:
        keys.remove("measured_h")
    return [f"{n:02d} [{strings[key]}](#{anchor(strings[key])})" for n, key in enumerate(keys, 1)]


def entry_points(strings: dict) -> list[tuple[str, str]]:
    """Header chips: the catalogue, its three curated paths, the other language.

    Spaces become &nbsp; so a chip wraps as a unit on phones, never mid-label.
    """
    lang = strings["lang_code"]
    explore = "浏览资源目录 ↗" if lang == "zh" else "Explore the catalogue ↗"
    paths = [("first-call", strings["collection_first"]), ("build", strings["collection_build"]), ("measured", strings["collection_measured"])]
    chips = [(f"{SITE}?lang={lang}", f"<b>{explore}</b>")]
    chips += [(f"{SITE}?collection={key}&amp;lang={lang}", title) for key, title in paths]
    chips.append((strings["other_readme"], strings["other_name"]))
    return [(href, title.replace(" ", "&nbsp;")) for href, title in chips]


def inline_measured(
    measured: list[dict], picked: list[str], limit: int = INLINE_MEASURED
) -> tuple[list[dict], list[dict]]:
    """The reports the README prints: `picked` (a collections.json path) that
    are among `measured`, in that order, then the first of the others by
    sort_key, `limit` in all. Returned apart, as (picks, others)."""
    by_slug = {entry["slug"]: entry for entry in measured}
    picks = [by_slug[slug] for slug in dict.fromkeys(picked) if slug in by_slug][:limit]
    taken = {entry["slug"] for entry in picks}
    others = [entry for entry in sorted(measured, key=sort_key) if entry["slug"] not in taken]
    return picks, others[: max(0, limit - len(picks))]


def negative_first(measured: list[dict]) -> tuple[list[dict], list[dict]]:
    """The negative results among `measured` by sort_key, and the other rows as
    given: the order every list of measured rows prints them in."""
    negatives = sorted((entry for entry in measured if is_negative(entry)), key=sort_key)
    return negatives, [entry for entry in measured if not is_negative(entry)]


def measured_selection(measured: list[dict], picked: list[str]) -> tuple[list[dict], list[dict], list[dict]]:
    """The rows "Measured, not claimed" prints, INLINE_MEASURED in all: the
    negative results first (negative_first), then inline_measured's picks and
    others from the rest. Returned apart, as (negatives, picks, others)."""
    negatives, rest = negative_first(measured)
    negatives = negatives[:INLINE_MEASURED]
    picks, others = inline_measured(rest, picked, INLINE_MEASURED - len(negatives))
    return negatives, picks, others


@dataclass(frozen=True)
class Page:
    """What every section reads: the rows, one language's strings, the stats
    snapshot, and the rows grouped the way the README groups them."""

    catalog: list[dict]
    retired: list[dict]
    strings: dict
    stats: dict
    by_pattern: dict[str, list[dict]]
    by_kind: dict[str, list[dict]]

    @property
    def lang(self) -> str:
        return self.strings["lang_code"]

    @property
    def live_patterns(self) -> list[str]:
        return [key for key in PATTERN_ORDER if self.by_pattern[key]]

    @property
    def live_kinds(self) -> list[str]:
        return [key for key in KIND_ORDER if self.by_kind[key]]


def cover_and_nav(page: Page) -> list[str]:
    """The cover image, entry-point chips, counts caveat and reading map."""
    strings, lang, catalog, stats = page.strings, page.lang, page.catalog, page.stats
    out: list[str] = []
    add = out.append

    add("<!--")
    add(f"  {strings['generated']}")
    add("-->")
    add("")
    add('<a name="top"></a>')
    add('<a name="awesome-jev"></a>')
    add('<a name="-awesome-jev"></a>')
    add("")
    # The cover's own <desc>, so the alt text carries the same counts, labels
    # and record caveat as the image instead of a third wording of them.
    cover_alt = f"awesome-jev — {build_readme_cover.description(lang, stats)}"
    add(f'<a href="{SITE}?lang={lang}">')
    add('<picture>')
    # The order is load-bearing; see build_readme_cover.picture_sources.
    for media, srcset in build_readme_cover.picture_sources(lang):
        add(f'  <source media="{media}" srcset="{srcset}">')
    add(f'  <img src="{build_readme_cover.asset_path(lang, "light")}" alt="{cover_alt}" width="100%">')
    add('</picture>')
    add('</a>')
    add("")
    # <kbd> is the one native element GitHub draws like a button: bordered,
    # rounded and shadowed, with no image to go stale or resist translation.
    add('<p align="center">')
    for href, title in entry_points(strings):
        add(f'<a href="{href}"><kbd>&nbsp;{title}&nbsp;</kbd></a>')
    add('</p>')
    add("")
    scope = "统计口径" if lang == "zh" else "About these counts"
    add(f'<p align="center"><sub>{strings["badge_note"]} <a href="#{anchor(strings["verified_h"])}">{scope}</a></sub></p>')
    add("")
    add('<details>')
    toc_label = "阅读导航 · 完整目录" if lang == "zh" else "On this page · full reading map"
    add(f'<summary><b>{toc_label}</b></summary>')
    add("")
    patterns_doc = REPO_FILES_ZH.get("docs/patterns.md", "docs/patterns.md") if lang == "zh" else "docs/patterns.md"
    add(f"[{strings['l_patterns']}]({patterns_doc}) · [{strings['l_compat']}](docs/compatibility.md) · [{strings['l_vetting']}](docs/vetting.md)")
    add("")
    has_measured = any(is_measured(e) for e in catalog)
    for item in section_nav(strings, has_measured=has_measured):
        add(f"- {item}")
    add("")
    add('</details>')
    add("")
    add("---")
    add("")
    return out


def what_this_is(page: Page) -> list[str]:
    """What Jev is, what this repository is, and what it is not."""
    strings = page.strings
    out: list[str] = []
    add = out.append

    add(f"## {strings['about_h']}")
    add("")
    for (line,) in strings["about_rows"]:
        add(f"- {line}")
    add("")
    add("> [!NOTE]")
    add(f"> {strings['about_not']}")
    add("")
    return out


def what_jev_returns(page: Page) -> list[str]:
    """The three primitives, as a generated figure."""
    strings, lang = page.strings, page.lang
    out: list[str] = []
    add = out.append

    add(f"## {strings['prims_h']}")
    add("")
    add(marked(strings, "prims_intro"))
    add("")
    add("<picture>")
    add(
        f'  <source media="(prefers-color-scheme: dark)" '
        f'srcset="docs/assets/primitives-{lang}-dark.svg">'
    )
    add(
        f'  <img src="docs/assets/primitives-{lang}-light.svg" '
        f'alt="{strings["prim_alt"]}" width="660">'
    )
    add("</picture>")
    add("")
    # Read by a person (question_types) and text signal only (primitives_seen),
    # as the figure counts them.
    add(marked(strings, "prims_layers"))
    add("")
    add(marked(strings, "prims_after"))
    add("")
    out += primitive_picker(page)
    return out


def primitive_picker(page: Page) -> list[str]:
    """picker.json as build_assets draws it, with its sources as links (an
    image cannot carry them) and the figure described in its alt text."""
    strings, lang = page.strings, page.lang
    picker = picker_rules.load()
    sources = " · ".join(
        f"[{n}] [{build_assets.short_url(url)}]({url})" for n, url in enumerate(picker_rules.sources(picker), 1)
    )
    alt = html.escape(build_assets.picker_description(picker, lang), quote=False).replace('"', "&quot;")
    return [
        marked(strings, "picker_intro"),
        "",
        "<picture>",
        f'  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/{build_assets.picker_file(lang, "dark")}">',
        f'  <img src="docs/assets/{build_assets.picker_file(lang, "light")}" alt="{alt}" width="{build_assets.PICK_WIDTH}">',
        "</picture>",
        "",
        marked(strings, "picker_sources", sources=sources),
        "",
    ]


def start_here(page: Page) -> list[str]:
    """START_HERE, in reading order, each with why it is on the list."""
    strings, lang = page.strings, page.lang
    by_slug = {entry["slug"]: entry for entry in page.catalog}
    out: list[str] = []
    add = out.append

    add(f"## {strings['start_h']}")
    add("")
    add(strings["start_intro"])
    add("")
    for index, slug in enumerate(START_HERE, 1):
        entry = by_slug.get(slug)
        if entry is None:
            raise KeyError(
                f"START_HERE names {slug!r}, which is not in catalog.json. Update the list in "
                "scripts/readme/sections.py when a curated row is renamed or removed."
            )
        why = entry.get("notes_zh" if lang == "zh" else "notes") or summary_of(
            entry, lang
        )
        # An ordered list: a table squeezed the title column until names wrapped.
        add(f"{index}. **[{esc(entry['title'])}]({entry['url']})**")
        add("")
        add(f"   {esc(why)}")
        add("")
    return out


def coverage(page: Page) -> list[str]:
    """The coverage figure, what it leaves out, and the pattern index."""
    strings, lang, stats = page.strings, page.lang, page.stats
    by_pattern, live_patterns = page.by_pattern, page.live_patterns
    out: list[str] = []
    add = out.append

    add(f"## {strings['coverage_h']}")
    add("")
    add(strings["coverage_intro"])
    add("")
    add("<picture>")
    add(
        f'  <source media="(prefers-color-scheme: dark)" '
        f'srcset="docs/assets/coverage-{lang}-dark.svg">'
    )
    add(
        f'  <img src="docs/assets/coverage-{lang}-light.svg" '
        f'alt="{strings["cov_alt"]}" width="100%">'
    )
    add("</picture>")
    add("")
    add(coverage_note(stats, lang))
    add("")
    add('<a name="pattern-index"></a>')
    add("")
    add("**场景索引 · 点击跳转到条目**" if lang == "zh" else "**Pattern index · jump to the examples**")
    add("")
    add("| 场景 | 场景 |" if lang == "zh" else "| Decision pattern | Decision pattern |")
    add("| :--- | :--- |")
    cells = []
    for key in live_patterns:
        name = label(PATTERN_LABELS, key, lang)
        cells.append(f"[{name}](#{anchor(name)}) · **{len(by_pattern[key])}**")
    for index in range(0, len(cells), 2):
        add(f"| {cells[index]} | {cells[index + 1] if index + 1 < len(cells) else ''} |")
    add("")
    return out


def measured_results(page: Page) -> list[str]:
    """Independent measurement reports, surfaced early; absent when there are none.

    The first INLINE_MEASURED (see inline_measured), and a link to the page
    with every one.
    """
    strings, lang = page.strings, page.lang
    measured = [entry for entry in page.catalog if is_measured(entry)]
    if not measured:
        return []
    negatives, picks, others = measured_selection(measured, collection_slugs("measured"))
    out = [f"## {strings['measured_h']}", "", strings["measured_intro"], ""]
    if any(direction_bit(entry, strings) for entry in negatives + picks + others):
        out += [direction_note(strings, docs="docs/"), ""]
    if negatives:
        out += [f"### {strings['negative_h']}", "", marked(strings, "negative_note", site=negatives_link(lang)), ""]
        out.extend(entry_list(negatives, strings, notes=True, readme_layout=True, keep_order=True))
        out += [f"### {strings['others_h']}", ""] if picks or others else []
    out.extend(entry_list(picks, strings, notes=True, readme_layout=True, keep_order=True) if picks else [])
    out.extend(entry_list(others, strings, notes=True, readme_layout=True) if others else [])
    shown = len(negatives) + len(picks) + len(others)
    links = {"n": len(measured), "page": f"docs/{measured_page(lang)}", "site": reports_link(lang)}
    if shown == len(measured):
        out.append(strings["pattern_all"].format(**links))
    elif negatives:
        out.append(marked(strings, "measured_more_negative", shown=shown, path=collection_link("measured", lang), **links))
    elif picks and others:
        out.append(marked(strings, "measured_more", shown=shown, path=collection_link("measured", lang), **links))
    else:
        out.append(strings["pattern_more"].format(shown=shown, **links))
    return out + [""]


def by_decision_pattern(page: Page) -> list[str]:
    """The primary index: the first rows of each pattern and a link to the rest."""
    strings, lang = page.strings, page.lang
    by_pattern, live_patterns = page.by_pattern, page.live_patterns
    out: list[str] = []
    add = out.append

    add(f"## {strings['patterns_h']}")
    add("")
    add(strings["patterns_intro"].replace("{site}", SITE))
    add("")
    add(stars_note(strings, catalog="catalog.json"))
    add("")
    add(marked(strings, "call_site_note"))
    add("")
    for key in live_patterns:
        name = label(PATTERN_LABELS, key, lang)
        blurb = label(PATTERN_LABELS, key, lang, field=2)
        rows = by_pattern[key]
        indexed, later = split_unindexed(rows)
        shown = min(len(indexed), INLINE_PER_PATTERN)
        page_link = f"docs/by-pattern/{page_name(key, lang)}"
        add(f"### {name}")
        add("")
        add(f"_{blurb}_")
        add("")
        out.extend(entry_list(indexed[:INLINE_PER_PATTERN], strings, readme_layout=True))
        more = "pattern_more" if len(rows) > shown else "pattern_all"
        add(strings[more].format(shown=shown, n=len(rows), page=page_link, site=site_link(key, lang)))
        add("")
        if later:
            add(f"#### {strings['unindexed_h']}")
            add("")
            add(unindexed_note(
                strings, "unindexed_readme", n=len(later), page=f"{page_link}#unindexed",
                site=site_link(key, lang), queue="docs/review-queue.md#unsorted-overview",
            ))
            add("")
        up = "↑ 场景索引" if lang == "zh" else "↑ Pattern index"
        add(f"<sub>[{up}](#pattern-index)</sub>")
        add("")
    return out


def by_resource_kind(page: Page) -> list[str]:
    """The same rows counted by kind, as a table."""
    strings, lang = page.strings, page.lang
    by_kind, live_kinds = page.by_kind, page.live_kinds
    out: list[str] = []
    add = out.append

    add(f"## {strings['kinds_h']}")
    add("")
    add(strings["kinds_intro"])
    add("")
    add(
        f"| {strings['th_kind'] if 'th_kind' in strings else 'Kind'} | {strings['th_count']} | {strings['th_find']} |"
    )
    add("| --- | ---: | --- |")
    for key in live_kinds:
        count = len(by_kind[key])
        add(
            f"| **{label(KIND_LABELS, key, lang)}** | **{count}** "
            f"| {esc(label(KIND_LABELS, key, lang, field=2))} |"
        )
    add("")
    return out


# The vendor's own agent skill, which skills/awesome-jev/ complements. The
# sentence under the table links its row and takes the address from it.
OFFICIAL_SKILL = "typesafe-skills-repo"


def also_in_this_repo(page: Page) -> list[str]:
    """The site preview and the files that are not the catalogue."""
    strings, lang = page.strings, page.lang
    out: list[str] = []
    add = out.append

    add(f"## {strings['repo_h']}")
    add("")
    add(strings["repo_intro"])
    add("")
    add('<details>')
    preview_label = "查看可搜索站点预览" if lang == "zh" else "Preview the searchable catalogue"
    add(f'<summary><b>{preview_label}</b></summary>')
    add("")
    shot = "site-zh.png" if lang == "zh" else "site-en.png"
    add(f'<a href="{SITE}?lang={lang}"><img src="{SITE}img/{shot}?v={preview_version()}" alt="{strings["shot_alt"]}" width="760"></a>')
    add("")
    add(f"<sub>{strings['shot_cap']}</sub>")
    add("")
    add('</details>')
    add("")
    add(f"| {strings['th_file']} | {strings['th_what']} |")
    add("| --- | --- |")
    for path, what_en, what_zh in REPO_FILES:
        link = REPO_FILES_ZH.get(path, path) if lang == "zh" else path
        add(f"| [`{link}`]({link}) | {esc(what_zh if lang == 'zh' else what_en)} |")
    add("")
    official = next((e for e in page.catalog if e["slug"] == OFFICIAL_SKILL), None)
    if official:
        add(marked(strings, "repo_skill_division", url=official["url"], row=f"{SITE}?lang={lang}#{OFFICIAL_SKILL}"))
        add("")
    return out


def what_is_verified(page: Page) -> list[str]:
    """What each kind of evidence record means, the caveat tags in use, and retired links."""
    strings, lang, stats = page.strings, page.lang, page.stats
    catalog, retired = page.catalog, page.retired
    # Recorded citations are not the result of the latest scheduled check, and
    # one count per evidence.kind: only the first is a place anyone calls Jev.
    recheck = strings["verified_recheck"].format(
        call_site=stats["call_site_rows"],
        wire_shape=stats["wire_shape_rows"],
        example_only=stats["example_only_rows"],
    )
    if lang == "zh" and "verified_recheck" in ZH_MACHINE:
        recheck += " <sub>(机翻)</sub>"
    summaries = strings["verified_summaries"].format(
        upstream=stats["summary_upstream"],
        stale=stats["summary_upstream_stale"],
        curated=stats["summary_curated"],
        unlabelled=stats["summary_unlabelled"],
        **source_marks(lang),
    )
    if lang == "zh" and "verified_summaries" in ZH_MACHINE:
        summaries += " <sub>(机翻)</sub>"
    # Who wrote the Chinese: a person, or a model (zh_machine, marked on every row).
    translations = marked(
        strings, "verified_translations", hand=stats["zh_hand"], machine=stats["zh_machine"], entries=stats["entries"]
    )
    # A person's reading and a script's text signal, counted apart.
    primitives = marked(
        strings,
        "verified_primitives",
        read=stats["primitive_rows"],
        signal=stats["primitive_signal_rows"],
        signal_only=stats["primitive_signal_only_rows"],
    )
    out: list[str] = []
    add = out.append

    add(f"## {strings['verified_h']}")
    add("")
    for text in [
        strings['verified_yes'].format(**stats), strings['verified_read'], summaries, translations, recheck,
        primitives, strings['verified_no'],
    ]:
        add(f"- {text}")
        add("")
    add("")
    add(f"### {strings['verified_flags_h']}")
    add("")
    used_flags = [
        flag for flag in FLAG_ORDER if any(flag in e.get("flags", []) for e in catalog)
    ]
    add(f"| {strings['th_tag']} | {strings['th_means']} |")
    add("| --- | --- |")
    for flag in used_flags:
        add(
            f"| `{label(FLAG_LABELS, flag, lang)}` "
            f"| {esc(label(FLAG_LABELS, flag, lang, field=2))} |"
        )
    add("")

    if retired:
        add(f"### {strings['retired_h']}")
        add("")
        add(strings["retired_intro"])
        add("")
        add(f"| {strings['th_example']} | {strings['th_why']} |")
        add("| --- | --- |")
        for entry in sorted(retired, key=lambda item: (item["title"].lower(), item["slug"])):
            why = entry.get("notes_zh" if lang == "zh" else "notes") or "—"
            status = entry.get("link_status")
            add(
                f"| {esc(entry['title'])} | {esc(why)}{f' `HTTP {status}`' if status else ''} |"
            )
        add("")
    return out


def machine_readable_data(page: Page) -> list[str]:
    """The data files, with the two catalogue files' live row counts."""
    strings, lang = page.strings, page.lang
    catalog, retired = page.catalog, page.retired
    out: list[str] = []
    add = out.append

    add(f"## {strings['data_h']}")
    add("")
    add(strings["data_intro"])
    add("")
    add(f"| {strings['th_file']} | {strings['th_what']} |")
    add("| --- | --- |")
    add(
        f"| [`catalog.json`]({RAW}/catalog.json) | {len(catalog)} {strings['stat_entries']} |"
    )
    add(
        f"| [`retired.json`]({RAW}/retired.json) | {len(retired)} {strings['stat_retired']} |"
    )
    for path, en, zh in DATA_FILES:
        add(f"| [`{path}`]({RAW}/{path}) | {zh if lang == 'zh' else en} |")
    add("")
    return out


def contributing_and_licence(page: Page) -> list[str]:
    """How to contribute, the licences, the maintenance checks and the footer."""
    strings, lang = page.strings, page.lang
    out: list[str] = []
    add = out.append

    add(f"## {strings['contrib_h']}")
    add("")
    add(strings["contrib_body"])
    add("")
    quoted = strings["license_summaries"].format(**source_marks(lang))
    if lang == "zh" and "license_summaries" in ZH_MACHINE:
        quoted += " <sub>(机翻)</sub>"
    add(strings["license_body"] + ("" if lang == "zh" else " ") + quoted)
    add("")
    checks_label = "维护检查" if lang == "zh" else "Maintenance checks"
    links_label = "定期链接检查" if lang == "zh" else "Scheduled link checks"
    claims_label = "调用点文本检查" if lang == "zh" else "Call-site text checks"
    add(f"**{checks_label}:** [![lint]({REPO_URL}/actions/workflows/lint.yml/badge.svg?branch=main)]({REPO_URL}/actions/workflows/lint.yml) · [{links_label}]({REPO_URL}/actions/workflows/links.yml) · [{claims_label}]({REPO_URL}/actions/workflows/claims.yml)")
    add("")
    add("---")
    add("")
    top_label = "↑ 返回顶部" if lang == "zh" else "↑ Back to top"
    add(f"**Jev Decision Atlas** · [{top_label}](#top) · [{strings['other_name']}]({strings['other_readme']})")
    add("")
    return out


SECTIONS = (
    cover_and_nav,
    what_this_is,
    what_jev_returns,
    start_here,
    coverage,
    measured_results,
    by_decision_pattern,
    by_resource_kind,
    also_in_this_repo,
    what_is_verified,
    machine_readable_data,
    contributing_and_licence,
)


def render(catalog: list[dict], retired: list[dict], strings: dict) -> str:
    """One README in the language of `strings`.

    The counts come from _stats.compute(), which reads the files on disk, so a
    test that renders a fixture patches _stats.compute as well.
    """
    by_pattern = group_by_pattern(catalog)
    by_kind: dict[str, list[dict]] = {key: [] for key in KIND_ORDER}
    for entry in catalog:
        by_kind[entry["kind"]].append(entry)
    # Counted in _stats so the badges, docs/status.md, llms.txt and the site's
    # meta tags all use one definition of "with code" or dated link records.
    stats = _stats.compute()
    page = Page(catalog, retired, strings, stats, by_pattern, by_kind)
    out: list[str] = []
    for section in SECTIONS:
        out.extend(section(page))
    return "\n".join(out)
