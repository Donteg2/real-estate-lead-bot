# DEVELOPMENT SETUP

**Project:** REAL ESTATE LEAD BOT\
**Client:** PrimeHomes Realty\
**Version:** 0.1\
**Status:** Draft / Implementation Ready

------------------------------------------------------------------------

## 1. Purpose

This document defines the local development environment and setup
procedure for the REAL ESTATE LEAD BOT.

The goal is to make development reproducible so that a developer can
clone the repository, configure the required services, install
dependencies, and run the system locally.

The development environment contains:

``` text
React Frontend
      |
      v
FastAPI Backend
      |
      +----------------+
      |                |
      v                v
SQL Database         n8n
                       |
                 +-----+-----+
                 |           |
                 v           v
                AI       Integrations
```

------------------------------------------------------------------------

# 2. Technology Stack

  Component         Technology          Purpose
  ----------------- ------------------- ---------------------------------------
  Frontend          React               Customer chat and sales UI
  Backend           Python + FastAPI    API and application boundary
  Automation        n8n                 Workflow orchestration
  AI                LLM / AI Provider   Language understanding and extraction
  Database          SQL                 Primary source of truth
  Operations        Google Sheets       Supporting operational layer
  Version Control   Git + GitHub        Source control
  API Format        REST + JSON         Service communication

------------------------------------------------------------------------

# 3. Prerequisites

Before starting development, install the required tools.

## Required

-   Git
-   Python
-   Node.js
-   npm
-   SQL database
-   n8n
-   Code editor such as VS Code

## Recommended

-   GitHub account
-   API client such as Postman or Insomnia
-   Docker Desktop
-   Browser developer tools

Check installations:

``` powershell
git --version
python --version
node --version
npm --version
```

If the project uses a specific Python version, the repository should
document that version and developers should use the same version where
practical.

------------------------------------------------------------------------

# 4. Clone the Repository

Clone the GitHub repository:

``` powershell
git clone git@github.com:YOUR_USERNAME/real-estate-lead-bot.git
```

Move into the project:

``` powershell
cd real-estate-lead-bot
```

Check the repository:

``` powershell
git status
```

------------------------------------------------------------------------

# 5. Project Structure

The expected project structure is:

``` text
real-estate-lead-bot/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── README.md
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── db/
│   │   └── core/
│   ├── migrations/
│   ├── tests/
│   ├── requirements.txt
│   └── README.md
│
├── n8n/
│   └── workflows/
│
├── database/
│   ├── migrations/
│   └── seeds/
│
├── tests/
│   ├── integration/
│   └── e2e/
│
├── docs/
│
├── .env.example
├── .gitignore
└── README.md
```

------------------------------------------------------------------------

# 6. Environment Variables

Create the local environment configuration from the example file.

Windows PowerShell:

``` powershell
Copy-Item .env.example .env
```

Do not commit `.env`.

The `.gitignore` must contain:

``` gitignore
.env
.env.*
!.env.example
```

------------------------------------------------------------------------

# 7. Environment Configuration

A typical development configuration may contain:

``` env
APP_ENV=development
APP_NAME=real-estate-lead-bot

DATABASE_URL=

API_BASE_URL=http://localhost:8000

N8N_BASE_URL=http://localhost:5678
N8N_WEBHOOK_SECRET=

AI_API_KEY=
AI_MODEL=

GOOGLE_SHEETS_CREDENTIALS=

JWT_SECRET=

CORS_ORIGINS=http://localhost:5173
```

Actual values should be entered locally.

Never place real credentials in:

-   GitHub
-   source code
-   React components
-   README files
-   documentation
-   screenshots

------------------------------------------------------------------------

# 8. Python Backend Setup

Move into the backend:

``` powershell
cd backend
```

Create a virtual environment:

``` powershell
python -m venv .venv
```

Activate it:

``` powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation because of execution policy, use an
approved local development configuration or activate the environment
from another supported shell.

Verify Python:

``` powershell
python --version
```

------------------------------------------------------------------------

# 9. Install Backend Dependencies

With the virtual environment activated:

``` powershell
pip install -r requirements.txt
```

If `requirements.txt` does not yet exist, create it when the backend
dependencies are finalized.

Typical development dependencies may include:

``` text
fastapi
uvicorn
sqlalchemy
alembic
pydantic
pydantic-settings
python-dotenv
pytest
httpx
```

The exact dependency list should remain controlled by the project's
`requirements.txt`.

------------------------------------------------------------------------

# 10. Run FastAPI Locally

From the backend directory:

``` powershell
uvicorn app.main:app --reload
```

The API should be available at:

``` text
http://localhost:8000
```

FastAPI documentation should be available at:

``` text
http://localhost:8000/docs
```

A health check should be available at:

``` text
http://localhost:8000/health
```

The exact health endpoint may change according to the final API
implementation.

------------------------------------------------------------------------

# 11. Backend Development Flow

Backend requests should follow this structure:

``` text
HTTP Request
     |
     v
Router
     |
     v
Schema Validation
     |
     v
Service
     |
     v
Business/Application Logic
     |
     v
Repository / Database
     |
     v
Response
```

Keep responsibilities separated.

### Router

Handles:

-   HTTP request
-   authentication dependencies
-   response formatting

### Schemas

Handle:

-   request validation
-   response validation
-   API data contracts

### Services

Handle:

-   application logic
-   lead operations
-   qualification operations
-   customer operations

### Database Layer

Handles:

-   database sessions
-   queries
-   persistence

------------------------------------------------------------------------

# 12. React Frontend Setup

Open a new terminal.

From the project root:

``` powershell
cd frontend
```

Install dependencies:

``` powershell
npm install
```

Start the development server:

``` powershell
npm run dev
```

The application will normally be available at:

``` text
http://localhost:5173
```

The actual port depends on the React/Vite configuration.

------------------------------------------------------------------------

# 13. Frontend Environment

Frontend configuration should contain only values that are safe to
expose to the browser.

Example:

``` env
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

Do not put the following in React environment variables:

-   Database passwords
-   AI API keys
-   n8n private credentials
-   JWT signing secrets
-   Google service-account private keys

Browser-exposed environment variables are not secret.

------------------------------------------------------------------------

# 14. Frontend Development Flow

The frontend communicates with FastAPI:

``` text
Customer
   |
   v
React
   |
   v
API Client
   |
   v
FastAPI
```

React must not communicate directly with:

-   SQL
-   n8n
-   AI providers
-   private Google APIs

------------------------------------------------------------------------

# 15. SQL Database Setup

The project requires a SQL database for persistent application data.

The database should contain the core entities:

``` text
Customer
Lead
Conversation
Message
LeadScore
FollowUp
SalesAgent
```

Development database requirements:

-   Local or isolated development instance
-   Separate credentials from production
-   Persistent data during development where useful
-   Migration support
-   Test data/seeds

The production database must never be used for local development.

------------------------------------------------------------------------

# 16. Database Migration Setup

The project should use a migration tool such as Alembic.

Typical commands:

Create migration:

``` powershell
alembic revision --autogenerate -m "describe change"
```

Apply migrations:

``` powershell
alembic upgrade head
```

Check current migration:

``` powershell
alembic current
```

Rollback one migration:

``` powershell
alembic downgrade -1
```

Exact commands may depend on the final Alembic configuration.

------------------------------------------------------------------------

# 17. n8n Local Setup

n8n is the workflow orchestration layer.

It handles:

-   Lead enquiry processing
-   AI extraction
-   Lead qualification orchestration
-   Notifications
-   Google Sheets synchronization
-   Follow-up automation
-   Error handling

If using a local n8n installation, the development instance should be
isolated from production.

A typical local n8n address is:

``` text
http://localhost:5678
```

------------------------------------------------------------------------

# 18. n8n Development Rules

Development workflows should:

-   Use development credentials
-   Use development database connections
-   Use development AI configuration where possible
-   Use test notification destinations
-   Avoid modifying production data
-   Be exported/version controlled where appropriate

