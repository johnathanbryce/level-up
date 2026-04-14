## Scenario: A healthtech startup (12 engineers) is building a patient portal where:

- Patients book appointments and view medical records
- Doctors upload lab results (large PDFs + images)
- The system sends SMS reminders 24 hours before each appointment
- They expect ~5,000 daily active users at launch, growing to maybe 50,000 in a year
- Medical data has strict compliance requirements — audit logs for every access

**Question:** What's your architecture? Monolith, microservices, serverless, or some combination? Walk me through your reasoning — don't just name it, justify each piece.

**My Answer:**

I would start with a monolith as we have only 12 engineers. We would focus on building out the core app logic and functionality as well as testing first, and if and when it comes time we could then make informed decisions on which services in our monolith should move to a microservice. Because we are unsure yet of our daily active users, it would be prudent to implement event driven architecture for sending SMS reminders to users 24 hrs before an appointment as this feature only needs to "know" about when patients book appointments and does not care about lab results, viewing medical records, etc. For security, if possible, I would see if we could setup an on-prem server with a postgres database to store their records. Bonus points if we could implement a vector database using a local Ollama LLM to quickly find records based on user semantic input, but only if the on-prem option exists so the health tech company and users know their data is being stored on a local server controlled by the company and not on a Cloud server or having any of their medical data or inputs trained on an LLM via an API call to OpenAI or Anthropic. For booking appointments, this would be a direct request-response: patients need to know ASAP whether they have successfully booked an appointment, and the docters as users need to know when they've been booked in. For viewing medical records, once again a robust conversation has to be made surrounding best practices for security - a lot of research needs to be done here as I am unsure if it would be allowed to host these records in a Cloud DNS. Once again, having an on-prem server would be the answer here, but only if this is possible.

With 5000 - 50,000K daily active users, that is a huge delta. We need to ensure our system can handle peak users during peak hours. 5000 daily active users is no problem, but 50,000 could become an issue. To start, a single server vertically scaled would be fine, but we would need to be ready to horizontally scale servers at a moments notice. Our postgres database should have no problem holding all of the user details, so we would only need to horizontally scale this if necessary and I doubt we would need to worry about having more than one database. Inactive users ever ~2 years could be cleaned from our database.

---

**Model Answer:**

**Core architecture: Modular monolith.** 12 engineers, early-stage product, requirements still evolving. Microservices would eat the team alive in operational overhead. Build one deployable unit with clean internal module boundaries (auth, appointments, records, notifications) so extraction is easy later if needed.

**Synchronous (request-response):**
- Appointment booking — patient needs immediate confirmation, doctor's calendar must update atomically. Strong consistency required.
- Viewing medical records — direct DB read, return the data. Every access writes an audit log entry (compliance requirement). Audit logging happens synchronously inside the request — you cannot afford to lose an audit record, so don't make it async and hope the queue delivers.

**Event-driven (async):**
- SMS reminders — a scheduled job or consumer listens for "appointment_created" events, queues an SMS to fire 24 hours before the appointment time. Decoupled from the booking flow entirely.
- File uploads — doctor uploads a PDF/image, the monolith saves the raw file to object storage (S3 or equivalent), writes a DB record marking it as "processing," and publishes a "file_uploaded" event. Consumers handle the heavy work asynchronously: thumbnail generation, virus scanning, OCR if needed. The doctor sees "upload received, processing..." immediately rather than waiting 30 seconds for all that to finish. This is the strongest candidate for eventual extraction into its own service if processing volume grows.

**Scaling:**
- 5,000–50,000 DAU is modest. A single vertically-scaled server handles this comfortably. Postgres on one machine with proper indexing is fine for this data volume for years.
- If/when the API tier needs horizontal scaling, the monolith is stateless (sessions in Redis or JWTs), so you put a load balancer in front and run multiple instances. The database stays vertical as long as possible.

**Compliance:**
- Audit log table records every medical record access (who, what, when, from where). This is non-negotiable in healthtech and often has legal retention requirements of 7-10+ years — no purging user data on a 2-year cycle.
- File storage in object storage with encryption at rest. Access controlled at the application layer with audit trails.

**What I would NOT do:**
- Microservices — 12 engineers, no proven scale pressure, no clear service boundaries yet.
- Serverless for the main API — steady predictable usage, compliance requirements make vendor lock-in risky.
- On-prem unless a specific regulation demands it — HIPAA-compliant cloud hosting (AWS GovCloud, etc.) is standard in healthtech and far easier to manage than on-prem for a startup.
