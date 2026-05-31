# Day 7 — Auth + Database

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `build`
**Supporting agents:** ask, debug

Day 7 advances the OneMillion pipeline. Today is not random work; it is the next stage after the previous verified artifact.

## Learning Frame

- **Mental model:** Auth + Database turns the current pipeline artifact into the next artifact or verified product state.
- **What can go wrong:** the harness jumps into tasks without teaching the concept, or the learner lets the agent make product decisions without review.
- **What to ignore today:** ignore polish outside this day's gate. Finish the current stage before expanding scope.

## What You Learn

- create Supabase project
- understand auth
- create first tables
- enable RLS
- store env vars safely

## Core Concepts

- Auth proves the product knows who the user is.
- RLS proves users cannot read or mutate each other's data.
- Environment variables separate public configuration from secrets.

## What You Produce

- Supabase auth
- RLS-protected tables

## Human Decisions

- auth provider choices
- table shape
- RLS policy intent
- redirect URLs

## Done Checklist

- [ ] Supabase project exists
- [ ] signup works locally and live
- [ ] login/logout works
- [ ] RLS enabled
- [ ] env vars are not leaked

## Verify Your Day 7

When the checklist is true, ask your harness to run the OneMillion verifier for Day 7. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 8 — Core Build](../day-08-core-build/learn.md)
