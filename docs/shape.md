<!-- Written by scripts/build_shape.py from catalog.json, compat.json, patterns.json, the entry schema and history/. Edit those, not this file. -->

# The catalogue's shape

<sub>[awesome-jev](../README.md) · [中文](shape.zh-CN.md)</sub>

Counts that describe this catalogue as a dataset, regenerated from `catalog.json` whenever it changes; the newest link check behind them is dated **2026-11-11**. They describe what the catalogue holds, which is what reached it through the sibling directories, this repository's discovery and its contributors, not the ecosystem at large. A star band is a popularity signal, not a quality verdict, and nothing here was run or reproduced by this repository. `python3 scripts/counts.py` prints the same numbers as text; the headline figures are on [the status page](status.md).

## Evidence by decision pattern

What the catalogue records about the rows filed under each pattern: reports counted, not a verdict. A row counts in every column that applies and under every pattern it is filed under. **Official documentation** is TypeSafe AI's own documentation pages (`kind: official-docs`). **Call site**, **wire shape** and **example only** count rows citing a file, by what `evidence.kind` records it shows: where the project calls Jev; a file speaking Jev's request shape rather than building on Jev; only an example the project ships. **Independent reports** are benchmark rows not flagged `vendor-reported`: their authors' measurements, not reproduced by this repository. **Negative results** are rows whose own author measured Jev for the use and concluded against it (author-stated; [listed on the status page](status.md#negative-results)). **No file cited** counts rows with no `evidence` (`evidence_none` may say why). The MCP server's `list_patterns` and each pattern's page give the same numbers.

| Pattern | Rows | Official documentation | Call site | Wire shape | Example only | Independent reports | Negative results | No file cited |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Tool selection](by-pattern/tool-selection.md) | 301 | 3 | 290 | 7 | 0 | 13 | 1 | 4 |
| [Intent routing](by-pattern/intent-routing.md) | 69 | 3 | 57 | 0 | 1 | 4 | 0 | 11 |
| [Context compaction](by-pattern/context-compaction.md) | 59 | 0 | 59 | 0 | 0 | 2 | 2 | 0 |
| [Safety gating](by-pattern/safety-gating.md) | 193 | 2 | 185 | 4 | 0 | 15 | 0 | 4 |
| [Output validation](by-pattern/output-validation.md) | 184 | 2 | 179 | 1 | 0 | 14 | 1 | 4 |
| [Retry control](by-pattern/retry-control.md) | 9 | 0 | 8 | 1 | 0 | 0 | 0 | 0 |
| [Human escalation](by-pattern/human-escalation.md) | 112 | 7 | 97 | 5 | 0 | 11 | 1 | 10 |
| [Model routing](by-pattern/model-routing.md) | 104 | 2 | 94 | 2 | 2 | 0 | 1 | 6 |
| [Speculative fan-out](by-pattern/fan-out.md) | 54 | 3 | 45 | 1 | 1 | 2 | 0 | 7 |
| [Search & ranking](by-pattern/search-ranking.md) | 108 | 3 | 104 | 0 | 0 | 8 | 2 | 4 |
| [Structured extraction](by-pattern/data-extraction.md) | 38 | 4 | 34 | 0 | 0 | 4 | 0 | 4 |
| [Classification](by-pattern/classification.md) | 237 | 4 | 225 | 3 | 0 | 24 | 2 | 9 |
| [ML feature extraction](by-pattern/feature-extraction.md) | 10 | 1 | 9 | 0 | 0 | 0 | 0 | 1 |
| [Document triage](by-pattern/document-triage.md) | 24 | 0 | 23 | 0 | 0 | 3 | 0 | 1 |
| [Support triage](by-pattern/support-triage.md) | 15 | 1 | 10 | 0 | 0 | 3 | 0 | 5 |
| [Content scoring](by-pattern/content-scoring.md) | 213 | 2 | 204 | 5 | 0 | 14 | 1 | 4 |
| [Recommendation](by-pattern/recommendation.md) | 4 | 0 | 4 | 0 | 0 | 0 | 0 | 0 |
| [Overview](by-pattern/overview.md) | 540 | 6 | 399 | 101 | 0 | 34 | 1 | 40 |

34 independent reports are filed under `overview` and no other pattern, so this table cannot count them for the decision they measured until a person files them under it.

## Languages

Rows recording each language (`languages`; a row may record several). 32 rows record none.

| Language | Rows |
| --- | --- |
| `python` | 671 |
| `typescript` | 508 |
| `javascript` | 177 |
| `go` | 70 |
| `rust` | 69 |
| `swift` | 23 |
| `java` | 17 |
| `csharp` | 13 |
| `ruby` | 13 |
| `kotlin` | 12 |
| `php` | 12 |
| `shell` | 12 |
| `cpp` | 10 |
| `elixir` | 10 |
| `c` | 4 |
| `haskell` | 1 |
| `lua` | 1 |

