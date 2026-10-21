# 结构化抽取

<sub>[awesome-jev](../../README.zh-CN.md) · [English](data-extraction.md)</sub>

_从杂乱文本中取出类型化字段 —— 靠在候选中选择，而不是生成。_

这个决策的全部已收录例子 —— 共 17 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#结构化抽取)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=data-extraction&lang=zh)还能按语言、原语和形态进一步筛选。

这个决策的设计说明见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#data-extraction)：它决定什么、用哪种原语来建模，以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版](../patterns.md#data-extraction)译写，以英文版为准。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 4 · 调用点 13 · 接口形态 0 · 仅示例 0 · 独立报告 1 · 负面结果 0 · 未引用文件 4。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

TypeSafe AI 自己发布、归在这个模式下的材料（标为 `official` 的行）。每一条在下文也都列出，附有摘要。 <sub>(机翻)</sub>

- [Cookbook: Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook) <sub>`官方文档` · `Py`</sub>
- [Cookbook: Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook) <sub>`官方文档` · `Py` · `choice`</sub>
- [Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat) <sub>`官方文档` · `Py`</sub>
- [Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade) <sub>`官方文档` · `Py`</sub>

## 本仓库的示例

本仓库没有这个模式的示例；已有的示例见 [`examples/`](../../examples/)。 <sub>(机翻)</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

- **[Cookbook: Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook)** ⭐ — 抽取绝对与相对日期：先问文档里点明了哪些部分，再在代码里做解析与校验，并按置信度决定是否送审。
  <sub>`官方文档` · `Py`</sub>

- **[Cookbook: Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook)** ⭐ — 先用正则找出候选的邮箱、电话、金额，再让模型挑出被问到的那一段，于是代码拿到的是逐字原值。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐ — 用两次请求把丢了格式的纯文本还原成 Markdown：一次把硬换行的段落重新接起来，一次给每个块分类。
  <sub>`官方文档` · `Py`</sub>

