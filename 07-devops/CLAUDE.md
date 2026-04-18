# DevOps Essentials — Progression Tracker

## Overview

Practical DevOps for a web/AI engineer. Not aiming for DevOps engineer depth — aiming for confident containerization, CI/CD pipeline creation, and understanding deployment strategies well enough to implement them and discuss them in interviews.

## Definition of Done

Can Dockerize any project, write a Docker Compose file for multi-service local development from memory, build a CI/CD pipeline with GitHub Actions, and explain deployment strategies (blue-green, rolling, canary) with trade-offs.

---

## Sub-Topics

### Shell Scripting Basics

You'll be reading and writing shell commands in Dockerfiles, CI/CD pipelines, and debugging containers. This isn't "become a bash wizard" — it's "stop being confused by the glue that holds DevOps together."

- [ ] Variables, quoting, and string interpolation (`$VAR`, `"$VAR"`, `'$VAR'` — know the difference)
- [ ] Conditionals: `if/then/else/fi`, test operators (`-f`, `-d`, `-z`, `-n`, `-eq`), `[[ ]]` vs `[ ]`
- [ ] Loops: `for`, `while`, iterating over files and command output
- [ ] Exit codes: `$?`, `set -e` (exit on error), `set -o pipefail`
- [ ] Piping and redirection: `|`, `>`, `>>`, `2>&1`, `/dev/null`
- [ ] Essential commands: `grep` (search), `awk` (extract columns), `sed` (find/replace), `xargs` (pipe to args), `find` (locate files)
- [ ] Reading and writing scripts that appear in Dockerfiles (chained `RUN` commands) and GitHub Actions (multi-line `run:` blocks)
- [ ] Environment variables: `export`, `.env` files, `source`, how they propagate to child processes

#### Shell Scripting Challenges

- [ ] Write a script that checks if a required environment variable is set, exits with an error if not
- [ ] Write a script that finds all `.log` files older than 7 days and deletes them
- [ ] Read and explain a real-world Dockerfile `RUN` block with chained commands (`apt-get update && apt-get install -y ... && rm -rf /var/lib/apt/lists/*`)
- [ ] Write a health-check script that curls an endpoint and exits 0/1 based on response code

### Docker: How It Works (conceptual — understand before building)

- [ ] What Docker actually is — OS-level virtualization, not a VM. Containers share the host kernel.
- [ ] Containers are stateless and ephemeral — when a container stops, everything inside it is gone. Why this matters.
- [ ] Images vs containers — an image is a blueprint, a container is a running instance. You can run many containers from one image.
- [ ] Layers and the union filesystem — each Dockerfile instruction creates a layer, layers are cached and shared. Why order matters for build speed.
- [ ] The container lifecycle: create → start → run → stop → remove. What persists and what doesn't at each stage.
- [ ] Docker vs VMs — when to use each, resource overhead differences

### Docker: Data Persistence

- [ ] Why data disappears when containers stop (stateless by design)
- [ ] Volumes: Docker-managed persistent storage. Data survives container restarts and removals.
- [ ] Bind mounts: map a host directory into the container. Used for local development (live code reloading).
- [ ] Volumes vs bind mounts — when to use each (volumes for data, bind mounts for development)
- [ ] tmpfs mounts — in-memory storage that never touches disk (for sensitive data)
- [ ] Named volumes vs anonymous volumes

### Docker: Networking

- [ ] Bridge networks: default container networking, container-to-container communication
- [ ] How containers find each other (DNS by container name within a network)
- [ ] Port mapping: exposing container ports to the host (`-p 8080:80`)
- [ ] Network isolation: why containers on different networks can't talk to each other by default

### Docker: Building Images

- [ ] Writing a Dockerfile: FROM, COPY, RUN, CMD, EXPOSE, ENV, WORKDIR, ARG
- [ ] CMD vs ENTRYPOINT — what each does and when to use which
- [ ] Multi-stage builds: reducing image size by separating build and runtime
- [ ] .dockerignore: what to exclude and why (node_modules, .git, .env)
- [ ] Image tagging and versioning strategies
- [ ] Base image selection: why alpine vs slim vs full matters (size, security, compatibility)
- [ ] Container security basics: run as non-root user (USER directive), don't use `latest` tag in production (pin versions), scan images for vulnerabilities (conceptual — know it exists, not tool-specific)
- [ ] Principle of least privilege in containers: only install what you need, minimize attack surface, don't run as root

