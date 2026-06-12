# Approach & Tooling — Open Decisions

Decisions to make **together** before we start designing. Nothing here is locked.
Each is logged as: the question, the options, John's lean, the honest take, and a STATUS.

---

## Decision 1 — Repo strategy (separate git repo vs. sub-folder here)

**John's lean:** move this to its own repo for version control; reasoning that using git
for a non-traditional-SWE deliverable signals git fluency "outside the VC terminal."

**Honest take (read this before deciding):**

- **Using git here is a legitimately good call** — but be precise about *why*, because the
  framing matters for what you do with it.
- **The weak version of the reasoning:** "interviewers will see I know git and it'll stand
  out." ⚠️ Mostly false. They will almost certainly **never look at your commit history.**
  A case-study panel evaluates the *design and your reasoning*, not your `git log`. If the
  repo sits private on your machine, the git-ness is invisible and earns nothing.
- **The strong version (this is the real value):**
  1. **Portfolio artifact.** A clean public GitHub repo — good README, diagrams committed,
     pseudo-code, an `assumptions.md` — is a durable thing you can link in future
     applications. *This* is where "I treat solutions work with engineering rigor" actually
     shows. That maps directly to the AI Solutions Architect / forward-deployed-engineer role.
  2. **Presentation surface.** They explicitly allow presenting from VSCode. If the repo
     README *is* your walkthrough (problem → design → flows → pseudo-code → eval), then the
     repo becomes the thing on screen — and the structure/version-control *does* become
     visible, on your terms. That's the only path where the "git stands out" instinct pays off.
  3. **Clean separation** from `level-up` (this learning repo) so it's shareable without
     dragging your whole study history along.
- **Net recommendation:** **Yes, its own repo — but commit to presenting from it** (README as
  the spine) so the rigor is actually seen. If you'd present from slides/Word instead, the
  separate repo is just tidy housekeeping (still fine, just not a "signal").
- **Sequencing:** keep building groundwork in *this* folder for now (low friction). When we
  start the real design, `git init` a fresh repo (e.g. `diligent-case-study` /
  `enterprise-ir-platform-design`) and either move or copy these files over. Don't nest a
  git repo inside the `level-up` repo — that creates a submodule-ish mess. Clean break.

**DECIDED (2026-06-12):**
- ✅ **Public GitHub repo** — so the panel can actually see it + portfolio value after.
- ⬜ Present-from-README vs slides/Word: **TBD — John planning tool choices over the weekend.**

**STATUS:** 🟡 partially decided (public repo locked; presentation surface pending weekend planning)

---

## Decision 2 — Diagramming tool

Prompt says "any diagramming tool." Candidates:

| Tool | Pro | Con |
|------|-----|-----|
| **Excalidraw** | Fast, clean, exports PNG/SVG, feels like whiteboarding | Not version-control-friendly (binary-ish `.excalidraw` JSON) |
| **Mermaid** | **Lives in markdown, diffs in git, renders on GitHub** | Less layout control; can get ugly for big architectures |
| **draw.io / diagrams.net** | Powerful, professional output, `.drawio` is XML (diffable-ish) | Heavier; more time fiddling |
| Lucidchart / Miro | Slick, collaborative | Cloud, export friction, overkill |

**Honest take:** if we go the repo-as-presentation route (Decision 1), **Mermaid** is the
synergy pick — diagrams live in the README, version-control nicely, and render on GitHub with
zero export step. Use **Excalidraw** for one or two "hero" visuals if Mermaid gets cramped.
**Decide Decision 1 first** — it constrains this.

**STATUS:** ⬜ undecided

---

## Decision 3 — Presentation surface (what's on screen during the 1 hour)

Options: (a) VSCode + README/markdown walkthrough; (b) slides (PowerPoint/Google Slides);
(c) Word doc. Cathy + the email both say **VSCode is fine** and polish isn't graded.

**John's comfort zone = VSCode.** Leaning (a). Ties into Decision 1 — if repo-as-spine, this
is automatic. Confirm.

**STATUS:** ⬜ undecided

---

## Decision 4 — Pseudo-code format

They want "high-level pseudo code (sequencing, steps, logic)." Decide: language-flavored
Python-ish pseudo-code (reads naturally, John's rebuild language) vs. truly language-agnostic
step lists. Lean: **Python-flavored pseudo-code in fenced blocks** — concrete enough to show
real understanding, not so concrete it looks like we were asked to code (we weren't).

**STATUS:** ⬜ undecided

---

## Decision 5 — Solution scope (DEFERRED — do not decide yet)

The actual architecture (RAG design, ACL-aware retrieval, Excel I/O, agentic write-back,
eval strategy, etc.) is the *content* and comes after the tooling decisions above. Logged here
only so it isn't forgotten. **Next session.**

**STATUS:** ⬜ not started (intentionally)

---

## Suggested order of operations (for the next working session)

1. Settle Decisions 1–4 (≈15 min — they're mostly one call: "repo + README + Mermaid + VSCode"
   as a bundle, or not).
2. Spin up the repo if we go that way; move these files.
3. *Then* start Decision 5 — the real design work, requirement by requirement.
