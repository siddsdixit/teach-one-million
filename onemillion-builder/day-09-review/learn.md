# Day 9 — Implementation Review

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `review`
**Supporting agents:** build

Day 9 advances the OneMillion pipeline. Today is not random work; it is the next stage after the previous verified artifact.

## Learning Frame

- **Mental model:** Implementation Review turns the current pipeline artifact into the next artifact or verified product state.
- **What can go wrong:** the harness jumps into tasks without teaching the concept, or the learner lets the agent make product decisions without review.
- **What to ignore today:** ignore polish outside this day's gate. Finish the current stage before expanding scope.

## What You Learn

- learn what code review means
- compare implementation to refined PRD
- detect spec drift
- classify blockers, bugs, edge cases, and observations

## Core Concepts

- Review asks: did we build what the spec said?
- Spec drift is a finding even if the code seems to work.
- Findings should be classified as blockers, bugs, edge cases, or observations.

## What You Produce

- `.onemillion/review-findings.md`

## Human Decisions

- what to fix now
- what to defer
- whether drift is intentional

## Done Checklist

- [ ] .onemillion/review-findings.md exists
- [ ] blockers are fixed or explicitly deferred with reason
- [ ] code still builds

## Verify Your Day 9

When the checklist is true, ask your harness to run the OneMillion verifier for Day 9. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 10 — QA + Tests](../day-10-qa-tests/learn.md)
