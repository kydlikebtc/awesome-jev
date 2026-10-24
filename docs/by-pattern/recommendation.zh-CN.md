# 实时推荐

<sub>[awesome-jev](../../README.zh-CN.md) · [English](recommendation.md)</sub>

_选择下一步呈现什么，快到能用在实时会话里。_

这个决策的全部已收录例子 —— 共 2 条。同样这些行及其警示也在[索引](../../README.zh-CN.md#实时推荐)里；[站点](https://kydlikebtc.github.io/awesome-jev/?p=recommendation&lang=zh)还能按语言、原语和形态进一步筛选。

这个决策的设计说明见 [docs/patterns.zh-CN.md](../patterns.zh-CN.md#recommendation)：它决定什么、用哪种原语来建模，以及（凡写了的）什么时候不该用决策模型。那一页由模型从[英文版](../patterns.md#recommendation)译写，以英文版为准。 <sub>(机翻)</sub>

本模式各行记录的证据（只是计数，不是结论；一行可能计入多项）：官方文档 0 · 调用点 2 · 接口形态 0 · 仅示例 0 · 独立报告 0 · 负面结果 0 · 未引用文件 0。“独立”指未标 vendor-reported 的基准测试，未经本仓库复现。[各模式并排对照](../shape.zh-CN.md#按决策模式看证据)。 <sub>(机翻)</sub>

## 官方材料

目录里没有归在这个模式下的 TypeSafe AI 官方材料。 <sub>(机翻)</sub>

## 本仓库的示例

本仓库没有这个模式的示例；已有的示例见 [`examples/`](../../examples/)。 <sub>(机翻)</sub>

## 完整列表

★ 以区间给出仓库的 GitHub star 数 —— ★10+、★100+、★1k+、★10k+、★100k+；没有仓库或不足 10 星的行不标区间。排序：官方优先，其次是含代码的，再按区间，最后按标题。区间只反映热度，不代表质量；最近一次从 GitHub 读到的精确数字在 [`catalog.json`](../../catalog.json) 和[站点](https://kydlikebtc.github.io/awesome-jev/?lang=zh)上。 <sub>(机翻)</sub>

*调用点*链接打开该行引用的那一个文件（`evidence.path`）在仓库默认分支 `HEAD` 上的版本；其后的日期是有人最近一次阅读该文件的日期（`evidence.read_on`）；注明“模型阅读”的，则是模型阅读该文件的日期（`evidence.model_read_on`）：这是阅读记录，不是运行过代码。*引用文件*链接同理，只是该文件表明项目采用了 Jev 的请求结构、并非基于 Jev 构建，或只是项目附带的示例（`evidence.kind`）。两种链接都没有固定到某个提交，打开的是文件的当前版本，可能与当时读到的不同；文件移动后链接就会失效，每周的 claims 检查会报告这种情况。 <sub>(机翻)</sub>

- **[1 Million Emojis](https://github.com/cwdx/1-million-emojis)** — 一块 1,000 × 1,000 的共享表情画布，Jev 和人一起作画：每一笔之后发一次请求，用 choice 从“表情加位置”的选项里挑一个，再用 noul 判断这一笔是否还没画完；先走 Vercel AI Gateway，TypeSafe 直连作为后备。 <sub>(模型撰写)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · cwdx · `TS` · `choice` · `noul` · 调用点 [`packages/jev/src/index.ts`](https://github.com/cwdx/1-million-emojis/blob/HEAD/packages/jev/src/index.ts)，2026-10-24 模型阅读</sub>

- **[Jevflix](https://github.com/ArielBubis/Jevflix)** — Jev 来挑，你来看。一个混合电影推荐器：快速的语义加关键词检索把 4,800 部电影缩小成短名单，再由 TypeSafe Jev 读懂你的请求并挑选。 <sub>(项目自述)</sub> <sub>(机翻)</sub>
  <sub>`开源项目` · arielbubis · `Py` · 调用点 [`movie_rec/jev_client.py`](https://github.com/ArielBubis/Jevflix/blob/HEAD/movie_rec/jev_client.py)，2026-09-24 阅读</sub>

---

<sub>由 `scripts/build_readme.py` 从 `catalog.json` 生成。请修改目录，不要改这个文件。</sub>
