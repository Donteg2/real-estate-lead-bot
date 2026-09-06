# DEPLOYMENT SPECIFICATION

**Project:** REAL ESTATE LEAD BOT\
**Client:** PrimeHomes Realty\
**Version:** 0.1\
**Status:** Draft / Implementation Ready

------------------------------------------------------------------------

## 1. Purpose

This document defines the technical deployment requirements for the REAL
ESTATE LEAD BOT.

It explains how the system moves from development to staging and
production, how each component is configured, how services communicate,
how secrets are managed, and how the system is monitored, backed up,
recovered, and rolled back.

The deployment architecture must preserve the project's core separation
of responsibilities:

-   **React** = presentation and user interaction
-   **FastAPI** = API and application boundary
-   **AI** = language understanding and structured extraction
-   **n8n** = workflow orchestration and integrations
-   **SQL database** = primary source of truth
-   **Google Sheets** = supporting operational layer

------------------------------------------------------------------------

# 2. Deployment Goals

The deployment must provide:

-   Reliable access to the customer-facing application
-   Secure communication between services
-   Separate development, staging, and production environments
-   Secure handling of credentials and API keys
-   Database persistence and backups
-   n8n workflow reliability
-   AI provider failure handling
-   Application health monitoring
-   Safe deployments and rollback capability
-   Reproducible configuration
-   Minimal downtime during releases

------------------------------------------------------------------------

# 3. System Architecture

The production deployment follows this logical flow:

``` text
CUSTOMER
   |
   v
REACT FRONTEND
   |
   v
FASTAPI BACKEND
   |
   +--------------------+
   |                    |
   v                    v
SQL DATABASE           n8n
                        |
              +---------+---------+
              |         |         |
              v         v         v
             AI       Sheets   Notifications
```

The frontend must never connect directly to:

-   SQL database
-   n8n
-   AI provider
-   Google Sheets APIs using private credentials

All sensitive integrations must be accessed through backend services or
controlled n8n workflows.

------------------------------------------------------------------------

# 4. Environments

The project should use three environments.

## 4.1 Development

Purpose:

-   Local development
-   Feature implementation
-   Unit testing
-   Workflow development
-   AI prompt development

Typical services:

``` text
React
FastAPI
SQL Database
n8n
AI Provider
```

Development data must not be treated as production data.

------------------------------------------------------------------------

## 4.2 Staging

Purpose:

-   Integration testing
-   End-to-end testing
-   Release validation
-   n8n workflow testing
-   AI behavior testing
-   Production-like configuration checks

Staging should resemble production as closely as practical.

No production customer data should be copied into staging unless it has
been appropriately anonymized and authorized.

------------------------------------------------------------------------

## 4.3 Production

Purpose:

-   Real customer interactions
-   Real lead processing
-   Sales notifications
-   Lead storage
-   Follow-up operations

Production must use:

-   HTTPS
-   Protected credentials
-   Persistent database storage
-   Database backups
-   Monitoring
-   Error logging
-   Rate limiting
-   Controlled deployment procedures

------------------------------------------------------------------------

# 5. Component Deployment

## 5.1 React Frontend

Responsibilities:

-   Customer chat interface
-   Sales dashboard
-   Lead information display
-   API communication

Deployment requirements:

-   Build the React application for production
-   Serve static assets through a production web server or hosting
    platform
-   Configure the production API base URL
-   Enable HTTPS
-   Do not include private secrets in frontend environment variables

Example configuration:

``` text
VITE_API_BASE_URL=https://api.example.com/api/v1
```

Any variable exposed to a browser must be considered public.

------------------------------------------------------------------------

# 6. FastAPI Backend

The FastAPI service is the main application/API boundary.

Responsibilities:

-   API endpoints
-   Input validation
-   Authentication
-   Authorization
-   Application services
-   Database interaction
-   Business-rule enforcement
-   Request tracing
-   Error handling

Production requirements:

-   Run behind HTTPS
-   Use a production ASGI server
-   Configure worker/process strategy appropriately
-   Use environment variables for configuration
-   Connect to the production SQL database
-   Never expose database credentials to the frontend

Example runtime concept:

``` text
Internet
   |
HTTPS
   |
Reverse Proxy
   |
FastAPI Application
   |
SQL Database
```

------------------------------------------------------------------------

# 7. SQL Database Deployment

The SQL database is the authoritative source of truth.

It stores:

-   Customers
-   Leads
-   Conversations
-   Messages
-   Lead scores
-   Follow-ups
-   Sales agents

Requirements:

-   Persistent storage
-   Authentication
-   Restricted network access
-   Automated backups
-   Migration support
-   Indexes and constraints
-   Monitoring
-   Recovery procedure

Database credentials must never be committed to Git.

------------------------------------------------------------------------

# 8. Database Migration Strategy

Database schema changes must be managed through migrations.

Deployment process:

``` text
Code Change
    |
    v
Migration Created
    |
    v
Migration Tested
    |
    v
Staging
    |
    v
Production
```

Rules:

1.  Never manually modify production tables without a documented
    emergency procedure.
2.  Every schema change must have a migration.
3.  Migrations must be tested in staging.
4.  Backups should be verified before risky production migrations.
5.  Destructive migrations require additional review.

------------------------------------------------------------------------

# 9. n8n Deployment

n8n is the workflow orchestration layer.

It handles:

-   Lead enquiry processing
-   AI processing
-   Lead qualification workflow orchestration
-   Notifications
-   Google Sheets synchronization
-   Follow-up automation
-   Error handling
-   Scheduled jobs

Production requirements:

-   Persistent n8n data
-   Secure credentials
-   HTTPS for public webhooks
-   Protected editor access
-   Reliable execution storage
-   Workflow error monitoring
-   Controlled workflow deployment

n8n must not become the replacement for the application's core backend.

Critical business rules should remain deterministic and testable outside
AI prompts where practical.

------------------------------------------------------------------------

# 10. AI Provider Deployment

The AI service may be hosted by an external provider.

Requirements:

-   API key stored as a secret
-   Structured output validation
-   Timeout handling
-   Retry strategy where appropriate
-   Provider error handling
-   Logging without exposing sensitive customer data

AI must not be trusted as the source of truth.

The system must validate AI-generated structured data before storing it.

AI must not invent:

-   Customer information
-   Property availability
-   Property prices
-   Agent information
-   Business policies

------------------------------------------------------------------------

# 11. Google Sheets Deployment

Google Sheets is a supporting operational layer.

It may be used for:

-   Sales visibility
-   Operational reporting
-   Lightweight exports
-   Supporting workflows

It must not replace the SQL database as the primary source of truth.

If synchronization fails:

``` text
SQL DATABASE
     |
     X
Google Sheets
```

The lead must remain safely stored in SQL.

The synchronization workflow should retry or record the failure for
later recovery.

------------------------------------------------------------------------

# 12. Notification Services

The system may use email or another approved notification channel.

Notifications may be triggered for:

-   HOT leads
-   New qualified leads
-   Assigned leads
-   Follow-up reminders
-   Workflow failures

Notification failure must not cause the primary lead record to be lost.

Example:

``` text
Lead Created
     |
     v
SQL Saved
     |
     v
Notification Attempt
     |
   +---+---+
   |       |
Success   Failure
           |
           v
       Retry / Log
```

------------------------------------------------------------------------

# 13. Domain and HTTPS

Production services should use dedicated HTTPS endpoints.

Example:

``` text
https://primehomes.example.com
https://api.primehomes.example.com
https://n8n.primehomes.example.com
```

The exact domains depend on the final hosting configuration.

Requirements:

-   TLS certificate
-   HTTPS redirect
-   Secure cookies where applicable
-   Valid CORS configuration
-   No sensitive data sent over plain HTTP

------------------------------------------------------------------------

# 14. Reverse Proxy

A reverse proxy may sit in front of the backend and n8n.

Responsibilities may include:

