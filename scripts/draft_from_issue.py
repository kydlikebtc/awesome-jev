#!/usr/bin/env python3
"""Answer a new-entry issue with a first read of its repository and a draft row.

The issue form (.github/ISSUE_TEMPLATE/new-entry.yml) asks for the link, the
title, what the project decides and which primitives its code calls. Until
2026-10-24 the form ended there: issue #27 waited from 2026-09-29 until a
person read the repository, wrote the row and landed it on 2026-10-24, and the
issue never heard back. The new-entry workflow now runs this when such an issue
is opened. It reads the repository with the code the weekly discovery run uses
(discover_candidates.inspect) and writes one comment saying

- what it found: a Jev call site (the file, and the strings it matched there),
  or none in the files it read, which is not a verdict on the project;
- for a call site, a draft row: discover_drafts.draft_row's fields from GitHub
  and the code, with what the form says on top (the title, the summary, the
  primitives and the boxes ticked, the issue as its source), and `_draft`
  first, listing what a person still has to check. lint.py refuses a row that
  still has that field;
- for a repository already catalogued, retired or declined, which row, or why.

It writes nothing to the repository and opens no pull request: anyone can open
an issue, so the job that answers one only comments. A person completes the
draft and opens the pull request. Everything the issue's author wrote is quoted
inside the JSON block, where Markdown is not rendered and an @mention notifies
no one; a path from the repository is shown as inline code.

Usage:
  python3 scripts/draft_from_issue.py --event "$GITHUB_EVENT_PATH" --out comment.md
  python3 scripts/draft_from_issue.py --issue 27 --out comment.md   # read it from the API
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _github  # noqa: E402
import discover_candidates  # noqa: E402
import discover_drafts  # noqa: E402
from lint import DRAFT_FIELD, FLAGS_NEEDING_NOTES  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://kydlikebtc.github.io/awesome-jev/"
MARKER = "<!-- written by scripts/draft_from_issue.py -->"

# The form's headings, as GitHub renders an issue form: `### <label>`, a blank
# line, the answer, and `_No response_` for an optional field left empty.
FIELDS = {
    "URL": "url",
    "Title": "title",
    "What does it actually demonstrate?": "summary",
    "Does it call Jev?": "is_jev",
    "Which primitives does the code actually call?": "primitives",
    "Which decision pattern(s)?": "patterns",
    "Anything a reader deserves to know before clicking?": "caveats",
    "Notes": "notes",
    "Confirmation": "confirm",
}
READ_IT = "Yes — I read the call site"
ALTERNATIVE = "No — it is a Jev-like alternative or reimplementation"
PRIMITIVES = ("choice", "score", "noul")
OWN = "This is my own project — I wrote or maintain it (listed with the `self-submitted` flag)"
# A box that names exactly one flag sets it.
CAVEAT_FLAGS = {
    "Performance numbers in it are the vendor's, not measured": "vendor-reported",
    "It makes measurement claims I could not verify": "unverified-claims",
    "Jev is wired in but changes no behaviour (shadow mode)": "shadow-mode-only",
    "I read the code but did not run it": "code-untested",
}
# A box that names several, or a fact the weekly refresh takes from GitHub, is
# passed on for a person to decide.
CAVEAT_CHOICES = {
    "One commit, or development has visibly stopped": "`single-commit` or `archived`, which the weekly "
    "refresh sets from GitHub",
    "No LICENSE file (whatever the README badge says)": "`no-license`, which the draft already sets from "
    "GitHub's licence answer",
    "Needs early access, or a key for a third-party service": "`early-access-required` or `third-party-api-key`",
    "Paywalled, marketing content, or looks machine-written": "`paywalled`, `marketing` or `ai-generated`",
}


def parse_form(body: str) -> dict[str, str]:
    """The form's answers by field name. Only the first heading of each name
    starts its field, so a heading typed inside an answer stays in that answer."""
    sections: dict[str, list[str]] = {}
    current = None
    for line in (body or "").replace("\r\n", "\n").split("\n"):
        heading = re.fullmatch(r"### (.+?)\s*", line)
        if heading and FIELDS.get(heading.group(1)) and FIELDS[heading.group(1)] not in sections:
            current = FIELDS[heading.group(1)]
            sections[current] = []
        elif current:
            sections[current].append(line)
    answers = {key: "\n".join(lines).strip() for key, lines in sections.items()}
    return {key: "" if value == "_No response_" else value for key, value in answers.items()}


def ticked(answer: str) -> list[str]:
    """The labels of the ticked boxes in a checkboxes answer."""
    return [m.group(1).strip() for m in re.finditer(r"^- \[[xX]\] (.+)$", answer or "", re.MULTILINE)]


def one_line(text: str) -> str:
    return " ".join((text or "").split())


def fence(text: str) -> str:
    """A backtick fence longer than any run of backticks in the text, so the
    text cannot close the block it is quoted in."""
    longest = max((len(run) for run in re.findall(r"`+", text)), default=0)
    return "`" * max(3, longest + 1)


def insert_after(row: dict, after: str, key: str, value) -> dict:
    """The row with `key` placed right after `after`, every other key in place."""
    out: dict = {}
    for name, item in row.items():
        if name != key:
            out[name] = item
        if name == after:
            out[key] = value
    if key not in out:
        out[key] = value
    return out


def pattern_keys(text: str) -> list[str]:
    """The pattern keys an answer names verbatim, in patterns.json's order."""
    keys = [p["key"] for p in json.loads((ROOT / "patterns.json").read_text(encoding="utf-8"))["patterns"]]
    return [key for key in keys if re.search(rf"(?<![\w-]){re.escape(key)}(?![\w-])", text or "")]


