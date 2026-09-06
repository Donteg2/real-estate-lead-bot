# UI-UX SPECIFICATION

**Project:** REAL ESTATE LEAD BOT\
**Client:** PrimeHomes Realty\
**Version:** 0.1\
**Status:** Draft / Implementation Ready

------------------------------------------------------------------------

## 1. Purpose

This document defines the user interface and user experience
requirements for the REAL ESTATE LEAD BOT.

The system has two primary user experiences:

1.  **Customer Experience** --- a simple conversational interface for
    real-estate enquiries.
2.  **Sales Experience** --- a dashboard for viewing, qualifying,
    managing, and following up with leads.

The interface should feel professional, simple, trustworthy, responsive,
and easy to use on mobile devices.

------------------------------------------------------------------------

# 2. UX Goals

The product should:

-   Make starting an enquiry easy
-   Minimize unnecessary form filling
-   Make the conversation feel natural
-   Ask only useful follow-up questions
-   Clearly communicate when the bot is processing
-   Prevent users from becoming confused about what happens next
-   Help sales agents quickly identify important leads
-   Make lead information easy to scan
-   Make follow-up actions obvious
-   Work well on mobile and desktop
-   Provide clear loading, empty, success, and error states
-   Follow basic accessibility principles

------------------------------------------------------------------------

# 3. Users

## 3.1 Customer

The customer may:

-   Ask about buying property
-   Ask about renting property
-   Ask about land
-   Ask about selling property
-   Provide property requirements
-   Provide contact information
-   Ask questions
-   Continue an existing conversation

The customer should not need to understand the underlying AI, FastAPI,
n8n, or database architecture.

------------------------------------------------------------------------

## 3.2 Sales Agent

The sales agent may:

-   View leads
-   Search leads
-   Filter leads
-   Open lead details
-   Review conversations
-   View lead priority
-   View qualification score
-   Update lead status
-   Create follow-ups
-   Review customer requirements

------------------------------------------------------------------------

## 3.3 Sales Manager / Administrator

Managers and administrators may additionally:

-   Review overall lead activity
-   Monitor HOT leads
-   Review sales follow-ups
-   Monitor team activity
-   Manage operational data according to their permissions

------------------------------------------------------------------------

# 4. Design Principles

## 4.1 Simplicity

The customer should be able to start a conversation immediately.

Avoid asking for a large form before the customer can interact with the
bot.

------------------------------------------------------------------------

## 4.2 Conversational First

The primary customer experience is chat.

Example:

``` text
Customer:
I'm looking for a 3-bedroom apartment in Lekki.

Bot:
Great. Are you looking to buy or rent, and what budget range
would you like us to work with?
```

------------------------------------------------------------------------

## 4.3 Progressive Information Collection

Do not ask every question at once.

Collect information naturally as the conversation progresses.

------------------------------------------------------------------------

## 4.4 Transparency

The customer should understand:

-   When a message has been sent
-   When the bot is processing
-   When an error occurs
-   When additional information is needed
-   When a sales representative may follow up

------------------------------------------------------------------------

## 4.5 Trust

The UI must avoid making unsupported claims.

The bot should not visually imply that a property is available unless
the system has verified that information.

------------------------------------------------------------------------

# 5. Visual Direction

The visual style should communicate:

``` text
Professional
Modern
Trustworthy
Clean
Warm
Premium but accessible
```

Avoid:

-   Excessive animations
-   Overcrowded dashboards
-   Excessive gradients
-   Tiny text
-   Too many colors
-   Unnecessary decorative elements

The final color palette should be defined by the project's brand
requirements. Components should use design tokens so the palette can be
changed without rewriting the UI.

------------------------------------------------------------------------

# 6. Typography

Use a highly readable modern sans-serif font.

Recommended hierarchy:

``` text
Page Title
     |
     +-- Section Heading
             |
             +-- Card Heading
                     |
                     +-- Body Text
                             |
                             +-- Supporting Text
```

Typography must maintain readable contrast and spacing on mobile.

Avoid using font size alone to communicate critical information.

------------------------------------------------------------------------

# 7. Customer Chat Experience

## 7.1 Chat Page

Primary route:

``` text
/chat
```

Recommended structure:

``` text
+--------------------------------------+
| PrimeHomes Realty              Help  |
+--------------------------------------+
|                                      |
| Bot message                          |
|                                      |
|              Customer message        |
|                                      |
| Bot message                          |
|                                      |
| Typing...                            |
|                                      |
+--------------------------------------+
| Type your message...            Send |
+--------------------------------------+
```

------------------------------------------------------------------------

## 7.2 Chat Header

The header should contain:

-   PrimeHomes Realty identity
-   Bot/service name
-   Optional availability indicator
-   Help or information action

Avoid exposing technical information.

------------------------------------------------------------------------

## 7.3 Welcome State

When a customer opens the chat, provide a short welcome message.

Example:

``` text
Hi! Welcome to PrimeHomes Realty.

I can help you with buying, renting, land,
or general property enquiries.

What are you looking for?
```

Optional quick-start actions:

``` text
Buy a property
Rent a property
Buy land
Ask a question
```

Quick actions should insert or send an appropriate message rather than
creating a separate complex flow.

------------------------------------------------------------------------

# 8. Message Bubbles

## Customer Message

Should visually distinguish:

-   User message
-   Timestamp where useful

## Bot Message

Should visually distinguish:

-   Bot response
-   Timestamp where useful

Do not use color alone to distinguish message ownership.

------------------------------------------------------------------------

# 9. Chat Input

The input area should support:

-   Text entry
-   Send button
-   Enter-to-send where appropriate
-   Multi-line input
-   Disabled state while necessary
-   Clear error state

The send action should be obvious.

Do not permanently disable the input during long processing unless
necessary.

------------------------------------------------------------------------

# 10. Typing / Processing State

When waiting for the backend:

``` text
PrimeHomes Bot is typing...
```

or a subtle typing indicator may be shown.

The UI must distinguish between:

``` text
Sending...
Processing...
Response received
Error
```

Avoid animations that continue indefinitely when the request has already
failed.

------------------------------------------------------------------------

# 11. Chat Error State

If the request fails:

``` text
Sorry, I couldn't process that message.

Please try again.
```

Provide:

``` text
[ Try Again ]
```

Do not expose:

-   Stack traces
-   API errors
-   Database errors
-   n8n execution details
-   AI provider errors

Technical information belongs in logs.

------------------------------------------------------------------------

# 12. Lead Information Collection

The bot should collect information conversationally.

Typical information:

``` text
Name
Email
Phone
Property Type
Bedrooms
Location
Budget
Transaction Type
Timeline
```

If the bot needs multiple pieces of information, ask a small number of
related questions rather than presenting a long form.

Example:

``` text
What area are you interested in, and what budget
range would you like to work with?
```

------------------------------------------------------------------------

# 13. Optional Structured Lead Form

A structured form may be used when conversational collection becomes
inefficient.

Example sections:

``` text
Your Details
----------------
Name
Email
Phone

Property Requirements
----------------
Buy / Rent
Property Type
Bedrooms
Location
Budget
Timeline
```

The form should complement the conversation, not replace it.

------------------------------------------------------------------------

# 14. Confirmation

When sufficient information has been collected, the customer may see a
concise summary.

Example:

``` text
Here's what I have:

Property: 3-bedroom apartment
Location: Lekki
Budget: ₦80M
Looking to: Buy
Timeline: Within 1 month

Would you like a PrimeHomes representative to follow up?
```

The customer should be able to correct information.

------------------------------------------------------------------------

# 15. Customer Follow-Up Expectations

The UI should clearly communicate when sales follow-up is expected.

Example:

``` text
Thanks! We've received your requirements.
A PrimeHomes representative can follow up with you
using the contact details you provided.
```

Do not promise a specific response time unless the business has defined
and verified one.

------------------------------------------------------------------------

# 16. Sales Dashboard

Primary route:

``` text
/dashboard
```

Recommended layout:

``` text
+----------------------------------------------------+
| PrimeHomes Realty          Dashboard      Profile |
+----------------------------------------------------+
|                                                    |
| New Leads | HOT Leads | WARM Leads | Follow-ups   |
|                                                    |
+----------------------------------------------------+
| Filters                                            |
| Status | Priority | Intent | Location | Agent     |
+----------------------------------------------------+
| Lead Table                                         |
| Customer | Intent | Property | Budget | Priority  |
|----------------------------------------------------|
| ...                                                |
+----------------------------------------------------+
```

------------------------------------------------------------------------

