# Conventions

> The single source of truth for data format. Every topic note, the index, and all ledgers follow this. Keeping these rules costs ~nothing today and makes a future RAG migration a one-script job. When in doubt, this file wins.

---

## 1. Topic Frontmatter Schema

Every file in `topics/` starts with this YAML block:

```yaml
---
id: topic-20260609-01
date: 2026-06-09
title: trust layer for professional retail traders
tags: [research, trading-tools]
stance: neutral
status: spun-off
relations: [narrowed-from:topic-20260605-01]
---
```

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string | yes | Permanent anchor. Format below. Never changes, even if the file is renamed. |
| `date` | `YYYY-MM-DD` | yes | The day the topic was discussed. |
| `title` | string | yes | Short, human-readable. May be Chinese. |
| `tags` | list | yes (≥1) | Chosen **only** from the controlled vocab in §3. |
| `stance` | enum | yes | `bullish` / `neutral` / `bearish`. |
| `status` | enum | yes | `draft` / `discussing` / `spun-off` / `archived`. |
| `relations` | list | optional | Each item is `relation-type:id` (see §4). |

---

## 2. ID Rule

```
topic-YYYYMMDD-NN
```

- `YYYYMMDD` = discussion date; `NN` = zero-padded sequence within that day (`01`, `02`, …).
- Globally unique and **permanent**. Filenames, titles, and tags may change; the id must not.
- Everything keys off the id: relations, the index, future vectors, and spinoff pointers.

**Filename** (separate from id): `YYYYMMDD_slug.md`, where `slug` is a short ascii/pinyin handle. The id inside frontmatter is authoritative; the filename is just for humans browsing `topics/`.

---

## 3. Controlled Vocabulary

Pick `tags` only from this list. Extend the list deliberately (add a row here first), never invent a tag inline — that's how "risk-control / risk control / RegTech" becomes three labels for one thing.

### tags (English slug — Chinese gloss)

| slug | gloss |
|---|---|
| `risk-control` | 风控 |
| `compliance` | 合规 / RegTech |
| `xai` | 可解释 AI |
| `research` | 投研 |
| `trading-tools` | 交易工具 |
| `ai-infra` | AI 基建 |
| `payments` | 支付 |
| `wealth` | 财富管理 |
| `lending` | 信贷 |
| `data-alt` | 另类数据 |

> Add new slugs here as directions appear. Keep them lowercase, hyphenated, English.

### stance

`bullish` (看好) · `neutral` (中立) · `bearish` (否定)

### status

`draft` (草稿) · `discussing` (讨论中) · `spun-off` (已立项) · `archived` (已归档)

---

## 4. Relation Types

`relations` entries use `type:id`. Allowed types:

| type | meaning |
|---|---|
| `narrowed-from` | this topic is a narrower cut of an earlier one |
| `derived-from` | spun out of / inspired by an earlier topic |
| `contradicts` | stance conflicts with the referenced topic (flag for the contradiction check) |
| `spun-off-as` | graduated into a standalone project (value may be a project name, not a topic id) |

---

## 5. In-Note Section Headers (fixed)

Every topic note uses these four headers, in order. They become stable chunk boundaries for future embedding.

```
## Opportunity   — the pitch: opportunity + why now + angle + risks
## Discussion    — how the conversation evolved
## Feedback      — the user's reaction, verbatim where it matters
## Signals       — taste signals extracted, to feed preferences.md
```

---

## 6. index.md Line Format

`index.md` is a projection of frontmatter — one row per topic, newest at the bottom. Dedup and contradiction checks read this instead of scanning all notes.

```
| id | date | title | tags | stance | status |
|---|---|---|---|---|---|
| topic-20260605-01 | 2026-06-05 | 可解释 AI 风控 | risk-control, compliance, xai | bearish | archived |
| topic-20260609-01 | 2026-06-09 | 职业个人交易者信号可信层 | research, trading-tools | neutral | spun-off |
```

Keep it in sync: every new topic appends exactly one row; a stance/status change edits that row in place.
