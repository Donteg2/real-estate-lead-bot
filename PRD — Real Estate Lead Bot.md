# Product Requirements Document (PRD)

**Product:** Real Estate Lead Bot  
**Reference Client:** PrimeHomes Realty  
**Document Version:** 0.1  
**Status:** Draft  
**Primary Stack:** React + FastAPI + n8n + SQL Database  
**Supporting Storage:** Google Sheets via n8n  
**Document Owner:** Product / Engineering  
**Last Updated:** September 2026

---

## 1. Product Overview

The Real Estate Lead Bot is a lead-management and customer-engagement system designed to help real estate companies automatically receive, understand, qualify, store, and route potential customers.

The system acts as a digital receptionist for a real estate company.

Instead of requiring sales staff to manually read and process every incoming customer message, the system will use a combination of:

- React for the customer-facing interface.
- FastAPI for backend APIs and custom business logic.
- n8n for workflow orchestration and integrations.
- AI/LLMs for natural-language understanding and response generation.
- SQL database for structured and reliable application data.
- Google Sheets through n8n for operational visibility, lightweight reporting, or selected workflow use cases.

The system should allow a potential customer to communicate naturally while converting their message into structured lead information that the business can act upon.

---

# 2. Problem Statement

Real estate companies receive potential customers from multiple channels and often process those enquiries manually.

A typical customer may send:

> "Hi, I'm looking for a 3-bedroom apartment around Lekki. My budget is around ₦80 million."

A salesperson must manually determine:

- Who the customer is.
- What property they want.
- Where they want it.
- Their budget.
- Whether they want to buy or rent.
- How soon they intend to act.
- How valuable the lead may be.
- What response should be sent.
- Whether another salesperson needs to follow up.

At relatively low message volumes this may be manageable.

At higher volumes, manual processing introduces several problems:

- Slow response times.
- Missed leads.
- Inconsistent qualification.
- Incomplete customer information.
- Poor follow-up tracking.
- Salespeople spending time on repetitive administrative work.
- Difficulty identifying high-value or urgent leads.
- Lack of centralized lead information.

The product exists to reduce these problems by automating the repetitive parts of the lead-management process while keeping humans involved where human judgment is important.

---

# 3. Product Vision

Build a reliable digital receptionist and lead-management system that enables real estate companies to respond to potential customers quickly, understand their requirements automatically, and give sales teams structured, actionable leads.

The long-term vision is not simply an AI chatbot.

It is a lightweight **real estate lead operating system** connecting:

**Customer → Conversation → AI Understanding → Lead → Qualification → Sales → Follow-up → Outcome**

---

# 4. Product Goals

## 4.1 Primary Goals

The system should:

1. Receive potential customer enquiries.
2. Understand natural-language messages.
3. Extract relevant lead information.
4. Validate extracted information.
5. Store structured lead data.
6. Identify missing information.
7. Ask appropriate follow-up questions.
8. Determine lead priority.
9. Generate appropriate customer responses.
10. Notify the appropriate sales personnel.
11. Allow sales staff to follow up.
12. Track lead status and progression.
13. Maintain a history of customer interactions.
14. Provide sufficient information for sales staff to act without rereading the entire conversation.

---

## 4.2 Business Goals

The system should help PrimeHomes Realty:

- Reduce manual lead-processing workload.
- Reduce response time.
- Reduce lost or forgotten leads.
- Improve lead qualification.
- Prioritize high-value opportunities.
- Improve sales-team visibility.
- Create consistent lead-processing procedures.
- Build a foundation for future sales automation.

---

# 5. Non-Goals

The initial version will NOT attempt to become a complete real estate CRM or property marketplace.

The MVP will not initially focus on:

- Full property listing management.
- Property purchase transactions.
- Online payments.
- Legal documentation.
- Property valuation.
- Automated negotiation.
- Mortgage processing.
- Property ownership verification.
- Complex sales forecasting.
- Fully autonomous AI sales agents.
- Replacing human salespeople.

The system's primary responsibility is **lead capture, understanding, qualification, routing, response, and follow-up tracking**.

---

# 6. Target Users

## 6.1 Potential Customer / Lead

