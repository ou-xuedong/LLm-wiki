---
title: Clawspan
created: 2026-04-28
updated: 2026-04-28
type: companies
tags:
  - #开源项目
  - #语音AI
  - #个人AI助理
  - #全栈自研
---

# Clawspan


## 关联

**竞品**：Siri, Alexa, Google Assistant

# Clawspan（macOS 个人 AI Chief of Staff）

## 1. 核心定位与业务模式

Clawspan 是一个 **语音优先、永远在线的 AI 私人助理**，核心理念：像联合创始人一样思考你的事。

**平台限制**：macOS 专属（依赖 AppleScript、afplay、osascript、screencapture、PyAutoGUI 等 macOS 特性）。

**核心差异化**：不是套壳 AI 平台，从底层全自研——意图路由、多 Agent 编排、记忆系统、工具分发、语音 UX 全部手写。Pipecat 仅用于语音 I/O（麦克风→STTS→TTS→扬声器）。

## 2. 核心架构

### BrainRouter — 三层路由

| Tier | 触发条件 | 延迟 | 原理 |
|------|---------|------|------|
| Tier 1 | 高置信度关键词命中 | ~0ms | 7 类路由的关键词打分，无需 LLM |
| Tier 2 | Tier 1 模糊时 | ~300ms | DeepSeek LLM 5 token 分类 |
| Tier 3 | 含连接词（and/then/also） | ~500ms | 多意图切分串行执行 |

**效果**：80% 请求在 Tier 1 解决，零 LLM 成本。

### Memory Palace — 四层记忆架构

```
L0: Identity — identity.txt，始终加载，~100 tokens
L1: Importance — 重要性 top-10，~500 tokens，每会话必加载
L2: Semantic — ChromaDB 向量相似度，~200 tokens，按需触发
L3: Knowledge Graph — SQLite 实体+三元组，结构化关系
```

**FactExtractor**：每轮对话结束后，gpt-4o-mini 异步提取用户事实（key-value-wing-importance），语义去重（相似度 > 0.92 则跳过）。比通用记忆系统更懂"你是谁"。

### Agent 编排
- **Domain Agent**：通用任务处理
- **Research Agent**：深度研究（含 Hunter.io 邮件情报）
- **GitHub Agent**：分 Monitor（只读）和 Action（写操作）

## 3. 技术选型对比（vs 框架方案）

| | LangChain/AutoGen/CrewAI | Clawspan |
|---|---|---|
| 延迟 | 100-300ms/hop | 直接 async Python，零中间件 |
| 工具形态 | 框架标准化，丧失控制 | 原始 OpenAI function schemas |
| 记忆 | 脆弱向量集成，难调 | 手写 MemPalace |
| 语音 UX | 无概念 | `_HEAVY_TOOLS` 集合 + LLM 摘要门控 |
| 路由 | 每条消息 LLM | 关键词 ~0ms |

## 4. 安全设计

**Passphrase Gate**：
- SHA-256 + 16-byte 随机盐，存于 ~/.clawspan_auth.json
- 明文密码永不存储或日志
- STT 模糊处理（数字拼写、空格、标点归一化）
- 3 次失败后 60 秒锁定

## 5. 与主人方向关联

Clawspan 的 **Memory Palace 架构**和 **四层记忆设计**是主人做投流 Agent 的重要参考：

- **记忆分层思路**：可迁移到投流 Agent 的"记忆分层"设计（近期投流记录 / 爆款模式库 / 品牌知识库）
- **FactExtractor**：自动从对话中提取结构化事实，值得借鉴到投流场景的"广告主偏好学习"
- **Tiered Routing**：极低成本拦截高频简单意图，只在必要时调用昂贵 LLM，是投流 Agent 优化成本的核心参考

## 6. 项目状态

- 319 Commits，活跃开发
- 1 GitHub Star（刚起步）
- 平台：macOS（Linux/Windows 不可用）
