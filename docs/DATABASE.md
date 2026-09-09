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

---

# 1. Purpose

This document defines the SQL database structure for the Real Estate Lead Bot.

The SQL database is the **primary source of truth** for core application data.

It stores:

- Customers
- Leads
- Conversations
- Messages
- Lead scores
- Follow-ups
- Sales agents
- Related application state

Google Sheets is treated only as a supporting operational layer.

---

# 2. Design Principles

1. SQL is authoritative for core business data.
2. Prefer clear, normalized structures.
3. Use explicit status and enum values.
4. Preserve history where useful (timestamps, status changes).
5. Support conversation context and lead lifecycle tracking.
6. Keep the schema understandable for both developers and AI coding assistants.
7. Design for the MVP while leaving room for future entities (properties, organizations, audit logs).

---

# 3. Recommended Database

**PostgreSQL** is the recommended primary database.

Reasons:

- Strong relational integrity
- Good JSON support if needed later
- Reliable concurrent access
- Mature ecosystem with SQLAlchemy + Alembic

Other SQL databases may be used for local development if necessary, but production should target PostgreSQL.

---

# 4. Core Entities

## 4.1 Customer

Represents a person interacting with the system.

| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER / SERIAL | Primary key |
| name | VARCHAR(255) | Nullable until collected |
| email | VARCHAR(255) | Unique, nullable, indexed |
| phone | VARCHAR(50) | Unique, nullable, indexed |
| preferred_contact_method | VARCHAR(50) | e.g. WHATSAPP, EMAIL, PHONE |
| created_at | TIMESTAMPTZ | |
| updated_at | TIMESTAMPTZ | |

---

## 4.2 Lead

The central business entity.

| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER / SERIAL | Primary key |
| customer_id | INTEGER | FK → customers.id, nullable |
| intent | VARCHAR(50) | BUY_PROPERTY, RENT_PROPERTY, etc. |
| property_type | VARCHAR(100) | APARTMENT, HOUSE, LAND, etc. |
| bedrooms | INTEGER | Nullable |
| location | VARCHAR(255) | |
| budget_min | NUMERIC | |
| budget_max | NUMERIC | |
| currency | VARCHAR(10) | Default NGN |
| transaction_type | VARCHAR(20) | BUY, RENT, SELL, INQUIRE |
| timeline | VARCHAR(50) | IMMEDIATE, WITHIN_1_MONTH, etc. |
| additional_requirements | TEXT | |
| status | VARCHAR(30) | NEW, CONTACTED, QUALIFIED, etc. |
| priority | VARCHAR(20) | HOT, WARM, COLD |
| score | NUMERIC | 0–100 |
| assigned_agent_id | INTEGER | FK → sales_agents.id |
| source | VARCHAR(100) | |
| notes | TEXT | |
| created_at | TIMESTAMPTZ | |
| updated_at | TIMESTAMPTZ | |

---

## 4.3 Conversation

| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER / SERIAL | Primary key |
| conversation_uid | VARCHAR(64) | Unique external identifier |
| customer_id | INTEGER | FK → customers.id |
| lead_id | INTEGER | FK → leads.id |
| status | VARCHAR(30) | ACTIVE, CLOSED |
| created_at | TIMESTAMPTZ | |
| updated_at | TIMESTAMPTZ | |

---

## 4.4 Message

| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER / SERIAL | Primary key |
| conversation_id | INTEGER | FK → conversations.id |
| role | VARCHAR(20) | user, assistant, system |
| content | TEXT | |
| message_uid | VARCHAR(64) | Unique, for idempotency |
| created_at | TIMESTAMPTZ | |

---

## 4.5 SalesAgent

| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER / SERIAL | Primary key |
| name | VARCHAR(255) | |
| email | VARCHAR(255) | Unique |
| phone | VARCHAR(50) | |
| role | VARCHAR(50) | SALES_AGENT, SALES_MANAGER, ADMIN |
| is_active | BOOLEAN | Default true |
| created_at | TIMESTAMPTZ | |
| updated_at | TIMESTAMPTZ | |

---

## 4.6 FollowUp

| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER / SERIAL | Primary key |
| lead_id | INTEGER | FK → leads.id |
| agent_id | INTEGER | FK → sales_agents.id |
| status | VARCHAR(30) | PENDING, COMPLETED, CANCELLED |
| notes | TEXT | |
| due_at | TIMESTAMPTZ | |
| completed_at | TIMESTAMPTZ | |
| created_at | TIMESTAMPTZ | |
| updated_at | TIMESTAMPTZ | |

---

# 5. Relationships

```text
Customer 1 ── * Lead
Customer 1 ── * Conversation
Lead 1 ── * Conversation
Conversation 1 ── * Message
Lead * ── 1 SalesAgent (assigned)
Lead 1 ── * FollowUp
SalesAgent 1 ── * FollowUp
```

---

# 6. Indexes

Recommended indexes:

- customers.email
- customers.phone
- leads.status
- leads.priority
- leads.customer_id
- leads.assigned_agent_id
- conversations.conversation_uid
- messages.conversation_id
- messages.message_uid

---

# 7. Constraints

- Unique constraints on email and phone where present.
- Foreign keys with appropriate ON DELETE behavior (RESTRICT or SET NULL).
- Check constraints or application-level validation for valid status/priority/intent values.
- Non-null constraints on critical fields (e.g. lead status).

---

# 8. Migration Strategy

Use Alembic.

- All schema changes must go through migrations.
- Initial migration creates the core tables.
- Seed data for development is separate from migrations.

---

# 9. Source of Truth Summary

| Data | Source of Truth |
|------|-----------------|
| Customer | SQL |
| Lead | SQL |
| Conversation | SQL |
| Message | SQL |
| Lead Score / Priority / Status | SQL |
| Follow-up | SQL |
| Sales Assignment | SQL |
| Operational reporting copies | Google Sheets (via n8n) |

**SQL remains the authoritative store for all core lead and conversation information. Google Sheets receives operational copies where useful.**

This database design provides the foundation for the next document:

**`API.md`**, which will define how the React frontend, FastAPI backend, n8n workflows, and external systems communicate using the domain and database model.
