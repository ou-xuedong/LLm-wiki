---
title: Human-like
created: 2026-05-09
updated: 2026-05-09
type: concept
tags:
  - #概念
  - #AgentInfra
  - #Memory
  - #长期记忆
  - #OpenClaw生态
---

# Human-like


## 关联

**上位概念**：[[agentic_memory_architecture_智能体记忆架构]]
**相关概念**：[[openclaw_自进化ai开源框架]], [[hermes_agent]], [[gbrain_ai记忆系统]], [[context_window_and_memory_architecture_上下文窗口与记忆架构]], [[agent记忆系统设计三大支柱收束论]]
**关键人物**：[[openclaw_自进化ai开源框架]]

# 🧠 Human-like Memory（类人记忆插件）

> **官网**：https://human-like.me
> **一句话定位**：基于认知科学第一性原理、为 AI Agent 提供更准确、更省 token、更可控的长期记忆能力的服务化插件
> **品牌主张**：From "stored" to "used right" — True Long-term Memory

## 1. 定义与核心原理

**Human-like Memory** 是由 [[openclaw_自进化ai开源框架]] 团队孵化、现已演进为**框架中立**的 Agent 长期记忆服务。其前身是 OpenClaw 内置的 "HumanLike OpenClaw plugin"（在产品自述中明确称为 "the historical HumanLike OpenClaw plugin"），现已抽离为独立服务，同时支持 OpenClaw 插件、[[hermes_agent]] native memory provider、通用 REST API 三种集成形态。

**核心原理（认知科学第一性原理）**：人脑并非用单一机制存储所有记忆——回忆"我是谁"、"昨天发生了什么"、"如何骑自行车"调用的是三套不同的脑系统。把这一切扁平化到向量库做语义相似检索，会同时损害**精确性**与**成本效率**。Human-like Memory 把记忆按类型分而治之，每类配套不同的检索范式，从根上解决"数据越多召回越糊"的传统问题。

---

## 2. 关键技术路线与变体

### 2.1 核心架构：Three Memory Types, Divide and Conquer（三类记忆，分而治之）

> 三句话区分："**Who are you**", "**What happened**", "**How to do it**" 是本质不同的问题。

| 记忆类型 | 对应问题 | 存储内容 | 检索范式 |
|---|---|---|---|
| **Semantic Memory（语义记忆）** | "知道你是谁" | profiles / preferences / rules / 稳定 persona facts，由零散历史巩固成持久认知 | 概念性召回 |
| **Episodic Memory（情景记忆）** | "记住发生了什么" | conversation events / scenes / 时间相关上下文 | 基于当前对话优先级，召回相关事件、关系变化、情感语境 |
| **Procedural Memory（程序性记忆）** | "怎么做事" | skills / tools / workflows / SOPs / 可执行知识 | **强调精确匹配（exact match），而非相似度分数**——这是与传统纯向量方案的最大分野 |

### 2.2 五大技术亮点

1. **不同类型用不同检索范式** — 降低假召回（false recall），打破"全量灌进向量库"的单一范式
2. **分层加载（Layered Loading）替代全文注入** — 直接砍掉无效 context 开销，token 越用越省
3. **三层隔离体系** — `user_id / agent_id / scenario` 三级命名空间，支持多用户、多 Agent、多工作流并存
4. **框架无关（framework-agnostic）** — 三种集成形态共享同一套 API，避免锁定单一 Agent 运行时
5. **企业级原生** — 数据隔离 / 访问控制 / 审计日志 / VPC 部署 / SSO / BYOK 加密 / 自定义模型路由 / SLA

### 2.3 三种集成形态

| 形态 | 适用场景 | 关键路径 |
|---|---|---|
| **OpenClaw Plugin / Skill** | 已在跑 [[openclaw_自进化ai开源框架]] 的团队 | 装插件 → 配 API Key → 切换默认 memory slot 为 `human-like-mem` |
| **Hermes Agent native provider** | [[hermes_agent]] 用户 | 装 provider → 链接到 `~/.hermes/hermes-agent/plugins/memory/humanlike` → 切换 `memory.provider: humanlike` |
| **通用 REST API** | 任意应用 / 自研 Agent / 第三方平台 | API Key + 两个核心端点：`Search Memory`（自然语言查询召回）+ `Add Memory`（对话消息批量存储） |

