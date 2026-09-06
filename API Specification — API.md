# REAL ESTATE LEAD BOT
## API Specification

**Project:** Real Estate Lead Bot  
**Client:** PrimeHomes Realty  
**Document:** API Specification  
**Version:** 0.1  
**Status:** Draft  
**Last Updated:** 2026-09-05  
**API Framework:** FastAPI  
**API Style:** REST  
**Base URL:** `/api/v1`

---

# 1. Purpose

This document defines the API contract for the Real Estate Lead Bot.

It specifies how application components communicate with the backend.

The primary consumers are:

- React frontend
- n8n workflows
- AI processing services
- Sales operations interface
- Future external integrations

The API is responsible for exposing controlled access to the application's domain.

---

# 2. API Architecture

The primary communication flow is:

```text
CUSTOMER
    ↓
REACT FRONTEND
    ↓
FASTAPI
    ↓
DATABASE
    ↓
n8n / AI PROCESSING
    ↓
FASTAPI
    ↓
REACT / SALES TEAM
```

The frontend should **not** communicate directly with:

- PostgreSQL
- n8n
- AI provider APIs
- Google Sheets

Instead:

```text
React → FastAPI → Internal Services
```

---

# 3. API Design Principles

The API should follow these principles:

1. Clear resource-oriented endpoints.
2. Versioned URLs.
3. JSON request and response bodies.
4. Strong request validation.
5. Consistent error responses.
6. Authentication where required.
7. Authorization based on role.
8. Idempotency for retry-sensitive operations.
9. No database credentials exposed to clients.
10. AI output validated before becoming domain data.

---

# 4. Base URL

All application endpoints use:

```text
/api/v1
```

Example:

```text
POST /api/v1/chat
```

Development server may use:

```text
http://localhost:8000
```

Therefore:

```text
http://localhost:8000/api/v1/chat
```

Production URL will be environment-specific.

---

# 5. Content Type

Requests containing JSON should use:

```text
Content-Type: application/json
```

Responses should normally use:

```text
Content-Type: application/json
```

---

# 6. API Resources

The initial API exposes these resources:

```text
Chat
Leads
Customers
Conversations
Follow-ups
Sales Agents
```

Initial endpoints:

```text
POST   /chat

POST   /leads
GET    /leads
GET    /leads/{lead_id}
PATCH  /leads/{lead_id}

GET    /leads/{lead_id}/follow-ups
POST   /leads/{lead_id}/follow-ups

GET    /conversations/{conversation_id}
GET    /conversations/{conversation_id}/messages
```

Additional endpoints may be added as implementation progresses.

---

# 7. Authentication

Authentication requirements depend on the client.

## Customer

For the initial public chat experience, customers may use an anonymous session.

The system can identify the conversation through:

```text
conversation_id
```

A future authenticated customer account may use:

```text
Authorization: Bearer <token>
```

---

## Sales Agent

Sales operations should require authentication.

Example:

```text
Authorization: Bearer <access_token>
```

---

## Administrator

Administrative operations require authenticated administrative privileges.

---

# 8. Authorization Roles

Initial roles:

```text
CUSTOMER
SALES_AGENT
SALES_MANAGER
ADMIN
```

### Customer

May:

- Create conversations
- Send messages
- View their own conversation
- Provide/update their own information

### Sales Agent

May:

- View assigned leads
- Update lead status
- Create follow-ups
- Add sales notes
- Contact customers

### Sales Manager

May:

- View broader lead data
- Assign leads
- Reassign leads
- View sales performance

### Admin

May:

- Manage system configuration
- Manage users
- Manage agents
- Access administrative functions

---

# 9. POST `/chat`

## Purpose

Receives a customer message and starts or continues a conversation.

This is the primary customer-facing endpoint.

---

## Request

```http
POST /api/v1/chat
```

### Request body

```json
{
  "message": "Hi, I'm looking for a 3-bedroom apartment around Lekki. My budget is around ₦80 million.",
  "conversation_id": null,
  "customer_id": null
}
```

---

## Field Definitions

