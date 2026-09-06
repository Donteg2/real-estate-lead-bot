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

## DEP-002 — Environment Configuration

**Status:** NOT_STARTED  
**Priority:** P0

Create:

```text
.env.example
```

Document required variables without exposing secrets.

---

## DEP-003 — Production Architecture

**Status:** NOT_STARTED  
**Priority:** P1

Define deployment for:

- React.
- FastAPI.
- n8n.
- SQL database.

---

## DEP-004 — Database Backups

**Status:** NOT_STARTED  
**Priority:** P1

Define database backup and recovery strategy.

---

## DEP-005 — Health Checks

**Status:** NOT_STARTED  
**Priority:** P1

Implement health endpoints and service monitoring.

---

# 16. Blocker Log

Use this section whenever development is blocked.

| ID | Date | Blocker | Impact | Owner | Status |
|---|---|---|---|---|---|
| BLK-001 | — | No blockers currently recorded | — | — | — |

---

# 17. Risk Log

| ID | Risk | Impact | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| RISK-001 | AI hallucinates information | High | Medium | Structured output + validation + restricted prompts | OPEN |
| RISK-002 | n8n becomes too complex | High | Medium | Keep business logic in backend/services | OPEN |
| RISK-003 | Google Sheets becomes primary database | High | Medium | SQL remains source of truth | OPEN |
| RISK-004 | Duplicate leads/messages | Medium | Medium | Idempotency and message IDs | OPEN |
| RISK-005 | Frontend tightly coupled to backend internals | Medium | Low | Strict API contract | OPEN |
| RISK-006 | Poor AI extraction accuracy | High | Medium | Evaluation dataset and validation | OPEN |

---

# 18. Decision Log

| ID | Decision | Reason |
|---|---|---|
| DEC-001 | React for frontend | Maintainable component-based UI |
| DEC-002 | FastAPI for backend | API validation and Python ecosystem |
| DEC-003 | n8n for orchestration | Integrations and workflow automation |
| DEC-004 | SQL as source of truth | Better data integrity and scalability |
| DEC-005 | Google Sheets as secondary layer | Operational visibility |
| DEC-006 | AI interprets; deterministic code decides critical rules | Reliability |
| DEC-007 | Frontend does not calculate lead score | Backend owns business rules |

---

# 19. Change Log

Track important implementation changes here.

| Version | Date | Change | Reason |
|---|---|---|---|
| 0.1 | — | Initial implementation plan | Project setup |

---

# 20. MVP Implementation Order

Development should generally follow this order:

```text
1. Documentation
       ↓
2. Domain
       ↓
3. Database
       ↓
4. FastAPI Backend
       ↓
5. AI Specification / AI Integration
       ↓
6. n8n Workflows
       ↓
7. React Frontend
       ↓
8. Integration
       ↓
9. Testing
       ↓
10. Security Review
       ↓
11. Deployment
```

The actual implementation may overlap where dependencies allow, but foundational contracts should be established first.

---

# 21. MVP Definition

The MVP should be able to perform this complete journey:

```text
Customer sends message
        ↓
React receives message
        ↓
FastAPI receives request
        ↓
n8n processes request
        ↓
AI understands message
        ↓
Requirements extracted
        ↓
Missing information identified
        ↓
Lead created/updated
        ↓
Lead qualified
        ↓
Lead score calculated
        ↓
Hot/Warm/Cold determined
        ↓
Lead stored in SQL
        ↓
Google Sheets updated
        ↓
Sales team notified when required
        ↓
Customer receives response
```

---

# 22. MVP Acceptance Criteria

The MVP is considered functionally complete when:

- [ ] Customer can start a conversation.
- [ ] Customer can send natural-language enquiries.
- [ ] System can identify customer intent.
- [ ] System can extract property requirements.
- [ ] System can identify missing information.
- [ ] System can maintain conversation context.
- [ ] System can create a lead.
- [ ] System can update an existing lead.
- [ ] System can qualify a lead.
- [ ] System can calculate a lead score.
- [ ] System can assign HOT/WARM/COLD priority.
- [ ] Lead is stored in SQL.
- [ ] Lead can be viewed by sales.
- [ ] Hot/actionable leads can trigger notifications.
- [ ] Customer receives an appropriate response.
- [ ] Follow-ups can be recorded.
- [ ] Google Sheets synchronization works.
- [ ] Critical error scenarios are handled.
- [ ] Core API tests pass.
- [ ] Core workflow tests pass.
- [ ] End-to-end test passes.
- [ ] No production secrets are exposed.

---

# 23. Definition of Done

A task can only be marked `DONE` when:

- [ ] Implementation is complete.
- [ ] Acceptance criteria are satisfied.
- [ ] Relevant tests have been completed.
- [ ] No critical errors remain.
- [ ] Code has been reviewed.
- [ ] Documentation has been updated if necessary.
- [ ] Integration points have been tested.
- [ ] Security implications have been considered.
- [ ] Changes have been committed to Git.

---

# 24. Development Checklist

For every feature:

### Before Development

- [ ] Requirement understood.
- [ ] Dependencies identified.
- [ ] API/data contract identified.
- [ ] Acceptance criteria defined.
- [ ] Relevant documentation reviewed.

### During Development

- [ ] Code follows architecture.
- [ ] Validation implemented.
- [ ] Errors handled.
- [ ] Logging added where required.
- [ ] Tests written.

### Before Completion

- [ ] Feature tested.
- [ ] Integration tested.
- [ ] Documentation updated.
- [ ] Git commit created.
- [ ] Acceptance criteria verified.
- [ ] Task moved to `DONE`.

---

# 25. Git Workflow

Recommended branch structure:

```text
main
│
├── feature/database
├── feature/backend-api
├── feature/frontend-chat
├── feature/ai-processing
├── feature/n8n-workflows
└── feature/testing
```

Example commits:

```text
feat: add lead database models
feat: implement chat endpoint
feat: add lead qualification service
feat: create customer chat interface
feat: add lead processing workflow
test: add lead scoring tests
fix: handle duplicate chat messages
docs: update API specification
```

---

# 26. Implementation Tracking Table

This is the main table to update during development.

| Task ID | Workstream | Task | Status | Priority | Dependency |
|---|---|---|---|---|---|
| DOC-003 | Documentation | Domain specification | READY | P0 | SAD |
| DOC-004 | Documentation | Database specification | READY | P0 | Domain |
| DOC-007 | AI | AI specification | READY | P0 | Domain |
| DB-001 | Database | SQL setup | NOT_STARTED | P0 | DATABASE.md |
| DB-002 | Database | Database models | NOT_STARTED | P0 | DB-001 |
| API-001 | Backend | FastAPI setup | NOT_STARTED | P0 | Engineering |
| API-002 | Backend | Database connection | NOT_STARTED | P0 | DB-001 |
| API-006 | Backend | Chat endpoint | NOT_STARTED | P0 | API-001 |
| API-010 | Backend | Lifecycle rules | NOT_STARTED | P0 | DB-002 |
| API-012 | Backend | Lead scoring | NOT_STARTED | P0 | Domain |
| FE-001 | Frontend | React setup | NOT_STARTED | P0 | FRONTEND.md |
| FE-003 | Frontend | API client | NOT_STARTED | P0 | API.md |
| FE-004 | Frontend | Chat interface | NOT_STARTED | P0 | FE-001 |
| AI-001 | AI | AI output schema | NOT_STARTED | P0 | AI-SPEC.md |
| AI-003 | AI | Requirement extraction | NOT_STARTED | P0 | AI-001 |
| AI-006 | AI | Response generation | NOT_STARTED | P0 | AI-003 |
| N8N-001 | n8n | n8n setup | NOT_STARTED | P0 | Engineering |
| N8N-002 | n8n | Lead enquiry workflow | NOT_STARTED | P0 | API + AI |
| N8N-006 | n8n | Qualification workflow | NOT_STARTED | P0 | API-012 |
| N8N-007 | n8n | Sales notification | NOT_STARTED | P0 | N8N-002 |
| TEST-001 | Testing | Backend tests | NOT_STARTED | P0 | Backend |
| TEST-005 | Testing | E2E testing | NOT_STARTED | P0 | Full integration |
| SEC-001 | Security | Secrets management | NOT_STARTED | P0 | Engineering |
| DEP-001 | Deployment | Development environment | NOT_STARTED | P0 | Engineering |

