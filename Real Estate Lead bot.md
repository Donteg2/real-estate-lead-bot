# REAL ESTATE LEAD BOT

## Project Overview

**REAL ESTATE LEAD BOT** is an AI-powered digital receptionist and
lead-management system designed for **PrimeHomes Realty**.

The system helps real-estate businesses respond to property enquiries,
understand customer requirements, collect lead information, qualify
prospects, and notify the sales team through an automated workflow.

The goal is to reduce missed enquiries, improve response speed, organize
customer information, and help sales teams focus their attention on the
most valuable leads.

------------------------------------------------------------------------

## 1. Problem Statement

Real-estate businesses receive enquiries through different channels,
often with incomplete information.

Common problems include:

-   Slow responses to potential customers
-   Missed or forgotten enquiries
-   Poorly organized customer information
-   Difficulty identifying serious buyers
-   Manual lead qualification
-   Repetitive questions from sales staff
-   Lack of consistent follow-up
-   Customer information being scattered across different systems

The REAL ESTATE LEAD BOT addresses these problems by providing a
structured, automated lead-capture and qualification process.

------------------------------------------------------------------------

## 2. Product Vision

The vision is to create a reliable digital receptionist that can
communicate naturally with potential customers while converting
conversations into structured, actionable sales leads.

The system should make it possible for a customer to simply say:

> "Hi, I'm looking for a 3-bedroom apartment around Lekki. My budget is
> around ₦80 million."

The system should understand the enquiry, collect any missing
information, create a lead, calculate its qualification level, and make
the information available to the sales team.

------------------------------------------------------------------------

## 3. Core Capabilities

### Customer Conversation

The bot can communicate with customers using natural language.

It can help identify:

-   Customer name
-   Email
-   Phone number
-   Preferred contact method
-   Property type
-   Number of bedrooms
-   Preferred location
-   Budget
-   Currency
-   Buying or renting intent
-   Timeline

### Lead Capture

Once enough information has been collected, the system creates a
structured lead.

Each lead can contain:

-   Contact information
-   Property requirements
-   Customer intent
-   Timeline
-   Lead status
-   Lead priority
-   Qualification score
-   Conversation history
-   Follow-up information

### Lead Qualification

The system evaluates leads using deterministic business rules.

Qualification considers factors such as:

-   Intent strength
-   Budget information
-   Timeline
-   Requirement completeness
-   Location specificity
-   Customer engagement

The resulting priority is:

-   **HOT**
-   **WARM**
-   **COLD**

AI may extract information from conversation, but the backend/business
rules remain responsible for the final qualification decision.

### Sales Dashboard

Sales staff can view and manage leads through a dashboard.

The dashboard can provide:

-   Lead list
-   Lead priority
-   Lead status
-   Qualification score
-   Customer requirements
-   Conversation history
-   Follow-up information
-   Search and filtering

### Notifications

Important lead events can trigger notifications to the appropriate sales
team.

Examples include:

-   New lead created
-   Hot lead identified
-   Follow-up required
-   Lead status changed

### Operational Synchronization

Google Sheets can be used as a supporting operational layer for sales
visibility or reporting.

The SQL database remains the primary source of truth.

------------------------------------------------------------------------

## 4. Example Customer Enquiries

The bot should be able to handle enquiries such as:

### Example 1 --- Apartment Purchase

> "Hi, I'm looking for a 3-bedroom apartment around Lekki. My budget is
> around ₦80 million."

Possible extracted information:

-   Intent: BUY_PROPERTY
-   Property type: APARTMENT
-   Bedrooms: 3
-   Location: Lekki
-   Maximum budget: ₦80,000,000

### Example 2 --- Apartment Search

> "Do you have any 2-bedroom apartments in Ikeja?"

Possible extracted information:

-   Intent: BUY_PROPERTY
-   Property type: APARTMENT
-   Bedrooms: 2
-   Location: Ikeja

The bot should ask for missing information where appropriate.

### Example 3 --- Land

