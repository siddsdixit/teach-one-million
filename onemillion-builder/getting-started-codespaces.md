# Getting Started With Codespaces

**Time: 15-30 minutes. Browser-only setup.**

Use this path if you have never coded, cannot install software on your laptop, use a Chromebook, or got stuck on local setup.

By the end, you will have:
- A browser-based dev environment
- Claude Code installed inside that environment
- A GitHub account
- A Supabase account
- A Vercel account
- An Anthropic API key

---

## Step 1: Create The Accounts

Create these accounts first:

| Service | What it does | Sign up at |
|---------|-------------|------------|
| GitHub | Stores your code and gives you Codespaces | [github.com/signup](https://github.com/signup) |
| Anthropic | Powers Claude Code and your AI features | [console.anthropic.com](https://console.anthropic.com) |
| Supabase | Database + authentication for your app | [supabase.com](https://supabase.com) |
| Vercel | Hosts your app on the internet | [vercel.com/signup](https://vercel.com/signup) |

Use the same email for all four if possible. It reduces confusion later.

---

## Step 2: Create Your Anthropic API Key

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Open **Settings** → **API Keys**
3. Click **Create Key**
4. Name it `onemillion-course`
5. Copy the key immediately. It starts with `sk-ant-`.

Add $20 in billing if you can. Most builders spend $5-15 in Anthropic credits during the course.

Detailed guide: [Getting Your API Keys](getting-your-api-key.md)

---

## Step 3: Open A Blank Codespace

1. Go to [github.com/codespaces](https://github.com/codespaces)
2. Click **New codespace**
3. Choose **Blank**
4. Wait for the browser editor and terminal to load

You now have a working Linux dev environment in your browser.

---

## Step 4: Install Claude Code

In the Codespaces terminal, run:

```bash
npm install -g @anthropic-ai/claude-code
```

Verify it:

```bash
claude --version
```

You should see a Claude Code version number.

---

## Step 5: Add Your API Key

Run:

```bash
claude
```

When Claude Code asks for your API key, paste the Anthropic key you created.

Then type:

```text
Hello! Are you ready to help me build something?
```

If Claude replies, setup works.

---

## Step 6: Create Your Project Folder

In the Codespaces terminal:

```bash
mkdir my-onemillion-build
cd my-onemillion-build
```

This is where your 18-day product will live.

---

## What To Do Next

Start the course:

→ [Day 0 — Public Commitment](day-0-commit/README.md)

Then continue:

→ [Day 1 — Vision + Mental Map](week-1-foundation/day-01-vision/learn.md)

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Codespace will not start | Refresh GitHub, try again, or use a different browser. |
| `npm install` fails | Wait 30 seconds and run the command again. |
| `claude` not found | Close and reopen the Codespaces terminal, then try `claude --version`. |
| API key rejected | Confirm the key starts with `sk-ant-` and has no spaces or quotes. |
| Codespaces says free hours are exhausted | Switch to local setup or wait for your monthly quota reset. |

