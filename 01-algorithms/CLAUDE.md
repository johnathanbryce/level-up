# Algorithms — Progression Tracker

## Overview

Daily algorithm practice running alongside all other sections. **Language split: ~60% Python, ~40% TypeScript.** Python is the primary skill to rebuild, but TypeScript must stay sharp. Claude manages the rotation — roughly 3 Python sessions for every 2 TypeScript sessions. John can override on any given day. Claude generates challenges calibrated to current level — no strict LeetCode list, but covers the same essential patterns. Claude tracks difficulty and progression per language independently.

## Goals

1. Rebuild Python coding fluency (syntax, stdlib, idiomatic patterns)
2. Master core algorithm patterns used in mid-level interviews
3. Develop ability to solve medium-difficulty problems independently within 25 minutes
4. Build comfort with timed problem-solving under interview conditions

## Runner Setup

**Python:** Uses `pytest-watch` (`ptw`) for live reloading. Run `ptw` in the `01-algorithms/python/` directory — tests auto-rerun on save. Each challenge should have a solution file and a test file (e.g., `two_sum.py` + `test_two_sum.py`). Install once: `pip install pytest-watch`.

**TypeScript:** Uses `tsx --watch` for live reloading. Run `tsx --watch solution.ts` — re-runs on save. Install once: `npm install -g tsx`.

**First session setup:** If these aren't installed yet, guide John through the install — it's two commands and takes 30 seconds.

## Current Level

**Python Fluency:** Beginner-Intermediate (can read well, writing is weak)
**Algorithm Patterns:** Not yet assessed
**Target Level:** Comfortable solving medium problems in Python within 25 min

---

## Phase 1: Python Fundamentals (start here)

Focus on Python syntax and stdlib before diving into algorithm patterns. Each session starts with a small drill.

- [ ] String manipulation (slicing, reversal, common methods)
- [ ] List operations (append, extend, insert, pop, slicing)
- [ ] List comprehensions (basic, conditional, nested)
- [ ] Dictionary operations (creation, iteration, get, setdefault)
- [ ] Dictionary comprehensions
- [ ] Set operations (union, intersection, difference)
- [ ] Tuple unpacking and usage patterns
- [ ] collections module: Counter
- [ ] collections module: defaultdict
- [ ] collections module: deque
- [ ] itertools basics (zip, enumerate, map, filter)
- [ ] Lambda functions
- [ ] String formatting (f-strings)
- [ ] File I/O basics
- [ ] Error handling (try/except patterns)
- [ ] Type hints basics

**Status:** NOT STARTED

---

## Phase 2: Core Algorithm Patterns

Each pattern: learn the concept, solve 3-5 problems, demonstrate mastery before moving on.

### Tier 1 — Essential (do these first)

- [ ] Hash Maps / Dictionaries (frequency counting, lookups, two-sum style)
- [ ] Two Pointers (sorted arrays, palindromes, container problems)
- [ ] Sliding Window (fixed and variable size, substring problems)
- [ ] Stack (matching brackets, monotonic stack, expression evaluation)
- [ ] Queue / Deque (BFS prep, sliding window max)
- [ ] Binary Search (sorted arrays, search space problems)

### Tier 2 — Important

- [ ] BFS (level-order traversal, shortest path in unweighted graphs)
- [ ] DFS (tree traversal, graph exploration, backtracking foundation)
- [ ] Tree Traversal (inorder, preorder, postorder — recursive and iterative)
- [ ] Recursion fundamentals (base case, recursive case, call stack)
- [ ] Sorting algorithms (understand mergesort, quicksort — not memorize, understand)

### Tier 3 — Interview Polish

- [ ] Dynamic Programming: basic (climbing stairs, fibonacci, coin change)
- [ ] Dynamic Programming: intermediate (longest common subsequence, knapsack)
- [ ] Greedy algorithms (interval scheduling, jump game)
- [ ] Graph basics (adjacency list, BFS/DFS on graphs, connected components)
- [ ] Linked List operations (reversal, cycle detection, merge)
- [ ] Heap / Priority Queue (top-K problems, merge K sorted)

**Status:** NOT STARTED

---

## Phase 3: Interview Simulation

Timed problems (25 min solve + 5 min review). Mix of all patterns. Simulate real interview conditions.

**Status:** NOT STARTED — begin after Phase 2 Tier 2 is solid

---

## Problem Log

Track every problem solved. Format:

| Date | Problem Description | Pattern | Language | Result | Time | Notes |
|------|-------------------|---------|----------|--------|------|-------|
| — | — | — | — | — | — | — |

---

## Weak Spots

Track patterns or concepts that consistently cause trouble. Revisit these periodically.

- (none yet)

---

## TypeScript Sessions

~40% of algorithm sessions should be in TypeScript. Same patterns and progression as Python but adapted for TS idioms. Claude manages the rotation (roughly 2 out of every 5 sessions). Track TS progression separately — John may be at different skill levels in each language for the same pattern.

| Date | Pattern | Problem | Result | Time | Notes |
|------|---------|---------|--------|------|-------|
| — | — | — | — | — | — |

---

## Session Log

Append a brief entry after each algorithm session.

| Date | What Was Practiced | Assessment | Next Focus |
|------|-------------------|------------|------------|
| — | — | — | — |
