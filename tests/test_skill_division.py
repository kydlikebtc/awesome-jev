"""The agent skill says what it is for next to TypeSafe's own (I37).

TypeSafe publishes an agent skill, typesafe-ai/skills, that covers the API
contract and how to design questions, from the live docs. This repository's
skill used to trigger on the same requests and repeat some of the same rules
without mentioning it. Now its description, a "Division of labour" section,
the README, llms.txt and the official skill's own catalogue row all say the
same thing: the official skill and the docs for the contract and the design,
this one for what the public ecosystem shows. Nothing says what happens when
both are installed: nothing here has observed it. The README is rendered in
memory; the other files are hand-written sources.
"""

from __future__ import annotations

import copy
import json
import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_readme  # noqa: E402
from readme import sections, strings  # noqa: E402

SKILL = ROOT / "skills" / "awesome-jev" / "SKILL.md"
OFFICIAL = "https://github.com/typesafe-ai/skills"
ROW = "typesafe-skills-repo"
CATALOG = json.loads((ROOT / "catalog.json").read_text())
RETIRED = json.loads((ROOT / "retired.json").read_text())

# Wording that would describe two installed skills interacting.
INTERACTION = re.compile(
    r"both (are |skills? )?(installed|loaded|active)|installed (together|side by side)|"
    r"(conflict|compete|override|shadow)s? (with )?(the )?(official|typesafe-ai)|double[- ]load|choose between the two",
    re.I,
)


def frontmatter(text: str) -> dict[str, str]:
    head = text.split("---\n", 2)[1]
    return dict(line.split(": ", 1) for line in head.strip().splitlines())


def section(text: str, heading: str) -> str:
    return text.split(f"\n## {heading}\n", 1)[1].split("\n## ", 1)[0]


class SkillTest(unittest.TestCase):
    text = SKILL.read_text()

    def test_the_description_defers_on_the_contract_and_says_what_it_adds(self):
        meta = frontmatter(self.text)
        self.assertEqual(meta["name"], "awesome-jev")
        description = meta["description"]
        # One plain YAML line: a ": " or " #" inside would change its meaning.
        self.assertNotIn(": ", description)
        self.assertNotIn(" #", description)
        sentences = [s for s in re.split(r"(?<=\.)\s+", description) if s]
        self.assertLessEqual(len(sentences), 4, sentences)
        self.assertIn("typesafe-ai", description)
        self.assertIn("docs.typesafe.ai", description)
        for words in ("worked example", "caveat", "model string", "Vercel", "independent", "negative"):
            self.assertIn(words, description)

    def test_division_of_labour_comes_first_and_links_the_official_skill(self):
        headings = re.findall(r"^## (.+)$", self.text, re.M)
        self.assertEqual(headings[0], "Division of labour")
        body = section(self.text, "Division of labour")
        self.assertIn(f"({OFFICIAL})", body)
        self.assertIn(f"https://kydlikebtc.github.io/awesome-jev/?lang=en#{ROW}", body)
        self.assertIn("https://docs.typesafe.ai/llms.txt", body)

    def test_the_design_rules_keep_only_what_the_official_skill_leaves_out(self):
        rules = section(self.text, "Design rules worth following")
        kept = re.findall(r"^\*\*(.+?)\*\*", rules, re.M)
        self.assertEqual(len(kept), 4, kept)
        joined = " ".join(kept).lower()
        for words in ("none", "noul", "policy", "security boundary", "pin"):
            self.assertIn(words, joined)
        # Compressed into one pointer at the official skill.
        self.assertNotIn("Ask everything in one request", rules)
        self.assertNotIn("Keep deterministic work in code", rules)
        self.assertIn("official skill", rules.split("\n\n", 1)[0] + rules.split("\n\n", 2)[1])
        # The escape-hatch rule now says only what the official one does not:
        # a `none` option is relative to the list, a `noul` is not.
        self.assertRegex(rules, r"relative")
        self.assertRegex(rules, r"absolute")

    def test_the_facts_and_limits_stay(self):
        # lint_docs holds these to compat.json; they are this skill's own.
        for heading in ("Get the facts right first", "Default limits", "Querying the catalogue", "Before believing a benchmark"):
            self.assertIn(f"\n## {heading}\n", self.text)

    def test_the_row_it_links_is_in_the_catalogue(self):
        row = next(e for e in CATALOG if e["slug"] == ROW)
        self.assertEqual(row["url"], OFFICIAL)
        self.assertTrue(row.get("official"))


class ReadmeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.readmes = {
            p["lang_code"]: build_readme.render(copy.deepcopy(CATALOG), copy.deepcopy(RETIRED), p)
            for p in (strings.EN, strings.ZH)
        }

    def also(self, lang: str) -> str:
        pack = strings.ZH if lang == "zh" else strings.EN
        return self.readmes[lang].split(f"## {pack['repo_h']}\n", 1)[1].split("\n## ", 1)[0]

    def test_also_in_this_repo_says_the_division_in_both_languages(self):
        for lang in ("en", "zh"):
            text = self.also(lang)
            self.assertIn(f"]({OFFICIAL})", text, lang)
            self.assertIn(f"](https://kydlikebtc.github.io/awesome-jev/?lang={lang}#{ROW})", text, lang)
        self.assertIn("API contract", self.also("en"))
        self.assertIn("API 契约", self.also("zh"))

    def test_the_chinese_sentence_is_marked_as_a_model_s(self):
        self.assertIn("repo_skill_division", strings.ZH_MACHINE)
        line = next(l for l in self.also("zh").splitlines() if OFFICIAL in l)
        self.assertTrue(line.endswith(" <sub>(机翻)</sub>"), line)
        line = next(l for l in self.also("en").splitlines() if OFFICIAL in l)
        self.assertNotIn("机翻", line)

    def test_no_row_no_sentence(self):
        catalog = [e for e in CATALOG if e["slug"] != sections.OFFICIAL_SKILL]
        text = build_readme.render(catalog, copy.deepcopy(RETIRED), strings.EN)
        self.assertNotIn(OFFICIAL + ")", text.split(f"## {strings.EN['repo_h']}\n", 1)[1].split("\n## ", 1)[0])

    def test_it_follows_the_row_s_url(self):
        catalog = copy.deepcopy(CATALOG)
        next(e for e in catalog if e["slug"] == ROW)["url"] = "https://github.com/typesafe-ai/moved"
        text = build_readme.render(catalog, copy.deepcopy(RETIRED), strings.EN)
        self.assertIn("](https://github.com/typesafe-ai/moved)", text)


class LlmsAndRowTest(unittest.TestCase):
    def test_llms_txt_for_agents_says_the_division(self):
        text = (ROOT / "llms.txt").read_text()
        agents = text.split("## For agents", 1)[1].split("\n## ", 1)[0]
        line = next(l for l in agents.splitlines() if l.startswith("Agent skill:"))
        self.assertIn(OFFICIAL, line)
        self.assertIn(ROW, line)
        self.assertIn("API contract", line)

    def test_the_official_row_records_the_division_and_who_wrote_its_chinese(self):
        row = next(e for e in CATALOG if e["slug"] == ROW)
        self.assertIn("skills/awesome-jev", row["notes"])
        self.assertIn("API contract", row["notes"])
        self.assertIn("A model wrote", row["notes"])
        self.assertIn("skills/awesome-jev", row["notes_zh"])
        self.assertIn("由模型撰写", row["notes_zh"])

    def test_nothing_claims_how_two_installed_skills_behave(self):
        row = next(e for e in CATALOG if e["slug"] == ROW)
        texts = {
            "SKILL.md": SKILL.read_text(),
            "llms.txt": (ROOT / "llms.txt").read_text(),
            "strings EN": strings.EN["repo_skill_division"],
            "strings ZH": strings.ZH["repo_skill_division"],
            "row notes": row["notes"],
        }
        for where, text in texts.items():
            self.assertIsNone(INTERACTION.search(text), where)
        for text in (strings.ZH["repo_skill_division"], row["notes_zh"]):
            self.assertNotRegex(text, r"同时安装|二选一|双加载|冲突")

    def test_the_interaction_pattern_is_not_vacuous(self):
        for claim in ("When both are installed, Claude Code picks one", "the two skills conflict with the official one",
                      "installed together they double-load"):
            self.assertIsNotNone(INTERACTION.search(claim), claim)


if __name__ == "__main__":
    unittest.main()
