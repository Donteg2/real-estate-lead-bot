# TASK.md

# REAL ESTATE LEAD BOT --- MASTER TASK TRACKER

**Client:** PrimeHomes Realty\
**Project:** REAL ESTATE LEAD BOT\
**Version:** 0.2\
**Status:** Implementation Planning / Foundation\
**Last Updated:** 2026-09-06

------------------------------------------------------------------------

## 1. Purpose

This document is the practical master checklist for building the REAL
ESTATE LEAD BOT.

Use this file to track what has been completed, what is currently being
worked on, and what needs to be done next.

### Status Legend

-   [ ] NOT_STARTED
-   \[\~\] IN_PROGRESS
-   [x] DONE
-   \[!\] BLOCKED
-   \[\>\] REVIEW

------------------------------------------------------------------------

# 2. CURRENT PROJECT STATUS

## Completed Foundation

-   [x] Product requirements documented
-   [x] System architecture documented
-   [x] Database/data model specification documented
-   [x] API specification documented
-   [x] AI specification documented
-   [x] n8n workflow specification documented
-   [x] Engineering standards documented
-   [x] Implementation plan documented
-   [x] Testing specification documented
-   [x] Deployment specification documented
-   [x] Development setup documented
-   [x] Lead qualification specification documented
-   [x] UI/UX specification documented
-   [x] REAL ESTATE LEAD BOT project overview documented
-   [x] Git/GitHub workflow practiced separately
-   [x] GitHub SSH connection tested successfully

## Current Focus

**Next major phase: Project repository and development foundation**

The immediate goal is to move from documentation into the actual project
codebase.

------------------------------------------------------------------------

# 3. PHASE 1 --- PROJECT FOUNDATION

## 3.1 Create GitHub Repository

-   [ ] Create GitHub repository: `real-estate-lead-bot`
-   [ ] Prefer Private visibility during development
-   [ ] Do not initialize with an unnecessary second README
-   [ ] Add repository description
-   [ ] Confirm SSH access
-   [ ] Connect local project to GitHub
-   [ ] Set `main` as default branch

### Git Foundation Commands

``` powershell
git init
git status
git add .
git commit -m "docs: initialize real estate lead bot project"
git branch -M main
git remote add origin git@github.com:YOUR_USERNAME/real-estate-lead-bot.git
git remote -v
git push -u origin main
```

------------------------------------------------------------------------

## 3.2 Repository Structure

Create the initial structure:

``` text
real-estate-lead-bot/
│
├── frontend/
├── backend/
├── n8n/
│   └── workflows/
├── database/
│   ├── migrations/
│   └── seeds/
├── tests/
│   ├── integration/
│   └── e2e/
├── docs/
├── .env.example
├── .gitignore
└── README.md
```

Tasks:

-   [ ] Create `frontend/`
-   [ ] Create `backend/`
-   [ ] Create `n8n/workflows/`
-   [ ] Create `database/migrations/`
-   [ ] Create `database/seeds/`
-   [ ] Create `tests/integration/`
-   [ ] Create `tests/e2e/`
-   [ ] Create `docs/`
-   [ ] Create `.env.example`
-   [ ] Create `.gitignore`
-   [ ] Verify structure
-   [ ] Commit foundation

------------------------------------------------------------------------

# 4. PHASE 2 --- DOCUMENTATION

## Documentation Checklist

-   [x] PRD
-   [x] SAD
-   [x] DOMAIN / domain decisions covered by project specifications
-   [x] DATABASE specification
-   [x] API specification
-   [x] FRONTEND specification
-   [x] AI-SPEC
-   [x] N8N-WORKFLOWS
-   [x] ENGINEERING
-   [x] IMPLEMENTATION
-   [x] TESTING
-   [x] DEPLOYMENT
-   [x] DEPLOYMENT_SPEC
-   [x] DEVELOPMENT_SETUP
-   [x] LEAD_QUALIFICATION_SPEC
-   [x] UI-UX-SPEC
-   [x] REAL ESTATE LEAD BOT overview
-   [x] TASK tracker

### Documentation Quality

