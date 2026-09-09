# System Architecture Document (SAD)

**Project:** Real Estate Lead Bot  
**Client:** PrimeHomes Realty  
**Document Version:** 0.1  
**Status:** Draft  
**Architecture Type:** Modular Application + Workflow Orchestration  
**Frontend:** React  
**Backend:** FastAPI  
**Automation:** n8n  
**AI:** LLM-based AI Processing  
**Primary Database:** SQL Database  
**Supporting Data Layer:** Google Sheets via n8n  

---

# 1. Purpose

This document defines the technical architecture of the Real Estate Lead Bot.

The purpose of this document is to establish:

- System components.
- Responsibilities of each component.
- Communication between components.
- Data flow.
- Integration boundaries.
- Technology responsibilities.
- Security boundaries.
- Reliability considerations.
- Scalability considerations.
- Deployment direction.

This document serves as a technical reference for developers and AI coding assistants working on the project.

---

# 2. Architecture Goals

The architecture should provide:

1. Clear separation of responsibilities.
2. Reliable lead processing.
3. Maintainable code.
4. Structured AI integration.
5. Reliable data persistence.
6. Clear API boundaries.
7. Flexible workflow automation.
8. Easy integration with external services.
9. Ability to scale beyond the MVP.
10. A clear source of truth for application data.

---

# 3. High-Level Architecture

The initial architecture is:

```text
                         ┌──────────────────┐
                         │     CUSTOMER     │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │  React Frontend  │
                         │                  │
                         │ Chat / Lead UI   │
                         └────────┬─────────┘
                                  │
                              HTTP/HTTPS
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    FastAPI       │
                         │     Backend      │
                         │                  │
                         │ API / Validation │
                         └────────┬─────────┘
                                  │
                                  │
                                  ▼
                         ┌──────────────────┐
                         │       n8n        │
                         │ Workflow Engine  │
                         └────────┬─────────┘
                                  │
                ┌─────────────────┼─────────────────┐
                │                 │                 │
                ▼                 ▼                 ▼
        ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
        │     AI       │  │ SQL Database │  │ Notifications│
        │   Processing │  │              │  │              │
        └──────────────┘  └──────────────┘  └──────────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   Sales Team     │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    Follow-up     │
                         └──────────────────┘
```

---

# 4. Architecture Principles

## 4.1 Separation of Responsibilities

Each technology has a defined responsibility.

```text
React
→ Presentation and user interaction

FastAPI
→ Application API and backend logic

n8n
→ Workflow orchestration and integrations

AI
→ Natural-language understanding and generation

SQL Database
→ Primary source of truth for application data

Google Sheets
→ Supporting operational data and reporting
```

No component should unnecessarily take responsibility for another component's job.

---

# 5. System Components

The system consists of the following major components:

```text
1. Customer Interface
2. FastAPI Backend
3. n8n Automation Layer
4. AI Processing Layer
5. SQL Database
6. Google Sheets Integration
7. Notification System
8. Sales Operations Interface
```

---

# 6. Frontend Architecture

## Technology

React.

The frontend provides the customer-facing interface.

Initial responsibilities include:

- Chat interface.
- Lead interaction.
- Message submission.
- Bot response display.
- Loading states.
- Error states.
- Basic lead forms where required.

---

## 6.1 Frontend Flow

```text
Customer
   │
   ▼
React UI
   │
   ▼
HTTP Request
   │
   ▼
FastAPI
```

The React application should communicate with the backend through defined API contracts.

The frontend should not directly access the SQL database.

The frontend should not contain sensitive credentials.

The frontend should not directly control n8n workflows.

---

# 7. Backend Architecture

## Technology

Python + FastAPI.

FastAPI acts as the application's API layer.

Responsibilities include:

- API endpoints.
- Request validation.
- Response validation.
- Authentication.
- Authorization.
- Business logic where appropriate.
- Data validation.
- Application-level error handling.
- Communication with internal/external services where appropriate.

---

## 7.1 Proposed Backend Structure

