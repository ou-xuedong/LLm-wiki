---
title: Sub-agent隔离机制
created: 2026-05-01
updated: 2026-05-01
type: concept
tags:
  - #概念
  - #Agent
  - #架构设计
  - #上下文管理
confidence: high
---

# Sub-agent隔离机制


## 关联

**上位概念**：[[harness_工程]]
**相关概念**：[[harness_工程]], [[上下文自动压缩]], [[agentic_search]]

# 🔒 Sub-agent 隔离机制（Agent Isolation）

## 1. 定义

**Sub-agent 隔离机制**是 Agentic Harness 中最优雅的设计模式之一：遇到大范围搜索/执行任务时，主控 Agent 不亲自下场，而是派生出一个只具备读取权限的 Explore 子 Agent，在独立上下文中处理大量中间检索日志，最终只向主进程返回一段高信息密度的结论。

## 2. 解决的问题

多轮搜索/执行场景下的**中间过程污染**问题：
- 大量 Grep/Read 结果涌入主 Context
- 无用信息稀释关键结论
- 主 Agent 被中间日志淹没，无法有效决策

## 3. 机制原理

```
主控 Agent（接收任务）
    ↓ 派生
Explore 子 Agent（独立上下文）
    ↓ 执行大量搜索/读取
中间检索日志（子 Agent 自行消化）
    ↓
高信息密度结论（返回主进程）
    ↓
主 Agent 继续下一步决策
```

关键设计原则：
- **只读权限**：子 Agent 不可写文件、不可执行危险命令
- **独立上下文**：中间日志不进入主 Context
- **结论过滤**：只返回最终结论，中间过程被截断

## 4. 对主人方向（亚马逊投流 Agent）的映射

多账号投流管理场景天然适合 Sub-agent 隔离：

```
主控 Agent（投流策略决策）
    ↓ 派生子 Agent
子 Agent 1 → 账号 A 关键词优化
子 Agent 2 → 账号 B 预算调整
子 Agent 3 → 账号 C 竞品监控
    ↓ 各子 Agent 独立执行
精简结论汇报（关键词调整建议/预算变动/竞品动态）
    ↓
主 Agent 汇总决策
```

优点：
- 各账号任务相互隔离，不会相互污染 Context
- 并行执行，效率更高
- 单个子 Agent 失败不影响全局
