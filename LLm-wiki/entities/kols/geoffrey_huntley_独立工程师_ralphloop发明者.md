---
title: Geoffrey
created: 2026-05-07
updated: 2026-05-07
type: kols
kol_domain: ai
tags:
  - #KOL
  - #AI编程
  - #独立工程师
  - #agentic_engineering
---

# Geoffrey


## 关联

**所属**：[[anthropic_直接操控计算机|anthropic_直接操控计算机]]
**专长**：[[ralph_loop_ai编程死循环模式|ralph_loop_ai编程死循环模式]], [[agentic_engineering_调度智能体的工程范式|agentic_engineering_调度智能体的工程范式]], [[sub-agent隔离机制|sub-agent隔离机制]]
**相关 KOL**：[[boris_cherny_知名工程师|boris_cherny_知名工程师]], [[andrej_karpathy_大牛_ai大牛|andrej_karpathy_大牛_ai大牛]]

# 👤 Geoffrey Huntley（独立工程师 · Ralph Wiggum Loop 发明者）

- 所属阵营/立场：工业界 / 独立派 / agentic engineering 极简主义者
- AI 细分领域：AI 编程工程化、笨循环 vs 复杂多 agent 框架、`Claude Code` 大规模并行
- 内容偏重类型：把 AI 编码自动化打到极致 + 真实成本数据 + 反共识的"愚蠢循环 > 复杂框架"主张
- **发声渠道**：个人博客: https://ghuntley.com/ | GitHub: https://github.com/ghuntley | Twitter (X): https://twitter.com/GeoffreyHuntley

## 1. 核心观点与主张

- **"愚蠢循环 > 复杂多 agent 框架"**：单线程 bash 死循环 + 强 prompt + 文件状态做记忆，比花哨的多 agent 编排更可预测、更易调试，跑出来的产物更扎实
- **"IDE 退化为文件浏览器"**：日常工作只维护 prompt 库，不再手敲业务代码——主张 2026 年底前大多数软件工程师会停止"手工艺式 commit"
- **"工程成本可被打到快餐工时价"**：真实案例——5 万美元合同打到 297 美元模型成本（97% AI 推理 + 3% 人审核）
- **"500 并行 sub-agent + 串行构建"**：用 sub-agent 并行做研究/规划/对照规约，但 build/test 必须串行避免冲突，靠"最终一致性"心态验收

## 2. 代表作与里程碑

- **[[ralph_loop_ai编程死循环模式|ralph_loop_ai编程死循环模式]]** — 用 `while :; do cat PROMPT.md | claude-code ; done` 单行命令跑通 AI 自动编程的工程范式（命名灵感来自《辛普森一家》傻乎乎重复同一句话的 Ralph Wiggum）
- **CURSED 编程语言** — 基于 LLVM（Low Level Virtual Machine，底层虚拟机）的全新生产级语言，Ralph Loop 跑了约 3 个月无人值守
- **Y Combinator hackathon 案例** — 用 Ralph 一夜跑完 6 个仓库
- **`how-to-ralph-wiggum` 公开模板**：https://github.com/ghuntley/how-to-ralph-wiggum

## 3. 关键原话

- "while :; do cat PROMPT.md | claude-code ; done" / "Ralph is deterministically bad in an undeterministic world." — [ghuntley.com/ralph](https://ghuntley.com/ralph/)
- "I seriously can't see a path forward where the majority of software engineers are doing artisanal hand-crafted commits by as soon as the end of 2026." — [ghuntley.com/six-month-recap](https://ghuntley.com/six-month-recap/)
- "These days, I primarily use IDEs as file explorer tools. I rarely use the IDE except to craft and maintain my prompt library." — 同上

## 4. 近期动态

- 2026-05-07: 摄入「程序员线 KOL 调研」专题——Geoffrey 与 [[boris_cherny_知名工程师|boris_cherny_知名工程师]]、[[andrej_karpathy_大牛_ai大牛|andrej_karpathy_大牛_ai大牛]] 同列"调度型程序员"代表，详见 [[ralph_loop_ai编程死循环模式|ralph_loop_ai编程死循环模式]]
- 2025-11 至今：持续在 ghuntley.com 公开 Ralph Loop 实战案例与成本数据
- 历史：曾就职 Sourcegraph、Gitpod，澳洲资深独立工程师身份

## 5. 学习入口（推荐顺序）

1. [ghuntley.com/ralph](https://ghuntley.com/ralph/) — Ralph Loop 一手原文 + 完整 PROMPT 模板片段
2. [github.com/ghuntley/how-to-ralph-wiggum](https://github.com/ghuntley/how-to-ralph-wiggum) — 可执行 repo + 多项目脚手架
3. [ghuntley.com/six-month-recap](https://ghuntley.com/six-month-recap/) — 半年实践复盘
4. [Dev Interrupted #256 播客](https://www.youtube.com/watch?v=C1YNGy6qusg) — 亲口讲为何笨循环跑赢复杂框架


## 近期动态
- 2026-05-26: AI: The Promise and the Peril with Sen. Bernie Sanders and Geoffrey Hinton - Institute of Politics and Public Service In
- 2026-05-26: 'Godfather Of AI' Geoffrey Hinton Said AI Would Replace Radiologists—A Decade Later, Demand Is Surging, Salaries Are Soa
- 2026-05-26: AI godfather Geoffrey Hinton says we must convince AI that it’s our mother BetaKit
- 2026-05-19: Time to apply the brakes to runaway AI, says pioneer UN News
- 2026-05-19: AI godfather Geoffrey Hinton says we must convince AI that it’s our mother BetaKit
- 2026-05-19: AI: The Promise and the Peril with Sen. Bernie Sanders and Geoffrey Hinton Institute of Politics and Public Service
- 2026-05-17: Chasing Utopia review — this might be the most terrifying film of the year The Times
- 2026-05-17: AI godfather Geoffrey Hinton says we must convince AI that it’s our mother BetaKit
- 2026-05-17: AI Godfather Geoffrey Hinton Calls For Brakes On Runaway AI Development Eurasia Review
- 2026-05-15: Geoffrey Pohanka Frames AI as Systemic Risk or Bogeyman Let's Data Science
- 2026-05-15: AI godfather Geoffrey Hinton says we must convince AI that it’s our mother BetaKit
- 2026-05-15: 'Godfather Of AI' Geoffrey Hinton Said AI Would Replace Radiologists—A Decade Later, Demand Is Surging, Salaries Are Soa
- 2026-05-15: Geoffrey Pohanka Frames AI as Systemic Risk or Bogeyman Let's Data Science
- 2026-05-15: AI godfather Geoffrey Hinton says we must convince AI that it’s our mother BetaKit
- 2026-05-15: 'Godfather Of AI' Geoffrey Hinton Said AI Would Replace Radiologists—A Decade Later, Demand Is Surging, Salaries Are Soa

- 2026-05-15: Geoffrey Pohanka Frames AI as Systemic Risk or Bogeyman Let's Data Science
- 2026-05-15: AI Godfather Geoffrey Hinton Calls For Brakes On Runaway AI Development Eurasia Review
- 2026-05-15: AI godfather Geoffrey Hinton says we must convince AI that it’s our mother BetaKit
