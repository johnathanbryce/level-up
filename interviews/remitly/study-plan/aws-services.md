# AWS Services — Vocabulary Pass

Recruiter context only. Goal: name common services by family and have a one-liner for each. **Do not try to learn AWS deeply in 2 days.**

---

## Why this matters at Remitly

All three target roles are on AWS. Roles 2 (CDP) and 3 (WARP) name AWS explicitly. You need to *recognize* service names if the recruiter drops them — not architect with them.

---

## Service families (the only ones worth knowing for a recruiter chat)

### Compute

- **EC2** — Elastic Compute Cloud. Virtual machines. The original AWS service. Long-running servers.
- **ECS** — Elastic Container Service. Run Docker containers without managing the orchestration layer yourself.
- **EKS** — Elastic Kubernetes Service. Managed Kubernetes. For teams that want K8s without running the control plane.
- **Lambda** — serverless functions. You write a function, AWS runs it on demand. No servers. Pay per invocation.
- **Fargate** — serverless containers. Underneath ECS or EKS. You don't manage the underlying VMs.

### Storage

- **S3** — Simple Storage Service. Object storage. The internet's hard drive. Files, images, backups, logs.
- **EBS** — Elastic Block Store. Disks attached to EC2 instances.
- **RDS** — Relational Database Service. Managed Postgres / MySQL / etc.
- **DynamoDB** — managed NoSQL. (See [dynamodb-nosql.md](dynamodb-nosql.md).)
- **ElastiCache** — managed Redis / Memcached.

### Messaging

- **SQS** — Simple Queue Service. Distributed message queue. Decouple producers from consumers.
- **SNS** — Simple Notification Service. Pub/sub. One message, many subscribers.
- **Kinesis** — managed stream processing. AWS's answer to Kafka. Ordered, partitioned, replay-able. (See [message-brokers.md](message-brokers.md).)
- **EventBridge** — event bus. Route events between AWS services.

### Networking

- **VPC** — Virtual Private Cloud. Your isolated network within AWS.
- **ALB / NLB** — Application / Network Load Balancer. Layer 7 (HTTP-aware) vs Layer 4 (TCP/UDP).
- **CloudFront** — CDN.
- **Route 53** — managed DNS.
- **API Gateway** — managed API frontend. Often pairs with Lambda for serverless APIs.

### Identity / Security

- **IAM** — Identity and Access Management. Who can do what to which resource. Everything in AWS flows through IAM.
- **KMS** — Key Management Service. Managed encryption keys.
- **Secrets Manager** — managed secret storage with rotation.

### Observability

- **CloudWatch** — logs + metrics + alarms. The default observability layer.
- **X-Ray** — distributed tracing.

---

## Likely recruiter prompts + canonical answers

- **"How comfortable are you with AWS?"** → "Surface familiarity — I can name the common services across compute, storage, messaging. I haven't been the primary person designing AWS infrastructure, but I'd be comfortable working alongside someone who is and ramping up."
- **"What AWS services have you used?"** → *Honest answer.* Probably some combination of S3, Lambda, CloudWatch. Don't fabricate.
- **"How does the team you'd join here use AWS?"** → *Flip it into a curiosity question.* "Honestly that's something I'd love to learn more about — what services the team leans on most, and where the architectural choices have been made deliberately vs. inherited."

---

## Gotchas to NOT walk into

- **EC2 ≠ ECS ≠ EKS.** Three completely different services. EC2 = VMs, ECS = containers, EKS = Kubernetes.
- **S3 is object storage, not a filesystem.** You don't open files on S3; you `GET` and `PUT` whole objects (or byte ranges).
- **DynamoDB is NoSQL, RDS is SQL.** Different products entirely.
- **Lambda has cold starts.** First invocation after idle period can be slow. Trade-off for paying-per-invocation.