A person interested in:

- Buying property.
- Renting property.
- Buying land.
- Selling property.
- Making a general property enquiry.

They interact primarily through the customer-facing interface.

---

## 6.2 Sales Agent

A sales team member responsible for following up with leads.

The sales agent needs to know:

- Who the lead is.
- What they want.
- Their budget.
- Their preferred location.
- Their timeline.
- Lead priority.
- Conversation history.
- Current lead status.
- Required next action.

---

## 6.3 Sales Manager

A manager responsible for monitoring and distributing leads.

The manager may need to:

- View incoming leads.
- See high-priority leads.
- Assign leads.
- Monitor follow-up.
- Track lead status.
- Review sales-team activity.

---

## 6.4 System Administrator

Responsible for system configuration and technical operation.

The administrator may manage:

- Users.
- Roles.
- Integrations.
- AI configuration.
- Workflow configuration.
- System settings.

---

# 7. Core User Journey

The primary customer journey is:

```text
Customer
   ↓
Sends Message
   ↓
System Receives Message
   ↓
Validate Input
   ↓
AI Understands Message
   ↓
Extract Lead Information
   ↓
Check Missing Information
   ↓
Ask Follow-up Question if Required
   ↓
Qualify Lead
   ↓
Calculate Lead Score
   ↓
Store / Update Lead
   ↓
Generate Customer Response
   ↓
Notify Sales Team
   ↓
Sales Follow-up
   ↓
Update Lead Status
   ↓
Track Outcome
```

---

# 8. Core Product Concept

The central concept of the system is the **Lead**.

A conversation becomes a structured lead when the system identifies a potential business opportunity.

A lead contains two major categories of information:

### Customer Information

- Name
- Email
- Phone
- Preferred contact method

### Requirement Information

- Intent
- Property type
- Location
- Bedrooms
- Budget
- Transaction type
- Timeline
- Additional requirements

The system should continuously improve the lead record as more information becomes available.

---

# 9. Lead Information Model

The initial lead model should support the following information.

## Customer

```text
name
email
phone
```

## Property Requirements

```text
property_type
bedrooms
location
budget_min
budget_max
currency
transaction_type
```

Where transaction type may include:

```text
BUY
RENT
SELL
INQUIRE
```

## Intent

Possible intents:

```text
BUY_PROPERTY
RENT_PROPERTY
BUY_LAND
SELL_PROPERTY
GENERAL_ENQUIRY
```

## Timeline

```text
IMMEDIATE
WITHIN_1_MONTH
WITHIN_3_MONTHS
RESEARCHING
UNKNOWN
```

## Lead Status

Initial statuses:

```text
NEW
CONTACTED
QUALIFIED
FOLLOW_UP
CONVERTED
LOST
CLOSED
```

## Lead Priority

```text
HOT
WARM
COLD
```

The exact definitions and scoring rules will be finalized in the Domain Specification and Lead Qualification Specification.

---

# 10. Functional Requirements

## FR-001 — Receive Customer Messages

The system must be able to receive a customer message from the supported frontend interface.

The message should include enough information to associate it with a conversation/session.

The system should record:

- Message content.
- Timestamp.
- Conversation/session identifier.
- Customer identifier where available.

---

## FR-002 — Validate Incoming Data

The backend must validate incoming requests before processing.

Validation should include:

- Required fields.
- Data types.
- String length.
- Valid identifiers.
- Malformed requests.
- Invalid values.

Invalid requests should return appropriate API errors.

---

## FR-003 — Understand Customer Intent

The AI processing layer should determine what the customer is trying to accomplish.

Example:

> "I need a house in Lekki."

Possible interpretation:

```text
intent: BUY_PROPERTY
property_type: HOUSE
location: LEKKI
```

The system must support uncertainty.

AI should not invent information that the customer did not provide.

---

## FR-004 — Extract Lead Information

The AI should convert natural-language messages into structured information.

Example input:

> "I'm looking for a 3-bedroom apartment around Lekki. My budget is about ₦80m and I'd like to move within two months."

Expected structured output:

