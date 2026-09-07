# Frontend — Real Estate Lead Bot

React application providing the customer chat interface and sales dashboard.

## Responsibilities

- Customer chat UI
- Lead interaction & message display
- Sales dashboard (leads list, filters, details)
- Communication with FastAPI backend only (never directly with DB, n8n, or AI)

## Structure (planned)

```text
frontend/
├── src/
│   ├── api/           # API client (chat, leads, conversations)
│   ├── components/    # UI components
│   ├── pages/         # Chat, Dashboard, Lead details
│   ├── hooks/
│   ├── types/
│   ├── App.tsx
│   └── main.tsx
├── public/
├── package.json
└── README.md
```

## Local Development

```bash
cd frontend
npm install
npm run dev
```

App runs at: http://localhost:5173

Set `VITE_API_BASE_URL=http://localhost:8000/api/v1` in a local `.env` (do not commit secrets).
