# Agentic Orchestration (Area 1 — THE screen)

> Articulation cram. Deliverable per item = tight spoken line + honest anchor. ~15-25 sec each: name it, take a position, caveat, STOP.

## Planner + deterministic tools (one-liner only — do NOT lecture)

_Target line:_ "The model decides which operation and with what params; deterministic services do anything that must be exactly right. At Caseway my agents don't invent case law — they call Elasticsearch and reason over real results."

## ReAct vs planner-executor

- **ReAct** = think -> act -> observe (looping). Modal decides the next step based n the last result
    - **Adaptive** to surprises, but can **loop or drift** and cost more 
    - Casey retrieval agent is ReAct 

- **Planner-executor** = produce the **full plan first** and then execute it. 
    - The plan is **inspectable before anything runs** -> a natural **HITL** gate and **cheaper**
    - Trade-off: **less-adaptive** mid-run if reality differs from the plan
    - **When to pick planner-executor:** when you want the plan *reviewed before execution* (trust/regulated/expensive operations) and cost/latency matters
    - **Deep-core tie-in:** a 3D model build is expensive and expert-reviewed -> planner-executor lets the geologist see the plan before the geostat compute runs ReAct fits the cheaper, exploratory retrieval loops 

## The trust stack (how an expert accepts agent output)
- **Grounding** - the agent reasons over real data (RAG / your data layer), doesn't free-associate (Casey ES retrieval)
- **Structured outputs as contracts** - between steps yu pass **typed, validated JSON** (e.g. Pydantic.) If it doesn't validate, you don't execute.
- **Validation gates - 3 kinds:**
    - **Schema** - is it well-formed? (structured-output check above)
    - **Semantic** - is it sensible? (geo ex: reject a physically impossible geology number)
    - **HITL** - the expert reviews and approves 
- **Traceability** - citations / showing the data behind the claim so the expert can verify rather than trust blindly (Casey ex: forcing it to cite relevant court cases in its responses)

*"I would assume that Deep Core's product is a HITL gate - the agent proposes, the geologists verifies.*

## Failure modes + guards
- **Failure modes:**
    - **Infinite loops / no progress** - ReAct agent keeps cycling
    - **Hallucinated tool calls** - invents a tool or bad arguments
    - **Long-horizon decay** - quality drops over many steps (context fills/drifts)
    - **Silence success** - returns junk with a 200

- **Guards**:
    - **Max loop cap** - kills infinite loops
    - **Strict schema + validation** - catches hallucinated/malformed tool calls
    - **Token budget + truncation guard** - prevents context overflow / runaway cost
    - **Retry with corrective message**
    - **Fallback/degredation** - cheap model fails -> escalate; tool down -> degrade gracefully

- **The "silent success" senior point:** only guard for junk-with-a-200 is **vals + semantic validation** - you have to check the outputs quality
- **Caseway anchors:** token/truncation guards, dual-model routing (cheap -> escalate), monitoring and observability 

## Evals (how you know the agent is good)
- **Offline evals** - a test set of inputs with known-good outputs that are scored. 
    - Often **LLM-as-judge** (a model grades the output aganst criteria). Run on every change to catch regressions
- **Online evals** - production monitoring: track quality/faithfulness, cost-per-call, error rates, drift over time

- **Deep Core relevance:** you could track the amount of times an expert (geologist) needed to accept an agents proposal unedited versus a heavy rework of its output. Acceptance rate as the most critical metric

## The Deep Core design-out-loud (six beats)

1. **Planner agent** ingest the NL query + data summary -> emits a **structured plan** of modeling operations
2. **Validation gate on the plan** - schema + semantic before anything expensive runs
3. **Geo services** execute each step - the LLM does not do the math
    - **HOW (tool calling / function calling):** you register tools w/ the LLM (name + description + param schema, e.g. `run_kriging(dataset_id, variogram, range)`). The LLM doesn't run code — it *emits a structured tool-call request* (which op + which params). **Your orchestration code** executes the real service, gets the result, feeds it back. LLM = brain (decides what); your code = hands (runs it). **Fully automated — no human in this loop.** Human only enters at the HITL gate (beat 6).
    - **Caseway parallel:** this IS my manual tool-calling loop — agent decides "search ES for X", my code runs the query, returns results, agent reasons. Deep Core just swaps ES retrieval for a kriging service. Same mechanism, different tool.
4. **Structured outputs** flow between steps and a **validate at each hop** - bad step caught before it corrupts the next
5. **Render** the candidate model in **Cesium** for the geologist
6. **Human gate** - geologist accepts or refines in NL -> **loop back**

A solid approach for planning a system like this at a high level: one HITL gate early, one gate at the end.
- **Plan-approval gate (early)** -> **deterministic compute** -> **render** -> **accept/refine gate (final)**
