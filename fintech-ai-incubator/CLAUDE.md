# fintech-ai-incubator — Agent Operating Manual

> Read this first, then `README.md` (blueprint) and `conventions.md` (data format). This is a pure-markdown, single-user system: each day, discuss one fintech × AI opportunity with the user, capture feedback, self-evolve, and graduate mature directions into standalone projects.
>
> Language: this manual and all structure are English. Discussions with the user are in Chinese (the user's persona settings live in the global `~/CLAUDE.md`). Topic notes record discussion in the language we actually talk in.

## Your Job

Pitch a topic → discuss with the user → record feedback → make the system understand the user's taste better over time. One topic per day, deep — not a pile of shallow ones.

## File Responsibilities

| File | Role | Who writes |
|---|---|---|
| `conventions.md` | Data format: frontmatter schema, controlled vocab, ID rules. The source of truth. | rarely, deliberately |
| `preferences.md` | The user's taste (self-evolving from feedback). Injected every run. | you, after each feedback |
| `contradictions.md` | Reconciled stance-flips, after asking the user. | you, when a flip is confirmed |
| `index.md` | One row per topic; dedup & contradiction lookup. | you, append one row per topic |
| `coverage.md` | Ledger of covered directions, for rotation. | you, per topic |
| `weekly.md` | Weekly compression (one line per topic). | you, weekly |
| `spinoffs.md` | Pointers to graduated standalone projects. | you, when a topic graduates |
| `topics/` | Full topic notes, one file each. | you |

## Daily Loop

1. **Read context**: all of `preferences.md` + all of `index.md` + `coverage.md` + `topics/` from the **last 7 days**. Only these — this is the key to constant token cost.
2. **Generate a candidate** fintech × AI opportunity based on preferences.
3. **Dedup** (read `index.md`): too similar to history → regenerate. Avoid directions over-used in the last 7 days (rotate coverage).
4. **Discuss**: pitch the opportunity card (opportunity + why now + angle + risks), go deep on one topic.
5. **Record**: create `topics/YYYYMMDD_slug.md` from `_template.md`, fill frontmatter per `conventions.md`; append one row to `index.md`; update `coverage.md`.
6. **Self-evolve**: write any taste signal into `preferences.md`.
7. **Check contradictions**: if a same-tag stance flips vs history, do **not** auto-overwrite — ask the user, then log the conclusion in `contradictions.md`.
8. **Incubate**: when a direction matures, graduate it into a standalone project (sibling directory) and record a pointer in `spinoffs.md`.

## The Four Mechanisms (keep them low-tech)

1. **Dedup** — read `index.md` and judge by eye; it's a few dozen rows. No embeddings/vector DB yet (see README's extensibility path for when that changes).
2. **Self-evolve** — after each feedback, append/revise one natural-language line in `preferences.md`. Next run injects it. Markdown-native preference learning, zero training.
3. **Contradiction** — on new feedback, scan `index.md` for same-tag history. Polarity flip (bullish last week, bearish now) → ask the user "changed your mind, or different scenario?" before recording. Distinguish real contradiction from normal evolution using the time window.
4. **Compression** — three layers: full `topics/` → `weekly.md` one line each → `preferences.md` at the top. Generate with only `preferences + index + last 7 days`; older content is covered by weekly + preferences. Run compression once a week.

## Triggers

- **Active (primary)**: the user opens a session and says "let's do today's" / "show me a draft" → run the daily loop.
- **Scheduled push (phase 2, later)**: a `/schedule` remote agent generates a draft daily. Not now — validate the active mode first.

## Red Lines

- 🔴 **Save tokens**: strictly read only `preferences + index + last 7 days`. Never scan full history.
- 🔴 **Loyal-minister honesty (诤臣)**: if an opportunity has a logic hole, a fake need, or real risk, say so directly — don't flatter, don't echo a wrong premise.
- 🔴 **One per day**: don't dump many topics; focus and go deep on one.
- 🔴 **Conventions are law**: every topic note must follow `conventions.md` (frontmatter, controlled vocab, fixed section headers). This is what keeps future migration a one-script job.
