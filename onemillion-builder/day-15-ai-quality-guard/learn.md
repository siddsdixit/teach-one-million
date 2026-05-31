# Day 15 — AI Quality Gate + Guard

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `test`
**Supporting agents:** guard, build

Day 15 advances the OneMillion pipeline. Today is not random work; it is the next stage after the previous verified artifact.

## Learning Frame

- **Mental model:** AI Quality Gate + Guard turns the current pipeline artifact into the next artifact or verified product state.
- **What can go wrong:** the harness jumps into tasks without teaching the concept, or the learner lets the agent make product decisions without review.
- **What to ignore today:** ignore polish outside this day's gate. Finish the current stage before expanding scope.

## What You Learn

- run AI evals or manual quality tests
- check cost risk
- audit secrets and auth
- fix critical safety issues before shipping

## Core Concepts

- AI quality gates prevent impressive but unreliable demos.
- Guard checks catch secrets, auth, RLS, privacy, and cost risks.
- Critical risks block shipping.

## What You Produce

- AI quality and guard evidence

## Human Decisions

- pass/fail examples
- quality threshold
- accepted risks

## Done Checklist

- [ ] AI evals or manual quality checks pass
- [ ] no exposed secrets
- [ ] critical guard checks pass
- [ ] cost/rate budget is represented

## Verify Your Day 15

When the checklist is true, ask your harness to run the OneMillion verifier for Day 15. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 16 — Ship Production](../day-16-ship-production/learn.md)
