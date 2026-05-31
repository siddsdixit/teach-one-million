# Day 5 — Plan Architecture

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `plan`
**Supporting agents:** validate-plan

Day 5 advances the OneMillion pipeline. Today is not random work; it is the next stage after the previous verified artifact.

## Learning Frame

- **Mental model:** Plan Architecture turns the current pipeline artifact into the next artifact or verified product state.
- **What can go wrong:** the harness jumps into tasks without teaching the concept, or the learner lets the agent make product decisions without review.
- **What to ignore today:** ignore polish outside this day's gate. Finish the current stage before expanding scope.

## What You Learn

- understand architecture before coding
- choose backend path
- default to Next.js plus Supabase unless FastAPI is justified
- map data model and API boundaries
- create sprint briefs

## Core Concepts

- Architecture is the bridge between product decisions and code.
- The default backend path is Next.js + Supabase. FastAPI is optional only when there is a real backend reason.
- Sprint briefs are contracts. Each sprint should be small enough to verify.

## What You Produce

- `.onemillion/architecture.md`
- `.onemillion/sprints/`

## Human Decisions

- backend path: Supabase-only or FastAPI
- data model
- API boundary
- sprint sequence
- MVP technical scope

## Done Checklist

- [ ] .onemillion/architecture.md exists
- [ ] .onemillion/sprints/ exists
- [ ] backend path decision is recorded
- [ ] validate-plan passes or findings are resolved

## Verify Your Day 5

When the checklist is true, ask your harness to run the OneMillion verifier for Day 5. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 6 — App Shell + First Deploy](../day-06-app-shell/learn.md)
