# Python Dict Patterns

## Frequency counting with `.get()`

The most common dict pattern: counting how many times something appears. Instead of the verbose if/else:

```python
# verbose
if char in counts:
    counts[char] += 1
else:
    counts[char] = 1
```

Use `dict.get(key, default)` — returns the value if the key exists, otherwise returns the default. So:

```python
# idiomatic
counts[char] = counts.get(char, 0) + 1
```

Read it as: "the new count is whatever was there before (or 0 if nothing) plus one." Use this every time you're counting.

## Structural equality with `==`

Python's `==` on dicts (and lists, tuples, sets) does **deep structural equality**: same keys, same values for each key. Order does not matter.

```python
{"a": 1, "b": 2} == {"b": 2, "a": 1}   # True
[1, 2, 3] == [1, 2, 3]                  # True
```

So when you need to check "do these two dicts/lists represent the same data?" — just use `==`. No looping required.

## `collections.Counter` — the stdlib shortcut

When the *whole point* of the code is "count occurrences," skip the manual dict and use `Counter`:

```python
from collections import Counter

Counter("listen")
# Counter({'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1})

# Anagram check becomes one line:
def valid_anagram(s, t):
    return Counter(s) == Counter(t)
```

`Counter` is a `dict` subclass, so all dict operations work on it (including `==`).

When to use which:
- **Manual dict + `.get()`** — when counting is one step inside a larger algorithm and you want explicit control
- **`Counter`** — when frequency counting *is* the algorithm

---

# Python vs JavaScript: `==` Equality Gotcha

One of the biggest cross-language gotchas. The same-looking operator means different things.

## Python: deep structural equality on built-in containers

```python
{"a": 1} == {"a": 1}    # True   ✓
[1, 2] == [1, 2]        # True   ✓
(1, 2) == (1, 2)        # True   ✓
```

Python compares contents recursively. Two different objects with the same data are equal.

## JavaScript: reference equality on objects/arrays

```js
({a: 1}) === ({a: 1})   // false  ✗
[1, 2] === [1, 2]       // false  ✗
```

JS only does structural equality on **primitives** (numbers, strings, booleans). Objects and arrays are compared by reference — "are these literally the same object in memory?" Two different objects with identical contents are NOT equal.

## How to do deep equality in JS

There's no built-in. Common workarounds:
- `JSON.stringify(a) === JSON.stringify(b)` — quick and dirty, breaks on key order, undefined, functions, dates
- Lodash `_.isEqual(a, b)` — the real answer in production code
- Hand-rolled recursive comparison

## Why this matters

When switching languages:
- **JS → Python:** "wait, I can just `==` two dicts? really?" Yes. Use it.
- **Python → JS:** "why is `[1,2] === [1,2]` false?!" Because JS reserves structural equality for primitives only.

This is the kind of thing that causes silent bugs when moving between codebases.
