<!-- Written by scripts/build_shape.py from catalog.json, compat.json, patterns.json, the entry schema and history/. Edit those, not this file. -->

# The catalogue's shape

<sub>[awesome-jev](../README.md) · [中文](shape.zh-CN.md)</sub>

Counts that describe this catalogue as a dataset, regenerated from `catalog.json` whenever it changes; the newest link check behind them is dated **2026-11-11**. They describe what the catalogue holds, which is what reached it through the sibling directories, this repository's discovery and its contributors, not the ecosystem at large. A star band is a popularity signal, not a quality verdict, and nothing here was run or reproduced by this repository. `python3 scripts/counts.py` prints the same numbers as text; the headline figures are on [the status page](status.md).

## Evidence by decision pattern

What the catalogue records about the rows filed under each pattern: reports counted, not a verdict. A row counts in every column that applies and under every pattern it is filed under. **Official documentation** is TypeSafe AI's own documentation pages (`kind: official-docs`). **Call site**, **wire shape** and **example only** count rows citing a file, by what `evidence.kind` records it shows: where the project calls Jev; a file speaking Jev's request shape rather than building on Jev; only an example the project ships. **Independent reports** are benchmark rows not flagged `vendor-reported`: their authors' measurements, not reproduced by this repository. **Negative results** are rows whose own author measured Jev for the use and concluded against it (author-stated; [listed on the status page](status.md#negative-results)). **No file cited** counts rows with no `evidence` (`evidence_none` may say why). The MCP server's `list_patterns` and each pattern's page give the same numbers.

| Pattern | Rows | Official documentation | Call site | Wire shape | Example only | Independent reports | Negative results | No file cited |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Tool selection](by-pattern/tool-selection.md) | 280 | 3 | 269 | 7 | 0 | 12 | 1 | 4 |
| [Intent routing](by-pattern/intent-routing.md) | 63 | 3 | 52 | 0 | 0 | 4 | 0 | 11 |
| [Context compaction](by-pattern/context-compaction.md) | 47 | 0 | 47 | 0 | 0 | 2 | 2 | 0 |
| [Safety gating](by-pattern/safety-gating.md) | 172 | 2 | 165 | 3 | 0 | 13 | 0 | 4 |
| [Output validation](by-pattern/output-validation.md) | 168 | 2 | 163 | 1 | 0 | 13 | 0 | 4 |
| [Retry control](by-pattern/retry-control.md) | 8 | 0 | 7 | 1 | 0 | 0 | 0 | 0 |
| [Human escalation](by-pattern/human-escalation.md) | 93 | 7 | 78 | 5 | 0 | 11 | 0 | 10 |
| [Model routing](by-pattern/model-routing.md) | 92 | 2 | 84 | 1 | 1 | 0 | 1 | 6 |
| [Speculative fan-out](by-pattern/fan-out.md) | 44 | 3 | 36 | 1 | 0 | 1 | 0 | 7 |
| [Search & ranking](by-pattern/search-ranking.md) | 95 | 3 | 91 | 0 | 0 | 8 | 1 | 4 |
| [Structured extraction](by-pattern/data-extraction.md) | 34 | 4 | 30 | 0 | 0 | 3 | 0 | 4 |
| [Classification](by-pattern/classification.md) | 197 | 4 | 185 | 3 | 0 | 20 | 1 | 9 |
| [ML feature extraction](by-pattern/feature-extraction.md) | 9 | 1 | 8 | 0 | 0 | 0 | 0 | 1 |
| [Document triage](by-pattern/document-triage.md) | 23 | 0 | 22 | 0 | 0 | 2 | 0 | 1 |
| [Support triage](by-pattern/support-triage.md) | 13 | 1 | 8 | 0 | 0 | 2 | 0 | 5 |
| [Content scoring](by-pattern/content-scoring.md) | 192 | 2 | 183 | 5 | 0 | 13 | 1 | 4 |
| [Recommendation](by-pattern/recommendation.md) | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 |
| [Overview](by-pattern/overview.md) | 521 | 6 | 383 | 98 | 0 | 29 | 1 | 40 |