```json
{
  "intent": "BUY_PROPERTY",
  "property_type": "APARTMENT",
  "bedrooms": 3,
  "location": "Lekki",
  "budget_max": 80000000,
  "currency": "NGN",
  "timeline": "WITHIN_3_MONTHS"
}
```

The AI extraction output must use a predefined schema.

---

## FR-005 — Handle Missing Information

The system should identify important information that has not yet been provided.

For example:

Customer:

> "I want to buy a house."

The system should not immediately classify the lead as fully qualified.

It may respond:

> "Absolutely. Which area are you looking to buy in, and what budget range are you considering?"

The system should collect information progressively rather than forcing the customer to complete a long form.

---

## FR-006 — Maintain Conversation Context

The system should maintain enough conversation context to understand follow-up messages.

Example:

Customer:

> "I'm looking for a 3-bedroom apartment."

Bot:

> "Which area are you interested in?"

Customer:

> "Lekki."

The system must associate "Lekki" with the existing conversation and lead.

---

## FR-007 — Create Lead

When a potential customer is identified, the system must create a lead record.

The lead should have:

- Unique ID.
- Customer information.
- Requirements.
- Lead status.
- Lead priority.
- Lead score.
- Created timestamp.
- Updated timestamp.

---

## FR-008 — Update Existing Lead

The system must update an existing lead when new information is received.

It should avoid creating duplicate leads unnecessarily.

Lead matching may use combinations of:

- Customer ID.
- Phone.
- Email.
- Conversation ID.

The final deduplication strategy will be defined during system design.

---

## FR-009 — Qualify Lead

The system should evaluate the quality and urgency of a lead.

Qualification may consider:

- Budget.
- Property type.
- Location specificity.
- Timeline.
- Buying intent.
- Completeness of requirements.
- Customer engagement.

Example:

```text
Lead:
3-bedroom apartment
Lekki
₦80m
Moving within 2 months
Buying

Priority:
HOT
```

The exact scoring algorithm will be defined separately from this PRD.

---

## FR-010 — Generate Customer Response

The AI should generate a response appropriate to the current conversation state.

Responses should:

- Be professional.
- Be concise.
- Be helpful.
- Avoid fabricating property availability.
- Ask only relevant missing questions.
- Avoid promising something the system cannot verify.

If the system does not have property inventory data, it must not claim that a specific property is available.

---

## FR-011 — Notify Sales Team

The system should notify the appropriate sales team when a lead reaches a defined qualification or priority threshold.

For example:

```text
🔥 HOT LEAD

Name: John Doe
Intent: Buy
Property: 3-bedroom apartment
Location: Lekki
Budget: ₦80m
Timeline: Within 2 months

Lead Score: 87/100
```

The exact notification channel will be determined during system design.

---

## FR-012 — Sales Follow-up

Sales staff should be able to follow up with leads.

The system should support recording:

- Assigned sales agent.
- Follow-up status.
- Follow-up notes.
- Next action.
- Follow-up date.
- Lead status.

---

## FR-013 — Track Lead Lifecycle

The system should track the lead from initial enquiry through its eventual outcome.

Example:

```text
NEW
 ↓
QUALIFIED
 ↓
ASSIGNED
 ↓
CONTACTED
 ↓
FOLLOW_UP
 ↓
CONVERTED
```

Alternative outcome:

```text
NEW
 ↓
CONTACTED
 ↓
LOST
```

---

## FR-014 — Store Conversation History

The system should maintain relevant conversation history associated with a lead.

This allows sales staff and the AI to understand previous interactions.

---

## FR-015 — Maintain Audit Information

Important lead changes should have timestamps and, where appropriate, information about what caused the change.

Examples:

- Lead created.
- Lead score changed.
- Lead assigned.
- Lead status changed.
- Sales agent added.
- Follow-up completed.

---

# 11. Non-Functional Requirements

## NFR-001 — Reliability

The system should handle temporary failures without unnecessarily losing customer messages or lead data.

---

## NFR-002 — Security

The system must protect customer information.

Sensitive configuration such as:

- API keys.
- Database credentials.
- AI provider credentials.
- n8n credentials.

must not be hardcoded in source code.

---

