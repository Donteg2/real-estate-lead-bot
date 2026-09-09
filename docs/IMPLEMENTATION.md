# REAL ESTATE LEAD BOT — IMPLEMENTATION

**Project:** Real Estate Lead Bot  
**Client:** PrimeHomes Realty  
**Version:** 0.1  
**Status:** Planning / Documentation  
**Primary Stack:** React + FastAPI + n8n + AI/LLM + SQL Database + Google Sheets

---

# 1. Purpose

This document is the central implementation and development tracking document for the Real Estate Lead Bot.

It translates the product and technical documentation into actionable development tasks.

The purpose is to:

- Track implementation progress.
- Define what needs to be built.
- Identify task dependencies.
- Track blockers and risks.
- Define acceptance criteria.
- Prevent important requirements from being forgotten.
- Coordinate frontend, backend, AI, n8n, database, testing, and deployment work.
- Provide a clear definition of when the project is ready for release.

This document should be updated throughout development.

---

# 2. Implementation Principles

Development should follow these principles:

1. Build from documented requirements.
2. Complete foundational work before dependent work.
3. Keep responsibilities separated between React, FastAPI, n8n, AI, and the database.
4. Validate data at system boundaries.
5. Keep critical business rules deterministic.
6. Do not allow AI output to bypass validation.
7. Keep SQL as the primary source of truth.
8. Keep Google Sheets as a supporting operational layer.
9. Keep secrets out of frontend code and Git.
10. Test features before marking them complete.
11. Update documentation when architecture or behavior changes.
12. Prefer simple, maintainable implementations over unnecessary complexity.

---

# 3. Status Definitions

| Status | Meaning |
|---|---|
| NOT_STARTED | Work has not started |
| READY | Requirements and dependencies are clear and task can begin |
| IN_PROGRESS | Currently being implemented |
| BLOCKED | Cannot continue because of a dependency or issue |
| REVIEW | Implementation is complete and awaiting review/testing |
| DONE | Acceptance criteria have been satisfied |

---

# 4. Priority Definitions

| Priority | Meaning |
|---|---|
| P0 | Critical for MVP / system cannot function without it |
| P1 | Important for MVP |
| P2 | Useful but can follow MVP |
| P3 | Future enhancement |

---

# 5. Project Workstreams

The project is divided into the following workstreams:

1. Documentation
2. Database
3. Backend/API
4. Frontend
5. AI
6. n8n Automation
7. Testing
8. Security
9. Deployment
10. Monitoring & Maintenance

---

# 6. Current Project Status

| Workstream | Status | Progress |
|---|---|---:|
| Documentation | IN_PROGRESS | 80% |
| Database | NOT_STARTED | 0% |
| Backend/API | NOT_STARTED | 0% |
| Frontend | NOT_STARTED | 0% |
| AI | NOT_STARTED | 0% |
| n8n | NOT_STARTED | 0% |
| Testing | NOT_STARTED | 0% |
| Security | NOT_STARTED | 0% |
| Deployment | NOT_STARTED | 0% |
| Monitoring | NOT_STARTED | 0% |

**Note:** Progress percentages are planning estimates and should be updated as implementation progresses.

---

# 7. Documentation Tasks

## DOC-001 — Product Requirements

**Status:** DONE  
**Priority:** P0

Create and maintain the PRD.

**Deliverable:**

`docs/PRD.md`

**Acceptance Criteria:**

- Product goals documented.
- Users documented.
- Functional requirements documented.
- Non-functional requirements documented.
- MVP scope documented.
- Success criteria documented.

---

## DOC-002 — System Architecture

**Status:** DONE  
**Priority:** P0

Create the System Architecture Document.

**Deliverable:**

`docs/SAD.md`

**Acceptance Criteria:**

- Components documented.
- Responsibilities documented.
- Data flow documented.
- Architecture decisions documented.
- Technology boundaries documented.

---

## DOC-003 — Domain Specification

