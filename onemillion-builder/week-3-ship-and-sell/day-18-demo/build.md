# Day 18 — Build Guide

**Time: 30-60 min. Record demo. Submit. Receive Builder #N.**

---

## Step 1: Plan The Demo (10 min)

In `.onemillion/demo-plan.md`:

```markdown
## Demo Plan (5 min total)

### Minute 1: Problem
- Open with: [one-sentence problem statement]
- Reference: Sarah, freelance UX designer, spends 90 min every Sunday on...

### Minute 2: Solution
- One sentence: [product name] does [outcome] in [time].

### Minutes 3-5: Live demo path
1. Open live URL: yourapp.com (12 sec)
2. Sign up as fresh user: test-day18@example.com (30 sec)
3. Land on dashboard, show empty state (10 sec)
4. Create first [entity]: name, status, due date (30 sec)
5. Trigger AI feature on it (30 sec)
6. Show AI response streaming (50 sec)
7. Save / use the output (20 sec)

### Last 30 sec: Wrap
- "Built this in 18 days through OneMillion. Joining as Builder #[X]."
- One ask: [early users / feedback / hiring]
```

Don't memorize. Have it open in a second monitor as you record.

---

## Step 2: Pre-Flight Checks (5 min)

Before hitting record:

- [ ] Close all other browser tabs
- [ ] Clear cookies on your live URL (so you start logged out)
- [ ] Have a fresh email ready for the demo signup
- [ ] Camera + mic test
- [ ] Quiet environment (turn off notifications)
- [ ] Live URL works (test it now — last time before recording)

---

## Step 3: Record (10-20 min)

Open Loom (Cmd+Shift+L on Mac, similar on Windows).

Settings:
- Screen + face camera
- HD quality
- Public link (or "Anyone with the link can view")

Hit record. Follow your demo plan. **Don't restart for small mistakes** — keep them in.

Recommended takes: 2. First is rehearsal. Second is the keeper.

Stop at 5 min if you can. Longer = nobody watches.

---

## Step 4: Get The Loom URL (2 min)

Loom uploads automatically. After a minute, you'll get a shareable URL.

Test it: paste the URL into an incognito browser. **You should see:** your demo playing, no login required.

If it's private: change permissions to "Anyone with the link."

---

## Step 5: Save Demo Info (3 min)

Create `.onemillion/demo.md`:

```markdown
# Day 18 — Demo Day Submission

**Builder Name:** [your display name — real name, alias, or handle]
**Product Name:** [your product]
**Live URL:** [yourapp.com or .vercel.app]
**Demo Loom URL:** [your public Loom link]
**GitHub Repo:** [optional]
**Cohort:** [Cohort 0 / self-serve / Cohort 1 / etc.]
**Graduated At:** [today's date]

## My 18-Day Summary
[Optional 2-3 sentences on what you built and what you learned]
```

---

## Step 6: Final Verification

```bash
claude
```

Paste contents of [`ai-instructions-day-18.md`](./ai-instructions-day-18.md).

This runs the FINAL check:
- Loom URL works
- Live URL works
- All 17 previous days verified
- Demo.md exists

If pass: Claude will tell you what your Builder # is (next available) and how to claim it.

---

## Step 7: Submit Your Builder Application

**Method 1 — Pull Request to OneMillion repo (current):**

1. Fork [github.com/siddsdixit/onemillion-builder](https://github.com/siddsdixit/onemillion-builder)
2. Open `builders/_data.json`
3. Add your entry to the `builders` array:
   ```json
   {
     "number": [next available — check current data],
     "name": "Sarah Designer",
     "product_name": "DeliverableDash",
     "product_url": "https://deliverabledash.com",
     "demo_url": "https://www.loom.com/share/abc123",
     "github_repo": "https://github.com/sarah/deliverabledash",
     "cohort": "Cohort 0",
     "graduated_at": "2026-05-12"
   }
   ```
4. Update `_total_builders` to reflect new count
5. Update `_founding_builders_remaining` if you're #1-100
6. Open Pull Request titled: "Add Builder #[X] — [your-name]"

Sid reviews within 48 hours. Merge = you're in.

**Method 2 — Web form (Sprint 3, when onemillion.build/claim is live):**
Coming Sprint 3. PR is the current path.

---

## Step 8: Share The Win

LinkedIn (or X if you use it):

```
🎉 Builder #[N] reporting in.

I shipped [product] in 18 days through OneMillion.

It does [one specific outcome].

Live at [URL]. 

Demo: [Loom URL]

#BuildingWith1M
```

Tag @SidDixit. The Builder Wall thanks you.

---

## What Should Be True After Day 18

- [ ] 5-min Demo Loom recorded + public
- [ ] `.onemillion/demo.md` saved with URLs
- [ ] All 18 days verified
- [ ] PR submitted to onemillion-builder repo with Builder data
- [ ] You shared on LinkedIn (or you'll share within 24 hours)
- [ ] You took 10 minutes to actually feel what you accomplished

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Loom recording failed mid-way | Save what you have, append the rest, or re-record. 2-take rule. |
| Loom is taking forever to upload | Often Loom processes in background. Refresh dashboard in a few min. |
| Live URL broke right before recording | Probably an env var issue. Fix it. Test again. Then record. |
| Can't decide on display name | Use your real name. Builder #N is a serious credential — fake names dilute it. |
| Demo went over 5 min | Re-record. Tighter script. 5 min is the rule. |
| GitHub repo is private and I want to keep it private | That's fine. Skip the github_repo field in your submission. Live URL + demo Loom are enough. |

---

## You're Done

Take this moment.

You spent 18 days. You built a real product. You shipped it to the internet. Real people are using it. You earned a Builder number.

The next person reading this — Builder #N+1 — is starting their Day 1 today. They have no idea what they're capable of. **You used to be them. Three weeks ago.**

The skill is yours forever. The product is yours forever. The number is yours forever.

The million starts with one. You're one of them.

---

→ [Back to README](../../README.md) · [Cohort](../../../cohort/README.md) · [Builder Wall](../../../builders/README.md)