```text
backend/
│
├── app/
│   ├── main.py
│   │
│   ├── routes/
│   │   ├── chat.py
│   │   ├── leads.py
│   │   └── followups.py
│   │
│   ├── services/
│   │   ├── lead_service.py
│   │   ├── chat_service.py
│   │   └── qualification_service.py
│   │
│   ├── models/
│   │   ├── lead.py
│   │   ├── customer.py
│   │   └── conversation.py
│   │
│   ├── schemas/
│   │   ├── lead.py
│   │   ├── chat.py
│   │   └── response.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   └── migrations/
│   │
│   └── core/
│       ├── config.py
│       ├── security.py
│       └── logging.py
│
└── tests/
```

The exact structure may evolve as implementation begins.

---

# 8. n8n Architecture

n8n acts as the **workflow orchestration layer**.

Its purpose is to coordinate multi-step processes.

For example:

```text
Receive Message
      ↓
Validate / Normalize
      ↓
AI Extraction
      ↓
Check Required Information
      ↓
Qualification
      ↓
Store / Update Lead
      ↓
Notify Sales Team
      ↓
Generate Customer Response
```

---

# 8.1 n8n Responsibilities

n8n is responsible for:

- Workflow orchestration.
- AI workflow execution.
- External integrations.
- Notifications.
- Lead routing.
- Selected database operations.
- Google Sheets synchronization.
- Follow-up automation.
- Retry workflows.
- Scheduled processes.

---

# 8.2 What n8n Should NOT Own

n8n should not become the entire application backend.

Avoid putting complex domain logic exclusively inside large workflows.

For example, complicated business rules should preferably be implemented in:

```text
FastAPI
or
a clearly defined service/module
```

rather than hidden inside dozens of n8n nodes.

This makes the system easier to test, version, and maintain.

---

# 9. AI Architecture

The AI layer processes unstructured customer messages.

Its primary responsibilities are:

- Intent detection.
- Information extraction.
- Missing-information detection.
- Conversation understanding.
- Conversation summarization.
- Response generation.

---

# 9.1 AI Processing Flow

```text
Customer Message
       │
       ▼
Conversation Context
       │
       ▼
AI Model
       │
       ├───────────────┐
       ▼               ▼
Structured Data     Response
       │
       ▼
Business Rules
       │
       ▼
Lead Processing
```

---

# 9.2 AI Boundary

The AI should not be treated as the authoritative source of application state.

For example:

```text
AI:
"I think the customer wants to buy."

Application:
Determine whether this interpretation is acceptable.
```

The AI should produce structured information.

The application should validate and persist that information.

---

# 9.3 Structured AI Output

AI extraction should use a defined schema.

Example:

```json
{
  "intent": "BUY_PROPERTY",
  "property_type": "APARTMENT",
  "bedrooms": 3,
  "location": "Lekki",
  "budget_min": null,
  "budget_max": 80000000,
  "currency": "NGN",
  "timeline": "WITHIN_3_MONTHS",
  "confidence": 0.94
}
```

The exact schema will be defined in the AI Specification and Domain Specification.

---

# 10. Database Architecture

The SQL database is the **primary source of truth** for core application data.

It should store structured business information.

Initial entities include:

```text
Customer
Lead
Conversation
Message
LeadScore
FollowUp
SalesAgent
```

Potential future entities include:

```text
Property
PropertyListing
Organization
Notification
AuditLog
```

---

# 10.1 Database Responsibility

The SQL database should be authoritative for:

- Customer records.
- Lead records.
- Lead status.
- Lead score.
- Conversations.
- Messages.
- Sales assignments.
- Follow-up records.
- Application state.

---

# 10.2 Database Access

The preferred architectural direction is:

```text
React
   ↓
FastAPI
   ↓
SQL Database
```

and where workflow processing requires it:

```text
n8n
   ↓
SQL Database
```

Database access must follow defined schemas and rules.

The frontend must never connect directly to the database.

---

# 11. Google Sheets Architecture

Google Sheets is a supporting operational data layer.

