## Scenario: A healthtech startup (12 engineers) is building a patient portal where:

- Patients book appointments and view medical records
- Doctors upload lab results (large PDFs + images)
- The system sends SMS reminders 24 hours before each appointment
- They expect ~5,000 daily active users at launch, growing to maybe 50,000 in a year
- Medical data has strict compliance requirements — audit logs for every access

**Question:** What's your architecture? Monolith, microservices, serverless, or some combination? Walk me through your reasoning — don't just name it, justify each piece.