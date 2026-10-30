#!/usr/bin/env python3
"""Start and check a row a model drafts from the discovery queue (E1).

Since 2026-10-24 the scheduled drafting runs (a daily one and the Thursday
upkeep) read candidates from issue #14 and add rows a model wrote: the C2 tier,
`evidence.model_read_on`, `summary_source: model-written`, `zh_machine`, and a
sentence in the notes saying no maintainer has read the call site. Until
2026-10-30 each run rebuilt those fields by hand from a helper that lived in its
own session and was lost with it, and the rules it checked (a summary of at most
300 characters, every matched string still in the cited file, none of a
person's fields) were the run's memory, not the repository's.

This script keeps both halves here, without the GitHub API, which the runs
cannot reach for other repositories: everything it reads comes from
raw.githubusercontent.com and the repository's own files.

    python3 scripts/model_draft.py OWNER/NAME PATH [--out drafts]

reads PATH, the file the model found the call in, refuses a candidate already
catalogued, retired, declined or held (docs/held.txt), and writes
drafts/<slug>.json: the row with what a script knows filled in (the model
tier's fields, the strong signals the file contains as `evidence.matched`, the
notes' closing sentence in both languages) and a `_draft` field listing what is
left for the model to write. lint.py refuses any row that still has it.

    python3 scripts/model_draft.py --check FILE [FILE ...]

checks a finished row (or a JSON array of them) before it goes into
catalog.json: the schema and lint's rules for one row, the model tier's fields
and nothing of a person's (`evidence.read_on`, `patterns_reviewed`,
`summary_source: curated`), the notes' sentence in both languages, a slug and
URL not already used, and every string in `evidence.matched` still in the cited
file at HEAD (`--no-fetch` skips that read). Exit 1 when anything is wrong.

Neither half reads the code for anyone. A row that passes --check is still a
model's reading, shown as one everywhere (docs/review-queue.md#model-read).
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import held as held_file  # noqa: E402
import lint  # noqa: E402
from _github import raw_get, repo_of, strong_signals  # noqa: E402
from discover_candidates import TEST_PATH, parse_declined  # noqa: E402
from discover_drafts import SOURCE, catalogue_slugs, languages_of, propose_slug  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
MATCHED_MAX = 3
NOTE_EN = (
    "Row drafted from the discovery queue (issue #14) by an AI assistant that read the README "
    "and the cited file on {day}; a maintainer has not yet read the call site."
)
NOTE_ZH = "本条目由 AI 助手根据发现队列（issue #14）起草，于 {day} 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。"
# What the notes must say, whatever else they add: the date-free part of each.
SAID_EN = "by an AI assistant"
SAID_ZH = "AI 助手"
# A person's fields: a model's reading never sets them (C2, 2026-10-24).
PERSON_FIELDS = ("patterns_reviewed",)
PERSON_EVIDENCE = ("read_on",)


def files(root: pathlib.Path = ROOT) -> dict:
    """What a check reads besides the row: the two row files, the schema,
    compat.json and taxonomy.json, docs/declined.txt and docs/held.txt."""

    def read(name: str, default):
        path = root / name
        return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default

    declined = root / "docs" / "declined.txt"
    held, _ = held_file.load(root / "docs" / "held.txt")
    return {
        "catalog": read("catalog.json", []),
        "retired": read("retired.json", []),
        "schema": read("schema/entry.schema.json", {}),
        "compat": read("compat.json", None),
        "taxonomy": read("taxonomy.json", None),
        "declined": parse_declined(declined.read_text(encoding="utf-8")) if declined.exists() else {},
        "held": held,
    }


def url_key(url: str) -> str:
    return str(url or "").rstrip("/").lower()


def settled(repo: str, known: dict) -> str:
    """Why OWNER/NAME should not get a new row, or "" when nothing says so."""
    key = repo.lower()
    url = url_key(f"https://github.com/{repo}")
    for label, rows in (("catalogued", known["catalog"]), ("retired", known["retired"])):
        for row in rows:
            if url_key(row.get("url")) == url or (repo_of(row) or "").lower() == key:
                return f"already {label} as {row.get('slug')}"
    if key in known["declined"]:
        return f"declined in docs/declined.txt: {known['declined'][key] or 'no reason given'}"
    if key in known["held"]:
        return f"held for a person in docs/held.txt: {known['held'][key] or 'no reason given'}"
    return ""


def instructions(repo: str, path: str, found: list[str], *, today: dt.date) -> list[str]:
    """The `_draft` field: what the script filled in and what the model writes."""
    day = today.isoformat()
    lines = [
        f"Draft written by scripts/model_draft.py on {day}, not a catalog row: lint.py refuses "
        "any row that still has this field.",
    ]
    if found:
        lines.append(
            f"evidence.matched holds the call-site strings the script found in {path}: "
            + ", ".join(json.dumps(s, ensure_ascii=False) for s in found)
            + ". Widen each to the line it sits in if that says more, as long as it stays an "
            "exact substring of the file, and keep at most six."
        )
    else:
        lines.append(
            f"{path} holds none of the strings the discovery run calls a Jev call site "
            "(_github.strong_signals). Cite the file that builds the request, and put exact "
            "substrings of it in evidence.matched."
        )
    if TEST_PATH.search(path):
        lines.append(
            "That path looks like a test or a fake. Find the file that sends the real request "
            "and cite it instead."
        )
    lines += [
        "Read the README and the cited file, then write summary (at most 300 characters: what "
        "the project asks Jev to decide) and summary_zh. Fill kind and patterns; add "
        "question_types for the primitives the code sends and platforms for how it reaches Jev. "
        "A project speaking Jev's wire shape without calling Jev is kind alternative with "
        "evidence.kind wire-shape; a call only in an example is evidence.kind example-only.",
        "Set patterns_model_read_on to today only if you read the row against docs/patterns.md. "
        "Never set evidence.read_on, patterns_reviewed or summary_source curated: those are a "
        "person's.",
        "Add repo_license (the LICENSE file's SPDX id, or unknown with the no-license flag) and "
        "any flag a reader needs (CONTRIBUTING.md, 'Flags are the point'). Leave stars and the "
        "other repo_* facts to the weekly refresh.",
        "notes and notes_zh end with the sentence saying an AI assistant drafted the row: put "
        "anything you add before it, and keep notes under 500 characters.",
        "Then delete this field and run python3 scripts/model_draft.py --check on this file "
        "before adding the row to catalog.json.",
    ]
    return lines


def draft_row(repo: str, path: str, body: str, *, slug: str, today: dt.date) -> dict:
    """The row a model starts from, `_draft` first, in the order model-read rows keep."""
    owner, name = repo.split("/")
    found = strong_signals(body)[:MATCHED_MAX]
    day = today.isoformat()
    row: dict = {
        lint.DRAFT_FIELD: instructions(repo, path, found, today=today),
        "slug": slug,
        "title": name,
        "summary": "",
        "summary_source": lint.MODEL_WRITTEN,
        "summary_zh": "",
        "url": f"https://github.com/{repo}",
        "kind": "",
        "patterns": [],
        "question_types": [],
        "platforms": [],
        "author": {"name": owner, "url": f"https://github.com/{owner}"},
    }
    languages = languages_of(path)
    if languages:
        row["languages"] = languages
    row["evidence"] = {"path": path, "matched": found, "model_read_on": day}
    row["notes"] = NOTE_EN.format(day=day)
    row["notes_zh"] = NOTE_ZH.format(day=day)
    row["sources"] = [dict(SOURCE)]
    row["license"] = "CC0-1.0"
    row["first_seen"] = day
    row["zh_machine"] = True
    row["has_code"] = True
    return row


def problems(row: object, where: str, known: dict, *, body: str | None,
             today: dt.date) -> lint.Findings:
    """What is wrong with one finished row. `body` is the cited file at HEAD,
    or None when it was not read."""
    report = lint.Report()
    if not isinstance(row, dict):
        report.err(where, "a row must be a JSON object")
        return report.findings()
    slug = row.get("slug", "?")
    if known["schema"]:
        report.add(lint.validate(row, known["schema"], where))
    report.add(lint.check_entry_invariants(row, where, retired=False, today=today))
    if known["compat"] is not None and known["taxonomy"] is not None:
        report.add(lint.check_platform_values([row], [], known["compat"], known["taxonomy"]))

    # The model tier, and nothing of a person's.
    evidence = row.get("evidence") if isinstance(row.get("evidence"), dict) else {}
    if row.get("summary_source") != lint.MODEL_WRITTEN:
        report.err(where, f"{slug}: summary_source must be {lint.MODEL_WRITTEN!r} on a model's row")
    if row.get("zh_machine") is not True:
        report.err(where, f"{slug}: zh_machine must be true: a model wrote the Chinese")
    if not evidence.get("model_read_on"):
        report.err(where, f"{slug}: evidence.model_read_on must be the day the model read the file")
    for field in PERSON_EVIDENCE:
        if field in evidence:
            report.err(where, f"{slug}: evidence.{field} is a person's reading; a model sets model_read_on")
    for field in PERSON_FIELDS:
        if field in row:
            report.err(where, f"{slug}: {field} is a person's reading; a model sets patterns_model_read_on")
    if SAID_EN not in str(row.get("notes", "")):
        report.err(where, f"{slug}: notes must carry the sentence: {NOTE_EN.format(day='<date>')}")
    if SAID_ZH not in str(row.get("notes_zh", "")):
        report.err(where, f"{slug}: notes_zh must carry the sentence: {NOTE_ZH.format(day='<date>')}")
    if "repo_license" not in row:
        report.warn(where, f"{slug}: no repo_license; the weekly refresh will add GitHub's")

    # Not a second row for anything already settled.
    url = url_key(row.get("url"))
    for label, rows in (("catalog.json", known["catalog"]), ("retired.json", known["retired"])):
        for other in rows:
            same_slug, same_url = other.get("slug") == slug, url_key(other.get("url")) == url
            if label == "catalog.json" and same_slug and same_url:
                continue  # this row, already added: checking it again is fine
            if same_slug:
                report.err(where, f"{slug}: slug is already used in {label}")
            elif same_url:
                report.err(where, f"{slug}: {row.get('url')} is already {other.get('slug')} in {label}")
    repo = repo_of(row)
    if repo and repo.lower() in known["declined"]:
        report.err(where, f"{slug}: {repo} is declined in docs/declined.txt")
    if repo and repo.lower() in known["held"]:
        report.err(where, f"{slug}: {repo} is held for a person in docs/held.txt; a person settles it")

    # The cited file still says what the row quotes.
    path, matched = evidence.get("path"), evidence.get("matched")
    if path and isinstance(matched, list) and TEST_PATH.search(path):
        report.warn(where, f"{slug}: evidence.path {path} looks like a test or a fake: cite the real call")
    if body is not None and isinstance(matched, list):
        missing = [s for s in matched if isinstance(s, str) and s not in body]
        if missing:
            report.err(where, f"{slug}: {path} at HEAD does not contain {json.dumps(missing, ensure_ascii=False)}")
    return report.findings()


def rows_in(path: pathlib.Path) -> list:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data if isinstance(data, list) else [data]


def check(paths: list[str], *, fetch=raw_get, read: bool = True, root: pathlib.Path = ROOT,
          today: dt.date | None = None) -> int:
    today = today or dt.date.today()
    known = files(root)
    found = lint.Findings()
    count = 0
    for name in paths:
        try:
            rows = rows_in(pathlib.Path(name))
        except (OSError, ValueError) as exc:
            found = lint.Findings(found.errors + (f"{name}: {exc}",), found.warnings)
            continue
        for i, row in enumerate(rows):
            count += 1
            where = name if len(rows) == 1 else f"{name}[{i}]"
            body = None
            evidence = row.get("evidence") if isinstance(row, dict) else None
            repo = repo_of(row) if isinstance(row, dict) else None
            if read and repo and isinstance(evidence, dict) and evidence.get("path"):
                body = fetch(repo, "HEAD", evidence["path"])
                if body is None:
                    found = lint.Findings(
                        found.errors + (f"{where}: {repo}@HEAD:{evidence['path']} could not be read",),
                        found.warnings,
                    )
                    continue
            more = problems(row, where, known, body=body, today=today)
            found = lint.Findings(found.errors + more.errors, found.warnings + more.warnings)
    lint.print_report(found)
    print(f"checked {count} row{'' if count == 1 else 's'}" + ("" if read else " without reading the cited files"))
    return 1 if found.errors else 0


def start(repo: str, path: str, out: str, *, fetch=raw_get, root: pathlib.Path = ROOT,
          today: dt.date | None = None, slug: str = "") -> int:
    today = today or dt.date.today()
    if repo.count("/") != 1 or not all(repo.split("/")):
        print(f"error: {repo!r} is not OWNER/NAME", file=sys.stderr)
        return 1
    reason = settled(repo, files(root))
    if reason:
        print(f"no draft for {repo}: {reason}", file=sys.stderr)
        return 1
    body = fetch(repo, "HEAD", path)
    if body is None:
        print(f"error: {repo}@HEAD:{path} could not be read", file=sys.stderr)
        return 1
    directory = pathlib.Path(out)
    taken = catalogue_slugs(root) | {p.stem for p in directory.glob("*.json")}
    slug = slug or propose_slug(*repo.split("/"), taken)
    target = directory / f"{slug}.json"
    if target.exists():
        print(f"error: {target} exists; delete it for a new draft", file=sys.stderr)
        return 1
    row = draft_row(repo, path, body, slug=slug, today=today)
    directory.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(row, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {target}")
    if not row["evidence"]["matched"]:
        print(f"note: {path} holds no Jev call-site string; see the draft's first lines", file=sys.stderr)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("repo", nargs="?", metavar="OWNER/NAME", help="the candidate to draft")
    parser.add_argument("path", nargs="?", metavar="PATH", help="the file it calls Jev in")
    parser.add_argument("--out", default="drafts", help="directory for the draft (default: drafts)")
    parser.add_argument("--slug", default="", help="the slug to use instead of the proposed one")
    parser.add_argument("--check", nargs="+", metavar="FILE", help="check finished rows instead")
    parser.add_argument("--no-fetch", action="store_true", help="with --check, skip reading the cited files")
    args = parser.parse_args(argv)
    if args.check:
        return check(args.check, read=not args.no_fetch)
    if not (args.repo and args.path):
        parser.error("give OWNER/NAME and PATH, or --check FILE")
    return start(args.repo, args.path, args.out, slug=args.slug)


if __name__ == "__main__":
    sys.exit(main())
