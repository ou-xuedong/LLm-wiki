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

**上位概念**：[[agentic_memory_architecture_智能体记忆架构|agentic_memory_architecture_智能体记忆架构]]
**相关概念**：[[memory_loop_six_stage_六阶段记忆闭环|memory_loop_six_stage_六阶段记忆闭环]], [[memory_hierarchy_llm_agent_llm智能体分层记忆|memory_hierarchy_llm_agent_llm智能体分层记忆]], [[agent记忆系统设计三大支柱收束论|agent记忆系统设计三大支柱收束论]], [[context_window_and_memory_architecture_上下文窗口与记忆架构|context_window_and_memory_architecture_上下文窗口与记忆架构]], [[human-like_memory_类人记忆插件|human-like_memory_类人记忆插件]], [[prompt_cache|prompt_cache]], [[上下文自动压缩|上下文自动压缩]]

# 🧠 记忆三约束三元悖论（Selective / Grounded / Efficient）

> 一句话：好的 Agent 记忆系统必须同时满足"只召回真正相关的少数证据 + 召回内容能锚定到当前上下文 + 在固定预算内完成"三个互相挤压的约束。

## 1. 定义与核心原理（Trilemma 本质）

这三个约束**不是并列的"最佳实践"，它们构成一个三元悖论（trilemma）**——你总是在三者之间做权衡。

| 约束 | 含义 |
|---|---|
| **Selective（选择性）** | 只召回对当前决策真正相关的少数证据 |
| **Grounded（可锚定）** | 召回的证据必须能对齐到当前上下文的具体锚点 |
| **Efficient（预算内）** | 在固定 token 预算和固定延迟预算内完成 |

**为什么是 trilemma**：
- Selective 要求做判断（判断要花算力，违反 Efficient）
- Grounded 要求保留足够原始细节做对齐（保留细节违反 Efficient）
- Efficient 要求压缩（压缩就丢信息，违反前两者）

好的记忆系统就是**在三者间画出一条合理曲线**。

## 2. 关键技术路线与变体

### 2.1 反模式（多数 LLM Agent 现状）

```
用户输入 → embedding → 向量库 top-k 检索 → 拼进 prompt → LLM 输出
```

对应三约束的表现：

| 约束 | 现状表现 |
|---|---|
| Selective | top-k 是 **passive 的**（被动），基于"语义相似"而非"任务相关" |
| Grounded | 几乎没有——retrieved chunks（召回的段落）跟当前问答的具体位置没有显式对齐 |
| Efficient | 无预算意识——top-k 直接拼 prompt，context 越涨越胖 |

### 2.2 应该长什么样：task-aware router + grounded retrieval + budgeted composition 三件套

```python
# 伪代码，不是完整实现
def memory_step(current_state, task, memory_bank, budget):
    # --- 1. Selective: task-aware router 而不是 cosine top-k ---
    query = build_query(current_state, task)
    candidates = memory_bank.coarse_filter(query, k=100)
    scores = task_aware_router(query, candidates)   # 学出来的，不是余弦
    selected = top_k_by_score(scores, k=5)          # 固定数量

    # --- 2. Grounded: 把召回的东西锚定到当前上下文 ---
    anchored = []
    for mem in selected:
        link = grounding_head(mem, current_state)   # 显式输出对齐关系
        anchored.append((mem, link))                # link 可以是对象 id/文档位置

    # --- 3. Efficient: 预算化组合,不是全堆 ---
    recent = current_state.recent_context(tokens=budget.recent)     # 近期
    long_term = render(anchored, tokens=budget.long_term)            # 长期
    assert recent.tokens + long_term.tokens <= budget.total

    return recent + long_term
```

## 3. 关键设计决策（做 Agent 记忆必须想清楚的三件事）

### 3.1 决策 A：Router 怎么训？

| 难度 | 方法 | 描述 |
|---|---|---|
| 最简单 | **蒸馏法** | 用大 LLM 当 oracle（神谕）给"这条 memory 对这个任务有用吗"打分，用小 router 去拟合 |
| 中等 | **对比学习** | 成功轨迹里被用到的记忆是正样本，没用到的是负样本 |
| 高级 | **端到端 BC（behavior cloning，行为克隆）或 RL** | 让 router 的检索结果直接影响最终输出的损失 |

### 3.2 决策 B：Grounding 怎么表达？

- **文本 Agent**：可以用 **span-level citation（段落级引用）**——retrieved chunk（召回的段落）里的 token 要能显式映射到 output（输出）里的 token 位置
- **工具调用 Agent**：retrieved memory 要显式标记它对应本次调用的哪个参数
- **通用原则**：grounding 必须是**结构化关系**，不是模糊的"相关"

### 3.3 决策 C：预算怎么分？

**典型分法**：

```
总预算 = 系统提示 + 任务描述 + 最近 N 轮（recent context）+ 长期召回（retrieved long-term）
```

**关键**：把预算当**硬约束**，超了就压缩或 evict（淘汰），不要靠"反正 context 还没满"。

## 4. 行业应用场景（陷阱与反模式）

| # | 陷阱 | 正解 |
|---|---|---|
| 1 | 把"向量库规模"当记忆能力指标 | 规模不是核心，**router 质量**才是 |
| 2 | grounding 做成事后的 citation UI | 应该是**架构级组件**，影响 loss |
| 3 | 预算靠"动态伸缩"（context 不够就扩） | 这等于没预算，会崩在长任务上 |

## 5. 代表性论文/项目（同主题映射）

- **上位框架**：[[agentic_memory_architecture_智能体记忆架构|agentic_memory_architecture_智能体记忆架构]]——本卡是其"如何设计 retrieve"的具体判据
- **同主题三件套**：[[memory_loop_six_stage_六阶段记忆闭环|memory_loop_six_stage_六阶段记忆闭环]]（定义"何时 retrieve 何时 store"）+ [[memory_hierarchy_llm_agent_llm智能体分层记忆|memory_hierarchy_llm_agent_llm智能体分层记忆]]（定义"memory bank 内部如何组织"）+ 本卡（定义"retrieve 那一刻的判据"）
- **收束总览**：[[agent记忆系统设计三大支柱收束论|agent记忆系统设计三大支柱收束论]]
- **典型实现**：[[human-like_memory_类人记忆插件|human-like_memory_类人记忆插件]] 的"三类记忆分而治之 + 程序性精确匹配"是本约束在产品上的体现
- **预算约束工程化**：[[prompt_cache|prompt_cache]]、[[上下文自动压缩|上下文自动压缩]] 是 Efficient 约束的具体技术

## 6. 争议与开放问题

- **task-aware router 的训练数据从哪来？** 蒸馏法依赖大 LLM 当 oracle，但 oracle 是否真的判断准确？
- **grounding 的颗粒度怎么选？** span-level / chunk-level / document-level 之间的工程权衡
- **预算分配是否应该动态？** 简单任务可能不需要 long_term，复杂任务可能需要更大 recent——硬预算 vs 自适应预算的边界

## 7. 信息来源

主人 2026-05-09 体系化整理。本卡是"Agent 记忆系统设计三大支柱"之一，配套 [[memory_loop_six_stage_六阶段记忆闭环|memory_loop_six_stage_六阶段记忆闭环]] + [[memory_hierarchy_llm_agent_llm智能体分层记忆|memory_hierarchy_llm_agent_llm智能体分层记忆]] + [[agent记忆系统设计三大支柱收束论|agent记忆系统设计三大支柱收束论]] 共同构成完整设计判据。
