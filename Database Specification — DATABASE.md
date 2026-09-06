# REAL ESTATE LEAD BOT
## Database Specification

**Project:** Real Estate Lead Bot  
**Client:** PrimeHomes Realty  
**Document:** Database Specification  
**Version:** 0.1  
**Status:** Draft  
**Last Updated:** 2026-09-05  
**Primary Database:** PostgreSQL (Recommended)  
**ORM Direction:** SQLAlchemy  
**Migration Tool:** Alembic  
**Source of Truth:** SQL Database

---

# 1. Purpose

This document defines how the core domain of the Real Estate Lead Bot will be persisted in the SQL database.

It translates the concepts defined in `DOMAIN.md` into:

- Tables
- Columns
- Primary keys
- Foreign keys
- Relationships
- Enums
- Constraints
- Indexes
- Data ownership rules

This document is the primary reference for implementing the database layer.

It will guide:

- SQL schema creation
- SQLAlchemy models
- Alembic migrations
- FastAPI data access
- n8n database operations
- API design

---

# 2. Database Design Goals

The database should provide:

1. A reliable source of truth.
2. Clear relationships between domain entities.
3. Support for customer conversations.
4. Support for multiple leads per customer.
5. Lead lifecycle tracking.
6. Lead qualification and scoring.
7. Sales assignment and follow-up tracking.
8. Duplicate prevention.
9. Good query performance.
10. Future extensibility.

---

# 3. Database Technology Decision

## Recommended Database

**PostgreSQL**

PostgreSQL is recommended because the system requires:

- Relational data
- Foreign keys
- Constraints
- Transactions
- Indexes
- Structured queries
- Strong consistency
- Potential JSON support
- Future scalability

---

## 3.1 Why Not Google Sheets as the Main Database?

Google Sheets will be used as a supporting operational layer through n8n.

It may be useful for:

- Lead visibility
- Reports
- Exports
- Manual review
- Sales team collaboration

However, Google Sheets is not suitable as the primary database for this system.

The source-of-truth architecture is:

```text
                    PRIMARY DATA
                         │
                         ▼
                   PostgreSQL
                         │
                         ▼
                        n8n
                         │
                         ▼
                   Google Sheets
                 Operational Copy
```

**PostgreSQL owns the authoritative data.**

Google Sheets should not silently overwrite SQL records.

---

# 4. Core Database Entities

The initial MVP database contains:

```text
customers
leads
conversations
messages
lead_scores
sales_agents
lead_assignments
follow_ups
```

Supporting tables may later include:

```text
notifications
audit_logs
properties
property_listings
organizations
```

---

# 5. Entity Relationship Overview

```text
CUSTOMERS
    │
    │ 1
    │
    ├────────< CONVERSATIONS
    │               │
    │               │ 1
    │               │
    │               └──────< MESSAGES
    │
    │ 1
    │
    └────────< LEADS
                    │
                    │ 1
                    ├─────── 1 LEAD_SCORES
                    │
                    ├──────< FOLLOW_UPS
                    │
                    └──────< LEAD_ASSIGNMENTS
                                  │
                                  │
                                  ▼
                             SALES_AGENTS
```

---

# 6. Primary Key Strategy

The system will use UUIDs as primary identifiers.

Example:

```text
customer_id = UUID
lead_id = UUID
conversation_id = UUID
message_id = UUID
```

## Reason

UUIDs are recommended because:

- IDs can be safely generated across services.
- FastAPI and n8n can reference records without exposing sequential IDs.
- They support distributed systems.
- They are useful for public APIs.
- They reduce collision risks across independent processes.

Example:

```text
8d77cbe1-2f4f-4f25-9f9e-7c1ab71b9e82
```

---

# 7. Common Columns

Most primary entities should include:

```text
id
created_at
updated_at
```

Where appropriate:

```text
created_by
updated_by
```

Timestamp storage should use timezone-aware timestamps.

Recommended PostgreSQL type:

```text
TIMESTAMPTZ
```

All application timestamps should be stored consistently in UTC.

---

# 8. ENUM Design

The system uses controlled values for important domain fields.

PostgreSQL enums may be used for stable values.

However, for values expected to change frequently, application-level enums or lookup tables may be preferable.