**Status:** READY  
**Priority:** P0

Define the business domain and terminology.

**Deliverable:**

`docs/DOMAIN.md`

**Acceptance Criteria:**

- Lead defined.
- Customer defined.
- Conversation defined.
- Property requirements defined.
- Lead lifecycle defined.
- Lead priorities defined.
- Business rules documented.

---

## DOC-004 — Database Specification

**Status:** READY  
**Priority:** P0

Define the SQL database structure.

**Deliverable:**

`docs/DATABASE.md`

**Acceptance Criteria:**

- Tables defined.
- Relationships defined.
- Primary keys defined.
- Foreign keys defined.
- Indexes defined.
- Constraints defined.
- Migration strategy defined.

---

## DOC-005 — API Specification

**Status:** DONE  
**Priority:** P0

Define the backend API contract.

**Deliverable:**

`docs/API.md`

---

## DOC-006 — Frontend Specification

**Status:** DONE  
**Priority:** P1

Define the React application structure and UX requirements.

**Deliverable:**

`docs/FRONTEND.md`

---

## DOC-007 — AI Specification

**Status:** READY  
**Priority:** P0

Define how AI is used in the system.

**Deliverable:**

`docs/AI-SPEC.md`

**Acceptance Criteria:**

- AI responsibilities defined.
- Extraction schema defined.
- Intent classification defined.
- Response generation defined.
- AI validation defined.
- Hallucination controls defined.
- Evaluation strategy defined.

---

## DOC-008 — n8n Workflow Specification

**Status:** DONE  
**Priority:** P0

Define all required n8n workflows.

**Deliverable:**

`docs/N8N-WORKFLOWS.md`

---

## DOC-009 — Engineering Specification

**Status:** DONE  
**Priority:** P1

Define engineering standards and development practices.

**Deliverable:**

`docs/ENGINEERING.md`

---

# 8. Database Implementation

## DB-001 — Set Up SQL Database

**Status:** NOT_STARTED  
**Priority:** P0

Set up the development SQL database.

**Acceptance Criteria:**

- Database accessible.
- Development credentials configured.
- Environment variables configured.
- Connection tested.

---

## DB-002 — Database Models

**Status:** NOT_STARTED  
**Priority:** P0

Implement the initial database models.

Required entities:

- Customer
- Lead
- Conversation
- Message
- LeadScore
- FollowUp
- SalesAgent

---

## DB-003 — Database Relationships

**Status:** NOT_STARTED  
**Priority:** P0

Implement relationships between entities.

---

## DB-004 — Database Constraints

**Status:** NOT_STARTED  
**Priority:** P0

Implement:

- Required fields.
- Unique constraints.
- Foreign keys.
- Valid status values.
- Valid enum values.
- Referential integrity.

---

## DB-005 — Database Migrations

**Status:** NOT_STARTED  
**Priority:** P0

Set up migration management.

**Acceptance Criteria:**

- Initial migration created.
- Migration can be applied to a fresh database.
- Migration rollback strategy documented.

---

## DB-006 — Seed Development Data

**Status:** NOT_STARTED  
**Priority:** P1

Create sample:

- Customers.
- Leads.
- Sales agents.
- Conversations.
- Follow-ups.

---

# 9. Backend Implementation

## API-001 — FastAPI Project Setup

**Status:** NOT_STARTED  
**Priority:** P0

Create the FastAPI application.

Expected structure:

```text
backend/
└── app/
    ├── main.py
    ├── api/
    ├── models/
    ├── schemas/
    ├── services/
    ├── db/
    └── core/
```

---

## API-002 — Database Connection

**Status:** NOT_STARTED  
**Priority:** P0

Connect FastAPI to the SQL database.

---

## API-003 — Request Validation

**Status:** NOT_STARTED  
**Priority:** P0

Implement request validation using FastAPI/Pydantic schemas.

---

## API-004 — Customer Service

**Status:** NOT_STARTED  
**Priority:** P1

