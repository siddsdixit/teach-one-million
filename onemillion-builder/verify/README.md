# Verification System — How Builder #N Is Earned

OneMillion's certificate isn't a PDF you get for clicking through 18 days of videos. It's earned by passing **18 verification checks** — one per day. Each check confirms specific, verifiable artifacts exist in your project.

This is what makes Builder #N credible: every Builder on the wall genuinely shipped what the course promised.

---

## How It Works

### Per-Day Verification

Every day in the course has an `ai-instructions-day-XX.md` file. This is a paste-able prompt you give to Claude Code (or your AI tool). The AI then:

1. Reads your project files
2. Checks structural requirements (files exist, code patterns present)
3. Reviews quality (PRD specific enough, prompts well-formed, etc.)
4. Reports pass / needs-revision with specifics
5. Writes the report to `.onemillion/verification-day-XX.md`

You run this at the end of each day. Pass it, move on. Fail it, fix the issues and re-run.

### Final Verification (Day 18)

On Day 18, you run a final pass that:
1. Confirms all 18 daily verifications have passed
2. Checks your deployed URL is still live
3. Confirms anti-cheating signals (deployed URL is unique, commit history shows organic build, demo Loom features the builder)
4. Issues your **Builder #N**

---

## Two Layers Of Verification

### Layer 1: Structural Checks (Automated)
File exists. JSON is valid. URL returns 200. API endpoint behavior matches expectations. RLS is enabled. These are binary — either they're true or they're not.

### Layer 2: Quality Checks (AI-Graded)
Is the PRD actually specific enough? Is the prompt well-designed? Does the landing page communicate clearly? These require judgment. Claude reviews and reports.

---

## Three Ways To Verify

### Option 1: In Claude Code (engineers + PMs)
The recommended path. After each day:
```
claude
```
Then paste the contents of `ai-instructions-day-XX.md`. Claude does the verification in your terminal.

### Option 2: Web Form (planned)
The future web verifier will let builders:
- Paste your GitHub repo URL
- Paste your deployed app URL
- Click "Verify Day X"
- Backend clones, runs checks, reports back

### Option 3: GitHub Action (planned)
The future GitHub Action will run verification automatically on every push and sync daily progress to the Builder Wall.

---

## The Schemas

For builders who want to know exactly what's checked: see `verify/schema/day-XX.json` files. Each contains the explicit checks for that day.

Engineers: feel free to read the schemas. They're machine-readable specifications of what "pass" means.

---

## Anti-Cheating

Builders can theoretically fork someone else's repo and pass verification. To prevent this:
- Verification stores a hash of the deployed URL + commit history
- Duplicate URLs are flagged for manual review
- The 5 user conversations (Day 2) require real names + dates — Sid spot-checks Cohort 0 manually
- Demo Loom (Day 18) must show the builder using the product live

It's not bulletproof. It's good enough. The Builder Wall is a reputation system — fakes get noticed.

---

## What Happens After All 18 Days Pass

```
1. System assigns next sequential Builder #N (atomic — no duplicates)
2. Builder profile created at onemillion.build/builders/[Builder-N]
3. Profile shows: deployed URL, 18-day commit history, demo Loom
4. Certificate PDF generated and downloadable
5. LinkedIn badge image generated (shareable, links back to profile)
6. Sid is notified to send personal congratulations DM
```

You receive:
- **Builder #N** — your permanent, sequential number
- **Public profile** — yours forever
- **Certificate PDF** — for your records / LinkedIn / interviews
- **LinkedIn badge** — verifiable, links to your profile

---

→ Back to: [README](../README.md) · [Getting Started](../getting-started.md)
