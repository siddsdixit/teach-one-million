# Tier 1: Claude Code Setup

The cleanest path. Claude Code is a CLI tool from Anthropic that runs in any terminal. The OneMillion agents are native Claude Code agents.

## Install

```bash
npm install -g @anthropic-ai/claude-code
```

Verify: `claude --version`

## Authenticate

First time you run `claude`, paste your Anthropic API key (from [console.anthropic.com](https://console.anthropic.com)).

## Use With OneMillion

In your project folder:

```bash
cd ~/my-onemillion-build
claude
```

Then in Claude Code:

### Run a daily lesson
Paste the contents of `week-1-foundation/day-XX/build.md` into Claude. Ask Claude to walk you through each step.

### Verify a day
Paste the contents of `week-1-foundation/day-XX/ai-instructions-day-XX.md`. Claude runs the verification.

### Install the agents (optional, advanced)
For the cleanest agentic SDLC experience, you can install the OneMillion agents into Claude Code's agent system. They'll show up as slash commands like `/idea`, `/spec`, `/build`.

Once the OneMillion agents are stable (Sprint 4), the install script will be:

```bash
git clone https://github.com/siddsdixit/onemillion-builder
cp -r onemillion-builder/agents/* ~/.claude/agents/
```

Then in any project: `/idea`, `/spec`, etc. work as slash commands.

> Note: Until Sprint 4, the agents reference an older tech stack. Use the daily ai-instructions files instead — they're the current source of truth.

## Editor Pairing

Claude Code runs in any terminal. So you can use Claude Code alongside:
- VS Code (open `code .`, then run `claude` in VS Code's integrated terminal)
- Cursor (same — Cursor's terminal works fine)
- Antigravity (same)
- Just a regular Mac Terminal / Windows Git Bash

Pick whichever editor feels good. Claude Code is the constant.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `claude: command not found` | Restart terminal. Or check `npm config get prefix`. |
| API key not accepted | Make sure you copied the full `sk-ant-...` key. |
| `Rate limit` error | Wait 60 sec. Or upgrade your Anthropic tier. |

## Cost

You'll spend $5-15 in API credits over 18 days. See [cost-transparency.md](../../cost-transparency.md).

---

→ Back to [Tools README](../README.md)