Implement customer creation and retrieval.

---

## API-005 — Lead Service

**Status:** NOT_STARTED  
**Priority:** P0

Implement lead creation, retrieval, update, and listing.

---

## API-006 — Chat Endpoint

**Status:** NOT_STARTED  
**Priority:** P0

Implement:

`POST /api/v1/chat`

The endpoint must:

- Receive customer messages.
- Validate input.
- Identify/create conversation.
- Trigger processing.
- Return bot response.

---

## API-007 — Lead Endpoints

**Status:** NOT_STARTED  
**Priority:** P0

Implement:

```text
POST   /api/v1/leads
GET    /api/v1/leads
GET    /api/v1/leads/{lead_id}
PATCH  /api/v1/leads/{lead_id}
```

---

## API-008 — Conversation Endpoints

**Status:** NOT_STARTED  
**Priority:** P1

Implement conversation and message retrieval.

---

## API-009 — Follow-up Endpoints

**Status:** NOT_STARTED  
**Priority:** P1

Implement:

```text
GET  /api/v1/leads/{lead_id}/follow-ups
POST /api/v1/leads/{lead_id}/follow-ups
```

---

## API-010 — Lead Lifecycle Rules

**Status:** NOT_STARTED  
**Priority:** P0

Implement valid lead status transitions.

Example:

```text
NEW
 ↓
CONTACTED
 ↓
QUALIFIED
 ↓
FOLLOW_UP
 ↓
CONVERTED
```

Leads may also move to:

```text
LOST
CLOSED
```

Invalid transitions must be rejected.

---

## API-011 — Lead Qualification Service

**Status:** NOT_STARTED  
**Priority:** P0

Implement deterministic qualification rules.

The service should evaluate information supplied by AI extraction and apply business rules.

---

## API-012 — Lead Scoring Service

**Status:** NOT_STARTED  
**Priority:** P0

Implement lead scoring.

Initial scoring factors:

- Intent strength.
- Budget.
- Timeline.
- Requirement completeness.
- Location specificity.
- Engagement.

The frontend must not calculate the score.

---

## API-013 — Error Handling

**Status:** NOT_STARTED  
**Priority:** P1

Implement consistent API error responses.

---

## API-014 — Authentication

**Status:** NOT_STARTED  
**Priority:** P1

Implement authentication for protected sales/admin functionality.

---

## API-015 — Authorization

**Status:** NOT_STARTED  
**Priority:** P1

Implement role-based access control.

Roles:

```text
CUSTOMER
SALES_AGENT
SALES_MANAGER
ADMIN
```

---

## API-016 — Logging and Request IDs

**Status:** NOT_STARTED  
**Priority:** P1

Implement structured application logging and request IDs.

---

## API-017 — API Tests

**Status:** NOT_STARTED  
**Priority:** P0

Create automated API tests for critical endpoints.

---

# 10. Frontend Implementation

## FE-001 — React Project Setup

**Status:** NOT_STARTED  
**Priority:** P0

Create the React application.

---

## FE-002 — Application Routing

**Status:** NOT_STARTED  
**Priority:** P1

Implement:

```text
/
 /chat
 /dashboard
 /leads/:leadId
 /not-found
```

---

## FE-003 — API Client

**Status:** NOT_STARTED  
**Priority:** P0

Create centralized API communication.

Expected structure:

```text
src/api/
├── client.js
├── chat.js
├── leads.js
├── conversations.js
└── followUps.js
```

---

## FE-004 — Customer Chat Interface

**Status:** NOT_STARTED  
**Priority:** P0

Build:

- Chat header.
- Message list.
- Message bubbles.
- Chat input.
- Typing indicator.
- Error states.

---

## FE-005 — Conversation State

**Status:** NOT_STARTED  
**Priority:** P0

Track:

- conversation_id.
- messages.
- loading state.
- errors.
- customer information.

---

## FE-006 — Lead Information Collection

