"""The site's own fonts (site/fonts/, since 2026-10-24) and the two lint_docs
rules that keep them: no page loads from another host, and every font stack on
a page that shows Chinese names the system CJK fonts."""

from __future__ import annotations

import pathlib
import re
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import lint_docs  # noqa: E402
import render_images  # noqa: E402

SITE = ROOT / "site"
FONTS = SITE / "fonts"


class FontFilesTest(unittest.TestCase):
    def test_every_face_names_a_file_here_and_every_file_is_named(self):
        css = (FONTS / "fonts.css").read_text(encoding="utf-8")
        named = set(re.findall(r'url\("([^"/]+)"\)', css))
        files = {path.name for path in FONTS.glob("*.woff2")}
        self.assertTrue(files)
        self.assertEqual(named, files)
        for name in files:
            self.assertEqual((FONTS / name).read_bytes()[:4], b"wOF2", name)

    def test_both_families_cover_latin_at_every_weight_the_pages_use(self):
        css = (FONTS / "fonts.css").read_text(encoding="utf-8")
        faces = re.findall(r"@font-face \{(.*?)\}", css, re.S)
        latin = [face for face in faces if "U+0000-00FF" in face]
        weights = {
            family: [w for face in latin if f'"{family}"' in face for w in re.findall(r"font-weight: ([\d ]+);", face)]
            for family in ("IBM Plex Sans", "IBM Plex Mono")
        }
        self.assertEqual(weights["IBM Plex Sans"], ["400 600"])
        self.assertEqual(sorted(weights["IBM Plex Mono"]), ["400", "500", "600"])
        self.assertTrue(all("font-display: swap;" in face for face in faces))

    def test_the_licence_ships_beside_the_fonts(self):
        text = (FONTS / "LICENSE.txt").read_text(encoding="utf-8")
        self.assertIn("SIL Open Font License", text)
        self.assertIn("IBM Corp.", text)

    def test_each_page_links_the_stylesheet_and_preloads_files_it_declares(self):
        for page, href in (
            ("index.html", "fonts/fonts.css"),
            ("card.html", "fonts/fonts.css"),
            # Served for any missing path, so its links are absolute.
            ("404.html", "/awesome-jev/fonts/fonts.css"),
        ):
            self.assertIn(f'<link rel="stylesheet" href="{href}" />', (SITE / page).read_text(encoding="utf-8"))
        html = (SITE / "index.html").read_text(encoding="utf-8")
        preloads = re.findall(r'rel="preload"\s+href="([^"]+)"', html)
        self.assertEqual(len(preloads), 2)
        css = (FONTS / "fonts.css").read_text(encoding="utf-8")
        for href in preloads:
            self.assertTrue((SITE / href).exists(), href)
            self.assertIn(f'url("{pathlib.PurePosixPath(href).name}")', css)


class SiteOriginTest(unittest.TestCase):
    def loads(self, text: str) -> list[str]:
        return [m.group(0) for m in lint_docs.FOREIGN_LOAD.finditer(text)]

    def test_the_pages_as_they_were_until_2026_10_24_are_refused(self):
        before = (
            '<link rel="preconnect" href="https://fonts.googleapis.com" />\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
            "<link\n"
            '  href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400&display=swap"\n'
            '  rel="stylesheet"\n'
            "/>\n"
        )
        self.assertEqual(len(self.loads(before)), 3)

    def test_scripts_images_imports_and_fetches_from_another_host_are_refused(self):
        for text in (
            '<script src="https://cdn.example.com/x.js"></script>',
            '<img alt="" src="//example.com/a.png">',
            '@import url("https://example.com/a.css");',
            "background: url(https://example.com/a.png);",
            'fetch("https://example.com/catalog.json")',
        ):
            self.assertEqual(len(self.loads(text)), 1, text)

    def test_links_a_reader_follows_and_local_files_are_fine(self):
        for text in (
            '<a href="https://github.com/kydlikebtc/awesome-jev">GitHub</a>',
            '<link rel="canonical" href="https://kydlikebtc.github.io/awesome-jev/" />',
            '<link rel="stylesheet" href="fonts/fonts.css" />',
            '<script type="module" src="catalog-core.mjs"></script>',
            'url("data:image/svg+xml,%3Csvg%3E")',
            'fetch("compat.json")',
        ):
            self.assertEqual(self.loads(text), [], text)

    def test_the_site_as_committed_loads_only_from_itself(self):
        self.assertEqual(lint_docs.check_site_origin(), [])


