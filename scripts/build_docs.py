#!/usr/bin/env python3
"""Refill every generated number and table inside the hand-written docs.

The README was always generated. The docs around it were not, and every one of
them froze at the first build: status.md said 148 entries and listed
`retry-control` as a pattern nobody had published, sources.md warned that
fourteen linked projects had no licence when the real number was 171, and the
site's link-preview text still said 148. None of that was ever wrong on the day
it was written. It became wrong silently, which is worse.

The site's link-preview tags are no longer here: since 2026-09-27 they are
written at deploy by `assemble_site.py --deploy`, and git keeps a placeholder.

The rule this enforces: a number describing the catalogue may appear only where
something re-derives it. Here that means one of

  * a block — `<!-- name:start -->` … `<!-- name:end -->` — whose whole body is
    generated (a table or a list), or
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
import json
import pathlib
import re
import sys
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _stats  # noqa: E402
from _markers import normalise, replace_block, replace_inline  # noqa: E402
from measurements import negative as negative_rows  # noqa: E402
from platform_values import load_query  # noqa: E402
from sibling_lists import SIBLINGS, citations_of, is_citation, listed_urls, read_lists  # noqa: E402
from thresholds import number as threshold_number  # noqa: E402

ROOT = _stats.ROOT

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


def model_check_cell(check: dict | None) -> str:
    if not check:
        return "not yet sampled"
    return f"{check['agreed']} of {check['sampled']} ({check['month']})"


def shape_block(s: dict) -> str:
    return table(
        ["", ""],
        [
            ["Entries", s["entries"]],
            ["Carrying code", s["with_code"]],
            ["Official (TypeSafe AI's own)", s["official"]],
            ["Links with a dated 2xx response record", s["link_ok"]],
            ["Most recent successful link-check date (dates vary by row)", s["last_sweep"]],
            ["Rows whose latest successful check is on that date", f"{s['sweep_coverage']} of {s['entries']}"],
            ["Rows citing a file where the project calls Jev (`evidence`; not a CI pass count)", s["call_site_rows"]],
            ["Rows citing a file that speaks Jev's request shape rather than building on Jev (`evidence.kind` `wire-shape`)", s["wire_shape_rows"]],
            ["Rows citing only an example the project ships (`evidence.kind` `example-only`)", s["example_only_rows"]],
            ["Rows with code citing no file and giving no reason (neither `evidence` nor `evidence_none`)", s["has_code_unbacked"]],
            ["Rows naming the primitives a person read the code calling (`question_types`)", s["primitive_rows"] - s["primitive_rows_model"]],
            ["Rows naming the primitives a model read the code calling (`question_types` on a row whose call site only a model has read, since 2026-10-24)", s["primitive_rows_model"]],
            ["Machine text signal: rows whose cited file contains a primitive's request or answer shape (`primitives_seen`; not a reading, never counted as `question_types`)", s["primitive_signal_rows"]],
            ["Of those, rows with no `question_types`: the text signal is all that is recorded about their primitives", s["primitive_signal_only_rows"]],
            ["Machine text signal: rows whose cited file uses an experimental Jev feature, Box or an opt-in header (`experimental_seen`; not one of the three primitives; [review queue](review-queue.md#experimental))", s["experimental_rows"]],
            ["Rows the README prints by name (*Start here*, the first reports under *Measured, not claimed*, the first rows of each pattern) still lacking a person's summary, Chinese or reading of the cited file ([review queue](review-queue.md#front-page))", f"{s['review_front_page']} of {s['front_page_rows']}"],
            ["Machine signal: evidence under an examples directory, not yet judged ([review queue](review-queue.md#examples-dir))", s["review_examples_dir"]],
            ["Machine signal: evidence resting on one model name or the API host ([review queue](review-queue.md#single-model-name))", s["review_single_model_name"]],
            ["Machine signal: `tool-selection` suggested only by keyword-rule words dropped on 2026-09-27 ([review queue](review-queue.md#tool-selection-broad-words))", s["review_tool_selection_broad"]],
            ["Machine signal: rows with code, not TypeSafe AI's own, whose summary names nothing about Jev and that carry no `notes` ([review queue](review-queue.md#generic-summary))", s["review_generic_summary"]],
            ["Benchmark rows indexing their own author's measurement (`measurement`: task, datasets, comparators, the author's direction; author-stated, not reproduced here; [side by side](benchmarks.md))", s["measured_rows"]],
            ["Machine signal: of those, measurements nobody has read against the author's report, neither a person nor a model ([review queue](review-queue.md#measurement-unread))", s["review_measurement_unread"]],
            ["Of those measured rows, measurements only a model has read against the report (`measurement.model_read_on`; [review queue](review-queue.md#model-read))", s["model_read"]["measurement"]],
            ["Rows recording thresholds their cited file compares a Jev answer with (`observed_thresholds`: each a constant written in that file; what one project chose, not a recommendation)", s["threshold_rows"]],
            ["Machine signal: of those, rows with a threshold nobody has read in the file, neither a person nor a model ([review queue](review-queue.md#thresholds-unread))", s["review_thresholds_unread"]],
            ["Of those rows, rows whose thresholds were all read, some only by a model (`model_read_on`; [review queue](review-queue.md#model-read))", s["model_read"]["thresholds"]],
            ["Negative results: rows whose own author measured Jev for the use and concluded against it (a benchmark's `measurement.direction` unfavourable, the `negative-result` flag on any other row; author-stated, not reproduced here; [listed below](#negative-results))", s["negative_results"]],
            ["Patterns covered", f"{s['patterns_covered']} of {s['patterns_total']}"],
            ["Rows whose `patterns` are exactly what the keyword rules suggest for their summary (agreement with the rules, not a review: any review of these rows was not recorded)", f"{s['patterns_rule_identical']} of {s['entries']}"],
            ["Rows whose patterns a person recorded reading (`patterns_reviewed`)", s["patterns_reviewed"]],
            ["Rows whose patterns only a model recorded reading (`patterns_model_read_on`, since 2026-10-24; shown as a model's reading; [review queue](review-queue.md#model-read))", s["model_read"]["patterns"]],
            ["Rows whose call site only a model recorded reading (`evidence.model_read_on`; [review queue](review-queue.md#model-read))", s["model_read"]["evidence"]],
            ["Of a monthly sample of those rows, how many a person agreed with (`scripts/model_sample.py`, [docs/model-checks.json](model-checks.json); agreeing is not reading the file)", model_check_cell(s["model_checks"])],
            ["Alternatives whose interface records were read in every cited file, some only by a model (`wire.source[].model_read_on`; [review queue](review-queue.md#model-read))", s["model_read"]["wire"]],
            ["Overview rows that are projects or plugins with code, listed apart as not yet indexed by pattern ([review queue](review-queue.md#unsorted-overview))", s["overview_unindexed"]],
            ["Summaries that are the project's own GitHub description (`summary_source` `upstream-description`)", f"{s['summary_upstream']} of {s['entries']}"],
            ["Summaries taken from that description that no longer match it (`upstream-description-stale`)", s["summary_upstream_stale"]],
            ["Summaries marked as written for this catalogue by a person (`curated`)", s["summary_curated"]],
            ["Summaries marked as written for this catalogue by a model (`model-written`, since 2026-10-24)", s["summary_model_written"]],
            ["Chinese summaries hand-written", f"{s['zh_hand']} of {s['entries']}"],
            ["Rows recording GitHub's creation date, last push and default-branch commit count for their repository (`repo_created_at`, `repo_pushed_at`, `repo_commits`; GitHub's facts at the last weekly refresh, not a judgement of upkeep)", f"{s['repo_facts_rows']} of {s['entries']}"],
            ["Rows flagged `single-commit`: one commit on the default branch (the refresh sets and clears it from `repo_commits`)", s["single_commit_rows"]],
            ["Rows with a GitHub repository that at least one sibling directory links (`sources` citations, from the lists' READMEs at the last weekly read; a count of mentions, not a review)", f"{s['cited_rows']} of {s['citable_rows']}"],
            ["Retired links", s["retired"]],
        ],
    )


# How the cited-by table groups the number of sibling directories linking a
# row: exact while small, then in ranges, so a row gaining one more list moves
# the table only when it crosses a range. (lower, upper); None = no upper bound.
CITED_BY_RANGES = ((0, 0), (1, 1), (2, 2), (3, 5), (6, 10), (11, 20), (21, None))


def cited_by_block(s: dict) -> str:
    """Rows with a GitHub repository, by how many sibling directories link it."""
    counts = s["cited_by"]
    if not counts:
        return "No row names a GitHub repository."
    rows = []
    for low, high in CITED_BY_RANGES:
        n = sum(rows_ for cited, rows_ in counts.items() if int(cited) >= low and (high is None or int(cited) <= high))
        label = str(low) if low == high else f"{low} or more" if high is None else f"{low}–{high}"
        rows.append([label, n])
    return table(["Sibling directories linking the repository", "Rows"], rows)


SITE = "https://kydlikebtc.github.io/awesome-jev/"


def negative_block(catalog: list[dict]) -> str:
    """Every negative result, most-starred band first, then by title and slug:
    the row, its kind, its other caveat flags (they travel with every row),
    and where the catalogue records that its own author concluded against Jev.
    Never the file's order, never an exact star count."""
    from readme.rows import FLAG_ORDER, star_band

    query = load_query()
    rows = sorted(
        negative_rows(catalog), key=lambda e: (-star_band(e.get("stars")), e["title"].lower(), e["slug"])
    )
    if not rows:
        return "No row records a negative result yet."
    lines = []
    for entry in rows:
        link = f"[{entry['title']}]({SITE}?lang=en#{entry['slug']})"
        flags = entry.get("flags") or []
        if query.NEGATIVE_FLAG in flags:
            how = "flagged `negative-result` (measured, not adopted)"
        else:
            how = "its measurement's direction is `unfavourable`"
        others = [f"`{flag}`" for flag in FLAG_ORDER if flag in flags and flag != query.NEGATIVE_FLAG]
        caveats = f"; caveats: {', '.join(others)}" if others else ""
        lines.append(f"- {link} (`{entry['kind']}`{caveats}): {how}; author-stated, not reproduced here.")
    return "\n".join(lines)


