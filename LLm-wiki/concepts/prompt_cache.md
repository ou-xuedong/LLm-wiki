---
title: Prompt
created: 2026-05-01
updated: 2026-05-01
type: concept
tags:
  - #概念
  - #Context管理
  - #Agent
  - #Token优化
confidence: high
---

# Prompt


## 关联

**上位概念**：[[harness_工程]]
**相关概念**：[[harness_工程]], [[上下文自动压缩]], [[sub-agent隔离机制]]

# ⚡ Prompt Cache（提示词缓存策略）

## 1. 定义

**Prompt Cache** 是 Agentic Harness 的核心 Token 优化机制：将 System Prompt 等静态背景内容切块，利用 API 的缓存机制实现重复复用，将重复计算成本压降 **80%+**。

## 2. 核心原理

Agentic 循环中，多轮对话的前缀（System Prompt、项目背景、工具定义）高度重合：
- 每次请求都重新计算相同的前缀 Token
- Prompt Cache 将这些静态前缀缓存，只对每次变化的对话部分计费

## 3. 效果

- 成本降低：80%+（官方数据）
- 延迟改善：减少重复的前缀计算
- API 计费优化：对高频调用的 Agent 场景效果显著

## 4. 适用场景

- 多轮对话 Agent（客服、助手）
- 代码搜索/重构（Claude Code 等长时间任务）
- 工作流自动化（需要多步骤迭代的任务）

## 5. 与 Context Auto-compaction 的区别

| 维度 | Prompt Cache | Context Auto-compaction |
|------|-------------|------------------------|
| 作用 | 避免重复计算静态前缀 | 压缩超限的动态上下文 |
| 时机 | 每次请求前检查缓存 | Token 逼近阈值时触发 |
| 对象 | System Prompt 等静态内容 | 多轮对话的动态上下文 |
| 效果 | 成本降低 80%+ | 腾出空间继续新任务 |