-   [ ] Remove conflicting requirements
-   [ ] Confirm endpoint names are consistent
-   [ ] Confirm database fields match API schemas
-   [ ] Confirm AI output matches backend schemas
-   [ ] Confirm qualification rules match tests
-   [ ] Confirm n8n workflows match API behavior
-   [ ] Confirm deployment instructions match actual stack

------------------------------------------------------------------------

# 5. PHASE 3 --- DEVELOPMENT ENVIRONMENT

## 5.1 Prerequisites

-   [ ] Git installed
-   [ ] Python installed
-   [ ] Node.js installed
-   [ ] npm installed
-   [ ] SQL database available
-   [ ] n8n available
-   [ ] AI provider account/API access available
-   [ ] GitHub SSH configured

## 5.2 Environment Variables

-   [ ] Create `.env.example`
-   [ ] Create local `.env`
-   [ ] Confirm `.env` is ignored by Git
-   [ ] Configure database URL
-   [ ] Configure API settings
-   [ ] Configure n8n settings
-   [ ] Configure AI settings
-   [ ] Configure authentication settings
-   [ ] Configure CORS
-   [ ] Configure notification settings

Never commit:

-   API keys
-   passwords
-   JWT secrets
-   database credentials
-   private credentials

------------------------------------------------------------------------

# 6. PHASE 4 --- DATABASE

## 6.1 Database Setup

-   [ ] Select development SQL database
-   [ ] Create development database
-   [ ] Configure database connection
-   [ ] Configure SQLAlchemy
-   [ ] Configure Alembic
-   [ ] Create initial migration
-   [ ] Run migration
-   [ ] Verify tables

## 6.2 Core Data Models

Implement:

