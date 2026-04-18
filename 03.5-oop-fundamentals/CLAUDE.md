# Section 3.5: OOP Fundamentals

## Overview

Vanilla Python and JavaScript. No frameworks. The goal is to understand OOP as a programming paradigm — the four pillars, the design judgment, when to use it vs. functional — so that when framework-specific patterns appear in Section 4 (FastAPI, SQLAlchemy), they read naturally rather than requiring re-learning.

**Language split:** Primarily Python. JS woven in at concepts where the contrast or comparison genuinely accelerates understanding (inheritance/prototypes, polymorphism via duck typing). Not a parallel track — Python-first, JS as anchor points.

**Definition of Done:** Can explain the four pillars from scratch, implement each in Python, articulate when OOP is the right tool vs. functional, and read class-based framework code without confusion.

**Status:** NOT STARTED

---

## Sub-topics

### 1. Classes and Objects
- [ ] What a class is vs. an instance (the blueprint vs. the thing)
- [ ] `class` keyword, `__init__`, `self`
- [ ] Instance attributes vs. class attributes
- [ ] The mutable class attribute trap — shared state across instances
- [ ] JS anchor: `class`, `constructor`, `this` — map the mental model across

### 2. Encapsulation
- [ ] Bundling data and behavior together — why this matters
- [ ] Access control conventions: `_protected`, `__private` (name mangling)
- [ ] `@property` — getter/setter without explicit get/set methods
- [ ] When to expose vs. hide — the design judgment
- [ ] JS anchor: no true private until `#field` syntax (ES2022) — contrast with Python conventions

### 3. Inheritance
- [ ] "Is-a" relationships — when subclassing is the right call
- [ ] `super()` and why skipping it causes silent bugs
- [ ] Method overriding — when and how to override cleanly
- [ ] Single vs. multiple inheritance (Python supports both; know the MRO exists)
- [ ] JS anchor: prototypal inheritance under the hood; how `class extends` maps to Python's model

### 4. Polymorphism
- [ ] Same interface, different behavior across subclasses
- [ ] Method overriding as the primary tool
- [ ] Duck typing in Python — "if it walks like a duck" and why it matters
- [ ] How polymorphism enables extensible, flexible code
- [ ] JS anchor: duck typing is idiomatic in both; no type enforcement by default

### 5. Abstraction
- [ ] Hiding complexity, exposing only what the caller needs
- [ ] Abstract classes as a contract: `ABC` + `@abstractmethod`
- [ ] Why enforced interfaces matter — what breaks without them
- [ ] Practical exercise: define an abstract class, implement two concrete versions
- [ ] JS anchor: no native abstract classes; TypeScript `abstract` keyword is the equivalent

### 6. `@classmethod` and `@staticmethod`
- [ ] `@classmethod` — takes `cls`, primary use case is alternative constructors (`User.from_dict()`)
- [ ] `@staticmethod` — utility function grouped in a class, no `self` or `cls`
- [ ] When to just use a module-level function instead
- [ ] JS anchor: static methods exist natively (`static foo()`) — contrast with Python's explicit decorators

### 7. Key Dunder Methods
- [ ] `__str__` vs. `__repr__` — display vs. debug
- [ ] `__eq__` and `__hash__` — equality and hashability
- [ ] `__len__`, `__getitem__` — making objects behave like built-ins
- [ ] The concept: Python's data model — everything is protocol-based
- [ ] JS anchor: no direct equivalent; Symbol.iterator and valueOf are the closest analogs

### 8. `@dataclass`
- [ ] What it replaces: manual `__init__`, `__repr__`, `__eq__` boilerplate
- [ ] `field()` for default values and metadata
- [ ] `slots=True` (Python 3.10+) — what it does and when to care
- [ ] When to use `@dataclass` vs. a plain class vs. a named tuple
- [ ] No JS equivalent — context: this is Python's modern data container tool

### 9. Composition vs. Inheritance
- [ ] The most important OOP design judgment call
- [ ] "Has-a" vs. "is-a" — when composition wins
- [ ] The fragile base class problem — why deep inheritance hierarchies break down
- [ ] Refactor exercise: untangle an over-engineered hierarchy using composition
- [ ] JS anchor: mixins via `Object.assign` — Python's composition pattern vs. JS mixin pattern

### 10. OOP vs. Functional — When to Use Which
- [ ] Python is multi-paradigm — you are not required to use classes
- [ ] When classes are the right tool: stateful objects, modeling real-world entities, framework integration
- [ ] When functions are the right tool: stateless transformations, pipelines, scripts
- [ ] The anti-pattern: wrapping every function in a class because "that's OOP"
- [ ] Design exercise: given a problem, argue for OOP and for functional — then decide

---

## End-of-Section Capstone

OOP is concept + code — the capstone tests both. Two parts, both required.

### Part 1 — Coding Challenge (45 min)
Claude provides a fresh prompt that requires all four pillars in one design. Example: "Build a notification system in Python: an abstract base `Notifier` class, two concrete implementations (`EmailNotifier`, `SMSNotifier`), encapsulated channel config, a polymorphic `send()` method, and a `NotificationService` that composes (not inherits) one or more notifiers." John implements from scratch with no notes. Graded on: correctness, appropriate use of OOP (not forcing it where functions would be cleaner), and idiomatic Python style.

### Part 2 — Design Judgment (10-15 min verbal)
Claude presents two short scenarios. John must argue whether OOP or functional is the right tool for each, and why. One scenario where OOP is clearly right, one where it's clearly wrong. Reasoning matters more than the answer.

**Pass criteria:** Part 1 implements all four pillars correctly with clean Python, Part 2 judgment calls are correct with specific reasoning. Section closes when both pass. Log result in Session Log below.

**Capstone result:** NOT YET RUN

---

## Session Log

| Date | Topics Covered | Assessment | Notes |
|------|---------------|------------|-------|

---

## Weak Spots

_Updated as sessions progress._

---

## Notes

- Framework-specific OOP (Pydantic `BaseModel`, SQLAlchemy `DeclarativeBase`, LangChain `BaseTool`) is intentionally excluded. Those get covered in Section 4 once fundamentals are solid.
- `typing.Protocol` excluded from this section — intermediate/Python-specific. Will surface naturally in Section 4.
- Metaclasses excluded — recognition only when encountered, not a topic to practice here.
- JS comparisons are anchor points, not a parallel curriculum. Python-first throughout.