For the MVP, the following values are treated as controlled application enums.

---

## 8.1 Intent

```text
BUY_PROPERTY
RENT_PROPERTY
BUY_LAND
SELL_PROPERTY
GENERAL_ENQUIRY
```

---

## 8.2 Transaction Type

```text
BUY
RENT
SELL
INQUIRE
```

---

## 8.3 Property Type

```text
APARTMENT
HOUSE
DUPLEX
LAND
COMMERCIAL
OFFICE
SHOP
ESTATE
OTHER
UNKNOWN
```

---

## 8.4 Timeline

```text
IMMEDIATE
WITHIN_1_MONTH
WITHIN_3_MONTHS
RESEARCHING
UNKNOWN
```

---

## 8.5 Lead Status

```text
NEW
CONTACTED
QUALIFIED
FOLLOW_UP
CONVERTED
LOST
CLOSED
```

---

## 8.6 Lead Priority

```text
HOT
WARM
COLD
```

---

## 8.7 Sender Type

```text
CUSTOMER
BOT
SALES_AGENT
SYSTEM
```

---

## 8.8 Follow-up Type

```text
CALL
EMAIL
WHATSAPP
SMS
OTHER
```

---

## 8.9 Follow-up Status

```text
PENDING
COMPLETED
CANCELLED
MISSED
```

---

# 9. Customers Table

## Table Name

```text
customers
```

## Purpose

Stores customer identity and contact information.

### Schema

| Column | Type | Required | Description |
|---|---|---:|---|
| `id` | UUID | Yes | Primary key |
| `name` | VARCHAR(255) | No | Customer name |
| `email` | VARCHAR(255) | No | Customer email |
| `phone` | VARCHAR(50) | No | Customer phone |
| `preferred_contact` | VARCHAR / ENUM | No | Preferred contact method |
| `created_at` | TIMESTAMPTZ | Yes | Record creation |
| `updated_at` | TIMESTAMPTZ | Yes | Last update |

### Primary Key

```text
customers.id
```

### Initial Constraints

A customer should normally have at least one identifiable contact method when available:

```text
email
OR
phone
```

However, the chat system may initially receive anonymous messages.

Therefore, both may be nullable during early conversation stages.

---

# 10. Customer Identification Strategy

Customer identification is a business concern and should be handled carefully.

Initial matching priority:

```text
1. Phone number
2. Email
3. Existing authenticated/session identity
4. Create new anonymous customer record
```

The system must avoid blindly merging two customers based only on name.

For example:

```text
"John"
```

is not sufficient for unique identification.

---

# 11. Leads Table

## Table Name

```text
leads
```

## Purpose

Stores a specific real estate opportunity.

### Schema

| Column | Type | Required | Description |
|---|---|---:|---|
| `id` | UUID | Yes | Primary key |
| `customer_id` | UUID | Yes | FK to customers |
| `intent` | VARCHAR / ENUM | Yes | Customer intent |
| `transaction_type` | VARCHAR / ENUM | No | Buy, rent, sell |
| `property_type` | VARCHAR / ENUM | No | Property category |
| `bedrooms` | INTEGER | No | Bedroom count |
| `location` | VARCHAR(255) | No | Desired location |
| `budget_min` | NUMERIC(15,2) | No | Minimum budget |
| `budget_max` | NUMERIC(15,2) | No | Maximum budget |
| `currency` | CHAR(3) | No | ISO currency code |
| `timeline` | VARCHAR / ENUM | Yes | Customer timeframe |
| `status` | VARCHAR / ENUM | Yes | Lead lifecycle status |
| `priority` | VARCHAR / ENUM | No | HOT/WARM/COLD |
| `created_at` | TIMESTAMPTZ | Yes | Creation time |
| `updated_at` | TIMESTAMPTZ | Yes | Last update |

---

## 11.1 Foreign Key

```text
leads.customer_id
    ↓
customers.id
```

Relationship:

```text
One Customer
     ↓
Many Leads
```

---

## 11.2 Lead Defaults

Initial defaults:

```text
timeline = UNKNOWN
status = NEW
priority = NULL
```

A priority may remain null until the lead has been scored.

---

