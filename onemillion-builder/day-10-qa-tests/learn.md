# Day 10 — QA + Tests

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `test`
**Supporting agents:** debug, build

Day 10 advances the OneMillion pipeline. Today is not random work; it is the next stage after the previous verified artifact.

## Learning Frame

- **Mental model:** QA + Tests turns the current pipeline artifact into the next artifact or verified product state.
- **What can go wrong:** the harness jumps into tasks without teaching the concept, or the learner lets the agent make product decisions without review.
- **What to ignore today:** ignore polish outside this day's gate. Finish the current stage before expanding scope.

## What You Learn

- understand good QA
- write behavior checks from acceptance criteria
- test happy paths and edge cases
- run local and live QA

## Core Concepts

- QA is evidence, not vibes.
- Acceptance criteria become tests or manual QA checks.
- Good QA includes happy paths, edge cases, permissions, and live verification.

## What You Produce

- `.onemillion/test-results.md`

## Human Decisions

- critical paths to test manually
- acceptable risk
- QA evidence

## Done Checklist

- [ ] .onemillion/test-results.md exists
- [ ] core tests or manual QA checklist pass
- [ ] live app passes critical path QA

## Verify Your Day 10

When the checklist is true, ask your harness to run the OneMillion verifier for Day 10. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 11 — AI Feature Spec](../day-11-ai-spec/learn.md)
