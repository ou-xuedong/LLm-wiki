---
title: Jagged
created: 2026-05-08
updated: 2026-05-08
type: concept
tags:
  - #概念
  - #AI局限
  - #AI工程
  - #评测
---

# Jagged


## 关联

**上位概念**：判断力_Judgment
**相关概念**：Agentic_Engineering_调度智能体的工程范式, Software_3.0_自然语言编程范式, 判断力_Judgment, Vibe_Coding_凭感觉接受LLM输出的编程模式
**关键人物**：Andrej_Karpathy_大牛_AI大牛

# 🧠 Jagged Intelligence（AI 能力不均衡现象）

## 1. 定义与核心原理

Jagged Intelligence 由 [[andrej_karpathy_大牛_ai大牛|andrej_karpathy_大牛_ai大牛]] 在 2026 年 Sequoia AI Ascent 演讲中提出，描述当前 AI 系统（尤其是 LLM）的一个根本性特征：

> **AI 的能力是"锯齿状"的——在某些领域表现超人类，在相邻领域却意外地差，中间没有平滑过渡。**

传统软件的特点是**自动化能被精确指定的行为**；AI/LLM 的特点是**自动化能被验证的行为**。两者并不等价，因此产生了 Jagged Intelligence 现象。

**核心区分：**
- 传统软件：Spec → 执行（精确映射）
- LLM：大量数据训练 → 能力涌现（不可精确预测哪些能力会涌现、哪些不会）

## 2. 关键技术路线与变体

### 2.1 表现形态

| 维度 | AI 表现 | 例子 |
|------|---------|------|
| **可验证任务** | ✅ 超人类 | 代码补全、翻译、格式整理、数学计算（封闭问题） |
| **需要外部工具** | ✅ 可靠 | 网页搜索、API 调用、代码执行 |
| **模糊/开放式** | ❌ 不可靠 | 开放式创意写作、商业判断、复杂谈判 |
| **长程一致性** | ❌ 退化 | 复杂项目的多模块协同、跨阶段状态保持 |
| **精确事实记忆** | ❌ 不可靠 | 日期、数字、专有名词（幻觉问题） |

### 2.2 在 Agentic Engineering 中的意义

[[agentic_engineering_调度智能体的工程范式|agentic_engineering_调度智能体的工程范式]] 的关键前提：只有把任务落在 AI"可验证区间"，agentic 工作流才能可靠运行。

Karpathy 的核心结论：**越是可验证的任务，AI 越强；越是模糊开放的任务，AI 越需要人类守着。**

这对[[判断力_judgment|判断力_judgment]]的要求：工程师必须知道当前任务的 Jaggness——即知道 AI 在哪个区段可靠、哪个区段不可靠，并在不可靠处加大人工监督强度。

## 3. 行业应用场景

- **投流助手/AI 决策工具**：CPC/ROI 等数值指标明确的优化任务落在"可验证区间"——适合 agentic 自动化；品牌调性、竞争策略等模糊判断落在"锯齿断裂处"——需要人类把关
- **AI Coding 工具**：代码补全（高可信）vs 架构建议（低可信）；单元测试生成（高可信）vs 系统设计（低可信）
- **AI 医疗/法律**：诊断建议（高可信区间）vs 综合法律策略（开放域，风险高）

## 4. 代表性来源

- 演讲原文：[karpathy.bearblog.dev/sequoia-ascent-2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/)
- 对应视频：YouTube "Andrej Karpathy: From Vibe Coding to Agentic Engineering"

## 5. 争议与开放问题

- **Jagged Intelligence 是暂时还是永久？** 随着模型能力提升，锯齿会被磨平吗？还是说能力不均衡是 Transformer 架构的本质局限？
- **\"可验证\"的标准也在动态变化**：曾经不可验证的任务（如蛋白质结构预测）后来有了 AlphaFold 这样的验证手段——这意味着 AI 能做的事的边界本身在扩展
- **企业落地误区**：很多企业把 AI 当作"在所有任务上都比人强或比人差"来评估，忽视了 Jaggness——导致在错误的任务上部署 AI（高风险场景用 AI 做决策，低风险场景反而用人工）