## NFR-003 — Data Integrity

Lead information stored in the SQL database must remain consistent.

Critical database operations should use appropriate validation and transactional behavior.

---

## NFR-004 — Performance

Customer interactions should receive responses within a reasonable period.

Long-running operations such as AI processing, notifications, or external integrations should be designed so they do not unnecessarily block the customer-facing API.

---

## NFR-005 — Observability

The system should provide sufficient:

- Logs.
- Error information.
- Workflow execution visibility.
- API monitoring.
- AI processing visibility.

to diagnose failures.

---

## NFR-006 — Maintainability

The system must maintain clear separation between:

```text
Frontend
Backend
Automation
AI
Database
Integrations
```

The implementation should avoid placing all business logic inside a single n8n workflow or a single backend file.

---

## NFR-007 — Scalability

The architecture should allow the system to grow from a small demonstration into a production application without requiring a complete rewrite.

---

# 12. Technology Responsibilities

## Frontend — React

Responsible for:

- Chat interface.
- Lead forms where required.
- User interaction.
- Displaying bot responses.
- Loading states.
- Error states.
- Basic sales interface where included.
- Communicating with the FastAPI backend.

---

## Backend — FastAPI

Responsible for:

- API endpoints.
- Request validation.
- Authentication/authorization where required.
- Business logic that should not live in n8n.
- Database-facing application logic where appropriate.
- API security.
- Communication between frontend and backend.
- Providing stable interfaces to other components.

---

## Automation — n8n

Responsible for:

- Workflow orchestration.
- AI workflow execution.
- Integrations.
- Notifications.
- Lead routing.
- Selected database operations.
- Follow-up automation.
- External service coordination.

n8n should not become the location for every piece of application logic.

---

## AI Layer

Responsible for:

- Natural-language understanding.
- Intent classification.
- Requirement extraction.
- Conversation summarization.
- Response generation.
- Lead classification where appropriate.

AI output must be constrained by structured schemas and application rules.

---

## SQL Database

The SQL database will serve as the **primary system of record for core application data**.

It should store:

- Leads.
- Customers.
- Conversations.
- Messages.
- Lead scores.
- Lead status.
- Sales assignments.
- Follow-up information.
- Relevant audit information.

The specific SQL technology will be finalized during System Design.

---

## Google Sheets

Google Sheets should be treated as a **supporting operational data layer**, not automatically as the authoritative database.

Potential uses include:

- Simple sales-team visibility.
- Operational reporting.
- Exporting leads.
- Lightweight business workflows.
- Demonstration/prototyping.
- Manual review.

The SQL database should remain the source of truth for core application data once the production architecture is established.

---

# 13. Initial API Requirements

The following endpoints are proposed for the MVP.

```text
POST /api/v1/chat
```

Receives a customer message.

```text
POST /api/v1/leads
```

Creates a lead.

```text
GET /api/v1/leads/{lead_id}
```

Retrieves a lead.

```text
PATCH /api/v1/leads/{lead_id}
```

Updates a lead.

```text
GET /api/v1/leads
```

Lists leads.

```text
POST /api/v1/leads/{lead_id}/follow-ups
```

Creates a follow-up activity.

These are initial API concepts, not final contracts.

The final API specification will be created in the API Design document.

---

# 14. Lead Qualification Concept

The system will assign a score to help sales staff prioritize leads.

A conceptual scoring model may consider:

```text
Intent
+
Budget
+
Timeline
+
Requirement completeness
+
Location specificity
+
Engagement
=
Lead Score
```

Example:

```text
80–100 → HOT
50–79  → WARM
0–49   → COLD
```

These thresholds are placeholders.

The actual qualification rules must be defined, tested, and documented before production use.

The AI should not have unrestricted authority to determine business-critical qualification rules.

Where possible:

```text
AI → extracts facts
Backend/n8n → applies deterministic business rules
System → calculates final score
```

This separation improves reliability and explainability.

---

# 15. AI Reliability Principle

The AI should **extract and interpret information, not invent facts**.

For example, if the customer says:

> "I have ₦50m."

The system may extract:

```text
budget: 50000000
currency: NGN
```

