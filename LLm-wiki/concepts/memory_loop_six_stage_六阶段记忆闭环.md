---
title: Memory
created: 2026-05-09
updated: 2026-05-09
type: concept
tags:
  - #概念
  - #Agent
  - #记忆系统
  - #设计方法论
confidence: high
---

# Memory


## 关联

**上位概念**：[[Agentic_Memory_Architecture_智能体记忆架构]]
**相关概念**：[[Memory_Trilemma_Selective_Grounded_Efficient_记忆三约束三元悖论]], [[Memory_Hierarchy_LLM_Agent_LLM智能体分层记忆]], [[Agent记忆系统设计三大支柱收束论]], [[Hermes_Agent]], [[GBrain_AI记忆系统]], [[Anthropic自举飞轮_Claude Code开发Claude Code]], [[自进化AI_RSI]]

# 🧠 六阶段记忆闭环（observe → store → retrieve → ground → act → improve）

> 一句话：Agent 记忆系统的完整持续学习闭环包含六阶段，多数 LLM Agent 只跑了前三步，后三步要么缺失要么被简化成副作用。

## 1. 定义与核心原理

这是一个 **六阶段的持续学习闭环（continual learning loop）**。多数 LLM Agent 只跑了前三步（observe-store-retrieve），后三步（ground-act-improve）要么缺失要么被简化成副作用。

### 1.1 典型系统覆盖阶段对比

| 系统 | 覆盖阶段 |
|---|---|
| **RAG**（retrieval-augmented generation，检索增强生成） | observe → retrieve → act（缺 store / ground / improve） |
| **MemGPT / Letta** | observe → store → retrieve → act（缺 ground / improve） |
| **Voyager**（2023 的 Minecraft agent） | observe → store → retrieve → act → improve（缺 ground） |
| **Generative Agents**（2023 斯坦福小镇） | observe → store → retrieve → act → improve（ground 很弱） |
| **本卡六阶段路线** | 全六阶段都有 |

## 2. 关键技术路线与变体（六阶段逐一讲）

### 2.1 observe（感知）

收集当前状态。LLM Agent 里对应"当前用户输入 + 工具返回 + 环境反馈"。

**关键设计**：区分 **signal vs noise**——并不是所有观测都值得存。

### 2.2 store（写入）

决定"存什么 / 存到哪一层"：

| 存储目标 | 内容类型 |
|---|---|
| **short-term buffer（短时缓冲）** | 原始信号 |
| **long-term memory（长时记忆）** | 跨任务有用的摘要 |
| **skill library（技能库）** | 技能/成功模式（Voyager 的贡献） |

具体分层结构详见 [[Memory_Hierarchy_LLM_Agent_LLM智能体分层记忆]]。

### 2.3 retrieve（召回）

就是 [[Memory_Trilemma_Selective_Grounded_Efficient_记忆三约束三元悖论]] 讲的 **selective router**（选择性路由器）——按当前任务定向召回，而非 cosine top-k。

### 2.4 ground（锚定）

就是约束 1 讲的 **grounded 对齐**——把召回的记忆与当前上下文做结构化映射。

> **这是多数 LLM Agent 缺失或薄弱的关键环节**。现状是 retrieve 完直接拼 prompt，没有把记忆与当前问题的具体锚点（参数位置 / token 位置 / 关系字段）显式连起来。

### 2.5 act（执行）

基于 **当前状态 + 召回记忆 + grounding 锚点** 产出动作。这一步没什么新鲜的，LLM Agent 都会做。

### 2.6 improve（自我改进）

**这是多数 Agent 最薄弱的一环**，包含三种机制：

