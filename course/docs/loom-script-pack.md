# Loom Script Pack

Use these as launch recording scripts. They are written for short Looms, not polished studio videos. Keep them human, direct, and screen-led.

Recommended recording style:

- Show your face for the first 20-30 seconds, then switch to screen.
- Keep each video 5-12 minutes.
- Do not over-explain every button. Show the exact learner action.
- End every video with the exact phrase: `When this is done, type day done in your coding harness.`
- If you make a small mistake, leave it in unless it confuses the learner. The course should feel doable, not cinematic.

## Launch Set

| # | Video | Target Length | Primary Job |
|---:|---|---:|---|
| 1 | Day 0: Welcome, Mission, GitHub, Fork, Clone, Install | 12-15 min | Get the learner oriented and unstuck from setup |
| 2 | Day 1: Idea Agent + PRD | 8-10 min | Teach what a good idea is and produce first PRD |
| 3 | Day 2: Validate The PRD | 7-9 min | Teach evidence, interviews, competitors, MVP |
| 4 | Day 3: Spec Agent | 8-10 min | Teach spec, CRUD, requirements, acceptance criteria |
| 5 | Day 4: Design Agent | 10-12 min | Teach product design, MUI, screens, states, mockup approval |
| 6 | Day 5: Architecture + Sprint Briefs | 12-15 min | Teach architecture decisions and build contracts |
| 7 | Days 6-8: App Shell, Deploy, Auth, Core Build | 12-15 min | Show first real app path |
| 8 | Days 9-10: Review, Manual QA, Automated Tests | 8-10 min | Teach review and testing discipline |
| 9 | Days 11-12: Add The First AI Feature | 10-12 min | Teach API keys, server-side AI calls, safety |
| 10 | Days 16-18: Ship, Sell, Demo, Builder Claim | 10-12 min | Teach production, launch, and final proof |

---

# Video 1 - Day 0: Welcome, Mission, GitHub, Fork, Clone, Install

## Goal

The learner understands what OneMillion is, why the fork matters, how the AI teacher works, and how to get to Day 0 done.

## Open On Screen

1. `https://github.com/siddsdixit/one-million-builders/tree/main/course`
2. `https://github.com/signup`
3. `https://github.com/siddsdixit/one-million-builders/fork`
4. Terminal in a clean folder
5. A coding harness such as Claude Code, Codex, Cursor, Gemini, or Copilot

## Script

Welcome to OneMillion. I am Sid, and I am excited you are here.

This course has one mission: help one million people learn how to take an idea and turn it into a real product with AI. Not a toy. Not a fake tutorial. A real app or agent, in a real GitHub repo, deployed to a real URL, with a demo and proof trail at the end.

You do not need to be an experienced programmer to start. You do need to be willing to make decisions, read what your AI teacher shows you, and keep going one verified day at a time.

The way this course works is different from a normal video course. You are not just watching me code. Your coding harness becomes your teacher. That can be Claude Code, Codex, Cursor, Gemini, Copilot, Antigravity, or another tool that can read a GitHub repo and work inside your project.

The course gives that harness a teaching protocol, a day-by-day plan, agents, verifiers, and exact setup links. The AI teacher guides. You decide. You touch the real tools. The AI verifies.

Here is the course page. This is the link you should share or paste into your coding harness:

`https://github.com/siddsdixit/one-million-builders/tree/main/course`

The first thing we do is Day 0. Day 0 is not coding. Day 0 is orientation, commitment, and setup.

You will learn what the OneMillion pipeline is: idea, research, PRD, spec, design, architecture, build, review, test, guard, ship, and sell. This pipeline matters because most people fail when they jump straight into code. They build before they know what they are building, who it is for, or how they will know it works.

By the end of the course, you should have a live app or agent, authentication, database where needed, an AI feature where appropriate, production checks, a Loom demo, and a Builder Claim.

Now let us set up your workspace.

First, you need a GitHub account. If you do not have one, go here:

`https://github.com/signup`

Create the account. Verify your email. Use a username you are comfortable having on a public builder profile.

Next, star the course repo. This helps the mission spread, but it also helps you find the course again.

Now fork the repo. A fork is your own copy of the course repo. It matters because your fork becomes your learning workspace and proof trail.

Use this link:

`https://github.com/siddsdixit/one-million-builders/fork`

Choose your GitHub account as the owner. Keep the repo name as `one-million-builders`. Public is best if you are comfortable building in public. Private is okay if you need privacy.

