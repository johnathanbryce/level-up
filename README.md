# Level-Up

A structured, deliberate-practice system for rebuilding and deepening full-stack and AI engineering skills, from raw language fluency through system design, backend, AI in production, frontend performance, and devops.

This repo is the working environment, the curriculum, and the tracking system, all in one place. Every file in here exists for one reason: to push competence forward and prevent the slow drift that happens when you let an LLM do the thinking for you.

---

## Why this exists

I leaned on LLMs too heavily at work and watched my Python, algorithmic instincts, and system design fluency get rusty. This repo is the fix: structured study, code I write myself, and a mentor protocol that quizzes me instead of letting me coast.

Goal is to operate solidly at mid-to-senior across the stack with real AI-engineering depth. Vocabulary and judgment that survive a whiteboard, not just autocomplete.

---

## How the system works

This isn't a notes folder. It's a curriculum with a mentor protocol enforced through [CLAUDE.md](CLAUDE.md) and a per-section tracker in each numbered directory.

Every working session follows the same shape:

1. **Algorithm warmup (15-30 min).** A coding problem in Python (~60% of sessions) or JavaScript (~40%). Language fluency is the floor everything else stands on. Problems are framed in real-world language, never named after their underlying pattern, so pattern recognition has to be earned. New patterns get a short formal lesson before the first problem; established patterns are drilled and then re-tested cold ~every third session.
2. **Applied recall question (2-3 min).** A scenario-flavored question pulled from any prior topic. Forces retrieval under pressure, not just recognition. This is the bridge from warmup-mode into study-mode.
3. **Roadmap topic (45-120 min).** One concrete sub-topic from the current section. Every topic ends with a "now apply it" beat: a written explain-back, a diagram, an applied scenario, or a small code exercise. Pure explanation followed by "got it, next" is explicitly the anti-pattern to avoid.
4. **End-of-section warm-down quiz.** Before any section is allowed to close, a structured 5-7 question quiz mixes recall, "explain why," trade-off reasoning, and one applied scenario. The quiz result is logged. Failures trigger targeted re-teach, not "we'll come back to it."
5. **End-of-section capstone.** A formal assessment or architecture defense gates section completion. No capstone, no close.

Everything gets logged. Every weak spot gets a name, a date, and an occurrence count. Patterns aren't called "locked" until they've been recalled cold, on a fresh surface, with no scaffolding.

---

## The roadmap

Numbered top-level directories map to the curriculum. Each section has its own `CLAUDE.md` with sub-topic checklist, session log, weak-spot tracking, and capstone definition.

| # | Section | Status | Focus |
|---|---|---|---|
| 01 | [Algorithms](01-algorithms/) | Ongoing | Python + JS fluency, core patterns, pattern recognition under interview conditions |
| 02 | [System Design](02-system-design/) | Pre-capstone | Request lifecycle, networking, scaling, caching, queues, DB architecture, resilience, observability + 5 case studies |
| 03 | [AI Foundations](03-ai-foundations/) | Queued | Embeddings, vector search, chunking, basic RAG POC |
| 03.5 | [OOP Fundamentals](03.5-oop-fundamentals/) | Queued | Four pillars, composition vs inheritance, Python dunders, dataclasses |
| 04 | [Backend](04-backend/) | Queued | FastAPI + Express, Postgres schema/indexing/EXPLAIN, Redis cache-aside |
| 05 | [AI Production](05-ai-production/) | Queued | Production RAG, hybrid search (BM25 + embeddings), pgvector, eval, cost control |
| 06 | [Frontend Performance](06-frontend/) | Queued | React rendering model, memoization economics, code splitting, virtualization |
| 07 | [DevOps Essentials](07-devops/) | Queued | Docker mental model, Compose, CI/CD pipelines, deployment strategies |
| 08 | [Kubernetes & Terraform](08-kubernetes-terraform/) | Deferred | Conversational competence, not expert depth |
| 09 | [Engineering Judgment](09-engineering-judgment/) | Deferred | Architecture teardowns, build-vs-buy, post-mortems, OSS reading |
| 10 | [Interview Prep](10-interview-prep/) | Cross-cutting | Per-technology question banks pulled into Block 3 of sessions |