It is NOT the primary source of truth for core application state once the SQL database is established.

Potential flow:

```text
SQL Database
      ↓
     n8n
      ↓
Google Sheets
```

Possible uses:

- Sales-team visibility.
- Simple reporting.
- Lead exports.
- Manual review.
- Operational workflows.
- Prototyping.

---

# 11.1 Source of Truth

The system should explicitly define ownership of data.

| Data | Source of Truth |
|---|---|
| Customer | SQL |
| Lead | SQL |
| Conversation | SQL |
| Message | SQL |
| Lead Score | SQL |
| Lead Status | SQL |
| Follow-up | SQL |
| Sales Assignment | SQL |
| Operational Sheet | Google Sheets |
| AI Output | Application-controlled after validation |

Google Sheets should not silently override authoritative SQL records.

---

# 12. Lead Processing Architecture

The core processing pipeline is:

```text
                 CUSTOMER
                    │
                    ▼
              React Frontend
                    │
                    ▼
                FastAPI
                    │
                    ▼
                  n8n
                    │
                    ▼
              Input Validation
                    │
                    ▼
               AI Processing
                    │
                    ▼
           Structured Extraction
                    │
                    ▼
          Required Fields Check
                    │
             ┌──────┴──────┐
             │             │
          Missing        Complete
             │             │
             ▼             ▼
       Ask Question     Qualification
                           │
                           ▼
                       Lead Score
                           │
                           ▼
                     Store / Update
                           │
                           ▼
                   Sales Notification
                           │
                           ▼
                    Customer Response
```

---

# 13. Chat Architecture

The chat system should maintain a conversation identifier.

Example:

```text
conversation_id
       │
       ├── message 1
       ├── message 2
       ├── message 3
       └── message 4
```

The conversation is associated with a customer and potentially a lead.

---

# 13.1 Example Chat Flow

Customer:

```text
I want to buy a 3 bedroom apartment.
```

System extracts:

```text
intent = BUY_PROPERTY
property_type = APARTMENT
bedrooms = 3
```

Missing:

```text
location
budget
timeline
```

Bot:

```text
Great. Which area are you looking to buy in?
```

Customer:

```text
Lekki.
```

System updates:

```text
location = Lekki
```

The conversation continues until enough information is available for the defined qualification process.

---

# 14. Lead Qualification Architecture

Lead qualification should use a combination of:

```text
AI extraction
      +
Deterministic business rules
      =
Lead qualification
```

AI should extract facts.

The application should apply business rules.

Example:

```text
AI:
budget = ₦80m

Business Rule:
budget >= ₦50m → high budget category
```

The final score can then be calculated deterministically.

---

# 15. Lead Scoring

Initial conceptual model:

```text
Lead Score =
Intent Strength
+ Budget
+ Timeline
+ Requirement Completeness
+ Location Specificity
+ Engagement
```

Example:

```text
Score: 87

Priority: HOT
```

The exact formula is intentionally not defined in the SAD.

It belongs in the business/domain specification.

---

# 16. Notification Architecture

When a lead reaches a defined priority or qualification state:

```text
Lead Qualified
      │
      ▼
n8n
      │
      ▼
Notification Service
      │
      ▼
Sales Team
```

Possible notification channels include:

- Email.
- Slack.
- WhatsApp.
- Telegram.
- Internal dashboard.

The MVP notification channel will be selected during implementation planning.

---

# 17. Sales Follow-up Architecture

After notification, the sales team should be able to continue the process.

Conceptual lifecycle:

```text
NEW
 ↓
QUALIFIED
 ↓
ASSIGNED
 ↓
CONTACTED
 ↓
FOLLOW_UP
 ↓
CONVERTED
```

Alternative:

```text
NEW
 ↓
CONTACTED
 ↓
LOST
```

Every status transition should be represented as structured application data.

---

# 18. API Communication

The primary communication path is:

```text
React
  │
  │ HTTPS
  ▼
FastAPI
  │
  │ API / Workflow Trigger
  ▼
n8n
```

Example:

```text
POST /api/v1/chat
```

Request:

```json
{
  "conversation_id": "conv_123",
  "message": "I need a 3 bedroom apartment in Lekki."
}
```

FastAPI validates the request before forwarding the appropriate information for processing.

---

# 19. API Responsibility Boundary

FastAPI is responsible for:

```text
Request validation
Authentication
Authorization
API contracts
Application logic
Error handling
```

n8n is responsible for:

```text
Workflow orchestration
AI processing
Integrations
Notifications
Automation
```

SQL is responsible for:

```text
Persistent application data
```

React is responsible for:

```text
Presentation
Interaction
Client-side state
```

---

# 20. Authentication and Authorization

Authentication will be required for protected sales/admin functionality.

The system should distinguish between:

```text
Customer
Sales Agent
Sales Manager
Administrator
```

Authorization determines what each role can access.

Example:

```text
Customer
→ Own conversation

Sales Agent
→ Assigned leads

Sales Manager
→ Team leads

Administrator
→ System configuration
```

The exact authentication mechanism will be defined during detailed system design.

---

# 21. Security Architecture

Security principles include:

- HTTPS for network communication.
- Secrets stored in environment variables or secret management systems.
- No API keys in frontend code.
- Database credentials must remain private.
- Authentication for protected APIs.
- Authorization checks for sensitive operations.
- Input validation.
- Output validation.
- Appropriate logging.
- Protection against unauthorized access.

Customer information should only be exposed to authorized users and services.

---

# 22. Error Handling Architecture

Failures should be isolated where possible.

Example:

```text
AI Failure
   ↓
Retry / Fallback
   ↓
Do not fabricate data
```

Database failure:

```text
Database Failure
   ↓
Log Error
   ↓
Retry where appropriate
   ↓
Preserve request/workflow state
```

Notification failure:

```text
Lead Stored
    ↓
Notification Failed
    ↓
Retry Notification
```

A notification failure must not cause an otherwise valid lead to disappear.

---

# 23. Reliability Strategy

The architecture should account for:

- API failures.
- AI failures.
- Database failures.
- n8n workflow failures.
- External API failures.
- Notification failures.
- Network failures.

Important workflows should have:

- Error handling.
- Retry strategies.
- Logging.
- Execution tracking.
- Idempotency where required.

---

# 24. Idempotency

The system should avoid processing the same customer message multiple times unintentionally.

A message may have a unique identifier:

```text
message_id
```

Before processing, the system can check whether that message has already been handled.

---

# 25. Observability

The system should provide visibility into:

- API requests.
- Workflow executions.
- AI calls.
- Database operations.
- Failures and retries.
- Lead lifecycle events.

---

# 26. Scalability Considerations

The initial architecture is designed for an MVP but should not prevent growth.

Possible future scaling directions include:

- Horizontal scaling of the FastAPI service.
- Queue-based processing for heavy AI or notification workloads.
- Read replicas for reporting.
- More advanced lead routing.
- Multi-tenant support.

---

# 27. Deployment Direction

The deployment model will be defined in the Deployment Specification.

The architecture assumes:

- Separable services.
- Environment-based configuration.
- No hard-coded secrets.
- Ability to run local development instances of each major component.

---

# 28. Summary of Technology Responsibilities

```text
React
→ User experience

FastAPI
→ API and application boundary

n8n
→ Workflow orchestration

AI
→ Natural-language understanding

SQL
→ System of record

Google Sheets
→ Supporting operational layer

Sales Team
→ Human decision-making and follow-up
```

The most important architectural principle is:

> **Use the right tool for the right responsibility.**

The system should not become an "everything in n8n" application, nor an "AI decides everything" application.

Instead:

```text
Frontend
→ presents

Backend
→ validates and governs

n8n
→ orchestrates

AI
→ interprets

Database
→ persists

Business Rules
→ determine

Sales Team
→ decides and acts
```

This architecture provides a foundation that is simple enough for the MVP while leaving room for the product to evolve into a more complete real estate lead-management platform.
