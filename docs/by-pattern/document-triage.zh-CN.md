# 文档分拣

<sub>[awesome-jev](../../README.zh-CN.md) · [English](document-triage.md)</sub>

_对进来的文档、发票、表单做分类和路由。_

这个决策的全部已收录例子 —— 共 22 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#文档分拣)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=document-triage&lang=zh)还能按语言、原语和形态进一步筛选。

这个决策的设计说明见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#document-triage)：它决定什么、用哪种原语来建模，以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版](../patterns.md#document-triage)译写，以英文版为准。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 0 · 调用点 21 · 接口形态 0 · 仅示例 0 · 独立报告 2 · 负面结果 0 · 未引用文件 1。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

目录里没有归在这个模式下的 TypeSafe AI 官方材料。 <sub>(机翻)</sub>

## 本仓库的示例

本仓库没有这个模式的示例；已有的示例见 [`examples/`](../../examples/)。 <sub>(机翻)</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）；注明“模型阅读”的，则是模型阅读该文件的日期（`evidence.model_read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

*作者结论*是基准测试作者本人对 Jev 在其所测任务上给出的结论方向（`measurement.direction`：有利、好坏参半、不利或无定论），按作者的报告索引：属作者自述，未经本仓库复现；作者没有用文字说明结论的则不标。[docs/benchmarks.zh-CN.md](../benchmarks.zh-CN.md) 把每条基准测试的测量字段并列展示。 <sub>(机翻)</sub>

- **[docjev](https://github.com/jerryjliu/docjev)** — 对 PDF、DOCX 和 PPTX 文件做分类和切分：LiteParse 在本地提取每页文字，然后 Jev 用一个 choice 按你的规则选出文档类别；对多文档合订本则逐页回答一个类别 choice 和一个“新文档是否从这里开始”的 noul。其报告涵盖 40 份真实 PDF。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · jerryjliu · `Py` · 调用点 [`src/jev_docs/engines/jev.py`](https://github.com/jerryjliu/docjev/blob/HEAD/src/jev_docs/engines/jev.py)，2026-09-22 阅读</sub>

- **[formanator](https://github.com/timrogers/formanator)** — 从命令行或 MCP 客户端提交 Forma 福利报销。使用 --category-provider jev 时，Jev 用一个 choice 从 Forma 允许的“福利加类别”组合（另加 no_match）中挑一个，只看商家和描述；置信度低于 0.5 或无匹配时，回退到配置好的 LLM。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · ★100+ · timrogers · `Rs` · 调用点 [`src/typesafe.rs`](https://github.com/timrogers/formanator/blob/HEAD/src/typesafe.rs)，2026-09-22 阅读</sub>

- **[tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)** — 税务文档分页分类器：每页一次请求，问 Jev 两个 choice：页面类型（7 个选项）和 IRS 表单（230 个另加“不在列表中”），五种表单的附表再用一个后续 choice 细分；选项描述由 IRS 官方 PDF 生成，代码以 0.95 为门槛。作者在 314 页已填写表单上测得严格错误为零。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★100+ · kyotofin · `TS` · 调用点 [`src/backend.ts`](https://github.com/kyotofin/tax-doc-classifier/blob/HEAD/src/backend.ts)，2026-09-22 阅读</sub>

- **[doc-router](https://github.com/misbahsy/doc-router)** — 逐页判断 PDF 是否需要 OCR 的 Rust 库：由 Jev（默认是内置的启发式规则）根据文字层证据对每页回答一个 noul；有文字的页面在本地提取，只有其余页面经 LiteLLM 交给 OCR 模型。在作者的测试中，155 页里只有 87 页计费。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · misbahsy · `Rs` · 调用点 [`crates/doc-router-jev/src/wire.rs`](https://github.com/misbahsy/doc-router/blob/HEAD/crates/doc-router-jev/src/wire.rs)，2026-09-22 阅读</sub>

- **[jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)** — 独立的社区地图，以中文为主，说明哪些任务适合交给 Jev 以及原因，依据是附带真实 API 调用记录的测试集，而不是排行榜：答案就在给定文字里时很准，比如该点击哪个 DOM 元素；别处则可能失准（DAIR Emotion 上平均置信度 0.819，实际只对 48%）。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★10+ · zaious · `Py` · 调用点 [`scripts/common/jev_client.py`](https://github.com/Zaious/jev-capability-atlas/blob/HEAD/scripts/common/jev_client.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jevmory](https://github.com/romiluz13/jevmory)** — 编程智能体的本地记忆：钩子把会话中真正说过的话按原文引语保存；jevmory audit 针对 MEMORY.md 的每一行问 Jev：已保存的证据是支持还是反驳它，并把各行标为保留、过时、错误或无依据。只用 Python 标准库和 SQLite；评分须主动开启。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · romiluz13 · `Py` · 调用点 [`jevmory/cli.py`](https://github.com/romiluz13/jevmory/blob/HEAD/jevmory/cli.py)，2026-09-22 阅读</sub>

- **[pdf-race](https://github.com/goodrahstar/pdf-race)** — 让三条流水线在 12 篇 arXiv 论文上比赛：Docling 加 Jev、Docling 加 Gemini 3.8 Flash，以及 Gemini 直接读 PDF，每篇回答四个问题，按 arXiv 自己的元数据评分。三条都答对了 12 篇中全部的类别和标题；Jev 这条的成本是 $0.0022，另两条为 $0.036 和 $0.088。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · ★10+ · goodrahstar · `JS` · 调用点 [`lib/lanes.mjs`](https://github.com/goodrahstar/pdf-race/blob/HEAD/lib/lanes.mjs)，2026-09-24 阅读</sub>

- **[decision-first](https://github.com/harrymunro/decision-first)** — 适用于 Claude Code、Codex、Cursor 等的智能体技能：当某一步工作是有界判断（分类、分诊、排序、路由、筛选、核验、把关）时，智能体先通过附带的脚本向 Jev 发送 noul、choice 或 score 问题，再考虑写正则或 LLM 提示，并记录每次尝试，无论是否采用。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · harrymunro · `Py` · 调用点 [`skills/decision-first/scripts/ask.py`](https://github.com/harrymunro/decision-first/blob/HEAD/skills/decision-first/scripts/ask.py)，2026-09-22 阅读</sub>

- **[Jev Playwright](https://github.com/arthurfiorette/jev-playwright)** — 一个 Playwright 报告器：在启动任何浏览器之前，询问 Jev 某次代码改动可能影响哪些现有端到端测试，并跳过明显无关的测试。默认会发送改动路径、补丁和测试代码；README 提醒它可能漏掉受影响的测试。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · arthurfiorette · `TS` · 调用点 [`src/config.ts`](https://github.com/arthurfiorette/jev-playwright/blob/HEAD/src/config.ts)，2026-10-24 模型阅读</sub>

- **[jev-boe-demo](https://github.com/Tatuck/jev-boe-demo)** — 每天早上，流水线下载西班牙官方公报（BOE），对每条内容用一次调用问 Jev：一个 0–3 的 score，衡量它对普通人生活的影响（2 分起算作相关）；13 个类别 noul（住房、就业、税收等），高于 0.6 才归类；以及一个 choice，选出静态网站上作为摘要引用的段落。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · tatuck · `TS` · 调用点 [`pipeline/analyze.ts`](https://github.com/Tatuck/jev-boe-demo/blob/HEAD/pipeline/analyze.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-builder](https://github.com/collapseindex/jev-builder)** — 构建 Jev 请求的网页表单：选模板、填空、复制代码。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · collapseindex · `JS` · 调用点 [`jev-builder-core.js`](https://github.com/collapseindex/jev-builder/blob/HEAD/jev-builder-core.js)，2026-09-22 阅读</sub>

- **[jev-decision-lab](https://github.com/jlov7/jev-decision-lab)** — 一个本地实验室，观察 Jev 在真实业务场景上的判断表现。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jlov7 · `Py` · 调用点 [`jev_lab/adapters.py`](https://github.com/jlov7/jev-decision-lab/blob/HEAD/jev_lab/adapters.py)，2026-09-22 阅读</sub>

- **[jev-document-classification](https://github.com/Charlyhno-eng/jev-document-classification)** — 对文本文档做快速且低成本的分类。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · charlyhno-eng · `TS` · 调用点 [`server/classification-cache.ts`](https://github.com/Charlyhno-eng/jev-document-classification/blob/HEAD/server/classification-cache.ts)，2026-09-22 阅读</sub>

- **[jev-information-extraction](https://github.com/abhishekmamdapure/jev-information-extraction)** — 解析 PDF 并抽取相关信息。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · abhishekmamdapure · `Py` · 调用点 [`backend/main.py`](https://github.com/abhishekmamdapure/jev-information-extraction/blob/HEAD/backend/main.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-layer](https://github.com/typakon4/jev-layer)** — 可移植的 System-1 决策层，面向智能体 harness，含宿主自控路由、凭据与回放。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`平台集成` · typakon4 · `JS` · 调用点 [`src/providers/typesafe.mjs`](https://github.com/typakon4/jev-layer/blob/HEAD/src/providers/typesafe.mjs)，2026-09-22 阅读</sub>

- **[jev-organize](https://github.com/nexibeo/jev-organize)** — 把一堆公司文件扔进去，就能按部门、类型、敏感度、日期、交易方等分类整理好。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · nexibeo · `JS` · 调用点 [`skills/jev-organize/scripts/src/jev.mjs`](https://github.com/nexibeo/jev-organize/blob/HEAD/skills/jev-organize/scripts/src/jev.mjs)，2026-09-24 阅读</sub>

- **[jev-report](https://github.com/HackSing/jev-report)** — 发明 RLHF 的人这次做了个不会说话的模型：Jev 独立研究报告，含中文实测复现包与可回溯数据表。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · hacksing · `Py` · 调用点 [`figs.py`](https://github.com/HackSing/jev-report/blob/HEAD/figs.py)，2026-09-22 阅读</sub>

- **[jev-score](https://github.com/a-Fig/jev-score)** — 由 Jev 驱动的本地优先文档评估工作区。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · a-fig · `JS` · 调用点 [`src/jev.mjs`](https://github.com/a-Fig/jev-score/blob/HEAD/src/jev.mjs)，2026-09-22 阅读</sub>

- **[last-exit](https://github.com/0x963D/last-exit)** — 由 Jev 驱动的赛博朋克边境遭遇战：忽悠守卫，检查凭据。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · 0x963d · `JS` · 调用点 [`lib/hosted.mjs`](https://github.com/0x963D/last-exit/blob/HEAD/lib/hosted.mjs)，2026-09-22 阅读</sub>

- **[Quicksilver](https://github.com/UditAkhourii/quicksilver)** — 一个 Claude Code 技能，把“是否相关”的判断交给 Jev：对每个文件、每行日志或每张工单问一个 noul（例如“这些文件里哪些处理鉴权？”），并行询问并按概率排序，于是 Claude 拿到的是带置信度的候选清单，而不必通读全部内容。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`插件` · uditakhourii · `JS` · `noul` · 调用点 [`skills/quicksilver/scripts/qs.mjs`](https://github.com/UditAkhourii/quicksilver/blob/HEAD/skills/quicksilver/scripts/qs.mjs)，2026-10-24 模型阅读</sub>

- **[tiab-review-plugin](https://github.com/youkiti/tiab-review-plugin)** — 一个加速系统综述中“标题与摘要筛选”的 Chrome 扩展，已上架 Chrome 应用商店。 <sub>(机翻)</sub>
  <sub>`插件` · youkiti · `TS` · 调用点 [`src/lib/providers/typesafe.ts`](https://github.com/youkiti/tiab-review-plugin/blob/HEAD/src/lib/providers/typesafe.ts)，2026-09-24 阅读</sub>

- **[jevai.org community showcase cases](https://www.jevai.org/cases)** — 九个社区演练场景：意图路由、发票分类、新闻过滤、商品打标、内容审核、主张核验、CSV 校验等。
  <sub>`开源项目` · ⚠ `宣称未核实`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
