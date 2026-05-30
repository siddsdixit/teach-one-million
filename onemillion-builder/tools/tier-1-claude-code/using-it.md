# Tier 1: Using Claude Code Daily

Day-by-day patterns for using Claude Code through the OneMillion course.

## The Daily Loop

```
1. Read the day's learn.md (concept)
2. Open Claude Code in your project: `claude`
3. Follow the day's build.md, using Claude Code for each step
4. End the day by pasting ai-instructions-day-XX.md into Claude
5. Claude verifies, reports pass/fail
6. Commit your work
```

## What Claude Code Is Good At

- Writing code from a clear spec
- Refactoring existing code
- Explaining errors
- Running terminal commands
- Reading files in your project
- Multi-step tasks ("first do X, then Y, then verify")

## What Claude Code Is Bad At

- Reading your mind (give specs, not vague prompts)
- Producing perfect code on the first try (review, iterate)
- Knowing about services it can't access (your Supabase dashboard requires you to click)
- Choosing scope (you're the product manager — Claude is the engineer)

## Pro Patterns

### Pattern 1: Spec → Code → Review
```
You: "I need a route that does X with constraints Y. Show me the plan before coding."
Claude: [proposes structure]
You: "Looks good. Generate it."
Claude: [generates]
You: [review, ask questions]
```

### Pattern 2: Bug → Stack trace → Fix
```
You: "Getting this error: [paste stack trace]. What's wrong?"
Claude: [diagnoses]
You: "Fix it."
Claude: [edits the file]
```

### Pattern 3: Multi-step with checkpoints
```
You: "Walk me through adding feature X. First show me the data model.
      Then API routes. Then UI. Pause for me to confirm at each step."
```

## Slash Commands

In Claude Code, anything starting with `/` is a command. Useful ones:

| Command | What it does |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation context |
| `/compact` | Compress conversation to free up context |
| `/model` | Switch models (sonnet, opus, haiku) |
| `/cost` | Show your session's API spending |

## When To Use Which Model

- **Haiku** (cheapest, fastest) — boilerplate code, simple refactors, quick edits
- **Sonnet** (balanced, default) — most course days
- **Opus** (smartest, most expensive) — complex debugging, architectural decisions, Day 6 + Day 10 builds

Switch with `/model`.

---

→ Back to [Tools README](../README.md)
