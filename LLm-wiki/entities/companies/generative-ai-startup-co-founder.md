---
title: Generative-AI-Startup-Co-Founder
created: 2026-05-01
updated: 2026-05-01
type: companies
tags:
  - #开源项目
  - #创业分析
  - #Multi-Agent
  - #Ollama
  - #MCP
---

# Generative-AI-Startup-Co-Founder


## 关联


# Generative-AI-Startup-Co-Founder

## 1. 核心定位与业务模式

Multi-agent AI 系统，自动生成完整创业分析报告——从创意评估、市场调研、财务预测、法律合规到 Pitch Deck 和战略规划，**一键端到端输出**。

核心理念：用 AI 替代重复性创业文档工作，让创始人聚焦核心决策。

## 2. 核心架构

### 技术栈
- **运行时**：Ollama（本地 LLM，无需云端）
- **协议**：MCP（Model Context Protocol）工具调用
- **前端**：Streamlit（Python Web UI）
- **数据校验**：Pydantic v2

### Agent 分工（agents/）
多角色 Agent 协同，各司其职：
- 创意评估 Agent
- 市场调研 Agent
- 财务建模 Agent
- 法律合规 Agent
- Pitch Deck 生成 Agent
- 战略规划 Agent

### 工具层（tools/）
MCP 工具集，封装外部能力供各 Agent 调用。

## 3. 输出产物

| 产物 | 说明 |
|------|------|
| 创意分析 | 问题 / 解决方案 / 市场匹配度 |
| 市场调研报告 | TAM / SAM / SOM / 竞争格局 |
| 财务模型 | 收入预测 / 成本结构 / 单元经济 |
| 法律合规清单 | 股权 / IP / 监管注意事项 |
| Pitch Deck | 投资人版商业计划书 |
| 战略路线图 | 里程碑 / 资源需求 / 风险点 |

## 4. 与主人方向关联

- **Multi-agent 协作架构**：多个专业 Agent 分工 → 可参考投流 Agent 的"竞品分析 / 关键词研究 / 出价策略 / 数据洞察"多 Agent 分工模式
- **一键生成完整报告**：与投流场景"输入Campaign目标，输出完整投流方案"思路相通
- **本地 LLM 优先**：Ollama 本地运行，成本可控，适合投流 Agent 的成本敏感场景

## 5. 项目状态

- GitHub：Saransh0412/Generative-AI-Startup-Co-Founder
- ⭐ 1 Star
- Commits：5
- 状态：早期起步
