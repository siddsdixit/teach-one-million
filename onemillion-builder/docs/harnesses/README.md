# Coding Harnesses

OneMillion is designed to run in the coding harness the learner already likes.

The universal path works everywhere:

```text
I am starting the OneMillion course.

Course repo:
https://github.com/siddsdixit/teach-one-million

Read AGENTS.md, onemillion-builder/course-manifest.json, onemillion-builder/docs/teaching-protocol.md, and onemillion-builder/course/single.md.
Become my OneMillion learning orchestrator.
Start me at Day 0.
First verify fork, clone, origin, and upstream.
Teach me one day at a time. Properly greet me, explain the course, explain the AI/human contract, introduce each day, provide copy-ready actions, and define what done means.
When I say "day done", verify the day and advance me.
Do not skip the learning or do the external tool steps for me.
```

For the most reliable setup, use the installer path:

```bash
git clone https://github.com/YOUR-USERNAME/teach-one-million.git
cd teach-one-million
./onemillion-builder/install-agents.sh
```

Then open the folder in your harness.

The installer verifies and creates local harness adapters for Claude Code, Cursor, Gemini, Antigravity-style agent rules, and GitHub Copilot. Codex uses the repository root `AGENTS.md` directly, so it does not need a separate generated adapter file.

## Harness Guides

- [Claude Code](claude-code.md)
- [Cursor](cursor.md)
- [Codex](codex.md)
- [Gemini](gemini.md)
- [Antigravity](antigravity.md)
- [GitHub Copilot](copilot.md)
