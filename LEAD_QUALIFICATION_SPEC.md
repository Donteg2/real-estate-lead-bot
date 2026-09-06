# LEAD QUALIFICATION SPECIFICATION

**Project:** REAL ESTATE LEAD BOT\
**Client:** PrimeHomes Realty\
**Version:** 0.1\
**Status:** Draft / Implementation Ready

------------------------------------------------------------------------

## 1. Purpose

This document defines how the REAL ESTATE LEAD BOT qualifies, scores,
prioritizes, and routes real-estate leads.

The qualification system converts unstructured customer conversations
into a consistent business decision that helps the sales team determine
which leads require immediate attention.

The core principle is:

``` text
AI = Understand and Extract
Business Rules = Decide
SQL = Store the Result
n8n = Orchestrate
React = Present
```

AI must not independently decide the final commercial priority of a
lead.

------------------------------------------------------------------------

# 2. Qualification Objectives

The qualification system should:

-   Identify customer intent
-   Understand the customer's property requirements
-   Measure requirement completeness
-   Evaluate buying/renting urgency
-   Consider stated budget
-   Consider location specificity
-   Consider customer engagement
-   Assign a lead score
-   Assign HOT, WARM, or COLD priority
-   Provide a qualification reason
-   Support sales routing
-   Trigger appropriate notifications and follow-up

------------------------------------------------------------------------

# 3. Lead Qualification Inputs

Qualification uses structured information extracted from the
conversation.

### Customer Information

-   Name
-   Email
-   Phone
-   Preferred contact method

### Property Requirements

-   Property type
-   Bedrooms
-   Location
-   Budget minimum
-   Budget maximum
-   Currency
-   Transaction type

### Intent

Supported intents:

``` text
BUY_PROPERTY
RENT_PROPERTY
BUY_LAND
SELL_PROPERTY
GENERAL_ENQUIRY
```

### Timeline

Supported values:

``` text
IMMEDIATE
WITHIN_1_MONTH
WITHIN_3_MONTHS
RESEARCHING
UNKNOWN
```

### Engagement

The system may consider:

-   Number of meaningful messages
-   Response to follow-up questions
-   Completion of required information
-   Request for viewing/contact
-   Repeated interest

------------------------------------------------------------------------

# 4. Qualification Pipeline

The qualification flow is:

``` text
Customer Message
      |
      v
AI Understanding
      |
      v
Structured Extraction
      |
      v
Output Validation
      |
      v
Requirement Completeness
      |
      v
Qualification Rules
      |
      v
Score Calculation
      |
      v
Priority Assignment
      |
      v
Lead Routing
      |
      v
SQL Storage
      |
      v
Sales Notification / Follow-up
```

------------------------------------------------------------------------

# 5. Qualification Principles

## 5.1 AI Is Not the Final Decision Maker

AI may extract:

``` text
Intent: BUY_PROPERTY
Location: Lekki
Bedrooms: 3
Budget: ₦80,000,000
Timeline: IMMEDIATE
```

The application then applies deterministic qualification rules.

The AI must not simply return:

``` text
Priority: HOT
```

and have that value trusted without validation.

------------------------------------------------------------------------

## 5.2 Missing Information

Missing information should reduce qualification completeness but must
not automatically make a lead cold.

Example:

``` text
"I want to buy a house in Lekki."
```

This is still a potentially valuable lead.

The bot should ask for useful missing information such as:

-   Budget
-   Property type
-   Bedrooms
-   Timeline
-   Contact details

------------------------------------------------------------------------

## 5.3 Unknown Information

Unknown values must be represented explicitly.

Examples:

``` text
timeline = UNKNOWN
budget_min = null
budget_max = null
bedrooms = null
```

Do not replace missing information with invented values.

------------------------------------------------------------------------

# 6. Qualification Factors

The initial scoring model uses six factors:

  Factor                       Maximum Points
  -------------------------- ----------------
  Intent Strength                          20
  Budget                                   20
  Timeline                                 20
  Requirement Completeness                 15
  Location Specificity                     15
  Engagement                               10
  **Total**                           **100**

