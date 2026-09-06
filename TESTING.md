# REAL ESTATE LEAD BOT — TESTING

**Project:** Real Estate Lead Bot  
**Client:** PrimeHomes Realty  
**Version:** 0.1  
**Status:** Planning  
**Primary Stack:** React + FastAPI + n8n + AI/LLM + SQL Database + Google Sheets

---

# 1. Purpose

This document defines the testing strategy for the Real Estate Lead Bot.

The goal is to ensure that the system is:

- Correct.
- Reliable.
- Secure.
- Maintainable.
- Predictable.
- Resistant to invalid input.
- Able to handle AI uncertainty and failures.
- Able to process a customer enquiry from beginning to end.

Testing must verify both individual components and the complete system.

---

# 2. Testing Goals

The testing process must verify that:

1. Customer messages are received correctly.
2. API requests are validated.
3. Conversations are maintained correctly.
4. AI extracts information accurately.
5. AI does not invent customer or property information.
6. Leads are created and updated correctly.
7. Qualification rules work correctly.
8. Lead scores are calculated correctly.
9. Lead statuses follow valid transitions.
10. Data is stored correctly.
11. n8n workflows execute correctly.
12. Sales notifications are triggered when required.
13. Customer responses are returned correctly.
14. Google Sheets synchronization works.
15. Failures are handled gracefully.
16. Protected resources cannot be accessed without authorization.
17. The complete customer journey works end-to-end.

---

# 3. Testing Principles

The project follows these principles:

### 3.1 Test Business-Critical Logic

Critical business rules must have automated tests.

Examples:

- Lead scoring.
- Lead qualification.
- Lead status transitions.
- Required field validation.
- Duplicate message handling.

### 3.2 Test System Boundaries

Every major boundary should be tested.

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
  ↓
Notifications
```

### 3.3 Test Failure Scenarios

Testing should not only verify successful operations.

The system must also be tested when:

- AI fails.
- Database fails.
- API fails.
- n8n fails.
- Customer sends invalid data.
- External services timeout.
- Duplicate requests are received.

### 3.4 Do Not Trust AI Output

AI-generated structured data must always be validated.

The system should assume that AI can:

- Misinterpret a message.
- Miss information.
- Return invalid values.
- Return unexpected structures.
- Produce unsupported claims.

---

# 4. Testing Pyramid

The project follows a testing pyramid:

```text
              E2E Tests
             /        \
        Integration Tests
       /                \
   API / Workflow Tests
   /                    \
       Unit Tests
```

The majority of tests should be unit and integration tests.

End-to-end tests should cover the most important customer journeys.

---

# 5. Test Levels

The system will use the following testing levels:

| Test Level | Purpose |
|---|---|
| Unit Testing | Test individual functions/services |
| Component Testing | Test React components |
| API Testing | Test FastAPI endpoints |
| Integration Testing | Test communication between services |
| AI Testing | Test extraction, classification and responses |
| Workflow Testing | Test n8n workflows |
| Database Testing | Test persistence and constraints |
| E2E Testing | Test complete user journeys |
| Security Testing | Test authentication, authorization and data protection |
| Performance Testing | Test system behavior under load |
| Regression Testing | Ensure new changes do not break existing functionality |

---

# 6. Test Environments

The project should maintain separate environments.

```text
Development
     ↓
Testing
     ↓
Staging
     ↓
