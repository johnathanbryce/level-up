# Algorithms — Progression Tracker

## Overview

Daily algorithm practice running alongside all other sections. **Language split: ~60% Python, ~40% TypeScript.** Python is the primary skill to rebuild, but TypeScript must stay sharp. Claude manages the rotation — roughly 3 Python sessions for every 2 TypeScript sessions. John can override on any given day. Claude generates challenges calibrated to current level — no strict LeetCode list, but covers the same essential patterns. Claude tracks difficulty and progression per language independently.

## Goals

1. Rebuild Python coding fluency (syntax, stdlib, idiomatic patterns)
2. Master core algorithm patterns used in mid-level interviews
3. Develop ability to solve medium-difficulty problems independently within 25 minutes
4. Build comfort with timed problem-solving under interview conditions

## Runner Setup

File watchers that rerun scripts on save. Output is via `print()` (Python) or `console.log()` (TypeScript) in the terminal. No test framework needed — just write code, save, see output.

**Python:** Uses `nodemon --exec python`. Install once: `npm install -g nodemon`.
**TypeScript:** Uses `tsx watch`. Install once: `npm install -g tsx`.

**How to start:** Open the file you're working on in VSCode, hit `Cmd+Shift+P` → "Run Task" → pick "Algo: Python Watcher" or "Algo: TypeScript Watcher." The watcher runs in a dedicated terminal panel and reruns the file every time you save.

**First session setup:** If `nodemon` or `tsx` aren't installed yet, guide John through the install — it's two commands (`npm install -g nodemon tsx`) and takes 30 seconds.

## Current Level

**Python Fluency:** Beginner-Intermediate (can read well, writing is weak)
**JavaScript Fluency:** Intermediate (strong in React context, needs assessment in raw algorithmic JS)
**Algorithm Patterns:** Not yet assessed in either language
**Target Level:** Comfortable solving medium problems in both Python and JS within 25 min

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

## JavaScript Sessions

~40% of algorithm sessions should be in JavaScript. **Write modern JavaScript syntax** — `const`, `let`, arrow functions, array methods, destructuring, etc. Do NOT focus on TypeScript-specific features (generics, interfaces, complex type annotations) during algorithm warmups. The goal is practicing logic and patterns in JS, not wrestling with the type system. Files can be `.ts` for the runner but the code itself should be plain modern JS. Claude manages the rotation (roughly 2 out of every 5 sessions). Track JS progression separately — John may be at different skill levels in each language for the same pattern.

**Context:** John has ~3 years of JS/TS/React experience. He is NOT a beginner — but he wants to revisit fundamentals to ensure he can write them fluently from scratch without framework crutches. React patterns (useState, JSX, component composition) are muscle memory. Raw algorithmic JS (manipulating arrays without .map in JSX, building data structures, writing utility functions from scratch) may have gaps. Phase 1 should move fast where he's solid and slow down where gaps appear.

### Phase 1: JavaScript Fundamentals (start here)

Revisit core JS to ensure fluency outside of React context. Expect to move faster than Python Phase 1 — but Claude should quiz aggressively and not let John skate past anything he can't actually write cold.

**Variables, Types & Primitives**
- [ ] `let`, `const`, `var` — scoping differences (block vs function scope)
- [ ] Primitive types vs reference types (why `[] === []` is false)
- [ ] Type coercion gotchas (`==` vs `===`, truthy/falsy values)
- [ ] `null` vs `undefined` — when each appears and why

**Strings**
- [ ] String methods: `slice`, `substring`, `split`, `join`, `includes`, `indexOf`, `replace`, `trim`
- [ ] Template literals and tagged templates
- [ ] String iteration and character access
- [ ] Common interview string patterns (reversal, palindrome check, anagram detection)

**Arrays**
- [ ] Core mutating methods: `push`, `pop`, `shift`, `unshift`, `splice`, `sort`, `reverse`
- [ ] Core non-mutating methods: `slice`, `concat`, `flat`, `Array.from`
- [ ] Iteration methods: `map`, `filter`, `reduce`, `forEach`, `find`, `findIndex`, `some`, `every`
- [ ] `reduce` deep-dive — can you use it to implement map, filter, groupBy, flatten?
- [ ] Array destructuring and rest/spread (`[first, ...rest] = arr`)
- [ ] Sorting with custom comparators (`arr.sort((a, b) => a - b)`)

**Objects**
- [ ] Object creation, property access (dot vs bracket notation)
- [ ] Object destructuring and renaming (`const { name: userName } = obj`)
- [ ] Spread operator for shallow copies (`{ ...obj, newProp: value }`)
- [ ] `Object.keys()`, `Object.values()`, `Object.entries()` — iteration patterns
- [ ] Optional chaining (`?.`) and nullish coalescing (`??`)
- [ ] Computed property names (`{ [dynamicKey]: value }`)

**Functions**
- [ ] Arrow functions vs function declarations (hoisting, `this` binding)
- [ ] Default parameters
- [ ] Rest parameters (`...args`)
- [ ] Closures — can you explain what a closure is and write one intentionally?
- [ ] Higher-order functions (functions that take/return functions)
- [ ] IIFE pattern (know what it is, even if rarely used now)

**Modern JS Patterns**
- [ ] Destructuring in function parameters (`function({ name, age })`)
- [ ] Spread/rest in different contexts (arrays, objects, function args)
- [ ] `Set` and `Map` objects — creation, common methods, when to use over plain objects/arrays
- [ ] `for...of` vs `for...in` — which iterates what
- [ ] Short-circuit evaluation patterns (`&&`, `||`, `??`)
- [ ] Ternary chaining and when it becomes unreadable

**Async Fundamentals**
- [ ] Promises: creation, `.then`, `.catch`, `.finally`
- [ ] `Promise.all`, `Promise.race`, `Promise.allSettled`
- [ ] `async`/`await` — syntactic sugar over Promises
- [ ] Error handling with try/catch in async functions
- [ ] Event loop basics — can you explain why `setTimeout(fn, 0)` doesn't run immediately?

**Status:** NOT STARTED

---

### JS Problem Log

| Date | Problem Description | Pattern | Result | Time | Notes |
|------|-------------------|---------|--------|------|-------|
| — | — | — | — | — | — |

---

## Session Log

Append a brief entry after each algorithm session.

| Date | What Was Practiced | Assessment | Next Focus |
|------|-------------------|------------|------------|
| — | — | — | — |
