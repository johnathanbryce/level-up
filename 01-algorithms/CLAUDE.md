# Algorithms — Progression Tracker

## Overview

Daily algorithm practice running alongside all other sections. **Language split: ~60% Python, ~40% JavaScript.** Python is the primary skill to rebuild, but JS fluency must stay sharp. Claude manages the rotation — roughly 3 Python sessions for every 2 JS sessions. John can override on any given day. Claude generates challenges calibrated to current level — no strict LeetCode list, but covers the same essential patterns. Claude tracks difficulty and progression per language independently.

## Scope Boundary (IMPORTANT)

Algorithms are **pure logic warmups**. They do NOT morph into framework / API / React challenges. The whole point is language fluency without framework noise — switching them to "build a FastAPI endpoint" defeats the warmup purpose. Framework-style interview challenges live in `10-interview-prep/` and run as the optional Block 3 of a session, not in place of the algo warmup.

## Where to Begin

**Day 1:** Start with Python Phase 1 (Python Fundamentals). This is the priority language.
**When JS rotation begins (~session 3-4):** Start with JS Phase 1 (JavaScript Fundamentals).
**Each language progresses independently.** Python may be in Phase 1 while JS is already in Phase 2, or vice versa. Track and advance each language on its own timeline.
**Phase 2 and Phase 3 are shared patterns** practiced in whichever language is up in the rotation. A pattern isn't "complete" until John has demonstrated it in BOTH languages.

## Goals

1. Rebuild Python coding fluency (syntax, stdlib, idiomatic patterns)
2. Rebuild JavaScript fluency outside of React context (raw algorithmic JS)
3. Master core algorithm patterns used in mid-level interviews — in both languages
4. Develop ability to solve medium-difficulty problems independently within 25 minutes
5. Build comfort with timed problem-solving under interview conditions

## Challenge Delivery Rules

When presenting an algorithm challenge, Claude should:

1. **If the challenge involves a concept John hasn't seen yet in this system** (check the Phase checklists and Problem Logs), give a brief contextual intro — 2-3 sentences explaining what the concept is, why it matters, and a quick example of how it works. Then present the challenge. This is NOT a lecture — just enough context to attempt the problem without Googling.

2. **If the challenge involves a concept John has already covered and demonstrated understanding of**, skip the intro. Just present the problem. He should recognize the pattern.

3. **If John fumbles a concept he's supposedly already learned**, that's a signal. Flag it as a weak spot, note it in the Weak Spots section, and schedule a revisit in a future session.

This creates a natural reinforcement loop: first encounter = explanation + practice, subsequent encounters = just practice, failure on a known concept = flagged for review.

## Runner Setup

File watchers that rerun scripts on save. Output is via `print()` (Python) or `console.log()` (JS) in the terminal. No test framework needed — just write code, save, see output.

**Python:** Uses `nodemon --exec python`. Install once: `npm install -g nodemon`.
**JavaScript/TypeScript:** Uses `tsx watch`. Install once: `npm install -g tsx`.

**How to start:** Open the file you're working on in VSCode, hit `Cmd+Shift+P` → "Run Task" → pick "Algo: Python Watcher" or "Algo: TypeScript Watcher." The watcher runs in a dedicated terminal panel and reruns the file every time you save.

**First session setup:** If `nodemon` or `tsx` aren't installed yet, guide John through the install — it's two commands (`npm install -g nodemon tsx`) and takes 30 seconds.

## Current Level

**Python Fluency:** Beginner-Intermediate (can read well, writing is weak)
**JavaScript Fluency:** Intermediate (strong in React context, needs assessment in raw algorithmic JS)
**Algorithm Patterns:** Not yet assessed in either language
**Target Level:** Comfortable solving medium problems in both Python and JS within 25 min

---

# PYTHON TRACK

## Python Phase 1: Fundamentals

Focus on Python syntax, stdlib, and core language features before diving into algorithm patterns. This is the foundation — don't rush it.

**Data Types & Basic Operations**