## How rows reach Jev

`platforms` records how a row reaches Jev. Discovery does not tag it: `scripts/discover_candidates.py` and the drafts it writes leave the field to the person adding a row, and `typesafe-api` is what a row records when nobody named another route. So the first group below counts that default at least as much as a finding: a row that reaches Jev through a pass-through may record `typesafe-api` alone ([compatibility](compatibility.md)). Each row counts in exactly one group.

| Group | Rows |
| --- | --- |
| `typesafe-api` and nothing else | 1244 |
| At least one value another surface in [the compatibility table](compatibility.md) stands for (a gateway, SDK or framework), and not `self-hosted` | 154 |
| Besides `typesafe-api`, only values no compatibility surface stands for (a host, tool or framework the example runs in, or a route that table does not describe), and not `self-hosted` | 89 |
| `self-hosted`, whatever else is recorded | 110 |
| No value recorded | 26 |

Every value rows record, with the compatibility surfaces that stand for it:

| Value | Compatibility surface | Rows |
| --- | --- | --- |
| `typesafe-api` | `typesafe-native` | 1423 |
| `self-hosted` | — | 110 |
| `openrouter` | `openrouter` | 100 |
| `claude-code` | — | 70 |
| `vercel-ai-gateway` | `vercel-eval`, `vercel-compat` | 54 |
| `mcp` | — | 37 |
| `cloudflare-workers-ai` | `cloudflare` | 11 |
| `opencode-zen` | — | 8 |
| `langchain` | `langchain` | 6 |
| `vercel-ai-sdk` | `vercel-eval`, `ai-sdk-direct` | 5 |
| `github` | — | 4 |
| `jevai-org` | — | 4 |
| `postgresql` | — | 3 |
| `discord` | — | 2 |
| `effect` | — | 2 |
| `litellm` | `litellm` | 2 |
| `pydantic-ai` | `pydantic-ai` | 2 |
| `ruby-llm` | — | 2 |
| `aimlapi` | `aimlapi` | 1 |
| `airflow` | — | 1 |
| `autogpt` | — | 1 |
| `bifrost` | `bifrost` | 1 |
| `composio` | — | 1 |
| `kiln` | — | 1 |
| `lancedb` | — | 1 |
| `langfuse` | — | 1 |
| `netlify` | `netlify` | 1 |
| `opik` | — | 1 |
| `rig` | `rig` | 1 |
| `spring-ai` | — | 1 |

## Licences

The licences the linked repositories declare are counted on [the sources page](sources.md#licences), beside what this repository's own licence covers.

## Stars by kind

Rows of each kind per star band, from GitHub's count at the last weekly refresh; a row without a repository has no count. The median is the band of the middle row (the lower of two). A band is a popularity signal, not a quality verdict, and says nothing about upkeep.

| Kind | Rows | With a star count | under 10 | ★10+ | ★100+ | ★1k+ | ★10k+ | ★100k+ | Median band |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Official docs (`official-docs`) | 31 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | ★1k+ |
| Integration (`integration`) | 40 | 28 | 8 | 9 | 1 | 4 | 5 | 1 | ★10+ |
| Project (`project`) | 812 | 737 | 360 | 238 | 98 | 22 | 17 | 2 | ★10+ |
| Plugin (`plugin`) | 334 | 296 | 142 | 119 | 30 | 4 | 1 | 0 | ★10+ |
| SDK (`sdk`) | 125 | 114 | 85 | 21 | 6 | 1 | 1 | 0 | under 10 |
| Snippet (`snippet`) | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Tutorial (`tutorial`) | 23 | 15 | 3 | 8 | 2 | 2 | 0 | 0 | ★10+ |
| Article (`article`) | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Video (`video`) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Benchmark (`benchmark`) | 111 | 91 | 57 | 24 | 6 | 2 | 1 | 1 | under 10 |
| Discussion (`discussion`) | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Jev-like alternative (`alternative`) | 123 | 110 | 19 | 46 | 31 | 13 | 1 | 0 | ★10+ |

## Languages by decision pattern

Rows per pattern recording each of the 6 most recorded languages; the rest share one column. A row recording two languages counts in both, and a row filed under two patterns counts in both.

| Pattern | `python` | `typescript` | `javascript` | `go` | `rust` | `swift` | Other languages |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Tool selection](by-pattern/tool-selection.md) | 132 | 107 | 47 | 4 | 6 | 8 | 2 |
| [Intent routing](by-pattern/intent-routing.md) | 33 | 22 | 5 | 2 | 0 | 2 | 5 |
| [Context compaction](by-pattern/context-compaction.md) | 16 | 32 | 6 | 3 | 2 | 0 | 0 |
| [Safety gating](by-pattern/safety-gating.md) | 70 | 77 | 28 | 9 | 6 | 1 | 3 |
| [Output validation](by-pattern/output-validation.md) | 67 | 70 | 22 | 8 | 10 | 1 | 5 |
| [Retry control](by-pattern/retry-control.md) | 3 | 2 | 1 | 0 | 1 | 1 | 1 |
| [Human escalation](by-pattern/human-escalation.md) | 58 | 34 | 7 | 4 | 4 | 0 | 2 |
| [Model routing](by-pattern/model-routing.md) | 29 | 51 | 16 | 2 | 6 | 1 | 1 |
| [Speculative fan-out](by-pattern/fan-out.md) | 28 | 18 | 6 | 1 | 2 | 1 | 5 |
| [Search & ranking](by-pattern/search-ranking.md) | 45 | 33 | 7 | 8 | 10 | 1 | 6 |
| [Structured extraction](by-pattern/data-extraction.md) | 22 | 11 | 4 | 0 | 0 | 0 | 1 |
| [Classification](by-pattern/classification.md) | 98 | 69 | 33 | 5 | 7 | 1 | 22 |
| [ML feature extraction](by-pattern/feature-extraction.md) | 5 | 3 | 1 | 0 | 0 | 0 | 1 |
| [Document triage](by-pattern/document-triage.md) | 9 | 5 | 7 | 0 | 2 | 0 | 0 |
| [Support triage](by-pattern/support-triage.md) | 9 | 4 | 0 | 1 | 0 | 0 | 3 |
| [Content scoring](by-pattern/content-scoring.md) | 96 | 71 | 29 | 2 | 5 | 3 | 11 |
| [Recommendation](by-pattern/recommendation.md) | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| [Overview](by-pattern/overview.md) | 229 | 117 | 44 | 38 | 30 | 9 | 65 |

