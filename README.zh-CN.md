<!--
  本文件由 catalog.json 生成。请修改目录数据后运行 `python3 scripts/build_readme.py`。
-->

<a name="top"></a>
<a name="awesome-jev"></a>
<a name="-awesome-jev"></a>

<a href="https://kydlikebtc.github.io/awesome-jev/?lang=zh">
<picture>
  <source media="(min-width: 768px) and (prefers-color-scheme: light)" srcset="docs/assets/readme-cover-zh-light.svg">
  <source media="(max-width: 767px) and (prefers-color-scheme: light)" srcset="docs/assets/readme-cover-zh-light-mobile.svg">
  <source media="(max-width: 767px)" srcset="docs/assets/readme-cover-zh-dark-mobile.svg">
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-cover-zh-dark.svg">
  <img src="docs/assets/readme-cover-zh-light.svg" alt="awesome-jev — Jev 决策图谱：1,310 条公开资源、1,261 条带日期的 HTTP 2xx 链接记录、1,139 条调用点引用记录。数字来自保存的记录，不代表当前链接可用或运行与性能测试通过。" width="100%">
</picture>
</a>

<p align="center">
<a href="https://kydlikebtc.github.io/awesome-jev/?lang=zh"><kbd>&nbsp;<b>浏览资源目录&nbsp;↗</b>&nbsp;</kbd></a>
<a href="https://kydlikebtc.github.io/awesome-jev/?collection=first-call&amp;lang=zh"><kbd>&nbsp;第一次调用&nbsp;</kbd></a>
<a href="https://kydlikebtc.github.io/awesome-jev/?collection=build&amp;lang=zh"><kbd>&nbsp;改造现有项目&nbsp;</kbd></a>
<a href="https://kydlikebtc.github.io/awesome-jev/?collection=measured&amp;lang=zh"><kbd>&nbsp;独立测量报告&nbsp;</kbd></a>
<a href="README.md"><kbd>&nbsp;English&nbsp;</kbd></a>
</p>

<p align="center"><sub>数字统计已保存的链接与证据记录，不代表当前 CI 通过数或运行测试结果。 <a href="#哪些经过核实哪些没有">统计口径</a></sub></p>

<details>
<summary><b>阅读导航 · 完整目录</b></summary>

[决策模式](docs/patterns.zh-CN.md) · [兼容性](docs/compatibility.md) · [核查指南](docs/vetting.md)