## 11.3 Lead Constraints

### Bedrooms

If present:

```text
bedrooms > 0
```

Bedrooms may be null when:

- Not provided
- Not applicable
- Property type is land

---

### Budget

If both values exist:

```text
budget_min <= budget_max
```

Example valid:

```text
budget_min = 50,000,000
budget_max = 80,000,000
```

Example invalid:

```text
budget_min = 100,000,000
budget_max = 80,000,000
```

---

# 12. Conversations Table

## Table Name

```text
conversations
```

## Purpose

Stores a customer interaction session.

### Schema

| Column | Type | Required | Description |
|---|---|---:|---|
| `id` | UUID | Yes | Primary key |
| `customer_id` | UUID | Yes | FK to customer |
| `lead_id` | UUID | No | Related lead |
| `status` | VARCHAR(50) | Yes | Conversation state |
| `created_at` | TIMESTAMPTZ | Yes | Created |
| `updated_at` | TIMESTAMPTZ | Yes | Last activity |

---

## 12.1 Relationships

```text
customers.id
     ↓
conversations.customer_id
```

One customer can have multiple conversations.

Optional lead relationship:

```text
leads.id
     ↓
conversations.lead_id
```

A conversation can exist before a lead is created.

---

# 13. Messages Table

## Table Name

```text
messages
```

## Purpose

Stores individual messages within a conversation.

### Schema

| Column | Type | Required | Description |
|---|---|---:|---|
| `id` | UUID | Yes | Primary key |
| `conversation_id` | UUID | Yes | FK to conversation |
| `sender_type` | VARCHAR / ENUM | Yes | Message sender |
| `content` | TEXT | Yes | Message content |
| `external_id` | VARCHAR(255) | No | External provider ID |
| `created_at` | TIMESTAMPTZ | Yes | Message timestamp |

---

## 13.1 Relationship

```text
One Conversation
       ↓
Many Messages
```

```text
conversations.id
       ↓
messages.conversation_id
```

---

# 14. Message Idempotency

External channels may retry message delivery.

To reduce duplicate processing, an external message ID may be stored.

Example:

```text
external_id = provider_message_123
```

Where an external ID exists, it should be unique within the relevant integration context.

This helps prevent:

```text
Same message
    ↓
Workflow retry
    ↓
Duplicate lead update
```

---

# 15. Lead Scores Table

## Table Name

```text
lead_scores
```

## Purpose

Stores the current or historical qualification score of a lead.

For the MVP, the table should preserve scoring history rather than only overwriting a single score.

### Schema

| Column | Type | Required | Description |
|---|---|---:|---|
| `id` | UUID | Yes | Primary key |
| `lead_id` | UUID | Yes | FK to lead |
| `score` | INTEGER | Yes | Score from 0–100 |
| `priority` | VARCHAR / ENUM | Yes | HOT/WARM/COLD |
| `reason` | TEXT | No | Explanation of score |
| `scoring_version` | VARCHAR(50) | Yes | Rule version |
| `created_at` | TIMESTAMPTZ | Yes | Score timestamp |

---

## 15.1 Score Constraint

```text
score >= 0
AND
score <= 100
```

---

## 15.2 Why Preserve Score History?

A lead can change over time.

Example:

```text
Day 1
Score = 45
Priority = COLD
```

Customer provides more information:

```text
Day 3
Score = 82
Priority = HOT
```

Historical scoring helps with:

- Auditing
- Debugging
- Sales analysis
- Improving qualification rules

---

# 16. Sales Agents Table

## Table Name

```text
sales_agents
```

## Purpose

Stores sales team members who can receive lead assignments.

### Schema

| Column | Type | Required | Description |
|---|---|---:|---|
| `id` | UUID | Yes | Primary key |
| `name` | VARCHAR(255) | Yes | Agent name |
| `email` | VARCHAR(255) | No | Work email |
| `phone` | VARCHAR(50) | No | Work phone |
| `is_active` | BOOLEAN | Yes | Active availability |
| `created_at` | TIMESTAMPTZ | Yes | Created |
| `updated_at` | TIMESTAMPTZ | Yes | Updated |

---

# 17. Lead Assignments Table

## Table Name

