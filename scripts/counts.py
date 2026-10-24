#!/usr/bin/env python3
"""Print catalog statistics.

Runs in CI so every build logs the shape of the catalog, which makes coverage
gaps visible over time: a pattern with zero entries is a research to-do, not a
rendering bug.

Run: python3 scripts/counts.py
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _stats  # noqa: E402


def block(title: str, counts: dict, universe: list[str] | None = None) -> None:
    """One breakdown, in the order `counts` gives (shape()'s: most first, then
    by name), or in `universe`'s with a gap marked."""
    print(f"\n{title}")
    if universe is not None:
        for key in universe:
            count = counts.get(key, 0)
            bar = "#" * count
            mark = " " if count else "!"
            print(f"  {mark} {key:<24} {count:>3} {bar}")
        missing = [key for key in universe if not counts.get(key)]
        if missing:
            print(f"    no entries yet: {', '.join(missing)}")
    else:
        for key, count in counts.items():
            print(f"    {key:<24} {count:>3} {'#' * count}")
        if not counts:
            print("    (none)")


def shape_lines(shape: dict) -> list[str]:
    """The breakdowns docs/shape.md publishes that are not a single tally."""
    from readme.rows import STAR_BANDS

    bands = ["<10", *(name.removeprefix("★") for _, name in STAR_BANDS)]
    lines = ["", "by platform group (docs/shape.md)"]
    lines += [f"    {tier:<24} {n:>4}" for tier, n in shape["platform_tiers"].items()]
    lines += ["", "stars by kind, rows per band (" + " ".join(bands) + "); median band"]
    for kind, row in shape["stars_by_kind"].items():
        if row["rows"]:
            median = "—" if row["median_band"] is None else bands[row["median_band"]]
            counted = " ".join(str(n) for n in row["bands"])
            lines.append(f"    {kind:<14} {row['with_stars']:>4} of {row['rows']:<4} {counted:<24} {median}")
    top = shape["top_languages"]
    lines += ["", f"languages by pattern ({', '.join(top)}, other)"]
    for key, langs in shape["languages_by_pattern"].items():
        cells = [str(langs.get(lang, 0)) for lang in top] + [str(sum(n for k, n in langs.items() if k not in top))]
        lines.append(f"    {key:<20} {' '.join(f'{c:>4}' for c in cells)}")
    lines += ["", f"patterns filed together ({shape['multi_pattern_rows']} rows carry more than one)"]
    lines += [f"    {a} + {b}: {n}" for a, b, n in shape["pattern_pairs"]]
    a = shape["authors"]
    lines += [
        "",
        f"authors        {a['authors']} named on {a['rows_naming_an_author']} rows: {a['one_row']} with one row, "
        f"{a['two_rows']} with two, {a['three_or_more_rows']} with three or more (most by one: "
        f"{a['most_rows_by_one_author']}); no name is published",
    ]
    return lines


def main() -> int:
    # Every number here is _stats': the headline ones from compute(), the
    # breakdowns from shape(), which docs/shape.md publishes. Nothing is
    # counted in this file.
    stats = _stats.compute()
    shape = _stats.current_shape()

    print(f"catalog.json   {stats['entries']} entries")
    print(f"retired.json   {stats['retired']} entries")
    print(f"with code      {stats['with_code']}")
    print(f"official       {stats['official']}")
    print(
        f"evidence       {stats['call_site_rows']} call-site, {stats['wire_shape_rows']} wire-shape, "
        f"{stats['example_only_rows']} example-only"
    )
    print(f"code, no cite  {stats['has_code_unbacked']} (neither evidence nor evidence_none)")
    print(
        f"primitives     {stats['primitive_rows'] - stats['primitive_rows_model']} read by a person, "
        f"{stats['primitive_rows_model']} by a model (question_types), "
        f"{stats['primitive_signal_rows']} with a text signal in the cited file (primitives_seen), "
        f"{stats['primitive_signal_only_rows']} of them with no question_types"
    )
    print(
        f"review queue   {stats['review_examples_dir']} under examples/, "
        f"{stats['review_single_model_name']} on one model name or host, "
        f"{stats['review_tool_selection_broad']} tool-selection on dropped keywords, "
        f"{stats['review_generic_summary']} summaries naming nothing about Jev (docs/review-queue.md)"
    )
    print(
        f"patterns       {stats['patterns_rule_identical']} equal the keyword rules' suggestion (no review recorded), "
        f"{stats['patterns_reviewed']} patterns_reviewed, {stats['overview_unindexed']} overview rows with code "
        "not yet indexed by pattern"
    )
    print(
        f"summaries      {stats['summary_upstream']} upstream-description, "
        f"{stats['summary_upstream_stale']} upstream-description-stale, {stats['summary_curated']} curated, "
        f"{stats['summary_model_written']} model-written, {stats['summary_unlabelled']} unlabelled (summary_source)"
    )
    model = stats["model_read"]
    print(
        f"model-read     {model['patterns']} patterns, {model['evidence']} call sites, "
        f"{model['measurement']} measurements, {model['wire']} interfaces, {model['thresholds']} threshold rows "
        "read only by a model (model_read_on; docs/review-queue.md#model-read)"
    )
    last_pushes = ", ".join(f"{month} {count}" for month, count in stats["pushed_by_month"].items()) or "none"
    print(
        f"repositories   {stats['repo_facts_rows']} with GitHub's creation date, last push and commit count, "
        f"{stats['single_commit_rows']} single-commit; last push by month (UTC): {last_pushes}"
    )
    directions = ", ".join(f"{key} {count}" for key, count in stats["measurement_directions"].items())
    print(
        f"measurements   {stats['measured_rows']} benchmark rows index their author's measurement "
        f"(author-stated directions: {directions}), {stats['review_measurement_unread']} read by nobody; "
        f"{stats['independent_reports']} independent reports (benchmarks not flagged vendor-reported)"
    )
    ranges = "; ".join(
        f"{group} {r['low']:g}–{r['high']:g} ({r['rows']} rows)" for group, r in stats["threshold_ranges"].items()
    ) or "none"
    print(
        f"thresholds     {stats['thresholds_recorded']} constants on {stats['threshold_rows']} rows compared with "
        f"a Jev answer (observed_thresholds; observations, not recommendations), "
        f"{stats['review_thresholds_unread']} rows read by nobody: {ranges}"
    )
    print(
        f"citations      {stats['cited_rows']} of {stats['citable_rows']} rows with a GitHub repository "
        "linked by at least one sibling directory (sources; a count of mentions, not a review)"
    )
    if stats["entries"]:
        print(f"zh hand-written {stats['zh_hand']}/{stats['entries']}")

    # The repository description is the one published sentence CI cannot rewrite
    # (description.yml files an issue when it drifts), so every run, a pull
    # request's included, shows what it should say once this tree is on main. It
    # changes only when the count crosses a hundred or pitch_public() is reworded.
    print(
        "\nrepository description once merged (count floored to the hundred; "
        f"next changes at {_stats.next_public_change(stats['entries']):,} entries):"
    )
    print(f"  {_stats.pitch_public(stats)}")

    block("by pattern (! = gap)", shape["by_pattern"], list(shape["by_pattern"]))
    block("by kind (! = gap)", shape["kinds"], list(shape["kinds"]))
    block("by language", shape["languages"])
    block("by platform", shape["platforms"])
    block("by question type", shape["question_types"])
    block("flags", shape["flags"])
    block("declared licence (repo_license)", shape["licences"])
    print("\n".join(shape_lines(shape)))
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