def draft(result: dict, form: dict, issue: dict, *, taken: set[str], today: dt.date) -> dict:
    """The draft row for a repository found calling Jev: draft_row's, with the
    form's answers on top and `_draft` saying where each came from."""
    owner, name = result["url"].rstrip("/").split("/")[-2:]
    slug = discover_drafts.propose_slug(owner, name, taken)
    # sourced=True only leaves out draft_row's "sources is empty" line; the
    # issue is the source, set below.
    row = discover_drafts.draft_row(result, slug=slug, today=today, sourced=True)
    number, link = issue["number"], issue["html_url"]
    boxes = ticked(form.get("caveats", ""))
    own = OWN in boxes
    said = [f"From issue #{number}: title, summary, question_types and flags are what the issue's author "
            "wrote and ticked. Check each against the call site; the script read none of them."]

    url = (form.get("url") or "").strip()
    if repository(url) == result["slug"] and url.rstrip("/").lower() != result["url"].rstrip("/").lower():
        # A page inside the repository, as the form gave it: the one link a reader opens.
        row["url"] = url
    if form.get("title"):
        row["title"] = one_line(form["title"])
    if form.get("summary"):
        row["summary"] = one_line(form["summary"])
        said.append("summary is the issue's own words: keep what the call site bears out, and set "
                    "summary_source to curated once a person has written it.")
    primitives = [p for p in PRIMITIVES if f"`{p}`" in ticked(form.get("primitives", ""))]
    if primitives and form.get("is_jev") == READ_IT:
        row = insert_after(row, "patterns", "question_types", primitives)
    elif primitives:
        said.append(f"The issue ticked {', '.join(primitives)} but did not say it read the call site, "
                    "so question_types is left for the person who does.")
    named = pattern_keys(form.get("patterns", ""))
    if named:
        row["patterns"] = named
    if form.get("patterns"):
        said.append(f"The issue describes its pattern as: {one_line(form['patterns'])}")

    flags = list(row.get("flags", []))
    flags += [flag for label, flag in CAVEAT_FLAGS.items() if label in boxes]
    if form.get("is_jev") == ALTERNATIVE:
        row["kind"] = "alternative"
        row["evidence"] = {**row["evidence"], "kind": "wire-shape"}
        flags.append("not-jev")
        said.append("The issue says this is an alternative, not built on Jev: kind alternative, "
                    "evidence.kind wire-shape and the not-jev flag follow from that.")
    if own:
        flags.append("self-submitted")
    if flags:
        row = insert_after(row, "first_seen", "flags", list(dict.fromkeys(flags)))
    for label, choice in CAVEAT_CHOICES.items():
        if label in boxes:
            said.append(f"The issue ticked \"{label}\": that is {choice}.")
    if form.get("notes"):
        row = insert_after(row, "evidence", "notes", one_line(form["notes"]))
        said.append("notes is the issue's own Notes answer: keep only what a reader needs.")
    reasons = [flag for flag in row.get("flags", []) if flag in FLAGS_NEEDING_NOTES]
    if reasons:
        said.append(f"{', '.join(reasons)} needs a notes line saying why (lint.py fails the row without one).")
    catalog = "author submission" if own else f"community submission (issue #{number})"
    row["sources"] = [{"catalog": catalog, "url": link}]
    row[DRAFT_FIELD] = said + row[DRAFT_FIELD]
    return row


# A repository, or a page inside one (a monorepo's subdirectory, a file).
GITHUB = re.compile(r"https://github\.com/([A-Za-z0-9][\w.-]*)/([\w.-]+?)(?:\.git)?(?:[/?#].*)?")


def repository(url: str) -> str | None:
    """owner/name, lower-cased, of the GitHub repository a URL is in; None otherwise."""
    match = GITHUB.fullmatch((url or "").strip())
    return discover_candidates.only_slug(f"{match.group(1)}/{match.group(2)}") if match else None


def find_row(rows: list[dict], slug: str) -> dict | None:
    return next((row for row in rows if (_github.repo_of(row) or "").lower() == slug), None)


