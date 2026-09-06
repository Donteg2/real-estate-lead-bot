# REAL ESTATE LEAD BOT

## n8n Workflows Specification

**Project:** Real Estate Lead Bot  
**Client:** PrimeHomes Realty  
**Document:** n8n Workflows Specification  
**Version:** 0.1  
**Status:** Draft  
**Last Updated:** 2026-09-05  
**Automation Platform:** n8n  
**Backend:** FastAPI  
**Frontend:** React  
**AI:** LLM Provider  
**Database:** SQL Database  
**Operational Layer:** Google Sheets  

---

# 1. Purpose

This document defines the automation workflows used by the Real Estate Lead Bot.

n8n acts as the **workflow orchestration and integration layer** connecting:

- FastAPI
- AI services
- SQL database
- Google Sheets
- Notification services
- Sales operations
- Follow-up processes

The purpose of n8n is to coordinate multi-step processes reliably without placing all application logic inside the frontend, backend, or AI model.

---

# 2. n8n's Role

The system follows:

```text
React
  ↓
FastAPI
  ↓
n8n
  ↓
AI / Database / Notifications / Integrations
```

n8n is responsible for:

- Workflow orchestration
- AI invocation
- Data transformation
- External integrations
- Notifications
- Lead routing
- Follow-up automation
- Google Sheets synchronization
- Workflow-level error handling

---

# 3. What n8n Should NOT Own

n8n should not become the entire backend application.

Critical application responsibilities remain outside n8n.

| Responsibility | Owner |
|---|---|
| Frontend presentation | React |
| API contract | FastAPI |
| Authentication | FastAPI |
| Authorization | FastAPI |
| Core business rules | Backend/domain |
| Lead scoring rules | Backend/domain |
| Database source of truth | SQL |
| Natural-language understanding | AI |
| Workflow orchestration | n8n |
| External integrations | n8n |

---

# 4. Workflow Architecture

The overall automation architecture is:

```text
                    CUSTOMER
                       │
                       ↓
                    REACT
                       │
                       ↓
                    FASTAPI
                       │
                       ↓
                      n8n
                       │
        ┌──────────────┼───────────────┐
        ↓              ↓               ↓
       AI             SQL          Notifications
        │              │               │
        └──────────────┼───────────────┘
                       ↓
                 SALES TEAM
                       │
                       ↓
                   FOLLOW-UP
```

---

# 5. Core Workflows

The MVP should contain the following workflows:

```text
WF-001 Lead Enquiry Processing
WF-002 Lead Creation / Update
WF-003 Lead Qualification
WF-004 Sales Notification
WF-005 Customer Response
WF-006 Follow-up Management
WF-007 Google Sheets Synchronization
WF-008 Error Handling
WF-009 Scheduled Follow-up Processing
WF-010 Workflow Monitoring
```

---

# 6. Workflow Naming Convention

n8n workflows should follow a consistent naming convention.

Recommended:

```text
REAL-ESTATE | WF-001 | Lead Enquiry Processing
REAL-ESTATE | WF-002 | Lead Creation Update
REAL-ESTATE | WF-003 | Lead Qualification
```

This makes workflows easier to identify as the project grows.

---

# 7. WF-001 — Lead Enquiry Processing

This is the primary workflow.

It processes a customer's message from the application.

## Trigger

FastAPI sends a request to an n8n webhook.

```text
POST
/webhook/real-estate/chat
```

---

## Input

Example:

```json
{
  "message_id": "msg-123",
  "conversation_id": "conv-456",
  "customer_id": null,
  "message": "I need a 3-bedroom apartment around Lekki. My budget is ₦80 million."
}
```

---

## Workflow

```text
Webhook
   ↓
Validate Input
   ↓
Get Conversation
   ↓
Get Existing Lead
   ↓
Prepare AI Context
   ↓
AI Extraction
   ↓
Validate AI Output
   ↓
Update/Create Lead
   ↓
Run Qualification
   ↓
Generate Customer Response
   ↓
Save Message
   ↓
Notify Sales if Required
   ↓
Return Response
```

