---
title: Software
created: 2026-05-08
updated: 2026-05-08
type: concept
tags:
  - #概念
  - #AI编程
  - #范式迁移
  - #软件开发史
confidence: high
---

# Software


## 关联

**上位概念**：判断力_Judgment
**相关概念**：Vibe_Coding_凭感觉接受LLM输出的编程模式, Agentic_Engineering_调度智能体的工程范式, Jagged_Intelligence_AI能力不均衡现象, Service_as_a_Software
**关键人物**：Andrej_Karpathy_大牛_AI大牛

# 🧠 Software 3.0（自然语言编程范式）

## 1. 定义与核心原理

Software 3.0 由 [[Andrej_Karpathy_大牛_AI大牛]] 在 2026 年 Sequoia AI Ascent 上系统阐述，是继 Software 1.0（手写代码）和 Software 2.0（神经网络从数据学习）之后的第三波软件开发范式：

| 范式 | 核心机制 | 开发者角色 |
|------|----------|------------|
| **Software 1.0** | 人类逐行手写指令 | 代码的作者 |
| **Software 2.0** | 神经网络从数据中学习模式 | 训练数据的定义者 |
| **Software 3.0** | 自然语言描述目标，大模型生成实现 | **目标的描述者 + 质量的评审者** |

**核心要义转变**：从"精确指定每一条指令" → "描述你想要什么（目标+约束+上下文），让模型自己找到路径"。

## 2. 关键技术路线与变体

### 2.1 标志性特征

- **Prompt 作为接口**：不再是 API 调用，而是用自然语言下达任务
- **模型作为编译器**：输入自然语言描述，输出可运行代码/执行结果
- **人作为验收者**：最终判断结果是否符合意图，而非逐行审查实现细节

### 2.2 技术支撑层

- **强基础模型**：GPT-4o、Claude 3.5/3.7、Sonnet 等具备超长上下文和复杂推理能力
- **Code Interpreter / Tool Use**：模型能执行代码、调用 API、操作文件系统
- **Multi-turn 对话**：任务在多轮迭代中逐步精确化（参考 [[Agentic_Engineering_调度智能体的工程范式]]）

### 2.3 与前身的关键区别

- **Software 1.0 vs 3.0**：确定性执行 vs 概率性生成；人类写出答案 vs 人类描述问题
- **Software 2.0 vs 3.0**：2.0 是隐式学习（数据→权重），3.0 是显式生成（语言→代码）；2.0 的行为不可解释，3.0 的输出仍可 Review

## 3. 行业应用场景

- **Vibe Coding**（见 [[Vibe_Coding_凭感觉接受LLM输出的编程模式]]）：Software 3.0 的早期形态，非结构化prompt → 快速代码
- **Agentic Engineering**（见 [[Agentic_Engineering_调度智能体的工程范式]]）：Software 3.0 的纪律化形态，spec + evaluation loop → 可验证的自主工作流
- **No-code/Low-code 平台**：自然语言描述 → 可用应用的最后一公里
- **AI Native IDE**：Cursor、Windsurf、Copilot 等工具将自然语言→代码转换嵌入编辑器核心

## 4. 代表性论文/项目

- Karpathy 演讲（完整 blog）：[karpathy.bearblog.dev/sequoia-ascent-2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/)
- YouTube 视频：[Andrej Karpathy: From Vibe Coding to Agentic Engineering](https://www.youtube.com/watch?v=96jN2OCOfLs)

## 5. 争议与开放问题

- **概率性 vs 确定性**：软件开发传统上要求确定性行为，Software 3.0 的概率性输出（同一 prompt 多次结果不同）是否满足生产级质量要求？
- **可解释性缺失**：当代码是模型生成而非人类书写时，如何保证安全合规（GDPR、审计追踪）？
- **测试与验证的范式转移**：传统测试是"验证代码实现了 spec"，Software 3.0 下测试变成"验证模型输出是否满足 spec"——evaluation loop 的设计本身成为核心竞争力
