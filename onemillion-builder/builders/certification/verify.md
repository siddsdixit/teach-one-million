# Certificate Verification Checklist

Use this checklist to self-verify before claiming your certificate.

## Phase Artifacts

- [ ] `.onemillion/prd.md` — product vision document exists
- [ ] `.onemillion/refined-prd.md` — engineering requirements with CRUD chains and acceptance criteria
- [ ] `.onemillion/design-spec.md` — design system and screen specs
- [ ] `.onemillion/architecture.md` — system architecture under 200 lines
- [ ] `.onemillion/sprints/` — at least 4 sprint brief files
- [ ] `.onemillion/test-results.md` — test run results from TEST agent
- [ ] `.onemillion/security-audit.md` — security audit with PASSED verdict
- [ ] `.onemillion/todo.md` — all sprints marked `[x]`

## Code Quality

- [ ] `backend/requirements.txt` — all dependencies listed
- [ ] `backend/tests/` — at least one test file per sprint
- [ ] `frontend/src/lib/api.ts` — typed API client present
- [ ] No hardcoded secrets in source (no `.env` files committed)
- [ ] `.env.example` files present in both backend and frontend

## Deployment

- [ ] Live frontend URL returns 200
- [ ] Live backend `/api/v1/health` returns `{"status": "ok"}`
- [ ] GitHub repo is public with full commit history
- [ ] All commits present (one per sprint, following `type: description` format)

## Product

- [ ] User can register and log in
- [ ] User can perform the core CRUD loop on the primary entity
- [ ] App works on mobile viewport (375px width)
- [ ] No unhandled errors visible in the UI
- [ ] Seed data loaded — app looks real on first visit

## Build Journal

- [ ] 18 entries written (Days 1-18)
- [ ] Each entry answers the day's Reflect assignment
- [ ] Final entry (Day 18) includes your product origin story

---

Once all boxes are checked, run `/sell Generate my completion certificate` in Claude Code.