Once the fork exists, clone your fork. Replace `YOUR-USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/one-million-builders.git
cd one-million-builders
./course/install-agents.sh
```

The install script checks that you are inside a real clone, that your origin points to your fork, that Sid's repo is the upstream, and that the course can create the harness instructions it needs.

If it stops you, that is good. It means it found a setup issue before Day 1.

Now open this folder in your coding harness and paste this:

```text
I am taking the OneMillion course at:
https://github.com/siddsdixit/one-million-builders/tree/main/course

Read AGENTS.md and course/course-manifest.json.
Read course/docs/teaching-protocol.md.
Read course/days/single.md.
Become my OneMillion learning orchestrator.
Properly greet me, explain the course, explain the AI/human contract, and guide me through GitHub setup, fork, clone, install, and Day 0.
If I do not have GitHub yet, walk me through account creation with exact links.
When the local clone is ready, enforce the Preflight Gate before Day 0.
Teach me one day at a time with copy-ready actions and clear done checklists.
When I say "day done", verify the day and advance me.
Do not skip the learning or do the external tool steps for me.
```

Day 0 also asks for a public or private commitment. Public commitment helps because it creates accountability. More people finish when someone else knows they started.

If you can post publicly, use LinkedIn or X.

LinkedIn:

`https://www.linkedin.com/feed/`

Tag me here:

`https://www.linkedin.com/in/siddharthdixit/`

Copy this:

```text
Starting OneMillion today.

I am learning how to build and ship a real AI-native product in 18 days.
The course is free and open source:
https://github.com/siddsdixit/one-million-builders/tree/main/course

Day 0: committed.
Next: idea, PRD, spec, design, architecture, build, test, ship, sell.

Following the course by @Siddharth Dixit.
```

If you do not want to post publicly, send a private message to five real people:

```text
I am starting OneMillion today.

I am going to build and ship a real AI-native product in 18 days.
I am telling you because I want accountability.

Course:
https://github.com/siddsdixit/one-million-builders/tree/main/course

I will send you my demo when I finish.
```

That is Day 0. You understand the mission, you understand the pipeline, you have a fork, you have a local clone, the installer ran, and you made a commitment.

When this is done, type `day done` in your coding harness.

---

# Video 2 - Day 1: Idea Agent + PRD

## Goal

The learner understands what makes an idea worth building and uses the idea agent to produce `.onemillion/prd.md`.

## Open On Screen

1. `course/days/day-01-idea/learn.md`
2. `.onemillion/prd.md` after generation
3. Coding harness chat

## Script

Day 1 is about the idea.

Most people think an idea is a clever feature. In OneMillion, a good idea starts with an unmet user need or a real pain point.

The question is not, "Can I build something with AI?" The question is, "Who has a painful job, what are they trying to do, where are they stuck, and what would a better solution make possible?"

Today you will describe five things.

First, the target user. Be specific. Not "everyone." Say "independent tutors who manage students in spreadsheets" or "small team leads who lose meeting action items."

Second, the pain point or unmet need. What is difficult, slow, expensive, confusing, or currently done with messy workarounds?

Third, the data. What information will the product use? Documents, emails, PDFs, CRM rows, calendar events, notes, forms, uploaded files, or user-entered records.

Fourth, the ideal solution. If you close your eyes and the problem is solved, what does the user see? What do they click? What becomes easier?

Fifth, success criteria. How will you know this product helped? Time saved, fewer missed tasks, higher completion rate, better quality, faster decisions, less manual work.

You will also learn user stories. A user story is a simple way to describe behavior from the user's perspective:

`As a [type of user], I want to [do something], so that [outcome].`

For example:

`As a teacher, I want to see which students are falling behind, so that I can intervene before the next exam.`

Today the idea agent takes your raw answers and turns them into a PRD, a product requirements document.

A PRD explains the user, problem, product direction, user stories, success criteria, assumptions, competitive alternatives, and basic market thinking.

The idea agent may also talk about TAM, SAM, and SOM.

TAM is the total possible market. SAM is the part of that market you could realistically serve. SOM is the small wedge you might actually reach first.

Do not obsess over perfect numbers today. The point is honest thinking.

Now ask your harness:

```text
I am on OneMillion Day 1.
Teach me what makes a good idea.
Interview me about my target user, pain point, data sources, ideal solution, user stories, and success criteria.
Then run the idea agent and create .onemillion/prd.md.
Do not mark Day 1 done until I review and approve the PRD.
```