Recommended workflow naming:

``` text
REAL-ESTATE | WF-001 | Lead Enquiry Processing
REAL-ESTATE | WF-002 | Lead Creation Update
REAL-ESTATE | WF-003 | Lead Qualification
```

------------------------------------------------------------------------

# 19. AI Development Setup

The AI layer is responsible for language understanding.

Development tasks include:

-   Prompt development
-   Intent classification
-   Requirement extraction
-   Missing-field detection
-   Structured output
-   Response generation
-   AI failure handling

AI configuration should use environment variables:

``` env
AI_API_KEY=
AI_MODEL=
```

AI output must be validated before application data is persisted.

------------------------------------------------------------------------

# 20. Local Service Configuration

A complete local development environment should approximately look like:

``` text
Frontend
http://localhost:5173

FastAPI
http://localhost:8000

FastAPI Docs
http://localhost:8000/docs

n8n
http://localhost:5678

SQL
localhost:<database-port>
```

Ports may be changed if they conflict with another local service.

------------------------------------------------------------------------

# 21. Recommended Terminal Layout

During active development, use separate terminals.

### Terminal 1 --- Backend

``` powershell
cd backend
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

### Terminal 2 --- Frontend

``` powershell
cd frontend
npm run dev
```

### Terminal 3 --- n8n

Run the local n8n development instance.

### Terminal 4 --- Git

Use this terminal for:

``` powershell
git status
git add .
git commit
git pull
git push
```

------------------------------------------------------------------------

# 22. Running Tests

Backend tests:

``` powershell
cd backend
pytest
```

Frontend tests should use the test command defined in `package.json`.

Integration and end-to-end tests should be run according to the
project's testing configuration.

Before committing a feature:

``` text
Code
 |
 v
Unit Tests
 |
 v
Integration Tests
 |
 v
Manual Verification
 |
 v
Git Commit
```

------------------------------------------------------------------------

# 23. Git Development Workflow

Create a feature branch:

``` powershell
git checkout -b feature/feature-name
```

Check changes:

``` powershell
git status
```

Stage changes:

``` powershell
git add .
```

Commit:

``` powershell
git commit -m "feat: describe change"
```

Push:

``` powershell
git push -u origin feature/feature-name
```

Do not develop directly on `main` for normal feature work.

------------------------------------------------------------------------

# 24. Code Quality

Before merging changes:

-   [ ] Code is readable
-   [ ] Functions have clear responsibilities
-   [ ] Duplicate logic is minimized
-   [ ] Validation exists at system boundaries
-   [ ] Errors are handled
-   [ ] Tests are added where appropriate
-   [ ] Secrets are not exposed
-   [ ] Documentation is updated when required

------------------------------------------------------------------------

# 25. Development Data

Use clearly identifiable test data.

Example:

``` text
Name: Test Customer
Email: test@example.com
Phone: 08000000000
Location: Lekki
Property: 3-bedroom apartment
Budget: ₦80,000,000
Transaction: BUY
Timeline: IMMEDIATE
```

Do not use real customer information for ordinary local testing.

------------------------------------------------------------------------

# 26. Example End-to-End Local Test

Customer sends:

``` text
Hi, I'm looking for a 3-bedroom apartment around Lekki.
My budget is around ₦80 million.
```

Expected flow:

``` text
React
  |
  v
POST /api/v1/chat
  |
  v
FastAPI
  |
  v
n8n
  |
  v
AI
  |
  v
Structured Extraction
  |
  v
Validation
  |
  v
Lead Qualification
  |
  v
SQL Database
  |
  v
Sales Notification
  |
  v
Customer Response
  |
  v