-   TLS termination
-   Request routing
-   Security headers
-   Rate limiting
-   Access control
-   Compression
-   Static asset handling where applicable

Conceptually:

``` text
Internet
   |
   v
Reverse Proxy
   |
   +------> React
   |
   +------> FastAPI
   |
   +------> n8n
```

------------------------------------------------------------------------

# 15. Environment Variables

Configuration must be externalized.

Example `.env.example`:

``` env
APP_ENV=development
APP_NAME=real-estate-lead-bot

DATABASE_URL=

API_BASE_URL=

N8N_BASE_URL=
N8N_WEBHOOK_SECRET=

AI_API_KEY=
AI_MODEL=

GOOGLE_SHEETS_CREDENTIALS=

JWT_SECRET=

CORS_ORIGINS=
```

The real `.env` file must never be committed.

Git must ignore:

``` text
.env
.env.*
```

while allowing:

``` text
.env.example
```

------------------------------------------------------------------------

# 16. Secret Management

Secrets include:

-   Database passwords
-   AI API keys
-   n8n credentials
-   Google credentials
-   JWT signing secrets
-   SMTP credentials
-   Third-party API keys

Rules:

1.  Never commit secrets to Git.
2.  Never place private credentials in React code.
3.  Never send private credentials to customers.
4.  Use environment variables or a dedicated secret manager.
5.  Rotate compromised credentials immediately.
6.  Restrict access according to environment and role.

------------------------------------------------------------------------

# 17. CORS

The FastAPI backend must allow only approved frontend origins.

Development example:

``` text
http://localhost:5173
```

Production example:

``` text
https://primehomes.example.com
```

Do not use unrestricted CORS in production unless there is a documented
reason.

------------------------------------------------------------------------

# 18. API Security

Production API security should include:

-   HTTPS
-   Authentication for protected operations
-   Authorization by role
-   Input validation
-   Rate limiting
-   Request size limits
-   Secure error responses
-   Request IDs
-   Logging
-   Protection against duplicate requests where applicable

Customer chat may support an anonymous conversation flow, but
administrative and sales operations must be protected.

------------------------------------------------------------------------

# 19. n8n Webhook Security

Public n8n webhooks must be protected.

Possible controls:

-   Shared secret
-   Signature validation
-   Authentication
-   IP restrictions where appropriate
-   Rate limiting
-   Payload validation

Webhook credentials must not be embedded in frontend source code.

------------------------------------------------------------------------

# 20. Health Checks

The backend should expose a health endpoint.

Example:

``` text
GET /health
```

A deeper readiness check may verify:

-   Application availability
-   Database connectivity
-   Required dependencies

Health checks should be used by the hosting environment and monitoring
system.

------------------------------------------------------------------------

# 21. Logging

Production logs should capture:

-   Timestamp
-   Service
-   Log level
-   Request ID
-   Endpoint/workflow
-   Execution result
-   Error information
-   Processing duration where useful

Do not log:

-   Passwords
-   API keys
-   Access tokens
-   Full sensitive customer information unnecessarily
-   Private credentials

Example:

``` text
INFO request_id=abc123 endpoint=/api/v1/chat status=200 duration=1.24s
```

------------------------------------------------------------------------

# 22. Monitoring

Monitor at minimum:

### Backend

-   API availability
-   Error rate
-   Response time
-   CPU/memory
-   Database connection failures

### n8n

-   Workflow failures
-   Execution duration
-   Failed executions
-   Webhook errors

### Database

-   Availability
-   Storage
-   Connections
-   Query performance
-   Backup status

### AI

-   Provider failures
-   Timeouts
-   Invalid structured responses
-   Usage/cost where available

------------------------------------------------------------------------

# 23. Alerting

Alerts should be configured for important failures.

Examples:

-   Backend unavailable
-   Database unavailable
-   Repeated n8n workflow failures
-   AI provider outage
-   Notification failure
-   Backup failure
-   High error rate
-   High resource usage

Alerts should be actionable and avoid unnecessary noise.

------------------------------------------------------------------------

