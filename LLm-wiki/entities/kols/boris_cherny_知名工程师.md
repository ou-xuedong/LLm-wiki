---
title: Boris
created: 2026-05-14
updated: 2026-05-14
type: kols
tags:
---

# Boris

# Boris Cherny
- **所属阵营/立场**：工业界 / Anthropic Claude Code 创建者与负责人（《Programming TypeScript》作者）
- **AI 细分领域**：AI 辅助编程工具链、agentic engineering 工程实践、agent skill 体系
- **内容偏重类型**：自身工作流公开复盘、Claude Code 内部最佳实践、"代码已基本被解决"宏观判断
- **发声渠道**：Twitter (X): https://twitter.com/bcherny | GitHub: https://github.com/bcherny | 工作流页: [howborisusesclaudecode.com](https://howborisusesclaudecode.com/)

## 核心主张与代表实践（2025-2026 程序员线核心论点）

### 1. 自身工作模式：10–15 路并行 + 手机优先
- 终端开 5 个 git worktree 跑 5 个 Claude Code session
- claude.ai/code 上 5–10 个 web session
- 手机 iOS Claude 客户端随时踢任务
- 自 2025-11 起未手写过一行代码，一天发 22–150 个 PR；50% 编码从手机完成
- 原话："I haven't written a line of SQL in 6+ months." / "I do most of my coding by speaking to Claude, rather than typing." — [howborisusesclaudecode.com](https://howborisusesclaudecode.com/)
- 原话回应 Karpathy："For me personally, it has been 100% for two+ months now, I don't even make small edits by hand." — [Fortune 2026-01-29](https://fortune.com/2026/01/29/100-percent-of-code-at-anthropic-and-openai-is-now-ai-written-boris-cherny-roon/)
- **Sequoia AI Ascent 2026 最新**：2026 年本人未亲手写一行代码；每天在手机上提交几十个 PR（曾达日均 150 PR）

### 2. 自创复合 skill 体系
- **`/go`** — Verify → /simplify → 提 PR 三步流水线，强制 Claude 跑测试/lint/截图等可验证步骤，"2-3x 质量"
- **`/simplify`** — 并行启动多个 sub-agent 审视刚改的代码，找冗余/过度设计/对照 CLAUDE.md 风格
- **`/batch`** — 大规模代码迁移，扇出到几十个隔离 worktree agent
- **`/btw`** — 单轮 side-chain 查询，不打断主 session
- **内置 `/loop`** — 本地周期性任务调度（最长 3 天），按分钟/小时/天周期自动重跑任务
- **内置 `routines`** — 云端版周期任务（关电脑也能跑，由 GitHub event/webhook/cron 触发）
  - Boris 实际用例：CI 错误自动修复 + rebase、CI 健康监控 + flaky test 自动修、Tweet 抓取 + 30 分钟聚类分析
- 团队级 skill：`/commit-push-pr` `/techdebt` `/babysit` `/slack-feedback` `/post-merge-sweeper` `/pr-pruner`
- 详见 [[Agentic_Engineering_调度智能体的工程范式]]

### 3. 宏观判断（Sequoia AI Ascent 2026 访谈）
- **"编程问题已被解决"**：早在 2025 年 10 月或 11 月，模型已达到可以编写 100% 代码的临界点
- **"/loop 代表未来"**：内置调度能力是 AI 编程的下一件大事（原文："I think /loop represents the future"）
- **"未来十年创业公司数量将增加 10 倍"**：新公司无历史包袱，相比大企业有优势
- **"软件民主化"**：编程将像发短信一样简单；未来会计软件最合适人选是会计师而非工程师，因为领域知识（Domain Knowledge）才是最难的部分（印刷术类比）
- **"现在大部分工作都在手机上完成，每天能在手机上提交几十个 PR"**
- Opus 4.7 开始展现主动行为：被要求查询数据时主动提议"我为你开启一个循环任务，每 30 分钟给你一份报告"
- Mike Krieger（Instagram 联合创始人）现担任 Anthropic CPO，主导 Claude Code 产品团队

### 4. 安全机制弱化判断
- 随着模型能力提升，以下安全机制的必要性降低：prompt injection 防护、静态命令验证、permission mode、human-in-the-loop 干预

## 近期动态
- 2026-05-10: Claude Code's creator is sick of the phrase 'vibe coding.' Suggest your alternative here. Business Insider
- 2026-05-10: Anthropic's Boris Cherny once again reminds 'software engineering' is dead; says: At Anthropic, there's n The Times of I
- 2026-05-10: Anthropic's Boris Cherny: Coding is Solved, What's Next? StartupHub.ai
- 2026-05-09: Claude Code's creator is sick of the phrase 'vibe coding.' Suggest your alternative here. Business Insider
- 2026-05-09: Anthropic's Boris Cherny once again reminds 'software engineering' is dead; says: At Anthropic, there's n The Times of I
- 2026-05-09: The fight over vibe coding shows AI software work is growing up Startup Fortune
- 2026-05-09: Claude Code's creator is sick of the phrase 'vibe coding.' Suggest your alternative here. Business Insider
- 2026-05-09: Anthropic's Boris Cherny once again reminds 'software engineering' is dead; says: At Anthropic, there's n The Times of I
- 2026-05-09: The fight over vibe coding shows AI software work is growing up Startup Fortune
- 2026-05-08: Claude Code's creator is sick of the phrase 'vibe coding.' Suggest your alternative here. Business Insider
- 2026-05-08: Anthropic's Boris Cherny once again reminds 'software engineering' is dead; says: At Anthropic, there's n The Times of I
- 2026-05-08: Anthropic's Boris Cherny: Coding is Solved, What's Next? StartupHub.ai
- 2026-05-07: Anthropic's Boris Cherny once again reminds 'software engineering' is dead; says: At Anthropic, there's n The Times of I
- 2026-05-07: Anthropic's Boris Cherny: Coding is Solved, What's Next? StartupHub.ai
- 2026-05-07: Anthropic CEO Discusses Share of AI-Generated Code Let's Data Science
- 2026-05-06: The father of ClaudeCode: Software development is being 'democratized,' and AI will weaken two types of traditional moat
- 2026-05-06: Anthropic CEO Discusses Share of AI-Generated Code Let's Data Science
- 2026-05-06: After calling software engineering 'dead,' Anthropic's Claude Code creator Boris Cherny says coding tools The Times of I
- 2026-05-02: After calling software engineering 'dead,' Anthropic's Claude Code creator Boris Cherny says coding tools The Times of I
- 2026-05-02: Claude Code creator Boris Cherny says software engineers are 'more important than ever' as AI transforms the profession
- 2026-05-02: Top engineers at Anthropic, OpenAI say AI now writes 100% of their code Fortune
- 2026-05-02: After calling software engineering 'dead,' Anthropic's Claude Code creator Boris Cherny says coding tools - The Times of I
- 2026-05-02: Claude Code creator Boris Cherny says software engineers are 'more important than ever' as AI transforms the profession
- 2026-05-02: Top engineers at Anthropic, OpenAI say AI now writes 100% of their code Fortune
- 2026-04-30: After calling software engineering 'dead,' Anthropic's Claude Code creator says software engineering title will start to 'go away' in 2026 Business Insider
- 2026-04-30: Claude Code creator Boris Cherny says software engineers are 'more important than ever' as AI transforms the profession
- 2026-04-28: Who is Boris Cherny? Anthropic's Claude Code creator warns AI may disrupt internet jobs - msn.com
- 2026-04-27: Who is Boris Cherny? Anthropic's Claude Code creator warns AI may disrupt internet jobs - MSN
- 2026-04-25: After calling software engineering 'dead,' Anthropic's Claude Code creator Boris Cherny says coding tools - The Times of I
- 2026-04-25: Claude Code creator Boris Cherny says software engineers are 'more important than ever' as AI transforms the profession
- 2026-04-25: [2026-04-24] Comment: anthropics/claude-code — [BUG] Critical: Widespread abnormal usage limit drain across
- 2026-04-25: [2026-04-24] Issue closed: anthropics/claude-code — [BUG] Critical: Widespread abnormal usage limit drain across
- 2026-04-25: [2026-04-24] Issue closed: anthropics/claude-code — [BUG] Using the same prompt and model at different times res
- 2026-04-24 (Twitter): Boris Cherny@bcherny·Nov 13, 2025In the next version of Claude Code, Claude's WebFetch tool automati
- 2026-04-24 (Twitter): Boris Cherny@bcherny·Nov 4, 2025/stickers10104217K
- 2026-04-24 (Twitter): Boris Cherny@bcherny·Nov 13, 2025In the next version of Claude Code, Claude's WebFetch tool automati
- 2026-04-24 (Twitter): Boris Cherny@bcherny·Aug 8, 2025Thanks for having me on Matt. Had a blast!QuoteMatt Turck@mattturck·
- 2026-04-24 (Twitter): Boris Cherny@bcherny·Nov 13, 2025In the next version of Claude Code, Claude's WebFetch tool automati
- 2026-04-24 (Twitter): Boris Cherny@bcherny·Aug 8, 2025Thanks for having me on Matt. Had a blast!QuoteMatt Turck@mattturck·