Production
```

Testing should not use production customer data.

---

# 7. Test Data

Test data should represent realistic PrimeHomes Realty enquiries.

### Example 1 — Complete Buying Enquiry

```text
Hi, I'm looking for a 3-bedroom apartment around Lekki.
My budget is around ₦80 million.
```

Expected extraction:

```json
{
  "intent": "BUY_PROPERTY",
  "transaction_type": "BUY",
  "property_type": "APARTMENT",
  "bedrooms": 3,
  "location": "Lekki",
  "budget_max": 80000000,
  "currency": "NGN"
}
```

---

### Example 2 — Rental Enquiry

```text
I need a 2 bedroom apartment for rent in Ikeja.
```

Expected:

```text
intent = RENT_PROPERTY
transaction_type = RENT
property_type = APARTMENT
bedrooms = 2
location = Ikeja
```

---

### Example 3 — Land Enquiry

```text
I need land around Ibadan, preferably below ₦20 million.
```

Expected:

```text
intent = BUY_LAND
transaction_type = BUY
property_type = LAND
location = Ibadan
budget_max = 20000000
currency = NGN
```

---

### Example 4 — Incomplete Enquiry

```text
Hello, I want to buy a house.
```

Expected behavior:

The system should identify the missing information and ask an appropriate follow-up question.

It should not invent:

- Location.
- Budget.
- Property type.
- Bedrooms.
- Timeline.

---

# 8. Unit Testing

Unit tests verify individual functions and services independently.

---

## TEST-UNIT-001 — Lead Scoring

Test different lead inputs and verify the calculated score.

Examples:

| Scenario | Expected |
|---|---|
| Strong intent + high budget + immediate timeline | High score |
| Researching only | Lower score |
| Missing requirements | Lower score |
| Specific location + budget + timeline | Higher score |

The exact score thresholds must come from the implemented business rules.

---

## TEST-UNIT-002 — Lead Qualification

Verify that qualification rules work correctly.

Test:

- Complete lead.
- Incomplete lead.
- High-value lead.
- Low-value lead.
- Immediate lead.
- Researching lead.

---

## TEST-UNIT-003 — Lead Status Transitions

Test valid transitions:

```text
NEW → CONTACTED
CONTACTED → QUALIFIED
QUALIFIED → FOLLOW_UP
FOLLOW_UP → CONVERTED
```

Also test:

```text
Any valid active status → LOST
```

Invalid transitions must be rejected.

---

## TEST-UNIT-004 — Input Validation

Test:

- Invalid email.
- Invalid phone.
- Negative budget.
- Invalid bedroom count.
- Invalid status.
- Invalid transaction type.
- Missing required fields.

---

## TEST-UNIT-005 — Duplicate Message Handling

Send the same message ID multiple times.

Expected:

```text
First request → Process
Duplicate request → Do not create duplicate record
```

---

# 9. Backend/API Testing

FastAPI endpoints must be tested independently from the frontend.

---

## API Test Matrix

| Endpoint | Method | Tests |
|---|---|---|
| `/chat` | POST | Valid/invalid messages |
| `/leads` | POST | Lead creation |
| `/leads` | GET | Listing/filtering |
| `/leads/{id}` | GET | Lead retrieval |
| `/leads/{id}` | PATCH | Lead update |
| `/conversations/{id}` | GET | Conversation retrieval |
| `/conversations/{id}/messages` | GET | Message history |
| `/leads/{id}/follow-ups` | GET | Follow-up retrieval |
| `/leads/{id}/follow-ups` | POST | Follow-up creation |

---

# 10. API Success Tests

Each endpoint must be tested with valid requests.

Verify:

- HTTP status code.
- Response structure.
- Response data.
- Database changes.
- Error-free execution.

Example:

```text
POST /api/v1/leads
```

Expected:

```text
HTTP 201 Created
```

---

# 11. API Validation Tests

Test invalid requests.

Examples:

```json
{
  "budget_max": -5000000
}
```

Expected:

```text
HTTP 422
```

Test:

- Missing required fields.
- Incorrect types.
- Invalid enum values.
- Invalid IDs.
- Invalid dates.
- Malformed JSON.

---

# 12. API Error Tests

Test expected failures.

Expected HTTP codes:

```text
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
409 → Conflict
422 → Validation Error
429 → Rate Limited
500 → Internal Server Error
503 → Service Unavailable
```

The API should return the standard error structure defined in `API.md`.

---

# 13. Database Testing

Database tests verify that information is stored and retrieved correctly.

Test:

- Customer creation.
- Lead creation.
- Lead update.
- Conversation creation.
- Message storage.
- Lead score storage.
- Follow-up creation.
- Sales agent assignment.

---

## Database Integrity Tests

Verify:

- Primary keys are unique.
- Foreign keys are valid.
- Required fields cannot be null.
- Invalid enum values are rejected.
- Duplicate records are prevented where required.
- Relationships remain consistent.

---

# 14. Conversation Testing

Test that conversations maintain context.

Example:

### Message 1

```text
I'm looking for an apartment in Lekki.
```

System stores:

```text
location = Lekki
property_type = APARTMENT
```

### Message 2

```text
3 bedrooms.
```

System should combine the information:

```text
location = Lekki
property_type = APARTMENT
bedrooms = 3
```

The second message must not erase valid information from the first message.

---

# 15. AI Testing

AI testing is critical because natural-language processing is probabilistic.

The goal is not only to test whether the model responds, but whether the output is **useful, structured, safe, and consistent enough for the application**.

---

# 16. AI Intent Tests

Test:

```text
BUY_PROPERTY
RENT_PROPERTY
BUY_LAND
SELL_PROPERTY
GENERAL_ENQUIRY
```

Example:

```text
"I want to buy a house."
```

Expected:

```text
BUY_PROPERTY
```

Example:

```text
"I need a place to rent in Ikeja."
```

Expected:

```text
RENT_PROPERTY
```

---

# 17. AI Extraction Tests

Verify extraction of:

- Customer name.
- Email.
- Phone.
- Property type.
- Bedrooms.
- Location.
- Budget.
- Currency.
- Transaction type.
- Timeline.

Test different natural-language variations.

Example:

```text
"I've got about 80m to spend."
```

Expected:

```text
budget_max = 80000000
currency = NGN
```

---

# 18. AI Missing Information Tests

Test whether AI correctly identifies missing information.

Example:

```text
"I want to buy a property."
```

Expected missing information may include:

- Location.
- Property type.
- Budget.
- Timeline.

The system should ask only useful follow-up questions.

---

# 19. AI Ambiguity Tests

Test ambiguous messages.

Examples:

```text
"I need something affordable."
"I want a nice place."
"Maybe somewhere around Lagos."
"I need a house soon."
```

The AI should not make unsupported assumptions.

Instead it should request clarification.

---

# 20. AI Hallucination Tests

Verify that AI does not invent:

- Property listings.
- Property availability.
- Prices.
- Addresses.
- Discounts.
- Customer information.
- Agent information.

Example:

```text
Customer: Do you have a 3-bedroom apartment in Lekki?
```

If the system has no verified property inventory, the response must not claim:

```text
"Yes, we have one available."
```

---

# 21. AI Structured Output Validation

AI output must pass schema validation before being used.

Example:

```json
{
  "bedrooms": "three"
}
```

should not be accepted when the schema requires:

```json
{
  "bedrooms": 3
}
```

Invalid output should trigger:

```text
AI Output
    ↓