| Field | Type | Required | Description |
|---|---|---:|---|
| `message` | string | Yes | Customer's message |
| `conversation_id` | UUID | No | Existing conversation |
| `customer_id` | UUID | No | Existing customer |

---

## Validation

`message` must:

- Exist
- Be a string
- Not be empty
- Be within the configured maximum length

Example:

```text
message = ""
```

should return a validation error.

---

# 10. Chat Processing Flow

The backend should process the request approximately as:

```text
POST /chat
     ↓
Validate Request
     ↓
Identify/Create Customer
     ↓
Identify/Create Conversation
     ↓
Store Customer Message
     ↓
Trigger Processing
     ↓
AI Understands Message
     ↓
Extract Requirements
     ↓
Validate AI Output
     ↓
Create/Update Lead
     ↓
Qualification
     ↓
Generate Response
     ↓
Store Bot Message
     ↓
Return Response
```

---

# 11. Chat Response

Example:

```json
{
  "conversation_id": "8d77cbe1-2f4f-4f25-9f9e-7c1ab71b9e82",
  "message_id": "4b82a9c4-7e7e-45dc-a5cc-1b32b5d2c1a9",
  "response": "Thanks! Are you looking to buy within the next month, or are you still exploring your options?",
  "lead_id": "e17e6b55-7c4e-4cc7-a0c7-2d8d1c9b3b22",
  "lead_status": "NEW"
}
```

---

# 12. Chat Response Fields

| Field | Type | Description |
|---|---|---|
| `conversation_id` | UUID | Conversation identifier |
| `message_id` | UUID | Generated bot message ID |
| `response` | string | Customer-facing response |
| `lead_id` | UUID/null | Related lead |
| `lead_status` | string/null | Current lead status |

---

# 13. POST `/leads`

## Purpose

Creates a lead directly.

This endpoint may be used by:

- Internal applications
- Admin tools
- n8n
- Future integrations

Customer chat normally should not manually construct every lead field. The backend can create a lead from processed conversation data.

---

## Request

```http
POST /api/v1/leads
```

### Example

```json
{
  "customer_id": "8d77cbe1-2f4f-4f25-9f9e-7c1ab71b9e82",
  "intent": "BUY_PROPERTY",
  "transaction_type": "BUY",
  "property_type": "APARTMENT",
  "bedrooms": 3,
  "location": "Lekki",
  "budget_min": 80000000,
  "budget_max": 80000000,
  "currency": "NGN",
  "timeline": "WITHIN_1_MONTH"
}
```

---

# 14. Lead Creation Response

Successful creation:

```http
201 Created
```

Example:

```json
{
  "id": "e17e6b55-7c4e-4cc7-a0c7-2d8d1c9b3b22",
  "customer_id": "8d77cbe1-2f4f-4f25-9f9e-7c1ab71b9e82",
  "intent": "BUY_PROPERTY",
  "transaction_type": "BUY",
  "property_type": "APARTMENT",
  "bedrooms": 3,
  "location": "Lekki",
  "budget_min": 80000000,
  "budget_max": 80000000,
  "currency": "NGN",
  "timeline": "WITHIN_1_MONTH",
  "status": "NEW",
  "priority": null
}
```

---

# 15. GET `/leads`

## Purpose

Retrieves leads.

```http
GET /api/v1/leads
```

This endpoint will primarily serve sales operations.

---

# 16. Lead Filtering

The API should support filtering.

Example:

```text
GET /api/v1/leads?status=NEW
```

Priority:

```text
GET /api/v1/leads?priority=HOT
```

Location:

```text
GET /api/v1/leads?location=Lekki
```

Intent:

```text
GET /api/v1/leads?intent=BUY_PROPERTY
```

Multiple filters may be combined:

```text
GET /api/v1/leads?status=NEW&priority=HOT
```

---

# 17. Pagination

Lead lists should support pagination.

Example:

```text
GET /api/v1/leads?page=1&page_size=20
```

Example response:

```json
{
  "items": [],
  "page": 1,
  "page_size": 20,
  "total": 0
}
```

The exact pagination implementation can be refined during backend development.

---

# 18. GET `/leads/{lead_id}`

## Purpose

Retrieves a single lead.

