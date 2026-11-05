# 发布榜

[English](launches.md)

目录收录能找到的所有 Jev 公开示例。发布榜是叠在目录之上的一层，只面向产品：每周由产品的 Maker 发布，大家投票，周末收榜排名。它回答的是"这周大家用 Jev 做了什么，大家怎么看"。

每个 Launch 旁边并排放着两样东西，二者从不相加：

- **票数**：有多少人关心，按下面的规则计票。
- **证据**：产品是否真的调用 Jev，谁读过那段代码。和目录里每一行记录的是同一份证据。

名次只是票数的排序，不是本目录的推荐。这里的一切都与 TypeSafe AI 无关。

榜单页面在站点上：[发布榜](https://kydlikebtc.github.io/awesome-jev/launches.zh.html)（[English](https://kydlikebtc.github.io/awesome-jev/launches.html)），每个产品一页（`products/<slug>.html`），每位 Maker 一页（`makers/<login>.html`），每个已收榜的周一页（`weeks/<week>.html`）。下面的规则都写在代码里：[`scripts/launches.py`](../scripts/launches.py)。

发布产品请用 [Launch a product](https://github.com/kydlikebtc/awesome-jev/issues/new?template=launch.yml) 表单，或者点产品页上的"发布它"，产品会自动填好。

## 进度

| 阶段 | 加了什么 | 状态 |
| --- | --- | --- |
| 产品页和 Maker 页 | 每个产品、每位 Maker 一页；榜单列出每周新收录的产品 | 已完成（2026-11-03） |
| 读取投票 | [`launch-votes.yml`](../.github/workflows/launch-votes.yml) 手动运行，读取一个 Discussion 上的点赞 | 已完成（2026-11-03）；当天在测试帖上读到了投票 |
| 开放发布 | 发布表单和自动检查、每个 Launch 一个投票帖、周一收榜、周榜页和徽章 | 已完成（2026-11-03）；当天已开启 Discussions 并建好 `Launches` 分类 |
| 给 Agent 用 | MCP 服务器的 `launch_board`、`top_launches` 工具，站点上的 [`api/v1/launches.json`](https://kydlikebtc.github.io/awesome-jev/api/v1/launches.json) | 已完成（2026-11-03） |
| 每周结果订阅 | 每个已收榜的周一条 Atom：[`launches.zh.xml`](https://kydlikebtc.github.io/awesome-jev/launches.zh.xml)（[English](https://kydlikebtc.github.io/awesome-jev/launches.xml)） | 已完成（2026-11-03） |
| 不等合并就排期 | [`launch-collect.yml`](../.github/workflows/launch-collect.yml) 每周五一早把下周的 Launch 写好并推到 `main` | 已完成（2026-11-04） |
| 通知每个 Launch | 周一在每个 Launch 的 issue 上贴出投票帖链接并关闭 issue；收榜时贴出结果，前三名附上徽章代码 | 已完成（2026-11-04） |
| 产品页一键操作 | 每个产品页上的"发布它"和"这是你做的？"会打开发布表单和 confirm-entry 表单，产品已填好；榜单上的新产品也有"发布它" | 已完成（2026-11-04） |
| 指标 | 每个已收榜的周记录有多少账号投票、多少是回头的，每个 Launch 记录开榜时谁读过调用点（[见下文](#榜单怎么衡量)） | 已完成（2026-11-04） |
| 上升最快 | 最近两次每周刷新之间 GitHub 星标涨得最快的产品，显示在榜单上；月报列出当月的（[见下文](#上升最快)） | 已完成（2026-11-04） |
| 每个产品一枚徽章 | 放进产品 README 的一行，图片依次显示已收录、正在发布、进过前三的名次；每个产品页都给出这一行（[见下文](#readme-徽章)） | 已完成（2026-11-04） |
| 链接预览 | 每个产品页、Maker 页、周榜页和榜单页都指定了站点的预览卡片，链接分享到哪里都会显示卡片 | 已完成（2026-11-04） |
| 不再等人 | 发布检查和收榜原来要等维护者决定的情况，都有了规则（[见下文](#已定的事2026-11-05)）；失败的运行会自己重跑；年度奖按规则写出 | 已完成（2026-11-05） |
| README 以榜开头 | 两个 README 都以发布榜开头：本周、下周已登记、上周前三、上升榜，像 feed 一样排，再讲怎样发布；封面图画的是同样的卡片。周五登记和周一开榜的提交会一并重新生成 | 已完成（2026-11-05） |
| 日榜 | 从周榜改为日榜 | 连续 4 周、每周至少 20 个 Launch 之后；榜单页会显示已连续几周 |

第一周开榜之前，榜单列出最新一周进入目录的产品，先按谁读过调用点、再按星标排序。这是排序，不是排名。不管哪一周有没有 Launch，榜单也列出上升最快的产品（[上升最快](#上升最快)）。

## 什么可以发布

**产品**是目录里满足以下条件的一行：类型为 `project`、`plugin`、`sdk` 或 `integration`，带代码，并且是用 Jev 做决策的示例（没有 `not-jev` 或 `shadow-mode-only` 标记）。文章、视频、教程、基准测试和替代品留在目录里，不参与发布。

还没被收录的产品，先按常规方式加入目录（[CONTRIBUTING.md](../CONTRIBUTING.md#adding-an-entry)）；发布需要先有这一行。

同一个产品 60 天内最多发布一次。

## 谁来发布

- **Maker**：这一行 `makers` 里的 GitHub 登录名；没有 `makers` 时，取 `author.url` 里的登录名。发布 issue 的检查还认仓库所有者、拥有仓库的组织的公开成员，以及提交数至少 5 次、排在仓库贡献者前三的人，并把他们加进 `makers`。其他自称 Maker 的人按 Hunter 发布，检查的回复会说明原因；不需要谁来确认。
- **Hunter**：替别人发布产品的人。Launch 会记下他们，产品的 Maker 之后仍可认领。榜单按他们带上榜并跑完一周的 Launch 数、以及其中进过前三的数致谢。
- 发现管线自动收录的行，在有人发布之前没有 Launch。

Maker 可以提一个 pull request，添加 `makers/<login>.json`（[schema](../schema/maker.schema.json)），在自己的页面上写名字、链接和中英文各一句介绍。页面上列出的产品始终来自目录。

Maker 还可以通过 [confirm-entry 表单](https://github.com/kydlikebtc/awesome-jev/issues/new?template=confirm-entry.yml) 或 pull request，给产品加上 `tagline`（及 `tagline_zh`）和 `demo_url`；产品页上的"这是你做的？"会打开这个表单，条目已填好。tagline 是 Maker 自己的话，模型从不代写。

发布过之后，产品页会说明什么时候可以再次发布：在当天提交的 Launch 距上一次发布的那一周还不满 60 天时，显示最早可以发布的那一周的周一；满了之后显示"再次发布"。

## 一周的流程

周按 ISO 周计算：周一 00:00 UTC 到周日 23:59 UTC。

1. 用表单在周四 23:59 UTC 前提交，进入下一周（之后提交的进入再下一周）。检查会马上回复这个 issue：可以上榜（附上规则替它定了什么）；还没读到（GitHub 没有回应，周五排期时会再读一次）；或者暂不能发布（附要改什么）。从 2026-11-05 起，不再有任何情况挂起等人：
   - 确认不了 Maker 身份的，按 Hunter 发布；
   - 提交者账号不满 30 天的，排进账号满 30 天之后开始的第一周；
   - fork 仓库要有至少 10 次自己的提交才能发布，60 天没有推送的仓库要有新的推送才能发布；在那之前暂不能发布，编辑 issue 会重新检查。

   调用点还没人读过的产品，会在开榜前读过，所以每个 Launch 开榜时至少有模型读过。
2. 周五一早（00:20 UTC）把这一周的 Launch 写进 `launches/<YYYY>-W<ww>.json`（[schema](../schema/launch.schema.json)）并推到 `main`，不用等合并。榜单在"下周"下面列出它们。错过了自己那一周的 Launch（比如信息读得太晚），排进这一周。
3. 周一 00:05 UTC 开榜：每个 Launch 在仓库的 `Launches` Discussions 里有一个帖子，在帖子上点赞就是投票。Launch 的 issue 会收到帖子链接，然后关闭。
4. 开榜期间，榜单按随机顺序展示，不显示票数，免得大家只给排在前面的投票。（Discussion 自己会显示点赞数，榜单不重复显示。）
5. 下一个周一收榜：统计票数，结果写入当周文件。一个 Launch 的票大多来自新账号时，这些票不计，按其余的票排名，结果和周榜页都会注明。至少计到一票的前三名，README 徽章会显示名次（[见下文](#readme-徽章)），这一周也有了自己的页面。每个 Launch 的 issue 会收到它的结果，前三名还会收到显示徽章的那行代码。

每个月的月报（[docs/monthly/](monthly/)，在下个月第一周写成）列出当月结束的每一周和它的前三名。

Agent 不用看页面也能读榜。MCP 服务器的 `launch_board()` 返回本周（随机顺序、不显示票数）、上周（已排名）和下周；`top_launches(pattern=…)` 返回名次最好的产品，每个产品只出现一次，取它最好的那一周。站点在 `api/v1/launches.json` 提供每一周的原始文件和榜单上的样子。两者都和页面一样，把每个 Launch 的证据和标记放在票数旁边。

## 怎么计票（规则 v2）

- 每个 GitHub 账号一票，必须在本周内投出。
- 产品 Maker 和 Launch 提交者自己的票不计。
- 投票时注册不满 30 天、或读不到注册时间的账号，按半票计。
- 一个 Launch 至少有 10 票、其中至少一半来自这样的账号时，看起来像是一批新账号在刷票：这些票不计，结果里会注明（`ring`）。
- 按计入的票数排名。同票时证据强的在前（有人读过调用点，其次模型读过，其次脚本匹配，最后没有证据），再同则先提交的在前。

规则从不原地修改：新规则用下一个名字，每个已收榜的周都记录当时用的规则。规则 v1（2026-11-03）只有一处不同：遇到疑似刷票，v1 先挂起等人决定，不参与排名；v2（2026-11-05）不用等人。没有哪一周是按 v1 收榜的。

仓库只保存数字：多少票、计入多少、打了折扣的有多少。从不保存谁投了票。

## 榜单怎么衡量

每个已收榜的周在结果旁边记几个数。榜单页显示上周的，周榜页显示那一周的，月报显示当月每一周的：

- **账号**：这一周有多少账号的票计入了（`voters`），其中多少个上周也投过（`returning_voters`）。和票数一样，只记数字。
- **计入票数达到 5 的 Launch**：榜单最主要的指标。
- **开榜前读过**：开榜时，有多少 Launch 的调用点已由人或模型读过（每个 Launch 的 `tier_at_open`）。目标是全部：`python3 scripts/launch_intake.py --unread` 列出即将开榜、还没人读过的 Launch，每日任务先读它们。
- **打折扣的票**：有多少票按不足一票计。

连续四周、每周至少 10 个 Launch 在榜、至少 50 个账号的票被计入，说明榜单在起作用；月报会写目前已连续几周。两者的规则都在 [`scripts/launches.py`](../scripts/launches.py)（`week_measures`、`gate_streak`）。

## 上升最快

榜单列出最近两次每周刷新（[history/](../history/) 里的快照，每周三一份）之间 GitHub 星标涨得最快的产品：至少涨了 10 个的，按涨幅占原有星标的比例排序，再按涨了多少，最多十个。和新收录一样，沉寂的产品（60 天没有推送）不列。每份月报按同样的规则列出当月的，从当月第一份快照到最后一份。

这样不管有没有 Launch，榜单每周都有内容，Hunter 也有地方下手：上升最快、可以发布的产品带"发布它"，本周在榜的带它的投票帖。星标是 GitHub 的计数，是热度信号，不是评价，也从不和票数或证据相加。上升不会得到任何奖励。规则是 [`scripts/launches.py`](../scripts/launches.py) 里的 `rising`。

## README 徽章

每个产品在 `badges/<slug>.svg` 有一枚徽章，产品页给出把它放进 README 的那一行，链接到产品页：

```markdown
[![awesome-jev](https://kydlikebtc.github.io/awesome-jev/badges/your-slug.svg)](https://kydlikebtc.github.io/awesome-jev/products/your-slug.html)
```

地址不变，图片会跟着变：先显示 **listed**（已收录）；排进某一周后显示 **launching 2026-W46**；那一周开榜期间显示 **vote this week**；在某一周进了前三、并且至少计到一票之后，显示名次（**#1 launch of 2026-W46**），直到之后某一周再次进前三。它随网站一起重建，不会说榜单没说的话。每个 Launch 的 issue 在开榜时会收到这一行，前三名收榜时会再收到一次。规则是 [`scripts/launches.py`](../scripts/launches.py) 里的 `badge_state`。

## 年度决策奖

Jev 在 2026-09-15 进入早期访问，所以发布榜的一年从 9 月 15 日算到下一年 9 月 14 日。从 2027-09-15 起，每年这一天给每种决策模式颁一个奖。`python3 scripts/award.py --year 2027` 从这一年已收榜的周里，为每种模式列出候选名单：只收有人或模型读过调用点的产品，每个产品取它最好的那一周，先按名次、再按计入票数排序，最多三个。每份名单的第一名就是获奖者。票数决定名单的顺序，证据决定谁能进名单。不需要人来选：[`award.yml`](../.github/workflows/award.yml) 每月 15 日运行 `award.py --due`，这一年结束后写出 `docs/award/<年份>.md`，已经写过的年份不再改动。

## 已定的事（2026-11-03）

仓库主人让这些悬而未决的问题直接定下来，不必等仓库主人确认。下面每一条都已定，想改可以开 issue 重新讨论。

- **名字。** 发布榜叫"awesome-jev 发布榜"（英文 "awesome-jev Launches"）。沿用目录的名字，不用另外注册什么，也不借用别的产品的名字。
- **邮件简报：不做，改为订阅源。** 每个已收榜的周是 [`launches.zh.xml`](https://kydlikebtc.github.io/awesome-jev/launches.zh.xml)（[English](https://kydlikebtc.github.io/awesome-jev/launches.xml)）里的一条，榜单页上有链接。用阅读器订阅即可；想收邮件的人可以用自己的服务把订阅源转成邮件。做邮件简报需要邮件服务、要保管一份邮箱名单、还要有人代表项目发信，这些发布榜都不保留。
- **站内评论（giscus）：不做。** 站点不加载其他网站的脚本，每个 Launch 在 Discussions 里的投票帖本身就是讨论的地方，产品页上有链接。
- **MCP Registry：等包发布到 PyPI 之后。** Registry 的条目指向一个已发布的包，而发布 `awesome-jev-mcp` 要由仓库主人来做（[MAINTAINING.md](../MAINTAINING.md#set-up-once)）。
- **单独的模板仓库：不建。** [launch-engine.zh-CN.md](launch-engine.zh-CN.md) 写清了要复制什么、改什么；再建一个仓库只是多一份要同步的副本。
- **联系 Maker：只在本仓库里。** 发布榜不在别处给任何人发消息，也不开社交账号。Maker 在他们本来就会经过的地方看到它：README 有链接，新条目机器人的评论会说已收录的产品可以发布，每个产品都有自己的页面。
- **增加审核人：暂不。** 每周只有几个 Launch 时一位维护者就读得过来；等哪一周超过 20 个再议。（从 2026-11-05 起，每日任务会在开榜前读完每个 Launch 的调用点，没有 Launch 要等审核人。）

## 已定的事（2026-11-05）

仓库主人希望整个流程都不需要他们亲手做任何事。原来要等维护者决定的情况，现在都有了规则，写在 [`scripts/launch_intake.py`](../scripts/launch_intake.py) 和 [`scripts/launches.py`](../scripts/launches.py) 里：

- **检查确认不了的 Maker**：按 Hunter 发布。检查还认提交数至少 5 次、排在仓库贡献者前三的人为 Maker。
- **fork 仓库**：要有至少 10 次自己的提交（按 GitHub 和上游仓库的比较）才能发布；在那之前，回复会写明它现在有几次。
- **60 天没有推送的仓库**：下一次推送之后可以发布，编辑 issue 会重新检查。
- **注册不满 30 天的提交者账号**：排进账号满 30 天之后开始的第一周，回复会写明是哪一周。
- **GitHub 没有回应的信息**：周五排期时再读一次；检查回复里没记下的信息，排期时也会去 GitHub 读。
- **错过了自己那一周的 Launch**：排进下一周。
- **疑似刷票的票**：按规则 v2 不计，这个 Launch 按其余的票排名。
- **年度奖**：每份名单的第一名，由 `award.yml` 写出。
- **失败的运行**：`main` 上失败的运行会自己再跑一次（[`retry.yml`](../.github/workflows/retry.yml)），周五和周一的运行当天还会再各跑两次；周五或周一推送时如果 `main` 变了，就在新的 `main` 上重新排期或重新计票，不再留下一个分支等人合并。

## 绝不做的事

- 不出售排名，不因为钱把一个 Launch 排到另一个前面。
- 疑似一批新账号刷票的，这些票不计（规则 v2）。发现其他刷票手段（比如买票）的 Launch 会被下榜，原因留在当周的文件里。
- 榜单不请任何人投票，也不在本仓库之外发帖。

## 文件

| 路径 | 内容 | 由谁写 |
| --- | --- | --- |
| `catalog.json` | 产品，含 `makers`、`tagline`、`tagline_zh`、`demo_url` | 贡献者和 Maker |
| `launches/<YYYY>-W<ww>.json` | 一周：它的 Launch、状态，收榜后的结果 | 发布脚本 |
| `makers/<login>.json` | Maker 自己的介绍，可选 | Maker 本人 |
| `scripts/launches.py` | 上面所有规则 | |
| `scripts/check_launches.py` | 按这些规则校验 `launches/` 和 `makers/` | |
| `scripts/launch_intake.py` | 检查发布 issue，汇总一周的 Launch，列出还没人读过的 | |
| `scripts/launch_week.py` | 开本周的榜，收上周的榜，通知每个 Launch 的 issue | |
| `scripts/launch_votes.py` | 读取一个 Discussion 的投票 | |
| `scripts/site_products.py` | 产品页、Maker 页、周榜页、榜单页、上升最快的列表、徽章和每周结果订阅 | |
| `history/<date>.json` | 每次每周刷新的计数和星标；上升最快的列表读最新的两份 | `metadata.yml` |
| `src/awesome_jev_mcp/query.py` | MCP 服务器的发布榜工具和 `api/v1/launches.json` 的内容 | |
| `scripts/award.py` | 年度奖：每种模式一份候选名单，第一名即获奖者 | |
| `docs/award/<year>.md` | 这一年结束后的年度奖 | `award.yml` |
| [launch-engine.zh-CN.md](launch-engine.zh-CN.md) | 怎样为另一个目录运行这套发布榜 | |
| `.github/workflows/launch-intake.yml` | 用检查结果回复每个发布 issue | |
| `.github/workflows/launch-collect.yml` | 每周五：把下周的 Launch 写到 `main` | |
| `.github/workflows/launch-week.yml` | 每周一：收上周的榜，开本周的榜，通知各 issue | |
| `.github/workflows/launch-votes.yml` | 手动运行：读取一个 Discussion 的投票 | |
| `.github/workflows/launch-probe.yml` | 手动运行：工作流能否在 `Launches` 分类发帖 | |
| `.github/workflows/award.yml` | 每月 15 日：到期时写出这一年的年度奖 | |
| `.github/workflows/retry.yml` | `main` 上失败的运行，自动再跑一次 | |

`python3 scripts/check_launches.py` 和其他检查一起运行（`python3 scripts/check.py`）。
