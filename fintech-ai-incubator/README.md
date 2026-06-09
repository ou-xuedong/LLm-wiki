# fintech-ai-incubator

> A pure-markdown, single-user system for incubating **fintech × AI opportunities**: every day we discuss one opportunity (a financial use case enhanced by AI, or an AI-infra opportunity that a financial scenario can incubate), capture feedback, self-evolve preferences, and graduate mature directions into standalone projects.
>
> This file is the project **blueprint**. The project is currently in the planning stage and will be filled in step by step (see the Roadmap at the end).
>
> Note on language: file structure, schema, and field names are **English** for portability. Topic discussions themselves are recorded in whatever language we actually talk in (currently Chinese) — that's data, not structure.

---

## 1. Design Principles (north star, keeps us from drifting)

1. **Simple first** — if a single markdown file does the job, never build a system.
2. **Single responsibility** — one file, one clear job.
3. **Files first, migration-friendly** — pure files for now, but formatted so the data can later be loaded/vectorized with a single script.
4. **Constant token cost** — each run reads only `preferences + index + last 7 days`, never a full scan (hard line).
5. **Human-readable, hand-editable** — always keep the markdown source.

---

## 2. Directory Structure (planned)

```
fintech-ai-incubator/
├── README.md           this file: the blueprint
├── CLAUDE.md           agent operating manual (how the daily loop runs)
├── conventions.md      ★ extensibility core: frontmatter schema + controlled vocab + ID rules
├── preferences.md      the user's taste (self-evolving from feedback)
├── contradictions.md   reconciled stance-flips (after asking the user)
├── index.md            one line per topic; dedup & contradiction lookup rely on this
├── coverage.md         ledger of covered directions, for coverage rotation
├── weekly.md           layered compression (each week, one line per topic)
├── spinoffs.md         pointers to graduated independent projects
└── topics/             full topic notes (the only subdir; grows without bound)
    ├── _template.md    new-note template with frontmatter
    └── YYYYMMDD_slug.md
```

**Trade-off note**: only `topics/` (which grows without bound) gets its own subdirectory; everything else stays flat even with distinct jobs — at the current scale, a directory holding one or two files is over-engineering. We split a directory out only when that file class actually grows.

---

## 3. Data Conventions (★ the real vehicle for extensibility, kept in `conventions.md`)

### 3.1 Uniform frontmatter on every topic

```yaml
---
id: topic-20260609-01      # the permanent anchor — never changes
date: 2026-06-09
title: trust layer for professional retail traders
tags: [research, trading-tools]   # chosen from the controlled vocab, not free-typed
stance: neutral            # bullish / neutral / bearish
status: spun-off           # draft / discussing / spun-off / archived
relations: [narrowed-from:topic-20260605-01]
---
```

### 3.2 ID rule

`topic-YYYYMMDD-NN` — stable and unique. Filenames may change; the id never does. Relations, vectors, and pointers all key off it.

### 3.3 Controlled vocabulary

`tags`, `stance`, and `status` all draw from **fixed enums**, so "risk-control / risk control / RegTech" can't end up as three labels for one thing. `conventions.md` holds the canonical list (with a Chinese gloss per tag for readability).

### 3.4 Fixed in-note section headers

`Opportunity / Discussion / Feedback / Signals` — these become stable chunk boundaries later, directly improving embedding quality.

> Follow these four while writing files and the cost is near zero today; when we migrate to RAG, one script parses everything into a store. **Extensibility lives in data hygiene, not in a system.**

---

## 4. Core Workflow (the daily loop, mapped onto the new structure)

1. **Read context**: `preferences + index + coverage + topics/ from the last 7 days` (only these — constant token cost).
2. **Generate a candidate**: one fintech × AI opportunity, based on preferences.
3. **Dedup**: read `index` to check similarity; regenerate if too close; avoid directions over-used in the last 7 days.
4. **Discuss**: pitch the opportunity card (opportunity + why now + angle + risks), go deep.
5. **Record**: fill the template into `topics/`; append one line to `index`.
6. **Self-evolve**: write any taste signal into `preferences.md`.
7. **Check contradictions**: if a same-tag stance flips in `index`, don't auto-overwrite — ask the user, then log the conclusion in `contradictions.md`.
8. **Incubate**: when a direction matures, graduate it into a standalone project and record a pointer in `spinoffs.md`.

---

## 5. Extensibility Path (future RAG — not built now)

When data grows large, the bottleneck isn't storage, it's: *the context window is finite — how do we retrieve only the most relevant items to feed the LLM?* The layered upgrade, when the time comes:

- **Thousands of records**: add SQLite for frontmatter metadata; bodies stay markdown.
- **Tens of thousands**: introduce vector retrieval for semantic dedup/recall — this is **RAG**.
- **Larger / multi-user**: move to Postgres + a dedicated vector store.

Because the data is clean from day one, **migration is running a parser script, not a rewrite.**

Upgrade triggers (consider only when one is met): ① data grows to thousands/tens of thousands; ② programmatic complex aggregate queries needed; ③ it becomes multi-user / multi-device. **Until then, markdown is optimal.**

---

## 6. Boundaries (keep it simple — explicitly NOT doing now)

- 🔴 No database, no scripts, no tooling.
- 🔴 No empty directories built only "for the future".
- 🔴 No features beyond the daily loop.

---

## 7. Build Roadmap (step by step)

- [x] R0 — Blueprint: this README
- [ ] R1 — Write `conventions.md` (frontmatter schema + controlled vocab + ID rules)
- [ ] R2 — Write `CLAUDE.md` (agent operating manual)
- [ ] R3 — Scaffold `topics/_template.md` and the remaining resident files
- [ ] R4 — Migrate existing data from the old incubator (`金融XAI方向探索/`, the 06-05 and 06-09 topics) into the new conventions
- [ ] R5 — Run the first full daily loop end-to-end to validate the flow

---

## Appendix: Relationship to the Old Project

This is an architectural redo of the `金融XAI方向探索/` incubator — more professional, single-responsibility, migration-friendly. The old directory's historical data migrates in at R4. Already-graduated sub-projects (e.g. `AI信号可信层/`) are unaffected and keep iterating in their own directories.
