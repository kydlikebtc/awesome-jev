# 结构化抽取

<sub>[awesome-jev](../../README.zh-CN.md) · [English](data-extraction.md)</sub>

_从杂乱文本中取出类型化字段 —— 靠在候选中选择，而不是生成。_

这个决策的全部已收录例子 —— 共 16 条，官方优先，其次是含代码的，再按 star 排序。同样这些行及其警示也在[索引](../../README.zh-CN.md#结构化抽取)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=data-extraction&lang=zh)还能按语言、原语和形态进一步筛选。

- **[Cookbook: Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook)** ⭐ — 抽取绝对与相对日期：先问文档里点明了哪些部分，再在代码里做解析与校验，并按置信度决定是否送审。
  <sub>`官方文档` · `Py`</sub>

- **[Cookbook: Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook)** ⭐ — 先用正则找出候选的邮箱、电话、金额，再让模型挑出被问到的那一段，于是代码拿到的是逐字原值。
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐ — 用两次请求把丢了格式的纯文本还原成 Markdown：一次把硬换行的段落重新接起来，一次给每个块分类。
  <sub>`官方文档` · `Py`</sub>

- **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐ — 「小模型 → 校验 → 推理模型」的两段级联，用一小部分成本拿到接近大推理模型的质量。
  <sub>`官方文档` · `Py`</sub>

- **[smart-paste](https://github.com/nomanjack/smart-paste)** — 根据粘贴的文本自动填写表单：把表单标题、字段标签和你的文字交给 TypeSafe，插入匹配到的值，提交前由你检查。 <sub>(机翻)</sub>
  <sub>`插件` · ★38 · nomanjack · `JS`</sub>

- **[jev-reviewer](https://github.com/choxos/jev-reviewer)** — 系统综述的数据抽取：让 Jev 从论文及其补充材料里按抽取表取值，并附原文引用。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★33 · choxos · `JS`</sub>

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)** — 开源的 macOS computer use 与原生 GUI 自动化，运行在 Apple 芯片上。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★21 · jcpsimmons · `JS`</sub>

- **[jevfill](https://github.com/imohitmayank/jevfill)** — 一个 Chrome 扩展：用 Jev 根据零散的文字笔记自动填写网页表单。把个人信息以纯文本粘贴一次即可，无需结构化档案，随时按需填表。 <sub>(机翻)</sub>
  <sub>`插件` · ★18 · imohitmayank · `TS`</sub>

- **[jeveryword](https://github.com/jkrup/jeveryword)** — 用 Jev 做文本抽取：字段抽取、PII 检测与逐字引文。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★4 · jkrup · `JS`</sub>

- **[jev-mcp-dispatcher](https://github.com/abhishekashokvkumar/jev-mcp-dispatcher)** — 完全由 Jev 驱动的自然语言 MCP 工具分发器，不用通用 LLM。 <sub>(机翻)</sub>
  <sub>`插件` · ★3 · abhishekashokvkumar · `Py` · ⚠ `无许可证`</sub>

- **[jevsume](https://github.com/unownone/jevsume)** — 由 Jev 驱动的 ATS 友好简历评审。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★3 · unownone · `TS` · ⚠ `无许可证`</sub>

- **[jev-information-extraction](https://github.com/abhishekmamdapure/jev-information-extraction)** — 解析 PDF 并抽取相关信息。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · abhishekmamdapure · `Py` · ⚠ `无许可证`</sub>

- **[typesafe-ai-jev-example](https://github.com/ItBayMax/typesafe-ai-jev-example)** — Jev 的动手演示：六个可运行示例与四则实战笔记。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★2 · itbaymax · `Py`</sub>

- **[ask-jev](https://github.com/logicrw/ask-jev)** — 极快、失败即放行的建议式决策，以及面向 AI 编码智能体和 CLI 管道的逐字抽取式阅读视图。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★1 · logicrw · `Py`</sub>

- **[jev-data-questions](https://github.com/narulaskaran/jev-data-questions)** — 带上数据集，看到合适的图表：界面检查 CSV 的结构并提出洞察，由 Jev 填入具体数值。 <sub>(机翻)</sub>
  <sub>`开源项目` · ★0 · narulaskaran · `TS` · ⚠ `无许可证`</sub>

- **[smoking-extraction-benchmark](https://github.com/vclic/smoking-extraction-benchmark)** — 合成的吸烟史抽取基准：对比 Jev 与 OpenAI 结构化输出。 <sub>(机翻)</sub>
  <sub>`基准测试` · ★0 · vclic · `Py` · ⚠ `无许可证`</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件 —— 两者不一致时 CI 会失败。</sub>
