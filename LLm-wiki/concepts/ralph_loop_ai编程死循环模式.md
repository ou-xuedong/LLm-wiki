---
title: Ralph
created: 2026-05-07
updated: 2026-05-07
type: concept
tags:
  - #概念
  - #AI编程
  - #agentic_engineering
  - #自进化
  - #工作流
confidence: high
---

# Ralph


## 关联

**上位概念**：[[agentic_engineering_调度智能体的工程范式|agentic_engineering_调度智能体的工程范式]]
**相关概念**：[[sub-agent隔离机制|sub-agent隔离机制]], [[Anthropic|Anthropic自举飞轮_Claude Code开发Claude Code]], [[自进化AI-RSI|自进化AI_RSI]], [[vibe_coding_凭感觉接受llm输出的编程模式|vibe_coding_凭感觉接受llm输出的编程模式]], [[superpowers_ai编程纪律工具|superpowers_ai编程纪律工具]]
**关键人物**：[[geoffrey_huntley_独立工程师_ralphloop发明者|geoffrey_huntley_独立工程师_ralphloop发明者]], [[anthropic_直接操控计算机|anthropic_直接操控计算机]]

# 🧠 Ralph Loop（AI 编程死循环模式）

## 1. 定义与核心原理

Ralph Loop 是 [[geoffrey_huntley_独立工程师_ralphloop发明者|geoffrey_huntley_独立工程师_ralphloop发明者]] 在 2025 年提出的 agentic engineering 工程范式：**用一个最简 bash 死循环把 AI 编码 agent 反复叫起来，每次只前进一小步，靠 git 历史 + 文件状态做长期记忆，最终堆出复杂产物**。命名灵感来自《辛普森一家》傻乎乎重复同一句话的 Ralph Wiggum。

**核心命令**：
```bash
while :; do cat PROMPT.md | claude-code ; done
```

每一轮：
1. `cat PROMPT.md` 把规章读进来
2. 管道喂给 claude-code 命令
3. Claude 读 fix_plan.md 看下一步该干啥
4. 干完一小步 → 修改 src/、更新 progress.md、更新 fix_plan.md、git commit
5. 进程结束、while 循环重启 → 下一轮 Claude 接着进度继续

## 2. 关键技术路线与变体

### 2.1 文件状态作为长期记忆

```
项目目录/
├── PROMPT.md          ← 给 agent 的"宪法"（每轮被读）
├── fix_plan.md        ← agent 自己维护的"工单"（每轮可改）
├── progress.md        ← agent 自己写的"进度报告"
├── specs/             ← 目标规约
├── src/               ← agent 写的代码
└── .git/              ← git 历史是"长期记忆"
```

### 2.2 实施型 vs 规划型 PROMPT 双轨

**实施型 PROMPT**：
> "Your task is to implement missing stdlib and compiler functionality using parallel subagents. Follow @fix_plan.md and choose the most important things."

**规划型 PROMPT**：
> "Study specs/* and use up to 500 subagents to compare existing source code against specifications, then create @fix_plan.md sorted by priority."

### 2.3 大规模并行 sub-agent + 串行 build

Ralph 单 Claude session 内可派发最多 500 个 sub-agent 做独立研究/规划/规约对照，但 build 与 test 必须串行（避免冲突），靠"最终一致性"心态验收。

## 3. 行业应用场景

- **大型代码迁移与重构**：长周期、可分块、有明确验证标准的工作（如某门语言重构、API 升级）
- **从零搭一个新项目**：由 PROMPT.md 描述目标 + 规约文件做约束 + agent 在循环中逐步堆出
- **Y Combinator hackathon 模式**：Geoffrey 用 Ralph 一夜跑完 6 个仓库
- **量化策略迭代/自动复盘**：将"策略说明 + 风控规则"写入 PROMPT.md，让 Claude Code 每晚收盘后跑回测+择时调整（参考 [[superpowers_ai编程纪律工具|superpowers_ai编程纪律工具]] 与卟卟鸡投资决策项目）

## 4. 代表性论文/项目

- **CURSED 编程语言**：基于 LLVM 的全新生产级语言，Ralph Loop 跑了约 3 个月无人值守
- **how-to-ralph-wiggum 模板 repo**：https://github.com/ghuntley/how-to-ralph-wiggum
- **Geoffrey 半年复盘**：[ghuntley.com/six-month-recap](https://ghuntley.com/six-month-recap/)
- **Ralph 原文**：[ghuntley.com/ralph](https://ghuntley.com/ralph/)
- **音频访谈**：[Dev Interrupted #256](https://www.youtube.com/watch?v=C1YNGy6qusg)

## 5. 争议与开放问题

- **"笨循环 vs 复杂多 agent 框架"反共识**：Geoffrey 主张单线程 bash 循环比花哨的 multi-agent 编排更可靠；但行业主流仍在卷 LangGraph、AutoGen、CrewAI 等多 agent 框架——双方在"是否需要复杂调度层"上对立
- **失控边界**：连续无人值守的循环偶尔会进入"伪进步"状态（agent 修改文件但不真前进），需要外部信号（测试失败、git diff 空提交计数）作为熔断
- **成本与时间的非线性**：Geoffrey 公开案例「5 万合同 297 美元模型成本」依赖任务可分块且验证清晰，**复杂创意性任务（设计、产品决策）尚未验证可同等压缩**
- **可验证性是边界**：与 [[判断力_judgment|判断力_judgment]] 关联——Ralph Loop 高效的前提是任务有清晰对错信号；伦理/审美/战略类任务仍属人手保留区
