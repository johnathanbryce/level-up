# DevOps Essentials — Progression Tracker

## Overview

Practical DevOps for a web/AI engineer. Not aiming for DevOps engineer depth — aiming for confident containerization, CI/CD pipeline creation, and understanding deployment strategies well enough to implement them and discuss them in interviews.

## Definition of Done

Can Dockerize any project, write a Docker Compose file for multi-service local development from memory, build a CI/CD pipeline with GitHub Actions, and explain deployment strategies (blue-green, rolling, canary) with trade-offs.

---

## Sub-Topics

### Docker Fundamentals

- [ ] What Docker is and why it matters (reproducible environments, isolation)
- [ ] Images vs containers — the mental model
- [ ] Layers and caching: how Docker builds images, why order in Dockerfile matters
- [ ] Writing a Dockerfile: FROM, COPY, RUN, CMD, EXPOSE, ENV
- [ ] Multi-stage builds: reducing image size
- [ ] .dockerignore: what to exclude and why
- [ ] Docker networking: bridge networks, container-to-container communication
- [ ] Docker volumes: persisting data, bind mounts vs named volumes

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
