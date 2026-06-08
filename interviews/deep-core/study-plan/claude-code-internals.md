# Claude Code Internals + Agent-Assisted Dev (Lesson 2)

### MCP - Model COntext Protocol
- Open standard for connecting LLMs to external tools / data sources / services through one uniform interfact
- **Problem it solves:** without it, every integration is a bespoke one-off. MCP standardizes **tool discovery + call format + response format** - any MCP client can talk to any MCP server
- "USB-C of AI integrations"
- **Deep core tie:** their data is hetergenous (drillhole DBs, geophysics, PDFs, etc.). MCP servers expose each source to the agent cleanly + auditably instead of custom glue per source. 

### Hooks
- Runs automatically on lifecycle events - pre/post tool use, on-stop, etc.
- **Stronger than a prompt:** a prompt is a *request* a model can ignore or forget; a hook is *guaranteed* code that runs every time
- **Examples:** lint/list after every edit; block a tool call touching protected files; log every action

### Subagents
- Spawn focused child agents for scoped/independent work, each with its **own context window**
- Parallel fan out for independent tasks
- Keeps main context clean

### Context / Compaction
- Context window is finite; long sessions fill it. **Compaction** = auto-summarizing earlier conversations so work continues without losing the thread
- Don't trust the window, externalize durable state to files (CLAUDE.md)
- This mentor service does exactly this - CLAUDE.md state survives across windows

---

## MCP — how it actually works (implementation)

> **Unlearn this:** MCP is NOT about switching between models. It standardizes the connection between *an agent and tools/data*. The "easy to switch" benefit is the other direction — because a server speaks a standard protocol, *any* MCP client (Claude Code, Cursor, your own app) can use it. Write the integration once, every client consumes it.

**Architecture (client ↔ server):**

```
┌──────────────────────┐     MCP protocol      ┌─────────────────────┐
│   MCP Host / Client  │   (JSON-RPC over      │     MCP Server      │
│  (Claude Code, your  │◄───stdio or HTTP/SSE)─►│ (wraps ONE tool or  │
│   VSCode agent, an   │                       │   data source)      │
│   app you build)     │                       │                     │
└──────────────────────┘                       └─────────────────────┘
   • the LLM app                                  • exposes: tools,
   • discovers tools                                resources, prompts
   • sends tool-call requests                     • e.g. Postgres, GitHub,
   • feeds results to the model                     filesystem, your API
```

**Runtime flow:** client connects → asks "what tools do you have?" (**discovery**) → server returns tool schemas → LLM emits a tool-call → client forwards it → server runs the real code → returns result → model reasons over it. *(Same tool-calling loop as the six-beat design — MCP just makes the wiring standard + reusable.)*

**1. Configure which servers your client connects to** (Claude Code / Desktop = JSON config):

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"]
    }
  }
}
```

**2. A minimal MCP server you'd write** (Python, official SDK) — exposing one geology tool:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("geo-tools")

@mcp.tool()
def run_kriging(dataset_id: str, variogram: str, range_m: float) -> dict:
    """Run ordinary kriging on a dataset and return the interpolated grid."""
    result = geostats_service.krige(dataset_id, variogram, range_m)
    return {"grid_id": result.id, "cells": result.cell_count}

if __name__ == "__main__":
    mcp.run()
```

Now any MCP client can discover + call `run_kriging` — no bespoke wiring. **Deep Core use:** run MCP servers wrapping the drillhole DB, geophysics store, report PDFs → the agent layer reaches all of them through one uniform, auditable interface.

## Hooks — how it actually works (implementation)

Hooks live in `settings.json` as **shell commands that fire on events**. Example — lint + tests after *every* file edit:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "ruff check . && pytest -q" }
        ]
      }
    ]
  }
}
```

The **harness** runs this after the Edit/Write — the model can't skip it; if it fails, output goes back as feedback. Prompt instruction = best-effort (model may forget); **hook = guaranteed.**
