# Level-Up

A structured practice system for rebuilding and deepening full-stack and AI engineering skills —
language fluency, system design, backend, AI in production, frontend performance, and devops. The
repo holds the curriculum, the working environment, and the tracking in one place.

## Why this exists

I relied on LLMs too heavily at work and let my Python, algorithmic instincts, and system design
fluency get rusty. This repo is the correction: structured study, code I write by hand, and a mentor
protocol (run through an LLM) that quizzes and corrects me instead of letting me coast. The goal is
to operate solidly at a mid-to-senior level across the stack, with real AI-engineering depth.

## How a session works

Each session follows the same shape, enforced through [CLAUDE.md](CLAUDE.md):

1. **Algorithm warmup (15–30 min).** One coding problem, roughly 60% Python and 40% JavaScript.
   Problems are described in real-world terms and not named after their pattern, so recognition has
   to be earned. New patterns get a short lesson first; established ones are drilled and later
   re-tested cold.
2. **Applied recall (2–3 min).** A scenario question pulled from an earlier topic, to force
   retrieval rather than recognition.
3. **Roadmap topic (45–120 min).** One sub-topic from the current section, ending with an applied
   exercise — an explain-back, a diagram, a scenario, or a small piece of code.
4. **Warm-down quiz.** A 5–7 question quiz (recall, "explain why," trade-offs, one applied scenario)
   before a section can close. Results are logged, and gaps trigger re-teaching.
5. **Capstone.** A formal assessment or architecture defense gates section completion.

Work is logged per section: what was covered, what was quizzed, and where understanding was shaky. A
pattern is marked complete only once it has been recalled cold, on a new problem, with no scaffolding.

## Roadmap

Numbered top-level directories map to the curriculum. Each has its own `CLAUDE.md` with a sub-topic
checklist, session log, weak-spot tracking, and capstone definition.

| # | Section | Focus |
|---|---|---|
| 01 | [Algorithms](01-algorithms/) | Python + JS fluency, core patterns, recognition under interview conditions |
| 02 | [System Design](02-system-design/) | Request lifecycle, networking, scaling, caching, queues, DB architecture, resilience, observability, case studies |
| 03 | [AI Foundations](03-ai-foundations/) | Embeddings, vector search, chunking, basic RAG |
| 03.5 | [OOP Fundamentals](03.5-oop-fundamentals/) | Four pillars, composition vs inheritance, Python dunders, dataclasses |
| 04 | [Backend](04-backend/) | FastAPI + Express, Postgres schema/indexing/EXPLAIN, Redis cache-aside |
| 05 | [AI Production](05-ai-production/) | Production RAG, hybrid search (BM25 + embeddings), pgvector, evaluation, cost control |
| 06 | [Frontend Performance](06-frontend/) | React rendering model, memoization, code splitting, virtualization |
| 07 | [DevOps Essentials](07-devops/) | Docker, Compose, CI/CD pipelines, deployment strategies |
| 08 | [Kubernetes & Terraform](08-kubernetes-terraform/) | Conversational competence |
| 09 | [Engineering Judgment](09-engineering-judgment/) | Architecture teardowns, build-vs-buy, post-mortems, OSS reading |
| 10 | [Interview Prep](10-interview-prep/) | Per-technology question banks |

A separate pull-based [reps/](reps/) track holds short, runnable build exercises (full-stack CRUD,
frontend, backend, devops) for rebuilding hands-on coding fluency.

## Repo structure

```
level-up/
├── CLAUDE.md                  # Mentor protocol + master tracker
├── JOHN-GUIDE.md              # Day-to-day operating manual
├── 01-algorithms/
│   ├── CLAUDE.md              # Pattern tracking, problem log
│   ├── python/{fundamentals,patterns}/
│   └── typescript/{fundamentals,patterns}/
├── 02-system-design/
│   ├── CLAUDE.md
│   ├── notes/                 # Topic files: request lifecycle → observability
│   ├── assignments/           # Applied design exercises
│   └── interview-questions.md # Question bank with answers
├── 03-.../                    # Same shape per section
├── reps/                      # Pull-based hands-on build exercises
└── .vscode/tasks.json         # File watchers for Python/TS algo work
```

Each directory is self-contained: its own `CLAUDE.md` tracker and its own venv or `package.json` for
any project, with no global dependencies beyond the algorithm runners. The `CLAUDE.md` trackers are
the main work product — they record what has been covered and where each topic stands.

## Tooling

- **VSCode + Claude Code.** The mentor protocol lives in `CLAUDE.md` and is read at the start of each session.
- **Algorithm watchers.** `nodemon --exec python` for Python and `tsx watch` for TypeScript,
  pre-configured in `.vscode/tasks.json`. Saving a file re-runs it.
- **Per-project environments.** Each backend/AI project has its own venv or `package.json`.
- **Git.** Weekly commits to main; single-author, no branching strategy.

## On AI assistance

The mentor in this system is an LLM. The point is not to avoid AI but to use it the way a junior uses
a senior engineer: to be challenged, corrected, and held to a standard. The code in the algorithm
directories and the notes files are written by hand; the LLM teaches, generates problems, runs
quizzes, and keeps the tracking honest. The aim is to use AI to learn faster while keeping the
reasoning and writing my own.