---

# 8. WF-001 — Validate Input

The workflow should validate basic information before AI processing.

Required:

```text
message
```

Optional:

```text
message_id
conversation_id
customer_id
```

Invalid input should stop processing.

Example:

```json
{
  "error": "INVALID_INPUT",
  "message": "Message is required."
}
```

---

# 9. WF-001 — Conversation Retrieval

If a conversation ID exists:

```text
conversation_id
```

n8n retrieves the relevant conversation context.

This may include:

```text
Conversation
├── Previous messages
├── Existing customer
├── Existing lead
└── Known requirements
```

---

# 10. WF-001 — AI Context Preparation

Before calling the AI model, n8n prepares the context.

Example:

```text
System Instructions
+
Business Rules
+
Existing Lead
+
Conversation Summary
+
Recent Messages
+
Current Message
```

Only relevant information should be passed to the model.

---

# 11. WF-001 — AI Extraction

The AI receives the prepared context.

Example customer message:

```text
I need a 3-bedroom apartment around Lekki.
My budget is ₦80 million.
```

Expected structured result:

```json
{
  "intent": "BUY_PROPERTY",
  "transaction_type": "BUY",
  "property_type": "APARTMENT",
  "bedrooms": 3,
  "location": "Lekki",
  "budget_max": 80000000,
  "currency": "NGN",
  "timeline": "UNKNOWN"
}
```

---

# 12. WF-001 — Validate AI Output

AI output must not be trusted blindly.

Flow:

```text
AI Output
   ↓
Parse JSON
   ↓
Schema Validation
   ↓
Business Validation
   ↓
Accepted Data
```

Invalid AI output:

```text
AI
 ↓
Invalid JSON
 ↓
Retry
 ↓
Still Invalid
 ↓
Error/Fallback
```

---

# 13. WF-002 — Lead Creation / Update

The system should determine whether a lead already exists.

```text
Existing conversation
        ↓
Existing lead?
   ┌────┴────┐
   │         │
  YES       NO
   │         │
Update     Create
   │         │
   └────┬────┘
        ↓
      Lead
```

Lead records should be stored in SQL.

---

# 14. Lead Matching

The system should use reliable identifiers when available.

Preferred matching:

```text
lead_id
conversation_id
customer_id
```

The system should avoid creating duplicate leads for every customer message.

---

# 15. WF-003 — Lead Qualification

Once structured lead information has been validated, qualification can occur.

Flow:

```text
Validated Lead Data
        ↓
Qualification Service
        ↓
Calculate Score
        ↓
Determine Priority
        ↓
Update Lead
```

Example:

```text
Score: 82
Priority: HOT
```

The scoring rules should be deterministic.

n8n may call the backend qualification service rather than implementing complex scoring logic itself.

---

# 16. Lead Qualification Inputs

Potential scoring inputs:

```text
Intent strength
Budget
Timeline
Requirement completeness
Location specificity
Customer engagement
```

The final score belongs to the backend/domain rules.

---

# 17. WF-004 — Sales Notification

Hot or otherwise actionable leads should trigger a notification.

Example:

```text
Lead Qualification
        ↓
Priority = HOT
        ↓
Sales Notification
```

Possible channels:

- Email
- Slack
- Microsoft Teams
- WhatsApp
- SMS
- Internal notification system

The initial implementation may start with email.

---

# 18. Sales Notification Example

Example notification:

```text
NEW HOT LEAD

Customer: John Doe
Intent: Buy Property
Property: 3-bedroom apartment
Location: Lekki
Budget: ₦80,000,000
Timeline: Within 1 Month
Score: 82

Action:
Contact customer as soon as possible.
```

Internal qualification details should not automatically be exposed to the customer.

---

# 19. WF-005 — Customer Response

After processing the customer's message, the system generates a response.

Flow:

```text
Validated Lead Information
        ↓
Conversation Context
        ↓
AI Response Generation
        ↓
Response Validation
        ↓
Save Message
        ↓
Return Response
```

