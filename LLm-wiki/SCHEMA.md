# Wiki Schema

## Domain

个人全量知识库——工作、生活、投资、创业、技术、健康、人际等所有领域的持续积累。知识的复利引擎。

## Conventions

- 文件名：小写、中划线、无空格（如 `a股-大盘-2026.md`）
- 页面以 YAML frontmatter 开头（见下方）
- 使用 `[[wikilinks]]` 互链，新建页面至少 2 条外链
- 更新页面时必须更新 `updated` 日期
- 每个新页面必须加到 `index.md` 对应章节
- 所有操作追加到 `log.md`
- **来源标注**：综合 3+ 来源的页面，在相关段落末尾加 `^[raw/articles/source-file.md]`
- **置信度**：单源/主观内容标记 `confidence: medium` 或 `low`

## Frontmatter

```yaml
---
title: 页面标题
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | query | summary | log
tags: [从标签体系选取]
sources: [raw/articles/source-name.md]
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
---
```

## Tag Taxonomy（标签体系）

- **投资**：a股、crypto、房产、基金、美股、债券
- **创业**：产品、投流、融资、战略、竞品
- **技术**：ai、llm、编程、工具、数据
- **新增**：大模型、微调、教育、训练
- **健康**：身体、饮食、运动、心理、睡眠
- **生活**：社交、旅行、阅读、影视、爱好
- **人物**：kol、 founder、投资人、朋友
- **组织**：公司、基金、实验室、平台
- **概念**：方法论、思维模型、商业模型
- **记录**：日记、周记、月度、年度

## Page Thresholds

- **建页**：实体/概念被 2+ 来源提及，或在单一核心来源中占重要位置
- **归入已有**：提及但非核心
- **不建页**：一次性提及、旁枝脚注
- **拆分**：超过 200 行则拆分，通过互链串联

## Update Policy

新旧信息冲突时：
1. 看日期——新来源通常覆盖旧来源
2. 矛盾无法调和时——两端并存，注明来源与日期
3. frontmatter 标记 `contradictions: [page-slug]`
4. lint 时报告，等待主人裁决

## Raw Frontmatter

```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: <body hash>
---
```
