# 工单分拣

<sub>[awesome-jev](../../README.zh-CN.md) · [English](support-triage.md)</sub>

_按意图和紧急度路由支持工单与会话。_

这个决策的全部已收录例子 —— 共 9 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#工单分拣)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=support-triage&lang=zh)还能按语言、原语和形态进一步筛选。

这个决策的设计说明见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#support-triage)：它决定什么、用哪种原语来建模，以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版](../patterns.md#support-triage)译写，以英文版为准。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 1 · 调用点 4 · 接口形态 0 · 仅示例 0 · 独立报告 1 · 负面结果 0 · 未引用文件 5。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

TypeSafe AI 自己发布、归在这个模式下的材料（标为 `official` 的行）。每一条在下文也都列出，附有摘要。 <sub>(机翻)</sub>

- [Quickstart](https://docs.typesafe.ai/introduction/quickstart) <sub>`官方文档` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

## 本仓库的示例

本仓库 [`examples/`](../../examples/) 里归在这个模式下的代码。每一条在下文也都列出，附有摘要；[示例的 README](../../examples/README.md) 说明了它们核验到了哪一步。 <sub>(机翻)</sub>

- [Example: three primitives in one request](../../examples/01-three-primitives/main.py) <sub>`代码片段` · `Py` · `choice` · `score` · `noul` · ⚠ `代码未实测`</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）；注明“模型阅读”的，则是模型阅读该文件的日期（`evidence.model_read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

- **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐ — 官方第一课：一条工单，一次请求里同时问一个 Choice、一个 Score 和一个 Noul，给了 Python / JS / cURL 三种写法。
  <sub>`官方文档` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)** — 一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。
  <sub>`教程` · ★1k+ · `Py` · `choice` · `score` · `noul` · 调用点 [`models/jev/06-criteria.py`](https://github.com/daveebbelaar/ai-cookbook/blob/HEAD/models/jev/06-criteria.py)，2026-09-22 阅读</sub>

- **[spring-ai-typesafe](https://spring.io/blog/2026/09/21/spring-ai-typesafe-structured-judgment)** — 社区维护的 Spring AI starter，把类型化决策带到 Java，用 builder API 封装三种问题类型。
  <sub>`平台集成` · ★10+ · `Java` · `choice` · `score` · `noul` · 调用点 [`examples/src/main/java/org/springaicommunity/typesafe/demo/JevQuickstart.java`](https://github.com/spring-ai-community/spring-ai-typesafe/blob/HEAD/examples/src/main/java/org/springaicommunity/typesafe/demo/JevQuickstart.java)，2026-09-22 阅读</sub>

- **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)** — 最小化的第一次调用：同时问一个 choice、一个 score 和一个 noul，并标注了容易踩的那几处不对称。
  <sub>`代码片段` · `Py` · `choice` · `score` · `noul` · 调用点 [`examples/01-three-primitives/main.py`](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/01-three-primitives/main.py)，2026-09-22 阅读 · ⚠ `代码未实测`</sub>

- **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)** — 逐个用例走一遍 —— 智能体路由、智能体内部的决策层、工单分拣 —— 每个都给出具体的选项集和示例响应。
  <sub>`教程` · Mehul Gupta · `Py` · `choice` · ⚠ `付费墙`</sub>

- **[Jev on AI/ML API](https://docs.aimlapi.com/api-references/decision-models/typesafe/jev)** — 又一个网关接入路径，值得记一笔是因为它的端点路径和请求外壳跟原生 API、跟 Cloudflare 都不一样。
  <sub>`平台集成` · `Py` · `noul` · `choice` · `score`</sub>

- **[Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/)** — Workers AI binding 与 REST 示例：一次调用同时问 noul、choice、score，并给出含逐答案置信度的完整响应。
  <sub>`平台集成` · `TS` · `sh` · `noul` · `choice` · `score`</sub>

- **[jev-triage](https://github.com/boldbug1/jev-triage)** — 基于 TypeSafe AI Jev 决策模型的 Go 消息分诊 CLI：为消息归类、给紧急程度打分并决定去向。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · boldbug1 · `Go` · 调用点 [`main.go`](https://github.com/boldbug1/jev-triage/blob/HEAD/main.go)，2026-09-24 阅读</sub>

- **[Support-routing benchmark: 100 held-out cases](https://decisionmodelhub.com/benchmarks/support-routing)** — 在 100 条留出的虚构客服消息上，将 Jev 与 Clef、Clef Flash、OpenAI 的 Decisions API 以及 GPT-6 Luna 结构化输出基线进行对比：每条消息路由到五个团队标签之一；所有用例和各模型的作答记录均可下载。 <sub>(机翻)</sub>
  <sub>`基准测试` · DecisionModelHub · ⚠ `作者自荐`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
