# Build Reps

Hands-on, runnable coding reps to rebuild production fluency — prioritized for live /
paired-programming interviews. Fluid and pull-based, not a fixed curriculum.

## How to use

Say **"let's do a rep"** (or "build-rep") on any day you're up for it. Claude reads
[CLAUDE.md](CLAUDE.md), surfaces the **Backlog** menu, and proposes a rep (or invents a fresh one)
based on your energy / time / category mood — then confirms scope + scaffold dial before any code.

- **Source of truth:** [CLAUDE.md](CLAUDE.md) — protocol, scaffold dial, Backlog menu, In Progress,
  and the Completed log.
- **Cadence:** ~weekly, opt-in. Never auto-scheduled.
- **Priority:** full-stack CRUD and other interview-transferable reps first; anything goes otherwise.

## Folder convention

Each rep is its own subfolder with an **isolated env** (per-project venv / node_modules), e.g.
`reps/001-drillhole-tracker/backend/` + `/frontend/`. Code lives in the rep folder; `CLAUDE.md`
only tracks. Rep 000 (the Deep Core `samples-app`) lives under `sandbox/interview-prep/deep-core/`
for historical reasons and is logged in `CLAUDE.md` by reference.

## Division of labor

Claude scaffolds boilerplate — env, **frontend markup/CSS**, stubs, dummy data, config. **I write
the business logic** — API routes, CORS, SQL, React hooks/forms/state. The scaffold dial
(Heavy / Medium / Light) drifts toward Light as fluency returns.