Validation
    ↓
Invalid
    ↓
Retry / Fallback / Error Handling
```

---

# 22. AI Response Quality Tests

Responses should be evaluated for:

- Accuracy.
- Relevance.
- Professional tone.
- Conciseness.
- Correct follow-up questions.
- No unsupported claims.
- No exposure of internal system information.

---

# 23. n8n Workflow Testing

Each important workflow must be tested independently.

---

## N8N Test Matrix

| Workflow | Main Test |
|---|---|
| WF-001 Lead Enquiry Processing | Complete enquiry |
| WF-002 Lead Creation/Update | Create/update correctly |
| WF-003 Lead Qualification | Correct qualification |
| WF-004 Sales Notification | Correct notification |
| WF-005 Customer Response | Correct response |
| WF-006 Follow-up | Correct follow-up |
| WF-007 Sheets Sync | Correct synchronization |
| WF-008 Error Handling | Failure recovery |
| WF-009 Scheduled Follow-up | Scheduled execution |
| WF-010 Monitoring | Execution visibility |

---

# 24. n8n Failure Testing

Test:

- AI API unavailable.
- FastAPI unavailable.
- Database unavailable.
- Invalid AI response.
- Google Sheets unavailable.
- Notification service unavailable.
- Workflow timeout.

The workflow should fail predictably and record enough information for troubleshooting.

---

# 25. Integration Testing

Integration tests verify communication between components.

Examples:

### React → FastAPI

Verify that chat requests are correctly sent and responses correctly displayed.

### FastAPI → n8n

Verify workflow invocation and response handling.

### n8n → AI

Verify structured AI requests and outputs.

### n8n → Database

Verify lead persistence.

### n8n → Google Sheets

Verify operational synchronization.

---

# 26. End-to-End Testing

End-to-end tests simulate real customer behavior.

---

## E2E-001 — Complete Lead Journey

```text
Customer
   ↓
Opens Chat
   ↓
Sends Enquiry
   ↓
React
   ↓
FastAPI
   ↓
n8n
   ↓
AI
   ↓
Extract Requirements
   ↓
Create Lead
   ↓
Qualify
   ↓
Score
   ↓
Store in SQL
   ↓
Notify Sales
   ↓
