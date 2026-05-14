---
title: Vibe
created: 2026-05-07
updated: 2026-05-07
type: concept
tags:
  - #概念
  - #AI编程
  - #agentic_engineering
  - #工作流
---

# Vibe


## 关联

**上位概念**：[[Agentic_Engineering_调度智能体的工程范式]]
**相关概念**：[[Ralph_Loop_AI编程死循环模式]], [[判断力_Judgment]], [[AI作为高配实习生_角色分工方法论]], [[Superpowers_AI编程纪律工具]]
**关键人物**：[[Andrej_Karpathy_大牛_AI大牛]]

# 🧠 Vibe Coding（凭感觉接受 LLM 输出的编程模式）

## 1. 定义与核心原理

Vibe Coding 由 [[Andrej_Karpathy_大牛_AI大牛]] 在 2025 年 2 月 X 推文中提出，原文定义：

> "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists."  
> — [@karpathy 2025-02-02](https://x.com/karpathy/status/1886192184808149383)

**核心要义**：人不再读懂每一行代码，而是把需求口述/打字给 LLM（如 Cursor Composer + Claude Sonnet），凭"感觉"接受输出——只要能跑、效果对，不再追问代码细节。Karpathy 当时已开始用 [SuperWhisper](https://superwhisper.com) 直接对 Composer 口述需求。

## 2. 关键技术路线与变体

### 2.1 三件必备
- **强模型**：Cursor Composer + Claude/GPT 顶级模型，能在小项目里 one-shot 跑通
- **语音输入**：SuperWhisper 等本地语音转文字，让"打字"环节也省掉
- **快速反馈**：能即时跑、即时看效果的项目类型（小工具、原型、玩具项目）

### 2.2 适用边界
- 适合：玩具项目、个人小工具、原型、一次性脚本
- 不适合：长期维护的生产代码、合规要求高的代码、有测试覆盖率约束的代码

### 2.3 已被 Karpathy 自己升级
2026 年 Sequoia AI Ascent 上 Karpathy 宣布 vibe coding 已不再是他的主流姿势——升级为 [[Agentic_Engineering_调度智能体的工程范式]]：
> "Vibe coding is now passé. The new default is agentic engineering—you're not writing the code 99% of the time, you are orchestrating agents who do, and acting as oversight."  
> — [karpathy.bearblog.dev/sequoia-ascent-2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/)

差别：vibe coding 是"接受感觉"，agentic engineering 是"写 spec + 监督 + 评估循环"，多了纪律。

## 3. 行业应用场景

- 业余开发者、产品经理、设计师做 demo（Lovable / v0 / Bolt 这类工具的繁荣即基于 vibe coding 心智）
- 工程师做不重要的辅助代码（脚本、自动化、玩具）
- 教学场景下让初学者快速看到结果

## 4. 代表性论文/项目

- 原推：[@karpathy 2025-02-02](https://x.com/karpathy/status/1886192184808149383)
- 升级演讲：[Karpathy: From Vibe Coding to Agentic Engineering（YouTube）](https://www.youtube.com/watch?v=96jN2OCOfLs)
- 个人复盘：[karpathy.bearblog.dev/sequoia-ascent-2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/)

## 5. 争议与开放问题

- **质量与速度的取舍**：vibe coding 短期效率惊人，但长期维护成本/技术债高度依赖模型一致性
- **"理解 vs 信任"分界**：Karpathy 自述"I started trusting the system more and more"——但他同时强调 "You can outsource your thinking, but you can't outsource your understanding"。这两句的矛盾正是 vibe → agentic 升级的核心动力
- **教学场景争议**：vibe coding 让初学者快速出活，但是否削弱编程基础认知仍有争议（与 [[判断力_Judgment]] 关联）