React
```

Expected extracted information includes:

``` text
Property Type: Apartment
Bedrooms: 3
Location: Lekki
Budget: ₦80,000,000
Transaction Type: BUY
```

The AI must not invent information that was not provided.

------------------------------------------------------------------------

# 27. Troubleshooting

## FastAPI does not start

Check:

``` powershell
python --version
```

Confirm the virtual environment is active:

``` powershell
.\.venv\Scripts\Activate.ps1
```

Check dependencies:

``` powershell
pip list
```

------------------------------------------------------------------------

## React does not start

Check:

``` powershell
node --version
npm --version
```

Then:

``` powershell
npm install
npm run dev
```

------------------------------------------------------------------------

## Database connection fails

Check:

-   `DATABASE_URL`
-   Database service status
-   Database credentials
-   Database host and port
-   Migration configuration

Do not copy production credentials into development.

------------------------------------------------------------------------

## n8n workflow fails

Check:

-   Workflow is active
-   Webhook URL is correct
-   Credentials are valid
-   Backend is running
-   AI configuration is valid
-   Database is available
-   Input payload matches the workflow contract

------------------------------------------------------------------------

## AI extraction fails

Check:

-   AI API key
-   AI model
-   Prompt
-   Structured output format
-   Timeout
-   Provider response

The system should fail safely instead of saving invalid AI data.

------------------------------------------------------------------------

# 28. Common Development Mistakes

Avoid:

-   Committing `.env`
-   Committing API keys
-   Connecting frontend directly to SQL
-   Connecting frontend directly to n8n
-   Using production database locally
-   Hardcoding secrets
-   Trusting AI output without validation
-   Putting all business logic inside n8n
-   Putting all business logic inside React
-   Skipping database migrations
-   Working directly on `main`
-   Skipping tests before merging

------------------------------------------------------------------------

# 29. Development Definition of Done

A development environment is considered ready when:

-   [ ] Repository is cloned
-   [ ] Git is configured
-   [ ] Python environment works
-   [ ] Backend dependencies are installed
-   [ ] FastAPI starts successfully
-   [ ] React starts successfully
-   [ ] SQL database is accessible
-   [ ] Database migrations work
-   [ ] n8n is accessible
-   [ ] AI configuration works
-   [ ] Environment variables are configured
-   [ ] `.env` is ignored by Git
-   [ ] Basic API request works
-   [ ] Basic frontend-to-backend request works
-   [ ] Basic n8n workflow works
-   [ ] Basic end-to-end test passes

------------------------------------------------------------------------

# 30. Development Setup Checklist

## Initial Setup

-   [ ] Install Git
-   [ ] Install Python
-   [ ] Install Node.js
-   [ ] Install npm
-   [ ] Install/configure SQL database
-   [ ] Install/configure n8n
-   [ ] Clone repository
-   [ ] Configure `.env`
-   [ ] Configure Git identity

## Backend

-   [ ] Create `.venv`
-   [ ] Activate `.venv`
-   [ ] Install dependencies
-   [ ] Configure database
-   [ ] Run migrations
-   [ ] Start FastAPI
-   [ ] Verify `/health`
-   [ ] Verify `/docs`

## Frontend

-   [ ] Install npm dependencies
-   [ ] Configure API URL
-   [ ] Start React
-   [ ] Open application
-   [ ] Test API connection

## n8n

-   [ ] Start n8n
-   [ ] Configure development credentials
-   [ ] Import/create workflows
-   [ ] Test webhook
-   [ ] Test AI integration
-   [ ] Test database operation

## Verification

-   [ ] Send test customer message
-   [ ] Extract requirements
-   [ ] Create lead
-   [ ] Store lead in SQL
-   [ ] Run qualification
-   [ ] Generate response
-   [ ] Verify notification
-   [ ] Verify conversation history

------------------------------------------------------------------------

# 31. Development Commands Reference

### Git

``` powershell
git status
git pull
git add .
git commit -m "message"
git push
```

### Python

``` powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### FastAPI

``` powershell
uvicorn app.main:app --reload
```

### React

``` powershell
npm install
npm run dev
```

### Tests

``` powershell
pytest
```

### Database

``` powershell
alembic upgrade head
alembic current
```

------------------------------------------------------------------------

*Full original content restored from the foundational specification.*