```http
GET /api/v1/leads/{lead_id}
```

Example:

```text
GET /api/v1/leads/e17e6b55-7c4e-4cc7-a0c7-2d8d1c9b3b22
```

---

## Response

```json
{
  "id": "e17e6b55-7c4e-4cc7-a0c7-2d8d1c9b3b22",
  "customer": {
    "id": "8d77cbe1-2f4f-4f25-9f9e-7c1ab71b9e82",
    "name": "John",
    "email": "john@example.com",
    "phone": "+2348000000000"
  },
  "intent": "BUY_PROPERTY",
  "transaction_type": "BUY",
  "property_type": "APARTMENT",
  "bedrooms": 3,
  "location": "Lekki",
  "budget_min": 80000000,
  "budget_max": 80000000,
  "currency": "NGN",
  "timeline": "WITHIN_1_MONTH",
  "status": "NEW",
  "priority": "HOT"
}
```

---

# 19. PATCH `/leads/{lead_id}`

## Purpose

Updates an existing lead.

```http
PATCH /api/v1/leads/{lead_id}
```

Only supplied fields should be changed.

---

## Example Request

```json
{
  "timeline": "WITHIN_1_MONTH",
  "status": "CONTACTED"
}
```

---

## Example Response

```json
{
  "id": "e17e6b55-7c4e-4cc7-a0c7-2d8d1c9b3b22",
  "timeline": "WITHIN_1_MONTH",
  "status": "CONTACTED"
}
```

---

# 20. Lead Status Transitions

The backend must validate lifecycle changes.

Recommended valid transitions:

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

Possible alternative outcomes:

```text
QUALIFIED → LOST
FOLLOW_UP → LOST
CONTACTED → LOST
```

A future implementation may allow controlled reopening of leads.

Invalid transitions should return an error.

Example:

```text
CONVERTED → NEW
```

should not be accepted without an explicit business rule.

---

# 21. GET `/conversations/{conversation_id}`

## Purpose

Returns conversation information.

```http
GET /api/v1/conversations/{conversation_id}
```

Example response:

```json
{
  "id": "8d77cbe1-2f4f-4f25-9f9e-7c1ab71b9e82",
  "customer_id": "c8b7e5b0-4b9d-4b7e-8f18-3b9b6e1e7e20",
  "lead_id": "e17e6b55-7c4e-4cc7-a0c7-2d8d1c9b3b22",
  "status": "ACTIVE",
  "created_at": "2026-09-05T10:00:00Z",
  "updated_at": "2026-09-05T10:05:00Z"
}
```

---

# 22. GET `/conversations/{conversation_id}/messages`

## Purpose

Retrieves conversation messages.

```http
GET /api/v1/conversations/{conversation_id}/messages
```

Example response:

```json
{
  "items": [
    {
      "id": "11111111-1111-1111-1111-111111111111",
      "sender_type": "CUSTOMER",
      "content": "I want to buy a house in Lekki.",
      "created_at": "2026-09-05T10:00:00Z"
    },
    {
      "id": "22222222-2222-2222-2222-222222222222",
      "sender_type": "BOT",
      "content": "Sure. What's your approximate budget?",
      "created_at": "2026-09-05T10:01:00Z"
    }
  ]
}
```

Messages should normally be returned chronologically.

---

# 23. GET `/leads/{lead_id}/follow-ups`

## Purpose

Retrieves follow-up actions for a lead.

```http
GET /api/v1/leads/{lead_id}/follow-ups
```

---

# 24. POST `/leads/{lead_id}/follow-ups`

## Purpose

Creates a follow-up action.

```http
POST /api/v1/leads/{lead_id}/follow-ups
```

### Request

```json
{
  "sales_agent_id": "3f1a2c4d-5678-4abc-9def-123456789abc",
  "type": "CALL",
  "scheduled_at": "2026-09-06T10:00:00Z",
  "notes": "Call customer to confirm preferred property options."
}
```

---

## Response

