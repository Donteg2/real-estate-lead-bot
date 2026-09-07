# n8n Workflows — Real Estate Lead Bot

n8n is the **workflow orchestration layer**.

## Responsibilities

- Lead enquiry processing pipeline
- AI extraction & validation orchestration
- Lead creation / update
- Qualification trigger
- Sales notifications
- Google Sheets synchronization (supporting layer)
- Follow-up automation
- Error handling & retries

## Guidelines (from Architecture)

- Do **not** put complex domain / business rules exclusively inside large workflows.
- Prefer deterministic rules in FastAPI services.
- SQL remains the primary source of truth.
- Google Sheets is supporting only.

## Recommended Naming

```text
REAL-ESTATE | WF-001 | Lead Enquiry Processing
REAL-ESTATE | WF-002 | Lead Creation / Update
REAL-ESTATE | WF-003 | Lead Qualification
REAL-ESTATE | WF-004 | Sales Notification
REAL-ESTATE | WF-005 | Follow-up Automation
```

Export workflows as JSON and keep them under `n8n/workflows/` for version control.