Each section closes only after its capstone passes. No sliding through.

---

## Repo structure

```
level-up/
├── CLAUDE.md                  # Master mentor protocol + current state of progress
├── JOHN-GUIDE.md              # Operating manual for using the system day-to-day
├── 01-algorithms/
│   ├── CLAUDE.md              # Pattern tracking, problem log, language phase tracking
│   ├── python/
│   │   ├── fundamentals/      # Pre-pattern fluency drills (list comp, stdlib, etc.)
│   │   └── patterns/          # Hash-map-complement, sliding window, frequency, stack...
│   └── typescript/
│       ├── fundamentals/
│       └── patterns/
├── 02-system-design/
│   ├── CLAUDE.md
│   ├── notes/                 # 12 topic files: request lifecycle → observability
│   ├── assignments/           # Applied design exercises per topic
│   └── interview-questions.md # Question bank with canonical answers
├── 03-...                     # Same shape as above for each section
└── .vscode/tasks.json         # Pre-wired file watchers for Python/TS algo work
```

Two organizing principles:

- **Each directory is self-contained.** Every section has its own CLAUDE.md tracker. Each backend/AI project gets its own venv or package.json. No global dependencies beyond the algo runners.
- **Tracking is a first-class artifact.** The CLAUDE.md files aren't a side effect of working. They *are* the work product. Anyone can open a section's CLAUDE.md and see exactly what's been covered, what's been quizzed, what wobbled, and where to pick up.

---

## What "progress" actually looks like here

The cheap version of self-study is reading docs and feeling smart. This system is built to defeat that. A few of the mechanisms:

- **Pattern recognition is tracked separately from pattern mechanics.** Knowing *what tool to reach for* is one skill; reflexively writing the right loop structure is another. Both are tested independently, on fresh surfaces, before a pattern is called "locked."
- **Every recurring weak spot gets named, counted, and drilled.** Examples currently being worked: "knows-the-rule, hasn't-internalized-implications" (now on its 7th tracked occurrence, drilling continues until it stops surfacing); rate-limit numerical calibration; cache stampede single-hot-key fix; consistent-hashing vs session-stickiness conflation.
- **Honest "I don't know" is reinforced.** Confident-wrong answers are treated as the failure mode; honest gaps are treated as data and turned into the next drill. Senior-flavor interview behavior is named explicitly when it appears so the muscle locks.
- **Notes get audited.** Markdown structure is enforced (`#` for title, `##` for sections, `###` for sub-sections, `**bold**` reserved for vocabulary, never as a section marker). Trimming "in the weeds" content from notes gets challenged when the trimmed content is actually load-bearing. There's a documented case where I trimmed a state machine I called "too in the weeds," failed the very next quiz on it, then re-locked it 22 days later. That kind of feedback loop only works when the tracking is honest.
- **Burnout is a signal, not a failure.** When a session hits the wall, the wrap-up happens cleanly. No marginal extra rep, no ego-driven push.

The point of all of this isn't perfectionism. It's forward progress with a definition of "done" that has teeth.

---

## Tooling

Lightweight by design. Nothing here exists for its own sake.

- **VSCode + Claude Code** as the working environment. Mentor protocol lives in CLAUDE.md and is read at the start of every session.
- **Algo watchers.** `nodemon --exec python` for Python, `tsx watch` for TypeScript. Pre-configured in `.vscode/tasks.json`. Open a file, run the task, save = re-run.
- **Per-project environments.** Each backend/AI project has its own venv or package.json. No global deps.
- **Git as backup.** Weekly commits to main. No branching strategy needed since the repo is single-author and the work is the artifact.

---

## A note on the AI-assisted nature of this work

The mentor in this system is an LLM. The point isn't to avoid AI. It's to use it the way a strong junior uses a senior engineer: to be challenged, corrected, quizzed, and held to a real standard. Every line of code in the algorithm directories is hand-written by me. Every notes file is written by me. The LLM's role is to teach, push back, generate problems, run quizzes, refuse to let me skate past things I don't actually understand, and keep the tracking honest.

Using AI to accelerate *learning* rather than to replace *thinking* is the whole reason this repo exists.