When the PRD appears, read it. Do not blindly accept it. Ask:

- Does this describe a real user?
- Is the pain specific?
- Are the user stories useful?
- Are the KPIs measurable?
- Is the MVP small enough?
- Did the agent invent anything that I do not believe?

Edit the PRD with your harness until it feels true enough to test.

When this is done, type `day done` in your coding harness.

---

# Video 3 - Day 2: Validate The PRD

## Goal

The learner validates whether the PRD is serious, updates the same PRD, and defines the MVP.

## Open On Screen

1. `.onemillion/prd.md`
2. `course/days/day-02-validate-prd/learn.md`
3. Notes from one user conversation or competitor review

## Script

Day 2 asks a hard question: is this PRD real?

Day 1 gave you a product direction. Day 2 tests it against reality.

Validation does not mean asking people, "Do you like my idea?" Most people will be polite. Validation means learning whether the pain exists, how people handle it today, how often it happens, how expensive it is, and what they would actually change.

If you can, talk to real potential users. Even two or three conversations can change the product.

Ask questions like:

```text
When was the last time this problem happened?
What did you do?
What did it cost you in time, money, stress, or quality?
What tools do you use today?
What happens if you do nothing?
What would make this worth switching for?
```

Avoid questions like:

```text
Would you use this?
Do you like this idea?
Would you pay for this?
```

Those create fake confidence.

Today you also look at competitors and alternatives. A competitor is not only another startup. It can be spreadsheets, email, a human assistant, a checklist, a Slack channel, or doing nothing.

You should update the PRD with what you learned.

You should also decide the MVP, the minimum viable product.

An MVP is not a bad version of the full product. It is the smallest complete version that proves the main value.

The full product might have dashboards, teams, billing, analytics, integrations, mobile, and AI. The MVP should usually have one target user, one main workflow, and one clear success moment.

Ask your harness:

```text
I am on OneMillion Day 2.
Help me validate the Day 1 PRD.
Interview me about user conversations, competitor alternatives, ICP, MVP, missing use cases, and success criteria.
Update the existing .onemillion/prd.md.
Do not create extra paperwork unless necessary.
The verifier should inspect the PRD and tell me whether it matches Day 2 goals.
```

By the end of Day 2, your PRD should be sharper, more honest, and smaller.

When this is done, type `day done` in your coding harness.

---

# Video 4 - Day 3: Spec Agent

## Goal

The learner understands spec, CRUD, functional requirements, acceptance criteria, and uses the spec agent to refine the PRD/spec.

## Open On Screen

1. `.onemillion/prd.md`
2. Day 3 learn/build files
3. Generated spec/refined PRD output

## Script

Day 3 is about the spec.

A PRD says what product should exist and why. A spec is a more detailed blueprint of what we are going to build and how it should behave.

The spec matters because AI coding tools need clear boundaries. If the scope is vague, the build becomes random. If the spec is clear, the builder can create the product in smaller, testable pieces.

One core idea today is CRUD: create, read, update, delete.

Most software is built from these operations. A user creates a task, reads a dashboard, updates a status, deletes an old record. Even advanced products often start with clear CRUD blocks.

The spec agent helps break the product into functional requirements. A functional requirement describes what the product must do.

For example:

```text
Users can create a client record with name, email, status, and notes.
Users can update the status of a client.
Users can filter clients by status.
Users can delete a draft client record.
```

A good spec also includes acceptance criteria. Acceptance criteria explain how we know a feature works.

For example:

```text
Given I am signed in,
when I create a client with required fields,
then the client appears in my dashboard and is saved to the database.
```

Today you are freezing the first buildable scope. Not forever. Just enough to build the MVP without drifting.

Ask your harness:

```text
I am on OneMillion Day 3.
Teach me what a spec is and why it matters.
Read my existing .onemillion/prd.md.
Run the spec agent to break the product into CRUD blocks, functional requirements, user stories, acceptance criteria, KPIs, and done criteria.
Help me review what is in or out of the MVP.
Update the existing core product documents instead of creating unnecessary new files.
Do not mark Day 3 done until I approve the spec.
```

When the spec is generated, read it like a builder.

Ask:

- Can I imagine the screens?
- Are the user stories specific?
- Are the requirements testable?
- Is the MVP too big?
- Is anything important missing?
- Did the agent add features I do not want yet?

Edit, rerun, and approve.

