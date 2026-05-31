# Day 12 — First AI Build

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `build`
**Supporting agents:** debug

Day 12 advances the OneMillion pipeline. Today is not random work; it is the next stage after the previous verified artifact.

## Learning Frame

- **Mental model:** First AI Build turns the current pipeline artifact into the next artifact or verified product state.
- **What can go wrong:** the harness jumps into tasks without teaching the concept, or the learner lets the agent make product decisions without review.
- **What to ignore today:** ignore polish outside this day's gate. Finish the current stage before expanding scope.

## What You Learn

- call Claude from the server side
- handle API keys safely
- build prompt inputs from product data
- show AI output in the app

## Core Concepts

- API keys must stay server-side.
- Prompts should be grounded in the product spec and user context.
- The first AI build should prove one useful path before adding advanced behavior.

## What You Produce

- working first AI call

## Human Decisions

- prompt behavior
- sample inputs
- first output quality

## Done Checklist

- [ ] AI route or server action exists
- [ ] AI output appears in app
- [ ] API key is not exposed to client code
- [ ] live app AI path works

## Verify Your Day 12

When the checklist is true, ask your harness to run the OneMillion verifier for Day 12. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 13 — AI UX + Safety](../day-13-ai-ux-safety/learn.md)