---

# 20. Response Generation Rules

The AI response should:

- Answer the customer's message
- Ask relevant missing questions
- Avoid unnecessary repetition
- Remain professional
- Avoid unsupported claims
- Avoid exposing internal lead scores
- Avoid claiming property availability without verification

---

# 21. Customer Response Example

Customer:

```text
I want to buy a 3-bedroom apartment in Lekki.
```

Bot:

```text
Great! What's your approximate budget, and when are you
looking to make the purchase?
```

---

# 22. WF-006 — Follow-up Management

Sales follow-ups should be stored and managed through the application.

Example:

```text
Lead
 ↓
Follow-up created
 ↓
scheduled_at
 ↓
n8n scheduled workflow
 ↓
Check due follow-ups
 ↓
Notify sales agent
```

---

# 23. Follow-up Types

Initial supported types:

```text
CALL
EMAIL
MESSAGE
MEETING
OTHER
```

---

# 24. WF-009 — Scheduled Follow-up Processing

This workflow runs on a schedule.

Example:

```text
Schedule Trigger
       ↓
Find Due Follow-ups
       ↓
Check Status
       ↓
Check Assigned Agent
       ↓
Send Reminder
       ↓
Record Notification
```

The exact schedule should be configured during deployment.

---

# 25. Follow-up Reminder

Example:

```text
FOLLOW-UP REMINDER

Customer: John Doe
Lead: LEAD-123
Type: CALL
Scheduled: 10:00 AM

Notes:
Confirm preferred property options.
```

---

# 26. WF-007 — Google Sheets Synchronization

Google Sheets is an operational layer.

It should not replace SQL as the source of truth.

Architecture:

```text
SQL DATABASE
     │
     ↓
   n8n
     │
     ↓
GOOGLE SHEETS
```

---

# 27. Google Sheets Purpose

Sheets may be used for:

- Simple sales visibility
- Operational reporting
- Manual review
- Quick exports
- Non-technical staff access

It should not be responsible for:

- Primary lead identity
- Complex relationships
- Transaction integrity
- Authentication
- Critical business logic

---

# 28. Sheet Structure

A possible lead sheet:

| Lead ID | Customer | Intent | Property | Location | Budget | Timeline | Score | Priority | Status | Agent |
|---|---|---|---|---|---:|---|---:|---|---|---|

SQL remains authoritative.

---

# 29. Sheet Sync Strategy

Recommended flow:

```text
Database Change
      ↓
n8n
      ↓
Transform Data
      ↓
Google Sheets
```

If synchronization fails:

```text
SQL Update
   ↓
Successful
   ↓
Sheet Sync Failed
   ↓
Log Error
   ↓
Retry
```

A failed Google Sheets update should not cause the authoritative SQL transaction to become invalid.

---

# 30. WF-008 — Error Handling

Every important workflow should have error handling.

General structure:

```text
Workflow
   ↓
Node Failure
   ↓
Error Handler
   ↓
Log Error
   ↓
Determine Retryable?
   ├── YES → Retry
   └── NO  → Record Failure
                  ↓
              Notify Admin
```

---

# 31. Retryable Errors

Examples:

```text
Temporary AI provider failure
Temporary network failure
Temporary notification failure
Rate limit
Temporary database connectivity issue
```

These may be retried according to controlled retry policies.

---

# 32. Non-Retryable Errors

Examples:

```text
Invalid input
Invalid business data
Authentication failure
Invalid schema
Unsupported operation
Missing required configuration
```

These should normally fail clearly rather than retry indefinitely.

---

# 33. Error Workflow

The error workflow should capture:

```text
workflow_name
execution_id
request_id
conversation_id
lead_id
node_name
error_type
error_message
timestamp
retry_count
```

Sensitive information should not be unnecessarily included in logs.

---

# 34. Idempotency

Workflows must avoid duplicate processing.

Example:

```text
message_id = msg-123
```

