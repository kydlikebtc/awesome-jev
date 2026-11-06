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
  <img src="docs/assets/readme-cover-zh-light.svg" alt="awesome-jev — Jev 发布榜：1,128 个用 Jev 做的产品、961 位 Maker、1,206 条调用点引用记录。数字来自保存的记录，不代表当前链接可用或运行与性能测试通过。" width="100%">
</picture>
</a>

<p align="center">
<a href="https://kydlikebtc.github.io/awesome-jev/launches.zh.html"><kbd>&nbsp;<b>发布榜&nbsp;↗</b>&nbsp;</kbd></a>
<a href="https://github.com/kydlikebtc/awesome-jev/issues/new?template=launch.yml"><kbd>&nbsp;发布产品&nbsp;</kbd></a>
<a href="https://kydlikebtc.github.io/awesome-jev/?lang=zh"><kbd>&nbsp;浏览资源目录&nbsp;↗&nbsp;</kbd></a>
<a href="https://kydlikebtc.github.io/awesome-jev/?collection=first-call&amp;lang=zh"><kbd>&nbsp;第一次调用&nbsp;</kbd></a>
<a href="https://kydlikebtc.github.io/awesome-jev/?collection=build&amp;lang=zh"><kbd>&nbsp;改造现有项目&nbsp;</kbd></a>
<a href="https://kydlikebtc.github.io/awesome-jev/?collection=measured&amp;lang=zh"><kbd>&nbsp;独立测量报告&nbsp;</kbd></a>
<a href="README.md"><kbd>&nbsp;English&nbsp;</kbd></a>
</p>

<p align="center"><sub>数字统计已保存的链接与证据记录，不代表当前 CI 通过数或运行测试结果。 <a href="#哪些经过核实哪些没有">统计口径</a></sub></p>

<details>
<summary><b>阅读导航 · 完整目录</b></summary>

[决策模式](docs/patterns.zh-CN.md) · [兼容性](docs/compatibility.md) · [核查指南](docs/vetting.md)