```json
{
  "id": "6a7b8c9d-1234-4567-89ab-123456789abc",
  "lead_id": "e17e6b55-7c4e-4cc7-a0c7-2d8d1c9b3b22",
  "sales_agent_id": "3f1a2c4d-5678-4abc-9def-123456789abc",
  "type": "CALL",
  "status": "PENDING",
  "scheduled_at": "2026-09-06T10:00:00Z",
  "notes": "Call customer to confirm preferred property options."
}
```

---

# 25. Error Response Format

All API errors should use a consistent structure.

Example:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The request contains invalid data.",
    "details": [
      {
        "field": "budget_max",
        "message": "budget_max must be greater than or equal to budget_min."
      }
    ],
    "request_id": "req_123456"
  }
}
```

---

# 26. HTTP Status Codes

The API should use standard HTTP status codes.

| Status | Meaning |
|---:|---|
| `200` | Successful request |
| `201` | Resource created |
| `204` | Successful request with no response body |
| `400` | Bad request |
| `401` | Authentication required |
| `403` | Permission denied |
| `404` | Resource not found |
| `409` | Conflict |
| `422` | Validation error |
| `429` | Rate limit exceeded |
| `500` | Internal server error |
| `503` | Service temporarily unavailable |

---

# 27. Validation Error

FastAPI/Pydantic validation should catch malformed requests.

Example:

```json
{
  "message": ""
}
```

Response:

```http
422 Unprocessable Entity
```

The API should return enough information for the frontend to display a useful error.

---

# 28. Authentication Error

Unauthenticated protected request:

```http
401 Unauthorized
```

Example:

```json
{
  "error": {
    "code": "AUTHENTICATION_REQUIRED",
    "message": "Authentication is required."
  }
}
```

---

# 29. Authorization Error

Authenticated user without permission:

```http
403 Forbidden
```

Example:

```json
{
  "error": {
    "code": "FORBIDDEN",
    "message": "You do not have permission to perform this action."
  }
}
```

---

# 30. Resource Not Found

Example:

```text
GET /api/v1/leads/non-existent-id
```

Response:

```http
404 Not Found
```

```json
{
  "error": {
    "code": "LEAD_NOT_FOUND",
    "message": "The requested lead could not be found."
  }
}
```

---

# 31. Conflict Handling

A conflict may occur when a duplicate operation is detected.

Example:

```text
Same external message processed twice.
```

Response:

```http
409 Conflict
```

or, where appropriate, the API may return the already-created resource.

The exact idempotency strategy will be implemented based on the integration.

---

# 32. Idempotency

Operations that may be retried must be designed to avoid duplicate records.

Potential request header:

```text
Idempotency-Key: unique-operation-id
```

For message processing, an external message ID may also be used.

Example:

```text
Provider message ID
        ↓
Check database
        ↓
Already exists?
    ┌───┴───┐
   YES      NO
    ↓        ↓
 Return    Process
 Existing
```

This is particularly important for n8n retries and external webhook systems.

---

# 33. AI/n8n Internal Integration

n8n should not bypass domain validation simply because it is an internal service.

A typical workflow may be:

```text
n8n
 ↓
AI extraction
 ↓
Structured result
 ↓
FastAPI validation endpoint
 ↓
Lead update
```

Alternatively, n8n may call protected internal service endpoints.

The exact implementation can be chosen after the n8n workflow design.

---

# 34. AI Extraction Contract

The AI layer may produce a structure such as:

```json
{
  "intent": "BUY_PROPERTY",
  "transaction_type": "BUY",
  "property_type": "APARTMENT",
  "bedrooms": 3,
  "location": "Lekki",
  "budget_min": 80000000,
  "budget_max": 80000000,
  "currency": "NGN",
  "timeline": "WITHIN_1_MONTH",
  "missing_fields": []
}
```

The backend should validate:

- Enum values
- Numeric values
- Budget relationships
- Field types
- Required fields
- Allowed ranges

AI output should never be blindly inserted into the database.

---

# 35. Customer Response Contract

The API should return the generated response as plain text.

Example:

```json
{
  "response": "Thanks! What timeframe are you considering for the purchase?"
}
```

The frontend is responsible for displaying the response.

---

# 36. API Security

The API must:

- Use HTTPS in production.
- Never expose database credentials.
- Never expose AI provider API keys.
- Never expose n8n credentials.
- Validate request bodies.
- Validate path parameters.
- Authenticate protected endpoints.
- Authorize sensitive operations.
- Apply rate limiting where appropriate.
- Avoid exposing unnecessary internal errors.

---

# 37. Sensitive Data

Customer contact information should be handled carefully.

Examples:

- Phone number
- Email
- Customer name
- Conversation content

The API should only return customer information to authorized clients.

---

# 38. Rate Limiting

Public endpoints such as:

```text
POST /chat
```

may require rate limiting.

Example conceptual policy:

```text
Anonymous customer:
Limited requests per minute
```

The exact limits will be determined during deployment and testing.

---

# 39. Request IDs

Each API request should have a request identifier.

Example:

```text
X-Request-ID: req_123456
```

If the client does not provide one, the backend can generate one.

The request ID should appear in logs and, where useful, error responses.

This allows us to trace:

```text
React
 ↓
