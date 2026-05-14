---
title: Sequoia
created: 2026-05-14
updated: 2026-05-14
type: query
tags:
---

# Sequoia

# 💡 Sequoia AI Ascent 2026 · Boris Cherny 访谈：8 条核心判断

## 核心结论

Boris Cherny 在 Sequoia AI Ascent 2026 舞台上给出了他迄今为止最激进的判断：**编码问题已被解决（2025年10-11月临界点）、/loop 代表未来、软件民主化将使创业公司数量十年增加10倍。** 这是一次从"工具使用"到"工作模式重构"认知跃迁。

## 详细分析

### 1. "2026 年，我还没有亲手写过一行代码"
Boris 明确表示 2026 年本人未亲手写一行代码，每天在手机上提交几十个 PR。这不是极端个例，而是 Anthropic 内部文化的公开宣言。

### 2. 编码临界点：早在 2025年10月或11月已达
Boris 认为模型早已具备编写 100% 代码的能力，编码问题实际上已被解决。这与 [[Andrej_Karpathy_大牛_AI大牛]] 的判断互为印证。

### 3. "/loop 代表未来"
这是访谈中最具前瞻性的判断。/loop 是 Claude Code 内置的周期性任务调度命令，可按分钟/小时/天自动重跑。结合 routines（云端版，关电脑也能跑），AI 编程正式进入"设置一次、自动运行"的时代。

Boris 实际用例：
- CI 错误自动修复 + rebase
- CI 健康监控 + flaky test 自动修复
- Tweet 抓取 + 30 分钟聚类分析

### 4. Opus 4.7 主动推送 loop 任务
AI 开始主动提议自动化：被要求查询数据时，Opus 4.7 主动提出"我为你开启一个循环任务，每 30 分钟给你一份报告"。这标志着 AI 从被动响应转向主动编排。

### 5. 软件民主化：印刷术类比
- 古登堡之前：只有 10% 欧洲人识字（受雇于皇室）
- 印刷机出现后 50 年：文学产量超过此前 1000 年总和
- 软件开发将走同一条路，且**比 50 年更快**

关键洞察：领域知识（Domain Knowledge）才是最难的部分。未来最合适的会计软件开发者不是工程师，而是精通业务的会计师。

### 6. 护城河重构
**重要性下降**：切换成本（AI 可迁移数据/功能）、流程能力（模型擅长优化工作流）

**重要性上升**：网络效应、品牌、独特数据资产

### 7. 未来十年创业公司数量增加 10 倍
新公司没有历史包袱和遗留基础设施，相比被迫重建的大企业拥有结构性优势。

### 8. 安全机制必要性下降
随着模型对齐能力提升，以下机制的必要性正在弱化：
- Prompt injection 防护
- 静态命令验证
- Permission mode
- Human-in-the-loop 干预

## 数据与证据

| 证据 | 来源 |
|---|---|
| "2026 年未写一行代码，每天在手机上提交几十个 PR" | Sequoia AI Ascent 2026 访谈 |
| "早在 2025年10月或11月，模型已达编写100%代码临界点" | Sequoia AI Ascent 2026 访谈 |
| "我觉得 /loop 代表了未来" | Sequoia AI Ascent 2026 访谈 |
| "未来十年创业公司数量将增加 10 倍" | Sequoia AI Ascent 2026 访谈 |
| "编程将像发短信一样简单" | Sequoia AI Ascent 2026 访谈 |
| Opus 4.7 主动提议 loop 任务 | Sequoia AI Ascent 2026 访谈 |
| Mike Krieger 担任 Anthropic CPO | Sequoia AI Ascent 2026 访谈 |
| Claude Code 日均 150 PR | howborisusesclaudecode.com |

## 行动建议

1. **重新定义"会编程"**：从写代码 → 调度 AI、审查输出、定义验收标准
2. **建立 loop 思维**：将重复性工作优先设为自动化 loop
3. **投资领域知识**：在 [[判断力_Judgment]] 和垂直领域专业知识上建立不可替代性
4. **关注 Claude Code /loop 与 routines 功能演进**：这将成为 AI 编程 Agent 的核心差异化能力

## 信息来源
- [Sequoia AI Ascent 2026 访谈原文](https://www.youtube.com/watch?v=SlGRN8jh2RI)
- [howborisusesclaudecode.com](https://howborisusesclaudecode.com/)
- Business Insider 2026-05-08
- StartupHub.ai 2026-05-07
