---
title: System
created: 2026-04-17
updated: 2026-04-17
type: concept
tags:
  - #概念
  - #企业服务
  - #AI壁垒
confidence: high
---

# System


## 关联

**上位概念**：[[Enterprise-Software|Enterprise_Software]]
**相关概念**：[[context_graph|context_graph]], [[System-of-Record|System_of_Record]], [[亚马逊投流决策助手|亚马逊投流决策助手]]

# 🧠 System_of_Decision

## 1. 定义与核心原理
决策型系统（System of Decision/Action）是指不仅仅记录业务终态（如审批通过、金额修改），而是深入业务工作流（Write Path），通过 AI Agent 的提案与人类用户的干预（修改、驳回、批准），捕获“为何做出该决策”的完整逻辑与推理轨迹的软件系统。

## 2. 关键技术路线与变体
- **基于 Agent 的工作流拦截**：在人类与业务系统交互的中间层插入 Agent，捕捉人类修正意见。
- **上下文图谱（Context Graph）构建**：将人类直觉、政治考量、隐性经验结构化，转化为可复用的机器资产。

## 3. 行业应用场景
- 复杂商务谈判审批（折扣为何设定为20%）。
- 医疗诊断与异常升级（为何不走常规流程）。
- 跨境电商/广告投流等经验密集型运营决策（如[[亚马逊投流决策助手|亚马逊投流决策助手]]）。

## 4. 代表性论文/项目
- 暂无特定开源项目，属于新一代 SaaS 的理念高地。

## 5. 争议与开放问题
- 隐私与权限控制：隐性决策往往涉及敏感数据与内部政治，如何实现“有权限的推理（Permissioned Inference）”是技术难点。