- 01 [本周发布榜](#本周发布榜)
- 02 [发布你的产品](#发布你的产品)
- 03 [这是什么](#这是什么)
- 04 [Jev 返回什么](#jev-返回什么)
- 05 [从这里开始](#从这里开始)
- 06 [覆盖度](#覆盖度)
- 07 [实测，而非宣称](#实测而非宣称)
- 08 [按决策模式](#按决策模式)
- 09 [按资源形态](#按资源形态)
- 10 [本仓库还有什么](#本仓库还有什么)
- 11 [哪些经过核实，哪些没有](#哪些经过核实哪些没有)
- 12 [机器可读数据](#机器可读数据)
- 13 [参与贡献与许可](#参与贡献与许可)

</details>

---

## 本周发布榜

用 Jev 做出来的产品，由 Maker 每周发布一次，任何人也可以推荐（hunt）自己发现的产品。大家在每个 Launch 的 [Discussions](https://github.com/kydlikebtc/awesome-jev/discussions/categories/launches) 帖子上点赞投票，每周日 23:59 UTC 收榜、排名。票数说明有多少人关心；每个 Launch 旁边的证据说明谁读过它调用 Jev 的代码。两者从不相加，名次也不是本目录的推荐。[发布榜](https://kydlikebtc.github.io/awesome-jev/launches.zh.html)上有每一周、每个产品和每位 Maker 的页面，以及上升榜。 <sub>(机翻)</sub>

榜上还没有 Launch。周四 23:59 UTC 前提交的 Launch 周五登记、下周一开榜：[发布一个产品](https://github.com/kydlikebtc/awesome-jev/issues/new?template=launch.yml)，自己做的或你发现的都行，比如下面上升最快的这些。 <sub>(机翻)</sub>

### ★ 上升最快：2026-10-28 至 2026-11-04

1. ★ **+35** **[jeveryword](https://kydlikebtc.github.io/awesome-jev/products/jeveryword.html)** — 用 Jev 做文本抽取：字段抽取、PII 检测与逐字引文。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>5 → 40 星（+700%） · 👤 有人读过调用点 · [发布它 ↗](https://github.com/kydlikebtc/awesome-jev/issues/new?template=launch.yml&product=jeveryword&title=Launch%3A%20jeveryword)</sub>
2. ★ **+12,379** **[agent-desktop](https://kydlikebtc.github.io/awesome-jev/products/agent-desktop.html)** — 桌面自动化。读系统无障碍树，判断下一步该点哪个按钮、菜单或输入框。<br>
  <sub>1,827 → 14,206 星（+678%） · 👤 有人读过调用点 · [发布它 ↗](https://github.com/kydlikebtc/awesome-jev/issues/new?template=launch.yml&product=agent-desktop&title=Launch%3A%20agent-desktop)</sub>
3. ★ **+26** **[anydecisionmodel](https://kydlikebtc.github.io/awesome-jev/products/anydecisionmodel.html)** — 一个 Swift 包：从语言模型获取类型化决策（概率、选择与分数）。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>24 → 50 星（+108%） · 👤 有人读过调用点 · [发布它 ↗](https://github.com/kydlikebtc/awesome-jev/issues/new?template=launch.yml&product=anydecisionmodel&title=Launch%3A%20anydecisionmodel)</sub>
4. ★ **+53** **[fastbrowse](https://kydlikebtc.github.io/awesome-jev/products/fastbrowse.html)** — 浏览器智能体：每个页面被索引成候选控件，由 Jev 选出下一步，因此不会点击页面上没有的东西；规划和阅读由 Gemini Flash 负责，答案引用页面原文。维护者记录的 46 个任务中成功率为 99.2%，托管版 Browser Use 为 97.8%，而成本不到其十分之一。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>120 → 173 星（+44%） · 🤖 模型读过调用点，尚无人复核 · [发布它 ↗](https://github.com/kydlikebtc/awesome-jev/issues/new?template=launch.yml&product=fastbrowse&title=Launch%3A%20fastbrowse)</sub>
5. ★ **+14** **[jev-guard](https://kydlikebtc.github.io/awesome-jev/products/jev-guard.html)** — 给编程智能体用的安全钩子：每次工具调用前，Jev 判断这次调用可能造成多大危害、是不是用户要求的、是否在执行不可信的文字，再由代码决定拒绝、询问还是放行；调用返回后，Jev 扫描结果中的提示注入。支持 Claude Code、Codex、Cursor 等。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>130 → 144 星（+11%） · 👤 有人读过调用点 · [发布它 ↗](https://github.com/kydlikebtc/awesome-jev/issues/new?template=launch.yml&product=jev-guard&title=Launch%3A%20jev-guard)</sub>

<sub>最近两次每周刷新之间，GitHub 星标涨得最快的 10 个产品：至少涨了 10 个，按涨幅占原有星标的比例排序，这里列前 5 个。星标是 GitHub 的计数，是热度信号，不是评价；上升不会得到任何奖励。[发布榜上的全部 10 个](https://kydlikebtc.github.io/awesome-jev/launches.zh.html)。 <sub>(机翻)</sub></sub>

## 发布你的产品

任何用 Jev 做的、代码公开的东西都可以发布：项目、插件、SDK 或集成，只要它的条目在目录里（没有就先[添加条目](https://github.com/kydlikebtc/awesome-jev/issues/new?template=new-entry.yml)）。Maker 发布自己的产品；任何人都可以推荐自己发现的产品。没有一步需要等维护者：每种情况都有规则，issue 上的检查会告诉你它的判定。 <sub>(机翻)</sub>

| 步骤 | 时间 | 会发生什么 |
| --- | --- | --- |
| **🚀 发布** | 周四 23:59 UTC 前 | 打开[发布表单](https://github.com/kydlikebtc/awesome-jev/issues/new?template=launch.yml)，或在产品页点「发布它」，表单会自动填好。检查会立刻在 issue 上回复：下周上榜，或者需要改什么。 |
| **▲ 投票** | 周一到周日 | 周一开榜，每个 Launch 在 [Discussions](https://github.com/kydlikebtc/awesome-jev/discussions/categories/launches) 里有一个帖子。投票就是在帖子上点赞：每个账号一票，Maker 自己的票不计，注册不满 30 天的账号算半票。 |
| **🏆 结果** | 下周一 | 计票、排名，前三名的徽章显示名次，每个 Launch 的 issue 都会收到结果。60 天后可以再次发布。 |
<sub>(机翻)</sub>

每个产品都有一枚自动更新的徽章：已收录，然后是发布中、本周投票，再到前三名的名次。在你的 README 里放一行，之后不用再改： <sub>(机翻)</sub>

[![awesome-jev](https://kydlikebtc.github.io/awesome-jev/badges/jeveryword.svg)](https://kydlikebtc.github.io/awesome-jev/products/jeveryword.html) <sub>← `jeveryword` 今天的样子</sub>

```markdown
[![awesome-jev](https://kydlikebtc.github.io/awesome-jev/badges/your-slug.svg)](https://kydlikebtc.github.io/awesome-jev/products/your-slug.html)
```

完整规则：[怎么计票](docs/launches.zh-CN.md#怎么计票规则-v2) · [发布榜](https://kydlikebtc.github.io/awesome-jev/launches.zh.html) · [每周结果订阅](https://kydlikebtc.github.io/awesome-jev/launches.zh.xml) · [给智能体的 JSON](https://kydlikebtc.github.io/awesome-jev/api/v1/launches.json) 以及 MCP 服务器的 `launch_board`、`top_launches` 工具 · [在你自己的仓库里跑同一套发布榜](docs/launch-engine.zh-CN.md)。 <sub>(机翻)</sub>

## 这是什么

- **Jev** 是 TypeSafe AI 的决策模型。它不生成文本 —— 你给它状态和类型化问题，它返回带校准置信度的类型化答案，快且便宜到可以放进智能体的内层循环。 <sub>(机翻)</sub>
- **本仓库**是目录之上的一个发布榜。上面的榜：用 Jev 做的产品，由 Maker 每周发布一次、大家投票。榜的下面是 Jev 决策图谱：这个索引能找到的每一个 Jev 公开用例，按所做的**决策**组织 —— 资料会过时，决策模式不会。发布需要先有条目；条目不需要发布。 <sub>(机翻)</sub>
- **如何判断可信度：**每一行都写明来源；有依据时记录调用点、原语声明和注意事项。榜上同一份记录就放在票数旁边，信一个名次之前先看看读过什么。 <sub>(机翻)</sub>

> [!NOTE]
> 不是产品本身，不是 SDK，与 TypeSafe AI 无隶属关系，也不构成推荐。收录是一份来源记录，名次只是票数的计数；两者都不代表运行验证或性能背书。详见[哪些经过核实](#哪些经过核实哪些没有)。 <sub>(机翻)</sub>

## Jev 返回什么

三个核心原语：Choice、Score 和 Noul。下面的模式使用它们；Noul 返回概率，没有单独的 confidence 字段。Jev 1.14 还新增了实验性 [Box](https://docs.typesafe.ai/primitives/box)：每个问题返回一个边界框和置信度，没有「未找到」答案。Box 需要图像，并须按下文显式启用图像功能。 <sub>(机翻)</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/primitives-zh-dark.svg">
  <img src="docs/assets/primitives-zh-light.svg" alt="三个面板，分别说明 choice、score、noul 三个原语各自返回什么" width="660">
</picture>

每个原语下方有两个互不相加的数：先是 `question_types` 记录了有人读过代码、确认调用该原语的行数；再是只有文本信号的行数 —— 每周刷新在该行所引的那一个文件中找到了它的请求或回答结构（`primitives_seen`），这并不表明代码调用了它。见[哪些经过核实](#哪些经过核实哪些没有)。 <sub>(机翻)</sub>

默认输入为文本或结构化 JSON。原生 API 的 Jev 1.13 和 1.14 也支持实验性 [PNG/JPEG 图像](https://docs.typesafe.ai/images)，须发送 `TypeSafe-Danger-Zone-Images: true`；不支持音频和视频。默认每次请求 **64k** token，其中 state 加最长问题最多 **32k**。实验性请求头 `TypeSafe-Danger-Zone-Long-Context: true` 将两项限制均提高到 **262k**，但速度和准确率会降低（见[模型文档](https://docs.typesafe.ai/models)）。输出 token 免费。截至 2026-11-05，原生 `jev-latest` 和 `jev-preview` 都指向 `jev-1.14.0`，目前没有单独的预览版；两个固定版本 ID（`jev-1.14.0`、`jev-1.13.0`）均可用。权重未公开，因此无法本地运行。跨平台差异全表见 [`docs/compatibility.md`](docs/compatibility.md)。 <sub>(机翻)</sub>

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
| [工具选择](#工具选择) · **256** | [意图路由](#意图路由) · **56** |
| [上下文压缩](#上下文压缩) · **42** | [安全闸门](#安全闸门) · **156** |
| [输出校验](#输出校验) · **153** | [重试控制](#重试控制) · **8** |
| [人工升级](#人工升级) · **80** | [模型路由](#模型路由) · **70** |
| [并行扇出](#并行扇出) · **39** | [检索与排序](#检索与排序) · **87** |
| [结构化抽取](#结构化抽取) · **22** | [分类](#分类) · **151** |
| [机器学习特征抽取](#机器学习特征抽取) · **9** | [文档分拣](#文档分拣) · **22** |
| [工单分拣](#工单分拣) · **13** | [内容评分](#内容评分) · **179** |
| [实时推荐](#实时推荐) · **3** | [总览](#总览) · **501** |

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

- **[deep-searcher](https://github.com/zilliztech/deep-searcher)**<br>
  深度研究工具：在 Milvus 等向量数据库中检索私有数据，再用 LLM 推理作答。它的评测把 LLM 自己做出的停止检索决定，与 Jev 就已收集的上下文是否足以作答给出的 noul 相比较，共 100 道题。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★1k+ · zilliztech · `Py` · [调用点](https://github.com/zilliztech/deep-searcher/blob/HEAD/evaluation/jev_stopping/run_full100.py)，2026-09-22 阅读</sub>

  > 只在评测中调用 Jev：在 100 道 2WikiMultiHopQA 题上，用 Jev 的一个 Noul 代替 LLM 自己做出的停止检索决定，并在 evaluation/jev_stopping/README.md 中公布对比结果（召回率、轮数、延迟、成本）。2026-11-05 由 AI 助手把类别从替代品改为基准；维护者尚未亲自阅读该报告。

- **[Convex Coding Evals](https://github.com/convex/convex-evals)**<br>
  Convex 的编程基准新增了决策模型赛道：108 道关于 Convex 知识的选择题，每题四个选项，覆盖其 112 个编程评测中的 90 个。Jev 通过 OpenRouter 的决策端点，以一个 `choice` 回答每道题；语言模型则通过聊天补全接口回答同样的问题。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★100+ · convex · `TS` · `choice` · [调用点](https://github.com/convex/convex-evals/blob/HEAD/runner/decisions/providers.ts)，2026-10-29 模型阅读</sub>

  > 决策赛道有独立的分数和排行榜；README 说明，选对答案并不代表模型能写出可用的 Convex 代码。托管运行固定使用 typesafe/jev-1.13，并采用三种选项排列。本条目由 AI 助手根据发现队列（issue #14）起草，于 2026-10-29 阅读了 README 和所引文件；维护者尚未亲自阅读调用点。

- **[hippo-memory](https://github.com/kitfunso/hippo-memory)**<br>
  受生物启发的智能体记忆：衰减、检索强化与巩固。零运行时依赖，基于 SQLite。 <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★100+ · kitfunso · `TS` · [调用点](https://github.com/kitfunso/hippo-memory/blob/HEAD/src/infra/rerankers/endpoint.ts)，2026-11-05 模型阅读 · 作者结论：好坏参半（作者自述，未经本仓库复现）</sub>

已显示 **10 / 83** 条：先是负面结果，再是精选路径[独立测量报告](https://kydlikebtc.github.io/awesome-jev/?collection=measured&lang=zh)选出的条目，按该路径的顺序，再按列表顺序补上其余条目中靠前的几条 · [在单独页面查看全部 83 条及全部备注 →](docs/measured.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?indep=1&lang=zh) <sub>(机翻)</sub>

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

- **[agent-desktop](https://github.com/vercel-labs/agent-desktop)**<br>
  桌面自动化。读系统无障碍树，判断下一步该点哪个按钮、菜单或输入框。<br>
  <sub>`开源项目` · ★10k+ · `Rs` · `choice` · `noul` · [调用点](https://github.com/vercel-labs/agent-desktop/blob/HEAD/scripts/jev/policy.mjs)，2026-09-24 阅读</sub>

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

已显示 **10 / 256** 条 · [在单独页面查看全部 256 条 →](docs/by-pattern/tool-selection.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=tool-selection&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 意图路由

_判断用户意图，把请求分流到正确的分支。_

- **[TypeSafe AI n8n node](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai)** ⭐<br>
  TypeSafe 官方的 n8n 社区节点。Evaluate 就每个条目向 Jev 提出类型化问题并写入答案；Route 按一个答案把条目送往对应输出，低置信度的选择题可走后备输出，两个是非题阈值之间的可走“不确定”输出。AI Agent 可把它当作工具使用。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★10+ · typesafe-ai · `TS` · `choice` · `noul` · `score` · [调用点](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai/blob/HEAD/nodes/TypeSafeAi/api.ts)，2026-11-04 模型阅读</sub>

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
  <sub>`开源项目` · ★10k+ · `TS` · `choice` · `noul` · [调用点](https://github.com/elie222/inbox-zero/blob/HEAD/apps/web/utils/decision-model/decision-model.ts)，2026-11-05 模型阅读</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br>
  一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。<br>
  <sub>`教程` · ★1k+ · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/daveebbelaar/ai-cookbook/blob/HEAD/models/jev/06-criteria.py)，2026-09-22 阅读</sub>

- **[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)**<br>
  一个 Android 回复副驾：从屏幕文本判断意图、时机和风险，OCR 与文案起草交给另外的模型。<br>
  <sub>`开源项目` · ★1k+ · `Java` · `choice` · `score` · `noul` · [调用点](https://github.com/jev-chat/jev-chat-jarvis/blob/HEAD/cn/app/src/main/java/com/jev/probe/jev/JevQuestions.kt)，2026-09-22 阅读</sub>

- **[Real Python: hello-jev](https://github.com/realpython/materials/tree/master/hello-jev)**<br>
  带对照组的教学示例：同一个问询台任务，一份是只认 Y/N 的纯 Python 写法，旁边是一个能读出意图的 Noul。<br>
  <sub>`教程` · ★1k+ · Real Python · `Py` · `noul` · [调用点](https://github.com/realpython/materials/blob/HEAD/hello-jev/jev_noul.py)，2026-09-22 阅读</sub>

已显示 **10 / 56** 条 · [在单独页面查看全部 56 条 →](docs/by-pattern/intent-routing.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=intent-routing&lang=zh)

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

- **[deepseek-harness-jev (luobosibing2)](https://github.com/luobosibing2/dsh-jev-plugin)**<br>
  DeepSeek Harness 插件，提供 12 项需手动开启的功能，用 Jev 作为判断模型：技能选择和 glob 结果排序（每个候选一个 `noul`）、完成度与目标检查、偏离提醒、插话路由、工具输出和测试日志过滤，以及对单个工作区操作的审批。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★100+ · luobosibing2 · `TS` · `noul` · [调用点](https://github.com/luobosibing2/dsh-jev-plugin/blob/HEAD/packages/jev/src/selection.ts)，2026-10-28 模型阅读</sub>

- **[jev-pruner](https://github.com/tamaratran/jev-pruner)**<br>
  在模型看到之前先修剪冗长的 shell 输出，每个片段问一个 Noul。<br>
  <sub>`插件` · ★100+ · tamaratran · `TS` · `noul` · [调用点](https://github.com/tamaratran/jev-pruner/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[mu](https://github.com/qybaihe/mu)**<br>
  基于 pi 的编程 Agent（命令行和桌面端），在 40 个决策点上问 Jev：工具输出的哪些片段进上下文、哪些过期的工具结果可以丢掉、被规则拦下的命令是不是用户要的、抓取的网页和 MCP 输出里有没有注入的指令。 <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · qybaihe · `TS` · `choice` · `noul` · `score` · [调用点](https://github.com/qybaihe/mu/blob/HEAD/packages/kyrn-judge/src/providers/typesafe.ts)</sub>

  **注意:** `作者自荐`

- **[Quicksilver](https://github.com/UditAkhourii/quicksilver)**<br>
  一个 Claude Code 技能，把“是否相关”的判断交给 Jev：对每个文件、每行日志或每张工单问一个 noul（例如“这些文件里哪些处理鉴权？”），并行询问并按概率排序，于是 Claude 拿到的是带置信度的候选清单，而不必通读全部内容。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★100+ · uditakhourii · `JS` · `noul` · [调用点](https://github.com/UditAkhourii/quicksilver/blob/HEAD/skills/quicksilver/scripts/qs.mjs)，2026-10-24 模型阅读</sub>

已显示 **10 / 42** 条 · [在单独页面查看全部 42 条 →](docs/by-pattern/context-compaction.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=context-compaction&lang=zh)

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

- **[agentgateway: Jev and OpenAI guardrail](https://github.com/agentgateway/agentgateway)**<br>
  对每个请求和每条回复提出三个是非问题（越狱、有害内容、泄露机密），概率达到 0.5 即以 HTTP 403 拒绝，评估出错时同样拦截；网关把一半评估以 Noul 形式发给 Jev，另一半发给 OpenAI。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★1k+ · `Rs` · `noul` · [调用点](https://github.com/agentgateway/agentgateway/blob/HEAD/examples/llm-guardrail-jev-openai/guardrail.ts)，2026-11-05 模型阅读</sub>

- **[DeepChat: agent tool-permission review](https://github.com/ThinkInAIXYZ/deepchat)**<br>
  从三个维度审查每次工具调用：风险等级、用户是否授权、以及一个显式的提示注入压力检查。<br>
  <sub>`开源项目` · ★1k+ · `TS` · `choice` · `noul` · [调用点](https://github.com/ThinkInAIXYZ/deepchat/blob/HEAD/src/shared/jevProtocol.ts)，2026-09-22 阅读</sub>

- **[atomic](https://github.com/bastani-inc/atomic)**<br>
  编程智能体运行时：工作流是带版本的 TypeScript 阶段，包含可执行检查、评审关卡和人工审批。其 AI 包从 models.dev 收录 Jev，作为 5 家提供方上的 System One 决策模型，与聊天模型分开列出；README 没有说明工作流在哪里调用它。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · bastani-inc · `TS` · [调用点](https://github.com/bastani-inc/atomic/blob/HEAD/packages/ai/src/decision-models.generated.ts)，2026-09-24 阅读</sub>

- **[deepseek-harness-jev (luobosibing2)](https://github.com/luobosibing2/dsh-jev-plugin)**<br>
  DeepSeek Harness 插件，提供 12 项需手动开启的功能，用 Jev 作为判断模型：技能选择和 glob 结果排序（每个候选一个 `noul`）、完成度与目标检查、偏离提醒、插话路由、工具输出和测试日志过滤，以及对单个工作区操作的审批。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★100+ · luobosibing2 · `TS` · `noul` · [调用点](https://github.com/luobosibing2/dsh-jev-plugin/blob/HEAD/packages/jev/src/selection.ts)，2026-10-28 模型阅读</sub>

- **[grok-bot-jev](https://github.com/Bodila51/grok-bot-jev)**<br>
  Grok Bot 的路由器：在调研、浏览、重试或启动子智能体之前，先问 Jev 这个请求需要哪种动作：复用已缓存的产物、停止失败的重试、运行确定性代码、限制调研规模、允许子智能体，或请人决定。影子模式只记日志；主动模式要靠粘贴进去的技能来执行。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★100+ · bodila51 · `Py` · [调用点](https://github.com/Bodila51/grok-bot-jev/blob/HEAD/src/jev_client.py)，2026-09-22 阅读</sub>

已显示 **10 / 156** 条 · [在单独页面查看全部 156 条 →](docs/by-pattern/safety-gating.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=safety-gating&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 输出校验

_在输出到达用户前，按评分标准检查模型产出。_

- **[Cookbook: Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check)** ⭐<br>
  用一个 Choice 对着原文核查引用是否错误或凭空编造，并用它的置信度把边缘情况标出来送审。<br>
  <sub>`官方文档` · `Py` · `choice`</sub>

- **[Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails)** ⭐<br>
  用一次请求筛查 LLM 应用的每一条进出消息，既点明风险类型、又给「照做会造成多大危害」打分。<br>
  <sub>`官方文档` · `Py` · `noul` · `score`</sub>

- **[celesto](https://github.com/CelestoAI/celesto)**<br>
  给 AI 智能体的安全持久化计算环境。 <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★1k+ · celestoai · `Py` · [调用点](https://github.com/CelestoAI/celesto/blob/HEAD/examples/pr-review-jev/models.py)，2026-09-22 阅读</sub>

- **[latitude-llm](https://github.com/latitude-dev/latitude-llm)**<br>
  面向 AI 智能体的开源可观测性平台，在调用轨迹里标出智能体出错的地方。其中一个影子提供方问 Jev 每个标记维度一个 noul，一次调用最多 11 个；所引文件看不出这些答案是否会改变任何标记，README 也没有提到 Jev。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★1k+ · latitude-dev · `TS` · [调用点](https://github.com/latitude-dev/latitude-llm/blob/HEAD/packages/platform/ai-jev/src/jev-shadow-decision-provider.ts)，2026-09-22 阅读</sub>

- **[reticle](https://github.com/reticlehq/reticle)**<br>
  通过实际操作正在运行的应用来核实 AI 智能体说的“完成”，给出通过、失败或无法判断。其基准测试框架就采集到的证据用一次调用问 Jev：五个 noul（预期结果是否发生、采集是否干净、应用是否报错等）、一个通过／失败／未知的 choice，以及一个严重程度 score。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★1k+ · reticlehq · `TS` · [调用点](https://github.com/reticlehq/reticle/blob/HEAD/bench/harness/jev.mjs)，2026-09-24 阅读</sub>

- **[abide](https://github.com/coldteadotai/abide)**<br>
  接入 Claude Code、Codex、OpenCode 和 Pi，在每次编辑或每一轮，就 AGENTS.md 或 CLAUDE.md 中的每条规则问 Jev 一个是非题，只给它看规则和 diff；违反的规则会退回给智能体修改。在 93 个回放的会话中，Jev 标出了 39 次编辑，其中 10 次经审阅者确认。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★100+ · coldteadotai · `TS` · [调用点](https://github.com/coldteadotai/abide/blob/HEAD/packages/cli/src/lib/jev.ts)，2026-09-24 阅读</sub>

- **[arc-cua](https://github.com/shhivv/arc-cua)**<br>
  面向计算机操作智能体的 macOS 动作循环：规划方交出一个有边界的桌面子任务，Jev 以 `choice` 问题从窗口实际提供的元素中选出下一步界面操作及其目标，并对每条成功标准再问一个 `choice`；字面文本只来自规划方。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · shhivv · `Py` · `choice` · [调用点](https://github.com/shhivv/arc-cua/blob/HEAD/src/arc_cua/policies/typesafe.py)，2026-10-29 模型阅读</sub>

- **[atomic](https://github.com/bastani-inc/atomic)**<br>
  编程智能体运行时：工作流是带版本的 TypeScript 阶段，包含可执行检查、评审关卡和人工审批。其 AI 包从 models.dev 收录 Jev，作为 5 家提供方上的 System One 决策模型，与聊天模型分开列出；README 没有说明工作流在哪里调用它。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · bastani-inc · `TS` · [调用点](https://github.com/bastani-inc/atomic/blob/HEAD/packages/ai/src/decision-models.generated.ts)，2026-09-24 阅读</sub>

- **[Canny](https://github.com/qkal/Canny)**<br>
  防 Coding Agent 嘴硬说自己做完了。看工具输出、代码 diff 和测试结果，再判断完成声明靠不靠谱。<br>
  <sub>`开源项目` · ★100+ · `TS` · `noul` · `score` · [调用点](https://github.com/qkal/Canny/blob/HEAD/src/jev.ts)，2026-09-22 阅读</sub>

- **[deepseek-harness-jev (luobosibing2)](https://github.com/luobosibing2/dsh-jev-plugin)**<br>
  DeepSeek Harness 插件，提供 12 项需手动开启的功能，用 Jev 作为判断模型：技能选择和 glob 结果排序（每个候选一个 `noul`）、完成度与目标检查、偏离提醒、插话路由、工具输出和测试日志过滤，以及对单个工作区操作的审批。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★100+ · luobosibing2 · `TS` · `noul` · [调用点](https://github.com/luobosibing2/dsh-jev-plugin/blob/HEAD/packages/jev/src/selection.ts)，2026-10-28 模型阅读</sub>

已显示 **10 / 153** 条 · [在单独页面查看全部 153 条 →](docs/by-pattern/output-validation.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=output-validation&lang=zh)

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

- **[TypeSafe AI n8n node](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai)** ⭐<br>
  TypeSafe 官方的 n8n 社区节点。Evaluate 就每个条目向 Jev 提出类型化问题并写入答案；Route 按一个答案把条目送往对应输出，低置信度的选择题可走后备输出，两个是非题阈值之间的可走“不确定”输出。AI Agent 可把它当作工具使用。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★10+ · typesafe-ai · `TS` · `choice` · `noul` · `score` · [调用点](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai/blob/HEAD/nodes/TypeSafeAi/api.ts)，2026-11-04 模型阅读</sub>

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

已显示 **10 / 80** 条 · [在单独页面查看全部 80 条 →](docs/by-pattern/human-escalation.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=human-escalation&lang=zh)

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

- **[oh-my-pi](https://github.com/can1357/oh-my-pi)**<br>
  深度整合 IDE 的编程智能体。 <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10k+ · can1357 · `TS` · [调用点](https://github.com/can1357/oh-my-pi/blob/HEAD/packages/ai/src/judgment/native.ts)，2026-11-05 模型阅读</sub>

- **[openwork](https://github.com/different-ai/openwork)**<br>
  Claude Cowork 的开源替代品，基于 opencode 构建。它的网关在 Auto 路由中为每个 Smart Router 任务向 Jev 提一个 Score 问题，再为思考强度提一个，然后按回答路由提示；没有 TypeSafe 密钥时走后备路由。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10k+ · different-ai · `TS` · `score` · [调用点](https://github.com/different-ai/openwork/blob/HEAD/ee/apps/gateway/src/auto-router/jev.ts)，2026-11-05 模型阅读</sub>

- **[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br>
  九个 agent 技能加一个 CLI，覆盖模型路由、记忆过滤、对话轮保留、多选一技能选择和下一步动作决策。<br>
  <sub>`插件` · ★1k+ · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/kerpopule/hermes-jev-skills/blob/HEAD/jevkit/client.py)，2026-09-22 阅读</sub>

  **注意:** `实测后未采用`

- **[Astra-Ares](https://github.com/miuuyy/Astra-Ares)**<br>
  运行一个打过补丁的 Codex CLI：Jev 读取有限的任务上下文，用两个 choice 选出 GPT-6 下一次回复的推理力度，以及这个力度持续几次回复（1、2、5 或 10）；GPT-6 改变推理力度不会破坏提示缓存。属于实验性的参考实现。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★100+ · miuuyy · `JS` · [调用点](https://github.com/miuuyy/Astra-Ares/blob/HEAD/src/jev.mjs)，2026-09-24 阅读</sub>

- **[distill](https://github.com/samuelfaj/distill)**<br>
  面向 Grok、Codex 订阅及任何兼容 OpenAI 协议的模型的编程智能体 harness 和 TUI，目标是少花 token。模型档位的推理力度保持默认的 auto 时，由 Jev 为每次调用挑选推理力度；客户端默认经 OpenRouter 调用 Jev。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · samuelfaj · `Rs` · [调用点](https://github.com/samuelfaj/distill/blob/HEAD/crates/codegen/distill-workspace/src/jev/client.rs)，2026-09-22 阅读</sub>

- **[jev-codex-router](https://github.com/0xNatoshi/jev-codex-router)**<br>
  先让 Jev 判断这一轮编程任务有多难，再决定模型档位、推理深度和速度模式。<br>
  <sub>`插件` · ★100+ · `JS` · `choice` · `score` · [调用点](https://github.com/0xNatoshi/jev-codex-router/blob/HEAD/server/jev_server.py)，2026-09-22 阅读</sub>

  **注意:** `已归档`

已显示 **10 / 70** 条 · [在单独页面查看全部 70 条 →](docs/by-pattern/model-routing.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=model-routing&lang=zh)

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

- **[Hey Jev](https://github.com/henryklunaris/hey-jev)**<br>
  macOS 语音助手：本地 Whisper 转写指令后，一次 Jev 请求同时问完所有问题（请求类别、是否复合、目标、应用、动作、音量级别），题型有 `choice`、`noul` 和 `score`；代码通过 AppleScript 执行动作，只有常识性问题才交给 LLM。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · henryklunaris · `Py` · `choice` · `noul` · `score` · [调用点](https://github.com/henryklunaris/hey-jev/blob/HEAD/siri.py)，2026-10-29 模型阅读</sub>

  **注意:** `无许可证` · `需第三方密钥`

- **[jev-chat-windows](https://github.com/jev-chat/jev-chat-windows)**<br>
  微信（Windows）旁挂回复辅助：截图加本地 OCR 读消息，Jev 判断意图，生成候选，发送永远手动。 <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★100+ · jev-chat · `Py` · [调用点](https://github.com/jev-chat/jev-chat-windows/blob/HEAD/core/jev_client.py)，2026-09-22 阅读</sub>

- **[jev-chat: a tool-calling chatbot with no LLM](https://github.com/w3cj/jev-chat)**<br>
  一个完全不含语言模型的 tool calling 聊天机器人：一次请求同时问清请求类型、该调哪个工具、以及每个工具的参数。<br>
  <sub>`开源项目` · ★100+ · `TS` · `choice` · `noul` · [调用点](https://github.com/w3cj/jev-chat/blob/HEAD/apps/server/src/jev/client.ts)，2026-09-22 阅读</sub>

已显示 **10 / 39** 条 · [在单独页面查看全部 39 条 →](docs/by-pattern/fan-out.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=fan-out&lang=zh)

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

- **[oh-my-pi](https://github.com/can1357/oh-my-pi)**<br>
  深度整合 IDE 的编程智能体。 <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10k+ · can1357 · `TS` · [调用点](https://github.com/can1357/oh-my-pi/blob/HEAD/packages/ai/src/judgment/native.ts)，2026-11-05 模型阅读</sub>

- **[OpenViking: retrieval reranking](https://github.com/volcengine/OpenViking)**<br>
  单次批量请求里对每个候选文档问一个 Noul，直接把「是」的概率当相关性分数。<br>
  <sub>`开源项目` · ★10k+ · `Py` · `noul` · [调用点](https://github.com/volcengine/OpenViking/blob/HEAD/openviking/models/rerank/jev_rerank.py)，2026-09-22 阅读</sub>

- **[XERJ](https://github.com/xerj-org/xerj)**<br>
  一个本地优先的搜索引擎兼 MCP 服务器，打包为单个 Rust 二进制文件。可选的 `rerank` 阶段对每条靠前结果向 Jev 提一个 `noul`（`document` 是否回答了 state 中的查询？），再按概率重新排序。作者报告 FiQA 上的 nDCG@10 从 0.24 升至 0.36，总共 648 次搜索花费约 0.64 美元。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10k+ · xerj-org · `Rs` · `noul` · [调用点](https://github.com/xerj-org/xerj/blob/HEAD/engine/crates/xerj-rerank/src/lib.rs)，2026-10-26 模型阅读</sub>

  **注意:** `厂商自报数据`

已显示 **10 / 87** 条 · [在单独页面查看全部 87 条 →](docs/by-pattern/search-ranking.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=search-ranking&lang=zh)

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

- **[jev playground (deepdave98)](https://github.com/deepdave98/jev-playground)**<br>
  每周一个的市场销售（GTM）实验，均用 Jev 完成并与 Claude 对比：线索分拣和路由、交易风险、回复分拣、从通话摘要中提取 MEDDPICC 字段、重复账户识别、已流失交易的重新激活，另有一个 MCP 服务器。共享客户端在取整前减去实测的 0.30 分数偏差。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · deepdave98 · `Py` · `noul` · `choice` · `score` · [调用点](https://github.com/deepdave98/jev-playground/blob/HEAD/common/jev.py)，2026-10-31 模型阅读</sub>

  **注意:** `无许可证`

- **[jev-apply](https://github.com/theadaply/jev-apply)**<br>
  面向命令行智能体的求职申请技能，会记住你的答案：Jev 为 Greenhouse、Ashby 或 Lever 表单的每个字段挑选合适的已存答案，并始终提供“都不合适”的出口；置信度低于阈值时，该字段交回给你，而不是去猜。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`插件` · ★10+ · theadaply · `JS` · `choice` · `noul` · [调用点](https://github.com/theadaply/jev-apply/blob/HEAD/src/jev/client.mjs)，2026-11-03 模型阅读</sub>

- **[jev-design](https://github.com/bilune/jev-design)**<br>
  让 Jev 设计仪表盘的实验：根据一句话的设计要求（例如“一本 18 世纪的印刷书”），分两轮发出 choice、score 和是非题，从人工编写的目录中选出每一个视觉参数（颜色、字体、圆角、图标），再由引擎把它们应用到一个 Next.js 控制台上。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10+ · bilune · `TS` · `choice` · `score` · `noul` · [调用点](https://github.com/bilune/jev-design/blob/HEAD/src/design/jev/generate.ts)，2026-10-30 模型阅读</sub>

  **注意:** `无许可证`

- **[jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop)**<br>
  面向 Apple 芯片上原生 macOS 应用的 computer use 智能体：由 OmniParser CoreML、Apple Vision OCR 和辅助功能标签在本机找出窗口里的控件，再由 Jev 根据观察到的文字（从不看像素）用 choice 选下一步动作。输入前有防护检查，基准测试核对的是实际结果，而不是 Jev 的 DONE 判断。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10+ · jcpsimmons · `JS` · [调用点](https://github.com/jcpsimmons/jev-macos-loop/blob/HEAD/src/providers.mjs)，2026-09-22 阅读</sub>

- **[jeveryword](https://github.com/jkrup/jeveryword)**<br>
  用 Jev 做文本抽取：字段抽取、PII 检测与逐字引文。 <sub>(项目自述)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10+ · jkrup · `JS` · [调用点](https://github.com/jkrup/jeveryword/blob/HEAD/src/client.mjs)，2026-09-22 阅读</sub>

已显示 **10 / 22** 条 · [在单独页面查看全部 22 条 →](docs/by-pattern/data-extraction.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=data-extraction&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 分类

_把条目归入分类体系，包括用概率遍历的深层层级。_

- **[WorkflowEvals](https://github.com/typesafe-ai/workflowevals)** ⭐<br>
  TypeSafe 用于复现其 WorkflowEvals 评测网站的代码：四个业务流程（发票审批与欺诈分拣、客服路由与处置、智能体运行中的动作选择、安全告警分拣），共 705 个案例，以 OpenAI、Anthropic 及共识结果为参考来评分。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · typesafe-ai · `Py` · `noul` · `choice` · `score` · [调用点](https://github.com/typesafe-ai/workflowevals/blob/HEAD/core/clients.py)，2026-11-02 模型阅读</sub>

  **注意:** `仅一次提交` · `厂商自报数据`

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
  <sub>`开源项目` · ★10k+ · `TS` · `choice` · `noul` · [调用点](https://github.com/elie222/inbox-zero/blob/HEAD/apps/web/utils/decision-model/decision-model.ts)，2026-11-05 模型阅读</sub>

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

已显示 **10 / 151** 条 · [在单独页面查看全部 151 条 →](docs/by-pattern/classification.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=classification&lang=zh)

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

- **[Truffler](https://github.com/kieranklaassen/truffler)**<br>
  面向 Rails 应用的意图搜索：每当记录被保存，Truffler 就向 Jev 提出为它声明的是非题、choice 和 score 问题，并把每个答案存成数值，使记录形成按名称分维的嵌入，搜索时按意图加权。用户需要时，Jev 还会把靠前结果重排为“很可能”“可能”“不太可能”三档。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`平台集成` · ★10+ · kieranklaassen · `Rb` · `noul` · `choice` · `score` · [调用点](https://github.com/kieranklaassen/truffler/blob/HEAD/lib/truffler/questions.rb)，2026-10-30 模型阅读</sub>

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

- **[WorkflowEvals](https://github.com/typesafe-ai/workflowevals)** ⭐<br>
  TypeSafe 用于复现其 WorkflowEvals 评测网站的代码：四个业务流程（发票审批与欺诈分拣、客服路由与处置、智能体运行中的动作选择、安全告警分拣），共 705 个案例，以 OpenAI、Anthropic 及共识结果为参考来评分。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`基准测试` · ★10+ · typesafe-ai · `Py` · `noul` · `choice` · `score` · [调用点](https://github.com/typesafe-ai/workflowevals/blob/HEAD/core/clients.py)，2026-11-02 模型阅读</sub>

  **注意:** `仅一次提交` · `厂商自报数据`

- **[Quickstart](https://docs.typesafe.ai/introduction/quickstart)** ⭐<br>
  官方第一课：一条工单，一次请求里同时问一个 Choice、一个 Score 和一个 Noul，给了 Python / JS / cURL 三种写法。<br>
  <sub>`官方文档` · `Py` · `TS` · `sh` · `choice` · `score` · `noul`</sub>

- **[ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook)**<br>
  一套循序渐进的课程：从第一次调用、逐个原语、state 形状与 criteria，一直到工单分拣和多步工作流，并对应了全部四个官方模式。<br>
  <sub>`教程` · ★1k+ · `Py` · `choice` · `score` · `noul` · [调用点](https://github.com/daveebbelaar/ai-cookbook/blob/HEAD/models/jev/06-criteria.py)，2026-09-22 阅读</sub>

- **[jev-demo](https://github.com/soyjorgepilo/jev-demo)**<br>
  三个西班牙语演示，展示同一模式：Jev 决策、代码执行。Jira 工单分诊，按结果直接应用、标记复核或升级；预检扫描先标出有问题的函数，再只让 Claude 解释这些函数；PR 路由把每个 pull request 分给规则、Haiku 或 Sonnet。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10+ · soyjorgepilo · `TS` · `choice` · `noul` · `score` · [调用点](https://github.com/soyjorgepilo/jev-demo/blob/HEAD/shared/jev.ts)，2026-11-04 模型阅读</sub>

  **注意:** `仅一次提交` · `无许可证` · `需第三方密钥`

- **[jevelry](https://github.com/backant-io/jevelry)**<br>
  命令行、终端界面和库，把给 Jev 的问题写成名为 jevel 的小文件；自带十七个，覆盖工单、issue、pull request、日志、告警和失败的测试。每个答案的确定程度被转换为执行、标记给人看或回退，所有决策都会记录，以便按实际结果调整阈值。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10+ · backant-io · `TS` · `choice` · `noul` · `score` · [调用点](https://github.com/backant-io/jevelry/blob/HEAD/src/ask.ts)，2026-11-04 模型阅读</sub>

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

已显示 **10 / 13** 条 · [在单独页面查看全部 13 条 →](docs/by-pattern/support-triage.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=support-triage&lang=zh)

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

已显示 **10 / 179** 条 · [在单独页面查看全部 179 条 →](docs/by-pattern/content-scoring.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=content-scoring&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 实时推荐

_选择下一步呈现什么，快到能用在实时会话里。_

- **[jev-linkmap](https://github.com/stas4000/jev-linkmap)**<br>
  重建网站的内部链接：代码抓取整站，为每个页面挑出 15 个相似页面以及正文中现成可用作锚文本的短语，然后每个页面向 Jev 发一次请求，针对每个目标询问是否应该链接（是非题）以及用哪个短语作锚文本（choice）。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · ★10+ · stas4000 · `Py` · `noul` · `choice` · [调用点](https://github.com/stas4000/jev-linkmap/blob/HEAD/jev_linkmap/jev.py)，2026-11-01 模型阅读</sub>

- **[1 Million Emojis](https://github.com/cwdx/1-million-emojis)**<br>
  一块 1,000 × 1,000 的共享表情画布，Jev 和人一起作画：每一笔之后发一次请求，用 choice 从“表情加位置”的选项里挑一个，再用 noul 判断这一笔是否还没画完；先走 Vercel AI Gateway，TypeSafe 直连作为后备。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · cwdx · `TS` · `choice` · `noul` · [调用点](https://github.com/cwdx/1-million-emojis/blob/HEAD/packages/jev/src/index.ts)，2026-10-24 模型阅读</sub>

  **注意:** `作者自荐`

- **[Jevflix](https://github.com/ArielBubis/Jevflix)**<br>
  电影推荐器：FAISS 与 BM25 检索把 4,800 部电影缩成短名单，Jev 读出请求里的约束（片长、不要血腥画面）供代码过滤，再由一次覆盖最多 250 个候选的 Jev choice 选出一部影片。没有把握时，由 LLM 权衡前五名或追问一个问题。 <sub>(模型撰写)</sub> <sub>(机翻)</sub><br>
  <sub>`开源项目` · arielbubis · `Py` · [调用点](https://github.com/ArielBubis/Jevflix/blob/HEAD/movie_rec/jev_client.py)，2026-09-24 阅读</sub>

已显示全部 3 条 · [单独页面](docs/by-pattern/recommendation.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=recommendation&lang=zh)

<sub>[↑ 场景索引](#pattern-index)</sub>

### 总览

_介绍模型或整个领域，而非单一模式。_

- **[Official agent skill for Claude Code](https://docs.typesafe.ai/agent-skill)** ⭐<br>
  把 TypeSafe 官方技能装进 Claude Code，让智能体自己写出正确的 Jev 调用，不必每次手动贴 API 结构。<br>
  <sub>`官方文档` · ★1k+ · `sh`</sub>

- **[typesafe-ai/skills](https://github.com/typesafe-ai/skills)** ⭐<br>
  Claude Code 插件背后的官方技能仓库，里面的 SKILL.md 教会智能体如何使用 System One API。<br>
  <sub>`插件` · ★1k+ · `sh`</sub>

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

已显示 **10 / 501** 条 · [在单独页面查看全部 501 条 →](docs/by-pattern/overview.zh-CN.md) · [在站点上筛选](https://kydlikebtc.github.io/awesome-jev/?p=overview&lang=zh)

#### 尚未按模式索引

其中 **232** 行是带代码的项目或插件。`overview` 也是关键词规则无法归类时给出的默认值，而这些行没有任何人对照决策模式阅读过的记录（`patterns_reviewed`），因此单独列出：见 [Overview 页面末尾](docs/by-pattern/overview.zh-CN.md#unindexed)、[站点](https://kydlikebtc.github.io/awesome-jev/?p=overview&lang=zh)，以及附有规则建议的[复核队列](docs/review-queue.md#unsorted-overview)。 <sub>(机翻)</sub>

<sub>[↑ 场景索引](#pattern-index)</sub>

## 按资源形态

同样这些行，按你点开链接后会看到什么来分组。

| 形态 | 例子数 | 点开会看到 |
| --- | ---: | --- |
| **官方文档** | **31** | 厂商文档、cookbook 与模式页。 |
| **SDK** | **103** | 客户端库，官方与社区。 |
| **平台集成** | **38** | 接入模型的网关、框架或平台路径。 |
| **代码片段** | **4** | 本仓库内的小型可运行样例。 |
| **开源项目** | **721** | 真正在调用 Jev 的应用或库。 |
| **插件** | **273** | 可安装的编辑器、智能体、MCP 集成。 |
| **教程** | **17** | 带代码的分步教学材料。 |
| **基准测试** | **82** | 实测。注意区分独立实测与厂商自报。 |
| **文章** | **14** | 讲解、分析与发布报道。 |
| **视频** | **3** | 演示与评测。 |
| **讨论** | **2** | 值得读的讨论，包括质疑的声音。 |
| **Jev 替代实现** | **105** | 独立复现实现。它们**不**调用 Jev。 |

## 本仓库还有什么

除目录数据之外的部分。

<details>
<summary><b>查看可搜索站点预览</b></summary>

<a href="https://kydlikebtc.github.io/awesome-jev/?lang=zh"><img src="https://kydlikebtc.github.io/awesome-jev/img/site-zh.png?v=24cf55c4cfeb5f80" alt="可搜索的 Jev 目录：精选路径、筛选排序、带日期的来源证据与条目卡片" width="760"></a>

<sub>点击条形即可筛选。另有两个视图：<a href="https://kydlikebtc.github.io/awesome-jev/?view=prims&lang=zh">三个原语</a> · <a href="https://kydlikebtc.github.io/awesome-jev/?view=compat&lang=zh">兼容性矩阵</a>。每个筛选条件和每个条目都是可分享的 URL。也有静态页面：<a href="https://kydlikebtc.github.io/awesome-jev/patterns/">每个模式一页</a> · <a href="https://kydlikebtc.github.io/awesome-jev/new.zh.html">每周新增与退役</a>（<a href="https://kydlikebtc.github.io/awesome-jev/feed.zh.xml">Atom 订阅</a>）。有代码的产品还可以上<a href="https://kydlikebtc.github.io/awesome-jev/launches.zh.html">每周发布榜</a>（<a href="docs/launches.zh-CN.md">规则说明</a>）。</sub>

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

- **链接检查** —— 有 1363 行记录了 HTTP 2xx 响应和 `checked` 日期，另有 30 行没有带日期的成功记录。检查日期因条目而异，过去成功不保证今天仍可访问。star 数和许可证也是仓库元数据的快照。

- **来源与代码阅读** —— `evidence.path` 指向所读文件，`evidence.read_on` 记录声明的阅读日期，`evidence.model_read_on` 记录模型的阅读、单独显示，`evidence_none` 解释缺少文件证据的原因。阅读调用点与运行代码是两件事。摘要包含源项目描述与机翻，详见[方法与局限](docs/method.md)。 <sub>(机翻)</sub>

- **摘要是谁的文字** —— 746 条摘要的英文原文就是被链接项目自己在 GitHub 上的描述，逐字相同，这些行标为 *(项目自述)*；29 条标为 *(项目旧自述)*：英文取自项目描述，但两者已不再相同。这些文字出自项目作者，中文摘要是其译文。11 条摘要标明由人为本目录撰写，293 条由模型为本目录撰写并标为 *(模型撰写)*，314 条未作记录。每周刷新会把每条英文摘要与其仓库描述比对并标出相同者；只有人才能把摘要标为人写的。 <sub>(机翻)</sub>

- **中文是谁写的** —— 1393 行中有 191 行的中文摘要由人撰写；其余 1202 行由模型翻译，带有 `zh_machine`，并在中文 README、中文模式页面和站点的中文视图中逐条标为 *(机翻)*。[翻译队列](docs/zh-queue.md)列出等待有人替换的机翻：先是星标最高各行的全部机翻，再按星标从高到低列出被脚本计算的三项文本信号（比英文短得多、缺少英文里的数字、大部分是 ASCII 字符）中至少一项标出的其他机翻。信号只是对照比较，不是对译文的结论，README、模式页面和站点上的各行都不显示信号。认领方法见[认领翻译](CONTRIBUTING.md#claim-a-translation)；只有你自己写的译文才能去掉 `zh_machine`。 <sub>(机翻)</sub>

- **调用点文本复查** —— 有 1206 行通过 `evidence` 记录了项目调用 Jev 的文件及其中匹配的字符串。另有 101 行记录的文件只表明项目采用了 Jev 的请求结构、并非基于 Jev 构建（所有 `alternative`——无论是自己提供这种结构，还是向 Jev 发送同样的请求作对比——以及由其他模型支撑的适配器），1 行记录的只是项目附带的示例；`evidence.kind` 标明属于哪一种。每周 [claims 任务](https://github.com/kydlikebtc/awesome-jev/actions/workflows/claims.yml) 检查这些字符串是否仍在默认分支，发现文本或文件缺失时报告。这些数字是已记录的证据数量，**不是最新 CI 通过数**。文本匹配不能证明调用实际执行、API 兼容或结果正确。脚本标出、需要人重读的引用列在[复核队列](docs/review-queue.md)。 <sub>(机翻)</sub>

- **用了哪些原语** —— 有 109 行在 `question_types` 中记录了有人读代码时确认调用的原语；另有 137 行记录的是模型读代码时确认的原语，这些行的调用点只有模型读过（`evidence.model_read_on`）。此外还有 749 行带 `primitives_seen`，这是机器文本信号：每周刷新在该行所引的那一个文件中找到了某个原语的请求或回答结构（`"type": "choice"`、`Noul(`、`.noul`）。文件里出现这种结构不等于调用；其中 618 行没有 `question_types`，这个信号就是关于它们所用原语的全部记录。本目录的筛选、计数和规则都不会把它当作原语声明。 <sub>(机翻)</sub>

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
| eliza | 2026-11-05 退役：本条目所引的 TypeSafe 服务已删除，默认分支（develop）上已没有任何文件调用 Jev 或提到 TypeSafe（2026-11-05 搜索）；自 2026-10-06 起每周检查都未通过。保留于此，以便这条引用仍可检索。 |
| jev-atlas | 2026-09-24 退役：仓库在 API 和网页上都返回 404，而作者账号仍然存在 —— 已删除或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| jev-block-android-ad | 2026-11-05 退役：该应用现在用设备上的 Laya 模型分类消息；其 README（2026-10-16）写明已删除 TypeSafe 后端、Jev API 设置和 API Key，默认分支上也已没有任何文件调用 Jev（2026-11-05 搜索）。保留于此，以便这条引用仍可检索。 |
| jev-browse | 2026-11-05 退役：自 2026-10-26 起每周检查都无法访问该仓库（最近一次为 2026-11-04）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| jev-curate | 2026-10-24 退役：自 2026-10-13 起每周刷新都无法访问该仓库（最近一次为 2026-10-21）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| jev-git | 2026-10-24 退役：自 2026-10-13 起每周刷新都无法访问该仓库（最近一次为 2026-10-21）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| jev-mac-voice | 2026-09-24 退役：仓库在 API 和网页上都返回 404，而作者账号仍然存在 —— 已删除或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| jev-reviewer | 2026-10-29 退役：自 2026-10-19 起每周检查都无法访问该仓库（最近一次为 2026-10-28）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
| jev-runtime-security | 2026-11-05 退役：自 2026-10-26 起每周检查都无法访问该仓库（最近一次为 2026-11-04）—— 已删除、改名且无跳转，或转为私有。保留于此，以便这条引用仍可检索。 `HTTP 404` |
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
| [`catalog.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/catalog.json) | 1393 条目 |
| [`retired.json`](https://raw.githubusercontent.com/kydlikebtc/awesome-jev/main/retired.json) | 19 已退休 |
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

**awesome-jev 发布榜** · 建在 Jev 决策图谱之上 · [↑ 返回顶部](#top) · [English](README.md)