- **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐ — 「小模型 → 校验 → 推理模型」的两段级联，用一小部分成本拿到接近大推理模型的质量。
  <sub>`官方文档` · `Py`</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — 开源的 macOS computer use 与原生 GUI 自动化，运行在 Apple 芯片上。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · jcpsimmons · `JS` · 调用点 [`src/providers.mjs`](https://github.com/jcpsimmons/jev-macos-loop/blob/HEAD/src/providers.mjs)，2026-09-22 阅读</sub>

- **[jev-reviewer](https://github.com/choxos/jev-reviewer)** — 系统综述的数据抽取：让 Jev 从论文及其补充材料里按抽取表取值，并附原文引用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · choxos · `JS` · 调用点 [`docs/jev.js`](https://github.com/choxos/jev-reviewer/blob/HEAD/docs/jev.js)，2026-09-22 阅读</sub>

- **[jevfill](https://github.com/imohitmayank/jevfill)** — 一个 Chrome 扩展：用 Jev 根据零散的文字笔记自动填写网页表单。把个人信息以纯文本粘贴一次即可，无需结构化档案，随时按需填表。 <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · imohitmayank · `TS` · 调用点 [`src/jev/client.ts`](https://github.com/imohitmayank/jevfill/blob/HEAD/src/jev/client.ts)，2026-09-24 阅读</sub>

- **[JevSpan](https://github.com/lzq-0529/jev-span)** — 中英文零样本命名实体识别：代码按标点列出带精确字符位置的候选片段，由 Jev 的 choice 问题为每种实体类型提名窗口、核验每个候选（该类型、none、mixed 或 partial）并选出准确边界，每个实体都保留概率和决策过程。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★10+ · lzq-0529 · `Py` · `choice` · 调用点 [`src/jevspan/jev_client.py`](https://github.com/lzq-0529/jev-span/blob/HEAD/src/jevspan/jev_client.py)，2026-09-30 阅读 · ⚠ `疑似 AI 生成` `作者自荐`</sub>

- **[smart-paste](https://github.com/nomanjack/smart-paste)** — 根据粘贴的文本自动填写表单：把表单标题、字段标签和你的文字交给 TypeSafe，插入匹配到的值，提交前由你检查。 <sub>(机翻)</sub>
  <sub>`插件` · ★10+ · nomanjack · `JS` · 调用点 [`worker.js`](https://github.com/nomanjack/smart-paste/blob/HEAD/worker.js)，2026-09-24 阅读</sub>

- **[ask-jev](https://github.com/logicrw/ask-jev)** — 极快、失败即放行的建议式决策，以及面向 AI 编码智能体和 CLI 管道的逐字抽取式阅读视图。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · logicrw · `Py` · 调用点 [`scripts/jev_context.py`](https://github.com/logicrw/ask-jev/blob/HEAD/scripts/jev_context.py)，2026-09-24 阅读</sub>

- **[jev-data-questions](https://github.com/narulaskaran/jev-data-questions)** — 带上数据集，看到合适的图表：界面检查 CSV 的结构并提出洞察，由 Jev 填入具体数值。 <sub>(机翻)</sub>
  <sub>`开源项目` · narulaskaran · `TS` · 调用点 [`src/server/jev.ts`](https://github.com/narulaskaran/jev-data-questions/blob/HEAD/src/server/jev.ts)，2026-09-24 阅读 · ⚠ `无许可证`</sub>

- **[jev-information-extraction](https://github.com/abhishekmamdapure/jev-information-extraction)** — 解析 PDF 并抽取相关信息。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · abhishekmamdapure · `Py` · 调用点 [`backend/main.py`](https://github.com/abhishekmamdapure/jev-information-extraction/blob/HEAD/backend/main.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jev-mcp-dispatcher](https://github.com/abhishekashokvkumar/jev-mcp-dispatcher)** — 完全由 Jev 驱动的自然语言 MCP 工具分发器，不用通用 LLM。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`插件` · abhishekashokvkumar · `Py` · 调用点 [`jev_mcp_dispatcher.py`](https://github.com/abhishekashokvkumar/jev-mcp-dispatcher/blob/HEAD/jev_mcp_dispatcher.py)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[jeveryword](https://github.com/jkrup/jeveryword)** — 用 Jev 做文本抽取：字段抽取、PII 检测与逐字引文。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · jkrup · `JS` · 调用点 [`src/client.mjs`](https://github.com/jkrup/jeveryword/blob/HEAD/src/client.mjs)，2026-09-22 阅读</sub>

- **[jevsume](https://github.com/unownone/jevsume)** — 由 Jev 驱动的 ATS 友好简历评审。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · unownone · `TS` · 调用点 [`packages/jev/http.ts`](https://github.com/unownone/jevsume/blob/HEAD/packages/jev/http.ts)，2026-09-22 阅读 · ⚠ `无许可证`</sub>

- **[smoking-extraction-benchmark](https://github.com/vclic/smoking-extraction-benchmark)** — 合成的吸烟史抽取基准：对比 Jev 与 OpenAI 结构化输出。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`基准测试` · vclic · `Py` · 调用点 [`smoking_eval/providers.py`](https://github.com/vclic/smoking-extraction-benchmark/blob/HEAD/smoking_eval/providers.py)，2026-09-22 阅读 · ⚠ `仅一次提交` `无许可证`</sub>

- **[typesafe-ai-jev-example](https://github.com/ItBayMax/typesafe-ai-jev-example)** — Jev 的动手演示：六个可运行示例与四则实战笔记。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · itbaymax · `Py` · 调用点 [`lib/typesafe_client.py`](https://github.com/ItBayMax/typesafe-ai-jev-example/blob/HEAD/lib/typesafe_client.py)，2026-09-22 阅读 · ⚠ `仅一次提交`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