**Status:** NOT_STARTED  
**Priority:** P1

Allow the bot to collect missing information conversationally.

---

## FE-007 — Sales Dashboard

**Status:** NOT_STARTED  
**Priority:** P1

Build dashboard containing:

- New leads.
- Hot leads.
- Warm leads.
- Follow-ups.
- Lead table.

---

## FE-008 — Lead Filters

**Status:** NOT_STARTED  
**Priority:** P1

Support filtering by:

- Status.
- Priority.
- Intent.
- Location.
- Timeline.
- Assigned agent.

---

## FE-009 — Lead Details

**Status:** NOT_STARTED  
**Priority:** P1

Display:

- Customer information.
- Property requirements.
- Qualification.
- Score.
- Priority.
- Status.
- Assigned agent.
- Conversation history.
- Follow-ups.

---

## FE-010 — Responsive Design

**Status:** NOT_STARTED  
**Priority:** P1

Ensure the application works on:

- Desktop.
- Tablet.
- Mobile.

---

# 11. AI Implementation

## AI-001 — Define AI Output Schema

**Status:** NOT_STARTED  
**Priority:** P0

Define structured AI output.

Example:

```json
{
  "intent": "BUY_PROPERTY",
  "transaction_type": "BUY",
  "property_type": "APARTMENT",
  "bedrooms": 3,
  "location": "Lekki",
  "budget_min": null,
  "budget_max": 80000000,
  "currency": "NGN",
  "timeline": "UNKNOWN",
  "customer_name": null,
  "customer_email": null,
  "customer_phone": null
}
```

---

## AI-002 — Intent Classification

**Status:** NOT_STARTED  
**Priority:** P0

Support:

```text
BUY_PROPERTY
RENT_PROPERTY
BUY_LAND
SELL_PROPERTY
GENERAL_ENQUIRY
```

---

## AI-003 — Requirement Extraction

**Status:** NOT_STARTED  
**Priority:** P0

Extract:

- Name.
- Email.
- Phone.
- Property type.
- Bedrooms.
- Location.
- Budget.
- Transaction type.
- Timeline.

---

## AI-004 — Missing Information Detection

**Status:** NOT_STARTED  
**Priority:** P0

Identify required information that has not been provided.

---

## AI-005 — Conversation Context

**Status:** NOT_STARTED  
**Priority:** P0

Ensure AI can use previous conversation messages when processing a new message.

---

## AI-006 — Customer Response Generation

**Status:** NOT_STARTED  
**Priority:** P0

Generate professional conversational responses.

AI must not:

- Invent property listings.
- Invent prices.
- Claim availability without verified data.
- Invent customer information.
- Expose internal scoring.
- Make unsupported promises.

---

## AI-007 — AI Output Validation

**Status:** NOT_STARTED  
**Priority:** P0

Validate AI-generated structured output before storing it.

---

## AI-008 — AI Evaluation

**Status:** NOT_STARTED  
**Priority:** P1

Create test cases covering:

- Complete enquiries.
- Incomplete enquiries.
- Ambiguous enquiries.
- Incorrect information.
- Multiple requirements.
- Land enquiries.
- Rental enquiries.
- Buying enquiries.

---

# 12. n8n Implementation

## N8N-001 — n8n Environment Setup

**Status:** NOT_STARTED  
**Priority:** P0

Configure development n8n environment.

---

## N8N-002 — Lead Enquiry Workflow

**Status:** NOT_STARTED  
**Priority:** P0

Implement:

```text
Receive Request
      ↓
Validate
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
Create/Update Lead
      ↓
Qualification
      ↓
Generate Response
      ↓
Save Message
      ↓
Notify Sales
      ↓
Return Response
```

---

## N8N-003 — AI Extraction

**Status:** NOT_STARTED  
**Priority:** P0

Connect n8n to the selected AI provider.

---

## N8N-004 — AI Output Validation

