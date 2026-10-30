#!/usr/bin/env python3
"""What someone read, could not settle, and left for a person: `docs/held.txt`.

The scheduled drafting runs read the discovery queue from the top, and until
2026-10-30 the top of it was the same fourteen candidates every day: each run
read them again, skipped them again, and said why only in its pull request.
The weekly upkeep's doubts about catalogued rows (a proposed path that is a
test, a call site gone with nothing to replace it) lived in its pull request
bodies too. Nothing in the repository kept either, so nothing showed what was
waiting on a person.

docs/held.txt keeps both, one per line with the reason after a `#`, like
docs/declined.txt: an owner/name is a discovery candidate, anything else a
catalogued row's slug. Holding decides nothing. scripts/queue_sync.py lists
held candidates under their own heading instead of among those to read, and
docs/review-queue.md#needs-person (scripts/build_review_queue.py) lists every
line. A person's decision is still a row in catalog.json or a line in
docs/declined.txt; whoever makes it deletes the line here.
"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PATH = ROOT / "docs" / "held.txt"


def parse(text: str) -> tuple[dict[str, str], dict[str, str]]:
    """(candidates, rows): each owner/name, lower-cased, and each row slug, to
    the reason given, in the file's order."""
    candidates: dict[str, str] = {}
    rows: dict[str, str] = {}
    for line in text.splitlines():
        body, _, reason = line.partition("#")
        key = body.strip()
        if not key:
            continue
        if "/" in key:
            candidates[key.lower()] = reason.strip()
        else:
            rows[key] = reason.strip()
    return candidates, rows


def load(path: pathlib.Path | str = PATH) -> tuple[dict[str, str], dict[str, str]]:
    """parse() of the file; a missing file holds nothing."""
    path = pathlib.Path(path)
    if not path.exists():
        return {}, {}
    return parse(path.read_text(encoding="utf-8"))