# 24. Backup Strategy

The production SQL database must be backed up regularly.

Backup requirements:

-   Automated backups
-   Retention policy
-   Secure storage
-   Backup monitoring
-   Periodic restore testing

Backups should be stored separately from the primary database
environment where practical.

------------------------------------------------------------------------

# 25. Disaster Recovery

If the production database or service fails:

``` text
Failure
   |
   v
Detect
   |
   v
Assess
   |
   v
Restore Service
   |
   v
Restore Database if Required
   |
   v
Verify
   |
   v
Resume Operations
```

Recovery procedures must be documented and tested.

Important recovery targets:

-   **RPO:** acceptable amount of data that may be lost
-   **RTO:** acceptable time to restore service

Exact RPO/RTO targets should be defined before production launch.

------------------------------------------------------------------------

# 26. Deployment Process

Standard release flow:

``` text
Developer
   |
   v
Feature Branch
   |
   v
Tests
   |
   v
Pull Request
   |
   v
Code Review
   |
   v
Merge
   |
   v
Staging
   |
   v
Integration / E2E Tests
   |
   v
Production Approval
   |
   v
Production Deployment
   |
   v
Smoke Test
   |
   v
Monitoring
```

------------------------------------------------------------------------

# 27. Backend Deployment

Recommended sequence:

1.  Build application.
2.  Install locked dependencies.
3.  Configure environment variables.
4.  Run database migrations.
5.  Start FastAPI.
6.  Verify health endpoint.
7.  Run smoke tests.
8.  Monitor logs and metrics.

------------------------------------------------------------------------

# 28. Frontend Deployment

Recommended sequence:

1.  Install dependencies.
2.  Run lint/tests.
3.  Build React application.
4.  Configure production API URL.
5.  Deploy static assets.
6.  Verify application loads.
7.  Test chat flow.
8.  Verify API communication.

------------------------------------------------------------------------

# 29. n8n Workflow Deployment

Before production activation:

-   Validate workflow structure
-   Verify credentials
-   Verify webhook URLs
-   Test AI node
-   Test database operations
-   Test notification nodes
-   Test error paths
-   Confirm environment-specific values
-   Run staging execution
-   Enable production workflow

Production workflows should be version controlled or exported and backed
up according to the project's Git strategy.

------------------------------------------------------------------------

# 30. Rollback Strategy

If a deployment causes a critical failure:

``` text
Production Failure
       |
       v
Stop / Disable Faulty Release
       |
       v
Restore Previous Application Version
       |
       v
Rollback Database Migration if Safe
       |
       v
Verify Health
       |
       v
Monitor
```

Database rollback must be handled carefully because application rollback
and schema rollback are not always safely reversible.

Prefer backward-compatible database changes when possible.

------------------------------------------------------------------------

# 31. Production Smoke Test

After deployment verify:

-   [ ] Frontend loads
-   [ ] Customer can start a conversation
-   [ ] Customer can send a message
-   [ ] FastAPI receives the request
-   [ ] n8n workflow executes
-   [ ] AI extraction works
-   [ ] Lead is stored in SQL
-   [ ] Qualification runs
-   [ ] Customer receives a response
-   [ ] Sales notification works
-   [ ] Google Sheets synchronization works
-   [ ] Conversation history is stored
-   [ ] Follow-up functionality works

------------------------------------------------------------------------

# 32. Deployment Failure Handling

Every major service must fail safely.

### AI unavailable

The system should:

-   Record the failure
-   Avoid inventing a response
-   Retry where appropriate
-   Return a safe fallback response

### Database unavailable

The system should:

-   Fail gracefully
-   Log the error
-   Avoid pretending the lead was stored
-   Alert operations

### n8n unavailable

The API should:

-   Detect the integration failure
-   Log the failure
-   Avoid silently losing the customer request
-   Provide an appropriate fallback or retry mechanism

### Google Sheets unavailable

The lead should remain available in SQL.

### Notification unavailable

The lead should remain stored and the notification should be retried or
flagged.

