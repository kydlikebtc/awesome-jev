# Practice reviews · 实践综述

<sub>[awesome-jev](../../README.md) · [design notes for every pattern](../patterns.md)</sub>

[docs/patterns.md](../patterns.md) says what each decision is for and when not to use a decision model, from the vendor's guidance. A practice review says how the projects catalogued here actually do it: how they phrase the questions, which primitive they pick, which thresholds their files compare answers with, what their authors measured, and a few call sites worth reading in full.

[docs/patterns.md](../patterns.md) 讲每种决策的用途，以及什么时候不该用决策模型，依据的是厂商的指南。实践综述讲的是本目录收录的项目实际怎么做：问题怎么写、选哪个原语、代码拿答案和哪些阈值比较、作者测了什么，再推荐几个值得完整读一遍的调用点。

**Written by a model.** Each review's prose was written by a model from this catalogue's records and its own reading of the recommended files on the date the page gives. No person has reviewed a page until it says so. Every count, table and list in a page is generated from `catalog.json` by `scripts/build_practice.py`, so those stay current; the prose describes the catalogue as it stood that day. · **由模型撰写。** 每篇的正文由模型根据本目录的记录和它在页面所注日期对推荐文件的阅读写成，在页面注明之前没有人审过。页面里的计数、表格和列表都由 `scripts/build_practice.py` 从 `catalog.json` 生成，会随目录更新；正文描述的是撰写当天的情况。

<!-- pages:start -->
- [Safety gating · 安全闸门](safety-gating.md): Decide whether an action is safe to run. Defence in depth, never a security boundary. · 在执行前判断一个动作是否安全。属纵深防御，绝不是安全边界。
- [Tool selection · 工具选择](tool-selection.md): Which tool or action the agent should call next. · 智能体下一步该调用哪个工具或动作。
- [Content scoring · 内容评分](content-scoring.md): Score quality, risk or relevance on an ordered scale. · 在有序量表上给质量、风险或相关性打分。
<!-- pages:end -->

These three came first because, apart from `overview`, they are the patterns with the most rows whose cited file a person has read. The plan is one review per pattern. · 先写这三篇，是因为除 `overview` 外，它们是有人读过所引文件的行最多的模式。计划是每个模式一篇。
