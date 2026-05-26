# Multi-Agent Governance (Light) — My Notes

> **Status:** Not yet taught.
> **Lesson plan:** [../lesson-tracker.md](../lesson-tracker.md) → Multi-Agent Governance Light section.
> **Concept-level, not framework alphabet soup.** Goal: discuss governance in your own words, not recite NIST/OWASP lists.

---

## Chunk 1 — What "governance" actually means for an agentic system
- **Governance** = policies + controls + traceability that makes autonomous systems **safe to deploy**
- NOT about restricting agents -> about making them **auditable + correctable + accountable**
- **3 pillars:**
    1. **WHAT agents can do** - role boundaries, capability scope
    2. **WHO approves** - RBAC, identity-aware orchestration
    3. **HOW you trace** - audit trails, decision logging

- **Why it exists:** autonomous agents WILL act incorrectly. Without governance, errors compound and you can't trace what went wrong and where. Critical for regulated industries

---

## Chunk 2 — Role boundaries + human-in-the-loop (HITL) checkpoints
- **Role Boundary** = each agent has explicit role + scoped permission

- **Why this is GOVERNANCE, not just clean architecture:**
  - Boundaries **limit blast radius** when an agent is compromised or hallucinates
  - If one agent gets prompt-injected, it can only do what its role allows
  - Without boundaries, one bad agent can ruin your whole system
  - Auditable separation of concerns

- **HITL triggers:**
  - Irreversible actions
  - Low confidence
  - High-risk operations

---

## Chunk 3 — Audit trails + accountability (who did what, when, why)
- **The 7 fields every agent decision must log:**
    1. **Timestamp**
    2. **Agent ID + version**
    3. **Inputs**
    4. **Tool calls + args**
    5. **Outputs**
    6. **Confidence score**
    7. **HITL approvals + policy violations**

---

## Chunk 4 — Escalation policies + tiered autonomy

_Your notes:_

---

## End-of-Lesson Self-Quiz Answers

_Filled in after Claude runs the quiz._
