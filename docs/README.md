# Documentation — Real Estate Lead Bot

This folder holds the project documentation.

## Available Documents

| Document | Description |
|----------|-------------|
| [OVERVIEW.md](./OVERVIEW.md) | High-level project overview |

## Foundational Specifications

The full set of approved specification documents (PRD, System Architecture, Implementation tracking, Development Setup, Database, API, AI, n8n Workflows, Lead Qualification, UI/UX, Deployment, Testing, Tasks) were originally committed at the repository root.

They have been cleaned from the root to reduce clutter. The complete content remains available in **git history**.

You can restore any of them with:

```bash
git log --all --full-history -- "*PRD*"
# or
git checkout <commit-sha> -- "PRD — Real Estate Lead Bot.md"
```

Or download from the commit that first added them (`df091c599933fb4cbb10bc2ebb9d164cf8735aa1`).

## Recommended clean structure

```text
docs/
├── OVERVIEW.md
├── PRD.md
├── SAD.md                 # System Architecture
├── IMPLEMENTATION.md
├── DEVELOPMENT_SETUP.md
├── DATABASE.md
├── API.md
├── AI-SPEC.md
├── N8N-WORKFLOWS.md
├── LEAD_QUALIFICATION.md
├── UI-UX.md
├── DEPLOYMENT.md
├── TESTING.md
└── TASK.md
```

If you want the full documents restored into `docs/` with clean names, just ask and they can be re-added from history.
