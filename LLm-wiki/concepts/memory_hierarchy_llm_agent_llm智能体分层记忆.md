---
title: Memory
created: 2026-05-09
updated: 2026-05-09
type: concept
tags:
  - #概念
  - #Agent
  - #记忆系统
  - #认知科学
  - #具身智能
confidence: high
---

# Memory


## 关联

**上位概念**：[[agentic_memory_architecture_智能体记忆架构]]
**相关概念**：[[memory_trilemma_selective_grounded_efficient_记忆三约束三元悖论]], [[memory_loop_six_stage_六阶段记忆闭环]], [[agent记忆系统设计三大支柱收束论]], [[context_window_and_memory_architecture_上下文窗口与记忆架构]], [[human-like_memory_类人记忆插件]], [[gbrain_ai记忆系统]]

# 🧠 LLM 智能体分层记忆（Working / Episodic / Semantic + 机器人侧反哺）

> 一句话：认知科学 + 计算机系统 + 机器人侧（PI MEM）三条独立学科线汇聚到同一答案——**有限带宽下，近的事情细节重要，远的事情结构重要**，所以记忆必须分层。

## 1. 定义与核心原理（双线汇聚 + 信息论必然）

两条独立学科线 + 一条机器人侧线汇聚到同一答案：

### 1.1 认知科学（Baddeley 工作记忆模型，1974 至今）

| 类型 | 容量 | 时间 | 特征 |
|---|---|---|---|
| **Working memory（工作记忆）** | ~7 项 | 秒级 | 精细 |
| **Long-term memory（长时记忆）** | 无限 | 天~年级 | 抽象 |

### 1.2 计算机系统（Memory hierarchy，50 年代至今）

```
L1/L2 cache → RAM → SSD → HDD
容量↑、速度↓、成本↓
```

### 1.3 机器人侧（PI MEM 架构）

PI 的 MEM = **短时视频编码（精细、秒级、高带宽）+ 长时语言摘要（抽象、分钟~小时级、低带宽）**。

LLM Agent 的 "recent context + selected key frames" 也是同构设计。

### 1.4 这不是巧合，是信息论必然

> **有限带宽下，近的事情细节重要，远的事情结构重要。**

## 2. 关键技术路线与变体（LLM Agent 的三层结构）

### 2.1 三层结构

| 层级 | 存什么 | 保留粒度 | 生命周期 | 对应实现 |
|---|---|---|---|---|
| **L1: 工作记忆（working memory）** | 当前对话、当前任务、工具返回 | 原始 token | 本轮~本任务 | prompt 里的 recent turns |
| **L2: 情节记忆（episodic memory）** | 完整的历史任务/对话片段 | 压缩摘要 + 关键原文 | 天~周 | 向量库 + 结构化字段 |
| **L3: 语义记忆（semantic memory）** | 用户偏好、事实、技能 | 高度抽象的键值对或规则 | 持久 | KV store / knowledge graph / skill library |

### 2.2 写入流

```
原始事件 → L1 (全保留)
任务结束 → L1 压缩 → L2 (摘要 + 关键片段)
L2 积累到阈值 → 归纳 → L3 (抽取偏好/事实/技能)
```

### 2.3 读取流

每轮决策**三层都查**，但**预算分配不同**：

```
总预算 8K token:
  L1: 4K  (最新 5 轮对话原文)
  L2: 3K  (近一周内相关 episode 的摘要,top-3)
  L3: 1K  (用户长期偏好,全量注入)
```

## 3. 机器人给 LLM Agent 的三个反哺启发（核心价值）

### 3.1 启发一：L2 不等于"一坨向量"

PI 的 MEM 把长时记忆做成**自然语言摘要**，这比向量 embedding 强在哪？

| 维度 | 向量 embedding | 自然语言摘要 |
|---|---|---|
| 可读 | ❌ 人不能审计 | ✅ 人能审计 |
| 可编辑 | ❌ 错了也改不动 | ✅ 错了能改 |
| 可组合 | ❌ 向量加减没意义 | ✅ 摘要 + 摘要 = 新摘要 |
| LLM 友好 | ⚠️ 要训 encoder | ✅ 天然被 LLM 理解 |