# 17. Dashboard Metrics

Suggested cards:

-   New Leads
-   HOT Leads
-   WARM Leads
-   Follow-ups Due

Metrics should be loaded from the backend.

The frontend must not independently calculate business-critical metrics.

------------------------------------------------------------------------

# 18. Lead Table

Suggested columns:

  Column     Purpose
  ---------- ---------------------------------
  Customer   Identify lead
  Intent     Understand customer goal
  Property   Understand property requirement
  Location   Desired area
  Budget     Financial requirement
  Timeline   Urgency
  Score      Qualification score
  Priority   HOT/WARM/COLD
  Status     Lead lifecycle
  Agent      Assigned sales agent
  Created    Lead creation date

On smaller screens, columns may be collapsed or replaced by lead cards.

------------------------------------------------------------------------

# 19. Priority Display

Priority should be visually recognizable:

``` text
HOT
WARM
COLD
```

Do not rely only on color.

Use:

-   Text label
-   Icon or visual indicator where appropriate
-   Accessible contrast

The priority value must come from the backend.

The frontend must not calculate the lead score.

------------------------------------------------------------------------

# 20. Lead Filters

Supported filters may include:

-   Status
-   Priority
-   Intent
-   Location
-   Timeline
-   Assigned agent

Filters should be easy to clear.

Example:

``` text
Priority: HOT
Status: NEW

[ Clear Filters ]
```

------------------------------------------------------------------------

# 21. Lead Search

Search should be handled by the backend.

Searchable values may include:

-   Customer name
-   Email
-   Phone
-   Lead ID
-   Location

Avoid loading the entire database into the browser merely to perform
search.

------------------------------------------------------------------------

# 22. Lead Details Page

Primary route:

``` text
/leads/:leadId
```

Recommended sections:

``` text
Lead Header
    |
    +-- Customer Information
    |
    +-- Property Requirements
    |
    +-- Qualification
    |
    +-- Conversation
    |
    +-- Follow-ups
    |
    +-- Lead Activity
```

------------------------------------------------------------------------

# 23. Lead Header

Should show:

``` text
Customer Name
Lead ID
Priority
Status
Assigned Agent
Created Date
```

Available actions may include:

``` text
Change Status
Assign Agent
Create Follow-up
```

Actions must respect user permissions.

------------------------------------------------------------------------

# 24. Customer Information Card

Display:

-   Name
-   Email
-   Phone
-   Preferred contact method

Avoid unnecessarily exposing sensitive information to users who do not
have permission.

------------------------------------------------------------------------

# 25. Property Requirements Card

Display:

-   Transaction type
-   Intent
-   Property type
-   Bedrooms
-   Location
-   Budget
-   Timeline

Unknown fields should be shown clearly.

Example:

``` text
Budget: Not provided
```

Do not display fake values.

------------------------------------------------------------------------

# 26. Qualification Card

Display:

``` text
Score: 86 / 100
Priority: HOT
```

Optional:

``` text
Qualification reason:
Strong buying intent, clear budget, specific location,
and immediate timeline.
```

If factor scores are exposed, they should be clearly labeled.

------------------------------------------------------------------------

# 27. Conversation History

Display the conversation chronologically.

Example:

``` text
Customer:
I'm looking for a 3-bedroom apartment in Lekki.

Bot:
Are you looking to buy or rent?

Customer:
Buy. My budget is around ₦80M.
```

The sales agent should be able to understand the lead without reading
unrelated technical logs.

------------------------------------------------------------------------

# 28. Follow-Up UI

Follow-up section should display:

-   Follow-up type
-   Assigned agent
-   Scheduled time
-   Status
-   Notes

Example:

``` text
Follow-up
----------------
Type: CALL
Agent: Sales Agent
Scheduled: Tomorrow
Status: PENDING

[ Mark Complete ]
```

------------------------------------------------------------------------

# 29. Lead Status

Supported statuses:

``` text
NEW
CONTACTED
QUALIFIED
FOLLOW_UP
CONVERTED
LOST
CLOSED
```

Status transitions are controlled by backend business rules.

The UI should prevent invalid transitions where the backend rejects
them.

------------------------------------------------------------------------

# 30. Responsive Design

The application must support:

-   Mobile phones
-   Tablets
-   Laptops
-   Desktop screens

### Mobile

Priorities:

1.  Chat usability
2.  Readable text
3.  Large touch targets
4.  Simple navigation
5.  Minimal horizontal scrolling

### Desktop

Priorities:

1.  Efficient sales dashboard
2.  Lead table
3.  Filtering
4.  Lead detail visibility
5.  Multi-column layouts

------------------------------------------------------------------------

# 31. Accessibility

The UI should follow accessible design principles.

Requirements:

-   Keyboard navigation
-   Visible focus states
-   Semantic HTML
-   Proper form labels
-   Accessible buttons
-   Sufficient text contrast
-   Meaningful error messages
-   Screen-reader-friendly labels
-   Do not rely solely on color
-   Appropriate touch target sizes

Images and icons should have appropriate alternative text or accessible
labels where needed.

------------------------------------------------------------------------

# 32. Loading States

Every asynchronous view should have an intentional loading state.

Examples:

``` text
Loading conversation...
Loading leads...
Loading lead details...
Saving follow-up...
```

Use skeletons, spinners, or progress indicators appropriately.

Avoid blank screens.

------------------------------------------------------------------------

# 33. Empty States

Examples:

### No Leads

``` text
No leads found.

Try changing your filters or search criteria.
```

### No Follow-Ups

``` text
No follow-ups scheduled.
```

### No Conversation

``` text
No conversation history available.
```

Empty states should explain what happened and, where useful, what the
user can do next.

------------------------------------------------------------------------

# 34. Error States

Errors should be:

-   Clear
-   Brief
-   Actionable
-   Non-technical

Example:

``` text
We couldn't load the leads.

[ Try Again ]
```

Do not expose internal implementation details.

------------------------------------------------------------------------

# 35. Notifications

The sales UI may provide notifications for:

-   New HOT lead
-   Assigned lead
-   Follow-up due
-   Workflow issue requiring attention

Notification priority should match the underlying business event.

------------------------------------------------------------------------

# 36. Navigation

Customer navigation should remain minimal.

Possible customer routes:

``` text
/
 /chat
```

Sales navigation may include:

``` text
/dashboard
/leads/:leadId
```

Additional routes may be added as the product grows.

------------------------------------------------------------------------

# 37. Frontend Architecture

Recommended React structure:

``` text
src/
│
├── components/
│   ├── chat/
│   ├── leads/
│   └── common/
│
├── pages/
│
├── api/
│
├── hooks/
│
├── utils/
│
├── styles/
│
├── App.jsx
└── main.jsx
```

------------------------------------------------------------------------

# 38. Component Responsibilities

### Chat Components

``` text
ChatHeader
MessageList
MessageBubble
ChatInput
TypingIndicator
```

### Lead Components

``` text
LeadTable
LeadFilters
LeadCard
LeadStatus
```

### Common Components

``` text
Button
Input
Modal
Loading
ErrorMessage
```

Components should be reusable and avoid containing unrelated business
logic.

------------------------------------------------------------------------

# 39. API Interaction

The frontend should use a centralized API client.

Suggested structure:

``` text
api/
├── client.js
├── chat.js
├── leads.js
├── conversations.js
└── followUps.js
```

React should not call raw backend URLs throughout individual components.

------------------------------------------------------------------------

# 40. Frontend State

For the MVP, use React state and custom hooks where sufficient.

Suggested hooks:

``` text
useChat
useLeads
useConversation
```

A larger state-management library should only be introduced when project
complexity justifies it.

------------------------------------------------------------------------

# 41. UX Rules for AI Responses

AI-generated responses displayed to customers should:

-   Be concise
-   Be helpful
-   Ask relevant questions
-   Avoid unsupported claims
-   Avoid inventing property availability
-   Avoid inventing prices
-   Avoid pretending a human has been contacted unless that action
    actually occurred
-   Clearly communicate when more information is needed

Example:

``` text
Thanks! What budget range are you considering?
```

is preferable to a long generic response.

------------------------------------------------------------------------

# 42. Security UX

The UI must never display:

-   API keys
-   Database credentials
-   n8n credentials
-   Internal workflow details
-   Stack traces
-   Private system configuration

Authentication and authorization failures should use user-friendly
messages.

------------------------------------------------------------------------

# 43. UX Analytics

Future versions may track product events such as:

``` text
chat_started
message_sent
lead_created
lead_completed
follow_up_requested
sales_contact_requested
```

