#!/usr/bin/env python3
"""Search a candidate's whole default branch for a Jev call, without the API.

The first rule for docs/held.txt (MAINTAINING.md, "Candidates a run cannot
settle") has the weekly upkeep search a held candidate's code for the
call-site strings `scripts/_github.py` knows before it declines the candidate.
The discovery workflow lists a repository's files through GitHub's tree API
with a token. The scheduled tasks' sandbox gets 403 from api.github.com for
other repositories, so a task on its own could only read files at paths it
already knew, and a decline would say "searched" of a guess. A shallow clone
over HTTPS works there, so:

    python3 scripts/find_calls.py OWNER/NAME [--dir PATH]

clones the default branch one commit deep into a new empty directory (or
reads PATH when given) and prints each code file that holds a strong signal,
one per line, the project's own files before its tests and fixtures:

    path<TAB>signal, signal, signal

Nothing in the clone is run: files are only read as text, symbolic links are
checked out as plain files and never followed, and directories of other
projects' code (`node_modules`, `vendor` and the like) are skipped. Exit 0
when a file matched, 1 when none did, 2 when the clone failed, with git's
reason on stderr: a repository gone or private says so there.
"""

from __future__ import annotations

import argparse
import os
import pathlib
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from _github import CODE_EXT, strong_signals  # noqa: E402
from discover_candidates import TEST_PATH, only_slug  # noqa: E402

# Other projects' code: a match in a dependency is that dependency calling
# Jev, not the candidate.
SKIP_DIRS = frozenset({
    ".git", "node_modules", "vendor", "third_party", "bower_components",
    ".venv", "venv", "site-packages", "__pycache__",
})
# A minified bundle or a data dump is not where a call is written.
MAX_BYTES = 1_000_000
# As many strings per file as discover_candidates.inspect() quotes.
MATCHED_MAX = 3
TIMEOUT = 180


def wanted(rel: str) -> bool:
    """A code file, or an extensionless one named after Jev (a CLI script with
    a shebang): the files discover_candidates.inspect() reads."""
    name = rel.rsplit("/", 1)[-1]
    if rel.endswith(CODE_EXT):
        return True
    return "." not in name and bool(re.search(r"jev|typesafe", name, re.I))


def search(root: pathlib.Path) -> list[tuple[str, list[str]]]:
    """(path, signals) for each file under root that holds a strong signal:
    the project's own files first, then its tests and fixtures, each by path."""
    found: list[tuple[str, list[str]]] = []
    for folder, dirs, files in os.walk(root, followlinks=False):
        here = pathlib.Path(folder)
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not (here / d).is_symlink())
        for name in sorted(files):
            path = here / name
            rel = path.relative_to(root).as_posix()
            if not wanted(rel) or path.is_symlink():
                continue
            try:
                if path.stat().st_size > MAX_BYTES:
                    continue
                body = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            signals = strong_signals(body)
            if signals:
                found.append((rel, signals[:MATCHED_MAX]))
    return sorted(found, key=lambda item: (bool(TEST_PATH.search(item[0])), item[0]))


def clone(slug: str, into: pathlib.Path) -> str | None:
    """Clone slug's default branch, one commit deep, into `into`: None when it
    worked, otherwise git's last line of complaint."""
    env = {**os.environ, "GIT_TERMINAL_PROMPT": "0", "GIT_LFS_SKIP_SMUDGE": "1"}
    command = [
        "git", "-c", "core.symlinks=false", "-c", "protocol.file.allow=never",
        "clone", "--quiet", "--depth", "1", "--single-branch", "--no-tags",
        "--", f"https://github.com/{slug}.git", str(into),
    ]
    try:
        done = subprocess.run(command, env=env, capture_output=True, text=True, timeout=TIMEOUT, check=False)
    except subprocess.TimeoutExpired:
        return f"no answer in {TIMEOUT} seconds"
    if done.returncode == 0:
        return None
    lines = [line.strip() for line in done.stderr.splitlines() if line.strip()]
    return lines[-1] if lines else f"git exited {done.returncode}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("repo", help="owner/name, or its github.com URL")
    parser.add_argument("--dir", type=pathlib.Path, help="read this directory instead of cloning")
    args = parser.parse_args(argv)
    slug = only_slug(args.repo)
    if slug is None:
        parser.error(f"not owner/name: {args.repo}")
    if args.dir is not None:
        hits = search(args.dir)
    else:
        with tempfile.TemporaryDirectory(prefix="find-calls-") as scratch:
            into = pathlib.Path(scratch) / "repo"
            problem = clone(slug, into)
            if problem:
                print(f"{slug}: could not clone it: {problem}", file=sys.stderr)
                return 2
            hits = search(into)
    for rel, signals in hits:
        print(f"{rel}\t{', '.join(signals)}")
    if not hits:
        print(f"{slug}: no code file holds a call-site string", file=sys.stderr)
    return 0 if hits else 1


if __name__ == "__main__":
    sys.exit(main())