When this is done, type `day done` in your coding harness.

---

# Video 5 - Day 4: Design Agent

## Goal

The learner learns product design basics and approves screens, states, seed data, design system, and mockup before app code.

## Open On Screen

1. Day 4 learn file
2. `.onemillion/design-spec.md`
3. `.onemillion/design-system.md`
4. `.onemillion/mockup/index.html`

## Script

Day 4 is where the product becomes visible.

Design is not decoration. Design is how the product explains itself to the user.

Good design answers:

- What should the user notice first?
- What action should they take next?
- What changed after they clicked?
- What happens when there is no data?
- What happens when something fails?
- Does the flow make the painful job easier?

The design should match the target user. A dashboard for enterprise managers should feel different from a mobile-first app for students. A power-user operations tool should be dense and scannable. A consumer product may need more warmth and onboarding.

In this course, MUI and Material Design are the shared design language. That gives learners a stable component system: buttons, dialogs, tables, forms, tabs, alerts, chips, navigation, and responsive layout.

Today the design agent should create:

- A design spec
- A design system
- Screen specs
- Realistic seed data
- An HTML mockup preview

Seed data matters. Empty apps are hard to judge. Realistic sample records help you see whether the product actually makes sense.

Ask your harness:

```text
I am on OneMillion Day 4.
Teach me what good product design means for my target user.
Read the PRD/spec.
Run the design agent to create design spec, design system, screen specs, seed data, and an HTML mockup.
Use MUI / Material Design as the course design language.
Show me the mockup and ask me to approve or revise it.
Do not start app code yet.
Do not mark Day 4 done until I approve the design direction.
```

When you inspect the mockup, do not ask only, "Is it pretty?"

Ask:

- Does this speak to my target user?
- Is the main workflow obvious?
- Are empty, loading, error, success, partial, and full states considered?
- Does mobile work?
- Does desktop work?
- Is the copy clear?
- Does the product feel like it could solve the pain from Day 1?

Approve it only when it feels good enough to build.

When this is done, type `day done` in your coding harness.

---

# Video 6 - Day 5: Architecture + Sprint Briefs

## Goal

The learner understands architecture decisions and uses the plan agent to produce architecture and sprint briefs.

## Open On Screen

1. `.onemillion/architecture.md`
2. `.onemillion/sprints/`
3. Day 5 learn/build files

## Script

Day 5 is one of the most important days in the course.

Architecture means deciding how the system is organized before you build it.

Architecture is where we decide:

- Is this a web app, mobile-first app, agent, or hybrid?
- What is frontend?
- What is backend?
- What is database?
- Where does auth live?
- Where do AI calls happen?
- What data must be protected?
- Is this single-user or multi-tenant?
- Do we need roles and permissions?
- How should the work be split into smaller build sprints?

The default course stack is Next.js, React, MUI, Vercel, and Supabase.

For many apps, Supabase plus Next.js is enough. Supabase gives auth, database, storage, and Row Level Security. Next.js gives frontend and server-side routes or server actions.

But some apps really are backend-heavy. If the product needs complex Python processing, background jobs, custom APIs, heavy integrations, or backend workflows that do not fit well in Next.js, then FastAPI can be justified.

The key is not ideology. The key is fit.

Today you should explicitly decide the backend path:

```text
Supabase-only
Next.js route handlers / server actions
FastAPI backend
Hybrid
```

You also decide tenancy.

Single-tenant means one user owns their own data. Multi-tenant means multiple people belong to an organization or workspace. RBAC means role-based access control: admins, members, viewers, managers, reviewers, or other roles with different permissions.

Even if you do not build every role today, you should think about it now. Auth and data models are painful to fix late.

Ask your harness:

```text
I am on OneMillion Day 5.
Teach me architecture in plain language.
Read my PRD, spec, and design artifacts.
Help me decide product type, frontend, backend, database, auth, tenancy, RBAC, security, scalability, integrations, observability, and cost constraints.
Default to Next.js + MUI + Supabase + Vercel unless FastAPI or another backend is clearly justified.
Run the plan agent and create .onemillion/architecture.md and sprint briefs in .onemillion/sprints/.
Explain why smaller sprint briefs are better build contracts for LLMs.
Do not mark Day 5 done until I approve the architecture and sprint plan.
```

Sprint briefs are build contracts. They help AI coding tools work in smaller slices, with less context confusion, easier testing, and cleaner reviews.

By the end of Day 5, you should know what you are building first and why.

