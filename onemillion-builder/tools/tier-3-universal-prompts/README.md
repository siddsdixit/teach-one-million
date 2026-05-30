# Tier 3: Universal Prompts

The fallback that works in **any AI chat**: Claude.ai web, ChatGPT, Gemini, Mistral — anything that accepts text in, returns text out.

## When To Use This Tier

- You can't install software locally (corporate laptop, etc.)
- You don't have a Claude API key
- You prefer chat-based AI to terminal/IDE AI
- You're on a phone or tablet (yes, you can do parts of the course on mobile this way)

## What You Get / What You Lose

| | Tier 1 (Claude Code) | Tier 3 (Universal) |
|--|--|--|
| AI writes code directly to your files | ✅ | ❌ — you copy-paste |
| AI runs terminal commands | ✅ | ❌ — you run them |
| AI verifies your work autonomously | ✅ | ❌ — you do the manual check |
| Works in any AI tool | ❌ Claude only | ✅ Any |
| Works on a phone | ❌ | ✅ |
| Cost | $5-15 (Anthropic API) | $0 if using free Claude.ai |

## How To Use

For each day:

1. Read the day's `learn.md` in this repo
2. Open your AI tool (Claude.ai, ChatGPT, etc.)
3. Paste the corresponding **universal prompt** from `prompts/day-XX.md` (coming Sprint 2)
4. AI walks you through, generates code
5. You manually copy-paste code into your editor
6. You manually run terminal commands
7. End of day: paste the verification prompt; AI tells you what to check

## Universal Prompts (Sprint 2)

Universal prompts are coming in Sprint 2 of course development. For now, you can adapt the day's `ai-instructions-day-XX.md` file as a starting point.

To convert any day's instructions to a universal prompt:
1. Open the day's `learn.md` and `build.md`
2. Paste the build.md content into your AI tool
3. Prefix with: "I'm following the OneMillion course Day X. Walk me through these steps. I can't install Claude Code or use a terminal — explain each step so I can do it manually. When you generate code, give me the full file content I should paste."

## Cohort Verification

For Tier 3 builders: the **web verification form** at onemillion.build/verify (coming Sprint 3) is for you. You paste your GitHub repo URL and Vercel URL; the form runs the checks server-side.

Until that exists: ask in cohort Slack to have someone with Claude Code run the verifier on your repo. Or sign up for Codespaces (free 60 hr/mo) and run Claude Code there.

---

→ Back to [Tools README](../README.md) · [Codespaces fallback](../../getting-started.md#codespaces-fallback-last-resort)
