# REAL ESTATE LEAD BOT

## Project Overview

**REAL ESTATE LEAD BOT** is an AI-powered digital receptionist and lead management system designed for real estate companies (reference client: PrimeHomes Realty).

It converts natural-language customer enquiries into structured, qualified leads that the sales team can act on.

### Core Flow

Customer message → React chat UI → FastAPI → n8n orchestration → AI extraction → Validation → Lead qualification & scoring → SQL storage → Sales notification → Customer response.

### Tech Stack

- **Frontend:** React (Vite)
- **Backend:** Python + FastAPI
- **Automation:** n8n
- **AI:** LLM-based extraction & response generation
- **Database:** SQL (primary source of truth)
- **Supporting:** Google Sheets via n8n

### Key Documents

All detailed specifications are available in the `docs/` folder:

- [PRD](./PRD.md)
- [System Architecture (SAD)](./SAD.md)
- [Implementation Tracking](./IMPLEMENTATION.md)
- [Development Setup](./DEVELOPMENT_SETUP.md)
- [Database Spec](./DATABASE.md)
- [API Spec](./API.md)
- [AI Spec](./AI-SPEC.md)
- [n8n Workflows](./N8N-WORKFLOWS.md)
- [Lead Qualification](./LEAD_QUALIFICATION.md)
- [UI/UX](./UI-UX.md)
- [Deployment](./DEPLOYMENT.md)
- [Testing](./TESTING.md)
- [Tasks](./TASK.md)

This overview file replaces the previous root-level `Real Estate Lead bot.md`.