| 机制 | 具体做法 | 什么时候用 |
|---|---|---|
| **Memory rewrite（记忆重写）** | 执行完一步，把"这次召回的记忆 + 当前观测 + 结果"写回 bank，可能更新原记忆的置信度 | 每步都做 |
| **Memory consolidation（记忆巩固）** | 离线阶段把最近 N 条记忆压缩成高层摘要，类似睡眠期海马→皮层的巩固过程 | 低峰期/定期批处理 |
| **Skill distillation（技能蒸馏）** | 多条成功轨迹 → 归纳出一条可复用"技能"，以代码/prompt/策略形式存进 skill library | 成功模式重复出现时 |

## 3. 行业应用场景（落到 LLM Agent 的具体例子）

假设做一个 **coding agent（编程智能体）**，完整六阶段闭环：

```
observe : 用户说"给我写个 K8s 部署脚本，像上次那个项目的风格"

store   : buffer 存原始输入；检测到"像上次"触发 long-term 检索意图

retrieve: task-aware router 从 memory bank 召回 3 条候选
          - episode #47: 上次的 K8s 脚本
          - episode #23: 上次用的镜像 registry
          - episode #91: 用户偏好 2 replicas 而不是 3

ground  : 把 episode #47 的 yaml 结构对齐到当前任务的参数位置
          (service name/port/image 等字段级别的映射，不是整段粘贴)

act     : 生成脚本，用 grounding 结果填入具体字段

improve : 用户说"完美，但 replicas 我现在想要 5"
          → memory rewrite: 把 episode #91 的"偏好 2 replicas"改为"偏好可变，默认 5"
          → 下次召回时新偏好生效
```

**注意 improve 这一步**——90% 的 Agent 现在做完 act 就结束了，用户反馈只进了当轮 context，**没进 memory**。这就是"**失忆型 Agent**"。

## 4. 代表性论文/项目（陷阱与反模式）

| # | 陷阱 | 正解 |
|---|---|---|
| 1 | 把 store 写死为"每轮都存全部" | 会导致 memory bank 被低价值日志淹没；要加 signal/noise 筛选 |
| 2 | improve 只有 reinforcement（强化正反馈）没有 correction（修正负反馈） | "用户说这次不对"比"用户说完美"信息量大得多，但大多数系统不记 |
| 3 | 闭环开太慢 | 机器人是每毫秒闭一次，LLM Agent 常常每轮才闭一次——应该在**单轮内也能闭环**（一次工具调用失败后，立刻修正 memory 再重试） |

## 5. 与同类概念的关系

- **同主题三件套**：[[Memory_Trilemma_Selective_Grounded_Efficient_记忆三约束三元悖论]]（retrieve 时的判据）+ [[Memory_Hierarchy_LLM_Agent_LLM智能体分层记忆]]（store/retrieve 的对象）+ 本卡（阶段与时机）
- **收束总览**：[[Agent记忆系统设计三大支柱收束论]]
- **类似闭环理念**：[[Anthropic自举飞轮_Claude Code开发Claude Code]] 是 Anthropic 内部的"开发→反馈→改进"自举闭环；[[自进化AI_RSI]] 是把 improve 这一步做到极致的递归自我提升
- **关联典型实现**：[[Hermes_Agent]]（improve 阶段的反馈驱动迭代）、[[GBrain_AI记忆系统]]（梦境循环 = consolidation 巩固机制）

## 6. 争议与开放问题

- **improve 的频次**：单轮内闭环 vs 每 N 轮闭环 vs 离线批处理，三种节奏的工程权衡
- **memory rewrite 的写入策略**：every-step 写所有 / 只在用户显式反馈时写 / 用户隐式信号（如继续对话不抱怨 ≈ 默认满意）
- **skill distillation 的触发阈值**：几条成功轨迹算"重复出现"？过早归纳会过拟合，过晚归纳错失复用
- **闭环错误传播**：错误的记忆被 rewrite/consolidate 后会污染 bank，如何防止"幻觉传染"？

## 7. 信息来源

主人 2026-05-09 体系化整理（对比 RAG / MemGPT / Voyager / Generative Agents 等典型系统后形成的六阶段判据）。本卡是"Agent 记忆系统设计三大支柱"之一。
