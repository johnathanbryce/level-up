# React Interview Questions

Curated mid-to-senior React questions, sourced from real 2025-2026 interview content. Focus is on logic, hooks, performance, and state — **not styling, not Next.js routing, not UI building.** John is already comfortable with the frontend; this is about deepening internals fluency and preparing for live coding rounds.

Each question has: a short prompt, what to demonstrate, and the discussion points an interviewer would expect.

---

## Tier 1 — Custom Hooks & Async (most common live-coding)

### 1. Build a `useDebounce` hook
Build a `useDebounce(value, delay)` hook. Use it inside a search input that hits a fake API on each debounced change.
- **Demonstrate:** `useEffect` cleanup (cancel pending timeout), proper dependency array, separation of input state vs debounced state.
- **Discuss:** Why debounce vs throttle? What happens if the user types fast and then unmounts mid-debounce? How does this differ from React Query's built-in debouncing?

### 2. Build a `useFetch` hook with loading/error/data states
`useFetch(url)` returns `{ data, loading, error, refetch }`.
- **Demonstrate:** `AbortController` to cancel in-flight requests on unmount or URL change, race condition handling (don't set state from a stale fetch).
- **Discuss:** Why this is a known footgun. Why most teams use React Query / SWR instead. What problems those libraries solve that a hand-rolled hook doesn't.

### 3. Build a debounced search input that hits an API
Combines #1 and #2. Type into an input → after 300ms of no typing → fetch results → render them. Cancel previous in-flight requests when a new one starts.
- **Demonstrate:** Composing hooks, race conditions, loading states, empty/error UI.
- **Discuss:** What if the slow request returns *after* the fast request? How do you guarantee the UI shows the latest result, not the latest *response*?

---

## Tier 2 — Performance & Rendering

### 4. Memoization quiz: when does it actually help?
Given a parent component with 5 children — some receive primitive props, some receive object props, some receive callback props. Predict which re-render when the parent re-renders. Then optimize.
- **Demonstrate:** `React.memo`, `useMemo`, `useCallback`, referential equality.
- **Discuss:** When memoization is wasted (cheap re-renders, props that change every render anyway). Why React.memo is useless if a parent passes a fresh object every time.

### 5. Build a virtualized list (render only visible items)
Render a list of 10,000 items. Only the visible ones (plus a small buffer) should be in the DOM.
- **Demonstrate:** Scroll position tracking, computing visible range, absolute positioning of items, handling variable row heights (or fix to constant for simplicity).
- **Discuss:** Why DOM nodes are expensive. When virtualization is overkill. Existing libraries (`react-window`, `react-virtual`) and what they solve.

### 6. Identify the re-render bug
Given a snippet with Context that re-renders every consumer on any change. Identify the bug and fix it.
- **Demonstrate:** Splitting context, memoizing context value with `useMemo`, when to reach for an external state library.
- **Discuss:** Why Context isn't a state library. The "context split" pattern. When Zustand / Jotai / Redux make sense.

---

## Tier 3 — State & Patterns

### 7. Convert a `useState` mess into `useReducer`
Given a form with 6 `useState` hooks and tangled update logic. Refactor to `useReducer`.
- **Demonstrate:** Action types, reducer purity, state shape design.
- **Discuss:** When reducer is overkill (1-2 fields), when it shines (interrelated state, multi-step flows).

### 8. Pagination component (controlled vs uncontrolled)
Build a paginated table that takes a `data` array and `pageSize`. Includes prev/next/page-jump.
- **Demonstrate:** Slicing logic, edge cases (last page, empty data, page out of range), keyboard accessibility (bonus).
- **Discuss:** When to do client-side pagination vs server-side. How cursor-based pagination differs from offset-based and why infinite scroll usually wants cursors.

### 9. Build an error boundary
Wrap a component that intentionally throws. Show fallback UI. Make it reset.
- **Demonstrate:** Class component (error boundaries can't be functional yet), `componentDidCatch`, `getDerivedStateFromError`, reset key pattern.
- **Discuss:** What error boundaries catch and what they don't (event handlers, async, SSR). How they integrate with Sentry/observability.

---

## Tier 4 — Senior-flavor curveballs

### 10. Explain (in code) why this useEffect is wrong
Show a snippet with a missing dependency / infinite loop / stale closure. Identify and fix.
- **Demonstrate:** Closures, dependency arrays, the "stale closure" problem.
- **Discuss:** Why the linter rule exists. When you'd suppress it intentionally and document why.

### 11. Implement `useLocalStorage`
A hook that syncs state to localStorage and reads initial value from it on mount.
- **Demonstrate:** SSR safety (window check), JSON serialization, cross-tab sync (bonus, via `storage` event).
- **Discuss:** Hydration mismatches, why this is harder than it looks in Next.js.

### 12. Build a form with controlled inputs and validation
Email field, password field, submit button. Validate on blur. Show inline errors. Disable submit while invalid.
- **Demonstrate:** Controlled inputs, blur vs change validation, accessibility (label associations, ARIA).
- **Discuss:** When to reach for `react-hook-form` or `formik`, what they solve.

---

## Notes on usage

- These are **logic-first** challenges. Don't get sidetracked styling them. A working unstyled solution beats a half-built styled one.
- For Block 3 use, pick a question that aligns with the topic just covered in Section 6. For on-demand use, pick whatever John asks for.
- Time-box each at 30-60 min. If you blow past that without progress, it's a signal the underlying concept needs more main-roadmap time.
