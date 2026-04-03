# DevOps Essentials — Progression Tracker

## Overview

Practical DevOps for a web/AI engineer. Not aiming for DevOps engineer depth — aiming for confident containerization, CI/CD pipeline creation, and understanding deployment strategies well enough to implement them and discuss them in interviews.

## Definition of Done

Can Dockerize any project, write a Docker Compose file for multi-service local development from memory, build a CI/CD pipeline with GitHub Actions, and explain deployment strategies (blue-green, rolling, canary) with trade-offs.

---

## Sub-Topics

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
- [ ] Build a complete pipeline for the backend project
- [ ] Branch protection and required checks (conceptual)

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

## Session Log

| Date | Topics Covered | Assessment | Next Focus |
|------|---------------|------------|------------|
| — | — | — | — |

---

## Notes & Weak Spots

- (none yet)