FastAPI
 ↓
n8n
 ↓
AI
 ↓
Database
```

for a single operation.

---

# 40. API Logging

The backend should log useful operational information such as:

- Request ID
- Endpoint
- HTTP method
- Response status
- Processing duration
- Error code
- Relevant resource ID

Do not log sensitive information unnecessarily.

---

# 41. API Versioning

The initial API uses:

```text
/api/v1
```

Future breaking changes can use:

```text
/api/v2
```

The existing API should not be silently broken when a new version is introduced.

---

# 42. OpenAPI Documentation

Because the backend uses FastAPI, the API should generate OpenAPI documentation automatically.

Development documentation will typically expose:

```text
/docs
```

and:

```text
/redoc
```

These are development conveniences and should be appropriately protected or disabled in production depending on security requirements.

---

# 43. API-to-Database Boundary

The frontend should never know database implementation details.

For example, React should request:

```text
GET /api/v1/leads/{lead_id}
```

rather than:

```text
SELECT * FROM leads WHERE id = ...
```

The API owns the boundary between application clients and the database.

---

# 44. API-to-n8n Boundary

FastAPI and n8n have different responsibilities.

### FastAPI

Owns:

- Validation
- Domain rules
- Authentication
- Authorization
- API contracts
- Database integrity

### n8n

Owns:

- Workflow orchestration
- External integrations
- Notifications
- AI workflow execution
- Google Sheets synchronization
- Follow-up automation

Architecture:

```text
React
  ↓
FastAPI
  ↓
Domain
  ↓
Database

FastAPI
  ↓
n8n
  ↓
AI / Notifications / Sheets
```

---

# 45. API Implementation Structure

Recommended FastAPI structure:

```text
backend/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── v1/
│   │       ├── router.py
│   │       ├── chat.py
│   │       ├── leads.py
│   │       ├── conversations.py
│   │       └── follow_ups.py
│   │
│   ├── models/
│   │   ├── customer.py
│   │   ├── lead.py
│   │   ├── conversation.py
│   │   ├── message.py
│   │   ├── lead_score.py
│   │   ├── sales_agent.py
│   │   └── follow_up.py
│   │
│   ├── schemas/
│   │   ├── chat.py
│   │   ├── lead.py
│   │   ├── conversation.py
│   │   └── follow_up.py
│   │
│   ├── services/
│   │   ├── lead_service.py
│   │   ├── chat_service.py
│   │   ├── qualification_service.py
│   │   └── customer_service.py
│   │
│   ├── db/
│   │   ├── session.py
│   │   └── base.py
│   │
│   └── core/
│       ├── config.py
│       ├── security.py
│       └── logging.py
│
├── migrations/
├── tests/
└── requirements.txt
```

This structure may evolve during implementation.

---

# 46. API Implementation Tasks

These tasks should be tracked in `IMPLEMENTATION.md`.

### API-001

Create FastAPI application.

### API-002

Configure API versioning.

### API-003

Configure Pydantic schemas.

### API-004

Create common error response format.

### API-005

Implement `POST /chat`.

### API-006

Implement `POST /leads`.

### API-007

Implement `GET /leads`.

### API-008

Implement `GET /leads/{lead_id}`.

### API-009

Implement `PATCH /leads/{lead_id}`.

### API-010

Implement conversation endpoints.

### API-011

Implement follow-up endpoints.

### API-012

Implement authentication.

### API-013

Implement authorization.

### API-014

Implement request IDs and logging.

### API-015

Implement idempotency strategy.

### API-016

Write API tests.

### API-017

Verify generated OpenAPI documentation.

---

# 47. API Acceptance Criteria

The API implementation is considered complete for MVP when:

- FastAPI starts successfully.
- `/api/v1` routes are registered.
- Requests are validated.
- Leads can be created.
- Leads can be retrieved.
- Leads can be updated.
- Lead filtering works.
- Conversations can be retrieved.
- Messages can be retrieved.
- Follow-ups can be created.
- Invalid data returns appropriate errors.
- Protected endpoints enforce authentication.
- Authorization rules work.
- Duplicate/retry scenarios are handled.
- API documentation is generated.
- Automated tests pass.

---

# 48. Example End-to-End Request

Customer sends:

> "Hi, I need a 2-bedroom apartment in Ikeja. My budget is ₦50 million."

React sends:

```http
POST /api/v1/chat
```

```json
{
  "message": "Hi, I need a 2-bedroom apartment in Ikeja. My budget is ₦50 million."
}
```

FastAPI:

```text
Validate
   ↓
