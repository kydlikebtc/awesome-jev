#!/usr/bin/env python3
"""Keep a dated snapshot of the catalogue's counts in history/, one per weekly refresh.

catalog.json holds each row as it is now: a star count, a licence, flags. The
figures the READMEs and docs/status.md publish are recomputed from it and
overwritten on every change, so nothing in the repository said what they were
last month, and the week's digest went with the runner. This writes
history/<date>.json, named by the UTC date it runs, holding

  * `stats`: _stats.compute() as it stands, every published number;
  * `counts`: rows per kind, pattern, flag, language and declared licence
    (_stats.shape(), the breakdowns docs/shape.md and counts.py print);
  * `rows`: each row's slug, stars, repo_license and flags, the facts the
    weekly refresh moves, so a later reader can say which rows changed;
  * `watch`: the value of each question watch.json counts (scripts/watch.py),
    which docs/status.md's "What to watch" states its recent change against;
  * `queue` (since 2026-10-30): the discovery queue's candidates in each state
    (to read, held, parked, ...), as scripts/queue_sync.py derives them from the
    files this refresh commits, so whether drafting keeps pace with discovery
    is a line in docs/shape.md rather than a guess;

under a header that says it is generated. Only metadata.yml runs it, after the
refresh and before its commit, so every snapshot is the state that refresh
committed. It is derived data, never a source: nothing reads a snapshot back
into catalog.json. docs/shape.md reads the files for its table of how the
counts moved (build_shape.py), and says how many there are until there are
enough to be a trend.

No backfill: git's history of catalog.json before the first snapshot spans a
few days of bulk edits, and re-running today's definitions over those commits
would put numbers in history/ that nobody published. A date before the newest
snapshot is refused for the same reason; running twice on one day rewrites
that day's file, identically if nothing moved.

Stdlib only, like the rest of scripts/.

Run: python3 scripts/snapshot_stats.py                  # history/<today, UTC>.json
     python3 scripts/snapshot_stats.py --date 2026-10-07
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _stats  # noqa: E402
import queue_sync  # noqa: E402
import watch  # noqa: E402

ROOT = _stats.ROOT
DIR = "history"
FILE = re.compile(r"^(\d{4}-\d{2}-\d{2})\.json$")
SOURCE = "scripts/snapshot_stats.py, run by .github/workflows/metadata.yml"
ABOUT = [
    "Generated, never edited by hand, and not a source of truth: catalog.json is. One file per weekly refresh, "
    "named by the UTC date it ran; a later file never rewrites an earlier one.",
    "stats: every number _stats.compute() published that day. counts: rows per kind, pattern, flag, language and "
    "declared licence (_stats.shape()). watch: each question watch.json counts, as scripts/watch.py counted it. "
    "queue: discovery candidates in each state, as scripts/queue_sync.py derived them (since 2026-10-30). "
    "rows: each row's slug, stars, repo_license and flags.",
    "Stars are GitHub's count at the refresh: a popularity signal, not a quality verdict.",
]
COUNTS = {"kinds": "kinds", "patterns": "by_pattern", "flags": "flags", "languages": "languages", "licences": "licences"}
ROW_FIELDS = ("slug", "stars", "repo_license", "flags")


def row_facts(entry: dict) -> dict:
    """The facts of one row a snapshot keeps; an absent one is left out."""
    out = {"slug": entry["slug"]}
    if entry.get("stars") is not None:
        out["stars"] = entry["stars"]
    if entry.get("repo_license"):
        out["repo_license"] = entry["repo_license"]
    if entry.get("flags"):
        out["flags"] = list(entry["flags"])
    return out


def snapshot(catalog: list[dict], patterns: list[dict], compat: dict, schema: dict, *, date: str,
             stats: dict, watched: dict | None = None, queue: dict | None = None) -> dict:
    """One snapshot, from the files it is handed, compute()'s stats,
    watch.values() and queue_sync.counts() (each left out when None)."""
    shape = _stats.shape(catalog, patterns, compat, schema)
    extra = {} if watched is None else {"watch": watched}
    if queue is not None:
        extra["queue"] = queue
    return {
        "generated": True,
        "source": SOURCE,
        "about": ABOUT,
        "date": date,
        "stats": stats,
        "counts": {name: shape[key] for name, key in COUNTS.items()},
        **extra,
        "rows": [row_facts(e) for e in sorted(catalog, key=lambda e: e["slug"])],
    }


def render(payload: dict) -> str:
    """Indented JSON, but one line per row, so a year of files stays small and
    a reader can diff two of them line by line."""
    head = json.dumps({k: v for k, v in payload.items() if k != "rows"}, indent=2, ensure_ascii=False)
    rows = [json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in payload.get("rows", [])]
    body = ",\n".join(f"    {line}" for line in rows)
    return head[:-2] + (f',\n  "rows": [\n{body}\n  ]\n}}\n' if rows else ',\n  "rows": []\n}\n')


def problems(name: str, payload: object) -> list[str]:
    """Why a file under history/ is not a snapshot this script would write."""
    match = FILE.match(name)
    if not match:
        return [f"{name}: not named YYYY-MM-DD.json"]
    if not isinstance(payload, dict):
        return [f"{name}: not a JSON object"]
    found = []
    if payload.get("generated") is not True or payload.get("source") != SOURCE:
        found.append(f"{name}: header must say generated: true and source {SOURCE!r}")
    if payload.get("date") != match.group(1):
        found.append(f"{name}: date {payload.get('date')!r} is not the file's")
    stats = payload.get("stats")
    if not isinstance(stats, dict) or not isinstance(stats.get("entries"), int):
        found.append(f"{name}: stats must be compute()'s numbers, entries included")
    counts = payload.get("counts")
    if not isinstance(counts, dict) or set(counts) != set(COUNTS) or not all(
        isinstance(v, dict) and all(isinstance(n, int) for n in v.values()) for v in counts.values()
    ):
        found.append(f"{name}: counts must map each of {', '.join(COUNTS)} to counts")
    watched = payload.get("watch", {})
    if not isinstance(watched, dict) or not all(isinstance(k, str) and isinstance(v, int) for k, v in watched.items()):
        found.append(f"{name}: watch must map question ids to counts")
    queue = payload.get("queue", {})
    if not isinstance(queue, dict) or not all(k in queue_sync.STATES and isinstance(v, int) for k, v in queue.items()):
        found.append(f"{name}: queue must map the discovery queue's states to counts")
    rows = payload.get("rows")
    slugs = [r.get("slug") for r in rows] if isinstance(rows, list) and all(isinstance(r, dict) for r in rows) else None
    if slugs is None or slugs != sorted(set(slugs)) or any(set(r) - set(ROW_FIELDS) for r in rows):
        found.append(f"{name}: rows must be {{{', '.join(ROW_FIELDS)}}} objects in slug order, each slug once")
    elif isinstance(stats, dict) and stats.get("entries") != len(rows):
        found.append(f"{name}: {len(rows)} rows but stats.entries is {stats.get('entries')}")
    return found


def load_history(folder: pathlib.Path | None = None) -> list[tuple[str, dict]]:
    """Every snapshot in history/ (or `folder`), oldest first, as (date,
    payload). Other files there (the README) are skipped; a snapshot that is
    not shaped like one stops the caller with every reason."""
    folder = ROOT / DIR if folder is None else folder
    out, found = [], []
    for path in sorted(folder.glob("*.json")) if folder.is_dir() else []:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as err:
            found.append(f"{path.name}: unreadable ({err})")
            continue
        errors = problems(path.name, payload)
        found += errors
        if not errors:
            out.append((payload["date"], payload))
    if found:
        raise ValueError(f"{DIR}/ holds files that are not snapshots:\n  " + "\n  ".join(found))
    return out


def write(path: pathlib.Path, text: str) -> None:
    """Replace the file in one step, so a crash never leaves half a snapshot."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=".snapshot-", suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(tmp, 0o644)
    os.replace(tmp, path)