- [ ] String manipulation (slicing, reversal, common methods)
- [ ] String formatting (f-strings)
- [ ] List operations (append, extend, insert, pop, slicing)
- [ ] List comprehensions (basic, conditional, nested)
- [x] Dictionary operations (creation, iteration, get, setdefault) — basic create/iterate/in solid; `.get()` shortcut introduced but needs reinforcement
- [ ] Dictionary comprehensions
- [x] Set operations (union, intersection, difference) — learned via Intersection of Two Arrays problem; knows `&` / `.intersection()`, `|` / `.union()`, `-` / `.difference()`; wrote manual set-based solution first, then learned the one-liner
- [ ] Tuple unpacking and usage patterns
- [ ] range() and its uses (basic iteration, custom ranges, reverse ranges)

**Functions & Scope**

- [ ] Function definitions (def, return, multiple return values)
- [ ] Default parameters and keyword arguments
- [ ] `*args` and `**kwargs` — what they are, when to use them
- [ ] Scope: local, global, nonlocal — how Python resolves variable names
- [ ] Lambda functions
- [ ] Higher-order functions (functions that take/return functions)

**Standard Library Essentials**

- [ ] collections module: Counter
- [ ] collections module: defaultdict
- [ ] collections module: deque
- [ ] itertools basics (zip, enumerate, map, filter)
- [ ] heapq basics (heappush, heappop, nlargest, nsmallest)
- [ ] functools: lru_cache (memoization decorator — critical for dynamic programming later)

**Error Handling & I/O**

- [ ] Error handling (try/except/else/finally patterns)
- [ ] Common exception types (ValueError, KeyError, TypeError, IndexError)
- [ ] File I/O basics (open, read, write, context manager `with` statement)
- [ ] Context managers — what the `with` statement does and why it matters

**OOP Fundamentals (REQUIRED — prerequisite for Phase 2 data structures)**

- [ ] Class definition: `class`, `__init__`, `self`
- [ ] Instance methods, instance variables
- [ ] Inheritance: single inheritance, `super()`
- [ ] Dunder methods: `__str__`, `__repr__`, `__len__`, `__eq__`
- [ ] Class methods (`@classmethod`) vs static methods (`@staticmethod`)
- [ ] Property decorator (`@property`) — getters and setters
- [ ] Build a simple class from scratch (e.g., Stack, Queue, or LinkedList node)

**Intermediate Python Patterns**

- [ ] Decorators — what they are, how to write a basic one, common built-in decorators
- [ ] Generators and `yield` — lazy iteration, memory efficiency
- [ ] Generator expressions vs list comprehensions (when to use which)
- [ ] Type hints basics
- [ ] Ternary expressions (`x if condition else y`)
- [ ] Walrus operator (`:=`) — basic awareness
- [ ] Regular expressions basics (re.match, re.search, re.findall — enough to use, not master)

**Status:** IN PROGRESS — started string manipulation

### Python Problem Log

| Date       | Problem Description                                        | Pattern                                     | Result                             | Time       | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------- | ---------------------------------------------------------- | ------------------------------------------- | ---------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-04-06 | String compression (consecutive char counting)             | String iteration, state tracking, f-strings | Solved with hints                  | ~15-20 min | Needed guidance on: tracking state across loop, appending on group change vs every iteration, flushing last group after loop. Got there with progressive hints.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 2026-04-06 | First non-repeating character                              | Hash map / dictionary, two-pass pattern     | Solved with minor hint             | ~5-10 min  | Faster than first challenge. Tripped on if/else logic (both branches firing). Knows .items() iteration and break. Hasn't learned Counter yet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 2026-04-07 | Running sum of 1d array                                    | List iteration, accumulator pattern         | Solved with hints                  | ~15 min    | Initial attempt overcomplicated: declared accumulator inside loop, added a meaningless `if nums[0]:` branch. Once reframed as "two-line loop body: update total, append total" it clicked. Wrong return type annotation (`-> int`) and returned `result[-1]` instead of full list. Briefly discussed why list comprehensions don't fit stateful accumulation; saw `itertools.accumulate` as the idiomatic stdlib option.                                                                                                                                                                                                                                                                                                              |
| 2026-04-07 | Move zeros (in-place)                                      | Array mutation, intro to two pointers       | Naive solved, two-pointer deferred | ~15 min    | Naive: built two buckets and concatenated. Forgot to mutate `nums` — important Python gotcha covered: `nums = result` rebinds local name vs `nums[:] = result` mutates in place. Two-pointer pattern (same-direction writer/reader) introduced and walked through with a trace, but John felt it was too much for current phase. Bookmarked for Phase 2 — do not grind now.                                                                                                                                                                                                                                                                                                                                                           |
| 2026-04-08 | Valid Anagram (3 approaches: sorted, manual dict, Counter) | Hash map / dictionary, frequency counting   | Solved all 3                       | ~20 min    | Sort approach clean (A-) — but used `"".join(sorted(...))` unnecessarily; lists compare structurally with `==` directly. Manual dict: built with `if char in d` pattern, didn't reach for `.get(key, default)` shortcut. Asked the right question unprompted: "is there a way to compare dicts easily in Python?" Answer: yes, `==` does deep structural equality on dicts/lists/tuples. Big cross-language gotcha vs JS surfaced (where `{a:1} === {a:1}` is false). Counter introduced as the stdlib one-liner. Notes written: `notes/python/dict-patterns.md` covering `.get()`, `==` deep equality, Counter, and the Python-vs-JS equality difference. Snake_case correction needed — JS muscle memory leaked into Python locals. |
| 2026-04-09 | Intersection of Two Arrays | Set operations, membership lookup | Solved ✓ | ~10 min | Wrote correct manual approach: build set from nums1, iterate nums2 checking membership, dedup output via set conversion. Nit: deduped after the fact (`list(set(similar_nums))`) instead of using a set for output from the start. Didn't know Python set intersection (`&` operator / `.intersection()`) — learned it after solving. Also learned `.union()` (`|`) and `.difference()` (`-`). Phase 1 set operations box checked. |

