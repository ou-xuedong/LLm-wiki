---
title: MindrianOS
created: 2026-04-28
updated: 2026-04-28
type: companies
tags:
  - #开源项目
  - #AI创新方法论
  - #知识图谱
  - #Claude_Code插件
---

# MindrianOS


## 关联


# MindrianOS（AI 创新联合创始人）

## 1. 核心定位与业务模式

MindrianOS 是 **面向创新者的 AI 协作插件**，核心理念："你的项目需要一个联合创始人。"

由 Jonathan Sagir 构建，基于 **PWS（Practical Innovation Methodology）**——30+ 年约翰霍普金斯大学沉淀的实战方法论。不是一个聊天机器人，而是一个**会主动挑战你思维盲区的 AI 导师**，帮你发现自己看不到的联系和空白。

**核心场景**：联邦提案、企业 VC 提案、创新流程诊断

## 2. 核心架构

### Larry — 思想伙伴
不是 chatbot，是**教学型 Agent**：
- 会主动质疑你的假设："你以为这是个 marketplace 问题，但如果它其实是物流问题呢？"
- 26 种 PWS 框架内化于对话中
- 透明展示思考过程（问题类型→选定框架→原因）
- 在你见投资人之前，主动告诉你"你论证里哪个环节最弱"

### Data Room — 自我组织的情报室
每个 Room = 文件系统 + 智能层 + 跨关系扫描，全部本地化。

| Section | 内容 |
|---------|------|
| problem-definition/ | 真正值得回答的问题 |
| market-analysis/ | 谁有这个痛点、有多痛 |
| solution-design/ | 技术方案 |
| business-model/ | 如何盈利 |
| competitive-analysis/ | 竞争格局 |
| opportunity-bank/ | 发现的融资/合作机会 |

### 知识图谱引擎
- 本地 SQLite 图数据库（room.db）
- 关系类型：INFORMS / CONTRADICTS / CONVERGES / INVALIDATES
- **查询成本**：约 3,500 tokens（精准图查询 + 片段摘录）vs 200,000 tokens（全量扫描）
- **57 倍成本优势**（实测数据）

### Opportunity Bank
每次方法论会话都往里面添加发现，持续复合增长：
-Whitespace 分析（77 个方法论框架对照你的思维空白）
- 隐藏联系发现（跨领域意外模式）
- 反向瓶颈识别（系统哪部分落后于整体）
- 创新评分（哪些跨界组合未被充分开发）

## 3. 技术栈

- **语言**：Node.js（≥22.5.0）+ Python（HISI 跨文档智能可选）
- **平台**：Claude Code CLI（全功能）/ Claude Desktop（对话式）/ Cowork（团队共享）
- **插件生态**：Marketplace + 手动安装
- **权限设计**：仅读 workspace，写仅限 ~/MindrianRooms/ 和 ./.mindrian/
- **无云依赖**：数据全部本地，不上传 brain.mindrian.ai

## 4. 核心数据

| 指标 | 数值 |
|------|------|
| Commands | 71+ |
| Skills | 10 |
| Agents | 13 |
| Hooks | 11 |
| Edge Types | 12 |
| Brain Nodes | 32K+ |
| 最新版本 | v1.10.10（持续活跃） |

## 5. 与主人方向关联

MindrianOS 的 **Opportunity Bank + 知识图谱查询** 方法论与 Project Deal（Anthropic Agent 二手交易实验）有高度方法论呼应：

- **可借鉴点**：如何用图数据库建立"洞察之间的关联网络"，而非暴力向量检索
- **Token 成本优化**：精准图查询 vs 全量扫描的思路，可迁移至投流 Agent 的决策日志设计
- **Human-in-the-loop 设计**：Larry 在关键决策点主动挑战用户，与投流 Agent 需要在出价异常时引入人工判断的理念一致
