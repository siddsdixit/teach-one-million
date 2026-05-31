# Day 5 — Build Guide

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

## Before You Start

- [ ] Previous day is verified in `.onemillion/state.json`.
- [ ] You are in the correct product/course workspace.
- [ ] You have read [learn.md](./learn.md).

## Step 1: Ask The Harness To Teach The Day

Paste this:

```text
I am on OneMillion Day 5: Plan Architecture.

Act as the `plan` agent for this day.
First teach me the concept in plain language.
Then guide me one step at a time.
Use the course manifest, single.md, and the current pipeline artifacts.
Do not skip my human decisions.
Do not create paperwork-only files.
When an external provider is needed, give the exact full URL and QA check.
```

## Step 2: Make The Human Decisions

Before the harness writes or changes anything, answer these decisions:

- backend path: Supabase-only or FastAPI
- data model
- API boundary
- sprint sequence
- MVP technical scope

## Step 3: Produce The Day Output

Expected output today:

- `.onemillion/architecture.md`
- `.onemillion/sprints/`

Work with the harness until the output matches the day's purpose. Review generated artifacts before accepting them.

## Step 4: External Tools

- No new external account is required today.

If the harness mentions an external provider, it must also give the exact link, permission/settings, and QA check from `onemillion-builder/docs/account-setup.md`.

## Step 5: Verify

Ask your harness:

```text
Run the OneMillion verifier for Day 5.
Inspect the relevant artifacts, app code, deployment links, and manual confirmations.
Record the result in .onemillion/state.json.
Do not create separate verifier markdown files.
```

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 5 complete
- **Last verified day:** Day 5
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 6.

## What Should Be True After Day 5

- [ ] .onemillion/architecture.md exists
- [ ] .onemillion/sprints/ exists
- [ ] backend path decision is recorded
- [ ] validate-plan passes or findings are resolved

## If You Are Stuck

Paste this into your harness:

```text
I am on OneMillion Day 5: Plan Architecture.
I am stuck on this part:
[paste the step or artifact]

Here is what I expected:
[describe]

Here is what happened:
[describe]

Help me find the smallest next action. Teach the concept if I am missing it. Do not skip the learning moment.
```


---

-> **Next:** [Day 6 — App Shell + First Deploy](../day-06-app-shell/learn.md)