It should not infer:

```text
bedrooms: 4
location: Lekki
timeline: immediate
```

unless those facts are explicitly supported by the conversation or another trusted data source.

Unknown information should remain:

```text
null
unknown
not_provided
```

rather than being guessed.

---

# 16. Error Handling

The system must account for failures in:

- Frontend requests.
- FastAPI.
- Database.
- n8n.
- AI provider.
- External APIs.
- Notifications.
- Network communication.

Examples:

### AI failure

The system should not silently create a lead using fabricated information.

It should fall back to a safe response or retry mechanism.

### Database failure

The system should record/log the failure and avoid falsely telling the user that their information has been successfully stored.

### Notification failure

The lead should remain stored even if the sales notification fails.

The system should support retrying the notification.

---

# 17. MVP Scope

The first usable version should focus on the following:

### Customer side

- React chat interface.
- Send message.
- Receive bot response.
- Basic conversation state.

### Backend

- FastAPI application.
- Chat endpoint.
- Lead endpoints.
- Request validation.
- Basic authentication architecture where required.

### n8n

- Receive/process workflow.
- AI extraction.
- Lead qualification.
- SQL persistence.
- Notification workflow.

### AI

- Intent classification.
- Structured information extraction.
- Missing-information detection.
- Response generation.
- Conversation summarization.

### Database

Core entities:

```text
Customer
Lead
Conversation
Message
LeadScore
FollowUp
SalesAgent
```

### Sales

- Receive lead notification.
- View lead information.
- Update lead status.
- Record follow-up.

---

# 18. Future Scope

Potential future capabilities include:

- WhatsApp integration.
- Instagram integration.
- Facebook Messenger integration.
- Property inventory integration.
- Automated property recommendations.
- Advanced CRM dashboard.
- Sales analytics.
- Lead assignment based on location.
- Agent performance analytics.
- Automated follow-up campaigns.
- Voice interaction.
- Multilingual support.
- Calendar integration.
- Appointment scheduling.
- AI-assisted sales recommendations.
- RAG over property listings.
- Lead conversion prediction.

These should not be allowed to expand the MVP without a deliberate product decision.

---

# 19. Success Metrics

The initial system should measure:

### Lead Response Time

How long it takes the system to respond to a customer.

### Lead Processing Time

Time from message received to structured lead creation/update.

### Lead Capture Rate

Percentage of potential leads successfully captured.

### Information Extraction Accuracy

Percentage of extracted fields that are correct.

### Lead Qualification Accuracy

How accurately the system prioritizes leads compared with agreed business rules/human review.

### Follow-up Rate

Percentage of qualified leads receiving appropriate sales follow-up.

### Conversion Rate

Percentage of leads eventually becoming successful business opportunities.

### Automation Success Rate

Percentage of workflows completed without requiring manual intervention.

---

# 20. Acceptance Criteria for MVP

The MVP can be considered functionally complete when:

1. A customer can send a message through the React interface.
2. FastAPI receives and validates the request.
3. The request can be passed into the n8n workflow.
4. AI can extract structured lead information.
5. Missing information can be identified.
6. The system can generate an appropriate response.
7. A lead can be created in the SQL database.
8. Existing leads can be updated.
9. A lead score can be calculated.
10. High-priority leads can trigger a sales notification.
11. Sales staff can identify the lead and its requirements.
12. Lead status can be updated.
13. Follow-up information can be recorded.
14. Conversation history can be associated with the lead.
15. Major system failures are logged and handled safely.
16. AI does not fabricate customer information or property availability.

---

# 21. Development Principles

The project should follow these principles.

### Principle 1 — Separation of Responsibilities

Each technology should have a clear purpose.

```text
React
→ User interface

FastAPI
→ Application/API layer

n8n
→ Workflow orchestration/integrations

AI
→ Language understanding/generation

SQL
→ Core persistent data

Google Sheets
→ Supporting operational workflows
```

---

### Principle 2 — AI Is Not the Source of Truth

AI interprets information.

The application determines what is valid.

The database stores the authoritative state.

---

### Principle 3 — Deterministic Logic Where Possible