- 01 [这是什么](#这是什么)
- 02 [Jev 返回什么](#jev-返回什么)
- 03 [从这里开始](#从这里开始)
- 04 [覆盖度](#覆盖度)
- 05 [实测，而非宣称](#实测而非宣称)
- 06 [按决策模式](#按决策模式)
- 07 [按资源形态](#按资源形态)
- 08 [本仓库还有什么](#本仓库还有什么)
- 09 [哪些经过核实，哪些没有](#哪些经过核实哪些没有)
- 10 [机器可读数据](#机器可读数据)
- 11 [参与贡献与许可](#参与贡献与许可)

</details>

---

## 这是什么

- **Jev** 是 TypeSafe AI 的决策模型。它不生成文本 —— 你给它状态和类型化问题，它返回带校准置信度的类型化答案，快且便宜到可以放进智能体的内层循环。
- **本仓库**收集它的公开使用例子，按所做的**决策**组织。你这周读的那篇资料是一次性的，决策模式不是。
- **如何判断可信度：**每一行都写明来源；有依据时记录调用点、原语声明和注意事项，方便你查看读过什么，以及哪些部分仍未实测。

> [!NOTE]
> 不是产品本身，不是 SDK，与 TypeSafe AI 无隶属关系，也不构成推荐。收录是一份来源记录，不代表运行验证或性能背书。详见[哪些经过核实](#哪些经过核实哪些没有)。

## Jev 返回什么

三个核心原语：Choice、Score 和 Noul。下面的模式使用它们；Noul 返回概率，没有单独的 confidence 字段。Jev 1.14 还新增了实验性 [Box](https://docs.typesafe.ai/primitives/box)：每个问题返回一个边界框和置信度，没有「未找到」答案。Box 需要图像，并须按下文显式启用图像功能。 <sub>(机翻)</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/primitives-zh-dark.svg">
  <img src="docs/assets/primitives-zh-light.svg" alt="三个面板，分别说明 choice、score、noul 三个原语各自返回什么" width="660">
</picture>

每个原语下方有两个互不相加的数：先是 `question_types` 记录了有人读过代码、确认调用该原语的行数；再是只有文本信号的行数 —— 每周刷新在该行所引的那一个文件中找到了它的请求或回答结构（`primitives_seen`），这并不表明代码调用了它。见[哪些经过核实](#哪些经过核实哪些没有)。 <sub>(机翻)</sub>

默认输入为文本或结构化 JSON。原生 API 的 Jev 1.13 和 1.14 也支持实验性 [PNG/JPEG 图像](https://docs.typesafe.ai/images)，须发送 `TypeSafe-Danger-Zone-Images: true`；不支持音频和视频。默认每次请求 **64k** token，其中 state 加最长问题最多 **32k**。实验性请求头 `TypeSafe-Danger-Zone-Long-Context: true` 将两项限制均提高到 **262k**，但速度和准确率会降低（见[模型文档](https://docs.typesafe.ai/models)）。输出 token 免费。截至 2026-10-15，原生 `jev-preview` 指向 `jev-1.14.0`，`jev-latest` 仍指向 `jev-1.13.0`；两个固定版本 ID 均可用。[10 月 14 日公告](https://typesafe.ai/blog/jev-1-14)称 latest 约一周后切换，未给出确切切换日期。权重未公开，因此无法本地运行。跨平台差异全表见 [`docs/compatibility.md`](docs/compatibility.md)。 <sub>(机翻)</sub>

某个决策该用哪个原语？下图把 TypeSafe 官方的指引排成一张判断清单：自上而下，遇到第一个「是」即停。顺序与措辞出自本仓库；每一步都注明所依据的页面，列在图下。这是厂商附有来源的设计指引，不是对本目录任何条目的推荐。 <sub>(机翻)</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/primitive-picker-zh-dark.svg">
  <img src="docs/assets/primitive-picker-zh-light.svg" alt="选哪个原语？一份依据 TypeSafe 官方文档整理的判断顺序。每个「是」依次通向：生成式模型，不用 Jev；用代码，不用 Jev；每件事各问一个问题；每个条目一个 noul；score；noul；choice。全部为「否」时：还不是一个即时判断。" width="720">
</picture>

每个原语旁是归入所列模式的行数，计法同上图：人读确认，或仅文本信号。这些步骤存于 [`picker.json`](picker.json)，网站的原语页也读取它。来源（编号同图中）：[1] [docs.typesafe.ai/model-jaggedness/jev-1.13#generation](https://docs.typesafe.ai/model-jaggedness/jev-1.13#generation) · [2] [docs.typesafe.ai/concepts/how-to-build-with-system-one#use-code-when-you-can](https://docs.typesafe.ai/concepts/how-to-build-with-system-one#use-code-when-you-can) · [3] [docs.typesafe.ai/primitives#split-a-complex-judgment-into-several-questions](https://docs.typesafe.ai/primitives#split-a-complex-judgment-into-several-questions) · [4] [docs.typesafe.ai/primitives/noul#good-practice-ask-more-than-one-question-per-call](https://docs.typesafe.ai/primitives/noul#good-practice-ask-more-than-one-question-per-call) · [5] [docs.typesafe.ai/model-jaggedness/jev-1.13#common-sense-structural-invariants](https://docs.typesafe.ai/model-jaggedness/jev-1.13#common-sense-structural-invariants) · [6] [docs.typesafe.ai/primitives#choose-a-question-type](https://docs.typesafe.ai/primitives#choose-a-question-type) · [7] [docs.typesafe.ai/primitives/score#writing-good-levels](https://docs.typesafe.ai/primitives/score#writing-good-levels) · [8] [docs.typesafe.ai/primitives/noul#writing-a-noul-question](https://docs.typesafe.ai/primitives/noul#writing-a-noul-question) · [9] [docs.typesafe.ai/primitives#ask-for-one-snap-judgment-per-question](https://docs.typesafe.ai/primitives#ask-for-one-snap-judgment-per-question)。 <sub>(机翻)</sub>

## 从这里开始

六条，按阅读顺序。手工挑选 —— 因为「star 最多」和「该先读哪个」不是一回事。

1. **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)**

   官方第一课：一条工单，一次请求里同时问一个 Choice、一个 Score 和一个 Noul，给了 Python / JS / cURL 三种写法。

2. **[Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)**

   该页明确针对 Jev 1.13，不能据此判断哪些局限仍存在于 Jev 1.14。它解释了为什么对选项做一个 Choice，与每个选项各问一个 Noul，回答的是不同问题。

3. **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)**

   按官方 API 参考编写并逐字段对照核实，但未针对线上 API 实际执行过。

4. **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)**

   每次工具调用恰好两个 noul：知道这次调用发生过是否还有意义、以及是否还需要完整原文输出。尽管它自己的描述里用了「打分」，实际并未使用 score 原语。

5. **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**

   找到的最好的结构化教程。它明确指出类型化输出不保证决策正确、列出了官方记录的弱项，并且对自己给出的成本示例做了限定而不是拿来营销。

6. **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)**

   本目录可信度最高的一条。召回率低于他们现有的摘要器，在相同上下文预算下与「按时间倒序」打平。成本确实低得多。在一个被热炒的模型上公开负面结果，非常少见。

## 覆盖度

全部决策模式，按本目录的收录数量排列长度。图表下方的场景索引可跳转到对应章节。数字为 0 的是待补的研究缺口，不是渲染 bug。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/coverage-zh-dark.svg">
  <img src="docs/assets/coverage-zh-light.svg" alt="十八个决策模式各有多少个目录条目的横向条形图" width="100%">
</picture>

全部 18 个模式均已收录条目。覆盖不代表已运行验证或各模式成熟度相同。 详见 [`docs/status.md`](docs/status.md)。

<a name="pattern-index"></a>

**场景索引 · 点击跳转到条目**

| 场景 | 场景 |
| :--- | :--- |
| [工具选择](#工具选择) · **241** | [意图路由](#意图路由) · **42** |
| [上下文压缩](#上下文压缩) · **41** | [安全闸门](#安全闸门) · **146** |
| [输出校验](#输出校验) · **141** | [重试控制](#重试控制) · **8** |
| [人工升级](#人工升级) · **74** | [模型路由](#模型路由) · **53** |
| [并行扇出](#并行扇出) · **36** | [检索与排序](#检索与排序) · **81** |
| [结构化抽取](#结构化抽取) · **19** | [分类](#分类) · **134** |
| [机器学习特征抽取](#机器学习特征抽取) · **9** | [文档分拣](#文档分拣) · **22** |
| [工单分拣](#工单分拣) · **9** | [内容评分](#内容评分) · **171** |
| [实时推荐](#实时推荐) · **2** | [总览](#总览) · **492** |

## 实测，而非宣称

本目录收录的独立测量报告，包括有助于理解适用边界的**负面结果**。这些是原作者的测量，本仓库没有独立复现。比较结果前，请分别查看数据集、测试方法和模型版本。

*作者结论*是基准测试作者本人对 Jev 在其所测任务上给出的结论方向（`measurement.direction`：有利、好坏参半、不利或无定论），按作者的报告索引：属作者自述，未经本仓库复现；作者没有用文字说明结论的则不标。[docs/benchmarks.zh-CN.md](docs/benchmarks.zh-CN.md) 把每条基准测试的测量字段并列展示。 <sub>(机翻)</sub>

### 负面结果优先

作者本人针对这一用途测量过 Jev 并得出不采用结论的行：基准测试的测量结论为*不利*，或其他行带有*实测后未采用*标记。作者自述，未经本仓库复现。请先读它们，再看正面例子；[站点也列出了它们](https://kydlikebtc.github.io/awesome-jev/?neg=1&lang=zh)。 <sub>(机翻)</sub>

- **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)**<br>
  把 Jev 压缩方案移植过来，与自家在用的摘要器对比实测，最后公开结论：不采用。<br>
  <sub>`基准测试` · ★100k+ · `Py` · `noul` · [调用点](https://github.com/NousResearch/hermes-agent/blob/HEAD/evals/compaction/jev_arm.py)，2026-09-22 阅读 · 作者结论：不利（作者自述，未经本仓库复现）</sub>

  > 本目录可信度最高的一条。召回率低于他们现有的摘要器，在相同上下文预算下与「按时间倒序」打平。成本确实低得多。在一个被热炒的模型上公开负面结果，非常少见。

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)**<br>
  用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。<br>
  <sub>`基准测试` · ★10k+ · `TS` · `choice` · [调用点](https://github.com/koala73/worldmonitor/blob/HEAD/shared/jev-classify.js)，2026-09-22 阅读 · 作者结论：不利（作者自述，未经本仓库复现）</sub>

  **注意:** `仅影子运行`

  > 接进去了但故意不生效：按他们自己的说法，Jev 返回的任何东西都不会进入标签、缓存行或告警。带黄金测试集。想在不拿生产环境下注的前提下试新模型，这是值得照抄的做法。

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br>
  九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。<br>
  <sub>`插件` · ★1k+ · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/kerpopule/hermes-jev-skills/blob/HEAD/jevkit/client.py)，2026-09-22 阅读</sub>

  **注意:** `实测后未采用`

  > 值得一提的是它公开了一个被放弃的用法：用 Jev 做交接摘要的召回率，反而不如原始对话记录。

- **[no-mistakes: Jev review pre-brief, measured and retired](https://github.com/kunchenguid/no-mistakes/pull/1165)**<br>
  为代码审查预选上下文：每个候选文件问一个 Score —— 测了两次后被移除：计费输入明显增加、耗时几乎没有收益；离线回放还表明，候选列表根本够不到审查发现实际所在的位置。<br>
  <sub>`基准测试` · ★1k+ · `Go` · `score` · 作者结论：不利（作者自述，未经本仓库复现）</sub>

  > 已在 PR #1165（2026-09-22）中移除。他们的离线测量发现：候选生成器从构造上就排除了被改动的文件，而几乎所有审查发现都落在被改动的文件上；按文件附带摘录反而让列表更不精确、token 成本更高。代码已不在默认分支上，所以这一行引用的是移除它的那次改动。

- **[jev-skill-router](https://github.com/shimo4228/jev-skill-router)**<br>
  Claude Code 钩子：每条提示都问 Jev 哪个已安装的技能合适。先用一个 choice 给全部技能排序，同时用三个 noul 判断提示本身；再用 choice 和逐个技能的 noul 评判前三名，低于 0.30 就不推荐。影子模式只记日志；作者用了一周，539 次推荐中只有 28 次随后调用了该技能。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★10+ · shimo4228 · `Py` · [调用点](https://github.com/shimo4228/jev-skill-router/blob/HEAD/scripts/jev_client.py)，2026-09-22 阅读</sub>

  **注意:** `实测后未采用`

  > 作者于 2026-09-21 运行后得出结论：作为路由器，它不太可能帮到本来就能看到全部技能描述的强模型。其 README 记录：0.2.0 版上 6 条脚本化请求全部处理得当，0.1.0 版在一次真实会话的 6 条提示中有 3 条出错，作者称这只是个例，不是比率。它一直停留在影子模式。https://dev.to/shimo4228/i-added-jevs-skill-router-to-claude-code-and-turned-back-just-before-rewriting-the-skill-listing-34in 本条中文备注由模型撰写。

### 其他独立测量报告

- **[An early-access test of TypeSafe's Jev: calibrated judgments for half a cent](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)**<br>
  找到的最好的独立实测：固定单一模型版本、24 份挪威语文档，开篇就展示了一个模型答错、但同时正确报出低置信度的案例。<br>
  <sub>`基准测试` · Lindfors</sub>

  > 方法论交代干净，并诚实限定为「单日快照」。开篇就摆失败案例，这才让它成为真正的校准检验，而不是一篇软文。

- **[Testing TypeSafe Jev, Mistral and Gemini for local event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation)**<br>
  找到的唯一三方横评，每个模型分别调过提示词，且明确把范围限定在单一任务上、不做通用排名。<br>
  <sub>`基准测试` · Near Here</sub>

  > 自我限定很规范：这是用例研究，不是模型排行榜。这种克制比数字本身更少见。

- **[hippo-memory](https://github.com/kitfunso/hippo-memory)**<br>
  受生物启发的智能体记忆：衰减、检索强化与巩固。零运行时依赖，基于 SQLite。 <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★100+ · kitfunso · `TS` · [调用点](https://github.com/kitfunso/hippo-memory/blob/HEAD/src/rerankers/jev.ts)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jev-arena](https://github.com/NanmiCoder/jev-arena)**<br>
  Jev 模型介绍与实测：通过 Choice / Score / Noul 将自然语言转为带类型的判断与概率，用于分类、评分和路由；支持与 DeepSeek 等模型对比评论打标、速度与结果，含 CSV/Excel 导入、原速回放与离线报告。<br>
  <sub>`基准测试` · ★100+ · nanmicoder · `JS` · [调用点](https://github.com/NanmiCoder/jev-arena/blob/HEAD/src/backends/jev.mjs)，2026-09-24 阅读</sub>

- **[jevbench](https://github.com/fstandhartinger/jevbench)**<br>
  Benchmark Heaven 维护的基准，评测 Jev 及兼容 Jev 的决策模型：通过 /v1/systemone 适配器把 noul、choice 和 score 任务发给各个系统，按准确率、校准、延迟和成本打分。当前版本 v1.6.1（2026-10-06）；部分输入是封存的，因此无法完全独立重跑。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★100+ · fstandhartinger · `Py` · [调用点](https://github.com/fstandhartinger/jevbench/blob/HEAD/jevbench/adapters/typesafe.py)，2026-09-22 阅读</sub>

已显示 **10 / 77** 条：先是负面结果，再是精选路径[独立测量报告](https://kydlikebtc.github.io/awesome-jev/?collection=measured&lang=zh)选出的条目，按该路径的顺序，再按列表顺序补上其余条目中靠前的几条 · [在单独页面查看全部 77 条及全部备注 →](docs/measured.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?indep=1&lang=zh) <sub>(机翻)</sub>

## 按决策模式

主索引。每个标题是智能体必须做的一个决策；下面的行是做这个决策的例子。警示以短标记呈现 —— 每行的完整备注在 [`catalog.json`](catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/)里。

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）；注明“模型阅读”的，则是模型阅读该文件的日期（`evidence.model_read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

### 工具选择

_智能体下一步该调用哪个工具或动作。_

- **[Cookbook: Function calling](https://docs.typesafe.ai/cookbooks/function_calling)** ⭐<br>
  把自然语言的交易请求映射到普通的类型化函数：函数名和有限取值的参数各自变成一个带置信度的问题。<br>
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion)** ⭐<br>
  为智能体的一轮对话从 182 个技能里最多挑一个：第一次请求给所有技能排序并顺便问「这轮到底需不需要技能」，第二次细读前三名。<br>
  <sub>`官方文档` · `Py` · `choice` · `noul`</sub>

- **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐<br>
  一个可运行的智能家居助手示例，用类型化决策来解析用户请求。<br>
  <sub>`官方文档` · `Py`</sub>

- **[ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)**<br>
  教学用的模拟交易与回测应用：每个“投资者人格”智能体把一份财务快照变成看涨、看跌或中性信号。选 TypeSafe 作为模型提供方时，每个智能体发一次 Jev 请求：用 choice 选方向，再用五级 score 分别评估看涨和看跌理由的强度，换算成与 LLM 智能体相同的 JSON。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`平台集成` · ★10k+ · virattt · `Py` · [调用点](https://github.com/virattt/ai-hedge-fund/blob/HEAD/hedge_fund/llm/client.py)，2026-09-24 阅读</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)**<br>
  三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。<br>
  <sub>`插件` · ★10k+ · `Py` · `TS` · `choice` · `score` · `noul` · [调用点](https://github.com/davila7/claude-code-templates/blob/HEAD/scripts/jev-spike.mjs)，2026-09-22 阅读</sub>

- **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)**<br>
  把工具目录编译成问题，再从答案还原出 tool call，并为「弃权」和「需确认」两种情况定义了专门的错误类型。<br>
  <sub>`开源项目` · ★10k+ · `Py` · `choice` · [调用点](https://github.com/ComposioHQ/composio/blob/HEAD/python/providers/typesafe/composio_typesafe/provider.py)，2026-09-22 阅读</sub>

- **[Cua driver: jev-use example](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use)**<br>
  Python 与 TypeScript 双实现的 computer-use 动作选择：Jev 从不可变候选集里挑下一个浏览器动作，保留 reobserve 和 abstain 两个特殊选项。<br>
  <sub>`开源项目` · ★10k+ · `Py` · `TS` · `choice` · [调用点](https://github.com/trycua/cua/blob/HEAD/libs/cua-driver/examples/jev-use/python/jev_adapter.py)，2026-09-22 阅读</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)**<br>
  两段式 MCP 工具检索：先用一个宽 Choice 对整个目录粗排，再给候选短名单配完整描述，每个候选各配一个 Noul 判断它到底是否胜任。<br>
  <sub>`开源项目` · ★10k+ · `Py` · `choice` · `noul` · [调用点](https://github.com/PrefectHQ/fastmcp/blob/HEAD/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)，2026-09-22 阅读</sub>

- **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)**<br>
  Browser Use 做的高速浏览器 Agent。Jev 每一步只判断「做什么、点哪个元素」，要打字才叫小模型。<br>
  <sub>`开源项目` · ★10k+ · Browser Use · `Py` · `choice` · [调用点](https://github.com/browser-use/jev-ultrafast/blob/HEAD/jev_ultrafast/model.py)，2026-09-22 阅读</sub>

  **注意:** `厂商自报数据`

- **[json-render](https://github.com/vercel-labs/json-render)**<br>
  Vercel Labs 的生成式 UI 框架。实验里 Jev 不逐 token 写 JSON，只负责选组件、属性和布局。<br>
  <sub>`开源项目` · ★10k+ · Vercel Labs · `TS` · `choice` · [调用点](https://github.com/vercel-labs/json-render/blob/HEAD/apps/web/lib/jev/compose.ts)，2026-09-22 阅读</sub>

已显示 **10 / 241** 条 · [在单独页面查看全部 241 条 →](docs/by-pattern/tool-selection.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=tool-selection&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 意图路由

_判断用户意图，把请求分流到正确的分支。_

- **[Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home)** ⭐<br>
  一个可运行的智能家居助手示例，用类型化决策来解析用户请求。<br>
  <sub>`官方文档` · `Py`</sub>

- **[Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)** ⭐<br>
  把 confidence 当作第二个维度：答案告诉你「是什么」，置信度告诉你「该不该照它执行」。<br>
  <sub>`官方文档` · `Py`</sub>

- **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐<br>
  对进来的请求做分类，路由到足够用的最便宜那个处理方：确定性代码、专用 LLM、或人。<br>
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)**<br>
  七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。<br>
  <sub>`开源项目` · ★100k+ · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/Significant-Gravitas/AutoGPT/blob/HEAD/autogpt_platform/backend/backend/blocks/typesafe/_client.py)，2026-09-22 阅读</sub>

- **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)**<br>
  把下游任务 id 变成 choice 的选项集，并用最小置信度闸门把不确定的运行转给人处理。<br>
  <sub>`平台集成` · ★10k+ · `Py` · `choice`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)**<br>
  七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。<br>
  <sub>`开源项目` · ★10k+ · `TS` · `choice` · `noul` · [调用点](https://github.com/elie222/inbox-zero/blob/HEAD/apps/web/utils/decision-model/typesafe.ts)，2026-09-22 阅读</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br>
  一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。<br>
  <sub>`教程` · ★1k+ · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/daveebbelaar/ai-cookbook/blob/HEAD/models/jev/06-criteria.py)，2026-09-22 阅读</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)**<br>
  一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。<br>
  <sub>`开源项目` · ★1k+ · `Java` · `choice` · `score` · `noul` · [调用点](https://github.com/jev-chat/jev-chat-jarvis/blob/HEAD/cn/app/src/main/java/com/jev/probe/jev/JevQuestions.kt)，2026-09-22 阅读</sub>

- **[Real Python: hello-jev](https://github.com/realpython/materials/tree/master/hello-jev)**<br>
  带对照组的教学示例：同一个问询台任务，一份是只认 Y/N 的纯 Python 写法，旁边是一个能读出意图的 Noul。<br>
  <sub>`教程` · ★1k+ · Real Python · `Py` · `noul` · [调用点](https://github.com/realpython/materials/blob/HEAD/hello-jev/jev_noul.py)，2026-09-22 阅读</sub>

- **[shapeshift](https://github.com/anishfn/shapeshift)**<br>
  一个随输入变成合适卡片的文本框（日程、清单、计时器、分账等）。配置 TypeSafe 密钥后，一次 Jev 调用回答 14 个问题：用 choice 选卡片类型，另有若干 choice、noul 和 score，例如紧急程度、是否视频通话；日期和金额由代码解析。离线时由关键词规则作答。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★1k+ · anishfn · `TS` · [调用点](https://github.com/anishfn/shapeshift/blob/HEAD/src/lib/jev/client.ts)，2026-09-24 阅读</sub>

已显示 **10 / 42** 条 · [在单独页面查看全部 42 条 →](docs/by-pattern/intent-routing.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=intent-routing&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 上下文压缩

_判断哪些工具调用和结果仍然相关，从而丢弃过期上下文。_

- **[Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent)**<br>
  把 Jev 压缩方案移植过来，与自家在用的摘要器对比实测，最后公开结论：不采用。<br>
  <sub>`基准测试` · ★100k+ · `Py` · `noul` · [调用点](https://github.com/NousResearch/hermes-agent/blob/HEAD/evals/compaction/jev_arm.py)，2026-09-22 阅读 · 作者结论：不利（作者自述，未经本仓库复现）</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)**<br>
  把记忆召回的整套检索栈替换掉 —— 不用 embedding、不用 BM25、不用重排器 —— 改为对每条候选记忆批量问一个 Noul。<br>
  <sub>`开源项目` · ★10k+ · `Rs` · `noul` · [调用点](https://github.com/1jehuang/jcode/blob/HEAD/crates/jcode-base/src/jev.rs)，2026-09-22 阅读</sub>

- **[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)**<br>
  一个 Claude Code 插件，用逐条决策取代压缩式摘要：过期的工具调用被丢弃或截断，保留下来的全部逐字不变。<br>
  <sub>`插件` · ★1k+ · tamaratran · `TS` · `noul` · [调用点](https://github.com/tamaratran/fast-jev-compaction/blob/HEAD/src/request.ts)，2026-09-22 阅读</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br>
  九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。<br>
  <sub>`插件` · ★1k+ · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/kerpopule/hermes-jev-skills/blob/HEAD/jevkit/client.py)，2026-09-22 阅读</sub>

  **注意:** `实测后未采用`

- **[jevgrep (dzhng)](https://github.com/dzhng/jevgrep)**<br>
  一个命令行工具和 Agent 技能，用“这段代码做什么”来找代码：`jg "遥测事件是如何记录的？" ./repo` 让 Jev 在目录、文件和声明层面判断相关性，返回相关文件、阅读线索和原文摘录。作者报告在 10 个 SWE-bench 任务上同样解决 8 个，成本约低 30%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★1k+ · dzhng · `TS` · `noul` · [调用点](https://github.com/dzhng/jevgrep/blob/HEAD/packages/core/test-node/provider-protocol.mjs)，2026-10-24 模型阅读</sub>

  **注意:** `厂商自报数据`

- **[compact-adviser](https://github.com/kunchenguid/compact-adviser)**<br>
  只回答一个问题的插件：现在该不该 /compact。一次 Jev 请求问两个 choice（最近一段工作是否已完成；是亲手干活还是在协调他人），由代码合成一个分数，随着上下文变满，门槛从 0.90 放宽到 0.50。它给出提示；在 Pi 和 Claude Code 上若你开启，也可以自动压缩。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · kunchenguid · `TS` · [调用点](https://github.com/kunchenguid/compact-adviser/blob/HEAD/packages/claude-mod/lib/judge.ts)，2026-09-22 阅读</sub>

- **[jev-pruner](https://github.com/tamaratran/jev-pruner)**<br>
  在模型看到之前先修剪冗长的 shell 输出，每个片段问一个 Noul。<br>
  <sub>`插件` · ★100+ · tamaratran · `TS` · `noul` · [调用点](https://github.com/tamaratran/jev-pruner/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[mu](https://github.com/qybaihe/mu)**<br>
  基于 pi 的编程 Agent（命令行和桌面端），在 38 个决策点上问 Jev：工具输出的哪些片段进上下文、哪些过期的工具结果可以丢掉、被规则拦下的命令是不是用户要的、抓取的网页和 MCP 输出里有没有注入的指令。 <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · qybaihe · `TS` · `choice` · `noul` · `score` · [调用点](https://github.com/qybaihe/mu/blob/HEAD/packages/kyrn-judge/src/providers/typesafe.ts)</sub>

  **注意:** `作者自荐`

- **[Quicksilver](https://github.com/UditAkhourii/quicksilver)**<br>
  一个 Claude Code 技能，把“是否相关”的判断交给 Jev：对每个文件、每行日志或每张工单问一个 noul（例如“这些文件里哪些处理鉴权？”），并行询问并按概率排序，于是 Claude 拿到的是带置信度的候选清单，而不必通读全部内容。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★100+ · uditakhourii · `JS` · `noul` · [调用点](https://github.com/UditAkhourii/quicksilver/blob/HEAD/skills/quicksilver/scripts/qs.mjs)，2026-10-24 模型阅读</sub>

- **[Winnow](https://github.com/GhalebDweikat/winnow)**<br>
  给 Claude Code 做上下文垃圾回收。Read / Bash / Grep 吐一大堆时，Jev 先判断哪些真和当前任务有关。<br>
  <sub>`插件` · ★100+ · `Py` · `noul` · [调用点](https://github.com/GhalebDweikat/winnow/blob/HEAD/sidecar/src/winnow/judge.py)，2026-09-22 阅读</sub>

已显示 **10 / 41** 条 · [在单独页面查看全部 41 条 →](docs/by-pattern/context-compaction.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=context-compaction&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 安全闸门

_在执行前判断一个动作是否安全。属纵深防御，绝不是安全边界。_

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐<br>
  给每条召回的段落打分，再由代码决定哪些能进入回答模型 —— 矛盾的标记保留，夹带提示注入的直接丢弃。<br>
  <sub>`官方文档` · `Py`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐<br>
  用一次请求筛查 LLM 应用的每一条进出消息，既点明风险类型、又给「照做会造成多大危害」打分。<br>
  <sub>`官方文档` · `Py` · `noul` · `score`</sub>

- **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)**<br>
  LangChain 集成的 JavaScript 对应版本，分类器与 middleware 形状一致。<br>
  <sub>`平台集成` · ★10k+ · `TS` · `choice` · `score` · `noul` · [调用点](https://github.com/langchain-ai/langchainjs/blob/HEAD/libs/providers/langchain-typesafe/src/types.ts)，2026-09-22 阅读</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)**<br>
  三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。<br>
  <sub>`插件` · ★10k+ · `Py` · `TS` · `choice` · `score` · `noul` · [调用点](https://github.com/davila7/claude-code-templates/blob/HEAD/scripts/jev-spike.mjs)，2026-09-22 阅读</sub>

- **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)**<br>
  作为审核 API 的直接替代：一次请求并行问多个 Noul，每个危害类别一个，且每条指令都带反注入前缀。<br>
  <sub>`开源项目` · ★10k+ · `Go` · `noul` · [调用点](https://github.com/Wei-Shaw/sub2api/blob/HEAD/backend/internal/pkg/typesafe/client.go)，2026-09-22 阅读</sub>

- **[agentgateway: CI-validated LLM guardrail](https://github.com/agentgateway/agentgateway)**<br>
  三个共用同一严重度量表的 Score 问题，两项以上越线即拦截请求，并且失败时默认关闭。<br>
  <sub>`开源项目` · ★1k+ · `Rs` · `score` · [调用点](https://github.com/agentgateway/agentgateway/blob/HEAD/examples/llm-guardrail-jev/guardrail.ts)，2026-09-22 阅读</sub>

- **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)**<br>
  从三个维度审查每次工具调用：风险等级、用户是否授权、以及一个显式的提示注入压力检查。<br>
  <sub>`开源项目` · ★1k+ · `TS` · `choice` · `noul` · [调用点](https://github.com/ThinkInAIXYZ/deepchat/blob/HEAD/src/shared/jevProtocol.ts)，2026-09-22 阅读</sub>

- **[atomic](https://github.com/bastani-inc/atomic)**<br>
  编程智能体运行时：工作流是带版本的 TypeScript 阶段，包含可执行检查、评审关卡和人工审批。其 AI 包从 models.dev 收录 Jev，作为 5 家提供方上的 System One 决策模型，与聊天模型分开列出；README 没有说明工作流在哪里调用它。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · bastani-inc · `TS` · [调用点](https://github.com/bastani-inc/atomic/blob/HEAD/packages/ai/src/decision-models.generated.ts)，2026-09-24 阅读</sub>

- **[grok-bot-jev](https://github.com/Bodila51/grok-bot-jev)**<br>
  Grok Bot 的路由器：在调研、浏览、重试或启动子智能体之前，先问 Jev 这个请求需要哪种动作：复用已缓存的产物、停止失败的重试、运行确定性代码、限制调研规模、允许子智能体，或请人决定。影子模式只记日志；主动模式要靠粘贴进去的技能来执行。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★100+ · bodila51 · `Py` · [调用点](https://github.com/Bodila51/grok-bot-jev/blob/HEAD/src/jev_client.py)，2026-09-22 阅读</sub>

- **[Jev-cu](https://github.com/Sac-Y/Jev-cu)**<br>
  一个 computer-use 智能体：判断该对无障碍树里哪个元素操作，并单独用一个 noul 判断这个动作是否需要用户显式确认。<br>
  <sub>`开源项目` · ★100+ · `JS` · `choice` · `noul` · [调用点](https://github.com/Sac-Y/Jev-cu/blob/HEAD/scripts/jev-decide.mjs)，2026-09-22 阅读</sub>

已显示 **10 / 146** 条 · [在单独页面查看全部 146 条 →](docs/by-pattern/safety-gating.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=safety-gating&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 输出校验

_在输出到达用户前，按评分标准检查模型产出。_

- **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐<br>
  用一个 Choice 对着原文核查引用是否错误或凭空编造，并用它的置信度把边缘情况标出来送审。<br>
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐<br>
  用一次请求筛查 LLM 应用的每一条进出消息，既点明风险类型、又给「照做会造成多大危害」打分。<br>
  <sub>`官方文档` · `Py` · `noul` · `score`</sub>

- **[latitude-llm](https://github.com/latitude-dev/latitude-llm)**<br>
  面向 AI 智能体的开源可观测性平台，在调用轨迹里标出智能体出错的地方。其中一个影子提供方问 Jev 每个标记维度一个 noul，一次调用最多 11 个；所引文件看不出这些答案是否会改变任何标记，README 也没有提到 Jev。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★1k+ · latitude-dev · `TS` · [调用点](https://github.com/latitude-dev/latitude-llm/blob/HEAD/packages/platform/ai-jev/src/jev-shadow-decision-provider.ts)，2026-09-22 阅读</sub>

- **[reticle](https://github.com/reticlehq/reticle)**<br>
  通过实际操作正在运行的应用来核实 AI 智能体说的“完成”，给出通过、失败或无法判断。其基准测试框架就采集到的证据用一次调用问 Jev：五个 noul（预期结果是否发生、采集是否干净、应用是否报错等）、一个通过／失败／未知的 choice，以及一个严重程度 score。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★1k+ · reticlehq · `TS` · [调用点](https://github.com/reticlehq/reticle/blob/HEAD/bench/harness/jev.mjs)，2026-09-24 阅读</sub>

- **[abide](https://github.com/coldteadotai/abide)**<br>
  接入 Claude Code、Codex、OpenCode 和 Pi，在每次编辑或每一轮，就 AGENTS.md 或 CLAUDE.md 中的每条规则问 Jev 一个是非题，只给它看规则和 diff；违反的规则会退回给智能体修改。在 93 个回放的会话中，Jev 标出了 39 次编辑，其中 10 次经审阅者确认。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★100+ · coldteadotai · `TS` · [调用点](https://github.com/coldteadotai/abide/blob/HEAD/packages/cli/src/lib/jev.ts)，2026-09-24 阅读</sub>

- **[atomic](https://github.com/bastani-inc/atomic)**<br>
  编程智能体运行时：工作流是带版本的 TypeScript 阶段，包含可执行检查、评审关卡和人工审批。其 AI 包从 models.dev 收录 Jev，作为 5 家提供方上的 System One 决策模型，与聊天模型分开列出；README 没有说明工作流在哪里调用它。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · bastani-inc · `TS` · [调用点](https://github.com/bastani-inc/atomic/blob/HEAD/packages/ai/src/decision-models.generated.ts)，2026-09-24 阅读</sub>

- **[Canny](https://github.com/qkal/Canny)**<br>
  防 Coding Agent 嘴硬说自己做完了。看工具输出、代码 diff 和测试结果，再判断完成声明靠不靠谱。<br>
  <sub>`开源项目` · ★100+ · `TS` · `noul` · `score` · [调用点](https://github.com/qkal/Canny/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[fastbrowse](https://github.com/agent-labs-dev/fastbrowse)**<br>
  浏览器智能体：每个页面被索引成候选控件，由 Jev 选出下一步，因此不会点击页面上没有的东西；规划和阅读由 Gemini Flash 负责，答案引用页面原文。维护者记录的 46 个任务中成功率为 99.2%，托管版 Browser Use 为 97.8%，而成本不到其十分之一。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · agent-labs-dev · `Py` · [调用点](https://github.com/agent-labs-dev/fastbrowse/blob/HEAD/src/fastbrowse/clients/typesafe.py)，2026-09-22 阅读</sub>

- **[formanator](https://github.com/timrogers/formanator)**<br>
  从命令行或 MCP 客户端提交 Forma 福利报销。使用 --category-provider jev 时，Jev 用一个 choice 从 Forma 允许的“福利加类别”组合（另加 no_match）中挑一个，只看商家和描述；置信度低于 0.5 或无匹配时，回退到配置好的 LLM。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★100+ · timrogers · `Rs` · [调用点](https://github.com/timrogers/formanator/blob/HEAD/src/typesafe.rs)，2026-09-22 阅读</sub>

- **[jev-eval-agent](https://github.com/vinilana/jev-eval-agent)**<br>
  一个把评测工作通过类型化决策来路由的智能体。<br>
  <sub>`开源项目` · ★100+ · vinilana · `TS` · [调用点](https://github.com/vinilana/jev-eval-agent/blob/HEAD/agent/lib/jev-router.ts)，2026-09-22 阅读</sub>

  **注意:** `无许可证`

已显示 **10 / 141** 条 · [在单独页面查看全部 141 条 →](docs/by-pattern/output-validation.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=output-validation&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 重试控制

_判断失败的步骤是否值得重试。_

- **[DuoMind](https://github.com/j1s4nn/duomind)**<br>
  一个 OpenAI 兼容的本地服务器，把 llama.cpp 上的小模型与 Jev 搭配：在生成之前、之中和之后共 18 个决策点（是否需要推理、是否安全、输出格式、是否该停、是否重试）引导本地模型。提示词会发送给 TypeSafe，生成过程留在本地。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10+ · j1s4nn · `Py` · `noul` · `choice` · [调用点](https://github.com/j1s4nn/duomind/blob/HEAD/src/duomind/jev_client.py)，2026-10-24 模型阅读</sub>

  **注意:** `厂商自报数据`

- **[jev-harness](https://github.com/ismaelsoilet/jev-harness)**<br>
  面向 AI 编码智能体的决策关卡，提供 CLI、MCP 服务器、CI 钩子以及 Python、TypeScript 和 Rust SDK：先用离线启发式规则，再可选地交给 Jev 判断：失败的测试日志是否需要动用 LLM、是否中止反复修改的循环、该用哪个模型档位和推理力度、某一步是否已完成。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★10+ · ismaelsoilet · `Py` · [调用点](https://github.com/ismaelsoilet/jev-harness/blob/HEAD/src/jev_harness/client.py)，2026-09-24 阅读</sub>

- **[harnessjudge](https://github.com/ndolinschi/harnessjudge)**<br>
  面向智能体开发者的网页应用：粘贴某一步的执行轨迹，由 Jev 判定为通过、重试、升级或停止。没有 TYPESAFE_API_KEY 时，本地启发式规则返回同样结构的答案，并标为演示模式。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ndolinschi · `TS` · [调用点](https://github.com/ndolinschi/harnessjudge/blob/HEAD/src/lib/jev.ts)，2026-09-22 阅读</sub>

  **注意:** `仅一次提交` · `无许可证`

- **[Jev by Example](https://github.com/ReallyArtificial/jev-by-example)**<br>
  十个可运行的 JavaScript 智能体决策，一个文件一个：新记忆与旧记忆冲突时该改还是该留、工具返回 200 是否真的完成了任务、写入超时后该重试还是该对账、上下文分块在预算内如何取舍、压缩后的交接是否丢掉了某条禁令。Jev 只回答带类型的问题，阈值和最终提案由普通代码决定。<br>
  <sub>`开源项目` · Really Artificial · `JS` · `choice` · `score` · `noul` · [调用点](https://github.com/ReallyArtificial/jev-by-example/blob/HEAD/src/client.mjs)，2026-09-22 阅读</sub>

  **注意:** `疑似 AI 生成`

- **[jev-reasoning-navigator](https://github.com/AndreuVM/praxeon)**<br>
  JEV 推理导航器：面向自主 LLM 智能体的认知监督、防止循环与反幻觉引擎。 <sub>(机翻)</sub><br>
  <sub>`开源项目` · andreuvm · `Py` · [调用点](https://github.com/AndreuVM/praxeon/blob/HEAD/praxeon/core/typesafe_client.py)，2026-09-24 阅读</sub>

  **注意:** `无许可证`

- **[jev-resilience](https://github.com/Vicente-MD/jev-resilience)**<br>
  面向 WebFlux 的 Spring Boot Starter：标注了 @SemanticCircuitBreaker 的方法会把每个响应体发给 Jev，用一个 noul 判断这个 HTTP 200 是否掩盖了错误、堆栈信息或维护通知；超过阈值（示例中为 0.85）就抛出熔断器可以计数的异常。失败即放行。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · vicente-md · `Java` · [调用点](https://github.com/Vicente-MD/jev-resilience/blob/HEAD/src/main/java/ai/jev/resilience/client/dto/JevRequest.java)，2026-09-22 阅读</sub>

  **注意:** `无许可证`

- **[jevswiftsdk](https://github.com/NSStudent/JevSwiftSDK)**<br>
  独立、非官方、零依赖的 System One API Swift SDK：choice、noul 和 score 问题都映射为 Swift 类型（比如对枚举的 choice），具名批量问题一次调用作答并逐个校验答案，支持按策略重试和取消。支持 iOS 15+、macOS 12+ 和 Linux。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`SDK` · nsstudent · `Swift` · [调用点](https://github.com/NSStudent/JevSwiftSDK/blob/HEAD/Sources/JevSwiftSDK/Configuration.swift)，2026-09-22 阅读</sub>

- **[XavierJev](https://github.com/liu-x27/XavierJev)**<br>
  Jev 形状的本地决策层：是非、选择和量表问题都从本地模型单个 token 的 logprob 读出答案；附带一个在留出命令集上测量过的 Claude Code 权限闸门。 <sub>(机翻)</sub><br>
  <sub>`Jev 替代实现` · Xinyu Liu · `TS` · `noul` · `choice` · `score` · [引用文件](https://github.com/liu-x27/XavierJev/blob/HEAD/src/gate.ts)，2026-09-25 阅读</sub>

  **注意:** `并非 Jev 本身` · `疑似 AI 生成`

已显示全部 8 条 · [单独页面](docs/by-pattern/retry-control.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=retry-control&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 人工升级

_用校准置信度决定哪些情况必须由人来看。_

- **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐<br>
  把年报分入 75 个行业组，再根据答案自身的置信度决定：报这个细分组，还是退回上一层的大类。<br>
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐<br>
  用一个 Choice 对着原文核查引用是否错误或凭空编造，并用它的置信度把边缘情况标出来送审。<br>
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐<br>
  判断两份商品目录间 450 个候选配对里哪些指的是同一个东西 —— 一个 Score 就够，它的三级正好对应三种可执行动作。<br>
  <sub>`官方文档` · `Py` · `score`</sub>

- **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐<br>
  在内容审核决策里显式加入「不确定」这个选项，并衡量标签一致率与自动处置比例之间的取舍。<br>
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Self-consistency with nouls](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook)** ⭐<br>
  把不确定的概率转人工复核，同时保留底层的 noul 数值本身，而不是压成一个标签了事。<br>
  <sub>`官方文档` · `Py` · `noul`</sub>

- **[Pattern: Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing)** ⭐<br>
  把 confidence 当作第二个维度：答案告诉你「是什么」，置信度告诉你「该不该照它执行」。<br>
  <sub>`官方文档` · `Py`</sub>

- **[Confidence](https://docs.typesafe.ai/confidence)** ⭐<br>
  Choice 和 Score 的 confidence 如何从概率推导、Noul 有何不同，以及如何针对问题与应用调节阈值。 <sub>(机翻)</sub><br>
  <sub>`官方文档`</sub>

- **[Airflow LLMBranchOperator with Jev](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html)**<br>
  把下游任务 id 变成 choice 的选项集，并用最小置信度闸门把不确定的运行转给人处理。<br>
  <sub>`平台集成` · ★10k+ · `Py` · `choice`</sub>

- **[Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe)**<br>
  把工具目录编译成问题，再从答案还原出 tool call，并为「弃权」和「需确认」两种情况定义了专门的错误类型。<br>
  <sub>`开源项目` · ★10k+ · `Py` · `choice` · [调用点](https://github.com/ComposioHQ/composio/blob/HEAD/python/providers/typesafe/composio_typesafe/provider.py)，2026-09-22 阅读</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)**<br>
  七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。<br>
  <sub>`开源项目` · ★10k+ · `TS` · `choice` · `noul` · [调用点](https://github.com/elie222/inbox-zero/blob/HEAD/apps/web/utils/decision-model/typesafe.ts)，2026-09-22 阅读</sub>

已显示 **10 / 74** 条 · [在单独页面查看全部 74 条 →](docs/by-pattern/human-escalation.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=human-escalation&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 模型路由

_选择由哪个下游模型或档位处理请求。_

- **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐<br>
  「小模型 → 校验 → 推理模型」的两段级联，用一小部分成本拿到接近大推理模型的质量。<br>
  <sub>`官方文档` · `Py`</sub>

- **[Pattern: Intent routing](https://docs.typesafe.ai/patterns/intent-routing)** ⭐<br>
  对进来的请求做分类，路由到足够用的最便宜那个处理方：确定性代码、专用 LLM、或人。<br>
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[@langchain/typesafe](https://github.com/langchain-ai/langchainjs)**<br>
  LangChain 集成的 JavaScript 对应版本，分类器与 middleware 形状一致。<br>
  <sub>`平台集成` · ★10k+ · `TS` · `choice` · `score` · `noul` · [调用点](https://github.com/langchain-ai/langchainjs/blob/HEAD/libs/providers/langchain-typesafe/src/types.ts)，2026-09-22 阅读</sub>

- **[claude-code-templates: three Jev plugins](https://github.com/davila7/claude-code-templates)**<br>
  三个可独立安装的 Claude Code 插件 —— 护栏、模型路由、技能推荐 —— 各自带 hook 和测试。<br>
  <sub>`插件` · ★10k+ · `Py` · `TS` · `choice` · `score` · `noul` · [调用点](https://github.com/davila7/claude-code-templates/blob/HEAD/scripts/jev-spike.mjs)，2026-09-22 阅读</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br>
  九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。<br>
  <sub>`插件` · ★1k+ · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/kerpopule/hermes-jev-skills/blob/HEAD/jevkit/client.py)，2026-09-22 阅读</sub>

  **注意:** `实测后未采用`

- **[Astra-Ares](https://github.com/miuuyy/Astra-Ares)**<br>
  运行一个打过补丁的 Codex CLI：Jev 读取有限的任务上下文，用两个 choice 选出 GPT-6 下一次回复的推理力度，以及这个力度持续几次回复（1、2、5 或 10）；GPT-6 改变推理力度不会破坏提示缓存。属于实验性的参考实现。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★100+ · miuuyy · `JS` · [调用点](https://github.com/miuuyy/Astra-Ares/blob/HEAD/src/jev.mjs)，2026-09-24 阅读</sub>

- **[jev-codex-router](https://github.com/0xNatoshi/jev-codex-router)**<br>
  先让 Jev 判断这一轮编程任务有多难，再决定模型档位、推理深度和速度模式。<br>
  <sub>`插件` · ★100+ · `JS` · `choice` · `score` · [调用点](https://github.com/0xNatoshi/jev-codex-router/blob/HEAD/server/jev_server.py)，2026-09-22 阅读</sub>

  **注意:** `已归档`

- **[jev-eval-agent](https://github.com/vinilana/jev-eval-agent)**<br>
  一个把评测工作通过类型化决策来路由的智能体。<br>
  <sub>`开源项目` · ★100+ · vinilana · `TS` · [调用点](https://github.com/vinilana/jev-eval-agent/blob/HEAD/agent/lib/jev-router.ts)，2026-09-22 阅读</sub>

  **注意:** `无许可证`

- **[jev-review](https://github.com/devagrawal09/jev-review)**<br>
  代码审查前先过一遍 Jev，把高风险改动挑出来，再交给更贵的大模型或人。带本地看板。<br>
  <sub>`开源项目` · ★100+ · `TS` · `choice` · `score` · `noul` · [调用点](https://github.com/devagrawal09/jev-review/blob/HEAD/src/review/codebase-judgments.ts)，2026-09-22 阅读</sub>

- **[jevrouter](https://github.com/BillionsBobby/JevRouter)**<br>
  面向模型、工具和子智能体的路由器。<br>
  <sub>`开源项目` · ★100+ · billionsbobby · `TS` · [调用点](https://github.com/BillionsBobby/JevRouter/blob/HEAD/functions/api/jev.js)，2026-09-22 阅读</sub>

已显示 **10 / 53** 条 · [在单独页面查看全部 53 条 →](docs/by-pattern/model-routing.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=model-routing&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 并行扇出

_把大量问题（包括推测性的）打包进一次请求，再由代码挑出真正用得上的答案。_

- **[Cookbook: Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions)** ⭐<br>
  对一篇长文提 13 个合规问题，证明全部打包进一次调用便宜得多、也快得多，而答案不变。<br>
  <sub>`官方文档` · `Py`</sub>

- **[Pattern: Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out)** ⭐<br>
  把大量问题（包括可能用不上的）打包进一次请求，之后再由代码决定哪些答案真的用得上。<br>
  <sub>`官方文档` · `Py`</sub>

- **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐<br>
  官方第一课：一条工单，一次请求里同时问一个 Choice、一个 Score 和一个 Noul，给了 Python / JS / cURL 三种写法。<br>
  <sub>`官方文档` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)**<br>
  七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。<br>
  <sub>`开源项目` · ★100k+ · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/Significant-Gravitas/AutoGPT/blob/HEAD/autogpt_platform/backend/backend/blocks/typesafe/_client.py)，2026-09-22 阅读</sub>

- **[jev-ultrafast](https://github.com/browser-use/jev-ultrafast)**<br>
  Browser Use 做的高速浏览器 Agent。Jev 每一步只判断「做什么、点哪个元素」，要打字才叫小模型。<br>
  <sub>`开源项目` · ★10k+ · Browser Use · `Py` · `choice` · [调用点](https://github.com/browser-use/jev-ultrafast/blob/HEAD/jev_ultrafast/model.py)，2026-09-22 阅读</sub>

  **注意:** `厂商自报数据`

- **[sub2api: Jev as a moderation endpoint](https://github.com/Wei-Shaw/sub2api)**<br>
  作为审核 API 的直接替代：一次请求并行问多个 Noul，每个危害类别一个，且每条指令都带反注入前缀。<br>
  <sub>`开源项目` · ★10k+ · `Go` · `noul` · [调用点](https://github.com/Wei-Shaw/sub2api/blob/HEAD/backend/internal/pkg/typesafe/client.go)，2026-09-22 阅读</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br>
  一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。<br>
  <sub>`教程` · ★1k+ · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/daveebbelaar/ai-cookbook/blob/HEAD/models/jev/06-criteria.py)，2026-09-22 阅读</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)**<br>
  一个完全不含语言模型的 tool calling 聊天机器人：一次请求同时问清请求类型、该调哪个工具、以及每个工具的参数。<br>
  <sub>`开源项目` · ★100+ · `TS` · `choice` · `noul` · [调用点](https://github.com/w3cj/jev-chat/blob/HEAD/apps/server/src/jev/client.ts)，2026-09-22 阅读</sub>

- **[jev-forge](https://github.com/zwliJay/jev-forge)**<br>
  并非 Jev：一套合成决策数据、训练并校准小型候选打分模型（JevForge-0.8B）、再通过兼容 Jev 的 API 提供服务的工具链，首个场景是在网页上挑选下一次点击或表单控件。其基准脚本把同一批留出的 choice、noul 和 score 问题发给真正的 Jev 作对比。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`Jev 替代实现` · ★100+ · zwlijay · `Py` · [引用文件](https://github.com/zwliJay/jev-forge/blob/HEAD/jevforge/bench_jev.py)，2026-09-22 阅读</sub>

  **注意:** `并非 Jev 本身`

- **[VideoJev](https://github.com/MCG-NJU/VideoJev)**<br>
  开源 System One 视频模型，在共享视频前缀上对多个问题的时间候选和多选答案直接打分，返回区间、答案和候选概率，无需生成文本。 <sub>(机翻)</sub><br>
  <sub>`Jev 替代实现` · ★100+ · Yuhan Zhu and collaborators · `Py`</sub>

  **注意:** `并非 Jev 本身` · `代码未实测` · `作者自荐`

已显示 **10 / 36** 条 · [在单独页面查看全部 36 条 →](docs/by-pattern/fan-out.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=fan-out&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 检索与排序

_对来自廉价检索步骤的候选做打分或重排。_

- **[Cookbook: Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages)** ⭐<br>
  给每条召回的段落打分，再由代码决定哪些能进入回答模型 —— 矛盾的标记保留，夹带提示注入的直接丢弃。<br>
  <sub>`官方文档` · `Py`</sub>

- **[Cookbook: Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find)** ⭐<br>
  对一份服务条款做语义检索：一次请求用 Choice 给 218 个行号打分，同时用 Noul 判断文档里到底有没有答案。<br>
  <sub>`官方文档` · `Py` · `choice` · `noul`</sub>

- **[Cookbook: Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe)** ⭐<br>
  对 40 个法律检索问题各取 30 条 BM25 候选，按「问题-候选」逐对提问重排，top-1 与 top-10 准确率均大幅提升。<br>
  <sub>`官方文档` · `Py`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)**<br>
  七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。<br>
  <sub>`开源项目` · ★100k+ · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/Significant-Gravitas/AutoGPT/blob/HEAD/autogpt_platform/backend/backend/blocks/typesafe/_client.py)，2026-09-22 阅读</sub>

- **[FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)**<br>
  两段式 MCP 工具检索：先用一个宽 Choice 对整个目录粗排，再给候选短名单配完整描述，每个候选各配一个 Noul 判断它到底是否胜任。<br>
  <sub>`开源项目` · ★10k+ · `Py` · `choice` · `noul` · [调用点](https://github.com/PrefectHQ/fastmcp/blob/HEAD/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py)，2026-09-22 阅读</sub>

- **[jcode: memory recall without embeddings](https://github.com/1jehuang/jcode)**<br>
  把记忆召回的整套检索栈替换掉 —— 不用 embedding、不用 BM25、不用重排器 —— 改为对每条候选记忆批量问一个 Noul。<br>
  <sub>`开源项目` · ★10k+ · `Rs` · `noul` · [调用点](https://github.com/1jehuang/jcode/blob/HEAD/crates/jcode-base/src/jev.rs)，2026-09-22 阅读</sub>

- **[LanceDB TypeSafeReranker](https://github.com/lancedb/lancedb/blob/main/python/python/lancedb/rerankers/typesafe.py)**<br>
  向量数据库的重排器：对每条结果问一个 Noul，把「是」的概率当作绝对相关性分数 —— 可以跨查询比较。<br>
  <sub>`开源项目` · ★10k+ · `Py` · `noul` · [调用点](https://github.com/lancedb/lancedb/blob/HEAD/python/python/lancedb/rerankers/typesafe.py)，2026-09-22 阅读</sub>

- **[OpenViking: retrieval reranking](https://github.com/volcengine/OpenViking)**<br>
  单次批量请求里对每个候选文档问一个 Noul，直接把「是」的概率当相关性分数。<br>
  <sub>`开源项目` · ★10k+ · `Py` · `noul` · [调用点](https://github.com/volcengine/OpenViking/blob/HEAD/openviking/models/rerank/jev_rerank.py)，2026-09-22 阅读</sub>

- **[XERJ](https://github.com/xerj-org/xerj)**<br>
  一个本地优先的搜索引擎兼 MCP 服务器，打包为单个 Rust 二进制文件。可选的 `rerank` 阶段对每条靠前结果向 Jev 提一个 `noul`（`document` 是否回答了 state 中的查询？），再按概率重新排序。作者报告 FiQA 上的 nDCG@10 从 0.24 升至 0.36，总共 648 次搜索花费约 0.64 美元。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10k+ · xerj-org · `Rs` · `noul` · [调用点](https://github.com/xerj-org/xerj/blob/HEAD/engine/crates/xerj-rerank/src/lib.rs)，2026-10-26 模型阅读</sub>

  **注意:** `厂商自报数据`

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)**<br>
  一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。<br>
  <sub>`开源项目` · ★1k+ · `Java` · `choice` · `score` · `noul` · [调用点](https://github.com/jev-chat/jev-chat-jarvis/blob/HEAD/cn/app/src/main/java/com/jev/probe/jev/JevQuestions.kt)，2026-09-22 阅读</sub>

已显示 **10 / 81** 条 · [在单独页面查看全部 81 条 →](docs/by-pattern/search-ranking.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=search-ranking&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 结构化抽取

_从杂乱文本中取出类型化字段 —— 靠在候选中选择，而不是生成。_

- **[Cookbook: Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook)** ⭐<br>
  抽取绝对与相对日期：先问文档里点明了哪些部分，再在代码里做解析与校验，并按置信度决定是否送审。<br>
  <sub>`官方文档` · `Py`</sub>

- **[Cookbook: Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook)** ⭐<br>
  先用正则找出候选的邮箱、电话、金额，再让模型挑出被问到的那一段，于是代码拿到的是逐字原值。<br>
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐<br>
  用两次请求把丢了格式的纯文本还原成 Markdown：一次把硬换行的段落重新接起来，一次给每个块分类。<br>
  <sub>`官方文档` · `Py`</sub>

- **[Cookbook: Structured data extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade)** ⭐<br>
  「小模型 → 校验 → 推理模型」的两段级联，用一小部分成本拿到接近大推理模型的质量。<br>
  <sub>`官方文档` · `Py`</sub>

- **[jev4pg](https://github.com/Sheltercosmo/jev4pg)**<br>
  为 PostgreSQL 提供自然语言 SQL 和 41 个语义算子。过滤、抽取、排序、匹配和核验以有上限的批次交给 Jev，答案须先通过校验；choice 选项需达 0.55、noul 需达 0.8 才算成立。作者报告其准确率为 98%，pg-jev 的请求路径为 92%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · Sheltercosmo · `Py` · `choice` · `noul` · [调用点](https://github.com/Sheltercosmo/jev4pg/blob/HEAD/sdd/generic/jev.py)，2026-10-26 模型阅读</sub>

  **注意:** `厂商自报数据`

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)**<br>
  面向 Apple 芯片上原生 macOS 应用的 computer use 智能体：由 OmniParser CoreML、Apple Vision OCR 和辅助功能标签在本机找出窗口里的控件，再由 Jev 根据观察到的文字（从不看像素）用 choice 选下一步动作。输入前有防护检查，基准测试核对的是实际结果，而不是 Jev 的 DONE 判断。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10+ · jcpsimmons · `JS` · [调用点](https://github.com/jcpsimmons/jev-macos-loop/blob/HEAD/src/providers.mjs)，2026-09-22 阅读</sub>

- **[jevfill](https://github.com/imohitmayank/jevfill)**<br>
  一个 Chrome 扩展：用 Jev 根据零散的文字笔记自动填写网页表单。把个人信息以纯文本粘贴一次即可，无需结构化档案，随时按需填表。 <sub>(机翻)</sub><br>
  <sub>`插件` · ★10+ · imohitmayank · `TS` · [调用点](https://github.com/imohitmayank/jevfill/blob/HEAD/src/jev/client.ts)，2026-09-24 阅读</sub>

- **[JevSpan](https://github.com/lzq-0529/jev-span)**<br>
  中英文零样本命名实体识别：代码按标点列出带精确字符位置的候选片段，由 Jev 的 choice 问题为每种实体类型提名窗口、核验每个候选（该类型、none、mixed 或 partial）并选出准确边界，每个实体都保留概率和决策过程。 <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10+ · lzq-0529 · `Py` · `choice` · [调用点](https://github.com/lzq-0529/jev-span/blob/HEAD/src/jevspan/jev_client.py)，2026-09-30 阅读</sub>

  **注意:** `疑似 AI 生成` · `作者自荐`

- **[smart-paste](https://github.com/nomanjack/smart-paste)**<br>
  根据粘贴的文本自动填写表单：把表单标题、字段标签和你的文字交给 TypeSafe，插入匹配到的值，提交前由你检查。 <sub>(机翻)</sub><br>
  <sub>`插件` · ★10+ · nomanjack · `JS` · [调用点](https://github.com/nomanjack/smart-paste/blob/HEAD/worker.js)，2026-09-24 阅读</sub>

- **[ask-jev](https://github.com/logicrw/ask-jev)**<br>
  只用标准库的命令行工具，在 280 毫秒的建议预算内把智能体的小判断交给 Jev：choose（choice）、check（用 noul 判断证据是否支持某个说法）、score、最多 32 题的 batch，以及 purify：对每段文字问一个 noul，只保留相关的原文行。失败即放行，由智能体做决定。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · logicrw · `Py` · [调用点](https://github.com/logicrw/ask-jev/blob/HEAD/scripts/jev_context.py)，2026-09-24 阅读</sub>

已显示 **10 / 19** 条 · [在单独页面查看全部 19 条 →](docs/by-pattern/data-extraction.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=data-extraction&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 分类

_把条目归入分类体系，包括用概率遍历的深层层级。_

- **[Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence)** ⭐<br>
  把年报分入 75 个行业组，再根据答案自身的置信度决定：报这个细分组，还是退回上一层的大类。<br>
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification)** ⭐<br>
  用对 Choice 概率做并行 beam search 的方式，遍历专利、零售、生物医学、源码这几套很深的分类体系。<br>
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment)** ⭐<br>
  判断两份商品目录间 450 个候选配对里哪些指的是同一个东西 —— 一个 Score 就够，它的三级正好对应三种可执行动作。<br>
  <sub>`官方文档` · `Py` · `score`</sub>

- **[Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat)** ⭐<br>
  用两次请求把丢了格式的纯文本还原成 Markdown：一次把硬换行的段落重新接起来，一次给每个块分类。<br>
  <sub>`官方文档` · `Py`</sub>

- **[Inbox Zero: seven email decisions](https://github.com/elie222/inbox-zero)**<br>
  七个互不相同的邮件决策，每个都有自己单独设定的阈值，任何出错都回落到普通 LLM。<br>
  <sub>`开源项目` · ★10k+ · `TS` · `choice` · `noul` · [调用点](https://github.com/elie222/inbox-zero/blob/HEAD/apps/web/utils/decision-model/typesafe.ts)，2026-09-22 阅读</sub>

- **[json-render](https://github.com/vercel-labs/json-render)**<br>
  Vercel Labs 的生成式 UI 框架。实验里 Jev 不逐 token 写 JSON，只负责选组件、属性和布局。<br>
  <sub>`开源项目` · ★10k+ · Vercel Labs · `TS` · `choice` · [调用点](https://github.com/vercel-labs/json-render/blob/HEAD/apps/web/lib/jev/compose.ts)，2026-09-22 阅读</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)**<br>
  用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。<br>
  <sub>`基准测试` · ★10k+ · `TS` · `choice` · [调用点](https://github.com/koala73/worldmonitor/blob/HEAD/shared/jev-classify.js)，2026-09-22 阅读 · 作者结论：不利（作者自述，未经本仓库复现）</sub>

  **注意:** `仅影子运行`

- **[pg-jev](https://github.com/realZachi/pg-jev)**<br>
  一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。<br>
  <sub>`开源项目` · ★1k+ · `Py` · `sh` · `choice` · `score` · `noul` · [调用点](https://github.com/realZachi/pg-jev/blob/HEAD/sql/jev--0.2.0.sql)，2026-09-22 阅读</sub>

- **[332_lab-jev-chat](https://github.com/Liyucheng1997/332_lab-jev-chat)**<br>
  电脑版微信助手：由 Jev 判断每条消息的意图，DeepSeek 给出建议回复。 <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · liyucheng1997 · `Kt` · [调用点](https://github.com/Liyucheng1997/332_lab-jev-chat/blob/HEAD/windows/jev_windows/jev_api.py)，2026-09-24 阅读</sub>

- **[classifier-dev](https://github.com/mrmps/classifier-dev)**<br>
  基于纯 HTTP 的零样本文本分类，无需密钥或注册：传入标签和文本，返回一个标签和校准过的置信度，一次请求可含一千条文本。两个档位都由 Jev 作答：每条文本一个 choice，多标签时每个标签一个 noul；smart 档会把置信度低于 0.7 的答案交给推理模型重答。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★100+ · mrmps · `TS` · [调用点](https://github.com/mrmps/classifier-dev/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

已显示 **10 / 134** 条 · [在单独页面查看全部 134 条 →](docs/by-pattern/classification.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=classification&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 机器学习特征抽取

_把自由文本转成数值特征，喂给下游的传统模型。_

- **[Cookbook: Autoresearch feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery)** ⭐<br>
  一个自动研究循环：自己提出问题、把自由文本转成数值特征、再用误差反过来改进下游的梯度提升回归模型。<br>
  <sub>`官方文档` · `Py`</sub>

- **[nimble](https://github.com/bespokelabsai/nimble)**<br>
  Bespoke-Nimble-9B 的数据、训练方法和推理代码：一个受 Jev 启发的开放决策模型，基于 Qwen3.5-9B 的 LoRA，对文本回答带概率的 choice 和是非题。在 324 条留出样本上，它与参考标注的一致率为 90.1%；按同样方式评分，Jev 1.13.0 为 93.2%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★1k+ · bespokelabsai · `Py` · [调用点](https://github.com/bespokelabsai/nimble/blob/HEAD/nimble/evaluation/evaluate_public_jev.py)，2026-09-22 阅读</sub>

  **注意:** `无许可证`

- **[jev-align](https://github.com/sutro-sh/jev-align)**<br>
  从人类反馈出发，构建经过校准的决策函数。<br>
  <sub>`开源项目` · ★100+ · sutro-sh · `Py` · [调用点](https://github.com/sutro-sh/jev-align/blob/HEAD/src/jev_align/jev.py)，2026-09-22 阅读</sub>

- **[Prism](https://github.com/irfndi/prism-liquidity-agent)**<br>
  不直接让 Jev 下单。它判断 toxic flow、市场压力、均值回归之类的状态，再交给原来的策略。<br>
  <sub>`开源项目` · ★100+ · `TS` · `choice` · `score` · [调用点](https://github.com/irfndi/prism-liquidity-agent/blob/HEAD/engine/jev-service.ts)，2026-09-22 阅读</sub>

- **[JEV Sees](https://github.com/CharlesFeng0314/JEV_sees)**<br>
  让 Jev“看见”：本地的 Florence-2 和 CLIP 模型在图像、视频或 RGB-D 画面中找出物体，并在帧之间保持物体 ID 一致，然后由 Jev 针对每个相关物体回答 choice、noul 或 score 问题（如公交车颜色、行人风险、动物运动状态）。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10+ · charlesfeng0314 · `Py` · `choice` · `noul` · `score` · [调用点](https://github.com/CharlesFeng0314/JEV_sees/blob/HEAD/jev_sees/session.py)，2026-10-24 模型阅读</sub>

- **[jev-board-lab](https://github.com/WebGrga/jev-board-lab)**<br>
  带密码保护的浏览器工作台，把 CSV 行变成 Jev 的判断：你写最多 20 个 noul、choice 或 score 问题，在最多 25 行选中的数据上运行，每行作为一个 state，经由保管密钥的 Cloudflare Worker 发送。CSV 文件留在浏览器里。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · webgrga · `JS` · [调用点](https://github.com/WebGrga/jev-board-lab/blob/HEAD/worker/src/index.js)，2026-09-22 阅读</sub>

  **注意:** `无许可证`

- **[jev-calibrated-narrative-coding](https://github.com/pozapas/jev-calibrated-narrative-coding)**<br>
  一篇论文的代码、问题模式和汇总结果：论文把 5,018,080 份得州警方交通事故叙述（2017–2025）以 noul、choice 和 score 问题交给 Jev，对照已编码字段和人工金标准集检验概率是否校准，并把校准结果换算成人需要复核多少被标记的记录。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · pozapas · `Py` · [调用点](https://github.com/pozapas/jev-calibrated-narrative-coding/blob/HEAD/src/jev_runner.py)，2026-09-24 阅读</sub>

- **[tiershift](https://github.com/iamvatsalpatel/tiershift)**<br>
  模型路由器：每个请求都从最便宜的档位开始，只有当 Jev 给出的信号（多步推理、难度、风险高低、安全）越过 YAML 策略时才往上升。在作者的 120 条提示上，它以低 40% 的成本达到旗舰模型的质量；而单用快速模型也得到同样的分数，成本只有 3%。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · iamvatsalpatel · `TS` · [调用点](https://github.com/iamvatsalpatel/tiershift/blob/HEAD/bench/experiments/gate-experiment.ts)，2026-09-22 阅读</sub>

- **[Truffler](https://github.com/kieranklaassen/truffler)**<br>
  面向 Rails 应用的意图搜索：每当记录被保存，Truffler 就向 Jev 提出为它声明的是非题、choice 和 score 问题，并把每个答案存成数值，使记录形成按名称分维的嵌入，搜索时按意图加权。用户需要时，Jev 还会把靠前结果重排为“很可能”“可能”“不太可能”三档。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`平台集成` · kieranklaassen · `Rb` · `noul` · `choice` · `score` · [调用点](https://github.com/kieranklaassen/truffler/blob/HEAD/lib/truffler/questions.rb)，2026-10-30 模型阅读</sub>

已显示全部 9 条 · [单独页面](docs/by-pattern/feature-extraction.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=feature-extraction&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 文档分拣

_对进来的文档、发票、表单做分类和路由。_

- **[docjev](https://github.com/jerryjliu/docjev)**<br>
  对 PDF、DOCX 和 PPTX 文件做分类和切分：LiteParse 在本地提取每页文字，然后 Jev 用一个 choice 按你的规则选出文档类别；对多文档合订本则逐页回答一个类别 choice 和一个“新文档是否从这里开始”的 noul。其报告涵盖 40 份真实 PDF。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · jerryjliu · `Py` · [调用点](https://github.com/jerryjliu/docjev/blob/HEAD/src/jev_docs/engines/jev.py)，2026-09-22 阅读</sub>

- **[formanator](https://github.com/timrogers/formanator)**<br>
  从命令行或 MCP 客户端提交 Forma 福利报销。使用 --category-provider jev 时，Jev 用一个 choice 从 Forma 允许的“福利加类别”组合（另加 no_match）中挑一个，只看商家和描述；置信度低于 0.5 或无匹配时，回退到配置好的 LLM。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★100+ · timrogers · `Rs` · [调用点](https://github.com/timrogers/formanator/blob/HEAD/src/typesafe.rs)，2026-09-22 阅读</sub>

- **[Quicksilver](https://github.com/UditAkhourii/quicksilver)**<br>
  一个 Claude Code 技能，把“是否相关”的判断交给 Jev：对每个文件、每行日志或每张工单问一个 noul（例如“这些文件里哪些处理鉴权？”），并行询问并按概率排序，于是 Claude 拿到的是带置信度的候选清单，而不必通读全部内容。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★100+ · uditakhourii · `JS` · `noul` · [调用点](https://github.com/UditAkhourii/quicksilver/blob/HEAD/skills/quicksilver/scripts/qs.mjs)，2026-10-24 模型阅读</sub>

- **[tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)**<br>
  税务文档分页分类器：每页一次请求，问 Jev 两个 choice：页面类型（7 个选项）和 IRS 表单（230 个另加“不在列表中”），五种表单的附表再用一个后续 choice 细分；选项描述由 IRS 官方 PDF 生成，代码以 0.95 为门槛。作者在 314 页已填写表单上测得严格错误为零。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · kyotofin · `TS` · [调用点](https://github.com/kyotofin/tax-doc-classifier/blob/HEAD/src/backend.ts)，2026-09-22 阅读</sub>

- **[doc-router](https://github.com/misbahsy/doc-router)**<br>
  逐页判断 PDF 是否需要 OCR 的 Rust 库：由 Jev（默认是内置的启发式规则）根据文字层证据对每页回答一个 noul；有文字的页面在本地提取，只有其余页面经 LiteLLM 交给 OCR 模型。在作者的测试中，155 页里只有 87 页计费。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10+ · misbahsy · `Rs` · [调用点](https://github.com/misbahsy/doc-router/blob/HEAD/crates/doc-router-jev/src/wire.rs)，2026-09-22 阅读</sub>

- **[jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)**<br>
  独立的社区地图，以中文为主，说明哪些任务适合交给 Jev 以及原因，依据是附带真实 API 调用记录的测试集，而不是排行榜：答案就在给定文字里时很准，比如该点击哪个 DOM 元素；别处则可能失准（DAIR Emotion 上平均置信度 0.819，实际只对 48%）。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · zaious · `Py` · [调用点](https://github.com/Zaious/jev-capability-atlas/blob/HEAD/scripts/common/jev_client.py)，2026-09-22 阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

- **[jevmory](https://github.com/romiluz13/jevmory)**<br>
  编程智能体的本地记忆：钩子把会话中真正说过的话按原文引语保存；jevmory audit 针对 MEMORY.md 的每一行问 Jev：已保存的证据是支持还是反驳它，并把各行标为保留、过时、错误或无依据。只用 Python 标准库和 SQLite；评分须主动开启。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10+ · romiluz13 · `Py` · [调用点](https://github.com/romiluz13/jevmory/blob/HEAD/jevmory/cli.py)，2026-09-22 阅读</sub>

- **[pdf-race](https://github.com/goodrahstar/pdf-race)**<br>
  让三条流水线在 12 篇 arXiv 论文上比赛：Docling 加 Jev、Docling 加 Gemini 3.8 Flash，以及 Gemini 直接读 PDF，每篇回答四个问题，按 arXiv 自己的元数据评分。三条都答对了 12 篇中全部的类别和标题；Jev 这条的成本是 $0.0022，另两条为 $0.036 和 $0.088。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · goodrahstar · `JS` · [调用点](https://github.com/goodrahstar/pdf-race/blob/HEAD/lib/lanes.mjs)，2026-09-24 阅读</sub>

- **[decision-first](https://github.com/harrymunro/decision-first)**<br>
  适用于 Claude Code、Codex、Cursor 等的智能体技能：当某一步工作是有界判断（分类、分诊、排序、路由、筛选、核验、把关）时，智能体先通过附带的脚本向 Jev 发送 noul、choice 或 score 问题，再考虑写正则或 LLM 提示，并记录每次尝试，无论是否采用。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · harrymunro · `Py` · [调用点](https://github.com/harrymunro/decision-first/blob/HEAD/skills/decision-first/scripts/ask.py)，2026-09-22 阅读</sub>

- **[Jev Playwright](https://github.com/arthurfiorette/jev-playwright)**<br>
  一个 Playwright 报告器：在启动任何浏览器之前，询问 Jev 某次代码改动可能影响哪些现有端到端测试，并跳过明显无关的测试。默认会发送改动路径、补丁和测试代码；README 提醒它可能漏掉受影响的测试。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · arthurfiorette · `TS` · [调用点](https://github.com/arthurfiorette/jev-playwright/blob/HEAD/src/config.ts)，2026-10-24 模型阅读</sub>

已显示 **10 / 22** 条 · [在单独页面查看全部 22 条 →](docs/by-pattern/document-triage.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=document-triage&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 工单分拣

_按意图和紧急度路由支持工单与会话。_

- **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐<br>
  官方第一课：一条工单，一次请求里同时问一个 Choice、一个 Score 和一个 Noul，给了 Python / JS / cURL 三种写法。<br>
  <sub>`官方文档` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br>
  一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。<br>
  <sub>`教程` · ★1k+ · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/daveebbelaar/ai-cookbook/blob/HEAD/models/jev/06-criteria.py)，2026-09-22 阅读</sub>

- **[spring-ai-typesafe](https://spring.io/blog/2026/09/21/spring-ai-typesafe-structured-judgment)**<br>
  社区维护的 Spring AI starter，把类型化决策带到 Java，用 builder API 封装三种问题类型。<br>
  <sub>`平台集成` · ★10+ · `Java` · `choice` · `score` · `noul` · [调用点](https://github.com/spring-ai-community/spring-ai-typesafe/blob/HEAD/examples/src/main/java/org/springaicommunity/typesafe/demo/JevQuickstart.java)，2026-09-22 阅读</sub>

- **[Example: three primitives in one request](https://github.com/kydlikebtc/awesome-jev/blob/main/examples/01-three-primitives/main.py)**<br>
  最小化的第一次调用：同时问一个 choice、一个 score 和一个 noul，并标注了容易踩的那几处不对称。<br>
  <sub>`代码片段` · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/kydlikebtc/awesome-jev/blob/HEAD/examples/01-three-primitives/main.py)，2026-09-22 阅读</sub>

  **注意:** `代码未实测`

- **[Jev AI Use Cases](https://medium.com/data-science-in-your-pocket/jev-ai-use-cases-9a87d57ac3b4)**<br>
  逐个用例走一遍 —— 智能体路由、智能体内部的决策层、工单分拣 —— 每个都给出具体的选项集和示例响应。<br>
  <sub>`教程` · Mehul Gupta · `Py` · `choice`</sub>

  **注意:** `付费墙`

- **[Jev on AI/ML API](https://docs.aimlapi.com/api-references/decision-models/typesafe/jev)**<br>
  又一个网关接入路径，值得记一笔是因为它的端点路径和请求外壳跟原生 API、跟 Cloudflare 都不一样。<br>
  <sub>`平台集成` · `Py` · `noul` · `choice` · `score`</sub>

- **[Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/)**<br>
  Workers AI binding 与 REST 示例：一次调用同时问 noul、choice、score，并给出含逐答案置信度的完整响应。<br>
  <sub>`平台集成` · `TS` · `sh` · `noul` · `choice` · `score`</sub>

- **[jev-triage](https://github.com/boldbug1/jev-triage)**<br>
  按紧急程度给消息排序的 Go 命令行工具：每条消息发一次 Jev 请求，问一个类型 choice（bug、计费、功能请求、账户、其他）、一个 0–3 的紧急程度 score，以及一个“发信人是否显得沮丧”的 noul。类别置信度低于 0.8 的消息放进人工复核列表。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · boldbug1 · `Go` · [调用点](https://github.com/boldbug1/jev-triage/blob/HEAD/main.go)，2026-09-24 阅读</sub>

- **[Support-routing benchmark: 100 held-out cases](https://decisionmodelhub.com/benchmarks/support-routing)**<br>
  在 100 条留出的虚构客服消息上，将 Jev 与 Clef、Clef Flash、OpenAI 的 Decisions API 以及 GPT-6 Luna 结构化输出基线进行对比：每条消息路由到五个团队标签之一；所有用例和各模型的作答记录均可下载。 <sub>(机翻)</sub><br>
  <sub>`基准测试` · DecisionModelHub</sub>

  **注意:** `作者自荐`

已显示全部 9 条 · [单独页面](docs/by-pattern/support-triage.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=support-triage&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 内容评分

_在有序量表上给质量、风险或相关性打分。_

- **[Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)** ⭐<br>
  在内容审核决策里显式加入「不确定」这个选项，并衡量标签一致率与自动处置比例之间的取舍。<br>
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Pattern: Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring)** ⭐<br>
  把一个笼统的判断拆成若干原子评分，再用你自己代码里的权重（而不是提示词里的）组合起来。<br>
  <sub>`官方文档` · `Py` · `score`</sub>

- **[AutoGPT TypeSafe blocks](https://github.com/Significant-Gravitas/AutoGPT/tree/master/autogpt_platform/backend/backend/blocks/typesafe)**<br>
  七个生产级 block（choice/score/yes-no/ask-many/route/pick-best/filter），带 UTF-8 字节预算、逐字报文留存和十一个测试文件。<br>
  <sub>`开源项目` · ★100k+ · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/Significant-Gravitas/AutoGPT/blob/HEAD/autogpt_platform/backend/backend/blocks/typesafe/_client.py)，2026-09-22 阅读</sub>

- **[worldmonitor: news threat classification](https://github.com/koala73/worldmonitor)**<br>
  用两个 Choice 判断威胁等级与类别；盲测发现 Jev 只是与原有模型打平，于是一直保持影子运行。<br>
  <sub>`基准测试` · ★10k+ · `TS` · `choice` · [调用点](https://github.com/koala73/worldmonitor/blob/HEAD/shared/jev-classify.js)，2026-09-22 阅读 · 作者结论：不利（作者自述，未经本仓库复现）</sub>

  **注意:** `仅影子运行`

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br>
  一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。<br>
  <sub>`教程` · ★1k+ · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/daveebbelaar/ai-cookbook/blob/HEAD/models/jev/06-criteria.py)，2026-09-22 阅读</sub>

- **[gptcache](https://github.com/zilliztech/GPTCache)**<br>
  面向 LLM 调用的语义缓存。其 Jev 评估器针对一条缓存答案和一个新请求问若干 noul：任务和上下文是否一致、格式是否合适、是否缺少内容、答案是否仍然新鲜；只有最低的一项也超过阈值（示例中为 0.70）才复用答案。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★1k+ · zilliztech · `Py` · [调用点](https://github.com/zilliztech/GPTCache/blob/HEAD/gptcache/similarity_evaluation/jev.py)，2026-09-22 阅读</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)**<br>
  一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。<br>
  <sub>`开源项目` · ★1k+ · `Java` · `choice` · `score` · `noul` · [调用点](https://github.com/jev-chat/jev-chat-jarvis/blob/HEAD/cn/app/src/main/java/com/jev/probe/jev/JevQuestions.kt)，2026-09-22 阅读</sub>

- **[pg-jev](https://github.com/realZachi/pg-jev)**<br>
  一个真正的 PostgreSQL 扩展，把三个原语暴露成 SQL 函数 —— 语义判断可以直接写进任意行类型的 WHERE 子句。<br>
  <sub>`开源项目` · ★1k+ · `Py` · `sh` · `choice` · `score` · `noul` · [调用点](https://github.com/realZachi/pg-jev/blob/HEAD/sql/jev--0.2.0.sql)，2026-09-22 阅读</sub>

- **[beebots](https://github.com/imikerussell/beebots)**<br>
  三个交易机器人在 OKX 永续合约上比赛，默认是模拟盘：每一步由 Jev（或 Gemini）用 choice 从合法动作中选出，再用 score 给出信心；另有确定性的备用选择器、纯代码写的风控层，以及显示每个决策由谁做出的实时面板。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · imikerussell · `TS` · `choice` · `score` · [调用点](https://github.com/imikerussell/beebots/blob/HEAD/src/jev.ts)，2026-10-24 模型阅读</sub>

- **[jev-as-a-judge](https://github.com/danielgshea/jev-as-a-judge)**<br>
  把 Jev 当作智能体评测的评委，与 GPT-5.6 Luna、GPT-5.6 Terra 和 Claude Sonnet 4.6 比较：一个天气智能体的五次固定运行，每次评 100 遍，给出质量分和通过与否。Jev 在全部 500 次判定中都与人工标注一致，其他三者为 99.8%、96.4% 和 80.0%；只有一位审阅者、五次运行。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · danielgshea · `Py` · [调用点](https://github.com/danielgshea/jev-as-a-judge/blob/HEAD/src/evals/judges/__init__.py)，2026-09-22 阅读</sub>

  **注意:** `无许可证`

已显示 **10 / 171** 条 · [在单独页面查看全部 171 条 →](docs/by-pattern/content-scoring.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=content-scoring&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 实时推荐

_选择下一步呈现什么，快到能用在实时会话里。_

- **[1 Million Emojis](https://github.com/cwdx/1-million-emojis)**<br>
  一块 1,000 × 1,000 的共享表情画布，Jev 和人一起作画：每一笔之后发一次请求，用 choice 从“表情加位置”的选项里挑一个，再用 noul 判断这一笔是否还没画完；先走 Vercel AI Gateway，TypeSafe 直连作为后备。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · cwdx · `TS` · `choice` · `noul` · [调用点](https://github.com/cwdx/1-million-emojis/blob/HEAD/packages/jev/src/index.ts)，2026-10-24 模型阅读</sub>

  **注意:** `作者自荐`

- **[Jevflix](https://github.com/ArielBubis/Jevflix)**<br>
  电影推荐器：FAISS 与 BM25 检索把 4,800 部电影缩成短名单，Jev 读出请求里的约束（片长、不要血腥画面）供代码过滤，再由一次覆盖最多 250 个候选的 Jev choice 选出一部影片。没有把握时，由 LLM 权衡前五名或追问一个问题。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · arielbubis · `Py` · [调用点](https://github.com/ArielBubis/Jevflix/blob/HEAD/movie_rec/jev_client.py)，2026-09-24 阅读</sub>

已显示全部 2 条 · [单独页面](docs/by-pattern/recommendation.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=recommendation&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 总览

_介绍模型或整个领域，而非单一模式。_

- **[Official agent skill for Claude Code](https://docs.typesafe.ai/agent-skill)** ⭐<br>
  把 TypeSafe 官方技能装进 Claude Code，让智能体自己写出正确的 Jev 调用，不必每次手动贴 API 结构。<br>
  <sub>`官方文档` · ★1k+ · `sh`</sub>

- **[@typesafe-ai/sdk (TypeScript / JavaScript)](https://github.com/typesafe-ai/typesafe-sdk-js)** ⭐<br>
  官方 TypeScript 客户端。同时提供 ESM、CJS 和类型声明，辅助函数是小写的 choice()/score()/noul()。<br>
  <sub>`SDK` · ★100+ · `TS` · `JS` · `choice` · `score` · `noul` · [调用点](https://github.com/typesafe-ai/typesafe-sdk-js/blob/HEAD/src/types.ts)，2026-09-22 阅读</sub>

- **[system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python)** ⭐<br>
  一个可直接替换 TypeSafeClient 的适配器，底层走普通 LLM API —— 没有 Jev 权限也能跑 Jev 形状的代码。<br>
  <sub>`SDK` · ★100+ · `Py` · [引用文件](https://github.com/typesafe-ai/system-one-adapter-python/blob/HEAD/src/system_one_adapter/_client.py)</sub>

- **[typesafe-sdk (Python)](https://github.com/typesafe-ai/typesafe-sdk-python)** ⭐<br>
  官方 Python 客户端。含同步与异步客户端、支持 retry-after 的重试策略，以及 Choice/Score/Noul 辅助类。<br>
  <sub>`SDK` · ★100+ · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/typesafe-ai/typesafe-sdk-python/blob/HEAD/src/typesafe_sdk/_core/client/aio/client.py)，2026-09-22 阅读</sub>

- **[API reference](https://docs.typesafe.ai/api)** ⭐<br>
  POST /v1/systemone 的核心 Choice、Score、Noul 问题请求与应答结构，以及请求校验和 HTTP 错误处理。 <sub>(机翻)</sub><br>
  <sub>`官方文档` · `sh` · `Py` · `TS`</sub>

- **[Models, pricing and limits](https://docs.typesafe.ai/models)** ⭐<br>
  原生 Jev 1.14/1.13 的 ID、别名、价格与限制：输入 $0.042/Mtok，输出免费，默认每次请求 64k token、每个问题 32k。默认输入为文本；图像和 262k 长上下文需显式开启实验功能。 <sub>(机翻)</sub><br>
  <sub>`官方文档` · `sh` · `Py` · `TS`</sub>

- **[Primitives: Choice, Score, Noul](https://docs.typesafe.ai/primitives)** ⭐<br>
  核心 Choice、Score、Noul 问题类型的选择、组合与 criteria 写法；Choice 最多 255 个选项，Score 支持 2–10 级。 <sub>(机翻)</sub><br>
  <sub>`官方文档` · `Py` · `TS` · `choice` · `score` · `noul`</sub>

- **[Introducing System One models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)** ⭐<br>
  发布博文：什么是 System One 模型、为什么要把决策从生成里拆出来，以及厂商自报的延迟与成本数字。<br>
  <sub>`文章` · Diogo Almeida</sub>

  **注意:** `厂商自报数据`

- **[Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13)** ⭐<br>
  厂商列出的 Jev 1.13 局限：字面化理解、算术与计数、日期比较、间接指代、夹杂无关细节的长 state，以及对抗性内容。 <sub>(机翻)</sub><br>
  <sub>`官方文档`</sub>

- **[Use case map](https://docs.typesafe.ai/concepts/use-case-map)** ⭐<br>
  厂商自己的分类体系：五大类、十九个行业方向、十种决策形态（从分类一直到结构化数据抽取）。<br>
  <sub>`官方文档`</sub>

已显示 **10 / 492** 条 · [在单独页面查看全部 492 条 →](docs/by-pattern/overview.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=overview&lang=zh)

#### 尚未按模式索引

其中 **252** 行是带代码的项目或插件。`overview` 也是关键词规则无法归类时给出的默认值，而这些行没有任何人对照决策模式阅读过的记录（`patterns_reviewed`），因此单独列出：见 [Overview 页面末尾](docs/by-pattern/overview.zh-CN.md#unindexed)、[站点](https://kydlikebtc.github.io/awesome-jev/?p=overview&lang=zh)，以及附有规则建议的[复核队列](docs/review-queue.md#unsorted-overview)。 <sub>(机翻)</sub>

<sub>[↑ 场景索引](#pattern-index)</sub>

## 按资源形态

同样这些行，按你点开链接后会看到什么来分组。

| 形态 | 例子数 | 点开会看到 |
| --- | ---: | --- |
| **官方文档** | **31** | 厂商文档、cookbook 与模式页。 |
| **SDK** | **100** | 客户端库，官方与社区。 |
| **平台集成** | **36** | 接入模型的网关、框架或平台路径。 |
| **代码片段** | **4** | 本仓库内的小型可运行样例。 |
| **开源项目** | **693** | 真正在调用 Jev 的应用或库。 |
| **插件** | **249** | 可安装的编辑器、智能体、MCP 集成。 |
| **教程** | **13** | 带代码的分步教学材料。 |
| **基准测试** | **75** | 实测。注意区分独立实测与厂商自报。 |
| **文章** | **14** | 讲解、分析与发布报道。 |
| **视频** | **3** | 演示与评测。 |
| **讨论** | **2** | 值得读的讨论，包括质疑的声音。 |
| **Jev 替代实现** | **90** | 独立复现实现。它们**不**调用 Jev。 |

## 本仓库还有什么

除目录数据之外的部分。

<details>
<summary><b>查看可搜索站点预览</b></summary>

<a href="https://kydlikebtc.github.io/awesome-jev/?lang=zh"><img src="https://kydlikebtc.github.io/awesome-jev/img/site-zh.png?v=4cedad20b736eaea" alt="可搜索的 Jev 目录：精选路径、筛选排序、带日期的来源证据与条目卡片" width="760"></a>

<sub>点击条形即可筛选。另有两个视图：<a href="https://kydlikebtc.github.io/awesome-jev/?view=prims&lang=zh">三个原语</a> · <a href="https://kydlikebtc.github.io/awesome-jev/?view=compat&lang=zh">兼容性矩阵</a>。每个筛选条件和每个条目都是可分享的 URL。也有静态页面：<a href="https://kydlikebtc.github.io/awesome-jev/patterns/">每个模式一页</a> · <a href="https://kydlikebtc.github.io/awesome-jev/new.zh.html">每周新增与退役</a>（<a href="https://kydlikebtc.github.io/awesome-jev/feed.zh.xml">Atom 订阅</a>）。</sub>

</details>

| 文件 | 是什么 |
| --- | --- |
| [`docs/patterns.zh-CN.md`](docs/patterns.zh-CN.md) | 逐个定义每个模式，并明确写出**什么时候不该用它**。 |
| [`docs/compatibility.md`](docs/compatibility.md) | 模型串、字段名、请求结构、端点、环境变量 —— 每个平台都不一样。这就是那张对照表。 |
| [`docs/vetting.md`](docs/vetting.md) | 信任一个条目之前该检查什么，以及大多数人会犯的那一个错。 |
| [`docs/status.md`](docs/status.md) | 这个生态第一周的真实样貌，包括缺口。 |
| [`docs/shape.zh-CN.md`](docs/shape.zh-CN.md) | 把目录当作数据集来看：语言、如何接入 Jev、各类型的 star 区间、各模式用的语言。 <sub>(机翻)</sub> |
| [`docs/method.md`](docs/method.md) | 目录是如何建起来的、排除了什么、以及它最弱的地方在哪。 |
| [`docs/sources.md`](docs/sources.md) | 每一行的来源，以及许可状况。 |
| [`examples/`](examples/) | 四个可运行样例。其中一个刻意把阈值策略留给你写。 |
| [`schema/entry.schema.json`](schema/entry.schema.json) | 一条目录记录允许包含什么。 |
| [`.claude-plugin/`](.claude-plugin/) | 在 Claude Code 里一次装好技能和 MCP server：先 `/plugin marketplace add kydlikebtc/awesome-jev`，再 `/plugin install awesome-jev@awesome-jev`。 |
| [`src/awesome_jev_mcp/`](src/awesome_jev_mcp/) | 一个 MCP server —— 让智能体可以查询目录而不是阅读它。每条结果都带着它的警示，也带着数据有多新。 |
| [`skills/awesome-jev/`](skills/awesome-jev/) | 一份 agent 技能：生成的 Jev 代码最常搞错的那些事实，以及值得遵循的设计规则。 |
| [`scripts/verify_claims.py`](scripts/verify_claims.py) | 每周重读每一处被引用的调用点 —— 让原语声明可核实，而不只是被断言。 |
| [`scripts/refresh_metadata.py`](scripts/refresh_metadata.py) | 从 GitHub API 重新读取 star、许可证与归档状态，并开 PR。 |

`skills/awesome-jev/` 是对 TypeSafe 官方智能体技能 [typesafe-ai/skills](https://github.com/typesafe-ai/skills)（[目录条目](https://kydlikebtc.github.io/awesome-jev/?lang=zh#typesafe-skills-repo)）的补充，而非替代：API 契约与问题设计以官方技能及其所读的实时文档为准；本技能补充公开生态里能看到的东西——实际示例及其警示、各平台差异，以及独立测量与负面结果。 <sub>(机翻)</sub>

## 哪些经过核实，哪些没有

- **链接检查** —— 有 1261 行记录了 HTTP 2xx 响应和 `checked` 日期，另有 49 行没有带日期的成功记录。检查日期因条目而异，过去成功不保证今天仍可访问。star 数和许可证也是仓库元数据的快照。

- **来源与代码阅读** —— `evidence.path` 指向所读文件，`evidence.read_on` 记录声明的阅读日期，`evidence.model_read_on` 记录模型的阅读、单独显示，`evidence_none` 解释缺少文件证据的原因。阅读调用点与运行代码是两件事。摘要包含源项目描述与机翻，详见[方法与局限](docs/method.md)。 <sub>(机翻)</sub>

- **摘要是谁的文字** —— 752 条摘要的英文原文就是被链接项目自己在 GitHub 上的描述，逐字相同，这些行标为 *(项目自述)*；27 条标为 *(项目旧自述)*：英文取自项目描述，但两者已不再相同。这些文字出自项目作者，中文摘要是其译文。11 条摘要标明由人为本目录撰写，203 条由模型为本目录撰写并标为 *(模型撰写)*，317 条未作记录。每周刷新会把每条英文摘要与其仓库描述比对并标出相同者；只有人才能把摘要标为人写的。 <sub>(机翻)</sub>

- **中文是谁写的** —— 1310 行中有 192 行的中文摘要由人撰写；其余 1118 行由模型翻译，带有 `zh_machine`，并在中文 README、中文模式页面和站点的中文视图中逐条标为 *(机翻)*。[翻译队列](docs/zh-queue.md)列出等待有人替换的机翻：先是星标最高各行的全部机翻，再按星标从高到低列出被脚本计算的三项文本信号（比英文短得多、缺少英文里的数字、大部分是 ASCII 字符）中至少一项标出的其他机翻。信号只是对照比较，不是对译文的结论，README、模式页面和站点上的各行都不显示信号。认领方法见[认领翻译](CONTRIBUTING.md#claim-a-translation)；只有你自己写的译文才能去掉 `zh_machine`。 <sub>(机翻)</sub>

- **调用点文本复查** —— 有 1139 行通过 `evidence` 记录了项目调用 Jev 的文件及其中匹配的字符串。另有 86 行记录的文件只表明项目采用了 Jev 的请求结构、并非基于 Jev 构建（所有 `alternative`——无论是自己提供这种结构，还是向 Jev 发送同样的请求作对比——以及由其他模型支撑的适配器），0 行记录的只是项目附带的示例；`evidence.kind` 标明属于哪一种。每周 [claims 任务](https://github.com/kydlikebtc/awesome-jev/actions/workflows/claims.yml) 检查这些字符串是否仍在默认分支，发现文本或文件缺失时报告。这些数字是已记录的证据数量，**不是最新 CI 通过数**。文本匹配不能证明调用实际执行、API 兼容或结果正确。脚本标出、需要人重读的引用列在[复核队列](docs/review-queue.md)。 <sub>(机翻)</sub>

- **用了哪些原语** —— 有 111 行在 `question_types` 中记录了有人读代码时确认调用的原语；另有 60 行记录的是模型读代码时确认的原语，这些行的调用点只有模型读过（`evidence.model_read_on`）。此外还有 692 行带 `primitives_seen`，这是机器文本信号：每周刷新在该行所引的那一个文件中找到了某个原语的请求或回答结构（`"type": "choice"`、`Noul(`、`.noul`）。文件里出现这种结构不等于调用；其中 615 行没有 `question_types`，这个信号就是关于它们所用原语的全部记录。本目录的筛选、计数和规则都不会把它当作原语声明。 <sub>(机翻)</sub>

- **本仓库未独立验证运行与性能** —— 所有目录条目默认都未经本仓库实测，没有 `code-untested` 标签也不代表已测试。被收录的基准是原作者的测量，本目录没有独立复现。仓库构建检查与安装包冒烟测试不运行这些集成，也不调用 Jev 在线 API；收录亦不代表安全审计。


### 这些标记是什么意思

| 标记 | 含义 |
| --- | --- |
| `并非 Jev 本身` | 完全不调用 Jev。协议兼容不等于校准兼容，所以阈值不能迁移。 |
| `仅影子运行` | 接进去了但故意不生效 —— 它返回的东西不会进入任何对用户可见的决策。 |
| `需早期访问` | 需要通过等候名单才能运行。 |
| `代码未实测` | 代码是读过的，没有实际运行。 |
| `仅一次提交` | 每周刷新上次询问 GitHub 时，默认分支只有一次提交；此标记由每周刷新自动添加和移除。 |
| `无许可证` | 没有 LICENSE 文件，不管 README 徽章怎么写。复用时这是硬障碍。 |
| `需第三方密钥` | 需要 TypeSafe 之外某个服务的密钥。 |
| `厂商自报数据` | 照搬厂商自测数据，不是独立实测。 |
| `宣称未核实` | 做出了无法核实的量化宣称。 |
| `疑似 AI 生成` | 读起来像机器生成的内容。 |
| `营销内容` | 发布目的既是讲解也是推销。 |
| `付费墙` | 有付费墙或阅读次数限制。 |
| `已归档` | 开发明显已经停止。 |
| `作者自荐` | 由项目作者或维护者本人提交。这是对关系的披露，不是质量评判。 |
| `实测后未采用` | 项目作者本人针对这一用途测量过 Jev，结论是不采用或已将其移除。这是作者的结论，未经本仓库复现；请先读它，再看正面例子。基准测试行改用 measurement.direction（不利）记录同一件事。 |

### 已退休的链接

已无法访问的链接。保留下来，让失效的引用仍可被搜索到，而不是凭空消失。

| 例子 | 原因 |
| --- | --- |
| datajev | 2026-10-24 退役：自 2026-09-29 起每周刷新都无法访问该仓库（最近一次为 2026-10-21）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| jev-atlas | 2026-09-24 退役：仓库在 API 和网页上都返回 404，而作者账号仍然存在 —— 已删除或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| jev-curate | 2026-10-24 退役：自 2026-10-13 起每周刷新都无法访问该仓库（最近一次为 2026-10-21）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| jev-git | 2026-10-24 退役：自 2026-10-13 起每周刷新都无法访问该仓库（最近一次为 2026-10-21）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| jev-mac-voice | 2026-09-24 退役：仓库在 API 和网页上都返回 404，而作者账号仍然存在 —— 已删除或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| jev-reviewer | 2026-10-29 退役：自 2026-10-19 起每周检查都无法访问该仓库（最近一次为 2026-10-28）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| jev-scout | 2026-10-24 退役：自 2026-10-13 起每周刷新都无法访问该仓库（最近一次为 2026-10-21）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| jev-screen-mcp | 2026-10-24 退役：自 2026-09-29 起每周刷新都无法访问该仓库（最近一次为 2026-10-21）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| jev-seo | 2026-10-24 退役：自 2026-10-13 起每周刷新都无法访问该仓库（最近一次为 2026-10-21）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| jev-skills | 2026-10-24 退役：自 2026-10-06 起每周刷新都无法访问该仓库（最近一次为 2026-10-21）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| jev-superpowers | 2026-10-24 退役：自 2026-10-13 起每周刷新都无法访问该仓库（最近一次为 2026-10-21）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| JevRev | 2026-10-24 退役：自 2026-10-13 起每周刷新都无法访问该仓库（最近一次为 2026-10-21）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| rh-guard | 2026-10-24 退役：自 2026-10-13 起每周刷新都无法访问该仓库（最近一次为 2026-10-21）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| typesafe-oracles | 2026-10-24 退役：自 2026-09-29 起每周刷新都无法访问该仓库（最近一次为 2026-10-21）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| zerosweep | 2026-10-24 退役：自 2026-09-29 起每周刷新都无法访问该仓库（最近一次为 2026-10-21）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |

## 机器可读数据

每个例子一条记录，每次推送都按 JSON Schema 校验。

| 文件 | 是什么 |
| --- | --- |
| [`catalog.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/catalog.json) | 1310 条目 |
| [`retired.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/retired.json) | 15 已退休 |
| [`compat.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/compat.json) | `docs/compatibility.md` 使用的平台兼容性数据 |
| [`patterns.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/patterns.json) | 生成器与 MCP server 共用的决策模式分类 |
| [`collections.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/collections.json) | 双语精选路径、推荐理由与使用限制 |
| [`schema/entry.schema.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/schema/entry.schema.json) | 每条目录记录的字段规范 |
| [`llms.txt`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/llms.txt) | 供智能体读取的目录说明，明确附带限制 |

## 参与贡献与许可

纠错优先于新增 —— 一个错的条目比一个缺失的条目代价更大。详见 [CONTRIBUTING.md](CONTRIBUTING.md)；收录标准是：*读者不点开链接，能否据此行动？*

`scripts/`、`site/`、`examples/` 中的代码采用 [MIT](LICENSE-MIT)。目录元数据采用 [CC0-1.0](LICENSE-CC0)，并带逐行 `license` 字段。被链接的作品各自保留原许可 —— `repo_license` 记录了各自声明的内容。标有 *(项目自述)* 或 *(项目旧自述)* 的摘要是被链接项目自己的文字（中文为其译文），不在上述 CC0 声明之内（见[来源与许可](docs/sources.md#licences)）。 <sub>(机翻)</sub>

**维护检查:** [![lint](https://github.com/kydlikebtc/awesome-jev/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/kydlikebtc/awesome-jev/actions/workflows/lint.yml) · [定期链接检查](https://github.com/kydlikebtc/awesome-jev/actions/workflows/links.yml) · [调用点文本检查](https://github.com/kydlikebtc/awesome-jev/actions/workflows/claims.yml)

---

**Jev Decision Atlas** · [↑ 返回顶部](#top) · [English](README.md)
