# Day 3 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Last no-code day.** Today you lock `.onemillion/prd.md` so the build agents can start tomorrow.

---

## Before You Start

- [ ] Day 2 verified.
- [ ] `.onemillion/prd.md` includes Day 2 validation evidence and MVP decision.
- [ ] You are in your `my-onemillion-build` folder.

---

## Step 1: Ask The Harness To Teach Spec Lock

Paste this:

```text
I am on OneMillion Day 3.

Teach me what a buildable spec is.

Explain:
- requirement vs idea
- user story vs use case
- acceptance criteria
- KPI / success signal
- out of scope
- definition of done
- why scope lock matters before code
- what the validate-spec agent checks

Then guide me one step at a time.
Use .onemillion/prd.md as the single source of truth.
Do not create extra Day 3 paperwork files.
```

---

## Step 2: Add The Day 3 Locked Spec Section

Open `.onemillion/prd.md`.

Add this section near the top, after the Day 2 validation update:

```markdown
## Day 3 Locked Spec

Spec locked on: 2026-05-31

### MVP Summary
[One paragraph: the smallest useful version we are building first.]

### Core User Stories
1. As [specific user], I want [specific action] so that [specific outcome].
2. As [specific user], I want [specific action] so that [specific outcome].
3. As [specific user], I want [specific action] so that [specific outcome].

### Use Cases
- [Real usage moment 1]
- [Real usage moment 2]
- [Optional usage moment 3]

### Acceptance Criteria
- Given [context], when [action], then [observable result].
- Given [context], when [action], then [observable result].
- Given [context], when [action], then [observable result].

### KPIs / Success Signals
- [Measurable usefulness signal]
- [Measurable usefulness signal]

### Out Of Scope For MVP
- [Tempting feature not in v1]
- [Tempting feature not in v1]
- [Tempting feature not in v1]
- [Tempting feature not in v1]
- [Tempting feature not in v1]

### Definition Of Done
[Concrete paragraph describing exactly what v1 can do when complete.]

### Agent Build Rule
Build agents may implement only the MVP above. If a requested change conflicts with this locked spec, stop and ask before changing scope.
```

---

## Step 3: Use The Spec Agent

Ask your harness:

```text
Act as the OneMillion spec agent.

Read .onemillion/prd.md.
Help me complete the Day 3 Locked Spec section.

Rules:
- exactly 3 core user stories
- each story must use: As [user], I want [action] so that [outcome]
- use cases must be real moments, not feature names
- acceptance criteria must be testable
- KPIs must measure usefulness, not vanity
- out of scope must include at least 5 items
- definition of done must describe the concrete v1 product state

Ask me one question at a time where my PRD is unclear.
Do not add new features beyond the Day 2 MVP decision.
```

---

## Step 4: Use The Validate-Spec Agent

Ask your harness:

```text
Act as the OneMillion validate-spec agent.

Review .onemillion/prd.md for Day 3.

Check:
- Is the MVP small enough?
- Are there exactly 3 core user stories?
- Are the use cases real scenarios?
- Are acceptance criteria testable?
- Are KPIs measurable?
- Is out of scope strong enough?
- Is Definition of Done concrete?
- Would a build agent know what to build next without guessing?

If it is weak, give me the smallest edits needed.
If it is strong, say it is ready to lock.
```

Make the edits in `.onemillion/prd.md`.

---

## Step 5: Read It Aloud

Read the Day 3 Locked Spec aloud.

If any sentence sounds like:

```text
make it easy
manage everything
support all users
smart dashboard
AI-powered workflow
```

rewrite it into observable behavior.

---

## Step 6: Commit The Spec Lock

From `my-onemillion-build`:

```bash
git add .onemillion/prd.md
git commit -m "Day 3: lock MVP spec"
```

If git is not initialized yet:

```bash
git init
git add .onemillion/prd.md
git commit -m "Day 3: lock MVP spec"
```

---

## Step 7: Run Day 3 Verification

Ask your harness:

```text
Run the OneMillion verifier for Day 3.

Review .onemillion/prd.md only.
Do not create extra verifier markdown files.
Record the result in .onemillion/state.json.
```

---

## What Should Be True After Day 3

- [ ] `.onemillion/prd.md` includes `## Day 3 Locked Spec`.
- [ ] The locked spec has exactly 3 core user stories.
- [ ] Each user story uses the correct format.
- [ ] Use cases are real scenarios.
- [ ] Acceptance criteria are testable.
- [ ] KPIs are measurable.
- [ ] Out of scope has at least 5 items.
- [ ] Definition of Done is concrete.
- [ ] Spec lock is committed to git.
- [ ] Verification passed.

---

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 3 complete
- **Last verified day:** Day 3
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 4.

## If You Are Stuck

Open your coding harness from your project folder and paste this:

```text
I am on OneMillion Day 03.

Here is the spec section I am stuck on:
[paste section]

Here is what feels unclear:
[describe issue]

Help me make the smallest edit that turns this into a buildable spec.
Do not create extra files.
Keep .onemillion/prd.md as the single source of truth.
Ask for one missing detail at a time if needed.
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| I have more than 3 stories | Pick the 3 required for the first useful loop. Move everything else to Out of Scope. |
| My use cases sound like features | Rewrite them as real moments from the user's day. |
| Acceptance criteria feel hard | Use: Given [context], when [action], then [result]. |
| KPIs are vague | Measure time saved, task completion, accepted output, repeat usage, or reduced manual work. |
| I want to pivot again | Only pivot if Day 2 evidence forced it. Otherwise lock and build. |

---

→ **Done with Day 3?** Move to [Day 4 — Stack + First Deploy](../day-04-stack/learn.md).
