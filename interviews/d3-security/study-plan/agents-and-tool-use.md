# Agents + Tool Use — My Notes

> **Status:** Not yet taught.
> **Lesson plan:** [../lesson-tracker.md](../lesson-tracker.md) → Agents + Tool Use section.
> Most directly D3-relevant note — Morpheus is an autonomous security operations agent. Take notes carefully.

---

## Chunk 1 — Single LLM call vs agent loop (when each wins; the cost-compounding trap)

- **The default reflex:**
  - **Default = single LLM call with a structured output**
  - Reach for an agent loop ONLY when the task needs dynamic tool discovery or course-correction mid-task

- **Why this matters:**
  - Agent loops accumulate context every turn - prompt + tools + observations all replay back into the next call
  - Context explodes -> cost compounds -> latency grows -> reliability drops
  - A 3-step agent run is often 5-10x the cost of one well-structured call

- **When agent loop is genuinely the right tool:**
  - The shape of the answer ISN'T known up front
  - The system needs to call tools, see the result, and _decide what to do next_ based on the result

- **When single call wins:**
  - Answer shape is known (extract these 5 fields, classify these into 3 buckets)
  - No tools needed, or tools are deterministic
  - Latency and cost matter

- **Interview line:** *"Agent loops are powerful but expensive. I default to a single structured call and only reach for the loop when the task requires dynamic discovery or mid-task course-correction."*

---

## Chunk 2 — ReAct pattern (Thought → Action → Observation loop) + failure modes

- What it stands for: **Re**asoning + **Act**ing - turns LLMs from "answer in one shot" to "think -> do -> see -> think again"

- **The loop:** Thought → Action → Observation → Thought → Action → Observation → ... → Final Answer
  - **Thought:** model reasons what to do next ("I need to check the user's recent logins")
  - **Action:** model picks a tool + args
  - **Observation:** tool returns result, fed back into next prompt
  - Repeat until model emits "Final Answer"

- **The 4 failure modes:**
  1. **Infinite loops** - agent stuck calling same tool repeatedly, or Thought -> Action with no progress
  2. **Hallucinated tool calls** - invents a tool that doesn't exist or invents arguments
  3. **Long-horizon decay** - quality degrades as steps pile up
  4. **Silent 200 with junk** - returns a normal-looking response that's actually empty/wrong ('I have completed the task' when nothing happened)

- **Mitigations:**
  - Max-step budget (hard iteration cap)
  - Strict tool schemas + validation
  - Reflection/critic step before final answer
  - Output validation downstream

- **Interview line:** *"ReAct gives you transparency and adaptiveness, but trades them for four failure modes — infinite loops, hallucinated tool calls, long-horizon decay, and silent 200s with junk."*

---

## Chunk 3 — Plan-and-execute (~40% cheaper than ReAct; natural HITL gate)

- Different topology vs. ReAct. Two phases instead of one loop:
  1. **Plan phase** - LLM produces a structured, ordered plan (list of steps + tool calls) ONCE up front
  2. **Execute phase** - runtime executes the plan step-by-step, deterministically (no LLM between steps unless something fails)

- **Replanning:** only when step fails or returns unexpected data
- **Why it's cheaper than ReAct:**
  - One big planning call vs. replan-every-step
  - Far fewer total LLM calls = less compounding growth + context growth
  - Plan = single artifact, single Human In The Loop gate (HITL), vs ReAct = approve every action mid-loop
    - **Single HITL gate on the plan itself, before any action fires** — human reviews the whole plan once, approves once, then execution is deterministic

- **When ReAct vs. when P&E:**
    - **ReAct** — real-time / interactive / dynamic discovery; step N depends on step N-1's actual output
    - **P&E** — production SLAs, regulated/auditable, multi-step coding, batch jobs where work is plannable up front

**Examples via Claude:**

