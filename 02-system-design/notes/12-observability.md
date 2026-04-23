# Observability

> **Review priority: LOW (Tier 3).** Just the buzzwords. One 50-second paragraph covers everything.

## The Three Pillars

| Pillar | What it answers |
| --- | --- |
| **Logs** | What happened (discrete events) |
| **Metrics** | What the system is doing now (aggregates, trends) |
| **Traces** | Where a request went and how long each hop took |

## Must-Know Buzzwords

### Logs

- **Structured JSON logs** — queryable by field in an aggregation platform (Datadog, Splunk, ELK, CloudWatch, Grafana Loki)
- **Log levels:** DEBUG / INFO / WARN / ERROR / FATAL — filter signal from noise; DEBUG off in prod
- **Correlation IDs** (`X-Request-ID`) — threaded through every service so one request's logs can be reassembled across services. THE #1 logging pattern for distributed systems.

### Metrics

- **Four Golden Signals** (Google SRE): **Latency**, **Traffic**, **Errors**, **Saturation**
- **Percentiles, not averages.** Always cite **p50, p95, p99** — averages hide tail pain.
- Tools: **Prometheus + Grafana**, **Datadog**, **CloudWatch**

### Tracing

- **Distributed tracing** via **OpenTelemetry (OTel)** — traces contain nested spans showing per-hop timing across services
- Only needed for 4+ service hops. Monoliths don't need it.

### Alerting

- Fire on threshold breach (error rate > 1%, p99 > SLA). Routed via **PagerDuty** to on-call.

## THE Interview Paragraph (memorize verbatim)

> "For observability we'd track the **three pillars**: **structured JSON logs** with **correlation IDs** for cross-service debugging, **metrics** via Prometheus or Datadog — the **Four Golden Signals** (latency, traffic, errors, saturation), and we monitor latency as **p50/p95/p99** percentiles, not averages. For complex request paths we'd add **distributed tracing** via OpenTelemetry to see per-hop timing. **Alerts** fire on threshold breach (error rate > 1%, p99 > SLA) routed through PagerDuty to on-call."