Create/identify customer
   ↓
Create conversation
   ↓
Store message
   ↓
Trigger processing
```

AI extracts:

```json
{
  "intent": "BUY_PROPERTY",
  "property_type": "APARTMENT",
  "bedrooms": 2,
  "location": "Ikeja",
  "budget_max": 50000000,
  "currency": "NGN"
}
```

Backend validates the extraction.

Lead is created/updated.

Qualification runs.

The response is returned:

```json
{
  "conversation_id": "conversation-id",
  "message_id": "message-id",
  "response": "Thanks! Are you looking to buy the apartment, or are you interested in renting?",
  "lead_id": "lead-id",
  "lead_status": "NEW"
}
```

React displays the response.

---

# 49. Future API Extensions

Possible future endpoints:

```text
POST   /auth/login
POST   /auth/refresh

GET    /customers/{customer_id}

GET    /sales-agents
POST   /sales-agents

POST   /leads/{lead_id}/assign
GET    /leads/{lead_id}/assignments

PATCH  /follow-ups/{follow_up_id}

GET    /dashboard/metrics

GET    /properties
GET    /properties/{property_id}

POST   /webhooks/...
```

These should not be implemented until supported by actual requirements.

---

# 50. API Design Decisions

## Decision API-001

**FastAPI is the primary application API layer.**

Reason:

It provides strong Python typing, validation, OpenAPI support, and good integration with the planned backend.

---

## Decision API-002

**API versioning starts at `/api/v1`.**

Reason:

Allows future breaking changes without silently breaking existing clients.

---

## Decision API-003

**React communicates with FastAPI rather than directly with n8n.**

Reason:

FastAPI provides a controlled security, validation, and domain boundary.

---

## Decision API-004

**AI output must pass validation before database persistence.**

Reason:

AI-generated data cannot be treated as inherently reliable.

---

## Decision API-005

**Critical business rules remain outside the AI prompt.**

Reason:

Business-critical behavior should be deterministic, testable, and maintainable.

---

# 51. Summary

The API provides the controlled communication layer between the Real Estate Lead Bot's frontend, backend, automation, AI, and database components.

The primary architecture is:

```text
                    CUSTOMER
                       ↓
                     REACT
                       ↓
                    FASTAPI
                       ↓
              ┌────────┴────────┐
              ↓                 ↓
          PostgreSQL           n8n
                                ↓
                         AI / Integrations
                                ↓
                           Sales Operations
```

The central API principle is:

> **Clients communicate with FastAPI; FastAPI protects and governs the domain; n8n orchestrates automation; PostgreSQL stores authoritative data; AI interprets language but does not define business truth.**

This API contract provides the foundation for the next major specification:

**`FRONTEND.md`** — defining the React application structure, screens, components, chat experience, state management, API integration, and customer/sales-team user experience.