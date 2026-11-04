# 为另一个目录运行这套发布榜

[English](launch-engine.md)

发布榜（[launches.zh-CN.md](launches.zh-CN.md)）由几份脚本组成，读一个目录文件，再加上每个公开 GitHub 仓库都有的四样东西：Issues 收提交，Discussions 收投票，Actions 每周收榜，Pages 展示榜单。不需要服务器、数据库或付费服务。这一页写给想在另一个目录上搭同样榜单的人。这一页就是模板：按 2026-11-03 的决定，不另建模板仓库（[launches.zh-CN.md](launches.zh-CN.md#已定的事2026-11-03)）。

## 榜单要用到每一行的哪些字段

产品就是 `catalog.json` 里的一行。榜单读这些字段：

| 字段 | 用途 |
| --- | --- |
| `slug`、`title`、`url` | 产品名称和链接 |
| `kind`、`has_code`、`flags` | 能不能发布（`launches.is_product`：带代码的 project、plugin、SDK 或 integration，且没有被标为不是示例） |
| `evidence`（`path`、`matched`、`read_on` 或 `model_read_on`） | 票数旁边显示的证据等级：有人读过调用点、模型读过、脚本匹配到，或没有 |
| `patterns` | `top_launches(pattern=…)` 和年度奖的候选名单 |
| `makers`，没有时用 `author.url` | 谁算 Maker |
| `repo_pushed_at`、`first_seen` | 停更检查和"本周新收录" |
| `tagline`、`tagline_zh`、`demo_url` | 可选，Maker 自己的话 |

另一个目录需要同样的字段，或者在脚本读取之前用一个小函数把自己的字段映射过来。

## 文件

规则部分只用标准库，不依赖本仓库的其他代码：

| 文件 | 作用 |
| --- | --- |
| `src/awesome_jev_mcp/query.py`（发布榜那一节） | 证据等级、随机顺序，以及 Agent 看到的一周是什么样 |
| `scripts/launches.py` | 榜单的全部规则：产品、周、投票权重、刷票检查、排名、徽章和 README 徽章显示什么、Hunter、日榜门槛、上升最快的列表 |
| `scripts/launch_votes.py` | 通过 GraphQL 读取一个 Discussion 的点赞和投票账号的注册时间 |
| `scripts/launch_week.py` | 收上周的榜、开本周的榜；`--probe` 检查令牌能否发帖 |
| `scripts/award.py` | 年度奖候选名单 |
| `scripts/_github.py` | 上面三个脚本用的 GitHub 客户端（令牌、GraphQL 查询和变更、任务摘要） |
| `schema/launch.schema.json`、`schema/maker.schema.json` | 周文件和 Maker 介绍的格式 |

收件检查和文件校验用到本目录自己的工具，另一个目录要换成自己的：

| 文件 | 依赖 |
| --- | --- |
| `scripts/launch_intake.py` | `draft_from_issue.py`（读 issue 表单）、`lint.py`（schema 校验） |
| `scripts/check_launches.py` | `lint.py`（`lint.validate`，一个最小的 JSON Schema draft-07 校验器） |
| `scripts/site_products.py` | 本站的页面外壳（`site_pages.py`）；别的站点用自己的方式渲染 `launches.weeks()`。上升最快的列表需要每行星标的两份每周快照（`history/<date>.json`，本仓库由 `scripts/snapshot_stats.py` 写入，`launches.refreshes()` 读取），没有快照的话榜单就没有这个列表 |

工作流：`.github/workflows/launch-intake.yml`、`launch-collect.yml`、`launch-week.yml`、`launch-votes.yml`、`launch-probe.yml`，以及 issue 表单 `.github/ISSUE_TEMPLATE/launch.yml`。`tests/test_launches.py`、`tests/test_launch_flow.py`、`tests/test_mcp_launches.py`、`tests/test_launch_award.py` 不联网就能测试全部内容。

## 要改什么

- 榜单的地址：`query.py` 里的 `SITE` 和 `REPOSITORY_URL`，以及 `_github.py` 里的 `SELF`。所有发布榜地址都由这三个推出来。
- 年份：`award.py` 里的 `ANNIVERSARY` 和 `FIRST_YEAR`。
- 规则：`launches.py` 里的 `RULES`。新增一个版本，不要修改已收榜的周用过的版本。
- 文案：issue 表单、投票帖（`launch_week.post`）和榜单页的文字。

## 仓库主人要打开什么

1. Discussions（Settings → Features），并建一个名叫 `Launches`、格式为 Announcement 的分类，这样只有维护者能在里面发帖。
2. 在 Actions 页面手动跑一次 `launch-probe`。如果工作流的令牌不能在 Announcement 分类里发帖，把分类改成 Open-ended：每周的工作流只认 `github-actions` 或仓库主人发的投票帖。
3. 对任意一个有点赞的帖子跑一次 `launch-votes`，确认令牌能读到点赞和账号注册时间。
4. 想要榜单页面的话，打开 Pages。