class CjkFallbackTest(unittest.TestCase):
    def check(self, page: str) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            (root / "site").mkdir()
            (root / "site" / "page.html").write_text(page, encoding="utf-8")
            with patch.object(lint_docs, "ROOT", root), patch.object(lint_docs, "tracked", return_value=["site/page.html"]):
                return lint_docs.check_cjk_fallback()

    def stack(self, families: tuple[str, ...]) -> str:
        return ", ".join(f'"{family}"' for family in families)

    def test_a_stack_naming_every_system_cjk_font_passes(self):
        page = f'<p>中文</p><style>:root {{ --sans: "IBM Plex Sans", {self.stack(lint_docs.CJK_FAMILIES)}, sans-serif; }}</style>'
        self.assertEqual(self.check(page), [])

    def test_a_stack_missing_one_is_named(self):
        families = tuple(f for f in lint_docs.CJK_FAMILIES if f != "Noto Sans CJK SC")
        page = f'<p>中文</p><style>:root {{ --mono: "IBM Plex Mono", {self.stack(families)}, monospace; }}</style>'
        problems = self.check(page)
        self.assertEqual(len(problems), 1)
        self.assertIn("--mono has no CJK fallback for Noto Sans CJK SC", problems[0])

    def test_a_page_without_chinese_needs_none(self):
        self.assertEqual(self.check('<style>:root { --sans: "IBM Plex Sans", sans-serif; }</style>'), [])

    def test_the_site_as_committed_passes(self):
        self.assertEqual(lint_docs.check_cjk_fallback(), [])


class RenderFontTest(unittest.TestCase):
    """render_images.py asks fontconfig for a CJK font before it renders."""

    def test_fontconfig_is_asked_on_linux_only(self):
        listed = "Noto Sans CJK SC,Noto Sans CJK SC Regular\nNoto Sans CJK SC\n"
        with patch.object(render_images.platform, "system", return_value="Linux"), \
                patch.object(render_images.shutil, "which", return_value="/usr/bin/fc-list"), \
                patch.object(render_images.subprocess, "run") as run:
            run.return_value.stdout = listed
            self.assertEqual(render_images.cjk_fonts(), ["Noto Sans CJK SC"])
            run.return_value.stdout = ""
            self.assertEqual(render_images.cjk_fonts(), [])
        with patch.object(render_images.platform, "system", return_value="Darwin"):
            self.assertIsNone(render_images.cjk_fonts())

    def run_main(self, *args: str, fonts=None):
        with tempfile.TemporaryDirectory() as directory:
            site = pathlib.Path(directory)
            for name in (*render_images.RUNTIME_FILES, "stats.json"):
                (site / name).parent.mkdir(parents=True, exist_ok=True)
                (site / name).write_text("{}")
            stop = RuntimeError("rendering would start here")
            with patch.object(render_images, "SITE", site), \
                    patch.object(render_images, "cjk_fonts", return_value=fonts), \
                    patch.object(render_images, "find_chrome", side_effect=stop), \
                    patch("sys.stderr") as stderr:
                try:
                    render_images.main(list(args))
                except RuntimeError as exc:
                    self.assertIs(exc, stop)
                return "".join(call.args[0] for call in stderr.write.call_args_list)

    def test_no_cjk_font_fails_the_deploy_and_warns_elsewhere(self):
        with self.assertRaises(SystemExit) as raised:
            self.run_main("--require-cjk-font", fonts=[])
        self.assertIn("no installed font draws Chinese", str(raised.exception))
        self.assertIn("warning: no installed font draws Chinese", self.run_main(fonts=[]))

    def test_a_cjk_font_or_no_fontconfig_renders_without_a_word(self):
        self.assertEqual(self.run_main("--require-cjk-font", fonts=["Noto Sans CJK SC"]), "")
        self.assertEqual(self.run_main("--require-cjk-font", fonts=None), "")

    def test_the_deploy_installs_one_and_requires_it(self):
        pages = (ROOT / ".github" / "workflows" / "pages.yml").read_text(encoding="utf-8")
        install = pages.index("apt-get install -y -qq --no-install-recommends fonts-noto-cjk")
        self.assertLess(install, pages.index("python3 scripts/render_images.py --require-cjk-font"))
        self.assertIn("Noto Sans CJK SC", lint_docs.CJK_FAMILIES)


if __name__ == "__main__":
    unittest.main()