> "I need land around Ibadan, preferably below ₦20 million."

Possible extracted information:

-   Intent: BUY_LAND
-   Property type: LAND
-   Location: Ibadan
-   Maximum budget: ₦20,000,000

### Example 4 --- General Enquiry

> "Hello, I want to buy a house."

The bot should continue the conversation by asking useful qualification
questions instead of creating an incomplete lead immediately.

------------------------------------------------------------------------

## 5. Customer Journey

The typical customer journey is:

1.  Customer opens the chat interface.
2.  Customer explains what they are looking for.
3.  AI extracts relevant requirements.
4.  Bot asks for missing information.
5.  Customer provides contact information.
6.  Backend validates the information.
7.  Lead is created or updated.
8.  Qualification rules calculate the lead score.
9.  Lead receives a HOT, WARM, or COLD priority.
10. Sales team is notified when required.
11. Sales staff reviews the lead.
12. Sales staff follows up with the customer.
13. Lead status is updated throughout the sales process.

------------------------------------------------------------------------

## 6. Sales Team Journey

The sales process is designed to be simple:

1.  Sales agent opens the dashboard.
2.  Agent sees newly created leads.
3.  High-priority leads are identified.
4.  Agent opens the lead details.
5.  Agent reviews customer requirements.
6.  Agent reviews the conversation history.
7.  Agent contacts the customer.
8.  Agent records follow-up information.
9.  Agent updates the lead status.
10. Lead eventually becomes CONVERTED, LOST, or CLOSED.

------------------------------------------------------------------------

## 7. High-Level Architecture

``` text
Customer
   |
   v
React Frontend
   |
   v
FastAPI Backend
   |
   +--------------------+
   |                    |
   v                    v
Business Services      n8n
   |                    |
   |                    +--> AI Services
   |                    +--> Notifications
   |                    +--> Google Sheets
   |
   v
SQL Database
   |
   v
Sales Dashboard
```

### Responsibility Boundaries

**React**

Responsible for:

-   User interface
-   Chat experience
-   Sales dashboard
-   Forms
-   Loading and error states

**FastAPI**

Responsible for:

-   API endpoints
-   Request validation
-   Authentication/authorization
-   Application boundaries
-   Database access
-   Business services

**AI**

Responsible for:

-   Understanding natural language
-   Extracting structured information
-   Detecting customer intent
-   Generating conversational responses

AI must not invent customer information or property availability.

**n8n**

Responsible for:

-   Workflow orchestration
-   Notifications
-   External integrations
-   AI workflow execution
-   Google Sheets synchronization
-   Scheduled follow-ups

**SQL Database**

Responsible for:

-   Leads
-   Customers
-   Conversations
-   Messages
-   Follow-ups
-   Qualification data
-   Persistent application state

SQL is the authoritative source of truth.

**Google Sheets**

Used as a supporting operational/reporting layer rather than the primary
database.

------------------------------------------------------------------------

## 8. Lead Lifecycle

Leads can move through the following statuses:

``` text
NEW
 |
 v
CONTACTED
 |
 v
QUALIFIED
 |
 +------> FOLLOW_UP
 |            |
 |            v
 |        CONVERTED
 |
 +------> LOST
 |
 +------> CLOSED
```

The exact status transition rules are defined in the project's detailed
specifications.

------------------------------------------------------------------------

## 9. Lead Qualification

The initial qualification model uses a score from **0 to 100**.

  Factor                       Maximum Score
  -------------------------- ---------------
  Intent Strength                         20
  Budget                                  20
  Timeline                                20
  Requirement Completeness                15
  Location Specificity                    15
  Engagement                              10
  **Total**                          **100**

Initial priority thresholds:

      Score Priority
  --------- ----------
    80--100 HOT
     50--79 WARM
      0--49 COLD

These thresholds should remain configurable rather than hard-coded
throughout the application.

------------------------------------------------------------------------

## 10. Technology Stack

The planned technology stack includes:

### Frontend