When this is done, type `day done` in your coding harness.

---

# Video 7 - Days 6-8: App Shell, Deploy, Auth, Core Build

## Goal

The learner sees the first real app path: Next.js/MUI shell, Vercel deploy, Supabase auth/database, and the main workflow.

## Open On Screen

1. Product repo folder
2. Vercel dashboard
3. Supabase dashboard
4. Running app locally and deployed URL

## Script

Days 6 through 8 are where the product becomes a working app.

Day 6 creates the app shell and gets the first deployment live. This is important because shipping starts early. A live URL changes how you think. You are no longer writing in private. You are building something that can be checked.

The course default is Next.js, React, MUI, and Vercel.

Ask your harness on Day 6:

```text
I am on OneMillion Day 6.
Create the Next.js + MUI app shell from the approved design and architecture.
Deploy it to Vercel.
Verify the live deployment matches the local source.
Do not mark Day 6 done until the app has a live URL and the verifier confirms it.
```

Day 7 adds auth and database.

Auth means we know who the user is. Authorization means we know what they are allowed to access. The database stores product records. Row Level Security protects rows so users cannot read each other's private data.

Ask:

```text
I am on OneMillion Day 7.
Teach me authentication, authorization, Supabase, database tables, and RLS.
Create Supabase auth and the first product tables from the architecture.
Protect private routes.
Configure local and Vercel environment variables.
Test with more than one user where possible.
Do not mark Day 7 done until auth, database, and RLS checks pass.
```

Day 8 builds the core workflow.

This is not the AI feature yet. It is the main useful workflow your target user needs even before AI.

Ask:

```text
I am on OneMillion Day 8.
Build one useful sprint from the sprint briefs.
Focus on the main workflow, not extra features.
Connect UI to Supabase.
Implement forms, validation, create/read/update/delete where needed, and visible success/error states.
Keep building until one real user journey works end to end.
```

At this stage, inspect the app like your target user.

Does it flow? Is it simple? Does it speak to the pain point? Is the main workflow obvious? Would this help even in a small way?

When this is done, type `day done` in your coding harness.

---

# Video 8 - Days 9-10: Review, Manual QA, Automated Tests

## Goal

The learner understands review, manual QA, automated QA, and how to use tests without turning the course into paperwork.

## Open On Screen

1. Running app
2. Review output
3. Test plan/test cases generated by harness
4. Terminal running tests

## Script

Days 9 and 10 are about quality.

Day 9 is implementation review. We compare what was built against the PRD, spec, design, and architecture.

Code review is not just looking for syntax problems. It asks:

- Did we build the right thing?
- Did we drift from the spec?
- Is anything insecure?
- Is the data model wrong?
- Is the UI confusing?
- Are there bugs or edge cases?
- What should be fixed before continuing?

Ask:

```text
I am on OneMillion Day 9.
Review the implementation against the PRD, spec, design, architecture, and sprint brief.
Classify findings as blocker, bug, UX issue, security issue, or accepted MVP risk.
Help me fix the important issues.
```

Day 10 is QA and tests.

Good QA means proving the product works for the target user. Manual QA means you personally use the app and inspect the experience. Automated QA means tests run repeatedly so regressions are caught.

Manual QA should include:

- First-time user flow
- Login/logout
- Main workflow
- Empty state
- Error state
- Mobile and desktop inspection
- Live deployment check

Automated QA can include:

- Unit tests for functions
- Backend/API tests
- Frontend component tests
- Playwright or Selenium browser tests
- Database/RLS checks
- AI behavior checks later

For this course, Playwright is especially useful because it tests the app like a user in a browser.

Ask:

```text
I am on OneMillion Day 10.
Teach me what good QA means.
Create test cases from my acceptance criteria.
Run manual QA on the live app and local app.
Add or run automated tests appropriate for this product: frontend tests, backend/API tests, Playwright browser tests, database checks, or other relevant checks.
Show me exactly what passed, what failed, and what must be fixed before moving on.
```

The goal is not perfect enterprise QA. The goal is no obvious broken core flow.

When this is done, type `day done` in your coding harness.

---

# Video 9 - Days 11-12: Add The First AI Feature

## Goal

The learner understands what adding AI means, how API keys work, and how to build one useful AI feature safely.

## Open On Screen

1. Anthropic Console, OpenAI keys page, or Google AI Studio
2. `.env.local`
3. Server route/action
4. App using the AI feature