-   [ ] Customer
-   [ ] Lead
-   \[Property Requirement
-   [ ] Conversation
-   [ ] Message
-   [ ] Follow-up
-   [ ] Qualification result/history
-   [ ] User/Sales Agent
-   [ ] Audit/event records where required

## 6.3 Lead Fields

Confirm support for:

-   [ ] Name
-   [ ] Email
-   [ ] Phone
-   [ ] Preferred contact method
-   [ ] Property type
-   [ ] Bedrooms
-   [ ] Location
-   [ ] Minimum budget
-   [ ] Maximum budget
-   [ ] Currency
-   [ ] Intent
-   [ ] Timeline
-   [ ] Lead status
-   [ ] Priority
-   [ ] Qualification score
-   [ ] Qualification reason
-   [ ] Created timestamp
-   [ ] Updated timestamp

## 6.4 Database Quality

-   [ ] Add primary keys
-   [ ] Add foreign keys
-   [ ] Add required constraints
-   [ ] Add indexes for important searches
-   [ ] Add timestamps
-   [ ] Test migrations
-   [ ] Test rollback strategy
-   [ ] Seed development data

------------------------------------------------------------------------

# 7. PHASE 5 --- FASTAPI BACKEND

## 7.1 Backend Foundation

-   [ ] Create Python virtual environment
-   [ ] Create FastAPI application
-   [ ] Configure application settings
-   [ ] Configure database
-   [ ] Configure logging
-   [ ] Add health endpoint
-   [ ] Add API versioning
-   [ ] Add error handling
-   [ ] Add CORS configuration

## 7.2 API Endpoints

Implement and test:

### Chat

-   [ ] `POST /api/v1/chat`

### Leads

-   [ ] `POST /api/v1/leads`
-   [ ] `GET /api/v1/leads`
-   [ ] `GET /api/v1/leads/{lead_id}`
-   [ ] `PATCH /api/v1/leads/{lead_id}`

### Follow-ups

-   [ ] `GET /api/v1/leads/{lead_id}/follow-ups`
-   [ ] `POST /api/v1/leads/{lead_id}/follow-ups`

### Conversations

-   [ ] `GET /api/v1/conversations/{conversation_id}`
-   [ ] `GET /api/v1/conversations/{conversation_id}/messages`

## 7.3 Backend Services

Create separate services for:

-   [ ] Lead service
-   [ ] Customer service
-   [ ] Conversation service
-   [ ] Qualification service
-   [ ] Follow-up service
-   [ ] Notification service
-   [ ] AI service
-   [ ] Authentication service

## 7.4 Backend Rules

-   [ ] Validate all incoming data
-   [ ] Never trust raw AI output
-   [ ] Keep business rules deterministic
-   [ ] Prevent unauthorized access
-   [ ] Handle duplicate requests
-   [ ] Return consistent error responses
-   [ ] Log important failures
-   [ ] Do not expose secrets

------------------------------------------------------------------------

# 8. PHASE 6 --- AI IMPLEMENTATION

## 8.1 AI Extraction

Implement extraction for:

-   [ ] Customer name
-   [ ] Email
-   [ ] Phone
-   [ ] Preferred contact method
-   [ ] Property type
-   [ ] Bedrooms
-   [ ] Location
-   [ ] Budget
-   [ ] Currency
-   [ ] Intent
-   [ ] Timeline

## 8.2 Intent Classification

Support:

-   [ ] `BUY_PROPERTY`
-   [ ] `RENT_PROPERTY`
-   [ ] `BUY_LAND`
-   [ ] `SELL_PROPERTY`
-   [ ] `GENERAL_ENQUIRY`

## 8.3 Timeline Classification

Support:

-   [ ] `IMMEDIATE`
-   [ ] `WITHIN_1_MONTH`
-   [ ] `WITHIN_3_MONTHS`
-   [ ] `RESEARCHING`
-   [ ] `UNKNOWN`

## 8.4 AI Safety

-   [ ] Validate structured AI output
-   [ ] Reject invalid fields
-   [ ] Handle missing values
-   [ ] Never invent customer details
-   [ ] Never invent property availability
-   [ ] Never allow AI to override business rules
-   [ ] Add fallback response for AI failure
-   [ ] Add prompt/version tracking where appropriate

------------------------------------------------------------------------

# 9. PHASE 7 --- LEAD QUALIFICATION

Implement deterministic scoring.

## Scoring Factors

-   [ ] Intent Strength --- 20
-   [ ] Budget --- 20
-   [ ] Timeline --- 20
-   [ ] Requirement Completeness --- 15
-   [ ] Location Specificity --- 15
-   [ ] Engagement --- 10

**Maximum score: 100**

## Priority Thresholds

-   [ ] 80--100 → HOT
-   [ ] 50--79 → WARM
-   [ ] 0--49 → COLD

## Qualification Rules

-   [ ] Missing information receives appropriate treatment
-   [ ] Invalid data does not receive points
-   [ ] Qualification reason is generated/stored
-   [ ] Qualification result is stored in SQL
-   [ ] Lead can be re-qualified
-   [ ] Qualification history can be tracked
-   [ ] Hot leads can trigger notifications
-   [ ] Qualification tests pass

------------------------------------------------------------------------

# 10. PHASE 8 --- N8N AUTOMATION

## WF-001 --- Lead Intake

-   [ ] Receive webhook/request
-   [ ] Validate input
-   [ ] Normalize data
-   [ ] Send relevant information to AI
-   [ ] Validate AI output
-   [ ] Send structured data to backend/database
-   [ ] Return appropriate response

## WF-002 --- Lead Qualification

-   [ ] Receive structured lead
-   [ ] Trigger qualification
-   [ ] Apply deterministic scoring
-   [ ] Store score
-   [ ] Store priority
-   [ ] Store qualification reason

## WF-003 --- Sales Notification

-   [ ] Detect important lead events
-   [ ] Detect HOT leads
-   [ ] Send notification
-   [ ] Log notification result
-   [ ] Handle notification failure

## WF-004 --- Google Sheets Sync

-   [ ] Sync approved lead data
-   [ ] Prevent duplicate rows
-   [ ] Handle API failures
-   [ ] Keep SQL as source of truth

## WF-005 --- Follow-up

-   [ ] Identify follow-up due
-   [ ] Trigger notification/reminder
-   [ ] Record follow-up result
-   [ ] Prevent duplicate execution

## Workflow Reliability

-   [ ] Add error branches
-   [ ] Add retry logic where appropriate
-   [ ] Add idempotency where needed
-   [ ] Log failures
-   [ ] Test duplicate events
-   [ ] Test external-service failure

------------------------------------------------------------------------

# 11. PHASE 9 --- FRONTEND

## 11.1 Customer Experience

-   [ ] Create React application
-   [ ] Create chat page
-   [ ] Create message list
-   [ ] Create message input
-   [ ] Create send button
-   [ ] Add typing/loading state
-   [ ] Add error state
-   [ ] Add contact information collection
-   [ ] Add confirmation state
-   [ ] Connect to `/chat`

## 11.2 Sales Dashboard

-   [ ] Create dashboard layout
-   [ ] Display lead metrics
-   [ ] Display lead table
-   [ ] Add search
-   [ ] Add filters
-   [ ] Add priority filter
-   [ ] Add status filter
-   [ ] Add lead detail page/panel
-   [ ] Display qualification score
-   [ ] Display customer requirements
-   [ ] Display conversation history
-   [ ] Display follow-ups
-   [ ] Add lead status update

## 11.3 Frontend Rules

-   [ ] Frontend does not calculate business-critical qualification
-   [ ] Frontend does not connect directly to SQL
-   [ ] Frontend does not expose AI credentials
-   [ ] Frontend displays backend decisions
-   [ ] Mobile layout works
-   [ ] Desktop layout works
-   [ ] Accessibility requirements are addressed

------------------------------------------------------------------------

# 12. PHASE 10 --- AUTHENTICATION & SECURITY

## Roles

-   [ ] CUSTOMER
-   [ ] SALES_AGENT
-   [ ] SALES_MANAGER
-   [ ] ADMIN

## Security Tasks

-   [ ] Implement authentication
-   [ ] Implement authorization
-   [ ] Protect sales endpoints
-   [ ] Protect admin endpoints
-   [ ] Secure n8n webhooks
-   [ ] Configure CORS
-   [ ] Add rate limiting
-   [ ] Validate input
-   [ ] Sanitize output
-   [ ] Protect secrets
-   [ ] Review logs for sensitive information
-   [ ] Verify HTTPS requirements for production

------------------------------------------------------------------------

# 13. PHASE 11 --- NOTIFICATIONS

-   [ ] Select notification channel
-   [ ] Configure credentials
-   [ ] Create new-lead notification
-   [ ] Create HOT-lead notification
-   [ ] Create follow-up notification
-   [ ] Add failure handling
-   [ ] Test delivery
-   [ ] Prevent duplicate alerts

------------------------------------------------------------------------

# 14. PHASE 12 --- TESTING

## Unit Tests

-   [ ] Qualification scoring
-   [ ] Validation
-   [ ] Data normalization
-   [ ] Business rules
-   [ ] Service functions

## API Tests

-   [ ] Chat endpoint
-   [ ] Lead creation
-   [ ] Lead retrieval
-   [ ] Lead update
-   [ ] Follow-ups
-   [ ] Conversations
-   [ ] Authentication
-   [ ] Authorization
-   [ ] Error responses

## AI Tests

-   [ ] Apartment enquiry
-   [ ] Land enquiry
-   [ ] Rental enquiry
-   [ ] General enquiry
-   [ ] Missing information
-   [ ] Ambiguous input
-   [ ] Invalid output
-   [ ] Hallucination resistance

## n8n Tests

-   [ ] Lead intake
-   [ ] AI processing
-   [ ] Qualification
-   [ ] Database storage
-   [ ] Notification
-   [ ] Sheets sync
-   [ ] Follow-up
-   [ ] Error path
-   [ ] Retry behavior
-   [ ] Duplicate event

## End-to-End Test

Example:

``` text
Customer
   ↓
React Chat
   ↓
FastAPI
   ↓
n8n
   ↓
AI
   ↓
Validation
   ↓
Qualification
   ↓
SQL
   ↓
Notification
   ↓
Sales Dashboard
```

-   [ ] Complete end-to-end flow passes

------------------------------------------------------------------------

# 15. PHASE 13 --- SAMPLE LEAD TEST

Use a sample lead based on the project requirements:

**Name:** Amina Yusuf\
**Phone:** 08000000000\
**Email:** amina@example.com

**Message:**

> "I am looking for a 3-bedroom apartment around Lekki. My budget is
> about ₦80 million and I want to buy within the next two months."

Expected extracted information:

-   [ ] Property type = apartment
-   [ ] Bedrooms = 3
-   [ ] Location = Lekki
-   [ ] Budget = ₦80,000,000
-   [ ] Intent = buying
-   [ ] Timeline = within approximately 3 months
-   [ ] Contact information captured

Expected result:

-   [ ] Lead created
-   [ ] Qualification calculated
-   [ ] Priority displayed
-   [ ] Lead stored in SQL
-   [ ] Sales notification triggered according to rules
-   [ ] Customer receives appropriate response

------------------------------------------------------------------------

# 16. PHASE 14 --- DEPLOYMENT

## Development

-   [ ] Local frontend works
-   [ ] Local backend works
-   [ ] Local database works
-   [ ] Local n8n works
-   [ ] AI integration works

## Staging

-   [ ] Deploy frontend
-   [ ] Deploy backend
-   [ ] Deploy database
-   [ ] Deploy/configure n8n
-   [ ] Configure secrets
-   [ ] Run migrations
-   [ ] Run integration tests
-   [ ] Run E2E tests
-   [ ] Perform release smoke test

## Production

-   [ ] Configure production domain
-   [ ] Configure HTTPS
-   [ ] Configure production database
-   [ ] Configure backups
-   [ ] Configure n8n
-   [ ] Configure AI provider
-   [ ] Configure notifications
-   [ ] Configure monitoring
-   [ ] Configure logging
-   [ ] Configure rate limiting
-   [ ] Run migrations
-   [ ] Run smoke tests
-   [ ] Confirm rollback plan

------------------------------------------------------------------------

# 17. PHASE 15 --- MONITORING & OPERATIONS

-   [ ] Add application health checks
-   [ ] Monitor FastAPI errors
-   [ ] Monitor database errors
-   [ ] Monitor n8n workflow failures
-   [ ] Monitor AI failures
-   [ ] Monitor notification failures
-   [ ] Monitor webhook failures
-   [ ] Configure alerts
-   [ ] Configure database backups
-   [ ] Test backup restoration
-   [ ] Document incident response
-   [ ] Document rollback procedure

------------------------------------------------------------------------

# 18. PHASE 16 --- FINAL SECURITY REVIEW

Before production:

-   [ ] No secrets committed to Git
-   [ ] `.env` ignored
-   [ ] Authentication tested
-   [ ] Authorization tested
-   [ ] API input validation tested
-   [ ] Webhook security tested
-   [ ] CORS reviewed
-   [ ] Rate limiting reviewed
-   [ ] Sensitive logging reviewed
-   [ ] Database access restricted
-   [ ] Production HTTPS enabled
-   [ ] Backup strategy verified

------------------------------------------------------------------------

# 19. PHASE 17 --- FINAL MVP ACCEPTANCE

The MVP is ready when:

### Customer

-   [ ] Customer can start a conversation
-   [ ] Customer can submit a property enquiry
-   [ ] Bot responds appropriately
-   [ ] Missing information is collected
-   [ ] Contact information can be captured

### AI

-   [ ] AI understands enquiries
-   [ ] AI extracts structured information
-   [ ] AI output is validated
-   [ ] AI does not invent information
-   [ ] AI failure has a fallback

### Backend

-   [ ] API works
-   [ ] Validation works
-   [ ] Leads are stored
-   [ ] Conversations are stored
-   [ ] Qualification works
-   [ ] Authentication works
-   [ ] Authorization works

### Automation

-   [ ] n8n processes leads
-   [ ] Notifications work
-   [ ] Sheets synchronization works if enabled
-   [ ] Follow-up automation works
-   [ ] Error handling works

### Sales

-   [ ] Sales dashboard works
-   [ ] Leads can be searched
-   [ ] Leads can be filtered
-   [ ] Lead details can be viewed
-   [ ] Qualification can be viewed
-   [ ] Conversations can be viewed
-   [ ] Follow-ups can be managed
-   [ ] Lead status can be updated

### Quality

-   [ ] Automated tests pass
-   [ ] End-to-end test passes
-   [ ] Security review passes
-   [ ] Deployment smoke test passes
-   [ ] Documentation matches implementation

------------------------------------------------------------------------

# 20. GIT WORKFLOW

Use small, focused commits.

Recommended branch examples:

``` text
main
feature/backend-foundation
feature/database
feature/ai-extraction
feature/n8n-lead-workflow
feature/frontend-chat
feature/sales-dashboard
feature/authentication
feature/testing
```

Basic workflow:

``` powershell
git status
git checkout -b feature/name
```

Make changes, then:

``` powershell
git add .
git status
git commit -m "feat: implement lead capture"
git push -u origin feature/name
```

Before merging:

``` powershell
git checkout main
git pull origin main
```

Then merge through a Pull Request where practical.

### Commit Style

Examples:

``` text
docs: update implementation documentation
feat: add lead creation endpoint
feat: implement qualification scoring
feat: add customer chat interface
feat: add n8n lead workflow
fix: handle invalid AI output
test: add qualification tests
chore: configure development environment
```

------------------------------------------------------------------------

# 21. CURRENT NEXT ACTIONS

Do these in order.

## NEXT 1 --- Create/prepare project folder

-   [ ] Create the local `real-estate-lead-bot` folder
-   [ ] Put the approved documentation into the project
-   [ ] Confirm filenames
-   [ ] Add `.gitignore`
-   [ ] Add `.env.example`

## NEXT 2 --- Initialize Git

-   [ ] `git init`
-   [ ] `git status`
-   [ ] `git add .`
-   [ ] Initial documentation commit

## NEXT 3 --- Create GitHub Repository

-   [ ] Create `real-estate-lead-bot`
-   [ ] Connect `origin`
-   [ ] Push `main`

## NEXT 4 --- Build Backend Foundation

-   [ ] Create FastAPI project
-   [ ] Create virtual environment
-   [ ] Install dependencies
-   [ ] Create health endpoint
-   [ ] Configure settings
-   [ ] Configure database

## NEXT 5 --- Build Database

-   [ ] Create models
-   [ ] Create migration
-   [ ] Run migration
-   [ ] Seed test lead

## NEXT 6 --- Build First API

-   [ ] Implement `POST /api/v1/leads`
-   [ ] Test with sample lead
-   [ ] Store lead in SQL

## NEXT 7 --- Build First n8n Workflow

Start simple:

``` text
Webhook
   ↓
Set / Edit Fields
   ↓
AI Processing
   ↓
IF
   ↓
Lead Storage
   ↓
Notification
```

This follows the project's intended incremental approach: build and
verify one working slice before expanding the system.

------------------------------------------------------------------------

# 22. IMPORTANT PROJECT RULES

1.  **AI extracts information; deterministic application logic makes
    business decisions.**
2.  **SQL is the primary source of truth.**
3.  **Google Sheets is a supporting operational layer.**
4.  **n8n is for orchestration and integrations, not the entire
    backend.**
5.  **Frontend presents backend decisions.**
6.  **Never commit secrets.**
7.  **Never invent customer or property information.**
8.  **Every important business rule must be testable.**
9.  **Build incrementally instead of trying to build the entire system
    at once.**
10. **A working simple workflow is better than a large untested
    workflow.**
11. **Keep documentation and implementation synchronized.**
12. **Do not mark a task DONE until it has been implemented and
    verified.**

------------------------------------------------------------------------

# 23. DEFINITION OF DONE

A task can be marked `[x] DONE` only when:

-   [ ] Implementation is complete
-   [ ] Relevant tests pass
-   [ ] Error handling has been considered
-   [ ] Security implications have been reviewed
-   [ ] Documentation is updated if necessary
-   [ ] Git changes are committed
-   [ ] The feature works in the intended environment

------------------------------------------------------------------------

# 24. PROJECT END STATE

The completed REAL ESTATE LEAD BOT should demonstrate a complete
business automation:

``` text
CUSTOMER
   ↓
REACT CHAT
   ↓
FASTAPI
   ↓
N8N
   ↓
AI EXTRACTION
   ↓
VALIDATION
   ↓
DETERMINISTIC QUALIFICATION
   ↓
SQL DATABASE
   ↓
SALES NOTIFICATION
   ↓
SALES DASHBOARD
   ↓
FOLLOW-UP
   ↓
LEAD CONVERSION
```

The final system should not merely be an n8n workflow.

It should be a complete, reliable software system that solves the
real-estate lead-management problem.