These values are initial business assumptions and can be adjusted after
real-world testing.

------------------------------------------------------------------------

# 7. Intent Strength Score

Intent measures how clearly the customer expresses a meaningful
real-estate action.

### Suggested scoring

  Intent              Points
  ----------------- --------
  BUY_PROPERTY            20
  BUY_LAND                20
  RENT_PROPERTY           18
  SELL_PROPERTY           16
  GENERAL_ENQUIRY          8
  UNKNOWN                  0

Examples:

### Strong

``` text
"I want to buy a 3-bedroom apartment in Lekki."
```

High intent.

### Weak

``` text
"Just checking what houses are available."
```

Lower intent.

------------------------------------------------------------------------

# 8. Timeline Score

Timeline measures urgency.

  Timeline            Points
  ----------------- --------
  IMMEDIATE               20
  WITHIN_1_MONTH          16
  WITHIN_3_MONTHS         10
  RESEARCHING              4
  UNKNOWN                  0

Example:

``` text
"I need to move within two weeks."
```

This indicates strong urgency.

------------------------------------------------------------------------

# 9. Budget Score

Budget indicates whether the customer has provided a usable financial
range.

The initial MVP should primarily score **budget completeness and
clarity**, not assume that a higher budget automatically means a better
customer.

Suggested scoring:

  Budget Information               Points
  ------------------------------ --------
  Clear usable range                   20
  Clear maximum/minimum                16
  Approximate budget                   12
  Budget mentioned but unclear          6
  No budget provided                    0

Example:

``` text
"My budget is around ₦80 million."
```

This is a usable approximate budget.

The exact commercial value of a budget should depend on actual
PrimeHomes property inventory and business rules. The system must not
assume that ₦80 million is automatically HOT without a defined business
rule.

------------------------------------------------------------------------

# 10. Requirement Completeness Score

This measures how much useful information has been collected.

Suggested required requirement fields:

-   Transaction type
-   Intent
-   Property type
-   Location
-   Budget
-   Bedrooms where relevant
-   Timeline
-   Contact information

Suggested scoring:

  Completeness                        Points
  --------------------------------- --------
  Nearly all required information         15
  Most information available              11
  Moderate information                     7
  Very limited information                 3
  No usable requirements                   0

The exact calculation should be implemented deterministically.

------------------------------------------------------------------------

# 11. Location Specificity Score

Location specificity measures how clearly the customer has identified
the desired area.

  Location Detail                Points
  ---------------------------- --------
  Specific neighborhood/area         15
  Specific city                      11
  General region                      6
  Very broad location                 3
  Unknown                             0

Examples:

``` text
Lekki Phase 1
```

is more specific than:

``` text
Lagos
```

The system must preserve the customer's original location rather than
inventing a more specific area.

------------------------------------------------------------------------

# 12. Engagement Score

Engagement measures evidence that the customer is actively progressing
the enquiry.

Suggested scoring:

  Engagement                                                Points
  ------------------------------------------------------- --------
  Requests viewing/contact or actively provides details         10
  Responds to follow-up questions                                8
  Provides several requirements voluntarily                      6
  Sends a basic enquiry                                          3
  No meaningful engagement                                       0

Engagement should not be manipulated through artificial chatbot
messages.

------------------------------------------------------------------------

# 13. Total Score

The total score is:

``` text
Total Score =
Intent Score
+ Budget Score
+ Timeline Score
+ Completeness Score
+ Location Score
+ Engagement Score
```

Maximum:

``` text
100
```

Minimum:

``` text
0
```

Example:

``` text
Intent          = 20
Budget          = 20
Timeline        = 20
Completeness    = 15
Location        = 15
Engagement      = 10
--------------------------------
Total           = 100
```

------------------------------------------------------------------------

# 14. Priority Classification

Initial thresholds:

  Score     Priority
  --------- ----------
  80--100   HOT
  50--79    WARM
  0--49     COLD

These thresholds are configurable business rules.

They should be reviewed after collecting real lead outcomes.

------------------------------------------------------------------------