Analytics must respect applicable privacy requirements and should avoid
collecting unnecessary personal data.

------------------------------------------------------------------------

# 44. UI/UX Testing

The UI should be tested for:

### Customer

-   [ ] Start chat
-   [ ] Send message
-   [ ] Receive response
-   [ ] Handle loading
-   [ ] Handle errors
-   [ ] Provide lead information
-   [ ] Correct information
-   [ ] Complete enquiry

### Sales

-   [ ] Open dashboard
-   [ ] View metrics
-   [ ] Search leads
-   [ ] Filter leads
-   [ ] Open lead details
-   [ ] View conversation
-   [ ] View qualification
-   [ ] Update status
-   [ ] Create follow-up

### Responsive

-   [ ] Mobile
-   [ ] Tablet
-   [ ] Desktop

### Accessibility

-   [ ] Keyboard navigation
-   [ ] Focus states
-   [ ] Form labels
-   [ ] Contrast
-   [ ] Screen-reader labels

------------------------------------------------------------------------

# 45. UI/UX Task Tracker

  ID       Task                                   Priority   Status
  -------- -------------------------------------- ---------- -------------
  UX-001   Define design tokens                   High       NOT_STARTED
  UX-002   Build chat layout                      High       NOT_STARTED
  UX-003   Build message components               High       NOT_STARTED
  UX-004   Build chat input                       High       NOT_STARTED
  UX-005   Build loading/error states             High       NOT_STARTED
  UX-006   Build lead information collection UI   High       NOT_STARTED
  UX-007   Build dashboard layout                 High       NOT_STARTED
  UX-008   Build lead table                       High       NOT_STARTED
  UX-009   Build lead filters                     High       NOT_STARTED
  UX-010   Build lead details page                High       NOT_STARTED
  UX-011   Build qualification display            High       NOT_STARTED
  UX-012   Build follow-up UI                     Medium     NOT_STARTED
  UX-013   Implement responsive layouts           High       NOT_STARTED
  UX-014   Implement accessibility requirements   High       NOT_STARTED
  UX-015   Perform usability testing              Medium     NOT_STARTED

------------------------------------------------------------------------

# 46. Definition of Done

The UI/UX implementation is considered complete when:

-   [ ] Customer can start a chat
-   [ ] Customer can send messages
-   [ ] Bot responses are displayed clearly
-   [ ] Loading states work
-   [ ] Error states work
-   [ ] Customer information can be collected
-   [ ] Sales dashboard is functional
-   [ ] Leads can be searched
-   [ ] Leads can be filtered
-   [ ] Lead details are accessible
-   [ ] Qualification information is displayed
-   [ ] Conversation history is displayed
-   [ ] Follow-ups are displayed/managed
-   [ ] Mobile layout works
-   [ ] Desktop layout works
-   [ ] Accessibility requirements are addressed
-   [ ] Frontend does not calculate business-critical qualification
    logic
-   [ ] Frontend does not expose secrets
-   [ ] UI tests pass

------------------------------------------------------------------------

# 47. Core UI/UX Rules

1.  **Conversation should be the easiest way to start.**
2.  **Ask only useful questions.**
3.  **Do not overwhelm customers with forms.**
4.  **Never expose technical errors to customers.**
5.  **Never display invented property information.**
6.  **Backend owns business decisions.**
7.  **Frontend presents backend results.**
8.  **Do not rely on color alone for meaning.**
9.  **Design mobile-first for the customer experience.**
10. **Keep the sales dashboard information-dense but organized.**
11. **Use reusable components.**
12. **Keep accessibility in the design from the beginning.**

------------------------------------------------------------------------

## Document Status

**Document:** UI-UX-SPEC.md\
**Version:** 0.1\
**Status:** Draft / Implementation Ready\
**Owner:** Project Engineering Team

**Related Documents:**

-   PRD.md
-   SAD.md
-   DOMAIN.md
-   API.md
-   FRONTEND.md
-   AI-SPEC.md
-   LEAD-QUALIFICATION-SPEC.md
-   N8N-WORKFLOWS.md
-   ENGINEERING.md
-   IMPLEMENTATION.md
-   TASK.md
-   TESTING.md
-   DEPLOYMENT.md
-   DEPLOYMENT_SPEC.md
-   DEVELOPMENT_SETUP.md
