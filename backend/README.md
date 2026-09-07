# Backend — Real Estate Lead Bot

FastAPI application that serves as the API and application boundary for the Real Estate Lead Bot.

## Responsibilities

- API endpoints (`/api/v1/...`)
- Request / response validation (Pydantic)
- Authentication & Authorization
- Business logic (lead qualification, scoring, lifecycle)
- Database access (SQLAlchemy)
- Communication with n8n workflows where needed

## Structure

```text
backend/
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── api/                 # Routers (chat, leads, followups)
│   ├── models/              # SQLAlchemy models
│   ├── schemas/             # Pydantic schemas
│   ├── services/            # Business logic
│   ├── db/                  # Database connection & session
│   └── core/                # Config, security, logging
├── migrations/              # Alembic migrations (to be added)
├── tests/
├── requirements.txt
└── README.md
```

## Local Development

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API docs: http://localhost:8000/docs  
Health: http://localhost:8000/health

## Environment

Copy `.env.example` from the project root and fill in values. Never commit real secrets.
