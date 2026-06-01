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

Day 7 turns the app shell into a product that knows who is using it and what data they are allowed to touch. Auth is one of the key product modules in the OneMillion pipeline, not a checkbox.

## Learning Frame

- **Mental model:** auth answers "who are you?", authorization answers "what can you do?", and RLS enforces "which rows are yours?" at the database boundary.
- **Input:** `.onemillion/architecture.md`, `.onemillion/sprints/S1-auth-db.md`, Day 6 app shell, and the deployed Vercel URL if available.
- **Output:** Supabase Auth, protected routes, first product tables, RLS policies, env vars, and verified signup/login/logout.
- **What can go wrong:** the harness wires a UI that looks logged in but does not protect data, exposes service-role keys, forgets redirect URLs, or never tests a second user.
- **What to ignore today:** do not build the full product workflow yet. Finish identity, session, database ownership, and RLS first.

## What You Learn

- what auth, sessions, authorization, and RLS mean
- when to use email/password, magic links, OAuth, invite-only access, or team roles
- how Supabase Auth works with Next.js
- how protected routes and auth callback routes work
- how to design first tables with `owner_id`, `tenant_id`, or membership fields
- how to keep public env vars separate from server-only secrets
- how to verify that one user cannot see another user's data

## Core Concepts

### Auth

Auth proves the product knows who the user is. The default course path is Supabase Auth because it gives beginners a real production auth system without writing password storage, token issuing, or session code from scratch.

### Session

A session is the signed proof that the user has already logged in. The app uses the session to show the right UI, protect pages, and make server-side requests as the current user.

### Authorization

Authorization is different from login. A logged-in user still needs permission to read, create, update, or delete a specific record. Admin/member/viewer roles belong here.

### Row Level Security

RLS is the database rule that prevents cross-user or cross-tenant data leaks. If a table stores private user or team data, RLS should be enabled and policies should reference the current authenticated user.

### Environment Variables

`NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY` can be used by browser code. Service-role keys and AI keys must stay server-only and must never be committed.

## What You Produce

- Supabase project configured for the app
- Supabase Auth wired into Next.js
- signup, login, logout, callback, and session state
- protected routes for private app areas
- first product tables from the architecture/sprint brief
- RLS policies for user-owned or tenant-owned records
- local and production redirect URLs
- `.env.example` placeholders and safe local env handling

## Human Decisions

- auth method: email/password, magic link, OAuth, invite-only, or admin-created users
- public vs protected pages
- whether the product is single-user, team/multi-tenant, or public/community
- profile or membership table shape
- RLS policy intent for each private table
- local and deployed redirect URLs

## Done Checklist

- [ ] Supabase project exists
- [ ] auth method is chosen and documented in the sprint output
- [ ] signup works locally and live when signup is part of the product
- [ ] login/logout works
- [ ] protected routes reject unauthenticated users
- [ ] first product tables exist
- [ ] RLS is enabled on private tables
- [ ] second-user isolation is tested when private data exists
- [ ] env vars are not leaked

## Verify Your Day 7

When the checklist is true, ask your harness to run the OneMillion verifier for Day 7. The verifier should inspect the relevant pipeline artifacts, app code, live URLs, and manual confirmations for this day.


---

-> **Next:** [Day 8 — Core Build](../day-08-core-build/learn.md)
