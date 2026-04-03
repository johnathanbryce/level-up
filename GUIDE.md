# Level-Up System: User Guide

This file is for YOU (John), not for Claude. It covers how to interact with the system, when to start new context windows, and how to keep everything aligned.

---

## Starting a Session

Open the `level-up` folder in VSCode. Open a new Claude chat. Type:

> "Let's begin today's session."

That's it. Claude will read CLAUDE.md, check where you left off, and brief you on what's next. If it doesn't do this automatically, say:

> "Read CLAUDE.md and follow session protocol."

---

## When to Start a New Context Window

Start a **new window** when any of these happen:

1. **You're switching topics.** If you just finished your algorithm warmup and want to move to the roadmap topic, that's fine in the same window. But if you're moving from system design to a completely different section (like frontend), consider a fresh window so Claude can load the right section's context cleanly.

2. **The conversation is getting long.** If you've been going back and forth for 30+ messages, Claude's ability to hold earlier context starts degrading. Wrap up, let Claude update the tracking files, and start fresh. You'll lose nothing because everything important is in the files.

3. **Claude starts giving vague or repetitive answers.** This is the clearest signal the context window is getting crowded. Don't push through it — wrap up and start a new window.

4. **You're starting a new day.** Every new day should ideally be a new window. Clean slate, fresh context, Claude reads the latest state from the files.

5. **You finished a major sub-topic or milestone.** After completing a pattern in algorithms or finishing a system design case study, that's a natural breakpoint.

**Rule of thumb:** One window per session (algorithm warmup + roadmap topic block). If a session runs long, split into two windows at the natural boundary between algorithm and roadmap work.

---

## How to End a Session

Before closing a window, ALWAYS say:

> "Let's wrap up. Update the tracking files."

Claude will update:
- The CURRENT STATE section in the root CLAUDE.md
- The relevant section's CLAUDE.md (checkboxes, session log, weak spots)
- The algorithm tracker if you did a warmup

**Wait for Claude to confirm the updates are written before closing the window.** If you close before updates happen, the next session starts with stale information.

If you forget and close early, start the next session with:

> "I closed the last session without updating tracking. Here's what I did last time: [brief summary]. Update the tracking files with this, then let's begin."

---

## Mid-Session Commands

These are things you can say during a session to steer Claude:

- **"Skip the warmup today."** — Jump straight to roadmap topic.
- **"Let's do TypeScript today."** — Override the language rotation.
- **"This is a rabbit hole. Let's move on."** — If you feel stuck and want to flag it and progress.
- **"I want to go deeper on this."** — If Claude is moving too fast past something you want to understand better.
- **"Quiz me on [topic]."** — Have Claude test your understanding.
- **"Explain this like I've never seen it."** — Reset Claude's assumptions about your knowledge on a topic.
- **"Review my code."** — Trigger an honest code review.
- **"I want you to code this part."** — Explicitly hand control to Claude for scaffolding/boilerplate/implementation.
- **"Where am I in the roadmap?"** — Get a quick status check.
- **"What are my weak spots?"** — Claude reviews tracking files and summarizes areas that need work.

---

## If Things Go Wrong

**Claude isn't following the system:**
Say: "Re-read the root CLAUDE.md and follow the mentor rules and session protocol."

**Claude is being too easy on you:**
Say: "You're being too soft. Challenge me harder and don't let me skate past things."

**Claude is dragging a topic out:**
Say: "I've got this. Quiz me to confirm, and if I pass, let's move on."

**Tracking files look wrong or outdated:**
Say: "Read the tracking files and tell me what the current state looks like. Something seems off."

**You want to adjust the roadmap:**
Come back to the Desktop Claude app (Cowork mode) for strategic planning conversations. The VSCode Claude should focus on execution, not restructuring the curriculum.

---

## What Lives Where

- **Root CLAUDE.md** — Master brain. Roadmap, rules, current state. Claude reads this every session.
- **Section CLAUDE.md files** — Granular tracking per domain. Checklists, session logs, weak spots.
- **GUIDE.md (this file)** — For you. How to use the system. Claude doesn't need to read this.
- **Code directories** — Where your actual work goes. Algorithms, projects, exercises.
- **.gitignore** — Standard ignores. Don't touch unless you add new tooling.

---

## Weekly Maintenance

Every Friday (or whenever you wrap up for the week):

1. Say "Let's do a weekly review" to Claude. It should summarize the week's progress across all sections.
2. Commit and push: `git add -A && git commit -m "weekly update" && git push`
3. (Optional) Scan the tracking files yourself to make sure they reflect reality.