---

# 27. Weekly Execution Checklist

At the beginning of each development cycle:

- [ ] Review current status.
- [ ] Select highest-priority READY tasks.
- [ ] Check dependencies.
- [ ] Identify blockers.
- [ ] Define expected deliverables.

During development:

- [ ] Update task status.
- [ ] Record blockers.
- [ ] Commit changes regularly.
- [ ] Run tests.

At the end:

- [ ] Verify acceptance criteria.
- [ ] Update documentation.
- [ ] Update implementation tracker.
- [ ] Review risks.
- [ ] Record important architectural decisions.

---

# 28. Release Checklist

Before MVP release:

### Product

- [ ] MVP requirements completed.
- [ ] Core customer journey works.
- [ ] Sales workflow works.

### Backend

- [ ] API tests passing.
- [ ] Validation working.
- [ ] Error handling working.
- [ ] Authentication/authorization working where required.

### Database

- [ ] Migrations tested.
- [ ] Constraints verified.
- [ ] Backups configured.

### AI

- [ ] Extraction tested.
- [ ] AI output validated.
- [ ] Hallucination controls implemented.
- [ ] Response quality reviewed.

### n8n

- [ ] Core workflows tested.
- [ ] Failure handling tested.
- [ ] Notifications tested.
- [ ] Google Sheets synchronization tested.

### Frontend

- [ ] Chat works.
- [ ] Dashboard works.
- [ ] Lead details work.
- [ ] Responsive behavior verified.
- [ ] Loading/error states implemented.

### Security

- [ ] Secrets removed from source code.
- [ ] Environment variables configured.
- [ ] Access controls tested.
- [ ] Sensitive information protected.

### Deployment

- [ ] Production configuration verified.
- [ ] Health checks working.
- [ ] Logging enabled.
- [ ] Monitoring configured.
- [ ] Backup/recovery process documented.

---

# 29. Final Project Completion Criteria

The project is complete when the system can reliably transform:

```text
RAW CUSTOMER MESSAGE
        ↓
UNDERSTANDING
        ↓
STRUCTURED REQUIREMENTS
        ↓
LEAD
        ↓
QUALIFICATION
        ↓
SCORE
        ↓
PRIORITY
        ↓
SALES ACTION
        ↓
FOLLOW-UP
        ↓
OUTCOME
```

and every major stage is:

- Documented.
- Implemented.
- Tested.
- Observable.
- Maintainable.

---

# 30. Responsibility Model

| Component | Primary Responsibility |
|---|---|
| React | User interface and interaction |
| FastAPI | API, validation, application boundary |
| Backend Services | Business/application logic |
| n8n | Workflow orchestration and integrations |
| AI | Natural-language understanding |
| SQL | System of record |
| Google Sheets | Operational support |
| Notifications | Sales alerts |
| Git | Version control |
| Documentation | System knowledge and project coordination |

---

# 31. Core Architecture Rule

The implementation should maintain this boundary:

```text
React
  ↓
FastAPI
  ↓
Business/Application Services
  ↓
n8n / AI / Integrations
  ↓
SQL Database
```

with:

```text
AI = Understand
FastAPI/Services = Decide
n8n = Orchestrate
SQL = Store Truth
React = Present
Google Sheets = Support Operations
```

This separation should be preserved as the system grows.