If a rule can reliably be implemented with normal code, it should not unnecessarily be delegated to an LLM.

For example:

```text
if budget >= 50000000:
    ...
```

is better handled by deterministic application logic than asking an LLM to calculate it.

---

### Principle 4 — Structured AI Outputs

AI should return structured data according to predefined schemas rather than unrestricted text wherever the application needs to consume AI output.

---

### Principle 5 — Build Incrementally

The project should be developed in vertical slices.

For example:

```text
Customer
 ↓
React
 ↓
FastAPI
 ↓
n8n
 ↓
AI
 ↓
SQL
 ↓
Response
```

should work end-to-end before adding large amounts of additional functionality.

---

### Principle 6 — Documentation Is Part of the System

Architecture decisions, domain terminology, API contracts, AI behavior, and engineering rules should be documented and kept synchronized with the implementation.

---

# 22. Product Architecture Direction

The initial architecture direction is:

```text
                     CUSTOMER
                         │
                         ▼
                ┌─────────────────┐
                │  React Frontend │
                │   Chat / Forms  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   FastAPI API   │
                │ Validation/API  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │       n8n       │
                │ Workflow Engine │
                └───────┬─────────┘
                        │
             ┌──────────┼──────────┐
             ▼          ▼          ▼
           AI         SQL       Notifications
             │          │          │
             └──────────┼──────────┘
                        ▼
                  SALES TEAM
                        │
                        ▼
                    FOLLOW-UP
```

This architecture is a **direction**, not yet the final technical architecture.

The System Architecture document will determine exactly where responsibilities belong and how components communicate.

---

# 23. Open Questions

The following decisions must be resolved during the next design stages:

1. Which SQL database will be used?
2. Will the frontend communicate only with FastAPI or also directly with n8n?
3. How will customer identity be established?
4. Which communication channels will the MVP support?
5. Which AI provider/model will be used?
6. Which notification channel will be used?
7. How will sales agents authenticate?
8. How will leads be assigned to sales agents?
9. What exact factors determine lead score?
10. What constitutes a HOT, WARM, or COLD lead?
11. What information is mandatory before a lead becomes QUALIFIED?
12. How will duplicate leads be detected?
13. How long should conversation history be retained?
14. What customer data requires additional protection?
15. What should happen when AI extraction fails?
16. What should happen when n8n is unavailable?
17. What should happen when the SQL database is unavailable?
18. What information should be synchronized with Google Sheets?
19. Which system is the authoritative source of truth for each type of data?
20. Which operations require human approval?

---

# 24. Definition of Done — Product Level

A feature is not considered complete simply because the code runs.

A feature is considered complete when:

```text
Requirement defined
        ↓
Acceptance criteria defined
        ↓
UI implemented where required
        ↓
API implemented
        ↓
Business logic implemented
        ↓
n8n workflow implemented where required
        ↓
AI behavior implemented where required
        ↓
Database persistence implemented
        ↓
Error handling implemented
        ↓
Tests added
        ↓
End-to-end flow verified
        ↓
Documentation updated
```

---

# 25. Document Dependencies

This PRD is the **product-level source of truth**.

It should lead into the remaining engineering documents:

```text
PRD
 │
 ├── Domain Specification
 │
 ├── System Architecture
 │
 ├── Database Specification
 │
 ├── API Specification
 │
 ├── Frontend Specification
 │
 ├── AI Specification
 │
 └── Engineering Specification
```

Those documents should not contradict the PRD.

If a technical decision requires changing a product requirement, the PRD should be updated rather than allowing the requirement and implementation to silently diverge.

---

# 26. Current Product Definition

At this stage, the product can be summarized as:

> **A real-estate lead-management system that uses a React interface, FastAPI backend, n8n workflow automation, AI-powered natural-language processing, and SQL-based persistence to automatically capture, understand, qualify, respond to, route, and track potential real-estate customers.**

The system is intended to **augment sales teams, not replace them**.

The AI handles language and repetitive processing.

The application handles validation and system state.

Deterministic business logic handles rules and qualification.

The database maintains the source of truth.

n8n orchestrates workflows and integrations.

Salespeople make human decisions where required.