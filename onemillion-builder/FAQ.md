# FAQ

The 12 questions everyone asks. Bookmark this; you'll come back.

---

## 1. Do I really not need to know how to code?

Correct. The AI writes the code. You direct it.

Most people who finish this course never wrote a line of code before Day 1. They wrote a clear spec, ran agents, reviewed what came out, and shipped. That's the whole skill. By Day 18 you'll have a deployed product and a feel for HOW software comes together — which is more useful than knowing a specific language.

Engineers: yes, you'll learn things too. The agentic SDLC framework is genuinely new — most engineers don't yet have a good intuition for spec-driven AI development. That's what you're here for.

---

## 2. How much time does this actually take?

| Audience | Per day | Total over 18 days |
|----------|---------|--------------------|
| Never coded | 1.5–2 hours | ~30 hours |
| Some technical background (PM, analyst, etc.) | 1–1.5 hours | ~20 hours |
| Engineer | 30–60 minutes | ~12 hours |

The course is calibrated for the middle. EAs will spend more time on Day 4 (setup) and Day 6 (CRUD). Engineers will skim much of Days 1–3 (concept). Everyone arrives at Day 18 around the same time.

If you fall behind, that's fine. The course is milestone-based, not calendar-based. Catch up. You're allowed to skip the weekend if you need to.

---

## 3. What if I get stuck on a day and can't move forward?

Three escalation steps:

1. **Read the day's troubleshooting table** (bottom of every `build.md`). Most problems are listed there.
2. **Re-run the AI verifier** for that day — paste the `ai-instructions-day-XX.md` prompt into Claude Code. It will tell you specifically what's missing.
3. **Ask in the cohort Slack** (if you're in a cohort) or open an issue on the GitHub repo (if you're self-serve). Tag the day number. Someone will help within a few hours.

Last resort: switch to **Codespaces** ([see getting-started.md](./getting-started.md#codespaces-fallback-last-resort)). 90% of "stuck" issues are local-environment-related. Codespaces eliminates them.

---

## 4. Can I use Cursor, Windsurf, or another AI tool instead of Claude Code?

For this version of the course, **Claude Code is the supported path**.

The course teaches an **agentic SDLC framework**, but the daily instructions and verifiers assume Claude Code. Other tools may work, but they are not the official path yet.

---

## 4.5 What if I fall behind?

You'll fall behind. Everyone does. Real life happens. The course is designed for it.

**There's no shame, no streak, no badge taken away if you skip a day or a week.** The 18 days are units of progress, not calendar days. Builder #N gets earned when you finish, not by when you finish.

Many builders take 30 or 60 calendar days to complete the 18 days of work. Some take 90 days. They all graduate. You will too.

The only failure mode is not coming back. If life pulls you away, just come back when it lets you. We're not Duolingo. The course waits.

## 5. Can I skip days or do them out of order?

Not really. Each day depends on the previous one. Day 4 needs Day 3's PRD. Day 7 needs Day 6's working app. The verification system enforces this — you can't get Builder #N if you skipped days.

You **can** take more than one calendar day per "day" if you need to. Spread Day 4 over a weekend. Take a week off. Come back. The 18 days are *units of progress*, not literal calendar days.

---

## 6. What if my product idea is bad?

You'll find out on Day 2 (the Mom Test conversations) and Day 3 (the PRD). By then you can pivot. Many builders change their idea between Day 1 and Day 4 — that's expected, not failure.

**Common pivots:**
- "Too big" → narrow scope to one user, one feature
- "Already exists" → focus on the niche existing tools ignore
- "I don't actually need this" → pick a problem you *do* feel personally

After Day 3 your PRD is locked. Don't pivot after that — finish what you started, learn the skill, then build the next product.

---

## 7. What if I break something during the build?

Welcome to engineering. This is normal.

Your code lives in a Git repo. Every change is reversible. The course shows you how to commit at safe checkpoints. If something breaks badly, you can roll back to yesterday's working version with one command:

```bash
git reset --hard HEAD~1   # undoes your last commit
```

(Don't run this until you understand it. Day 4 explains git in detail.)

If things really go sideways, you can delete the project and start over. You'll lose your code, not your skill.

---

## 8. Will my product actually work, or is it a toy?

It will actually work.

By Day 18 your product will have:
- Real authentication (signup, login, password reset)
- A real database (Supabase Postgres, not localStorage)
- A real AI feature (calling Claude with streaming, tool use, and your user's data)
- Production monitoring (Sentry catches errors, Vercel Analytics tracks usage)
- A custom domain with SSL
- At least one real user (someone who's not you)

It is not a demo. It is a product. You can keep building on it after Day 18, ship features, get more users, charge money if you want. It's yours.

---

## 9. What if I'm not in a cohort?

Self-serve works fine. The entire course content + verification system is in this repo. You'll miss two things:

1. **Sid's live Saturday sessions** — you can watch the recordings instead
2. **The cohort community** — you can join the OneMillion Crew Slack (open to all builders, even self-serve)

Self-serve completion rate is lower (~25%) than cohort completion (~45%). The community and accountability matter. But many builders finish solo.

---

## 10. How does Builder #N actually work?

When you complete Day 18 and pass all verification checks, the system assigns you the next sequential Builder number. It's:

- **Permanent.** Yours forever. No re-certification.
- **Sequential.** Builder #47 was the 47th person to graduate. Builder #500 was the 500th.
- **Public.** Listed on this repo and at onemillion.build/builders.
- **Linked.** Your profile shows your deployed product, 18-day commit history, demo Loom.
- **Shareable.** A LinkedIn badge image links back to your verified profile.

The first 100 builders ever get **Founding Builder** status — same number, additional permanent badge, plus Sid's personal Slack DM access and an intro to one investor or hiring manager on graduation.

---

## 11. What if Anthropic / Vercel / Supabase changes pricing?

Then we update the course. The agentic SDLC framework is stable — the tools may shift.

If a service we recommend becomes too expensive or shuts down, we'll publish migration guides and update the course content. The Builder Wall is permanent regardless.

(For what it's worth: Anthropic, Vercel, Supabase, and GitHub all have free tiers that have been generous and stable for years. We don't expect issues.)

---

## 12. What happens on Day 19?

Whatever you want.

Common paths:
- **Keep building.** Add features, polish, market it, monetize if you can.
- **Build another product.** You have the skill now. Pick another idea, ship in 5 days, then 3 days, then 1.
- **Become a Ship Captain.** Help run the next cohort. Get paid in OneMillion equity-of-mission (and Sid's gratitude).
- **Teach what you learned.** Many alumni become AI-builder consultants, charging $200–500/hr to help companies adopt the same patterns.
- **Just exist with the skill.** Use it when you need it. The skill doesn't expire.

Builder #N is the credential. What you do with it is up to you.

---

→ **More:** [Manifesto](../MANIFESTO.md) · [Getting Started](./getting-started.md) · [API Keys + Cost](./getting-your-api-key.md) · [Day 1](./week-1-foundation/day-01-vision/learn.md)