- Plan mode in Claude Code = plan-and-execute. I produce a plan → you review (the HITL gate) → on approval, execution fires. Perfect mapping.
- Edit Automatically = ReAct. Thought (internal reasoning) → Action (tool call: Read/Edit/Bash) → Observation (tool result) → next Thought → loop until done. Canonical implementation.

---

## Chunk 4 — Reflection / self-critique (Reflexion, critic agent, self-refine)

- **Reflection pattern** = generate → evaluate → revise. One extra LLM round to lift output quality.
- **Critic agent** (separate LLM judges, rigorous, expensive) vs. **self-refine** (same LLM judges itself, cheaper, weaker — same biases).
- **Use for high-stakes outputs** (security verdicts, code that auto-deploys); **skip for latency-sensitive paths.**

---

## Chunk 5 — Function calling / tool use (provider landscape, schema discipline, failure modes)

- Tool use IS what makes agents do anything - without it, an LLM is a text generator with opinions
- All providers use JSON schema to define tools
- **Tool definition shape (JSON schema):**

        {
        "name": "query_auth_logs",
        "description": "Get login attempts for a user in the last N hours.",
        "parameters": {
            "type": "object",
            "properties": {
            "user_id": { "type": "integer", "description": "..." },
            "hours": { "type": "integer", "description": "..." }
            },
            "required": ["user_id", "hours"]
          }
        }

- **Schema discipline**
  - **Descriptions matter more than names** - the model picks tools based on description text
  - **required vs optional** must be explicit - vague schemas -> hallucinated args
  - **Strict types** - e.g. _"type: "integer"_ not _"type": "number"_ when you mean integer
  - **Enum constraints** where values are known - prevents the model from inventing values

- **tool_choice** parameter (the lever)
  - **auto** - model decides whether to call a tool (default)
  - **required** - model MUST call SOME tool (not necessarily the right one)
  - **{specific_tool}** - force a specific tool

  ```python
  # 1. auto (default) — model decides whether to call any tool
  client.chat.completions.create(
      model="gpt-4",
      messages=[...],
      tools=[query_auth_logs, get_user_profile],
      tool_choice="auto",
  )

  # 2. required — model MUST call SOME tool
  #    Use when: model under-fires (refuses to call tools when it should)
  #    Don't use when: model picks WRONG tool — required just forces another wrong pick
  client.chat.completions.create(
      ...,
      tool_choice="required",
  )

  # 3. specific tool — force exactly one tool (for testing, pinned workflows)
  client.chat.completions.create(
      ...,
      tool_choice={"type": "function", "function": {"name": "query_auth_logs"}},
  )
  ```

  **Senior framing:** `tool_choice` is a knob for *whether* a tool fires, not *which* tool fires correctly. Mis-selection is a schema/description problem, not a `tool_choice` problem.

- **Parallel tool calls** - most providers support multi tools in one turn.

- **Failure modes:**
  - **Hallucinated arguments** — model invents a `user_id` that doesn't exist (mitigation: validate args + retry with error feedback)
  - **Wrong tool picked** — ambiguous descriptions or overlapping tools
  - **Selection accuracy drops hard without schema discipline**

- **Interview line:** *"Tool use accuracy is dominated by schema discipline. Descriptions, strict types, required-vs-optional, and validation-with-retry are extremely important to implement correctly."*

---

## Chunk 6 — MCP (Model Context Protocol) — the "USB-C of AI integration"
- **What it is:**
  - Open standard for **LLM <--> tool integration**
  - One connector standard, any tool plus into any LLM

- **What MCP standardizes (3 things)**
    1. **Tool discovery** - how an LLM finds out what tools are available on a server
    2. **Tool call format** - how the LLM invokes a tool (request shape)
    3. **Audit trail format** - how the call gets logged

- **Before MCP:** every LLM provider had its own tool format -> fragmented integrations + audit loops across providers. Migrating from OpenAI tools to Anthropic tools meant rewriting tool definitions
- **After MCP:** write once, plug into any compliant LLM. **Governance can audit any tool call regardless of which LLM made it**

