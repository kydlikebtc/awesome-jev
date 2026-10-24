#!/usr/bin/env python3
"""Render every image that shows catalogue data, from the data, at deploy time.

The social card and the README screenshots were PNGs committed once and never
regenerated, so they said 148 entries long after the catalogue passed 800. This
renders them from the assembled site on every Pages deploy instead, and they
are served from Pages rather than committed — an image that is rebuilt from the
data it shows cannot drift from it, and git history does not collect a new
half-megabyte PNG every week.

  img/og.png           card.html?mode=live — the site's og:image, live figures
  img/card.png         card.html — the durable card for GitHub's social preview,
                       which has to be uploaded by hand; it contains no figures
                       or dates that can become stale
  img/site-en.png      the site, English — the README hero image
  img/site-zh.png      the site, Chinese — the Chinese README hero image
  img/site-compat.png  the compatibility view — docs/compatibility.md

Each page is first loaded with --dump-dom and must have set data-ready="1" and
contain an expected string, or nothing is published: a screenshot of a page
whose fetch failed would otherwise go live looking like a real preview.

Stdlib plus a Chrome binary. GitHub's ubuntu runners ship Google Chrome, so CI
needs no install step; locally, set CHROME if it is not found.

Chinese is drawn with a system font (the site loads no Chinese web font, since
2026-10-24; site/fonts/fonts.css says why), and the runner image has none: on
Linux this asks fontconfig for one first. Without one, the Chinese screenshot
and the cards' "中文" would be empty boxes. `--require-cjk-font`, which
pages.yml passes after installing fonts-noto-cjk, makes that an error rather
than a warning; elsewhere (CI's lint run, a local check) the images are thrown
away, and only their data is checked.

Run: python3 scripts/assemble_site.py && python3 scripts/render_images.py
"""

from __future__ import annotations

import argparse
import functools
import http.server
import os
import pathlib
import platform
import shutil
import subprocess
import sys
import threading

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from assemble_site import ROOT, RUNTIME_FILES  # noqa: E402

SITE = ROOT / "site"
OUT = SITE / "img"
BUDGET_MS = 15000

# (output name, page, viewport, strings the rendered DOM must contain)
TARGETS = (
    (
        "og.png", "card.html?mode=live", (1280, 640),
        (
            'data-mode="live"', "Jev Decision Atlas", "indexed examples",
            "link checked · 2xx", "call-site cited",
        ),
    ),
    (
        "card.png", "card.html", (1280, 640),
        (
            'data-mode="durable"', "Jev Decision Atlas", "Browse by task",
            "Check link status", "Read call-site citations",
        ),
    ),
    ("site-en.png", "index.html?lang=en", (1200, 900), ("Tool selection",)),
    ("site-zh.png", "index.html?lang=zh", (1200, 900), ("工具选择",)),
    ("site-compat.png", "index.html?lang=en&view=compat", (1200, 900), ("typesafe/jev",)),
)

CANDIDATES = (
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
)


def find_chrome() -> str:
    for candidate in (
        [os.environ["CHROME"]] if os.environ.get("CHROME") else []
    ) + list(CANDIDATES):
        path = shutil.which(candidate) or (
            candidate if os.path.exists(candidate) else None
        )
        if path:
            return path
    raise SystemExit(
        "error: no Chrome found. Set CHROME to a Chrome or Chromium binary."
    )


class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args: object) -> None:  # one line per image is enough
        pass


def serve() -> tuple[http.server.ThreadingHTTPServer, int]:
    handler = functools.partial(_Quiet, directory=str(SITE))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, server.server_address[1]


def chrome(
    binary: str, size: tuple[int, int], *args: str
) -> subprocess.CompletedProcess:
    flags = [
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        f"--window-size={size[0]},{size[1]}",
        f"--virtual-time-budget={BUDGET_MS}",
    ]
    # The runner's container has no user namespace for Chrome's sandbox. These
    # are our own static pages, rendered once and thrown away.
    if platform.system() == "Linux":
        flags.append("--no-sandbox")
    return subprocess.run(
        [binary, *flags, *args], capture_output=True, text=True, timeout=120
    )


def cjk_fonts() -> list[str] | None:
    """The font families fontconfig would draw Chinese with, or None where
    there is no fontconfig to ask: macOS and Windows draw Chinese with their
    own system fonts, which every font stack on the site names."""
    if platform.system() != "Linux" or not shutil.which("fc-list"):
        return None
    listed = subprocess.run(["fc-list", ":lang=zh", "family"], capture_output=True, text=True).stdout
    return sorted({line.split(",")[0].strip() for line in listed.splitlines() if line.strip()})


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--require-cjk-font", action="store_true",
        help="fail, rather than warn, when no installed font draws Chinese (pages.yml)",
    )
    args = parser.parse_args(argv)
    for name in (*RUNTIME_FILES, "stats.json"):
        if not (SITE / name).exists():
            raise SystemExit(f"error: site/{name} is missing; run assemble_site.py first")
    if cjk_fonts() == []:
        problem = (
            "no installed font draws Chinese, so site-zh.png and the cards' 中文 would be empty boxes; "
            "install one (pages.yml installs fonts-noto-cjk)"
        )
        if args.require_cjk_font:
            raise SystemExit(f"error: {problem}")
        print(f"warning: {problem}", file=sys.stderr)

    OUT.mkdir(exist_ok=True)
    binary = find_chrome()
    server, port = serve()
    failures = []
    try:
        for name, page, size, expect in TARGETS:
            url = f"http://127.0.0.1:{port}/{page}"
            target = OUT / name
            # Never leave a previous render in place: a stale image that
            # survives a failed render is exactly the bug this script removes.
            target.unlink(missing_ok=True)
            dom = chrome(binary, size, "--dump-dom", url).stdout
            if 'data-ready="1"' not in dom or not all(text in dom for text in expect):
                failures.append(f"{name}: {page} never finished rendering its data")
                continue
            chrome(binary, size, f"--screenshot={target}", url)
            if not target.exists() or target.stat().st_size < 10_000:
                failures.append(f"{name}: Chrome produced no usable screenshot")
                continue
            print(
                f"  rendered img/{name}  {size[0]}×{size[1]}  {target.stat().st_size // 1024} KB"
            )
    finally:
        server.shutdown()

    for failure in failures:
        print(f"error: {failure}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