### 2.4 关键 API 端点（通用 REST）

- `Search Memory` — 自然语言查询召回相关记忆，按相关度打分排序，**用于 AI 响应前注入上下文**
- `Add Memory` — 对话消息批量提交，系统自动抽取并结构化存储，**支持异步处理**避免阻塞
- 工作流：plugin 缓存对话 → 按 turn threshold 或 timeout 自动 flush → Agent 可主动调用 `memory_search` / `memory_store`

---

## 3. 行业应用场景

| 场景 | 价值点 |
|---|---|
| **AI Companion / Social Agents** | 长期伴侣型 Agent 需记住偏好、关系、情感语境 |
| **Long-horizon Task Agents** | 长任务跨会话追踪目标与进度 |
| **Personalized Assistants** | 个人助理持续累积用户画像与行为模式 |
| **Skill-driven Agents** | 需精确匹配 SOP、工作流、配置的 Agent（程序性记忆精确匹配优势最大） |

---

## 4. 性能与对标

### 4.1 LoCoMo Benchmark 战绩

> **同等评测条件下（GPT-4.1 mini 统一打分），Human-like Memory 比 [[openclaw_自进化ai开源框架]] Native Memory：准确率/完成率更高 + Total Token 消耗显著更低，整体性能提升 +35%**

匿名化对比主流系统（A–I 标签横跨多个 long-memory benchmark），Overall 分数稳居前列。

### 4.2 痛点对标（传统长期记忆方案三大病）

| 病灶 | Human-like Memory 解法 |
|---|---|
| **More data, less precision**（扁平化导致召回噪声随数据增长） | 按记忆类型分桶，独立检索通道 |
| **Exact match becomes fuzzy match**（SOP / 配置需精确，相似度"差不多"不行） | 程序性记忆走精确匹配通道 |
| **Context gets expensive without getting better**（注入长摘要 token 涨而效果未必涨） | 分层加载，按需展开 |

---

## 5. 代表性项目与生态位

- **本体**：[Human-like Memory 官网](https://human-like.me) / Humanlike Server
- **孵化方**：[[openclaw_自进化ai开源框架]]
- **同生态产品**：[[hermes_agent]]（Nous Research 出品 · native provider 集成）
- **横向竞品/参照**：
  - [[gbrain_ai记忆系统]]（YC 总裁 Garry Tan 开源 · "梦境循环" + 三层混合搜索 · 偏个人本地）
  - **MemGPT**（OS 虚拟内存范式 · 已在 [[agentic_memory_architecture_智能体记忆架构]] 中收录）
  - **Mem0 / Letta** 等记忆即服务方案

---

## 6. 争议与开放问题

- **三类记忆的边界判定** — Episodic 与 Semantic 之间的"巩固时机"如何确定？模型自决 vs 规则驱动 vs 用户标注？
- **精确匹配的可扩展性** — 程序性记忆走 exact match 在 SOP 数量爆炸时如何保证检索性能？
- **跨 Agent 共享 vs 隐私** — `agent_id / scenario` 让多 Agent 共享同一记忆池成为可能，但权限边界如何审计？
- **与 [[openclaw_自进化ai开源框架]] 的边界关系** — 现产品定位"框架中立"，但 LoCoMo 直接对比 OpenClaw Native，长期是独立竞品还是 OpenClaw 生态护城河延伸？
- **依赖 LLM 抽取的成本** — Add Memory 需要 LLM 提取结构化记忆，自身 token 成本如何与"省 token"主张平衡？

---

## 7. 关键参考链接

- 官网：https://human-like.me
- OpenClaw 插件文档入口（站内）：dashboard 登录后查看
- Hermes Agent 集成：通过 `~/.hermes/.env` 配置 `HUMAN_LIKE_MEM_AGENT_ID` / `HUMAN_LIKE_MEM_SCENARIO` / `HUMAN_LIKE_MEM_BASE_URL`
- 用户社群：飞书 Human-like Memory 用户群（官网首页 QR 码）
