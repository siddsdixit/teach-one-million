# Tier 2: Antigravity Setup

**Status: Limited support — Antigravity is brand new (Google announced it late 2024/early 2025). Patterns are still emerging.**

If you're an Antigravity early adopter and want to take OneMillion in it: you can. Here's the honest current state.

## What's Confirmed To Work

- **Antigravity has a built-in AI agent.** You can use it as a Tier 2 persona-switcher similarly to Cursor.
- **Antigravity has a terminal.** You can run Claude Code inside it for true Tier 1 fidelity. This is the recommended path for now.

## Install

1. Download Antigravity from Google's site
2. Set up your Google AI account / API key

## Recommended: Use Claude Code In Antigravity's Terminal

The simplest path:

1. Open Antigravity
2. Open terminal inside Antigravity
3. Install Claude Code: `npm install -g @anthropic-ai/claude-code`
4. Run `claude` — proceed as Tier 1

This gives you Tier 1 fidelity with Antigravity as the editor.

## Alternative: Use Antigravity's Native Agent

Antigravity's native agent system is evolving. To use it for OneMillion:

1. Create a project rule file (Antigravity's equivalent of `.cursor/rules`)
2. Copy the OneMillion mega-rule from `tools/tier-2-cursor/onemillion-rule.mdc` and adapt the syntax
3. Antigravity's agent should adopt the personas

This pattern is unstable as of writing — recommend Tier 1 + Antigravity as the editor instead.

## Caveats

- Antigravity's documentation is less mature than Cursor's
- Smaller community = fewer Stack Overflow answers when you hit issues
- Google may change behavior in updates that break OneMillion patterns

If you're a Google AI loyalist: try Antigravity for the editing experience, but run Claude Code in its terminal for the agentic SDLC fidelity. This is the lowest-risk path.

## Cost

- Antigravity may have its own subscription
- + Anthropic API credits if using Claude Code inside it ($5-15 total for course)

---

→ Back to [Tools README](../README.md) · Or use [Cursor](../tier-2-cursor/setup.md) (more stable) or [Claude Code directly](../tier-1-claude-code/setup.md)