If the same request is received twice:

```text
msg-123
   ↓
Already processed?
   ↓
YES
   ↓
Do not create duplicate message/lead
```

This is especially important when retries or webhook delivery issues occur.

---

# 35. Webhook Security

n8n webhooks must not be treated as publicly trusted endpoints.

Possible protections include:

- Authentication
- Signed requests
- Secret webhook tokens
- IP restrictions where appropriate
- Request validation
- Rate limiting at the application layer

FastAPI should control access to internal n8n operations.

---

# 36. Credentials Management

n8n credentials must be stored using n8n's credential system or secure secret management.

Credentials must not be:

```text
Hard-coded in workflows
Committed to Git
Sent to React
Returned through API responses
Stored in customer messages
```

---

# 37. Workflow Variables

Workflows should use consistent field names.

Example:

```text
request_id
message_id
conversation_id
customer_id
lead_id
sales_agent_id
```

Data should not be renamed unnecessarily between nodes.

---

# 38. Data Transformation

n8n Code nodes should only be used when they provide clear value.

Good uses:

```text
Custom calculations
Data normalization
Validation
Transformation
Formatting
Small business-specific processing
```

Avoid putting the entire application inside Code nodes.

---

# 39. AI Workflow Boundary

The AI workflow should follow:

```text
Input
 ↓
Context
 ↓
AI
 ↓
Structured Output
 ↓
Validation
 ↓
Backend Decision
```

Not:

```text
Customer
 ↓
AI
 ↓
AI decides everything
 ↓
Database
```

---

# 40. Database Operations

n8n may interact with the SQL database when appropriate.

Operations may include:

```text
Create customer
Create conversation
Create message
Create/update lead
Read lead
Read conversation
Create follow-up
Update follow-up
```

Critical database operations should follow the application's defined API and data contracts.

---

# 41. Recommended Database Boundary

Where possible:

```text
React
 ↓
FastAPI
 ↓
Application Services
 ↓
SQL
```

For workflow-specific operations:

```text
FastAPI
 ↓
n8n
 ↓
Integration / automation
```

The architecture should avoid uncontrolled direct database writes from many unrelated workflows.

---

# 42. Workflow Communication

Each workflow should have a clear input/output contract.

Example:

### Input

```json
{
  "conversation_id": "conv-123",
  "message_id": "msg-456",
  "message": "I need land around Ibadan."
}
```

### Output

```json
{
  "conversation_id": "conv-123",
  "message_id": "msg-789",
  "lead_id": "lead-123",
  "response": "Sure. What's your approximate budget?",
  "status": "NEW",
  "priority": "COLD"
}
```

---

# 43. Workflow Modularity

Workflows should remain modular.

Instead of one extremely large workflow:

```text
Webhook
 ↓
Everything
 ↓
Everything
 ↓
Everything
```

Prefer:

```text
Lead Processing
      ↓
Qualification
      ↓
Notification
      ↓
Follow-up
```

Each workflow should have a clear responsibility.

---

# 44. Workflow Dependencies

Example dependency map:

```text
WF-001 Lead Processing
        │
        ├── WF-002 Lead Create/Update
        │
        ├── WF-003 Qualification
        │
        └── WF-005 Customer Response
                 │
                 └── WF-004 Sales Notification
```

Scheduled processes:

```text
WF-009 Follow-up Processing
        ↓
WF-004 Sales Notification
```

---

# 45. Workflow Execution Tracking

Each important execution should be traceable using:

```text
request_id
execution_id
workflow_id
conversation_id
lead_id
```

This allows a developer to trace:

```text
Customer Message
       ↓
API Request
       ↓
n8n Execution
       ↓
AI Call
       ↓
Database Update
       ↓
Notification
```

---

# 46. Workflow Monitoring

The system should monitor:

- Successful executions
- Failed executions
- Execution duration
- AI failures
- Database failures
- Notification failures
- Retry counts
- Workflow volume

---

# 47. Alerts

Administrators should be alerted when critical workflows repeatedly fail.

