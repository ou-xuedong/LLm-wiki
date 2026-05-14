---
title: GBrain
created: 2026-05-09
updated: 2026-05-09
type: concept
tags:
  - #概念
  - #AgentInfra
  - #Memory
---

# GBrain


## 关联

**上位概念**：[[Agent Infra]]
**相关概念**：[[Context_Graph]], [[MCP]], [[Human-like_Memory_类人记忆插件]], [[Memory_Loop_Six_Stage_六阶段记忆闭环]], [[Agent记忆系统设计三大支柱收束论]]
**关键人物**：[[Garry Tan]], [[OpenClaw]]

# 🧠 GBrain_AI记忆系统

## 1. 定义与核心原理
GBrain 是由 YC 总裁 Garry Tan 开源的生产级个人 AI 记忆系统（第二大脑）。它的核心思路是：让 AI Agent 拥有一个持续成长的知识库，在每次回答问题前先读取该知识库，对话结束后再写入新内容。通过所谓的“梦境循环（Dream Cycle）”，Agent 能够在后台自动扫描对话、补充缺失实体、修复断开的引用，从而将知识内化并产生复利效应。

核心数据结构遵循“已整理事实 + 时间线”：
- **已整理事实（上方）**：对某件事的最佳理解，整体重写。
- **时间线（下方）**：证据和历史记录，只追加，永不修改。

## 2. 关键技术路线与变体
- **存储方案**：默认使用 PGLite（基于 WASM 的嵌入式 Postgres 17.5），实现本地零配置运行。数据量大时支持一键迁移至 Supabase。
- **检索架构**：采用三层混合搜索：
  1. 多查询扩展（如 Claude Haiku 改写查询）。
  2. 向量搜索（HNSW余弦相似度）+ 关键词搜索（tsvector）。
  3. RRF融合排名与四层去重（最优分块、相似度合并、多样性上限等）。
- **接入协议**：原生支持 MCP 协议（Model Context Protocol），暴露 30 个 MCP 工具（如 `get_page`, `put_page`, `search`, `sync_brain`），可无缝对接 OpenClaw、Hermes、Claude Code、Cursor 等。

## 3. 行业应用场景
- **个人迷你 AGI**：将会议记录、邮件、推文、日历、语音等整合汇入知识库（自带 Voice/Email/X/Calendar-to-Brain 集成）。
- **社交图谱分析**：交叉检索人物关系（如查询“谁同时认识A和B”）。
- **上下文备忘**：基于历史数据进行会议准备或回顾思考历程。

## 4. 代表性论文/项目
- **GBrain 官方仓库**：[https://github.com/garrytan/gbrain](https://github.com/garrytan/gbrain) (MIT协议)
- **Garry Tan 的 Gstack**：GBrain 配合使用的工程框架，涉及 Agent 的技能库（ingest, query, maintain, enrich, briefing, migrate）。

## 5. 争议与开放问题
- 依赖强算力模型：目前推荐搭配 Claude Opus 4.6 和 GPT-5.4 Thinking 等大模型，较小模型由于指令遵循或上下文处理能力有限，可能无法很好地运行该系统。
