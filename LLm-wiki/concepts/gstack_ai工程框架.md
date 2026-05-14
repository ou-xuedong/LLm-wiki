---
title: gstack
created: 2026-04-24
updated: 2026-04-24
type: concept
tags:
  - #概念
  - #AgentInfra
  - #DevTools
  - #AI编程
---

# gstack


## 关联

**上位概念**：[[Agent Infra]]
**相关概念**：[[gbrain_ai记忆系统]], [[OpenClaw]]
**关键人物**：[[Garry Tan]]

# 🧠 gstack (AI工程框架)

## 1. 定义与核心原理
`gstack` 是由 Y Combinator 总裁 Garry Tan 开源的一套专门针对 Claude Code（及 OpenClaw 等其他 AI Agent）设计的 AI 辅助工程框架。
它的核心理念是**“将单一的 Copilot 转化为一支全功能的虚拟工程团队”**。通过预设 23 个具有强烈倾向性（opinionated）的专家角色技能（如 CEO、设计总监、研发经理、发布工程师、QA 测试等）和 8 个强力工具，将软件开发的生命周期切割并标准化。

其核心工作流遵循敏捷开发的完整闭环：
**Think（思考） → Plan（规划） → Build（构建） → Review（审查） → Test（测试） → Ship（发布） → Reflect（复盘）**

## 2. 关键模块与核心命令
gstack 不仅仅是工具合集，更是一种“流程（Process）”。其核心命令设计极具针对性：
- **前置推演层**：
  - `/office-hours`：扮演 YC 合伙人，用 6 个强制性问题拷问产品定义，拒绝伪需求。
  - `/plan-ceo-review`：扮演 CEO 审查产品计划，寻找 10 星级体验的潜能，严格控制范围（Scope）。
- **设计与构建层**：
  - `/design-shotgun`：探索式设计，一次生成 4-6 个 AI UI 变体并开启浏览器对照，用户挑选反馈，快速迭代。
  - `/design-html`：将确定的 Mockup 直接转化为极具弹性和自适应能力、零外部依赖的生产级 HTML/CSS 代码。
- **质量与发布层**：
  - `/qa`：开启真实无头浏览器进行页面点击测试，自动发现 Bug、提交原子化修复并生成回归测试用例。
  - `/review` 和 `/codex`：独立双重代码审查，甚至可引入交叉模型（如 Claude 与 OpenAI）进行对抗性质询。
- **复盘学习层**：
  - `/retro`：工程师经理视角的周报级代码、提交流程复盘。
  - `/learn`：记忆提取与模式积累，随会话不断精进对当前代码库的认知。

## 3. 行业应用场景
- **单人开发者的效率飞升**：允许一名具有产品直觉的开发者在短时间内（如数十天内部署超 60 万行代码）具备一支 20 人研发团队的产出效率。
- **多 Agent 并发协作**：借助 Conductor 或多终端并发，可同时跑 10-15 个 Agent 进程并行处理不同分支的需求、审计和 QA，消除串行瓶颈。

## 4. 代表性论文/项目
- **GitHub 官方仓库**: [garrytan/gstack](https://github.com/garrytan/gstack)

## 5. 争议与开放问题
- **过度流程化的利弊**：对于极小微的临时脚本改动，走全套 gstack 流程显得冗杂，框架需要使用者自行把握尺度。
- **并发状态的冲突管理**：虽然多个 Agent 分别处在不同的会话或终端，如何避免它们在合并代码或调用公共资源时产生相互覆盖或锁死，依然考验使用者的微观调控能力。

## 6. 最新动态 (2026-03-28)
- **5万 GitHub Star 里程碑**：Garry Tan 宣布 gstack 达到 5 万 Star，现可直接在 Claude Code 中通过命令安装使用
- **/design-shotgun 上线**：探索式 AI UI 设计工具，一次生成多版本变体并开启浏览器对照
- **AI Agent 消除代码分支腐烂**：Garry Tan 实测 AI Agent 辅助编程让代码分支不再因长时间搁置而腐烂，随时可用 Agent 快速跟进