------------------------------------------------------------------------

# 33. CI/CD

A future CI/CD pipeline should perform:

``` text
Push / Pull Request
        |
        v
Lint
        |
        v
Unit Tests
        |
        v
API Tests
        |
        v
Build
        |
        v
Integration Tests
        |
        v
Deploy Staging
        |
        v
E2E Tests
        |
        v
Production Approval
        |
        v
Deploy Production
```

Production deployment should require successful automated checks.

------------------------------------------------------------------------

# 34. Deployment Checklist

## Before Deployment

-   [ ] Tests pass
-   [ ] Documentation updated
-   [ ] Environment variables verified
-   [ ] Secrets verified
-   [ ] Database backup verified
-   [ ] Migration reviewed
-   [ ] n8n workflows tested
-   [ ] AI integration tested
-   [ ] Release version identified

## During Deployment

-   [ ] Deploy application
-   [ ] Run migrations
-   [ ] Deploy/activate workflows
-   [ ] Verify health checks
-   [ ] Monitor logs

## After Deployment

-   [ ] Run smoke tests
-   [ ] Test customer chat
-   [ ] Test lead creation
-   [ ] Test qualification
-   [ ] Test notification
-   [ ] Verify database
-   [ ] Verify n8n
-   [ ] Verify monitoring
-   [ ] Confirm release success

------------------------------------------------------------------------

# 35. Deployment Task Tracker

  ID        Task                                Priority   Status
  --------- ----------------------------------- ---------- -------------
  DEP-001   Define deployment environments      High       NOT_STARTED
  DEP-002   Choose hosting architecture         High       NOT_STARTED
  DEP-003   Configure production database       High       NOT_STARTED
  DEP-004   Configure backend deployment        High       NOT_STARTED
  DEP-005   Configure frontend deployment       High       NOT_STARTED
  DEP-006   Configure n8n production instance   High       NOT_STARTED
  DEP-007   Configure environment variables     High       NOT_STARTED
  DEP-008   Configure HTTPS/domain              High       NOT_STARTED
  DEP-009   Configure monitoring                Medium     NOT_STARTED
  DEP-010   Configure database backups          High       NOT_STARTED
  DEP-011   Configure CI/CD                     Medium     NOT_STARTED
  DEP-012   Test rollback procedure             Medium     NOT_STARTED
  DEP-013   Complete production smoke test      High       NOT_STARTED

------------------------------------------------------------------------

# 36. Deployment Definition of Done

Deployment is considered complete when:

-   [ ] Production environment is configured
-   [ ] React application is accessible
-   [ ] FastAPI API is accessible
-   [ ] SQL database is persistent
-   [ ] n8n workflows are operational
-   [ ] AI integration is operational
-   [ ] Secrets are protected
-   [ ] HTTPS is enabled
-   [ ] Monitoring is active
-   [ ] Backups are configured
-   [ ] Recovery procedure is documented
-   [ ] Smoke tests pass
-   [ ] Rollback procedure is documented
-   [ ] Documentation reflects the final deployment architecture

------------------------------------------------------------------------

# 37. Core Deployment Rules

1.  Production credentials must never be committed to Git.
2.  Production must use HTTPS.
3.  SQL is the primary source of truth.
4.  Google Sheets is not the primary database.
5.  React must not access private services directly.
6.  n8n must not replace FastAPI application logic.
7.  AI output must be validated.
8.  Critical business rules must be deterministic.
9.  Production deployments must be tested.
10. Database changes must use migrations.
11. Backups must be tested, not merely configured.
12. Every production release must have a rollback strategy.

------------------------------------------------------------------------

## Document Status

**Document:** DEPLOYMENT_SPEC.md\
**Version:** 0.1\
**Status:** Draft / Implementation Ready\
**Owner:** Project Engineering Team\
**Related Documents:** PRD.md, SAD.md, DATABASE.md, API.md,
N8N-WORKFLOWS.md, ENGINEERING.md, IMPLEMENTATION.md, TESTING.md