def today() -> str:
    return dt.datetime.now(dt.timezone.utc).date().isoformat()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--date", help="the snapshot's date, YYYY-MM-DD (default: today in UTC)")
    parser.add_argument("--history", type=pathlib.Path, default=ROOT / DIR, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    date = args.date or today()
    try:
        dt.date.fromisoformat(date)
    except ValueError:
        print(f"error: --date {date!r} is not YYYY-MM-DD", file=sys.stderr)
        return 2
    history = load_history(args.history)
    if history and date < history[-1][0]:
        print(f"error: history/ already has {history[-1][0]}; a snapshot is never dated before the newest one",
              file=sys.stderr)
        return 1
    catalog, _retired, patterns, compat, schema = _stats.load()
    watched = watch.values(watch.load(), catalog)
    queue = queue_sync.counts(queue_sync.derive(*queue_sync.read_files(ROOT)))
    text = render(snapshot(catalog, patterns, compat, schema, date=date, stats=_stats.compute(), watched=watched,
                           queue=queue))
    path = args.history / f"{date}.json"
    before = path.read_text(encoding="utf-8") if path.exists() else None
    if before != text:
        write(path, text)
    dates = sorted({d for d, _ in history} | {date})
    shown = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
    print(
        f"{shown}: {'unchanged' if before == text else 'rewritten' if before else 'written'}, "
        f"{len(catalog)} rows, {len(text.encode()):,} bytes; {len(dates)} snapshot(s) since {dates[0]}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
