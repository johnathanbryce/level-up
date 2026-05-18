# React + TypeScript — Speaking Vocabulary

You use React every day. This is NOT for learning — it's a vocab refresh so you can *speak* about it intelligently in an interview without searching for words mid-sentence.

---

## React

### Virtual DOM

React keeps an in-memory representation of the UI (the "Virtual DOM") and **diffs** the previous tree against the next one when state changes. Only the changed nodes get committed to the real DOM. This is what makes React fast — direct DOM manipulation is expensive; diffing in memory is cheap.

> **Common confusion (interview gotcha):** Virtual DOM ≠ Shadow DOM.
> - **Virtual DOM** is a *React* runtime concept — the in-memory tree React diffs against.
> - **Shadow DOM** is a *browser* feature for Web Components — encapsulates a component's DOM + CSS so styles don't leak (think `<video>` controls).
> If you mean React's in-memory tree, say "Virtual DOM."

### Reconciliation

The diffing algorithm itself. React walks the new tree, compares to the previous, and computes the minimum set of DOM mutations. **Keys on list items are critical** — without stable keys, React assumes worst-case and re-renders every item in the list. Using array indexes as keys for dynamic lists is the classic bug.

### Re-renders + immutability

A React component re-renders when (a) its state changes, (b) its props change by reference, or (c) its parent re-renders. **State and props must be replaced, not mutated.**

- ✓ `setState({...state, count: state.count + 1})` — new object reference, triggers re-render.
- ✗ `state.count++` — mutates in place, React doesn't detect the change.
- ✓ `setArr([...arr, item])` — new array, triggers re-render.
- ✗ `arr.push(item)` — mutates the existing array, React doesn't detect.

This is the "you said mutations" thing. React detects changes by **reference equality**, not deep equality. New object reference = new render.

### Common hooks (canonical 6)

- **`useState`** — local component state. Returns `[value, setter]`. Setter call triggers a re-render.
- **`useEffect`** — side effects after render (fetching, subscriptions, DOM manipulation). Dependency array controls when it re-runs. Empty `[]` = run once on mount.
- **`useMemo`** — memoize an expensive computation. Recomputes only when listed dependencies change.
- **`useCallback`** — memoize a function *reference*. Useful when passing callbacks to memoized children.
- **`useRef`** — mutable container that persists across renders without triggering re-renders. Common for DOM refs (`ref={inputRef}`) and storing mutable values that shouldn't cause renders.
- **`useContext`** — consume a Context value. Avoids prop drilling for things like theme, auth, user.

### Memoization — when it helps vs hurts

`React.memo`, `useMemo`, `useCallback` all add overhead (the dependency comparison check on every render). They're **only worth it when the work they prevent is more expensive than the comparison.** Wrapping every component in `React.memo` is an anti-pattern — most components re-render cheaply, and the memo overhead becomes the new bottleneck.

### State management hierarchy

- **Local state:** `useState` / `useReducer`. Default starting point.
- **Lifted state:** moved to the closest common parent of components that need it.
- **Context:** good for low-frequency global state (theme, auth, locale). Bad for high-frequency state — every consumer re-renders on every change.
- **External library:** Redux, Zustand, Jotai, etc. — for app-wide state with complex updates or where Context causes too many re-renders. Don't reach for these by default.

---

## TypeScript

### Why use TypeScript (canonical answer)

Catches type errors at compile time instead of runtime. Self-documenting — function signatures tell you what's expected. IDE intelligence (autocomplete, refactor safety). At scale, the maintenance cost of types is paid back in fewer production bugs and faster onboarding.

### Type vs Interface (interview classic)

- **Both** describe object shapes.
- **`interface`** is *extensible* via declaration merging — you can re-open and add fields later. Standard for public API contracts.
- **`type`** is more flexible (unions, intersections, mapped types, conditional types) but not extensible.
- **Rule of thumb:** use `interface` for objects others may extend; use `type` for unions and computed types.

### Utility types worth naming

- **`Partial<T>`** — all fields optional.
- **`Required<T>`** — all fields required.
- **`Pick<T, K>`** — subset of fields.
- **`Omit<T, K>`** — all fields *except* K.
- **`Record<K, V>`** — object with K keys, V values.
- **`Readonly<T>`** — all fields readonly.

### Generics (one-sentence definition)

Functions or types parameterized over other types. `function identity<T>(x: T): T` works for any T while preserving the type relationship between input and output.

---

## Likely recruiter prompts + canonical answers

- **"How long have you worked with React?"** → "About 3 years, daily. Mostly on Next.js apps in production."
- **"What about TypeScript?"** → "Same — 3 years, default mode for me. I don't reach for plain JS unless the project is already that way."
- **"How comfortable are you with React performance work?"** → "Comfortable with the vocabulary — memoization, code splitting, virtualized lists. Honest answer: I've done it, but I'd want to deepen the diagnostic side — profiling, bundle analysis."
- **"What state management have you used?"** → Honest answer with the hierarchy in mind. Probably some combo of `useState` / `useReducer` / Context, maybe Zustand or Redux if the project demanded it.

---

## Interview gotchas to NOT walk into

- **Virtual DOM vs Shadow DOM** — see above. Easy way to lose credibility.
- **`useEffect` cleanup** — the function you return from a `useEffect` runs on unmount AND before the next run if deps change. Easy to forget when handling subscriptions.
- **Stale closures** — `useEffect(() => { fn(state) }, [])` captures the initial `state` forever. Add `state` to deps or use the functional update form.
- **JSX is sugar** — `<div>hi</div>` compiles to `React.createElement('div', null, 'hi')`. Worth knowing this exists.
- **Keys** — never use array index as the key for a dynamic list. Use a stable id.