Examples:

```text
Lead processing failure
Database connection failure
AI provider unavailable
Notification workflow failure
Repeated workflow errors
```

---

# 48. Development Workflow

During development:

```text
Build workflow
      ↓
Test manually
      ↓
Test with sample data
      ↓
Test error paths
      ↓
Connect to FastAPI
      ↓
Integration test
      ↓
Production configuration
```

---

# 49. Test Customer Messages

The workflows should be tested with:

### Example 1

```text
Hi, I'm looking for a 3-bedroom apartment around Lekki.
My budget is around ₦80 million.
```

### Example 2

```text
Do you have any 2-bedroom apartments in Ikeja?
```

### Example 3

```text
I need land around Ibadan, preferably below ₦20 million.
```

### Example 4

```text
Hello, I want to buy a house.
```

### Example 5

```text
I need something around Ikeja.
```

---

# 50. Expected Workflow Behavior

For a complete enquiry:

```text
Customer
 ↓
Message received
 ↓
AI extracts requirements
 ↓
Data validated
 ↓
Lead created/updated
 ↓
Qualification calculated
 ↓
Priority assigned
 ↓
SQL updated
 ↓
Sales notified if required
 ↓
Customer receives response
```

---

# 51. Workflow Failure Behavior

If AI fails:

```text
Customer
 ↓
FastAPI
 ↓
n8n
 ↓
AI failure
 ↓
Retry
 ↓
Fallback
 ↓
Customer receives safe response
```

If notification fails:

```text
Lead saved
 ↓
Notification failure
 ↓
Retry
 ↓
Log failure
```

The lead should not be lost because a notification failed.

---

# 52. Production Reliability Principles

n8n workflows should follow:

1. Idempotency
2. Explicit validation
3. Controlled retries
4. Timeouts
5. Clear error handling
6. Modular workflow design
7. Secure credentials
8. Traceable executions
9. Minimal unnecessary Code nodes
10. Clear workflow contracts

---

# 53. Workflow Versioning

Workflow changes should be tracked.

Recommended metadata:

```text
workflow_id
workflow_name
workflow_version
last_modified
change_description
```

Production workflow changes should be reviewed before deployment.

---

# 54. n8n and Git

Workflow definitions should eventually be version-controlled where practical.

Recommended repository structure:

```text
n8n/
├── workflows/
│   ├── lead-processing.json
│   ├── lead-qualification.json
│   ├── sales-notification.json
│   ├── follow-up-processing.json
│   └── error-handler.json
│
└── README.md
```

Secrets and credentials must never be committed.

---

# 55. n8n Environment Separation

Development and production environments should be separated.

Example:

```text
Development
    ↓
Testing
    ↓
Production
```

Each environment should have its own:

- Credentials
- Webhook URLs
- Database configuration
- AI configuration
- Notification configuration

---

# 56. n8n Implementation Tasks

These tasks should be added to `IMPLEMENTATION.md`.

### N8N-001

Set up n8n development environment.

### N8N-002

Configure secure credentials.

### N8N-003

Create lead enquiry webhook.

### N8N-004

Implement input validation.

### N8N-005

Implement conversation retrieval.

### N8N-006

Implement AI context preparation.

### N8N-007

Connect AI provider.

### N8N-008

Implement structured AI output validation.

### N8N-009

Implement lead creation/update workflow.

### N8N-010

Connect qualification service.

### N8N-011

Implement customer response generation.

### N8N-012

Implement sales notification.

### N8N-013

Implement follow-up processing.

### N8N-014

Implement Google Sheets synchronization.

### N8N-015

Implement workflow error handling.

### N8N-016

Implement retries and timeouts.

### N8N-017

Implement idempotency.

### N8N-018

Implement execution tracking.

### N8N-019

Create workflow monitoring.

### N8N-020

Create integration tests.

### N8N-021

Version-control workflow definitions.

### N8N-022

Prepare production workflows.

---

# 57. n8n Acceptance Criteria

