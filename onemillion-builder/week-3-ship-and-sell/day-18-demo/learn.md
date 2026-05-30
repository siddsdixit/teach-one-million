# Day 18 — Demo Day → Builder #N

**Week 3 | ~30-60 min | First Voyage**

---

## What You'll Have After Today

- A **5-minute Demo Loom** of your product, working live
- **Final verification** — all 18 days passed
- Your **Builder #N** — your permanent, sequential number on the OneMillion wall
- A **public profile** at onemillion.build/builders/[your-number]
- A **LinkedIn badge** to share
- The ability to say: **"I built this in 18 days."**

You did it. Today is the proof.

---

## Watch First (5 min) 🎬

[Embedded Loom — Sid records his own Demo Day Loom live]

*Loom recording link will be added in Sprint 3.*

---

## Part 1: The 5-Minute Demo Structure (~10 min read)

Your demo has a tight structure. Same as a YC Demo Day. Same as a Series A pitch. Same as Stripe's first investor pitch.

**5 minutes. 5 sections.**

### Minute 1: The Problem (1 min)
- Who has it. Be specific. Named user from your PRD.
- Why it matters. Specific story. Time/money lost.
- One sentence: "[User] spends [time/effort] dealing with [pain]."

### Minute 2: The Solution (30 sec)
- One sentence: what does your product do?
- No features. The OUTCOME. "[Product name] [solves the pain] in [time]."

### Minutes 3-5: Live Demo (3 min)
- Open your live URL
- Sign up as a fresh user (use a test email)
- Use the core feature
- Trigger the AI feature
- Show what happens

No slides. Real product. Real interactions.

If you screw something up live, **leave it in.** The "oh, oops, let me try again" moment is more relatable than a polished take.

### Last 30 sec: What's Next
- What you'd build next (your "v2" from your PRD's Out-Of-Scope)
- The Builder number context: "Joining as Builder #[X]"
- A clear ask if you have one (early users? feedback? hiring?)

---

## Part 2: Why Loom + Public (~5 min read)

Two formats: live presentation (in cohort) or pre-recorded Loom. Both count.

For Cohort 0 and self-serve: **Loom is the default.**

Why:
- Easier to schedule (you record on your time)
- You can re-record if you genuinely flub
- The Loom URL goes on your Builder profile → permanent record
- People can watch async at their own pace

Loom requirements:
- 5 min max (longer = nobody watches)
- Screen + face camera
- Your live URL working in the recording
- Publicly viewable (anyone with the link)

---

## Part 3: The Lock-In Moment (~5 min read)

Today is the day you stop being someone "building a product" and become someone who **built a product**.

Tomorrow morning you'll wake up to a public profile that says **Builder #[X]**. That number is yours. Permanent. Sequential. It's not a participation trophy — every Builder went through the same gauntlet you did.

People will ask: "What did you build?" You'll have an answer. A real URL. A real demo. A real product.

This isn't a small thing. Most people who try to build something never finish. You finished.

---

## Today's Assignment

1. Plan your 5-minute demo (script lightly, don't read)
2. Record your Loom
3. Submit your Builder application (URL, repo, demo Loom, optional bio)
4. Run final verification (all 18 days)
5. Receive your Builder #N

---

## What Good Looks Like

A great Demo Day Loom:
- Opens with: "I'm [name]. I built [product] in 18 days using OneMillion."
- Has a working live URL
- Shows you signing up + using the core feature LIVE
- Shows the AI feature working
- Has at least one real, slightly imperfect moment (proves it's live)
- Closes with: "Joining the Crew as Builder #[X]." + 1-sentence what's next

5 minutes. Clean. Honest. Real.

---

## Common Mistakes (Today)

1. **Over-polishing.** 5 retakes trying to make it perfect. Stop at take 2 or 3. Imperfection = authenticity.

2. **Slides.** No slides today. Real product, live screen.

3. **Talking over the demo.** Show, don't just tell. Click. Wait. Let the AI respond. The silence + the result is more powerful than your narration.

4. **Asking for everything at the end.** "Sign up, give feedback, hire me, invest in me, mention me to your friends!" Pick ONE ask. Maximum.

5. **Skipping the submission.** Recording a Loom but not submitting it. You only become Builder #N when the submission is verified.

---

## What Should Be True After Day 18

- [ ] 5-minute Demo Loom recorded
- [ ] Loom is publicly viewable (you tested the link in incognito)
- [ ] Live URL still works (test it now)
- [ ] All 18 daily verifications passed (or 17 + explicit skip note)
- [ ] Builder submission filed
- [ ] You received your Builder #N
- [ ] You took a moment to notice you actually did this

---

## Verify Your Day 18

Paste contents of [`ai-instructions-day-18.md`](./ai-instructions-day-18.md). Claude will:
- Check Demo Loom URL exists in `.onemillion/demo.md`
- Verify Loom URL returns 200
- Check live URL still works
- Verify all previous 17 day verifications passed
- Issue Builder #N (or instruct you to claim it)
- Report pass / needs revision

---

## After Verification: Claim Your Number

Once verified:

1. Open `builders/_data.json` (in the OneMillion repo via PR, or onemillion.build/claim form when available)
2. Submit your entry:
   ```json
   {
     "number": [next available],
     "name": "[your display name]",
     "product_name": "[your product]",
     "product_url": "[yourapp.com or .vercel.app]",
     "demo_url": "[your Loom URL]",
     "github_repo": "[optional, link to your repo]",
     "cohort": "[Cohort 0 / self-serve / etc.]",
     "graduated_at": "[date]"
   }
   ```
3. Sid reviews your submission within 48 hours
4. Once approved, you're on the wall forever

The Founding Builder badge (first 100) is automatic if your number is ≤100.

---

## Share It

```
🎉 Builder #[N] reporting in. 

Shipped [product] in 18 days through OneMillion.

It does [one sentence]. Live at [URL]. 

Demo: [Loom URL]

If you have a problem you want to build solutions for — the next cohort
opens [date]. I'll be there as a Ship Captain.

#BuildingWith1M #OneMillionBuilder
```

Post on LinkedIn (and X if you use it). Tag Sid. The Builder Wall thanks you.

---

## And Then What?

You're done with the course. The skill is yours.

Things to consider over the next week:
1. **Keep iterating on your product.** Real users → real feedback → real improvements. Days 19, 20, 21...
2. **Become a Ship Captain.** Help run the next cohort. See [cohort/README.md](../../../cohort/README.md).
3. **Build your next product.** You did this in 18 days. Try to do the next one in 9.
4. **Teach what you learned.** Charge $200-500/hr for AI consulting. Companies need this skill desperately.

The course is done. Your build continues.

---

## Go Deeper

- **[Sid's Day 18 reflection](#)** — what graduating Builder #1 actually felt like (Sprint 3)
- **[The Crew Slack](#)** — alumni community (Sprint 3)
- **[Sprint 4: Build something else](#)** — guided path for your second product

---

## Welcome To The Crew

You're Builder #N. That's yours, forever.

The million starts with one. You're one of them now.

→ [Back to README](../../README.md) · [Cohort](../../../cohort/README.md) · [Builder Wall](../../../builders/README.md)
