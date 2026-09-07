# Real Estate Lead Bot

**Client:** PrimeHomes Realty  
**Stack:** React + FastAPI + n8n + AI/LLM + SQL Database (+ Google Sheets as supporting layer)

A lead-management and customer-engagement system that acts as a digital receptionist for real estate companies. It receives natural-language enquiries, extracts structured lead information, qualifies leads, notifies the sales team, and maintains conversation history.

---

## High-Level Architecture

```text
Customer → React Frontend → FastAPI Backend → n8n Workflows
                                              ├── AI Processing
                                              ├── SQL Database (source of truth)
                                              ├── Notifications
                                              └── Google Sheets (supporting)
```

Clear separation of responsibilities:

| Component     | Responsibility                              |
|---------------|---------------------------------------------|
| **React**     | Presentation & user interaction             |
| **FastAPI**   | API, validation, business logic, auth       |
| **n8n**       | Workflow orchestration & integrations       |
| **AI**        | NLU, extraction, response generation        |
| **SQL**       | Primary source of truth for application data|
| **Sheets**    | Supporting operational visibility           |

---

## Project Structure

```text
real-estate-lead-bot/
├── frontend/                 # React + Vite application
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── README.md
│
├── backend/                  # FastAPI application
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── db/
│   │   └── core/
│   ├── tests/
│   ├── requirements.txt
│   └── README.md
│
├── n8n/
│   └── workflows/            # Exported n8n workflow JSONs
│
├── database/
│   ├── migrations/
│   └── seeds/
│
├── tests/
│   ├── integration/
│   └── e2e/
│
├── docs/                     # Documentation index
│
├── .env.example
├── .gitignore
└── README.md
```

The full set of approved specification documents currently lives at the repository root (PRD, System Architecture, IMPLEMENTATION, DEVELOPMENT_SETUP, Database Spec, API Spec, AI Spec, n8n Workflows Spec, etc.). See `docs/README.md`.

---

## Quick Start (Local Development)

### Prerequisites
- Git, Python 3.11+, Node.js 18+, npm
- SQL database (PostgreSQL recommended)
- n8n (local or cloud)

### 1. Clone & Configure

```bash
git clone https://github.com/Donteg2/real-estate-lead-bot.git
cd real-estate-lead-bot
cp .env.example .env
# Edit .env with your local values (never commit real secrets)
```

### 2. Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate          # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- Health: http://localhost:8000/health

### 3. Frontend

```bash
cd frontend
npm install
npm run dev
```

- App: http://localhost:5173

### 4. n8n

Start your local n8n instance (typically http://localhost:5678) and import/create workflows under `n8n/workflows/`.

---

## Key Documents

| Document | Description |
|----------|-------------|
| [PRD](./PRD%20—%20Real%20Estate%20Lead%20Bot.md) | Product Requirements |
| [System Architecture](./System%20Architecture%20Document%20—%20Real%20Estate%20Lead%20Bot%20(1).md) | SAD – architecture & component boundaries |
| [IMPLEMENTATION](./IMPLEMENTATION.md) | Task tracking & implementation status |
| [DEVELOPMENT_SETUP](./DEVELOPMENT_SETUP.md) | Detailed local setup guide |
| [Database Spec](./Database%20Specification%20—%20DATABASE.md) | Schema & entities |
| [API Spec](./API%20Specification%20—%20API.md) | API contracts |
| [AI Spec](./AI%20Specification.md) | AI responsibilities & schemas |
| [n8n Workflows](./n8n%20Workflows%20Specification.md) | Workflow definitions |
| [Lead Qualification](./LEAD_QUALIFICATION_SPEC.md) | Scoring & qualification rules |

---

## Development Principles

1. SQL is the primary source of truth.
2. AI extracts facts; the application applies deterministic business rules.
3. Never put secrets in frontend code or commit them to Git.
4. Frontend talks only to FastAPI.
5. Keep complex domain logic out of large n8n workflows.
6. Validate at system boundaries.
7. Prefer maintainable, testable code over premature complexity.

---

## License

MIT — see [LICENSE](./LICENSE).