---

# JAVASCRIPT TRACK

**Context:** John has ~3 years of JS/TS/React experience. He is NOT a beginner — but he wants to revisit fundamentals to ensure he can write them fluently from scratch without framework crutches. React patterns (useState, JSX, component composition) are muscle memory. Raw algorithmic JS (manipulating arrays without .map in JSX, building data structures, writing utility functions from scratch) may have gaps. Write modern JavaScript syntax — `const`, `let`, arrow functions, array methods, destructuring, etc. Do NOT focus on TypeScript-specific features (generics, interfaces, complex type annotations). Files can be `.ts` for the runner but the code itself should be plain modern JS.

## JS Phase 1: Fundamentals

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

**`this` Keyword (common interview topic)**

- [ ] `this` in regular functions vs arrow functions
- [ ] `this` in object methods
- [ ] Explicit binding: `call()`, `apply()`, `bind()` — what each does and when to use
- [ ] `this` in event handlers and callbacks (and why arrow functions solve the problem)
- [ ] Can you predict what `this` refers to in a given code snippet? (interview question format)

**Prototypes & Inheritance (how JS actually works under the hood)**

- [ ] Prototype chain — what happens when you access a property that doesn't exist on an object
- [ ] `Object.create()` and prototypal inheritance
- [ ] How `class` syntax maps to prototypes (classes are syntactic sugar)
- [ ] `instanceof` and how it works
- [ ] Why this matters: understanding what's actually happening when you write `class Foo extends Bar`

**Modern JS Patterns**

- [ ] Destructuring in function parameters (`function({ name, age })`)
- [ ] Spread/rest in different contexts (arrays, objects, function args)
- [x] `Set` and `Map` objects — creation, common methods, when to use over plain objects/arrays (Two Sum + Contains Duplicate, 2026-04-08) NEEDS MORE PRACTICE
- [ ] `for...of` vs `for...in` — which iterates what
- [ ] Short-circuit evaluation patterns (`&&`, `||`, `??`)
- [ ] Ternary chaining and when it becomes unreadable
- [ ] Iterators and generators (`function*`, `yield`, `Symbol.iterator`) — basic awareness
- [ ] Modules: `import`/`export` vs `require()`/`module.exports` — know the difference

**Async Fundamentals**

- [ ] Promises: creation, `.then`, `.catch`, `.finally`
- [ ] `Promise.all`, `Promise.race`, `Promise.allSettled`
- [ ] `async`/`await` — syntactic sugar over Promises
- [ ] Error handling with try/catch in async functions
- [ ] Event loop basics — can you explain why `setTimeout(fn, 0)` doesn't run immediately?

**Error Handling**