Respond to Customer
```

Expected:

- Conversation created.
- Message stored.
- Lead created.
- Requirements extracted.
- Score calculated.
- Priority assigned.
- Sales notification generated.
- Customer receives response.

---

# 27. E2E-002 — Incomplete Lead

Customer:

```text
I want to buy a house.
```

Expected:

- Conversation created.
- Partial information stored.
- Missing requirements identified.
- Customer receives follow-up question.
- Lead remains incomplete.
- No unsupported assumptions made.

---

# 28. E2E-003 — Returning Customer

Customer provides information across multiple messages.

Expected:

- Same conversation maintained.
- Existing lead identified.
- New information merged.
- Existing valid information preserved.
- Lead updated rather than duplicated.

---

# 29. E2E-004 — Hot Lead

Customer:

```text
I need a 4-bedroom house in Lekki.
My budget is ₦150 million and I want to buy immediately.
```

Expected:

- High-intent lead detected.
- Requirements extracted.
- Lead qualified.
- Score calculated.
- Priority assigned according to business rules.
- Sales notification triggered.
- Customer receives appropriate response.

---

# 30. E2E-005 — Land Lead

Customer:

```text
I need land around Ibadan below ₦20 million.
```

Expected:

```text
intent = BUY_LAND
property_type = LAND
location = Ibadan
budget_max = 20000000
currency = NGN
```

---

# 31. Security Testing

Security tests must verify:

### Authentication

- Unauthenticated users cannot access protected resources.
- Invalid credentials are rejected.
- Expired credentials are rejected.

### Authorization

Verify that:

```text
CUSTOMER
SALES_AGENT
SALES_MANAGER
ADMIN
```

have the correct permissions.

### Input Security

Test:

- Malformed input.
- Oversized input.
- Injection attempts.
- Unexpected data types.

### Secret Protection

Verify that:

- API keys are not exposed.
- Database credentials are not exposed.
- n8n credentials are not exposed.
- AI provider credentials are not exposed to React.

---

# 32. Performance Testing

Performance testing should measure:

- API response time.
- Chat response time.
- Database query performance.
- n8n workflow execution time.
- AI response latency.
- Concurrent users.

Important target:

The customer should not experience unnecessary delays caused by inefficient workflow design.

Performance targets should be finalized before production deployment.

---

# 33. Load Testing

Simulate multiple customers using the system simultaneously.

Example scenarios:

```text
10 concurrent users
50 concurrent users
100 concurrent users
```

Measure:

- Response time.
- Error rate.
- Database performance.
- n8n execution capacity.
- AI provider limits.

Actual production capacity should be determined from deployment infrastructure and provider limits.

---

# 34. Regression Testing

Whenever an existing feature is changed, previously working functionality must be tested again.

Example:

Changing lead scoring should trigger regression tests for:

- Lead qualification.
- Lead priority.
- Sales notification.
- Dashboard display.

---

# 35. Test Automation

Automate repeatable tests wherever practical.

Recommended areas:

```text
Backend
→ pytest

Frontend
→ React component/integration testing

API
→ Automated HTTP tests

E2E
→ Browser automation

n8n
→ Workflow test cases

AI
→ Evaluation dataset
```

The exact testing libraries can be selected during implementation.

---

# 36. Test Naming Convention

Tests should clearly describe expected behavior.

Examples:

```text
test_create_lead_with_valid_data
test_reject_negative_budget
test_calculate_hot_lead_score
test_prevent_invalid_status_transition
test_extract_three_bedroom_requirement
test_handle_missing_location
test_prevent_duplicate_message
test_notify_sales_for_hot_lead
```

---

# 37. Test Organization

Recommended structure:

```text
tests/
├── unit/
│   ├── test_lead_scoring.py
│   ├── test_qualification.py
│   └── test_validation.py
│
├── api/
│   ├── test_chat.py
│   ├── test_leads.py
│   └── test_followups.py
│
├── integration/
│   ├── test_chat_flow.py
│   ├── test_lead_processing.py
│   └── test_database.py
│
├── ai/
│   ├── test_intent.py
│   ├── test_extraction.py
│   └── test_responses.py
│
└── e2e/
    ├── test_customer_journey
    └── test_sales_journey
```

---

# 38. Test Coverage

Coverage should focus on business-critical code rather than chasing a percentage.

Highest-priority coverage:

- Lead scoring.
- Qualification.
- Validation.
- Status transitions.
- Authentication.
- Authorization.
- Lead creation/update.
- Chat processing.
- AI output validation.
- n8n critical workflows.

---

# 39. Bug Severity

| Severity | Description |
|---|---|
| Critical | System unusable, data loss, security breach |
| High | Major feature broken |
| Medium | Feature partially broken |
| Low | Minor issue or cosmetic problem |

---

# 40. Bug Report Format

When a bug is discovered, record:

```text
Bug ID:
Title:
Date:
Environment:
Severity:
Steps to Reproduce:
Expected Result:
Actual Result:
Error:
Affected Component:
Possible Cause:
Status:
Resolution:
```

Example:

```text
Bug ID: BUG-001
Title: Duplicate lead created from repeated message
Severity: High
Component: n8n / Database
Status: OPEN
```

---

# 41. Testing Workflow

Every feature should follow:

```text
Requirement
    ↓
