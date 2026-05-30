# Getting Started

**Time: 30-60 minutes. One-time setup.**

By the end of this guide you'll have:
- A working dev environment on your laptop
- Claude Code installed and authenticated
- A GitHub account
- A Supabase account
- A Vercel account
- An Anthropic API key

That's it. Then you go to [Day 1](./week-1-foundation/day-01-vision/learn.md).

> 🧭 **First time with any of this?** Don't worry. Every step has expected output. If something doesn't match, the [troubleshooting table](#troubleshooting) at the bottom has answers. If you're still stuck after 10 minutes, ask in the cohort Slack (or use [Codespaces](#codespaces-fallback-last-resort) as a fallback).

> 🔧 **Engineers:** You probably have most of this already. Skip to step 4 (Claude Code) if Node/Git/an editor are installed.

---

## Pick Your Path First (1 min decision)

Two paths through this course:

### Path A — Local Install (recommended for most)
You install everything on your laptop. Real dev environment forever. Skill transfers to any project. **Pick this if:** you have admin rights on your laptop, an OS update from the past 2 years, and you've used a terminal more than 3 times in your life.

→ Continue below with Step 1.

### Path B — Codespaces (browser-only, zero install)
Everything runs in your browser via GitHub Codespaces. No local install. Works on Chromebook, locked-down corporate laptops, anything with a browser. Free 60 hrs/month covers the course.

**Pick this if:** you're on a corporate laptop where you can't install software, you've never opened a terminal in your life, your laptop is more than 5 years old, OR local install has failed for you in the past.

→ [Skip to Codespaces setup](#codespaces-fallback-last-resort) (it's at the bottom of this page — same instructions, less friction).

> 💡 **Honest take:** Path A teaches you more. Path B gets you to Day 1 faster. Both produce a real shipped product by Day 18. Pick what fits your reality.

---

## Step 1: Install Node.js (the engine your app runs on)

Node.js is the runtime your Next.js app needs. You'll use it daily.

### Mac

Open **Terminal** (Cmd+Space, type "Terminal", press Enter). Paste this and press Enter:

```bash
curl -fsSL https://nodejs.org/dist/v20.18.0/node-v20.18.0.pkg -o /tmp/node.pkg && sudo installer -pkg /tmp/node.pkg -target /
```

Verify it worked:
```bash
node -v
```

**You should see:** `v20.18.0` (or higher).

### Windows

1. Go to [nodejs.org](https://nodejs.org)
2. Click the green button labeled **"20.x.x LTS"** (the one on the left)
3. Run the installer. Click Next on every screen. Default options are fine.
4. Open **PowerShell** (Start menu → type "PowerShell")
5. Type `node -v` and press Enter

**You should see:** `v20.18.0` (or higher).

> 🆘 **If you see `command not found` or `node is not recognized`:** Close and reopen your terminal. It needs to re-read the PATH. Still not working? See [troubleshooting](#troubleshooting).

---

## Step 2: Install Git (your time machine)

Git tracks every change you make. Without it you can't deploy to Vercel.

### Mac
```bash
xcode-select --install
```
A dialog box pops up. Click **Install**. Wait 5-10 minutes for Apple's developer tools.

Verify: `git --version` → **You should see:** `git version 2.x.x`.

### Windows
1. Go to [git-scm.com/downloads](https://git-scm.com/downloads)
2. Click **Download for Windows**
3. Run installer. Default options.
4. Open **Git Bash** from the Start menu (yes, a new terminal — Git Bash is what you'll use on Windows for the course)
5. Type `git --version`

**You should see:** `git version 2.x.x`.

> 💡 **Windows note:** Use **Git Bash** as your terminal for the rest of the course, not PowerShell or CMD. Git Bash gives you Unix-style commands (`ls`, `cd`, etc.) — much easier when the course shows commands.

---

## Step 3: Install VS Code (or your editor of choice)

VS Code is the default. It's free and works on Mac + Windows.

1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Download for your OS, run installer
3. Open VS Code once to confirm it launched

> 🔧 **Engineers:** If you prefer Cursor, Antigravity, Windsurf, or JetBrains — install any of them. The course works with all of them. See [tools/README.md](./tools/README.md) for editor-specific notes.

---

## Step 4: Install Claude Code (your AI builder)

This is your agentic AI tool. It lives in your terminal and writes code with you.

In your terminal (Terminal on Mac, Git Bash on Windows):

```bash
npm install -g @anthropic-ai/claude-code
```

This takes 30-60 seconds. **You should see:** A long output ending with something like `added 142 packages in 38s`.

Verify it installed:
```bash
claude --version
```

**You should see:** A version number like `1.x.x` or `claude-code 2.x.x`.

> 🆘 **If you see `command not found` after install:** Close terminal, reopen. Still nothing? Run `npm config get prefix` — the result should be a directory in your PATH. See troubleshooting.

---

## Step 5: Get an Anthropic API Key

Claude Code needs an API key to talk to Anthropic's models.

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up (Google or email, free)
3. Click **Settings** → **API Keys** (left sidebar)
4. Click **Create Key**, name it `onemillion-course`
5. **Copy the key NOW** — it starts with `sk-ant-` — you won't see it again

Now tell Claude Code about it. In your terminal:

```bash
claude
```

The first time you run `claude`, it asks for your API key. Paste it.

> 💰 **Cost reality:** You'll spend $5-15 in API credits over the 18 days. Anthropic gives you $5 free to start. Add $20 to your account and you'll have plenty. Full breakdown: [cost-transparency.md](./cost-transparency.md).

> 📖 **Detailed key setup with screenshots:** [getting-your-api-key.md](./getting-your-api-key.md).

---

## Step 6: Sign Up For GitHub, Supabase, Vercel

You won't use these today. You'll use them starting Day 4. But signing up takes 5 minutes total and gets it out of the way.

| Service | What it does | Sign up at |
|---------|-------------|-----------|
| **GitHub** | Stores your code, deploys to Vercel | [github.com/signup](https://github.com/signup) |
| **Supabase** | Database + authentication for your app | [supabase.com](https://supabase.com) (use "Continue with GitHub") |
| **Vercel** | Hosts your app on the internet | [vercel.com/signup](https://vercel.com/signup) (use "Continue with GitHub") |

> 💡 **Pick a GitHub username you'll be proud of.** It becomes your builder identity. `your-real-name` not `coolguy420`.

All three have **free tiers** that cover the full 18-day course with room to spare.

---

## Step 7: Verify Everything Works

In your terminal, run this verification sequence:

```bash
node -v          # should show v20.x or higher
git --version    # should show git version 2.x
claude --version # should show a Claude Code version
```

If all three show versions, you're done.

Now create a folder for your project:

```bash
mkdir my-onemillion-build
cd my-onemillion-build
claude
```

Once Claude Code starts, type:

```
Hello! Are you ready to help me build something?
```

If you get a response, you're set. **Setup is complete.**

---

## Codespaces Fallback (Last Resort)

> ⚠️ **This is a real last resort.** Local install is the magic — it gives you skills that work forever, on any machine. Try local for at least 30 minutes before switching. Many people who started in Codespaces moved to local once they had confidence.

If local install genuinely won't work for you:

1. Sign in to [github.com](https://github.com) (do Step 6 first)
2. Go to [github.com/codespaces](https://github.com/codespaces)
3. Click **New codespace** → pick **Blank**
4. Wait 60 seconds for it to start
5. In the Codespace terminal, run Step 4 (`npm install -g @anthropic-ai/claude-code`)
6. Add your API key as a Codespace secret: Settings → Codespaces → Secrets → add `ANTHROPIC_API_KEY`

Free tier: 60 hours/month, more than enough for the course.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `command not found: node` (Mac) | Close terminal, reopen. If still broken: `brew install node` (install Homebrew first if needed: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`) |
| `node is not recognized` (Windows) | Restart your computer. The Node installer needs a reboot to update PATH on some Windows systems. |
| `EACCES: permission denied` on `npm install -g` | Mac: prefix the command with `sudo` (`sudo npm install -g @anthropic-ai/claude-code`). Windows: run PowerShell/Git Bash as Administrator. |
| `claude: command not found` after install | The npm global bin isn't in your PATH. Run `npm config get prefix` — add `/bin` (Mac) or `\bin` (Windows) to your PATH. Or: restart terminal. |
| API key not accepted | Make sure you copied the FULL key (starts with `sk-ant-`, ~100 characters). No quotes around it. Check Anthropic console — has the key been deleted or rate-limited? |
| `xcode-select: command not found` (Mac) | You're on a really old Mac. Update to macOS 12+ or use Codespaces fallback. |
| Vercel/Supabase signup hangs | Some corporate networks block these. Try from your phone hotspot. |

---

## What's Next

You're set up. Now you build.

→ **[Day 1: Vision + Mental Map](./week-1-foundation/day-01-vision/learn.md)** — your first day starts here.

Or read the foundation:
- [The Manifesto](./MANIFESTO.md) — why this exists
- [How verification works](./verify/README.md) — how you earn Builder #N
- [Cost transparency](./cost-transparency.md) — what you'll actually spend
