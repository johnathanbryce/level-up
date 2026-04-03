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

### Coding Challenges (Build from Scratch, No AI)

- [ ] Debounced search input with API call
- [ ] Virtualized list (render only visible items)
- [ ] Component that demonstrates useMemo impact (with profiling)
- [ ] Custom hook: useDebounce
- [ ] Custom hook: useFetch with caching
- [ ] Drag and drop interface (stretch goal)

---

## Session Log

| Date | Topics Covered | Assessment | Next Focus |
|------|---------------|------------|------------|
| — | — | — | — |

---

## Notes & Weak Spots

- (none yet)
