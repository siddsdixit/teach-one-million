# Hybrid PRD Template

Use this template when `product_type` is `hybrid` (web app with embedded AI agent). Fill every section.

## Template Structure

```markdown
# Hybrid Product Requirements Document
**App Name:** [Name]
**Product Type:** Hybrid (Web App + AI Agent)
**Build Scope:** MVP | Full Product
**Primary Device:** Mobile | Desktop
**Date:** [Date]

---

## Executive Summary

[Same as web_app template, plus:]

**AI integration point:** [Where the agent appears — chat widget, inline suggestions, background automation]

**Agent role:** [What the AI does that the web app alone cannot]

---

## Persona

[Full narrative paragraph — include how AI saves them time specifically]

---

## Web App Features

[Standard feature table — same as web_app template]

---

## Agent Capabilities

[Same as agent template — capabilities, triggers, tools]

---

## Integration Points

| Web App Screen | Agent Trigger | Agent Output | UX Pattern |
|---------------|--------------|-------------|------------|
| [Screen] | [User action] | [What agent returns] | [Chat/Inline/Toast] |

---

## Data Flow

The agent endpoint lives at `POST /api/v1/chat` in the FastAPI backend. Web app frontend calls it via the standard API client. Agent has access to the same MongoDB database as the web app.

---

## Market Research

[Same as web_app template]
```