- **Why this matters for Morpheus / D3:** 800+ tool integrations is the kind of surface MCP was designed for. Regulated security workflows need a single, standardized audit trail.

### MCP is NOT LangChain

- **LangChain** abstracts the **LLM side** — Python library, runs IN your app, uniform `.invoke()` across Claude/GPT/Gemini. *Client-side library.*
- **MCP** abstracts the **tool side** — network protocol BETWEEN your app and tool servers, standardizes the tool integration shape. *Network protocol.*
- They can coexist: a LangChain app can use an MCP client to talk to MCP servers.

### Architecture (before vs after)

**Before MCP:** 3 LLM providers × N tools = N×3 wrappers, N×3 audit formats
```
Claude API ← (Anthropic's tool format) ← Your wrapper #1 → Postgres
OpenAI API ← (OpenAI's tool format)    ← Your wrapper #2 → Postgres
Gemini API ← (Google's tool format)    ← Your wrapper #3 → Postgres
```

**After MCP:** N tools, written once
```
Claude  ─┐
OpenAI  ─┼→ [MCP client in your app] ──(MCP protocol)──→ [Postgres MCP server] → Postgres
Gemini  ─┘
```

### The 3 pieces (the mental model)

1. **MCP Server** — small process that wraps a capability. Says "I expose these tools, these resources, these prompts." Examples:
   - `@modelcontextprotocol/server-postgres` — read your DB
   - `@modelcontextprotocol/server-github` — read/write GitHub
   - `@modelcontextprotocol/server-filesystem` — local files
   - `@modelcontextprotocol/server-slack` — Slack
2. **MCP Client** — lives in your LLM app, speaks the MCP protocol. Claude Desktop, Cursor, Windsurf, Cline all ship with one. You can embed one in custom apps.
3. **MCP Protocol** — JSON-RPC over stdio or HTTP. Standard message shapes: `list_tools`, `call_tool`, `list_resources`, `read_resource`.