### Docker Compose

- [ ] What Compose solves (multi-service local development)
- [ ] docker-compose.yml structure: services, networks, volumes
- [ ] Service dependencies (depends_on, healthchecks)
- [ ] Environment variables and .env files
- [ ] Compose a multi-service setup: API + Postgres + Redis (using backend project)
- [ ] Common Compose commands: up, down, build, logs, exec
- [ ] Compose profiles for different environments (dev vs test)

### CI/CD

- [ ] What CI/CD is and why it matters (automated quality gates)
- [ ] GitHub Actions: workflow files, triggers, jobs, steps
- [ ] Build stage: install dependencies, compile/build
- [ ] Test stage: run unit tests, integration tests
- [ ] Deploy stage: push Docker image, deploy to environment (simulated)
- [ ] Secrets management in CI/CD (GitHub Secrets)
- [ ] Secrets management concepts: why secrets in code/images/env vars are dangerous, awareness of tools (HashiCorp Vault, AWS Secrets Manager, Doppler), the pattern of "never commit secrets, inject at runtime"
- [ ] Common secrets anti-patterns: hardcoded API keys, secrets in Docker images, `.env` files committed to git
- [ ] Build a complete pipeline for the backend project
- [ ] Branch protection and required checks (conceptual)

### Monitoring & Logging in Containers

Light coverage — ties into Observability in System Design (Section 2). Focus is on what it looks like in a containerized setup, not tool mastery.

- [ ] Structured logging in containers: why JSON logs matter, how `docker logs` works, the problem with logging to files inside containers
- [ ] Log aggregation concepts: how logs get from containers to a centralized system (stdout → log driver → aggregator), awareness of ELK/Loki/CloudWatch (know they exist, not how to configure them)
- [ ] Basic health monitoring: Docker healthchecks, liveness vs readiness (conceptual — what they check and why), knowing what metrics matter (CPU, memory, restart count, response time)

### Deployment Strategies

- [ ] Blue-green deployment: what it is, trade-offs, rollback strategy
- [ ] Rolling deployment: gradual replacement, how it handles failures
- [ ] Canary deployment: partial rollout, traffic splitting, monitoring
- [ ] Feature flags: decoupling deployment from release
- [ ] Rollback strategies: when and how to roll back safely
- [ ] Environment separation: dev → staging → production pipeline

---

## Hands-On Exercises

- [ ] Dockerize the FastAPI project from Section 4
- [ ] Dockerize the Express project from Section 4
- [ ] Write a docker-compose.yml: API + Postgres + Redis
- [ ] Write a GitHub Actions workflow: lint → test → build → (simulated) deploy
- [ ] Practice: tear down and rebuild the Compose setup from memory

---

## End-of-Section Capstone

DevOps is hands-on. The real test is: can you do it from scratch with no references?

### Part 1 — From-Scratch Build (60-90 min)
Claude provides a simple, fresh Python app (not one of the section projects). John must write three files from scratch with no looking at previous work:
1. **Dockerfile** — correct base image, layering order for cache efficiency, non-root user, .dockerignore
2. **docker-compose.yml** — the app + Postgres + Redis, correct networking, volumes, env vars, healthcheck
3. **GitHub Actions workflow** — install → test → build Docker image → push to registry (simulated)

All three must be functional. Claude reviews for correctness and best practices (security, layer caching, secret handling).

### Part 2 — Deployment Strategy Defense (10-15 min verbal)
Claude presents a scenario: "You're deploying a breaking API change to a service with 50K daily active users. You can't take downtime. Walk me through which deployment strategy you'd choose, why, and exactly how you'd roll back if the new version starts throwing 500s." John answers cold — no notes.

**Pass criteria:** All three files are functional and follow best practices (no root, no `latest` in production, no secrets in the image), deployment strategy answer covers the correct trade-offs and rollback mechanism. Section closes when both pass. Log result in Session Log below.

**Capstone result:** NOT YET RUN

---

## Session Log

| Date | Topics Covered | Assessment | Next Focus |
|------|---------------|------------|------------|
| — | — | — | — |

---

## Notes & Weak Spots

- (none yet)