- [ ] try/catch/finally patterns
- [ ] Custom error types (`class AppError extends Error`)
- [ ] Error handling in async code (try/catch with await vs .catch() on promises)

**Status:** NOT STARTED

### JS Problem Log

| Date       | Problem Description                                               | Pattern                                                                                | Result                                   | Time    | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-04-07 | Reverse a string (two ways: `.reverse()` one-liner + manual loop) | String iteration, JS fundamentals                                                      | Solved both ✓                            | ~10 min | First attempt had a bogus 1-char guard returning a message string instead of the char (contract violation) — fixed. Solid grasp of spread + reverse + join. Concept check: knew `.reverse()` mutates ✓, misunderstood `.join("")` as "removing spaces" — corrected. Manual loop was clean. Taught two senior-flavor concepts: (1) `[...str]` vs `str.split("")` Unicode difference, (2) string concatenation in a loop is O(n²) due to string immutability — push to array + join at end for O(n). Both worth remembering.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 2026-04-08 | Valid Palindrome — both reverse-and-compare AND two-pointer       | String iteration, intro to opposite-direction two pointers                             | Solved both ✓                            | ~25 min | Reverse-and-compare clean (B+, two real nits: `x ? true : false` antipattern, dead code in length guard). Then asked for two-pointer lesson — admitted he hadn't really understood it. Re-taught from first principles: pointer = index variable, opposite-direction vs same-direction, why `for...of` is the wrong loop construct here. Walked the off-by-one bug (`str.length` vs `str.length - 1`). John wrote the two-pointer version cleanly on first attempt after the lesson — A grade. This is the breakthrough on a pattern he bookmarked from yesterday. **Two-pointer (opposite direction) now unblocked.** Same-direction (Move Zeros style) still bookmarked for Phase 2. Notes written: `notes/two-pointer.md` capturing the mental model + palindrome example.                                                                                                                                                                                                                                                                                 |
| 2026-04-08 | Two Sum — both brute force AND hash map                           | Hash map / dictionary lookup, "replace search with lookup" pattern, first JS `Map` use | Solved both (heavy guidance on hash map) | ~40 min | Brute force: walked from "describe in plain English how you'd solve it by hand" → nested loop. First attempt had 3 bugs (`<=` instead of `<` on both bounds, `j = 1` instead of `j = i + 1`, dead code map declaration). Fixed cleanly after walkthrough. Hash map version: got tangled on which key to look up and what to return — wrote `numsMap.get(n)` instead of `numsMap.get(complement)`, returned `[complement, value]` instead of `[seen.get(complement), i]`. Said "I am lost" and "big fail" — neither was true; he had ~90% of the structure right and got stuck on the value-vs-index distinction. Wrote final solution for him with full line-by-line explanation. Mental model locked in: "replace search-for-something with lookup-of-something." Important emotional/pedagogical moment — wrote the solution rather than dragging him through more hints once he hit the wall, was the right call. Style nits: `let` instead of `const` on test inputs (recurring), `numsMap` vs `seen` naming (variable should describe purpose not type). |
| 2026-04-08 | Contains Duplicate                                                | Hash set, membership tracking, first JS `Set` use                                      | Solved cleanly ✓                         | ~10 min | A grade. Wrote it cold immediately after Two Sum explanation. Idiomatic: used `Set` instead of `Map` (correct judgment — only need "have I seen this?", not value+index), `for...of` instead of indexed for (correct — doesn't need `i`), good naming (`seen`), check-then-add order. Fast, clean reinforcement of the hash pattern from the Two Sum struggle. Recurring nits still present: `let` instead of `const` on test inputs, only tested one input even though four were declared, `emptryArr` typo. Also had a defensive `length <= 1` guard which is technically dead code but defensible (style call, leaving it). Pattern locked in cross-problem: hash Map + hash Set both demonstrated in the same session, picking the right tool for each question.                                                                                                                                                                                                                                                                                          |
| 2026-04-09 | Valid Anagram (JS — bonus hash map rep)                           | Hash map, frequency counting, JS `Map` mechanics                                       | Solved with guidance ✓                   | ~20 min | Two-map approach. Bugs encountered: (1) `currCharCount + 1` expression not assigned (didn't know expression vs assignment difference — important JS fundamental, now corrected), (2) missing `else` on the set-to-1 branch causing overwrite on every iteration, (3) missing `return true` at end of function (fell off without explicit return → `undefined`). Needed nudge on JS Map comparison — no built-in deep equality like Python `==`, had to write manual size + iteration check. Learned the `.get(c) || 0` idiom as JS equivalent of Python's `dict.get(key, 0)`. Shown single-map elegant version (increment first string, decrement second). Non-trivial `!` usage on `currCharCount` for TS null assertion — working but not ideal; the `|| 0` pattern avoids the need entirely. |

---

# SHARED PHASES (both languages)

These phases apply to BOTH Python and JavaScript. Practice each pattern in whichever language is up in the rotation. A pattern is only fully "complete" when demonstrated in both languages.

## Phase 2: Core Algorithm Patterns

Each pattern: learn the concept, solve 3-5 problems per language, demonstrate mastery before moving on.

### Tier 1 — Essential (do these first)

**Python Status / JS Status**

- [ ] / [ ] Hash Maps / Dictionaries (frequency counting, lookups, two-sum style)
- [ ] / [ ] Two Pointers (sorted arrays, palindromes, container problems)
- [ ] / [ ] Sliding Window (fixed and variable size, substring problems)
- [ ] / [ ] Stack (matching brackets, monotonic stack, expression evaluation)
- [ ] / [ ] Queue / Deque (BFS prep, sliding window max)
- [ ] / [ ] Binary Search (sorted arrays, search space problems)

### Tier 2 — Important

- [ ] / [ ] BFS (level-order traversal, shortest path in unweighted graphs)
- [ ] / [ ] DFS (tree traversal, graph exploration, backtracking foundation)
- [ ] / [ ] Tree Traversal (inorder, preorder, postorder — recursive and iterative)
- [ ] / [ ] Recursion fundamentals (base case, recursive case, call stack)
- [ ] / [ ] Sorting algorithms (understand mergesort, quicksort — not memorize, understand)

### Tier 3 — Interview Polish

- [ ] / [ ] Dynamic Programming: basic (climbing stairs, fibonacci, coin change)
- [ ] / [ ] Dynamic Programming: intermediate (longest common subsequence, knapsack)
- [ ] / [ ] Greedy algorithms (interval scheduling, jump game)
- [ ] / [ ] Graph basics (adjacency list, BFS/DFS on graphs, connected components)
- [ ] / [ ] Linked List operations (reversal, cycle detection, merge)
- [ ] / [ ] Heap / Priority Queue (top-K problems, merge K sorted)

**Status:** NOT STARTED

---

## Phase 3: Interview Simulation

Timed problems (25 min solve + 5 min review). Mix of all patterns. Both languages. Simulate real interview conditions.

**Status:** NOT STARTED — begin after Phase 2 Tier 2 is solid in both languages

---

# TRACKING

## Weak Spots

Track patterns or concepts that consistently cause trouble in either language. Revisit these periodically.

- **Two pointers (same-direction writer/reader):** Introduced 2026-04-07 on Move Zeros. Concept felt overwhelming. Bookmarked — revisit when Phase 2 Tier 1 begins formally. Naive approach is fine for now.
- **Two pointers (opposite direction):** ✅ UNBLOCKED 2026-04-08 via Valid Palindrome. John wrote it cleanly after a from-first-principles lesson. Pattern is now usable in JS — needs Python demonstration before being marked "complete" in both languages.
- **In-place vs rebinding in Python:** `nums = result` (rebind, caller untouched) vs `nums[:] = result` (mutate). Watch for this in any in-place problem.
- **Accumulator pattern:** Tendency to overcomplicate stateful loops with unnecessary conditionals. Reinforce: declare accumulator outside loop, update inside, that's it.
- **Snake_case in Python:** JS muscle memory leaks into Python locals (`sortedStrOne` instead of `sorted_str_one`). Function names are correct snake_case; locals are the gap. Call out every time until it's reflexive.
- **`dict.get(key, default)` for counting:** John still reaches for `if char in d / else` instead of the idiomatic `.get()` shortcut. Reinforce on next counting problem.
- **Boolean return antipattern:** `return x === y ? true : false` instead of `return x === y`. Surfaced 2026-04-08 in palindrome. Burn out of muscle memory — comparison operators already return booleans.

## Session Log

Append a brief entry after each algorithm session.

| Date       | Language   | What Was Practiced                                                | Assessment                                                                                                                                                                                                                                                                                                                                                                                                     | Next Focus                                                                                                                                                   |
| ---------- | ---------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2026-04-06 | Python     | String compression + first non-repeating char                     | Compression needed progressive hints. Hash map problem solved faster with only minor guidance. Improving within session.                                                                                                                                                                                                                                                                                       | Continue Python Phase 1 — list operations, comprehensions                                                                                                    |
| 2026-04-07 | Python     | Running sum + Move zeros (naive)                                  | Running sum: overcomplicated then cleaned up. Move zeros: naive worked, two pointers introduced but too early — bookmarked. Solid forward progress on Phase 1 list ops.                                                                                                                                                                                                                                        | Tomorrow: JS warmup first (Phase 1 start) then a Python warmup                                                                                               |
| 2026-04-07 | JavaScript | Reverse string (one-liner + manual loop)                          | Solid first JS session. Idiomatic spread/reverse/join one-liner came naturally. Concept gaps: thought `.join("")` removes spaces (corrected). Senior concepts introduced: spread vs split for Unicode, O(n²) string concatenation.                                                                                                                                                                             | Continue JS Phase 1 — strings or arrays                                                                                                                      |
| 2026-04-08 | JavaScript | Valid Palindrome (reverse-and-compare + two-pointer breakthrough) | A grade overall. Two-pointer (opposite direction) re-taught from scratch and locked in cleanly. Important breakthrough — pattern was bookmarked yesterday on Move Zeros and was overwhelming then. Today's smaller problem (palindrome) made it click. Two minor antipatterns flagged: ternary boolean returns + dead code length guards. Notes written on two-pointer.                                        | Continue JS Phase 1 — try the easier patterns now that two-pointer is unblocked, OR push into Phase 2 stack work (Valid Parentheses queued for next session) |
| 2026-04-08 | JavaScript | Two Sum (brute force + hash map) — bonus algos                    | Big learning session. Brute force solved with iterative bug fixes (loop bound off-by-ones, `j = i + 1` pattern). Hash map version: got 90% there, tangled on the value-vs-index return, asked for the full solution. Wrote it for him with full line-by-line explanation rather than over-hinting — right call. Mental model "replace search with lookup" locked in. First JS `Map` use (Phase 1 box checked). | More hash map reps to lock the pattern in — see next-day prompt                                                                                              |
| 2026-04-08 | JavaScript | Contains Duplicate — bonus algo                                   | A. Cold solo solve, immediate reinforcement of hash pattern. Correctly chose `Set` over `Map` (right tool for "have I seen this?"). First JS `Set` use (Phase 1 box checked).                                                                                                                                                                                                                                  | Continue JS hash map reps next session before normal warmup                                                                                                  |
| 2026-04-08 | Python     | Valid Anagram (sorted, manual dict, Counter — all 3 approaches)   | A-. Built all 3 approaches. Asked the right unprompted question ("can I just compare dicts?"), which surfaced the Python `==` deep-equality vs JS reference-equality gotcha. Manual dict still using verbose if/else instead of `.get()`. Snake_case slip on locals. Notes written: `notes/python/dict-patterns.md`.                                                                                           | Continue Python Phase 1 — dict comprehensions, sets, OR introduce `.get()` reinforcement next counting problem                                               |
| 2026-04-09 | JavaScript | Valid Anagram (JS — bonus hash map rep)                           | B+. Solved with guidance. Core frequency-counting logic was right but hit 3 bugs: expression-not-assigned, missing else (overwrite), missing return true. Learned expression vs assignment distinction (important JS fundamental). Learned `|| 0` default idiom for Map.get(). Shown elegant single-map version for comparison. | Continue Python Phase 1 (rotation says Python next) |
| 2026-04-09 | Python     | Intersection of Two Arrays                                        | B+. Correct manual approach using set for lookup + list for output. Nit: deduped after the fact instead of using set for output from the start. Didn't know set intersection (`&`) — learned it + union (`|`) + difference (`-`). Phase 1 set operations checked off. | Continue Python Phase 1 — tuple unpacking, list comprehensions, dict comprehensions |
