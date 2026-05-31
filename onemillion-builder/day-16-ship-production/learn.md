# Day 16 — Ship Production

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `ship`
**Supporting agents:** guard, debug

Day 16 advances the OneMillion pipeline. Today is not random work; it is the next stage after the previous verified artifact.

## Learning Frame

- **Mental model:** Ship Production turns the current pipeline artifact into the next artifact or verified product state.
- **What can go wrong:** the harness jumps into tasks without teaching the concept, or the learner lets the agent make product decisions without review.
- **What to ignore today:** ignore polish outside this day's gate. Finish the current stage before expanding scope.

## What You Learn

- production deployment verification
- custom domain optionality
- monitoring basics
- rollback and smoke tests

## Core Concepts

- Shipping means the live product is reachable, observable, and verifiable.
- Custom domains are optional; production verification is not.
- Monitoring turns failures into signals.

## What You Produce

- verified production app

## Human Decisions

- custom domain or skip
- alert email
- monitoring thresholds

## Done Checklist

- [ ] production URL works
- [ ] live app matches local source
- [ ] monitoring configured or documented skip
- [ ] custom domain works or skip is documented

## Verify Your Day 16

When the checklist is true, ask your harness to run the OneMillion verifier for Day 16. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 17 — Sell + First Users](../day-17-sell-users/learn.md)
