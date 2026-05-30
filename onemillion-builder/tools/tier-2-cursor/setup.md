# Tier 2: Cursor Setup

Cursor is a VS Code fork with built-in AI agent (Composer). The OneMillion course works in Cursor — you use a single mega-rule that lets Composer adopt different OneMillion personas based on which day you're on.

## Install

1. Download Cursor at [cursor.com](https://cursor.com)
2. Open Cursor → Sign in (free tier works)
3. Settings → AI → enable Composer (Cmd+Shift+I to test)

## Use With OneMillion

### Option A: With Claude Code as a CLI inside Cursor (RECOMMENDED for course)

Even though Cursor has its own AI, you can run Claude Code in Cursor's integrated terminal. This gives you Tier 1 fidelity with Cursor as the editor.

1. Install Claude Code: `npm install -g @anthropic-ai/claude-code`
2. Open Cursor's terminal: ` ` ` (Ctrl+~ on Mac)
3. Run `claude` and follow Tier 1 instructions

This is what most engineers do.

### Option B: With Cursor's own Composer (PURE Cursor)

Use Cursor Composer as your AI builder, with the OneMillion framework as Cursor rules.

1. Copy `tools/tier-2-cursor/onemillion-rule.mdc` into your project at `.cursor/rules/onemillion.mdc`
2. Activate it: Cursor Settings → Rules → enable
3. Open Composer (Cmd+I)
4. Composer now follows OneMillion patterns

## Daily Workflow (Option B)

Same daily loop as Tier 1, but with Composer instead of Claude Code:

```
1. Read day's learn.md
2. Open Composer (Cmd+I)
3. Paste the day's build.md instructions
4. Composer walks you through
5. End day: paste ai-instructions-day-XX.md into Composer to verify
```

## Cost

Cursor's pricing is separate from Anthropic's. Free tier: limited. Pro: $20/mo includes Cursor's AI + lets you use your own Anthropic API key.

## Tradeoffs vs Tier 1

| | Cursor Composer (Tier 2) | Claude Code (Tier 1) |
|--|--|--|
| Subagent orchestration | ❌ One main agent | ✅ Multiple agents |
| File system access | ✅ Yes | ✅ Yes |
| Verification flow | ⚠️ Paste-based, less clean | ✅ Native |
| Cost predictability | Cursor Pro = flat $20/mo | Pay per call ($5-15 total) |
| Already a Cursor user | ✅ Stay in your flow | Adds Claude Code learning |

## Recommendation

If you're already paying for Cursor: use it. Especially if you've internalized Composer.

If you're new: try Claude Code first (Tier 1). Add Cursor later.

---

→ Back to [Tools README](../README.md)