29 independent reports are filed under `overview` and no other pattern, so this table cannot count them for the decision they measured until a person files them under it.

## Languages

Rows recording each language (`languages`; a row may record several). 32 rows record none.

| Language | Rows |
| --- | --- |
| `python` | 621 |
| `typescript` | 473 |
| `javascript` | 170 |
| `rust` | 62 |
| `go` | 60 |
| `swift` | 22 |
| `java` | 16 |
| `ruby` | 13 |
| `kotlin` | 12 |
| `csharp` | 11 |
| `php` | 11 |
| `shell` | 11 |
| `elixir` | 9 |
| `cpp` | 7 |
| `c` | 5 |
| `haskell` | 1 |
| `lua` | 1 |

## How rows reach Jev

`platforms` records how a row reaches Jev. Discovery does not tag it: `scripts/discover_candidates.py` and the drafts it writes leave the field to the person adding a row, and `typesafe-api` is what a row records when nobody named another route. So the first group below counts that default at least as much as a finding: a row that reaches Jev through a pass-through may record `typesafe-api` alone ([compatibility](compatibility.md)). Each row counts in exactly one group.

| Group | Rows |
| --- | --- |
| `typesafe-api` and nothing else | 1198 |
| At least one value another surface in [the compatibility table](compatibility.md) stands for (a gateway, SDK or framework), and not `self-hosted` | 114 |
| Besides `typesafe-api`, only values no compatibility surface stands for (a host, tool or framework the example runs in, or a route that table does not describe), and not `self-hosted` | 68 |
| `self-hosted`, whatever else is recorded | 105 |
| No value recorded | 25 |

Every value rows record, with the compatibility surfaces that stand for it:

| Value | Compatibility surface | Rows |
| --- | --- | --- |
| `typesafe-api` | `typesafe-native` | 1327 |
| `self-hosted` | — | 105 |
| `openrouter` | `openrouter` | 68 |
| `claude-code` | — | 51 |
| `vercel-ai-gateway` | `vercel-eval`, `vercel-compat` | 42 |
| `mcp` | — | 21 |
| `cloudflare-workers-ai` | `cloudflare` | 8 |
| `langchain` | `langchain` | 5 |
| `opencode-zen` | — | 5 |
| `github` | — | 4 |
| `jevai-org` | — | 4 |
| `postgresql` | — | 3 |
| `vercel-ai-sdk` | `vercel-eval`, `ai-sdk-direct` | 3 |
| `effect` | — | 2 |
| `litellm` | `litellm` | 2 |
| `pydantic-ai` | `pydantic-ai` | 2 |
| `ruby-llm` | — | 2 |
| `aimlapi` | `aimlapi` | 1 |
| `airflow` | — | 1 |
| `autogpt` | — | 1 |
| `bifrost` | `bifrost` | 1 |
| `composio` | — | 1 |
| `discord` | — | 1 |
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
| Integration (`integration`) | 39 | 28 | 8 | 9 | 1 | 4 | 5 | 1 | ★10+ |
| Project (`project`) | 760 | 738 | 361 | 238 | 98 | 22 | 17 | 2 | ★10+ |
| Plugin (`plugin`) | 305 | 297 | 142 | 120 | 30 | 4 | 1 | 0 | ★10+ |
| SDK (`sdk`) | 116 | 114 | 85 | 21 | 6 | 1 | 1 | 0 | under 10 |
| Snippet (`snippet`) | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Tutorial (`tutorial`) | 20 | 15 | 3 | 8 | 2 | 2 | 0 | 0 | ★10+ |
| Article (`article`) | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Video (`video`) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Benchmark (`benchmark`) | 97 | 90 | 56 | 24 | 6 | 2 | 1 | 1 | under 10 |
| Discussion (`discussion`) | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Jev-like alternative (`alternative`) | 119 | 110 | 19 | 46 | 31 | 13 | 1 | 0 | ★10+ |

## Languages by decision pattern

Rows per pattern recording each of the 6 most recorded languages; the rest share one column. A row recording two languages counts in both, and a row filed under two patterns counts in both.