```text
lead_assignments
```

## Purpose

Tracks assignment of leads to sales agents.

This is separate from the `leads` table to preserve assignment history.

### Schema

| Column | Type | Required | Description |
|---|---|---:|---|
| `id` | UUID | Yes | Primary key |
| `lead_id` | UUID | Yes | FK to lead |
| `sales_agent_id` | UUID | Yes | FK to sales agent |
| `assigned_at` | TIMESTAMPTZ | Yes | Assignment time |
| `unassigned_at` | TIMESTAMPTZ | No | End of assignment |
| `assigned_by` | UUID | No | User/system responsible |

---

## 17.1 Active Assignment

A lead's current assignment can be identified as:

```text
unassigned_at IS NULL
```

This allows assignment history without losing previous records.

---

# 18. Follow-ups Table

## Table Name

```text
follow_ups
```

## Purpose

Tracks planned and completed sales follow-up actions.

### Schema

| Column | Type | Required | Description |
|---|---|---:|---|
| `id` | UUID | Yes | Primary key |
| `lead_id` | UUID | Yes | FK to lead |
| `sales_agent_id` | UUID | No | FK to sales agent |
| `type` | VARCHAR / ENUM | Yes | Follow-up method |
| `status` | VARCHAR / ENUM | Yes | Follow-up state |
| `scheduled_at` | TIMESTAMPTZ | No | Planned time |
| `completed_at` | TIMESTAMPTZ | No | Completion time |
| `notes` | TEXT | No | Follow-up notes |
| `created_at` | TIMESTAMPTZ | Yes | Created |
| `updated_at` | TIMESTAMPTZ | Yes | Updated |

---

# 19. Lead Assignment and Follow-up Flow

```text
LEAD CREATED
      │
      ▼
QUALIFIED
      │
      ▼
ASSIGN SALES AGENT
      │
      ▼
CREATE FOLLOW-UP
      │
      ▼
CONTACT CUSTOMER
      │
      ▼
UPDATE FOLLOW-UP
      │
      ▼
UPDATE LEAD STATUS
```

---

# 20. Relationship Summary

| Parent | Relationship | Child |
|---|---|---|
| Customer | 1 → Many | Leads |
| Customer | 1 → Many | Conversations |
| Conversation | 1 → Many | Messages |
| Lead | 1 → Many | Lead Scores |
| Lead | 1 → Many | Lead Assignments |
| Lead | 1 → Many | Follow-ups |
| Sales Agent | 1 → Many | Lead Assignments |
| Sales Agent | 1 → Many | Follow-ups |

---

# 21. Recommended Indexes

Indexes should support common application queries.

## Customers

```text
INDEX customers_email_idx
INDEX customers_phone_idx
```

Email and phone matching are common during customer identification.

---

## Leads

Recommended:

```text
INDEX leads_customer_id_idx
INDEX leads_status_idx
INDEX leads_priority_idx
INDEX leads_created_at_idx
INDEX leads_location_idx
```

Useful queries include:

```text
All leads for customer
All HOT leads
All NEW leads
Recent leads
Leads by location
```

---

## Conversations

```text
INDEX conversations_customer_id_idx
INDEX conversations_lead_id_idx
```

---

## Messages

```text
INDEX messages_conversation_id_idx
INDEX messages_created_at_idx
```

Common query:

```text
Get conversation messages ordered by time.
```

---

## Lead Scores

```text
INDEX lead_scores_lead_id_idx
INDEX lead_scores_created_at_idx
```

---

## Follow-ups

```text
INDEX follow_ups_lead_id_idx
INDEX follow_ups_sales_agent_id_idx
INDEX follow_ups_status_idx
INDEX follow_ups_scheduled_at_idx
```

Important query:

```text
Which follow-ups are pending today?
```

---

# 22. Unique Constraints

Potential constraints include:

## Customer Email

A unique constraint should **not automatically** be added immediately unless the business confirms one email always belongs to exactly one customer.

Initial recommendation:

```text
Index email for lookup.
```

Then refine uniqueness based on customer identity rules.

---

## Customer Phone

Same approach:

```text
Index phone for lookup.
```

Phone normalization should happen before identity matching.

---

## External Message ID