## Patterns filed together

488 rows are filed under more than one pattern. The 10 pairs most often filed on the same row:

| Patterns | Rows |
| --- | --- |
| [Classification](by-pattern/classification.md) + [Content scoring](by-pattern/content-scoring.md) | 56 |
| [Safety gating](by-pattern/safety-gating.md) + [Output validation](by-pattern/output-validation.md) | 45 |
| [Tool selection](by-pattern/tool-selection.md) + [Safety gating](by-pattern/safety-gating.md) | 39 |
| [Safety gating](by-pattern/safety-gating.md) + [Classification](by-pattern/classification.md) | 39 |
| [Human escalation](by-pattern/human-escalation.md) + [Classification](by-pattern/classification.md) | 32 |
| [Tool selection](by-pattern/tool-selection.md) + [Output validation](by-pattern/output-validation.md) | 30 |
| [Safety gating](by-pattern/safety-gating.md) + [Human escalation](by-pattern/human-escalation.md) | 30 |
| [Safety gating](by-pattern/safety-gating.md) + [Content scoring](by-pattern/content-scoring.md) | 27 |
| [Human escalation](by-pattern/human-escalation.md) + [Content scoring](by-pattern/content-scoring.md) | 27 |
| [Output validation](by-pattern/output-validation.md) + [Content scoring](by-pattern/content-scoring.md) | 25 |

## Authors

1506 rows name an author; they name 1379 different ones, compared by display name without regard to case. 1280 of them have one row here, 80 two, and 19 three or more; the most any one author has is 6. No author is named on this page: it shows how concentrated the catalogue is, not who contributes to it.

## Over time

The catalogue's counts at each weekly refresh, from the snapshots in `history/` (generated data, never a source): 7 since 2026-09-30, the newest 7 shown. A count is what was catalogued on that day, not how the ecosystem grew; a dash is a count that snapshot did not record. Candidates to read is the discovery queue's "To read" (issue #14), recorded since 2026-10-30: when it grows, drafting is behind discovery.

| Snapshot | Entries | With code | Rows citing a call site | Independent reports | Negative results | Alternatives | No licence declared | Candidates to read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-30 | 1210 | 1182 | 1076 | 71 | 5 | 58 | 198 | — |
| 2026-10-08 | 1214 | 1185 | 1078 | 71 | 5 | 59 | 197 | — |
| 2026-10-14 | 1217 | 1186 | 1079 | 72 | 5 | 59 | 196 | — |
| 2026-10-21 | 1218 | 1187 | 1079 | 72 | 5 | 60 | 194 | — |
| 2026-10-28 | 1265 | 1233 | 1107 | 72 | 5 | 78 | 192 | — |
| 2026-11-04 | 1370 | 1338 | 1192 | 78 | 5 | 97 | 205 | 444 |
| 2026-11-11 | 1483 | 1451 | 1287 | 90 | 5 | 114 | 214 | 443 |

---

Generated by `scripts/build_shape.py` from `catalog.json`, `compat.json`, `patterns.json`, the entry schema and the snapshots in `history/`; edit those, not this page.
