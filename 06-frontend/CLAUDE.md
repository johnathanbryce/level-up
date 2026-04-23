# Frontend Performance — Progression Tracker

## Overview

Deep dive into React internals, rendering behavior, and performance optimization. Johnathan has ~3 years of React experience — this section isn't about learning React from scratch, it's about understanding WHY things work the way they do and being able to optimize and articulate decisions in interviews.

## Definition of Done

Can explain React's rendering model to an interviewer, identify performance bottlenecks in a component tree, implement optimizations with measurable results, and know when optimization is premature vs warranted.

---

## Sub-Topics

### React Rendering Model

- [ ] How React decides when to re-render (state change, prop change, parent re-render)
- [ ] Virtual DOM reconciliation — what actually happens during a re-render
- [ ] React Fiber: what it is (high level), concurrent features
- [ ] Why unnecessary re-renders matter (and when they DON'T matter)
- [ ] React DevTools Profiler — how to use it to identify bottlenecks

### Memoization

- [ ] React.memo: what it does, when it helps, when it's wasted
- [ ] useMemo: memoizing expensive computations — with real examples of "expensive"
- [ ] useCallback: memoizing function identity — why it only helps with memoized children
- [ ] The anti-pattern: memoizing everything (premature optimization)
- [ ] Referential equality: why objects/arrays as props break memoization

### State Management Patterns

- [ ] State colocation: keeping state as close to where it's used as possible
- [ ] When to lift state up vs use context vs use a state library
- [ ] useReducer: when it's better than useState (complex state logic)
- [ ] Context API: how it works, performance implications (every consumer re-renders)
- [ ] Context + useMemo pattern to reduce unnecessary re-renders
- [ ] When you actually need an external state library (and which ones)

### Advanced Hooks

- [ ] useRef: beyond DOM references (storing mutable values without re-renders)
- [ ] useTransition: non-blocking state updates for heavy renders
- [ ] useDeferredValue: deferring non-urgent updates
- [ ] Custom hooks: extracting and composing logic, dependency management
- [ ] Hook rules and why they exist (call order, conditional hooks)

### Performance Optimization Techniques

- [ ] Code splitting with React.lazy and Suspense
- [ ] Dynamic imports and route-based splitting
- [ ] Virtualization for long lists (concept + implementation)
- [ ] Debouncing and throttling user input
- [ ] Image optimization and lazy loading
- [ ] Bundle analysis: identifying what's bloating the bundle

### Block 3 Interview Mini-Challenges

When a sub-topic has a clean interview-question equivalent, pull from `10-interview-prep/react/` as the optional third block of a session. Not every session — only when there's a natural fit. The React interview prep folder is logic-focused (hooks, performance, state, async) — no styling, no Next.js routing. See `10-interview-prep/CLAUDE.md` for usage.

### Coding Challenges (Build from Scratch, No AI)

- [ ] Debounced search input with API call
- [ ] Virtualized list (render only visible items)
- [ ] Component that demonstrates useMemo impact (with profiling)
- [ ] Custom hook: useDebounce
- [ ] Custom hook: useFetch with caching
- [ ] Drag and drop interface (stretch goal)

---

## End-of-Section Capstone

Frontend performance knowledge is only real if you can find problems in unfamiliar code — not just describe patterns you already know. Two parts.

### Part 1 — Performance Audit (30-40 min)
Claude provides a deliberately broken, unoptimized React component tree with 4-6 embedded issues: unnecessary re-renders, incorrect `useEffect` dependency arrays, missing memoization where it matters, wrong state placement, referential equality traps breaking `React.memo`, etc. John must:
1. Identify every issue and explain specifically why it's a performance problem
2. Fix each one with the correct tool (memo, useCallback, useMemo, colocation, etc.)
3. For the two most impactful fixes, describe what he'd look for in React DevTools Profiler to confirm the improvement

### Part 2 — Rendering Model Verbal (10 min)
Without notes: explain React's rendering model as if teaching it to an experienced developer who hasn't learned the internals — when it re-renders, what reconciliation actually does, how Fiber enables concurrent features, and what the practical implication is for how you write components. Claude asks 2-3 follow-ups targeting the weakest point in the explanation.

**Pass criteria:** All Part 1 issues correctly identified and fixed with accurate reasoning, Part 2 explanation is coherent and accurate with no major gaps. Section closes when both pass. Log result in Session Log below.

**Capstone result:** NOT YET RUN

---

## Session Log

| Date | Topics Covered | Assessment | Next Focus |
|------|---------------|------------|------------|
| — | — | — | — |

---

## Notes & Weak Spots

- (none yet)