## Script

Days 11 and 12 add AI.

Adding AI means your application calls a large language model to do a specific job. The AI is not magic dust. It should help the user complete a real task.

For example, if you are building a college counselor app, the AI might read a student's profile and suggest next steps. If you are building a meeting follow-up app, the AI might extract action items and owners. If you are building a customer support tool, it might draft a response from context.

Day 11 is AI feature specification. You decide what the AI should do, what inputs it receives, what output it returns, and how you know the output is good.

Ask:

```text
I am on OneMillion Day 11.
Teach me what adding AI means.
Help me choose one useful AI feature tied to the existing PRD.
Update the existing core documents instead of creating a new spec flow.
Define inputs, outputs, prompt plan, structured response, privacy boundary, cost limit, latency target, failure modes, and acceptance criteria.
Do not overcomplicate with LangChain, LangGraph, CrewAI, Google ADK, Langflow, or RAG unless this product truly needs it.
```

Day 12 builds it.

You need an API key from a provider.

Anthropic:

`https://console.anthropic.com/`

OpenAI:

`https://platform.openai.com/api-keys`

Google AI Studio:

`https://aistudio.google.com/app/apikey`

Store secrets safely. Local secrets go in `.env.local`. Deployed secrets go in Vercel environment variables. Never put real API keys in GitHub. Never expose AI keys as `NEXT_PUBLIC_*`.

Ask:

```text
I am on OneMillion Day 12.
Build the selected AI feature server-side.
Help me create or use the provider API key safely.
Store the key in .env.local and Vercel env vars.
Update .env.example with placeholders only.
Build the route handler or server action.
Show AI output inside the app.
Handle missing key, invalid key, timeout, rate limit, and bad response errors.
Run a key leak scan before marking the day done.
```

Tool calling means the model can call defined functions or tools to take actions or fetch structured information. It is powerful, but you do not need it for every first AI feature.

Advanced frameworks like LangChain, LangGraph, Langfuse, CrewAI, and Google ADK are useful later. For this course, start simple. One server-side AI feature that solves one user problem is enough.

When this is done, type `day done` in your coding harness.

---

# Video 10 - Days 16-18: Ship, Sell, Demo, Builder Claim

## Goal

The learner understands the final shipping arc: production verification, brand/marketing/first users, demo, and Builder Claim.

## Open On Screen

1. Vercel production deployment
2. Supabase production settings
3. Product landing page
4. Loom recorder
5. Builder Claim issue page

## Script

The final stretch is where the product becomes launchable.

Day 16 is production shipping.

Production is not just "it deployed once." Production means the live app has the right environment variables, auth redirect URLs, database security, smoke tests, monitoring, and rollback path.

Ask:

```text
I am on OneMillion Day 16.
Verify production shipping.
Check Vercel production env vars, Supabase Site URL and redirect URLs, RLS, live smoke tests, logs, monitoring, and rollback plan.
Confirm the live app matches the local build in a meaningful way.
Update .onemillion/state.json with the live URL only after verification passes.
```

Monitoring can be simple. Vercel Analytics can show traffic. Sentry can catch errors. UptimeRobot or another uptime monitor can ping the site and alert if it is down. Use the simplest useful setup for the learner's product.

Day 17 is sell users.

Selling does not mean being spammy. It means explaining who the product is for, what pain it solves, and inviting the right people to try it.

Ask:

```text
I am on OneMillion Day 17.
Run the sell agent.
Help me create positioning, a simple product page, pricing stance, launch posts, first-user outreach messages, and a feedback capture loop.
Keep it honest and specific to my target user.
```

Your product page should answer:

- Who is this for?
- What painful job does it help with?
- What does it do?
- Why is it better than the current workaround?
- What should the user do next?

Day 18 is demo and Builder Claim.

Your demo should be short:

1. Problem
2. Target user
3. Product walkthrough
4. AI feature if included
5. Live URL
6. What you learned
7. What comes next

Record the Loom. Keep it under five minutes if possible.

Then submit the Builder Claim:

`https://github.com/siddsdixit/one-million-builders/issues/new/choose`

Ask:

```text
I am on OneMillion Day 18.
Help me prepare a 5-minute Loom demo and Builder Claim.
Verify my live URL, GitHub proof trail, daily verification trail, final README, and demo link.
Create the Builder Claim packet.
```

This is the point of the course. Not just learning concepts. Shipping proof.

When this is done, type `day done` in your coding harness.