### Concrete: Claude Desktop config (real, runnable today)

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres",
               "postgresql://localhost/mydb"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_TOKEN": "ghp_xxx" }
    }
  }
}
```
Claude Desktop reads this on startup → spawns server processes → talks to them via MCP → exposes their tools to Claude. **Zero code changes to Claude, zero code changes to Postgres.**

### When MCP is right vs overkill (the senior decision)

**MCP is right when:**
- 10+ tools (integration boilerplate compounds)
- Supporting multiple LLM providers (cost optimization / fallback)
- Need third-party / customer tool extensibility (Cursor plugin ecosystem model)
- Regulated environment requiring unified audit log across heterogeneous tools
- "Tool surface" itself is a product feature

**MCP is overkill when:**
- MVP / pre-PMF startup — ship fast, validate first
- Single LLM provider, no swap planned
- <10 internal tools
- No multi-tenant extensibility needed
- Simple AI feature (RAG-only chat, classification, summarization)

**MVP recommendation:** start with **native function calling** (Anthropic `tool_use`, OpenAI `function_calling`). Migrate to MCP when you hit one of these triggers:
- Managing 10+ tool definitions and the boilerplate hurts
- You decide to support multiple LLM providers
- You add third-party / customer tool extensibility
- A regulated audit requirement appears

**MCP is a refactor target, not a starting architecture.** Same logic as "do we need Kubernetes on day 1?" — usually no.

---

## Chunk 7 — Multi-agent orchestration (supervisor / pipeline / swarm / hierarchical)
- **Supervisor** - orchestrator, delegates to specialist
- **Pipeline** - sequential chain, agent N+1 transforms agent N's output
- **Swarm** - parallel agents, merge results
- **Hierarchical** - multi-level supervisor of supervisors

- **These are composable patterns, NOT mutually exclusive choices.** Real production systems mix them:
  - **Supervisor** at the top + each specialist IS a **pipeline** internally
  - **Hierarchical** is literally nested supervisors
  - **Swarm** of supervisors, each supervising a pipeline
  - Morpheus-likely shape: top-level supervisor routes alerts → one specialist is a pipeline (enrich → investigate → verdict) → another is a swarm (parallel evidence gathering)

- **Failure mode: context inconsistency** - agents don't share state, step on each other
    - **Mitigation:** shared state store + structured handoff messages

---

## Chunk 8 — Agent frameworks (LangGraph for regulated)
- **LangGraph** - graph-based state machine for agents. THE framework for regulated/auditable workflows
    - Agents + tools modeled as nodes in a directed graph; transitions are explicit
    - Built-in check-pointing
    - Built-in audit trail
    - Pairs with LangSmith for observability

- **Interview line:** *"For a regulated security workflow like Morpheus, LangGraph is the right choice:. Graph-based architecture maps directly onto audit trails and HITL gates that regulated AI systems need*

---

## Chunk 9 — Human-in-the-loop (HITL) + tiered autonomy

### Tiered autonomy (THE answer to "Multi-Agent Governance")

For every action an agent is about to take, ask two questions:
1. **How confident am I in this decision?**
2. **How bad is it if I'm wrong?** (blast radius / reversibility)

Map the answers to one of three tiers:

| Tier | Condition | What happens | Morpheus example |
|---|---|---|---|
| **T1** | High confidence + low risk | **Auto-action**, no human | Auto-close a known-benign phishing alert |
| **T2** | Mid confidence OR mid risk | **HITL approval gate** — agent pauses, waits for human yes/no | Quarantine an endpoint (reversible, but real cost) |
| **T3** | Low confidence OR destructive/irreversible action | **Full analyst review** — agent hands off, human decides | Disable a user account; push global firewall rules |

Key insight: it's **(confidence × risk)**, not just one axis. A 99%-confidence action can still be T3 if it's destructive enough (you don't want to push global firewall rules on autopilot even at high confidence).

- **Two flavors of HITL:**
    1. **Approval gate** - binary yes/no reviewed by human. Agent doesn't continue without approval
    2. **Collaborative edit** - human modifies the proposed action before approving

- **Identity-aware orchestration:**
    - Agent pauses -> request goes to authorized human
    - **Time-boxed window** - if no response in N minutes, escalate or fail
    - Full audit log: who approved when, with what context
    - **RBAC** enforces who can approve what (T2 analyst can approve quarantine; only a T3 lead can approve global firewall changes)

- **Interview line:** *"Tiered autonomy maps confidence × risk into auto-action, HITL approval, or full analyst review — with RBAC enforcing who can approve what, and time-boxed windows forcing escalation if no one responds."*

---

## Chunk 10 — Production gotchas + security (token explosion, prompt injection via tools)
- **Token cost explosion** - hard $/run, kill switch at threshold
- **Infinite retry loops** - max-step budget + loop detection
- **Hallucinated tool calls** - strict schema validation + retry-with-error-feedback.

- **Security - the D3 critical component**
  - **Prompt injection through the tool output** is THE agent-specific security threat. Attacker plants malicious instructions in data the agent retrieves, LLM can't distinguish data from instructions, and now the attacker is steering your agent 

- **5 mitigations:**
    1. **Isolate system prompts from user/tool input** - the system-prompt boundary IS the trust boundary. Never let tool output reach the system-prompt slot
    2. **Input validation** - sanitize user input before it reaches LLM (strip "ignore previous" patterns, length limits)
    3. **Output filtering** - scan LLM output before executing tool calls 
    4. **Least-privilege tool access** - each agent gets only the tools it needs; no agent has read-all + write-all
    5. 

---

## D3 / Morpheus Mapping

_Notes on how these primitives map to Morpheus's autonomous SOC architecture:_

---

## End-of-Lesson Self-Quiz Answers

_Filled in after Claude runs the quiz._
