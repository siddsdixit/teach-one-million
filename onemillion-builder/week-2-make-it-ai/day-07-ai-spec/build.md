# Day 7 — Build Guide

**No code today.** Pure spec writing. Use Claude to help draft.

---

## Before You Start

- [ ] Week 1 complete + verified
- [ ] You've read [learn.md](./learn.md) (especially Part 1 — the 3 patterns)
- [ ] You know your product's main user story from your PRD

---

## Step 1: Open Claude Code In Your Project

```bash
cd ~/my-onemillion-build
claude
```

---

## Step 2: Draft Your AI Feature Spec

Paste this prompt into Claude:

```
I'm on Day 7 of OneMillion (Week 2 — Make It AI). I need to write an AI
Feature Spec for my product.

Here's my PRD:
[paste contents of .onemillion/prd.md]

Help me draft an AI feature for this product. Walk me through it section
by section. Push back on vagueness. The output goes in
.onemillion/ai-feature.md and has these sections:

- Pattern (A / B / C — see Day 7 learn.md)
- What It Does
- When It Runs
- Input
- Output
- Quality Criteria (must be measurable)
- Out Of Scope (minimum 4 items)
- Cost Budget (per call + max)

Start by asking me which of the 3 patterns best matches my PRD's user stories.
```

Claude asks questions. You answer. Claude drafts. Iterate.

---

## Step 3: Sanity Check

Read your spec aloud. Ask yourself:

- **Specificity check:** Could a stranger read this and build the AI feature without asking me clarifying questions?
- **Pattern fit:** Does the pattern (A/B/C) actually match what the feature does?
- **Quality check:** Are my Quality Criteria things I can MEASURE, or are they wishes?
- **Scope check:** Is "Out Of Scope" honest? Does it include things I was tempted to add?
- **Budget check:** Did I do the math on cost? (Calls per day × cost per call = monthly burn)

If any answer is no, ask Claude to revise that section.

---

## Step 4: Save And Lock

Once it's solid:

```
Save the final version to .onemillion/ai-feature.md
```

Then commit it:

```bash
git add .onemillion/ai-feature.md
git commit -m "Day 7: AI feature locked"
```

From this point: no scope creep on the AI feature. If you think of something cool to add, it goes to "Out Of Scope" or "v2", not into the current build.

---

## Step 5: Verify

```bash
claude
```

Paste contents of [`ai-instructions-day-07.md`](./ai-instructions-day-07.md).

---

## What Should Be True After Day 7

- [ ] `.onemillion/ai-feature.md` exists with all 8 sections
- [ ] One pattern selected (A, B, or C)
- [ ] Quality Criteria are measurable (numbers or verifiable conditions)
- [ ] Cost Budget includes per-call cost AND a max
- [ ] Out Of Scope has 4+ items
- [ ] You committed the spec to git
- [ ] Verification passed ✅

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Claude wrote a 10-section spec | Tell it: "Reduce to exactly these 8 sections: [list]. No more." |
| I can't decide between Pattern A and Pattern B | Pick A. Simpler. You can add B-style judgment in v2. |
| My Quality Criteria are vague ("output is good") | Ask Claude: "Rewrite Quality Criteria as measurable checks. Each one a number or a verifiable condition." |
| I don't know the cost per call | Claude knows. Ask: "What's the cost for my use case using Claude Haiku vs Sonnet?" |
| I'm tempted to add more features | Add them to Out Of Scope. Don't expand v1. |

---

→ **Done with Day 7?** Move to [Day 8 — First AI Call + Prompt Design](../day-08-first-ai-call/learn.md).
