# Day 14 — AI Data + Tools

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `build`
**Supporting agents:** research, review

Day 14 advances the OneMillion pipeline. Today is not random work; it is the next stage after the previous verified artifact.

## Learning Frame

- **Mental model:** AI Data + Tools turns the current pipeline artifact into the next artifact or verified product state.
- **What can go wrong:** the harness jumps into tasks without teaching the concept, or the learner lets the agent make product decisions without review.
- **What to ignore today:** ignore polish outside this day's gate. Finish the current stage before expanding scope.

## What You Learn

- choose tool use or RAG only if needed
- ground AI in user data safely
- protect privacy and RLS
- test cross-user boundaries

## Core Concepts

- RAG is optional. Tool use is optional. Use the simplest path that solves the user problem.
- AI data access must respect auth and RLS boundaries.
- Advanced AI behavior needs cross-user tests.

## What You Produce

- AI data/tool path or explicit skip decision

## Human Decisions

- RAG vs tool use vs no advanced AI data path
- data scope
- read/write limits
- privacy boundaries

## Done Checklist

- [ ] AI uses app data or tool actions only if justified
- [ ] scope is documented
- [ ] RLS still protects user data
- [ ] advanced AI path has tests or manual QA evidence

## Verify Your Day 14

When the checklist is true, ask your harness to run the OneMillion verifier for Day 14. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 15 — AI Quality Gate + Guard](../day-15-ai-quality-guard/learn.md)