-   React
-   JavaScript/TypeScript
-   Responsive web UI

### Backend

-   Python
-   FastAPI
-   REST API

### Automation

-   n8n

### AI

-   LLM-based natural-language understanding and response generation

### Database

-   SQL relational database

### Supporting Services

-   Google Sheets
-   Email/notification services
-   Authentication system

### Development Tools

-   Git
-   GitHub
-   Virtual environments
-   Automated tests
-   Environment-based configuration

------------------------------------------------------------------------

## 11. MVP Scope

The Minimum Viable Product should provide:

### Customer

-   Chat interface
-   Natural-language enquiry
-   Requirement collection
-   Contact-information collection
-   Confirmation of captured information

### Backend

-   REST API
-   Lead creation
-   Lead retrieval
-   Lead updates
-   Conversation storage
-   Validation
-   Qualification logic

### AI

-   Intent detection
-   Requirement extraction
-   Missing-information detection
-   Conversational responses

### n8n

-   Lead-processing workflow
-   AI orchestration
-   Notification workflow
-   Google Sheets synchronization

### Sales

-   Lead dashboard
-   Lead filtering
-   Lead details
-   Qualification visibility
-   Conversation history
-   Follow-up management

------------------------------------------------------------------------

## 12. Security Principles

The system should follow these principles:

-   Never commit secrets to Git.
-   Use environment variables for credentials.
-   Validate API input.
-   Authenticate protected endpoints.
-   Apply role-based authorization.
-   Protect webhook endpoints.
-   Use HTTPS in production.
-   Restrict CORS appropriately.
-   Avoid exposing unnecessary customer information.
-   Log important events without exposing sensitive credentials.
-   Keep database access controlled.

------------------------------------------------------------------------

## 13. Reliability Principles

The system should be designed so that failures in one integration do not
unnecessarily destroy the core lead record.

Important principles include:

-   SQL remains the source of truth.
-   External integrations should be retryable.
-   n8n workflows should be idempotent where appropriate.
-   Duplicate leads should be handled carefully.
-   AI output should be validated before being trusted.
-   Business rules should be deterministic.
-   Errors should be observable.
-   Critical workflows should have clear failure handling.

------------------------------------------------------------------------

## 14. Project Documentation

The project is supported by detailed technical documents covering:

-   Product requirements
-   System architecture
-   Database and data model
-   API specification
-   Frontend specification
-   AI specification
-   n8n workflow specification
-   Lead qualification
-   UI/UX
-   Development setup
-   Implementation plan
-   Testing
-   Deployment
-   Engineering standards
-   Task tracking

This overview document provides the high-level understanding of the
complete system. Detailed implementation decisions should be taken from
the relevant specification documents.

------------------------------------------------------------------------

## 15. Future Improvements

Potential future versions may include:

-   WhatsApp integration
-   Voice conversations
-   Property listing search
-   Automated property recommendations
-   CRM integrations
-   Advanced analytics
-   Agent performance reporting
-   Automated follow-up campaigns
-   Customer self-service property booking
-   Multi-language support
-   More advanced lead-scoring models
-   Human handoff during live conversations

These features are outside the initial MVP unless explicitly added to
the implementation plan.

------------------------------------------------------------------------

## 16. Success Criteria

The project should be considered successful when:

-   Customers can submit natural-language property enquiries.
-   The system reliably extracts relevant requirements.
-   Missing information is collected through conversation.
-   Leads are stored correctly.
-   Qualification scores are calculated consistently.
-   Sales agents can easily review leads.
-   Hot leads can be identified quickly.
-   Follow-ups can be tracked.
-   Integrations operate reliably.
-   The system is secure and testable.
-   The application can be deployed and maintained without depending
    entirely on manual processes.

------------------------------------------------------------------------

## 17. Core Project Principle

> **AI understands the conversation. The application controls the
> business logic. The database owns the truth. n8n orchestrates the
> integrations.**

This principle should guide future development decisions for the REAL
ESTATE LEAD BOT.