def comment(issue: dict, *, read=None, today: dt.date | None = None) -> str:
    """The comment for one new-entry issue. `read` is how a repository is read
    (discover_candidates.inspect unless a test says otherwise)."""
    read = read or discover_candidates.inspect
    today = today or dt.date.today()
    form = parse_form(issue.get("body") or "")
    head = [MARKER, ""]
    slug = repository(form.get("url", ""))
    if not slug:
        return "\n".join(head + [
            "This is an automatic first read, and it could not start: the URL field does not name a "
            "GitHub repository (`https://github.com/owner/name`). That is fine for an article, a video or "
            "a docs page; a maintainer reads those by hand.",
            "",
        ])

    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    retired = json.loads((ROOT / "retired.json").read_text(encoding="utf-8"))
    own = OWN in ticked(form.get("caveats", ""))
    listed = find_row(catalog, slug)
    if listed:
        lines = [f"`{slug}` is already in the catalogue, as [`{listed['slug']}`]({SITE}#{listed['slug']}). "
                 "Nothing new to add; if the row is wrong, say what here, citing the file or page."]
        if own and "self-submitted" not in (listed.get("flags") or []):
            lines.append("")
            lines.append("The form says this is your own project, and the row does not say so yet. A "
                         "maintainer adds the `self-submitted` flag with this issue as its source, so every "
                         "surface discloses it.")
        return "\n".join(head + lines + [""])
    gone = find_row(retired, slug)
    if gone:
        return "\n".join(head + [
            f"`{slug}` was catalogued as `{gone['slug']}` and later retired (`retired.json`), with this "
            "note:", "", f"> {one_line(gone.get('notes', '')) or '(no note)'}", "",
            "If that no longer holds, say what changed and a maintainer reads it again.", "",
        ])
    declined = discover_candidates.read_declined()
    if slug in declined:
        return "\n".join(head + [
            f"`{slug}` was read and declined before (`docs/declined.txt`): "
            f"{declined[slug] or 'no reason was recorded'}. If that no longer holds, say what changed.", "",
        ])

    result = read(slug)
    if result.get("verdict") != discover_drafts.PROPOSED:
        why = {
            "repo-gone": "GitHub did not return the repository: it may be private, renamed or deleted.",
            "tree-unavailable": "GitHub did not list the repository's files.",
            "mentions-only": "its README mentions Jev, but none of the files read calls it.",
            "no-signal": "none of the files read mentions Jev.",
        }.get(result.get("verdict"), f"its verdict was {result.get('verdict')}.")
        return "\n".join(head + [
            f"This is an automatic first read of `{slug}`, not a review, and it found no Jev call site: {why}",
            "",
            "That is not a verdict on the project: the script reads a few dozen files and looks for the "
            "endpoint, the SDK and the model names. If you know the file that calls Jev, reply with its "
            "path, and a maintainer reads it.",
            "",
        ])

    taken = discover_drafts.catalogue_slugs()
    row = draft(result, form, issue, taken=taken, today=today)
    text = json.dumps(row, indent=2, ensure_ascii=False)
    marks = fence(text)
    path = result["evidence_path"]
    found = ", ".join(f"`{discover_candidates.code_span(s)}`" for s in result["matched"])
    test = (" It looks like a test file, so the call site in the implementation is the one to cite."
            if result.get("evidence_is_test") else "")
    return "\n".join(head + [
        f"This is an automatic first read of `{slug}`, not a review: a maintainer still reads the call "
        "site before anything is added.",
        "",
        f"**Call site:** [`{discover_candidates.code_span(path)}`]"
        f"({discover_candidates.blob_url(result['url'], path)}), where the script found {found}.{test}",
        "",
        "Below is a draft row, built from GitHub, that file and this form. It is not in the catalogue: "
        f"its `{DRAFT_FIELD}` field lists what a person still checks, and `lint.py` refuses the row "
        "until that field is deleted.",
        "",
        "<details><summary>Draft row</summary>",
        "",
        f"{marks}json",
        text,
        marks,
        "",
        "</details>",
        "",
        "To add it yourself, complete the draft, add it to `catalog.json`, run "
        "`python3 scripts/check.py --fix` and open a pull request: the template's first checklist is "
        f"what one row needs, and `Closes #{issue['number']}` in its description closes this issue when "
        "the row lands. Or leave it here, and a maintainer will.",
        "",
    ])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--event", metavar="FILE", help="the `issues` event payload ($GITHUB_EVENT_PATH)")
    source.add_argument("--issue", metavar="NUMBER", help="read this issue from the API instead")
    parser.add_argument("--out", required=True, metavar="FILE", help="write the comment here")
    args = parser.parse_args(argv)

    if args.event:
        issue = json.loads(pathlib.Path(args.event).read_text(encoding="utf-8")).get("issue") or {}
    else:
        if not re.fullmatch(r"[1-9]\d{0,6}", args.issue.strip()):
            print(f"error: --issue takes an issue number, not {args.issue!r}", file=sys.stderr)
            return 2
        repo = os.environ.get("GITHUB_REPOSITORY") or _github.SELF
        issue = _github.api_get(f"/repos/{repo}/issues/{args.issue.strip()}") or {}
    if not isinstance(issue.get("number"), int) or "pull_request" in issue:
        print("error: no issue to answer", file=sys.stderr)
        return 2

    pathlib.Path(args.out).write_text(comment(issue), encoding="utf-8")
    output = os.environ.get("GITHUB_OUTPUT")
    if output:
        with open(output, "a", encoding="utf-8") as handle:
            handle.write(f"number={issue['number']}\n")
    print(f"wrote the comment for issue #{issue['number']} to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
