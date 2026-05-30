# OneMillion Builder Subdirectory Bootstrap

This file exists because many learners begin from the GitHub-rendered course page at `onemillion-builder/`.

If you are a coding harness reading this subdirectory first, do this:

1. Load the repository root `AGENTS.md`.
2. Load `onemillion-builder/course-manifest.json`.
3. Enforce the Preflight Gate before Day 0 or Day 1.
4. Use `onemillion-agents/agents/orchestrator.md` as the teaching protocol.

## Hard Preflight Gate

Do not start the course unless the learner is inside a real git clone of their own fork.

Required setup:

- `git rev-parse --show-toplevel` succeeds.
- Root `AGENTS.md` exists.
- `onemillion-builder/course-manifest.json` exists.
- `origin` points to the learner's fork.
- `upstream` points to `siddsdixit/teach-one-million`.
- The learner has starred and forked `siddsdixit/teach-one-million`.

If anything is missing, stop and fix setup first. Prefer:

```bash
./onemillion-builder/install-agents.sh
```

If the repo has not been cloned yet, give the learner this exact sequence and do not continue:

```bash
git clone https://github.com/YOUR-USERNAME/teach-one-million.git
cd teach-one-million
./onemillion-builder/install-agents.sh
```

Only after preflight is correct, start Day 0.
