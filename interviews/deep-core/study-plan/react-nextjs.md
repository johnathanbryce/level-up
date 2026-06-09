# React / Next.js (Area 5 — medium level, interview-ready)

## 1. Rendering model (re-render triggers, reconciliation, keys)

- A component re-renders when:
  - 1. its state changes
  - 2. its parent re-renders
  - 3. a context it consumes changes
  - 4. its props change
- It must be **state** changes for React to know

- **Batching:** React batches multiple state updates in the same event handler into **one** re-render.
  - E.g. 3 setState calls in a click handler = one render, not 3

- **State updates are asynchronous** - you won't see the new value on the next line; use the **updater form:** _setCount(c => c + 1)_ when the new state depends on the old

- **_Key_** - changing a components key forces React to **unmount and remount it** (fresh state) - a useful trick to "reset" a component

## 2. Hooks overview + Rules of Hooks

- **useState** - local component state. returns [value, setter]
- **useEffect** - run side effects after render (fetching, subs, DOM)
- **useRef** - a mutable container that persists across renders without triggering a re-render. Two uses:
  - 1. Grab a DOM node
  - 2. hold a mutable value (timer ID, prev value) you don't want to re-render on
- **useContext** - read a context value without prop drilling
- **useReducer** - state via a reducer. Reach for it when state logic is complex
- **useMemo/useCallback** - cache a value / a function identity

## 3. useEffect deep (deps, cleanup, pitfalls)

- useEffect runs side effects **after** render. Things outside React's render flow: data fetching, subs, timers, manual DOM work, logging
- **Cleanup function** - return a function from the effect; React runs it **before the next effect run and on unmount**. Essential for anything that needs teardown: unsubscribe, clear interval, abort a fetch, destroy a 3rd party instance.

## 4. State management (local / lifted / context / external; controlled vs uncontrolled)

- The Context gotcha - when a Context value changes, **every consumer re-renders**
  - Context has no selective subscription. Fixes: split by concerns, memoize the value, or use an external store (Zustand) that lets components **subscribe to slices**.
  - _"Context is for low-frequency global values, not a state-management library_

- **Server state vs. client state**: a lot of "state" is really **server data** (cached API responses). That's not what Redux is for - use **React Query / SWR / RSC** which handles caching, refetching, and staleness.

- **Controlled vs. uncontrolled components:**
  - **Controlled** - React state is the single source of truth; the input's value comes from state. onChange updates it. Predictable, validatable, the default for forms
  - **Uncontrolled** - the DOM holds the value; you read it via a _ref_ when needed
  - One-liner: _"Controlled re-renders every keystroke; uncontrolled doesn't — that's why big forms often go uncontrolled."_

## 5. Performance (memoization, code splitting, lazy, virtualization)

1. **Memoization:**
   - **React.memo** - skips a child's re-render when props are unchanged
   - **useMemo** - cache an expensive computed value
   - **useCallback** - stablize a functions identity so a memoized child doesn't see a "new" prop every render
   - useCallback memoizes the function; useMemo memoizes the function's result.

2. **Code splitting + lazy loading:**
   - Don't ship one giant JS bundle. Split so users download only what they need
   - React.lazy + Suspense to load a component only when needed
   - **Biggest win pattern:** lazy-load heavy or rarely used components (a charting lib, a 3D viewer)

3. **Virtualization (windowing)**
   - Rendering 10,000 list rows = 10,000 DOM nodes. **Virtualization** renders only the **visible** rows (+ a small buffer) and recycles them as you scroll.
   - Libraries: _react-window_, _react-virtual_

4. **Other common levers:**
   - **Debounce/throttle** expensive handlers (search-as-you-type -> debounce the API call)
   - **Stable keys** to avoid needless remounts
   - **Lift state down** - push state to the smallest subtree that needs it so changes don't re-render a big tree

- **Deep core relevance:** a Cesium 3D viewer is heavy.So you'd _dynamic()_ **import it (client-only)**, lazy-load it, keep it out of React's re-render path, and virtualize any big data tables

## 6. Server vs Client Components (App Router)

- The mental shift in the App Router: **Components are Server Components by default**, and you opt into client behavior explicitly

- **Server Components (default)**
  - Render **on the server**; their JS is **never shipped to the browser** -> smaller bundles
  - Can **fetch data directly** (async/await, hit the DB or APIs right in the component) - no useEffect, no API round-trip from the client
  - Can safely use **secrets** (API keys, DB creds) - code never reaches the client
  - **Cannot** use state, effects, or browser APIs - they don't run in the browser

- **Client Components ("use client")**
  - Run in the browser -> can use state, effects, event handlers, browser APIs
  - Needed for anything interactive
  - Their JS is shipped and they hydrate on the client

- **How to combine them:**
  - Default to Server Components; push "use client" to the leaves - the small interactive bits (a button, a form, the 3D canvas), not the whol epage
  - Goal: ship the **least client JS** - keep the static/data-heavy shell on the server

## 7. Data fetching + rendering strategies (SSR / SSG / ISR / streaming, server actions)
- 4 rendering stategies (classic Next.js interview question):
    - **SSG (Static Site Generation)** - render HTML at **build time**. Fastest possible (served from CDN) but content is frozen until next build -> marketing pages, docs, blogs
    - **SSR (Server-Side Rendering)** - render on **each request** on the server. Always fresh, good for SEO, but slower -> personalized or always-current pages
    - **CSR (Client-Side Rendering)** - render in the browser after JS loads -> highly interactive dashboards behind auth wher

- **Streaming + Suspense:** the server can **stream HTML in chunks** - send the shell immediately, stream slow parts in as they resolve. Wrap a slow component in *<Suspense fallback={...}>* -> user sees the page instantly with a skeleton, and the slow data **pops in** when ready. Avoids one whole query blocking the whole page

- **Server Actions:** functions marked *"user server"* that **run on the server but are callable from the client** (e.g. on form submit) - no manually writing an API route. Next handles the round-trip. Great for mutations (create/update) straight from a component

- **Deep Core relevance**: the app is an authenticated, interactive tool, so it leans dynamic/SSR + client interactivity, not SSG. Streaming/Suspense fits perfectly — render the shell instantly, stream in slow data (model lists, job results) rather than blocking. Server Actions are a clean way to trigger mutations like "submit a model build" without hand-rolling API routes.

## 8. Cesium-in-Next reality