# 15. Qualification Examples

## Example 1 --- Strong Buying Lead

Customer:

``` text
Hi, I'm looking for a 3-bedroom apartment around Lekki.
My budget is around ₦80 million and I want to buy within the next two weeks.
```

Extracted:

``` text
Intent: BUY_PROPERTY
Transaction: BUY
Property Type: Apartment
Bedrooms: 3
Location: Lekki
Budget: ₦80M
Timeline: IMMEDIATE
```

Expected result:

``` text
High qualification
Likely HOT
```

The exact score depends on the deterministic scoring implementation.

------------------------------------------------------------------------

## Example 2 --- Rental Enquiry

Customer:

``` text
Do you have any 2-bedroom apartments in Ikeja for rent?
```

Extracted:

``` text
Intent: RENT_PROPERTY
Transaction: RENT
Property Type: Apartment
Bedrooms: 2
Location: Ikeja
Budget: Unknown
Timeline: Unknown
```

Expected result:

``` text
Moderate qualification
Likely WARM or COLD depending on engagement/completeness
```

The system should request missing useful information.

------------------------------------------------------------------------

## Example 3 --- Land Enquiry

Customer:

``` text
I need land around Ibadan, preferably below ₦20 million.
```

Extracted:

``` text
Intent: BUY_LAND
Transaction: BUY
Property Type: LAND
Location: Ibadan
Budget Max: ₦20M
```

Expected result:

``` text
Meaningful lead
Priority determined by score and business rules
```

The bot should ask for timeline and contact information if missing.

------------------------------------------------------------------------

## Example 4 --- Very Early Enquiry

Customer:

``` text
Hello, I want to buy a house.
```

Extracted:

``` text
Intent: BUY_PROPERTY
Transaction: BUY
Property Type: Unknown
Location: Unknown
Budget: Unknown
Bedrooms: Unknown
Timeline: Unknown
```

Expected result:

``` text
Low completeness
Potentially COLD initially
```

The bot should continue qualification rather than dismissing the
customer.

------------------------------------------------------------------------

# 16. Hard Qualification Rules

The following rules override or constrain the normal scoring process.

### Rule 1 --- No Invented Information

If a value is not provided or reliably inferred from the customer's
message, store it as unknown/null.

### Rule 2 --- AI Cannot Override Business Rules

AI output must pass through deterministic qualification logic.

### Rule 3 --- Invalid Data Cannot Increase Score

Invalid budget, impossible bedroom values, or malformed data must not
receive points until corrected.

### Rule 4 --- Missing Information Requires Follow-up

If important information is missing, the bot should ask a targeted
question.

### Rule 5 --- Priority Is Backend-Owned

The frontend displays the priority returned by the backend.

### Rule 6 --- SQL Is the Source of Truth

The final score and priority must be stored in SQL.

### Rule 7 --- Google Sheets Is Secondary

A Sheets synchronization failure must not change the SQL qualification
result.

------------------------------------------------------------------------

# 17. Special Lead Rules

Some leads may require special handling.

## HOT Lead

When a lead qualifies as HOT:

``` text
Lead Scored
    |
    v
Priority = HOT
    |
    v
Save to SQL
    |
    v
Notify Sales
    |
    v
Create/Recommend Immediate Follow-up
```

------------------------------------------------------------------------

## COLD Lead

COLD does not mean useless.

A cold lead may:

-   Receive additional qualification questions
-   Enter a standard follow-up sequence
-   Become warmer as more information is collected
-   Be re-scored when the customer responds

------------------------------------------------------------------------

## Returning Lead

If a customer continues an existing conversation:

-   Update the existing lead
-   Preserve previous information
-   Add newly extracted information
-   Recalculate qualification
-   Do not create unnecessary duplicate leads

------------------------------------------------------------------------

# 18. Re-Qualification

Lead qualification should run again when meaningful information changes.

Examples:

``` text
Budget added
Timeline changed
Location clarified
Property requirement added
Customer requests viewing
Customer provides contact details
```

Example:

``` text
Initial:
Score = 42
Priority = COLD

Customer provides budget + timeline:

New Score = 78
Priority = WARM
```

A later interaction could move the lead to HOT.

------------------------------------------------------------------------

# 19. Lead Status vs Priority

Status and priority are different concepts.

### Status

Represents the lifecycle:

``` text
NEW
CONTACTED
QUALIFIED
FOLLOW_UP
CONVERTED
LOST
CLOSED
```

### Priority

Represents current qualification:

``` text
HOT
WARM
COLD
```

Example:

``` text
Status: QUALIFIED
Priority: HOT
```

A lead can be HOT while still waiting for sales contact.

------------------------------------------------------------------------

# 20. Qualification Output

The qualification service should return structured data similar to:

``` json
{
  "lead_id": "lead_123",
  "score": 86,
  "priority": "HOT",
  "factors": {
    "intent": 20,
    "budget": 20,
    "timeline": 20,
    "completeness": 13,
    "location": 15,
    "engagement": 8
  },
  "missing_fields": [],
  "reason": "Strong buying intent, clear budget, specific location, and immediate timeline."
}
```

The exact response schema should match the API and database models.

------------------------------------------------------------------------

# 21. Missing Fields Output

If information is incomplete:

``` json
{
  "lead_id": "lead_123",
  "score": 44,
  "priority": "COLD",
  "missing_fields": [
    "budget",
    "timeline",
    "phone"
  ],
  "next_action": "Ask for budget and intended purchase timeline."
}
```

The next question should be useful and concise.

------------------------------------------------------------------------

# 22. Sales Routing

Initial routing rules:

``` text
HOT
 |
 +--> Immediate sales notification
 |
 +--> Priority follow-up

WARM
 |
 +--> Standard sales queue
 |
 +--> Follow-up

COLD
 |
 +--> Continue qualification
 |
 +--> Standard follow-up if appropriate
```

Future versions may route based on:

-   Location
-   Property type
-   Sales agent specialization
-   Agent workload
-   Language
-   Lead source

------------------------------------------------------------------------

# 23. Qualification and n8n

n8n orchestrates the qualification process but should not become the
only place where scoring logic exists.

Recommended flow:

``` text
n8n
 |
 v
AI Extraction
 |
 v
FastAPI / Qualification Service
 |
 v
Deterministic Score
 |
 v
Priority
 |
 v
SQL
 |
 v
n8n
 |
 +--> Notification
 +--> Sheets Sync
 +--> Follow-up
```

This keeps the qualification rules testable and maintainable.

------------------------------------------------------------------------

# 24. Qualification and Database

The qualification result should be persisted.

Important fields include:

``` text
lead_id
score
priority
qualification_reason
qualified_at
updated_at
```

If detailed factor scores are stored, they should be associated with the
lead score record.

The database should preserve enough information to understand why a lead
received its current qualification.

------------------------------------------------------------------------

# 25. Qualification History

Future versions should support historical scoring.

Example:

``` text
09:00
Score 38 — COLD

09:15
Customer provides budget
Score 54 — WARM

09:30
Customer confirms immediate purchase
Score 78 — WARM

09:45
Customer requests viewing
Score 88 — HOT
```

This creates an auditable qualification history.

------------------------------------------------------------------------

# 26. Testing Requirements

The qualification system must be tested against:

### Complete leads

-   [ ] Complete buying lead
-   [ ] Complete rental lead
-   [ ] Complete land lead

### Incomplete leads

-   [ ] Missing budget
-   [ ] Missing location
-   [ ] Missing timeline
-   [ ] Missing contact details
-   [ ] Missing property type

### Invalid data

-   [ ] Invalid budget
-   [ ] Negative budget
-   [ ] Invalid bedroom count
-   [ ] Invalid timeline
-   [ ] Invalid transaction type

### Behavior

-   [ ] HOT classification
-   [ ] WARM classification
-   [ ] COLD classification
-   [ ] Re-qualification
-   [ ] Returning lead
-   [ ] Duplicate message
-   [ ] AI output failure
-   [ ] Missing AI fields

