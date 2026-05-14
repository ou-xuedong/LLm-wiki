---
title: Agentic
created: 2026-05-07
updated: 2026-05-07
type: concept
tags:
  - #概念
  - #AI编程
  - #工作流
  - #方法论
confidence: high
---

# Agentic


## 关联

**上位概念**：[[判断力_Judgment]], [[AI作为高配实习生_角色分工方法论]]
**相关概念**：[[Vibe_Coding_凭感觉接受LLM输出的编程模式]], [[Ralph_Loop_AI编程死循环模式]], [[Sub-agent隔离机制]], [[Superpowers_AI编程纪律工具]], [[OpenSpec_AI开发规范框架]], [[Anthropic自举飞轮_Claude Code开发Claude Code]]
**关键人物**：[[Andrej_Karpathy_大牛_AI大牛]], [[Boris_Cherny_知名工程师]], [[Geoffrey_Huntley_独立工程师_RalphLoop发明者]]

# 🧠 Agentic Engineering（调度智能体的工程范式）

## 1. 定义与核心原理

由 [[Andrej_Karpathy_大牛_AI大牛]] 在 2026 年 Sequoia AI Ascent 上正式提出，作为 [[Vibe_Coding_凭感觉接受LLM输出的编程模式]] 的进化版：

> "Agentic engineering—'agentic' because the new default is that you are not writing the code directly 99% of the time, you are orchestrating agents who do and acting as oversight."  
> — [karpathy.bearblog.dev/sequoia-ascent-2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/)

**核心要义**：人从"写代码的人"升级为"调度智能体的人"。具体职责重心：
1. **写 spec**（需求规约/约束/测试）
2. **审 diff**（看 agent 改了什么）
3. **写 evaluation loop**（怎么自动判断 agent 干得对不对）
4. **守闸门**（PR 合并、生产部署、不可逆操作）

代码本身被"外包"，但**理解、判断、闸门**留在人手里。

## 2. 关键技术路线与变体

### 2.1 三种典型实践姿势

| 流派 | 代表人物 | 标志 |
|---|---|---|
| **多并行 + 闸门式** | [[Boris_Cherny_知名工程师]] | 5 worktree × 5 Claude session × 手机 + `/loop` `/go` `/simplify` skill 链路 |
| **YOLO + 隔离式** | [[Andrej_Karpathy_大牛_AI大牛]] | git worktree 隔离 + `--dangerously-skip-permissions` + 语音口述 |
| **笨循环 + 状态文件式** | [[Geoffrey_Huntley_独立工程师_RalphLoop发明者]] | [[Ralph_Loop_AI编程死循环模式]] + fix_plan.md/progress.md |

### 2.2 关键基础设施

- **git worktree**：同一仓库多个独立工作目录，每个 worktree 跑一个 agent，互不干扰，主分支不污染
- **YOLO 模式**：`--dangerously-skip-permissions` 命令行参数，跳过所有确认让 agent 全自动跑——必须配合 worktree 隔离才安全
- **CLAUDE.md / PROMPT.md**：项目根目录维护的"宪法"，每次新会话都基于同一套上下文（参考 [[OpenSpec_AI开发规范框架]]）
- **skill 体系**：自创复合命令（如 Boris 的 `/go`：verify→simplify→PR）强制 agent 走可验证步骤
- **MCP（Model Context Protocol，模型上下文协议）**：让 agent 直接连数据库、行情、文档等外部资源，减少手工搬数据

### 2.3 与 vibe coding 的差别

| 维度 | Vibe Coding | Agentic Engineering |
|---|---|---|
| 核心动作 | 凭感觉接受输出 | 写 spec + 监督 + 评估 |
| 适用范围 | 玩具/原型/小项目 | 生产代码、长期维护项目 |
| 纪律强度 | 低（"forget that the code even exists"） | 高（"isolate worktrees, manage permissions, preserve quality"） |
| 失败回收 | 重写 | git revert / 删 worktree |

## 3. 行业应用场景

- **个人开发者**：Boris 一天 150 个 PR、Geoffrey 一夜 6 个 repo——同一个时间块内的产出量级跃升
- **企业研发流程**：Anthropic 内部"pretty much 100%" 代码 AI 生成；OpenAI 类似（[[Anthropic自举飞轮_Claude Code开发Claude Code]]）
- **量化与交易**：CLAUDE.md 写交易系统记忆 + Claude Code 自动复盘 + 多 worktree 跑不同策略变体
- **PM/产品**：把 PRD 替换为可点原型 + agent 自动产出文档反推（参考 [[判断力_Judgment]]、[[AI作为高配实习生_角色分工方法论]]）

## 4. 代表性论文/项目

- Karpathy 升级演讲：[karpathy.bearblog.dev/sequoia-ascent-2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/)
- Boris 工作流公开页：[howborisusesclaudecode.com](https://howborisusesclaudecode.com/)
- Geoffrey 半年复盘：[ghuntley.com/six-month-recap](https://ghuntley.com/six-month-recap/)
- Anthropic + OpenAI "100% 代码 AI 写"：[Fortune 报道 2026-01-29](https://fortune.com/2026/01/29/100-percent-of-code-at-anthropic-and-openai-is-now-ai-written-boris-cherny-roon/)

## 5. 争议与开放问题

- **"放手"与"理解"的分寸**：Karpathy 名言"You can outsource your thinking, but you can't outsource your understanding"——agentic engineering 落地的最大挑战不是工具栈而是分寸感
- **新人成长路径断裂**：基层工程师如果一开始就在 agentic 模式下工作，是否会失去"读懂代码"的能力？这关系到行业人才结构（与 [[判断力_Judgment]] 直接关联）
- **责任归属**：agent 写错代码上线引发事故，责任在 agent、闸门人、还是 spec 编写者？目前业界尚无定论
- **企业适用性**：Anthropic/OpenAI 这类前沿公司的"100%" 数据是否能复刻到传统软件公司？工具链、文化、合规约束都是变量