The n8n layer is MVP-ready when:

- FastAPI can trigger the lead-processing workflow.
- Customer messages are validated.
- Conversation context can be retrieved.
- AI can extract structured requirements.
- AI output is validated.
- Leads can be created or updated.
- Qualification can be triggered.
- Customer responses can be generated.
- Responses can be returned to FastAPI.
- Hot leads can trigger sales notifications.
- Follow-ups can be processed.
- Google Sheets synchronization works where required.
- Errors are handled.
- Retry behavior is controlled.
- Duplicate processing is prevented.
- Credentials are securely managed.
- Workflow executions are traceable.
- Core workflows are tested.

---

# 58. Definition of Done

A workflow is considered complete when:

1. Its purpose is documented.
2. Its input contract is defined.
3. Its output contract is defined.
4. Required credentials are configured securely.
5. Validation is implemented.
6. Failure handling is implemented.
7. Retry behavior is defined.
8. Idempotency is considered.
9. Logging/traceability is available.
10. The workflow passes integration testing.
11. No unnecessary business logic is duplicated inside the workflow.
12. The workflow is documented in `IMPLEMENTATION.md`.

---

# 59. Core n8n Design Decisions

## Decision N8N-001

**n8n is the orchestration layer.**

Reason:

It is well suited for connecting AI, databases, notifications, and external services.

---

## Decision N8N-002

**SQL remains the source of truth.**

Reason:

Google Sheets is useful operationally but should not become the primary database.

---

## Decision N8N-003

**Critical business rules remain deterministic.**

Reason:

Lead qualification and other important decisions must be predictable and testable.

---

## Decision N8N-004

**AI is used for language understanding rather than authoritative decision-making.**

Reason:

LLMs can interpret natural language but should not control critical business rules.

---

## Decision N8N-005

**Workflows should remain modular.**

Reason:

Large monolithic workflows become difficult to test, debug, and maintain.

---

# 60. End-to-End Example

Customer sends:

```text
Hi, I'm looking for a 3-bedroom apartment around Lekki.
My budget is around ₦80 million and I want to buy within a month.
```

System:

```text
React
 ↓
FastAPI
 ↓
n8n
 ↓
Retrieve conversation
 ↓
AI extraction
 ↓
Validate output
 ↓
Create/update lead
 ↓
Qualification service
 ↓
Score = 82
 ↓
Priority = HOT
 ↓
SQL Database
 ↓
Sales notification
 ↓
Generate customer response
 ↓
FastAPI
 ↓
React
```

Customer receives:

```text
Thanks! I've noted your preference for a 3-bedroom apartment
in Lekki with a budget of around ₦80 million. A member of our
sales team can follow up with you shortly.
```

Sales receives:

```text
NEW HOT LEAD

3-bedroom apartment
Lekki
₦80M
Purchase within 1 month
Score: 82
```

---

# 61. Final Architecture

The complete system is:

```text
                         CUSTOMER
                            │
                            ↓
                         REACT
                            │
                            ↓
                         FASTAPI
                            │
                            ↓
                           n8n
                            │
             ┌──────────────┼───────────────┐
             ↓              ↓               ↓
            AI             SQL        Notifications
             │              │               │
             ↓              ↓               ↓
       Structured Data   Lead Data       Sales Team
             │
             ↓
        Validation
             │
             ↓
      Qualification
             │
             ↓
          Follow-up
             │
             ↓
        Google Sheets
```

---

# 62. Summary

n8n is the automation backbone of the Real Estate Lead Bot.

Its primary responsibility is to coordinate the flow between:

```text
FastAPI
   ↓
AI
   ↓
Database
   ↓
Qualification
   ↓
Notifications
   ↓
Follow-up
   ↓
Operational Integrations
```

The key principle is:

> **n8n orchestrates the process; AI understands language; FastAPI and domain services enforce application rules; SQL stores the truth; React handles interaction.**

This separation keeps the system modular, testable, secure, and maintainable as the Real Estate Lead Bot grows.