------------------------------------------------------------------------

# 27. Business Rule Configuration

Scoring values and thresholds should be configurable rather than
scattered throughout the codebase.

Example configuration:

``` text
HOT_THRESHOLD=80
WARM_THRESHOLD=50

INTENT_MAX=20
BUDGET_MAX=20
TIMELINE_MAX=20
COMPLETENESS_MAX=15
LOCATION_MAX=15
ENGAGEMENT_MAX=10
```

Production configuration should be controlled and documented.

------------------------------------------------------------------------

# 28. Future Improvements

Potential future qualification enhancements:

-   Property inventory matching
-   Historical conversion-rate scoring
-   Lead source scoring
-   Agent availability
-   Customer engagement prediction
-   Response-time scoring
-   Location/property demand
-   Budget-to-inventory fit
-   Sales outcome feedback
-   Machine-learning-assisted ranking

These are outside the initial MVP unless explicitly approved.

------------------------------------------------------------------------

# 29. Qualification Task Tracker

  ID         Task                                 Priority   Status
  ---------- ------------------------------------ ---------- -------------
  QUAL-001   Implement qualification data model   High       NOT_STARTED
  QUAL-002   Implement intent scoring             High       NOT_STARTED
  QUAL-003   Implement budget scoring             High       NOT_STARTED
  QUAL-004   Implement timeline scoring           High       NOT_STARTED
  QUAL-005   Implement completeness scoring       High       NOT_STARTED
  QUAL-006   Implement location scoring           High       NOT_STARTED
  QUAL-007   Implement engagement scoring         Medium     NOT_STARTED
  QUAL-008   Implement total score calculation    High       NOT_STARTED
  QUAL-009   Implement HOT/WARM/COLD thresholds   High       NOT_STARTED
  QUAL-010   Implement missing-field detection    High       NOT_STARTED
  QUAL-011   Implement re-qualification           High       NOT_STARTED
  QUAL-012   Implement qualification history      Medium     NOT_STARTED
  QUAL-013   Connect qualification to n8n         High       NOT_STARTED
  QUAL-014   Connect qualification to SQL         High       NOT_STARTED
  QUAL-015   Add qualification tests              High       NOT_STARTED

------------------------------------------------------------------------

# 30. Definition of Done

Lead qualification is considered complete when:

-   [ ] Structured lead information is available
-   [ ] AI output is validated
-   [ ] Qualification rules are deterministic
-   [ ] All six scoring factors are implemented
-   [ ] Total score is calculated correctly
-   [ ] HOT/WARM/COLD thresholds are implemented
-   [ ] Missing information is detected
-   [ ] Lead priority is stored in SQL
-   [ ] Qualification reason is stored
-   [ ] Leads can be re-qualified
-   [ ] HOT leads can trigger sales notifications
-   [ ] Qualification is covered by automated tests
-   [ ] n8n integration works
-   [ ] Frontend displays backend qualification results
-   [ ] Documentation matches the implementation

------------------------------------------------------------------------

# 31. Core Qualification Rules

1.  **AI extracts; deterministic rules decide.**
2.  **Never invent missing customer or property information.**
3.  **Missing information should trigger useful follow-up questions.**
4.  **Score must be calculated consistently.**
5.  **Priority must come from backend business logic.**
6.  **Status and priority are separate concepts.**
7.  **Qualification can change as the conversation develops.**
8.  **SQL stores the authoritative qualification result.**
9.  **Google Sheets is only a supporting operational layer.**
10. **Every scoring rule must be testable.**

------------------------------------------------------------------------

## Document Status

**Document:** LEAD_QUALIFICATION_SPEC.md\
**Version:** 0.1\
**Status:** Draft / Implementation Ready\
**Owner:** Project Engineering Team

**Related Documents:**

-   PRD.md
-   SAD.md
-   DOMAIN.md
-   DATABASE.md
-   API.md
-   AI-SPEC.md
-   N8N-WORKFLOWS.md
-   ENGINEERING.md
-   IMPLEMENTATION.md
-   TASK.md
-   TESTING.md