Where available:

```text
UNIQUE (external_id)
```

or, for multiple message providers:

```text
UNIQUE (provider, external_id)
```

The final design depends on the communication channels added.

---

# 23. Data Normalization

The initial schema follows relational normalization principles.

Examples:

Do not store all messages inside:

```text
leads.messages
```

Instead:

```text
conversations
     ↓
messages
```

Do not store repeated sales agent information inside every lead.

Instead:

```text
sales_agents
     ↓
lead_assignments
```

This reduces:

- Duplicate data
- Update problems
- Inconsistent records

---

# 24. Unknown vs NULL

`NULL` should be used carefully.

In this system, `NULL` generally means:

```text
Information is currently unavailable
```

Example:

```text
budget_max = NULL
```

means the budget is unknown.

It does **not** mean:

```text
Budget = 0
```

These are different business meanings.

---

# 25. Monetary Data

Monetary values should use:

```text
NUMERIC(15,2)
```

Not:

```text
FLOAT
```

Example:

```text
80000000.00
```

Using decimal/numeric types avoids floating-point precision problems.

Currency should be stored separately.

Example:

```text
budget_max = 80000000.00
currency = NGN
```

---

# 26. Data Validation Responsibilities

Validation occurs at multiple levels.

## Frontend

Basic user experience validation.

Example:

```text
Email format
Required form fields
```

---

## FastAPI

Authoritative request validation.

Example:

```text
Budget cannot be negative.
Bedrooms cannot be negative.
Score must be 0–100.
```

---

## Database

Final data integrity protection.

Example:

```text
CHECK score >= 0 AND score <= 100
```

Important rules should not depend on only one layer.

---

# 27. Transaction Strategy

Important multi-step database operations should use transactions.

Example:

```text
Create Lead
     +
Create Lead Score
     +
Create Assignment
```

If the operation requires all records to succeed together, the system should avoid partial inconsistent state.

---

# 28. Soft Delete Strategy

For the initial MVP:

Core business records should generally **not be physically deleted casually**.

Potential future approach:

```text
deleted_at TIMESTAMPTZ NULL
```

However, soft deletion should only be added where there is a clear business requirement.

For now, avoid premature columns and complexity.

---

# 29. Audit Strategy

Initial audit requirements can be handled through:

- `created_at`
- `updated_at`
- Lead score history
- Lead assignment history

A dedicated `audit_logs` table can be introduced later when the application requires detailed change tracking.

---

# 30. AI Data Storage

Raw AI processing should not automatically become the source of truth.

The recommended flow is:

```text
Customer Message
       ↓
AI Processing
       ↓
Structured Extraction
       ↓
Validation
       ↓
Update SQL Domain Data
```

For future debugging and AI evaluation, we may later add an `ai_extractions` table.

Possible future fields:

```text
id
message_id
model
prompt_version
raw_response
structured_output
validation_status
created_at
```

This is not required for the first MVP schema but is a likely future extension.

---

# 31. n8n Database Access Rules

n8n may read and write SQL data where workflow orchestration requires it.

However:

1. SQL remains the source of truth.
2. n8n should use defined database operations.
3. Critical validation should not exist only inside workflow nodes.
4. Workflow retries must consider duplicate processing.
5. Database writes should be idempotent where possible.

Example:

```text
n8n Retry
   ↓
Check Message ID
   ↓
Already Processed?
   │
 ┌─┴─┐
YES   NO
 │     │
Skip  Process
```

---

# 32. Google Sheets Synchronization

Google Sheets should receive selected operational data.

Recommended pattern:

```text
PostgreSQL Updated
       ↓
n8n Workflow
       ↓
Transform Data
       ↓
Google Sheets
```

Potential exported columns:

```text
Lead ID
Customer Name
Phone
Email
Intent
Location
Budget
Timeline
Score
Priority
Status
Assigned Agent
Created Date
```

Google Sheets is an operational projection of the SQL data.

It is not the primary transactional database.

---

# 33. Data Flow

The primary data flow is:

```text
Customer
   ↓
React
   ↓
FastAPI
   ↓
Validate Request
   ↓
Store Message
   ↓
n8n / AI Processing
   ↓
Structured Data
   ↓
Validate
   ↓
Create or Update Lead
   ↓
Calculate Score
   ↓
Store Score
   ↓
Assign / Notify Sales
   ↓
Sync Selected Data to Google Sheets
```

---

# 34. Database Migration Strategy

Database changes must be version-controlled.

Recommended process:

```text
Change SQLAlchemy Model
       ↓
Create Alembic Migration
       ↓
Review Migration
       ↓
Run on Development Database
       ↓
Test
       ↓
Apply to Staging
       ↓
Apply to Production
```

Avoid manually changing production tables without a tracked migration.

---

# 35. Initial SQL Schema Order

The recommended creation order is:

```text
1. customers
2. sales_agents
3. leads
4. conversations
5. messages
6. lead_scores
7. lead_assignments
8. follow_ups
```

This order respects foreign key dependencies.

---

# 36. Initial MVP Scope

The first database implementation should include:

- `customers`
- `leads`
- `conversations`
- `messages`
- `lead_scores`
- `sales_agents`
- `lead_assignments`
- `follow_ups`

Do not add future tables until they are needed.

---

# 37. Database Implementation Tasks

These tasks will later be added to `IMPLEMENTATION.md`.

### DB-001

Set up PostgreSQL database.

### DB-002

Configure database connection in FastAPI.

### DB-003

Configure SQLAlchemy.

### DB-004

Configure Alembic migrations.

### DB-005

Create `customers` table.

### DB-006

Create `sales_agents` table.

### DB-007

Create `leads` table.

### DB-008

Create `conversations` table.

### DB-009

Create `messages` table.

### DB-010

Create `lead_scores` table.

### DB-011

Create `lead_assignments` table.

### DB-012

Create `follow_ups` table.

### DB-013

Add indexes.

### DB-014

Add constraints.

### DB-015

Create and test initial migration.

### DB-016

Seed development data.

---

# 38. Database Design Decisions

## Decision DB-001

**PostgreSQL is the primary database.**

Reason:

The application has relational data and requires strong consistency and structured querying.

---

## Decision DB-002

**UUIDs are used as primary keys.**

Reason:

They work well across APIs, workflows, and distributed components.

---

## Decision DB-003

**Lead scoring history is preserved.**

Reason:

Lead scores can change as new customer information becomes available.

---

## Decision DB-004

**Lead assignment history is preserved.**

Reason:

Sales ownership may change and historical tracking is useful.

---

## Decision DB-005

**Google Sheets is not the source of truth.**

Reason:

SQL provides stronger data integrity and relationship management.

---

## Decision DB-006

**Monetary values use NUMERIC rather than FLOAT.**

Reason:

Avoid floating-point precision issues.

---

# 39. Future Database Extensions

Potential future additions:

```text
properties
property_listings
property_images
notifications
audit_logs
ai_extractions
users
roles
organizations
integrations
webhook_events
```

These should only be introduced when supported by actual product requirements.

---

# 40. Definition of Done

The database design is ready for implementation when:

- Core entities are defined.
- Tables are identified.
- Relationships are documented.
- Primary keys are defined.
- Foreign keys are defined.
- Controlled values are defined.
- Constraints are documented.
- Important indexes are identified.
- Data ownership is clear.
- PostgreSQL is confirmed as the source of truth.
- Google Sheets' supporting role is defined.
- Migration strategy is documented.
- Implementation tasks are identified.

---

# 41. Summary

The Real Estate Lead Bot uses PostgreSQL as its authoritative database.

The core model is:

```text
CUSTOMER
   │
   ├──< CONVERSATION
   │        │
   │        └──< MESSAGE
   │
   └──< LEAD
           │
           ├──< LEAD_SCORE
           │
           ├──< LEAD_ASSIGNMENT >── SALES_AGENT
           │
           └──< FOLLOW_UP
```

The key architectural rule is:

> **PostgreSQL stores the truth. React displays it. FastAPI governs access to it. n8n orchestrates processes around it. AI interprets unstructured information. Google Sheets receives operational copies where useful.**

This database design provides the foundation for the next document:

**`API.md`**, which will define how the React frontend, FastAPI backend, n8n workflows, and external systems communicate using the domain and database model.