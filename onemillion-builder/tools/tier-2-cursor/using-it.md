# Tier 2: Using Cursor Daily

## Daily Loop With Composer

```
1. Read the day's learn.md
2. Open Composer (Cmd+I)
3. Tell it: "I'm on Day X. Walk me through [paste build.md instructions]"
4. Composer responds, you iterate
5. End of day: paste ai-instructions-day-XX.md into Composer
6. Composer adopts VERIFY persona, runs checks
7. Commit your work
```

## Tips Specific To Cursor

### Triggering Persona Switches
The `onemillion-rule.mdc` makes Composer adopt different personas based on cues. To trigger a specific one, be explicit:

```
"I'm on Day 5 of OneMillion. BUILD persona please. I need..."
```

Or just reference the day number — the rule infers.

### Composer vs Chat
- **Composer (Cmd+I):** for code generation and editing across multiple files
- **Chat (Cmd+L):** for explanation, debugging, single questions

Use Composer for build days (4-6). Use Chat for verify days.

### Including Files
Cursor lets you `@` mention files. Use it to give Composer context:

```
"Help me debug @app/api/deliverables/route.ts — getting 401s"
```

### When Composer Goes Off Track
If Composer starts suggesting a different stack (e.g., Prisma instead of pure Supabase), interrupt with:

```
"Stop. OneMillion uses raw Supabase, not Prisma. Restart with the
Supabase server client."
```

The mega-rule should prevent this, but Composer occasionally drifts.

## What Doesn't Work Well

- **Long verification reports** — Composer truncates. Paste verification prompt in Chat instead.
- **Multiple agents at once** — Cursor's one main agent can't simulate true subagent orchestration.

## Cost Strategy

Cursor Pro ($20/mo) gives generous AI usage. If you stay in the course's flow, $20 covers all 18 days easily.

Alternative: Free Cursor + bring your own Anthropic API key. Slightly more friction.

---

→ Back to [Tools README](../README.md)