def pushed_block(s: dict) -> str:
    """Rows per calendar month of their repository's last push, newest first.
    Absolute months, never an age: the table changes only when a push lands
    in a new month, and says nothing about whether anything is maintained."""
    months = s["pushed_by_month"]
    if not months:
        return "No row records a last push yet."
    return table(
        ["Month of the last push (UTC)", "Rows"],
        [[month, count] for month, count in months.items()],
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


# The one line docs/sources.md's table gives every sibling-list citation
# together; the table under it names each list. Separate rows for the
# fifty-odd lists would bury every other source.
CITATIONS_ROW = "Sibling directories linking the row's repository (one `owner/name` item per list, read weekly)"
CITATIONS_ANCHOR = "[each list, below](#sibling-directories-linking-catalogued-repositories)"


def sources_block(catalog: list[dict]) -> str:
    counts: Counter = Counter()
    urls: dict[str, set] = {}
    for entry in catalog:
        # A row citing one source twice still counts once for that source.
        for source in {s["catalog"]: s for s in entry["sources"] if not is_citation(s)}.values():
            counts[source["catalog"]] += 1
            urls.setdefault(source["catalog"], set()).add(source["url"])
    rows = [
        [name, f"<{next(iter(urls[name]))}>" if len(urls[name]) == 1 else "various", n]
        for name, n in counts.items()
    ]
    cited_rows = sum(1 for entry in catalog if citations_of(entry))
    if cited_rows:
        rows.append([CITATIONS_ROW, CITATIONS_ANCHOR, cited_rows])
    rows.sort(key=lambda row: (-row[2], row[0].lower()))
    return table(["Source", "URL", "Rows"], rows)


def citations_block(catalog: list[dict], listed: list[str]) -> str:
    """Every list docs/sibling-lists.txt names, with how many catalogued rows'
    repositories it links: the lists' names and URLs, nothing of their text."""
    counts = Counter(url for entry in catalog for url in citations_of(entry))
    urls = [*listed, *(url for url in counts if url not in listed)]
    urls.sort(key=lambda url: (-counts.get(url, 0), url.lower()))
    rows = [[f"[{url.removeprefix('https://github.com/')}]({url})", counts.get(url, 0)] for url in urls]
    return table(["Sibling directory", "Catalogued rows whose repository its README links"], rows)


def licences_block(shape: dict) -> str:
    """Declared licences, as _stats.shape() counts them (counts.py prints the same)."""
    rows = [[LICENCE_LABEL.get(lic, lic), n] for lic, n in shape["licences"].items()]
    return table(["Licence", "Repositories"], rows)


def row_licences_block(s: dict, catalog: list[dict]) -> str:
    """Whose words the summaries are, and what the per-row licence covers.

    Until 2026-09-27 this said every row being CC0 meant no descriptive text was
    inherited — while most summaries were the linked project's own GitHub
    description, copied. Now the split comes from summary_source, counted by
    _stats. Facts only: who wrote the words and what this repository claims.
    """
    quoted = s["summary_upstream"] + s["summary_upstream_stale"]
    labels = {
        item["key"]: item["en"]
        for item in json.loads((ROOT / "taxonomy.json").read_text())["summary_sources"]
    }
    parts = []
    if quoted:
        parts.append(
            f"{s['summary_upstream']} of the {s['entries']} summaries in `catalog.json` are the linked "
            "project's own GitHub description, word for word apart from letter case, spacing and a "
            "final full stop (`summary_source: upstream-description`), and "
            f"{s['summary_upstream_stale']} more were taken from such a description and no longer "
            "match it (`upstream-description-stale`). The projects' authors wrote those words and the "
            "copyright in them is theirs: this repository does not dedicate them under `CC0-1.0`. "
            f"{s['summary_upstream_zh_machine']} of their Chinese counterparts are machine translations "
            "of them (`zh_machine`); the Chinese of such a row translates the project's words, and this "
            "repository does not dedicate it under `CC0-1.0` either. The READMEs, the pattern pages and "
            "the site mark each such summary "
            f"*({labels['upstream-description']})* or *({labels['upstream-description-stale']})*."
        )
    parts.append(
        f"{s['summary_curated']} summaries are marked `curated`: written for this catalogue by a person. "
        f"{s['summary_model_written']} are marked `model-written`: written for it by a model, and marked "
        f"*({labels['model-written']})* wherever they are shown. The other {s['summary_unlabelled']} carry "
        "no `summary_source`, so where their words come from is not recorded row by row."
    )
    by = Counter(e["license"] for e in catalog)
    scope = (
        "covers the row's structured metadata (slug, kind, patterns, flags, dates, counts, evidence "
        "records and the rest) and any text written for this catalogue, not a summary labelled as "
        "the project's own description or the Chinese translation of one."
    )
    if set(by) == {"CC0-1.0"}:
        parts.append(f"Every row's `license` field is `CC0-1.0`. It {scope}")
    else:
        parts.append(
            f"{by.get('CC0-1.0', 0)} rows are `CC0-1.0`; {by.get('CC-BY-4.0', 0)} are "
            "`CC-BY-4.0` because their descriptive text was inherited from a CC BY 4.0 "
            "source, and the attribution is that row's `sources` array. Either way the "
            f"field {scope}"
        )
    return "\n\n".join(parts)


# ---- patterns.md -----------------------------------------------------------


def catalogued_block(key: str, n: int, lang: str) -> str:
    """The line closing a pattern's section of the patterns page: how many rows
    the catalogue files under the pattern, the page listing every one of them
    (docs/by-pattern/, written only while there are rows) and the site's
    filter, in the page's language."""
    from readme.rows import PATTERN_LABELS, label, page_name, site_link

    name, site = label(PATTERN_LABELS, key, lang), site_link(key, lang)
    page = f"by-pattern/{page_name(key, lang)}"
    # A practice review (docs/practice/, build_practice.py), where one is written.
    practice = (ROOT / "docs" / "practice" / f"{key}.md").exists()
    if lang == "zh":
        review = f" · [实践综述（模型撰写，附中文要点）](practice/{key}.md)" if practice else ""
        if not n:
            return f"目录中的**{name}**：暂无条目 · [站点筛选]({site}){review}。"
        return f"目录中的**{name}**：共 {n} 条，[逐条列出并附警示]({page}) · [站点筛选]({site}){review}。"
    review = f" · [how projects do it, written by a model](practice/{key}.md)" if practice else ""
    if not n:
        return f"**{name}** in the catalogue: no rows yet · [the site's filter]({site}){review}."
    rows = "1 row, [listed with its caveats]" if n == 1 else f"{n} rows, [each listed with its caveats]"
    return f"**{name}** in the catalogue: {rows}({page}) · [the site's filter]({site}){review}."


def pattern_blocks(s: dict, patterns: list[dict], lang: str) -> dict[str, str]:
    """One `catalogued-<key>` block per pattern in patterns.json, for
    docs/patterns.md (`en`) or its Chinese rendering docs/patterns.zh-CN.md
    (`zh`). A section without its markers fails the build (replace_block), and
    lint_docs checks each block sits in its own `## key` section."""
    return {f"catalogued-{p['key']}": catalogued_block(p["key"], s["by_pattern"][p["key"]], lang) for p in patterns}


# ---- driver ----------------------------------------------------------------

# The two ranges SKILL.md and examples/README.md state instead of a typed
# "0.3 to 0.9": (inline key part, _stats threshold_ranges group). Never one
# range across both: a noul probability is not a choice confidence.
THRESHOLD_RANGES = (("noul", "noul probability"), ("choice", "choice confidence"))


def threshold_values(s: dict) -> dict[str, object]:
    """Inline values for what catalogued files compare Jev's answers with
    (observed_thresholds): rows, thresholds, rows no person has checked (no
    reading recorded, or only a model's), and per THRESHOLD_RANGES group its
    rows and lowest and highest constant."""
    out: dict[str, object] = {
        "threshold_rows": s["threshold_rows"],
        "thresholds_recorded": s["thresholds_recorded"],
        "thresholds_unchecked": s["review_thresholds_unread"] + s["model_read"]["thresholds"],
    }
    for key, group in THRESHOLD_RANGES:
        found = s["threshold_ranges"].get(group, {})
        out[f"threshold_{key}_rows"] = found.get("rows", 0)
        out[f"threshold_{key}_low"] = threshold_number(found.get("low"))
        out[f"threshold_{key}_high"] = threshold_number(found.get("high"))
    return out


def inline_values(s: dict) -> dict[str, object]:
    return {
        **threshold_values(s),
        "entries": s["entries"],
        "with_code": s["with_code"],
        "official": s["official"],
        "link_ok": s["link_ok"],
        "link_unstamped": s["link_unstamped"],
        "last_sweep": s["last_sweep"],
        "sweep_coverage": s["sweep_coverage"],
        "call_site_rows": s["call_site_rows"],
        "wire_shape_rows": s["wire_shape_rows"],
        "example_only_rows": s["example_only_rows"],
        "primitive_rows": s["primitive_rows"],
        "primitive_rows_cited": s["primitive_rows_cited"],
        "primitive_signal_rows": s["primitive_signal_rows"],
        "primitive_signal_only_rows": s["primitive_signal_only_rows"],
        "measured_rows": s["measured_rows"],
        "negative_results": s["negative_results"],
        "no_licence": s["no_licence"],
        "platforms": s["platforms"],
        "sibling_lists": s["sibling_lists"],
        "cited_rows": s["cited_rows"],
        "patterns_total": s["patterns_total"],
        "patterns_rule_identical": s["patterns_rule_identical"],
        "patterns_reviewed": s["patterns_reviewed"],
        "overview_unindexed": s["overview_unindexed"],
        "zh_hand": s["zh_hand"],
        "zh_machine": s["zh_machine"],
        "kinds": ", ".join(s["kinds"]),
        "pattern_keys": ", ".join(s["pattern_keys"]),
        "fields": ", ".join(s["fields"]),
    }


def render() -> dict[pathlib.Path, str]:
    catalog, _, patterns, compat, schema = _stats.load()
    s = _stats.compute()
    shape = _stats.shape(catalog, patterns, compat, schema)
    values = inline_values(s)

    blocks = {
        "docs/status.md": {
            "shape": shape_block(s),
            "pushed": pushed_block(s),
            "cited-by": cited_by_block(s),
            "negative": negative_block(catalog),
            "gaps": gaps_block(s, patterns),
        },
        "docs/sources.md": {
            "sources": sources_block(catalog),
            "citations": citations_block(catalog, listed_urls(read_lists(SIBLINGS))),
            "licences": licences_block(shape),
            "row-licences": row_licences_block(s, catalog),
        },
        "llms.txt": {},
        "docs/patterns.md": pattern_blocks(s, patterns, "en"),
        "docs/patterns.zh-CN.md": pattern_blocks(s, patterns, "zh"),
        # Inline values only: the threshold ranges a hand-typed number stated.
        "skills/awesome-jev/SKILL.md": {},
        "examples/README.md": {},
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
        print(
            "generated values in docs/status.md, docs/sources.md, docs/patterns.md, docs/patterns.zh-CN.md, "
            "llms.txt, skills/awesome-jev/SKILL.md and examples/README.md are up to date"
        )
        return 0

    print(("rewrote " + ", ".join(rel)) if stale else "nothing to update")
    return 0


if __name__ == "__main__":
    sys.exit(main())
