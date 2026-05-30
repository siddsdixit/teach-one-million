# Agent PRD Template

Use this template when `product_type` is `agent`. Fill every section.

## Template Structure

```markdown
# Agent Requirements Document
**Agent Name:** [Name]
**Product Type:** AI Agent
**Build Scope:** MVP | Full Product
**Date:** [Date]

---

## Executive Summary

**One-line description:** [What the agent does in one sentence]

**Agent type:** [Reactive (responds to input) | Proactive (runs on schedule) | Both]

**Primary interaction:** [Chat | Email | Webhook | API | Scheduled]

**MVP Hypothesis:** [What can be validated with the core capability]

---

## Persona

[Full narrative paragraph of the user who benefits from this agent]

---

## Agent Capabilities

| ID | Capability | Trigger | Output | Priority |
|----|-----------|---------|--------|----------|
| CA-01 | [Name] | [What triggers it] | [What it produces] | [MVP] |

---

## Tools Required

| Tool | Purpose | API/Service |
|------|---------|-------------|
| [Tool name] | [What it does] | [Service/API] |

---

## Conversation Design

**Personality:** [3 adjectives]

**Opening message:** "[Exact first message the agent sends]"

**Tone:** [Formal/Casual/Technical]

---

## Error & Edge Cases

| Scenario | Agent Behavior |
|----------|---------------|
| Ambiguous input | Ask clarifying question |
| API failure | Graceful degradation + user notification |
| Out of scope | Politely redirect |

---

## Cost & Performance

- **Model:** [Claude Sonnet / GPT-4o / Gemini Pro]
- **Avg tokens per conversation:** [estimate]
- **Rate limiting:** [requests/user/day]
- **Budget cap:** [$X/day]
```
