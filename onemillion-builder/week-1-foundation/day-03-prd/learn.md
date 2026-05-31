# Day 3 — Lock The Spec

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Week 1 | ~60-90 min | Last no-code day before building**

Day 1 created the first PRD. Day 2 validated it. Day 3 locks it into a buildable spec.

You are still working in one core pipeline artifact:

```text
.onemillion/prd.md
```

Today answers:

```text
Can an agent read this PRD and build the first version without guessing?
```

---

## Learning Frame

- **Mental model:** A spec is a contract between the learner, the product, and the build agents.
- **What can go wrong:** You leave fuzzy requirements, so the build agent fills gaps with guesses.
- **What to ignore today:** Ignore implementation details, UI polish, Vercel, Supabase, and AI APIs. Today is the last scope lock before code.

## What You'll Have After Today

- `.onemillion/prd.md` updated into the locked Day 3 spec
- exactly 3 core user stories
- 2-3 real use cases
- acceptance criteria for the MVP
- measurable KPIs or success signals
- a clear out-of-scope list
- a concrete definition of done
- an explicit spec-lock note saying what agents may and may not build

---

## Part 1: What Is A Spec?

A PRD explains the product. A spec makes the product buildable.

A good spec tells the build agent:

- who the product is for
- what pain it solves
- what evidence supports it
- what the MVP includes
- what the MVP does not include
- what the user must be able to do
- what counts as correct behavior
- what counts as done

Bad prompt:

```text
Build my app.
```

Better prompt:

```text
Build the MVP described in .onemillion/prd.md. Do not add features outside the 3 locked user stories. If the PRD is ambiguous, stop and ask.
```

This is the point of OneMillion: the learner uses agents, but the learner controls the spec.

## Part 2: Requirements

A requirement is a behavior the product must support.

Weak requirement:

```text
The app should be easy to use.
```

Buildable requirement:

```text
The teacher can paste classroom notes, select a student, generate a parent-update draft, edit the draft, and mark it ready to send.
```

Requirements should be:

- observable
- specific
- small enough to build
- connected to the validated pain
- limited to the MVP

## Part 3: User Stories

User stories describe what the user wants to do and why.

Format:

```text
As [specific user], I want [specific action] so that [specific outcome].
```

Day 3 requires exactly 3 user stories.

Not 5. Not 12. Exactly 3.

Why? Because the next days need a small build target. Too many stories make the build random.

Good:

```text
As a K-5 teacher, I want to paste rough classroom notes so that I can start from what I already capture during the week.
```

Bad:

```text
As a user, I want to manage everything so that my life is easier.
```

## Part 4: Use Cases

Use cases are real moments from the user's life.

They answer:

```text
When does the user use this product?
What happens before, during, and after?
```

Example:

```text
Weekly parent update: On Friday afternoon, the teacher pastes rough notes from the week, selects three students, generates draft updates, edits tone, and marks each update ready to send.
```

Use cases stop the spec from becoming abstract.

## Part 5: Acceptance Criteria

Acceptance criteria define what must be true for a feature to count as working.

Example:

```text
Given a teacher has pasted notes and selected a student,
When they click Generate Draft,
Then the app creates a parent-update draft that references that student's notes and can be edited before sending.
```

You do not need a large test suite today. You need the spec to contain testable behavior.

## Part 6: KPIs

KPIs are not vanity metrics. They should measure whether the product solves the pain.

Weak KPI:

```text
Get many users.
```

Better KPI:

```text
A teacher creates 3 usable parent-update drafts in under 10 minutes.
```

Good early KPIs usually measure:

- time saved
- successful task completion
- draft acceptance
- repeat usage
- reduced manual work

## Part 7: Out Of Scope

Out of scope is where good builders win.

Every tempting feature that is not part of the MVP goes here.

Examples:

- mobile app
- billing
- team accounts
- admin dashboard
- automated sending
- integrations
- analytics
- advanced permissions

If an agent tries to add these during the build, the spec says no.

## Part 8: Definition Of Done

Definition of Done is the exact state where v1 counts as complete.

Example:

```text
A teacher can sign up, paste classroom notes, select a student, generate a draft parent update, edit it, save it, and view saved drafts later. No automatic sending. No parent portal. No roster import.
```

If this sentence is vague, the build will drift.

---

## What Should Be True After Day 3

- [ ] `.onemillion/prd.md` includes a `Day 3 Locked Spec` section.
- [ ] The MVP has exactly 3 core user stories.
- [ ] Each user story uses the format `As [user], I want [action] so that [outcome]`.
- [ ] The PRD has at least 2 real use cases.
- [ ] The PRD has acceptance criteria for the MVP.
- [ ] The PRD has 2+ measurable KPIs or success signals.
- [ ] The PRD has 5+ out-of-scope items.
- [ ] The PRD has a concrete Definition of Done.
- [ ] The learner has committed the spec lock to git.

---

## Verify Your Day 3

Ask your harness to run the OneMillion verifier for Day 3. It should review `.onemillion/prd.md`, not create new paperwork.

---

## Share It

```text
Day 3 of OneMillion done.

Spec locked.

MVP: [one sentence]
3 core stories: [short summary]
Out of scope: [biggest thing I cut]

Tomorrow: first app + first deploy.
#BuildingWith1M
```

---

→ **Next:** [Day 4 — Stack + First Deploy](../day-04-stack/learn.md)
