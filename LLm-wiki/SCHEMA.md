---
title: LLM Wiki Schema
type: schema
domain: AI/创业 / AI & Venture Intelligence
created: 2026-05-14
updated: 2026-05-14
---

# Wiki Schema — AI & Venture Intelligence

## Domain
本 wiki 服务于 AI/创业情报系统，涵盖：
- AI 领域 KOL（投资人、创始人、研究者、工程师）
- AI 公司与产品（赛道、融资金额、技术路线）
- 投资机构（VC/CVC/ETF）
- 行业事件（黑客松、会议、峰会）
- 核心概念与技术范式（Agent、Memory、RAG、编程范式）
- 深度洞察（投资逻辑、产品分析、趋势判断）

## Conventions

### 文件命名
- 全部小写，中划线分隔：`agentic-memory-architecture.md`
- 不得有空格或下划线（用于连接词时也用中划线）

### Wikilinks
- 同一目录下：`[[target-page]]` 或 `[[target-page|显示文字]]`
- 不同目录：`[[subdir/target-page]]`
- 最低要求：每个页面至少 2 个 outbound wikilinks

### Frontmatter（必须字段）
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [tag1, tag2]
sources: [raw/articles/source-name.md]
# Optional:
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
---
```

### Provenance（来源标注）
当页面综合 3+ 来源时，在相关段落末尾加 `^[raw/articles/source-file.md]`

### Tag Taxonomy
```
# 人/组织
kols / vc / company / event / person

# 技术/概念
agent / memory / rag / inference / fine-tuning / coding
infrastructure / security / benchmark

# 商业/市场
ecommerce / amazon / monetization / startup / funding

# 方法论
framework / methodology / principle / trend

# 元
comparison / query / summary / meta
```

## Page Thresholds
- **新建页面**：该实体/概念在 2+ 来源中出现，或在单一重要来源中处于核心位置
- **更新现有**：旧页面 facts 与新来源矛盾 → 保留双方，标 `contested: true`
- **合并/split**：超过 200 行 → 拆分为子主题页
- **归档**：内容完全被取代 → 移入 `_archive/`，从 index.md 移除

## Update Policy
当新信息与旧内容冲突：
1. 保留旧内容（不覆盖）
2. 在 frontmatter 标记 `contested: true` + `contradictions: [other-slug]`
3. 将新内容追加到正文，明确标注来源和日期
4. 报告给用户（lint 环节）

## Layer 1 — Raw Sources（Immutable）
- `raw/articles/` — Web 文章、公众号、新闻
- `raw/papers/` — 学术论文、PDF
- `raw/transcripts/` — 访谈记录、会议记录
- `raw/assets/` — 图片、图表（引用方式 `![](../raw/assets/image.png)`）

## Layer 2 — Wiki Pages
- `entities/kols/` — 意见领袖
- `entities/companies/` — 公司/产品
- `entities/vcs/` — 投资机构
- `entities/events/` — 行业事件
- `concepts/` — 概念/技术/范式
- `comparisons/` — 对比分析
- `queries/` — 值得归档的问答结果（与 insights 对应）

## Layer 3 — Schema
- `SCHEMA.md` — 本文件，规范定义
- `index.md` — 内容总索引，按 section 分类
- `log.md` — 操作日志（append-only，>500 条年度轮转）
