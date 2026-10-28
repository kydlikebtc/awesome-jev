<!-- Written by scripts/build_shape.py from catalog.json, compat.json, patterns.json, the entry schema and history/. Edit those, not this file. -->

# 目录的形状

<sub>[awesome-jev](../README.zh-CN.md) · [English](shape.md)</sub>

> 本页中文说明由模型撰写（机翻），未经人工审校。

把本目录当作一个数据集来描述的计数，每当 `catalog.json` 变化就重新生成；其背后最新一次链接检查的日期是 **2026-10-28**。这些数字描述的是目录收录了什么——即经由兄弟目录、本仓库的发现流程和贡献者进入目录的内容——而不是整个生态。star 区间是热度信号，不是质量结论；这里的一切都没有被本仓库运行或复现。`python3 scripts/counts.py` 以文本形式打印同样的数字；主要数字见[状态页](status.md)。

## 按决策模式看证据

目录对归入每个模式的行记录了什么：只是计数，不是结论。一行在所有适用的列里都计数，归入几个模式就在几个模式下计数。**官方文档**是 TypeSafe AI 自己的文档页（`kind: official-docs`）。**调用点**、**接口形态**和**仅示例**按 `evidence.kind` 记录的文件内容，统计引用了文件的行：项目调用 Jev 的位置；只采用了 Jev 的请求结构、并非基于 Jev 构建的文件；项目附带的示例。**独立报告**是没有标 `vendor-reported` 的基准测试行：测量是其作者的，未经本仓库复现。**负面结果**是作者本人为该用途测过 Jev、并得出不利于它的结论的行（作者自述；[在状态页列出](status.md#negative-results)）。**未引用文件**统计没有 `evidence` 的行（`evidence_none` 可能说明了原因）。MCP server 的 `list_patterns` 和每个模式的页面给出同样的数字。

| 模式 | 行数 | 官方文档 | 调用点 | 接口形态 | 仅示例 | 独立报告 | 负面结果 | 未引用文件 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [工具选择](by-pattern/tool-selection.zh-CN.md) | 236 | 3 | 228 | 4 | 0 | 11 | 1 | 4 |
| [意图路由](by-pattern/intent-routing.zh-CN.md) | 39 | 3 | 28 | 0 | 0 | 2 | 0 | 11 |
| [上下文压缩](by-pattern/context-compaction.zh-CN.md) | 37 | 0 | 37 | 0 | 0 | 2 | 2 | 0 |
| [安全闸门](by-pattern/safety-gating.zh-CN.md) | 142 | 2 | 136 | 2 | 0 | 10 | 0 | 4 |
| [输出校验](by-pattern/output-validation.zh-CN.md) | 136 | 2 | 131 | 1 | 0 | 11 | 0 | 4 |
| [重试控制](by-pattern/retry-control.zh-CN.md) | 8 | 0 | 7 | 1 | 0 | 0 | 0 | 0 |
| [人工升级](by-pattern/human-escalation.zh-CN.md) | 73 | 7 | 58 | 5 | 0 | 10 | 0 | 10 |
| [模型路由](by-pattern/model-routing.zh-CN.md) | 49 | 2 | 42 | 1 | 0 | 0 | 1 | 6 |
| [并行扇出](by-pattern/fan-out.zh-CN.md) | 34 | 3 | 26 | 1 | 0 | 1 | 0 | 7 |
| [检索与排序](by-pattern/search-ranking.zh-CN.md) | 71 | 3 | 67 | 0 | 0 | 6 | 1 | 4 |
| [结构化抽取](by-pattern/data-extraction.zh-CN.md) | 18 | 4 | 14 | 0 | 0 | 1 | 0 | 4 |
| [分类](by-pattern/classification.zh-CN.md) | 127 | 4 | 117 | 1 | 0 | 11 | 1 | 9 |
| [机器学习特征抽取](by-pattern/feature-extraction.zh-CN.md) | 8 | 1 | 7 | 0 | 0 | 0 | 0 | 1 |
| [文档分拣](by-pattern/document-triage.zh-CN.md) | 22 | 0 | 21 | 0 | 0 | 2 | 0 | 1 |
| [工单分拣](by-pattern/support-triage.zh-CN.md) | 9 | 1 | 4 | 0 | 0 | 1 | 0 | 5 |
| [内容评分](by-pattern/content-scoring.zh-CN.md) | 165 | 2 | 156 | 5 | 0 | 9 | 1 | 4 |
| [实时推荐](by-pattern/recommendation.zh-CN.md) | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| [总览](by-pattern/overview.zh-CN.md) | 475 | 6 | 373 | 63 | 0 | 23 | 1 | 39 |

有 23 份独立报告只归入了 `overview`、没有归入任何其他模式，所以在有人把它们归入所测的决策之前，这张表无法把它们计入那个决策。

## 语言

记录了每种语言的行数（`languages`；一行可以记录多种语言）。有 32 行没有记录语言。

| 语言 | 行数 |
| --- | --- |
| `python` | 490 |
| `typescript` | 415 |
| `javascript` | 153 |
| `rust` | 51 |
| `go` | 47 |
| `swift` | 17 |
| `java` | 15 |
| `ruby` | 12 |
| `shell` | 10 |
| `kotlin` | 9 |
| `php` | 8 |
| `csharp` | 7 |
| `elixir` | 7 |
| `cpp` | 6 |
| `c` | 5 |
| `haskell` | 1 |
| `lua` | 1 |

## 各行如何接入 Jev

`platforms` 记录一行如何接入 Jev。发现流程不会标注它：`scripts/discover_candidates.py` 及其生成的草稿都把这个字段留给添加该行的人，而没有人写明其他路径时，一行记录的就是 `typesafe-api`。所以下面第一组的数字至少同样反映了这个默认值，而不只是发现：经由透传接入 Jev 的行也可能只记录 `typesafe-api`（见[兼容性](compatibility.md)）。每行恰好计入一组。

| 分组 | 行数 |
| --- | --- |
| 只有 `typesafe-api` | 1096 |
| 至少有一个值对应[兼容性表](compatibility.md)中的其他接入面（网关、SDK 或框架），且不含 `self-hosted` | 48 |
| 除 `typesafe-api` 外只记录没有任何兼容性接入面对应的值（示例运行所在的主机、工具或框架，或该表未描述的路径），且不含 `self-hosted` | 36 |
| 含 `self-hosted`，无论还记录了什么 | 64 |
| 未记录任何值 | 21 |

各行记录的每个值，以及对应它的兼容性接入面：

| 值 | 兼容性接入面 | 行数 |
| --- | --- | --- |
| `typesafe-api` | `typesafe-native` | 1147 |
| `self-hosted` | — | 64 |
| `vercel-ai-gateway` | `vercel-eval`, `vercel-compat` | 21 |
| `claude-code` | — | 18 |
| `openrouter` | `openrouter` | 18 |
| `mcp` | — | 6 |
| `github` | — | 4 |
| `langchain` | `langchain` | 4 |
| `jevai-org` | — | 3 |
| `opencode-zen` | — | 2 |
| `postgresql` | — | 2 |
| `pydantic-ai` | `pydantic-ai` | 2 |
| `vercel-ai-sdk` | `vercel-eval`, `ai-sdk-direct` | 2 |
| `aimlapi` | `aimlapi` | 1 |
| `airflow` | — | 1 |
| `autogpt` | — | 1 |
| `bifrost` | `bifrost` | 1 |
| `cloudflare-workers-ai` | `cloudflare` | 1 |
| `composio` | — | 1 |
| `discord` | — | 1 |
| `effect` | — | 1 |
| `kiln` | — | 1 |
| `lancedb` | — | 1 |
| `langfuse` | — | 1 |
| `litellm` | `litellm` | 1 |
| `netlify` | `netlify` | 1 |
| `opik` | — | 1 |
| `rig` | `rig` | 1 |
| `ruby-llm` | — | 1 |
| `spring-ai` | — | 1 |

## 许可证

被链接仓库声明的许可证统计在[来源页](sources.md#licences)，旁边说明了本仓库自身许可覆盖的范围。

## 按类型看 star

每种类型在各 star 区间的行数，取自最近一次每周刷新时 GitHub 的计数；没有仓库的行没有计数。中位数是居中那一行所在的区间（两行居中时取较低者）。区间是热度信号，不是质量结论，也不说明是否有人维护。

| 类型 | 行数 | 有 star 计数 | 不足 10 | ★10+ | ★100+ | ★1k+ | ★10k+ | ★100k+ | 中位区间 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 官方文档 (`official-docs`) | 31 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | ★1k+ |
| 平台集成 (`integration`) | 35 | 25 | 8 | 6 | 1 | 4 | 5 | 1 | ★10+ |
| 开源项目 (`project`) | 674 | 671 | 357 | 186 | 90 | 21 | 15 | 2 | 不足 10 |
| 插件 (`plugin`) | 241 | 241 | 126 | 81 | 29 | 4 | 1 | 0 | 不足 10 |
| SDK (`sdk`) | 99 | 98 | 75 | 17 | 5 | 0 | 1 | 0 | 不足 10 |
| 代码片段 (`snippet`) | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| 教程 (`tutorial`) | 12 | 9 | 2 | 3 | 2 | 2 | 0 | 0 | ★10+ |
| 文章 (`article`) | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| 视频 (`video`) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| 基准测试 (`benchmark`) | 72 | 69 | 49 | 13 | 4 | 1 | 1 | 1 | 不足 10 |
| 讨论 (`discussion`) | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — |
| Jev 替代实现 (`alternative`) | 78 | 76 | 12 | 27 | 26 | 9 | 2 | 0 | ★10+ |

## 按决策模式看语言

每个模式下记录了最常见的 6 种语言各自的行数；其余语言合为一列。记录两种语言的行在两列都计数，归入两个模式的行在两个模式下都计数。

| 模式 | `python` | `typescript` | `javascript` | `rust` | `go` | `swift` | 其他语言 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [工具选择](by-pattern/tool-selection.zh-CN.md) | 91 | 88 | 45 | 3 | 4 | 6 | 1 |
| [意图路由](by-pattern/intent-routing.zh-CN.md) | 18 | 14 | 3 | 0 | 1 | 0 | 3 |
| [上下文压缩](by-pattern/context-compaction.zh-CN.md) | 10 | 22 | 4 | 1 | 0 | 0 | 0 |
| [安全闸门](by-pattern/safety-gating.zh-CN.md) | 50 | 60 | 20 | 4 | 5 | 0 | 4 |
| [输出校验](by-pattern/output-validation.zh-CN.md) | 45 | 54 | 19 | 7 | 4 | 1 | 4 |
| [重试控制](by-pattern/retry-control.zh-CN.md) | 3 | 2 | 1 | 0 | 0 | 1 | 1 |
| [人工升级](by-pattern/human-escalation.zh-CN.md) | 44 | 22 | 1 | 1 | 0 | 0 | 2 |
| [模型路由](by-pattern/model-routing.zh-CN.md) | 18 | 21 | 9 | 1 | 0 | 1 | 0 |
| [并行扇出](by-pattern/fan-out.zh-CN.md) | 17 | 13 | 3 | 1 | 1 | 1 | 4 |
| [检索与排序](by-pattern/search-ranking.zh-CN.md) | 31 | 21 | 5 | 8 | 3 | 0 | 5 |
| [结构化抽取](by-pattern/data-extraction.zh-CN.md) | 11 | 3 | 4 | 0 | 0 | 0 | 0 |
| [分类](by-pattern/classification.zh-CN.md) | 46 | 35 | 25 | 3 | 1 | 0 | 14 |
| [机器学习特征抽取](by-pattern/feature-extraction.zh-CN.md) | 5 | 2 | 1 | 0 | 0 | 0 | 0 |
| [文档分拣](by-pattern/document-triage.zh-CN.md) | 7 | 5 | 7 | 2 | 0 | 0 | 0 |
| [工单分拣](by-pattern/support-triage.zh-CN.md) | 5 | 2 | 0 | 0 | 1 | 0 | 3 |
| [内容评分](by-pattern/content-scoring.zh-CN.md) | 70 | 59 | 24 | 4 | 1 | 1 | 9 |
| [实时推荐](by-pattern/recommendation.zh-CN.md) | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| [总览](by-pattern/overview.zh-CN.md) | 183 | 119 | 45 | 24 | 31 | 8 | 52 |

## 一起归档的模式

有 300 行归入了不止一个模式。最常出现在同一行上的 10 对模式：

| 模式 | 行数 |
| --- | --- |
| [安全闸门](by-pattern/safety-gating.zh-CN.md) + [输出校验](by-pattern/output-validation.zh-CN.md) | 31 |
| [工具选择](by-pattern/tool-selection.zh-CN.md) + [安全闸门](by-pattern/safety-gating.zh-CN.md) | 27 |
| [人工升级](by-pattern/human-escalation.zh-CN.md) + [内容评分](by-pattern/content-scoring.zh-CN.md) | 27 |
| [分类](by-pattern/classification.zh-CN.md) + [内容评分](by-pattern/content-scoring.zh-CN.md) | 25 |
| [安全闸门](by-pattern/safety-gating.zh-CN.md) + [内容评分](by-pattern/content-scoring.zh-CN.md) | 22 |
| [输出校验](by-pattern/output-validation.zh-CN.md) + [内容评分](by-pattern/content-scoring.zh-CN.md) | 22 |
| [安全闸门](by-pattern/safety-gating.zh-CN.md) + [分类](by-pattern/classification.zh-CN.md) | 21 |
| [工具选择](by-pattern/tool-selection.zh-CN.md) + [输出校验](by-pattern/output-validation.zh-CN.md) | 19 |
| [安全闸门](by-pattern/safety-gating.zh-CN.md) + [人工升级](by-pattern/human-escalation.zh-CN.md) | 19 |
| [工具选择](by-pattern/tool-selection.zh-CN.md) + [内容评分](by-pattern/content-scoring.zh-CN.md) | 18 |

## 作者

有 1148 行写明了作者，共 1044 位不同的作者（按显示名比较，不区分大小写）。其中 971 位在本目录只有一行，58 位有两行，15 位有三行或更多；单个作者最多有 11 行。本页不列出任何作者的名字：它显示的是目录的集中程度，而不是谁在贡献。

## 随时间的变化

每次每周刷新时目录的计数，取自 `history/` 中的快照（生成的数据，从不作为数据源）：自 2026-09-30 起共 5 份，显示最新的 5 份。计数反映的是当天目录收录了什么，而不是生态增长了多少；短横表示该快照没有记录这项计数。

| 快照 | 条目 | 含代码 | 引用调用点的行 | 独立报告 | 负面结果 | 替代实现 | 未声明许可证 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09-30 | 1210 | 1182 | 1076 | 71 | 5 | 58 | 198 |
| 2026-10-08 | 1214 | 1185 | 1078 | 71 | 5 | 59 | 197 |
| 2026-10-14 | 1217 | 1186 | 1079 | 72 | 5 | 59 | 196 |
| 2026-10-21 | 1218 | 1187 | 1079 | 72 | 5 | 60 | 194 |
| 2026-10-28 | 1265 | 1233 | 1107 | 72 | 5 | 78 | 192 |

---

由 `scripts/build_shape.py` 根据 `catalog.json`、`compat.json`、`patterns.json`、条目 schema 与 `history/` 中的快照生成；请修改这些文件，不要改本页。