**Status:** NOT_STARTED  
**Priority:** P0

Reject malformed AI output before database updates.

---

## N8N-005 — Lead Creation/Update Workflow

**Status:** NOT_STARTED  
**Priority:** P0

Create a new lead or update an existing lead.

---

## N8N-006 — Qualification Workflow

**Status:** NOT_STARTED  
**Priority:** P0

Trigger deterministic qualification.

---

## N8N-007 — Sales Notification

**Status:** NOT_STARTED  
**Priority:** P0

Notify the sales team when a lead requires immediate attention.

---

## N8N-008 — Customer Response Workflow

**Status:** NOT_STARTED  
**Priority:** P0

Return an appropriate response to the customer.

---

## N8N-009 — Follow-up Workflow

**Status:** NOT_STARTED  
**Priority:** P1

Create and manage sales follow-ups.

---

## N8N-010 — Scheduled Follow-up Workflow

**Status:** NOT_STARTED  
**Priority:** P1

Process scheduled follow-ups automatically.

---

## N8N-011 — Google Sheets Synchronization

**Status:** NOT_STARTED  
**Priority:** P1

Synchronize relevant lead information to Google Sheets.

**Important:**

SQL remains the authoritative source of truth.

---

## N8N-012 — Error Handling Workflow

**Status:** NOT_STARTED  
**Priority:** P0

Handle:

- AI failures.
- API failures.
- Database failures.
- Timeout errors.
- Invalid data.
- External integration failures.

---

## N8N-013 — Workflow Monitoring

**Status:** NOT_STARTED  
**Priority:** P1

Track workflow executions and failures.

---

# 13. Testing Implementation

## TEST-001 — Backend Unit Tests

**Status:** NOT_STARTED  
**Priority:** P0

Test:

- Validation.
- Lead scoring.
- Qualification.
- Lifecycle transitions.
- Business rules.

---

## TEST-002 — API Integration Tests

**Status:** NOT_STARTED  
**Priority:** P0

Test frontend/backend API contracts.

---

## TEST-003 — AI Tests

**Status:** NOT_STARTED  
**Priority:** P0

Test extraction and classification accuracy.

---

## TEST-004 — n8n Workflow Tests

**Status:** NOT_STARTED  
**Priority:** P0

Test all critical workflows.

---

## TEST-005 — End-to-End Tests

**Status:** NOT_STARTED  
**Priority:** P0

Test:

```text
Customer
   ↓
React
   ↓
FastAPI
   ↓
n8n
   ↓
AI
   ↓
Database
   ↓
Qualification
   ↓
Sales Notification
   ↓
Customer Response
```

---

## TEST-006 — Failure Testing

**Status:** NOT_STARTED  
**Priority:** P1

Simulate:

- AI unavailable.
- Database unavailable.
- n8n failure.
- Invalid customer input.
- Duplicate message.
- API timeout.

---

# 14. Security Implementation

## SEC-001 — Environment Secrets

**Status:** NOT_STARTED  
**Priority:** P0

Store credentials in environment variables or secure secret management.

Never commit:

- API keys.
- Database passwords.
- AI credentials.
- n8n credentials.
- JWT secrets.

---

## SEC-002 — API Authentication

**Status:** NOT_STARTED  
**Priority:** P1

Protect sales/admin endpoints.

---

## SEC-003 — Authorization

**Status:** NOT_STARTED  
**Priority:** P1

Ensure users can only access resources allowed by their role.

---

## SEC-004 — Input Validation

**Status:** NOT_STARTED  
**Priority:** P0

Validate all external input.

---

## SEC-005 — PII Protection

**Status:** NOT_STARTED  
**Priority:** P1

Protect customer:

- Name.
- Email.
- Phone.
- Conversation history.

---

# 15. Deployment

## DEP-001 — Development Environment

**Status:** NOT_STARTED  
**Priority:** P0

Create reproducible local development environment.

---

*Full original content restored from the foundational specification.*