**反哺**：LLM Agent 的 L2 应该是**"摘要为主，向量为辅索引"**，而不是反过来。

### 3.2 启发二：L1 和 L2 之间的压缩应该是学出来的

机器人里"短时视频怎么压到长时摘要"是**神经网络做的（可学）**。LLM Agent 里这一步常常是 **hand-crafted（人工写规则）**——"最近 10 轮，每轮超过 200 字就截断"。应该换成让模型学"什么值得留"。

**反哺**：把 **memory compression（记忆压缩）当作一个可训练模块**，用 downstream task（下游任务）loss 反传训练。

### 3.3 启发三：跨层 attention（这个 LLM Agent 完全没做）

机器人里**当前控制步的 attention 同时访问 L1 + L2，带不同的 gate（门控）**。LLM Agent 现在是"把三层平铺拼进 prompt 让 LLM 自己区分"，**效率低**。

真正的架构级做法应该是**给 attention layer 多头分工**：
- 一部分头看 L1
- 一部分看 L2
- 一部分看 L3
- 各自有不同的 positional encoding（位置编码）和 dropout

## 4. 行业应用场景（陷阱与反模式）

| # | 陷阱 | 正解 |
|---|---|---|
| 1 | 分层但不分 budget（预算） | 三层共用一个 context，高频 L1 吃满了 L2/L3 就废了；必须**给每层独立预算上限**（详见 [[memory_trilemma_selective_grounded_efficient_记忆三约束三元悖论]] §3.3） |
| 2 | consolidation（巩固）只从 L1 到 L2，没有从 L2 到 L3 | L2 越长越胖，**抽象层（L3）永远不成形**；必须有 L2→L3 的归纳通路（详见 [[memory_loop_six_stage_六阶段记忆闭环]] §2.6） |
| 3 | 三层的 query（查询）用同一个 embedding | 应该不同层用不同查询方式——**L1 按时间近度，L2 按语义相似，L3 按键直查** |

## 5. 代表性论文/项目（同主题映射）

- **上位框架**：[[agentic_memory_architecture_智能体记忆架构]] 已有"Working/Episodic/Semantic 三层"基础认知；本卡补足"如何分预算 + 如何巩固 + 机器人侧反哺"
- **同主题三件套**：[[memory_trilemma_selective_grounded_efficient_记忆三约束三元悖论]]（每次 retrieve 的判据）+ [[memory_loop_six_stage_六阶段记忆闭环]]（store/retrieve 的时机）+ 本卡（memory bank 内部如何组织）
- **收束总览**：[[agent记忆系统设计三大支柱收束论]]
- **典型实现对照**：
  - [[human-like_memory_类人记忆插件]] 的"三类记忆分而治之 Semantic/Episodic/Procedural"是这套分层在产品上的落地
  - [[gbrain_ai记忆系统]] 的"已整理事实 + 时间线"是 L2/L3 的简化版
  - [[context_window_and_memory_architecture_上下文窗口与记忆架构]] 提供了 L1 上下文窗口的物理边界讨论

## 6. 争议与开放问题

- **L2 摘要 vs 向量的混合权重**：摘要为主、向量为辅索引——但比例怎么定？
- **可训练压缩模块的训练数据来源**：downstream task 是哪个 task？任务分布漂移时怎么重训？
- **跨层 attention 的工程实现**：multi-head 分工是模型架构改造（动 Transformer 层），现有 LLM API 不支持——这是开源 Agent 自训模型的机会窗
- **L3 语义记忆的边界**：知识图谱 vs KV store vs skill library 三种实现选哪种？混合用如何治理？

## 7. 信息来源

主人 2026-05-09 体系化整理（整合认知科学 Baddeley 1974、计算机系统 Memory hierarchy、机器人具身侧 PI MEM 架构三条线索的结论）。本卡是"Agent 记忆系统设计三大支柱"之一。