| Pattern | `python` | `typescript` | `javascript` | `rust` | `go` | `swift` | Other languages |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Tool selection](by-pattern/tool-selection.md) | 117 | 103 | 46 | 6 | 4 | 8 | 1 |
| [Intent routing](by-pattern/intent-routing.md) | 31 | 19 | 4 | 0 | 2 | 2 | 5 |
| [Context compaction](by-pattern/context-compaction.md) | 13 | 27 | 5 | 1 | 1 | 0 | 0 |
| [Safety gating](by-pattern/safety-gating.md) | 63 | 70 | 25 | 4 | 7 | 1 | 3 |
| [Output validation](by-pattern/output-validation.md) | 62 | 64 | 21 | 8 | 6 | 1 | 5 |
| [Retry control](by-pattern/retry-control.md) | 3 | 1 | 1 | 1 | 0 | 1 | 1 |
| [Human escalation](by-pattern/human-escalation.md) | 52 | 30 | 5 | 1 | 0 | 0 | 2 |
| [Model routing](by-pattern/model-routing.md) | 29 | 43 | 14 | 5 | 1 | 1 | 1 |
| [Speculative fan-out](by-pattern/fan-out.md) | 25 | 13 | 5 | 2 | 1 | 1 | 4 |
| [Search & ranking](by-pattern/search-ranking.md) | 42 | 26 | 7 | 8 | 6 | 1 | 7 |
| [Structured extraction](by-pattern/data-extraction.md) | 20 | 9 | 4 | 0 | 0 | 0 | 1 |
| [Classification](by-pattern/classification.md) | 80 | 57 | 31 | 5 | 1 | 0 | 20 |
| [ML feature extraction](by-pattern/feature-extraction.md) | 5 | 2 | 1 | 0 | 0 | 0 | 1 |
| [Document triage](by-pattern/document-triage.md) | 8 | 5 | 7 | 2 | 0 | 0 | 0 |
| [Support triage](by-pattern/support-triage.md) | 7 | 4 | 0 | 0 | 1 | 0 | 3 |
| [Content scoring](by-pattern/content-scoring.md) | 88 | 61 | 27 | 5 | 2 | 2 | 10 |
| [Recommendation](by-pattern/recommendation.md) | 2 | 1 | 0 | 0 | 0 | 0 | 0 |
| [Overview](by-pattern/overview.md) | 218 | 115 | 45 | 27 | 36 | 9 | 59 |

## Patterns filed together

420 rows are filed under more than one pattern. The 10 pairs most often filed on the same row:

| Patterns | Rows |
| --- | --- |
| [Classification](by-pattern/classification.md) + [Content scoring](by-pattern/content-scoring.md) | 42 |
| [Safety gating](by-pattern/safety-gating.md) + [Output validation](by-pattern/output-validation.md) | 39 |
| [Tool selection](by-pattern/tool-selection.md) + [Safety gating](by-pattern/safety-gating.md) | 35 |
| [Safety gating](by-pattern/safety-gating.md) + [Classification](by-pattern/classification.md) | 32 |
| [Tool selection](by-pattern/tool-selection.md) + [Output validation](by-pattern/output-validation.md) | 27 |
| [Human escalation](by-pattern/human-escalation.md) + [Content scoring](by-pattern/content-scoring.md) | 27 |
| [Safety gating](by-pattern/safety-gating.md) + [Content scoring](by-pattern/content-scoring.md) | 25 |
| [Output validation](by-pattern/output-validation.md) + [Content scoring](by-pattern/content-scoring.md) | 24 |
| [Safety gating](by-pattern/safety-gating.md) + [Human escalation](by-pattern/human-escalation.md) | 22 |
| [Human escalation](by-pattern/human-escalation.md) + [Classification](by-pattern/classification.md) | 22 |

## Authors

1393 rows name an author; they name 1273 different ones, compared by display name without regard to case. 1180 of them have one row here, 75 two, and 18 three or more; the most any one author has is 6. No author is named on this page: it shows how concentrated the catalogue is, not who contributes to it.

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