Implementation
    ↓
Unit Test
    ↓
Integration Test
    ↓
E2E Test
    ↓
Review
    ↓
DONE
```

---

# 42. Pre-Merge Testing

Before merging a feature:

- [ ] Code compiles/runs.
- [ ] Unit tests pass.
- [ ] Relevant integration tests pass.
- [ ] Existing tests still pass.
- [ ] No critical errors.
- [ ] Security implications reviewed.
- [ ] Documentation updated if required.

---

# 43. Pre-Release Testing

Before release:

- [ ] Full automated test suite passes.
- [ ] Critical E2E flows pass.
- [ ] AI evaluation passes.
- [ ] n8n workflows pass.
- [ ] Database migrations tested.
- [ ] Authentication tested.
- [ ] Authorization tested.
- [ ] Error scenarios tested.
- [ ] Performance reviewed.
- [ ] Production configuration reviewed.
- [ ] Secrets verified.
- [ ] Backup strategy verified.

---

# 44. MVP Test Scenarios

The following scenarios are mandatory for MVP:

| ID | Scenario | Expected Result |
|---|---|---|
| TEST-001 | Customer wants to buy apartment | Lead created |
| TEST-002 | Customer wants to rent apartment | Rental intent identified |
| TEST-003 | Customer wants land | Land intent identified |
| TEST-004 | Customer wants to sell | Selling intent identified |
| TEST-005 | Customer gives incomplete information | Follow-up question |
| TEST-006 | Customer sends multiple messages | Context maintained |
| TEST-007 | Customer sends duplicate message | No duplicate processing |
| TEST-008 | High-value urgent lead | Correct priority |
| TEST-009 | Low-intent researching customer | Lower qualification |
| TEST-010 | AI returns invalid data | Output rejected |
| TEST-011 | AI unavailable | Graceful failure |
| TEST-012 | Database unavailable | Error handled |
| TEST-013 | Sales notification required | Notification sent |
| TEST-014 | Google Sheets unavailable | Core SQL operation remains authoritative |
| TEST-015 | Unauthorized dashboard access | Access denied |

---

# 45. Definition of Test Completion

A feature is considered tested when:

- [ ] Happy path tested.
- [ ] Invalid input tested.
- [ ] Edge cases tested.
- [ ] Failure path tested.
- [ ] Relevant integration tested.
- [ ] Relevant security behavior tested.
- [ ] Automated tests created where practical.
- [ ] Acceptance criteria satisfied.
- [ ] No critical unresolved bugs remain.

---

# 46. Testing Tasks

| Task ID | Task | Priority | Status |
|---|---|---|---|
| TEST-001 | Backend unit tests | P0 | NOT_STARTED |
| TEST-002 | API tests | P0 | NOT_STARTED |
| TEST-003 | Database tests | P0 | NOT_STARTED |
| TEST-004 | AI evaluation tests | P0 | NOT_STARTED |
| TEST-005 | n8n workflow tests | P0 | NOT_STARTED |
| TEST-006 | Integration tests | P0 | NOT_STARTED |
| TEST-007 | E2E tests | P0 | NOT_STARTED |
| TEST-008 | Security tests | P1 | NOT_STARTED |
| TEST-009 | Performance tests | P1 | NOT_STARTED |
| TEST-010 | Regression test suite | P1 | NOT_STARTED |

---

# 47. Relationship With IMPLEMENTATION.md

Testing tasks must be tracked in `IMPLEMENTATION.md`.

The testing process should not exist separately from development.

```text
IMPLEMENTATION.md
        ↓
Development Task
        ↓
Implementation
        ↓
TESTING.md
        ↓
Validation
        ↓
Task marked DONE
```

A task should not be marked `DONE` simply because the code was written.

It should be marked `DONE` after the required testing and acceptance criteria have been satisfied.

---

# 48. Final Testing Principle

The system is not considered reliable simply because:

```text
"The code works."
```

It is reliable when:

```text
The expected input works
        +
Invalid input is handled
        +
Failures are handled
        +
AI uncertainty is controlled
        +
Data remains consistent
        +
Security rules work
        +
The complete customer journey works
```

The ultimate test is whether a real customer can send an enquiry and the system can reliably move that enquiry from:

```text
CUSTOMER MESSAGE
      ↓
UNDERSTANDING
      ↓
LEAD
      ↓
QUALIFICATION
      ↓
SALES ACTION
      ↓
FOLLOW-UP
      ↓
OUTCOME
```

without losing, corrupting, or inventing important information.