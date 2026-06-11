# Assignment: Samples Explorer (full-stack)

A small full-stack app for managing geological **samples**. Mirrors the Deep Core
shape: a Python (FastAPI) service + a Next.js/TS frontend that consumes it.

Build in **vertical slices** — get one runnable thing working end-to-end, confirm,
then layer. Don't build it all silently in one shot.

---

## Part 1 — Backend (FastAPI)  ← today

A REST API over an in-memory collection of samples (a DB comes in Part 3).

### The resource

A **sample** has:

- `id` — server-assigned, unique
- `name` — non-empty string
- `rock_type` — one of a known set (e.g. `granite`, `basalt`, `shale`, `limestone`, `sandstone`)
- `grade` — float, grams/tonne, must be `>= 0`
- `depth_m` — float, metres, must be `> 0`

### Endpoints

| Method | Path             | Behaviour                                                        |
|--------|------------------|-----------------------------------------------------------------|
| GET    | `/samples`       | List all samples. Support optional `?rock_type=` filter.        |
| GET    | `/samples/{id}`  | Return one sample. `404` if not found.                          |
| POST   | `/samples`       | Create a sample. Validate body. Return `201` + the created one. |
| DELETE | `/samples/{id}`  | Delete a sample. `404` if not found, else `204`.               |

### Requirements

- **Separate Pydantic models** for input vs output: a `SampleCreate` (no `id`) for
  the POST body, and a `Sample` (with `id`) for responses. Don't let clients set `id`.
- **Validation** enforced by the models: `grade >= 0`, `depth_m > 0`, `name` non-empty,
  `rock_type` restricted to the allowed set. Bad input should return `422` (FastAPI does
  this for you once the model is right).
- **Correct status codes** (`201` on create, `204` on delete, `404` on missing).
- Seed the store with **3–5 dummy samples** so GET returns something immediately.
- Enable **CORS** for the frontend (Part 2) to call it from the browser.

### Done when

`uvicorn` serves it, the interactive docs at `/docs` exercise every endpoint, and the
404 / 422 paths behave correctly.

---

## Part 2 — Frontend (Next.js / TS)  ← tomorrow

- Fetch and render the samples list with **loading** and **error** states.
- A **rock-type filter** input that queries the API (debounced — `useDebounce` rep).
- (Stretch) a form to create a sample, posting to the API.

## Part 3 — Persistence (SQLite)  ← tomorrow

- Swap the in-memory store for SQLite behind the same routes. Read + write through FastAPI.
