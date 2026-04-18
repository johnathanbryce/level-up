# Architectural Patterns

## Monolith

- A **monolith** is a single deployable unit. All your features (auth, project management, notifications, billing, etc) live in one codebase and as one process
  - One server, one deploy, one database
- It's usually the right call for early-stage production
  - easier to debug
  - shared memory and function calls instead of HTTP requests between components
  - easier to refactor
- Where it breaks down:
  - a single slow feature (e.g. a massive report job) can degrade the whole app - **there is no isolation**
  - scaling meanings scaling _everything_, even the parts that don't need it
  - as the team grows past ~15-20 engineers, everyone stepping on each others toes
  - deployment is all-or-nothing - one bad line of code takes everything down

## Microservices

- Opposite of a monolith, instead of one deployable unit, you split your system into **small, independently deployable services**, each owning a specific piece of functionality
  - Each service has its own codebase, its own deployment pipeline, and often its own database

Ex: Trello clone: auth service, board service, notification service, billing service - each running separately communicating over HTTP or message queues

- **What problems they solve:**
  - **Fault isolation**
  - **Independent scaling** - your boards service gets 100x more traffic than billing? Scale just the boards service
  - **Independent deployment** -- team A ships boards without waiting for team B to finish billing changes
  - **Team autonomy** -- each team owns a service end-to-end
- **What problems they create:**
  - **Network complexity** -- function calls become HTTP requests (they can fail, time out, arrive out of order). You now need retries, timeouts, etc. for things that used to be a function call
  - **Data consistency** -- each service has its own database. Super hard to keep data in sync across services
  - **Operational overhead** -- instead of one deploy pipeline, you have 5,10,20. Each needs monitoring, logging, alerting.
  - **Debugging difficulty** -- a bug that spans two services means reading logs from two places

## Monolith vs. Microservices - The Decision Framework

- It's not a "which is better" debate, its a "when does each make sense" question
- **Start with a monolith when:**
  - small team (>10-15 engineers)
  - early-stage product where requirements are still shifting
  - don't yet know where the service boundaries should be
- **Move to microservices when:**
  - team size makes coordination in one codebase painful
  - you have a specific service that needs independent scaling (e.g. your image processing burns 10x more CPU than everything else)
  - you have clear, stable domain boundaries
  - you can afford the operational overhead (dedicated DevOps, monitors, CI/CD per service)

- The real-world path is **monolith -> modular monolith -> extract services one at a time when needed**
- So, build a well-structured monolith, and extract services when you have evidence you need them

## Serverless

- Serverless doesn't mean "no servers", it means **you don't manage the servers**. The cloud provider runs your code in response to events, handles scaling automatically, and charges you per execution
- The most common form is **Faas (Functions as a Service)** - AWS Lambda, Google Cloud Functions, Vercel serverless functions
  - You write a function, deploy it, and the provider runs it when triggered (HTTP request, file upload, cron schedule, queue message)

- **What you get:**
  - **Zero server management**
  - **Auto-scaling to zero** -- if nobody calls your function, you pay nothing. if 10,000 people call it at once, it scales automatically
  - **Pay-per-execution** -- great for bursty or unpredictable traffic
- **What it costs you:**
  - Vendor lock-in
  - Cold starts
  - Debugging difficulty
  - Execution limits
  - Costs at scale

## Event-Driven Architecture

- So far, every pattern we've covered assumes **synchronous communication** -- service A calls service B and waits for a response
- Event driven architecture flips this: **service A announces that something has happened, and anyone who cares can react to it**
- The core concept is **pub/sub (publish/subscribe)**
  - A **producer** publishes an event ("user signed up")
  - A **message broker** holds the event (Kafka, AWS SNS/SQS)
  - One or more **consumers** subscribe to events they care about and process them independently

Back to Trello example, a user creates a new board. In a synch monolith, your code might do:

1. Save board to DB
2. Send welcome email
3. Update analytics
4. Notify team members
5. Return response to user

The user waits for ALL of that. In an event-driven approach:

1. Save board to DB
2. Publish event: "board_created"
3. Return response to user

- Asynchronously:
  - email service hears "board_created" -> sends welcome email
  - analytics service hears "board_created" -> logs it
  - notification service hears "board_created" -> pings team members

**What you get:** 
  - **Decoupling** -- board service doesn't know or care that emails exist 
  - **Responsiveness** -- the user gets an immediate response, heavy work happens in the background 
  - **Resilience** -- if email service is down, the board still gets created

**What it costs you:** 
  - **Debugging complexity** 
  - **Message ordering** -- events can arrive out of order. If "board_deleted" arrives before "board_created" in a consumer, you have a problem 
  - **Infrastructure overhead** -- you need a message broker (Kafka, SQS, etc.), that's another system to run, monitor, and understand

**When it makes sense:** - Multiple systems need to react to the same event - You need to decouple heavy background work from user-facing responses - Resilience matters - you'd rather queue work than drop it when a service is down

- **When it doesn't:**
  - Simple request/response flows where the user needs the result immediately
  - Small systems
