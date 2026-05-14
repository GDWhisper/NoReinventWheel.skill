# Fork-It.skill

## Find it. Fork it. Make it yours.

[🇨🇳 简体中文](./README_zh.md)

---

## 📋 Table of Contents

- [💡 Core Philosophy](#-core-philosophy)
- [🎯 What is this?](#-what-is-this)
- [🚀 Quick Start](#-quick-start)
- [📖 Usage](#-usage)
- [🤖 How It Works](#-how-it-works)
- [📦 Package Structure](#-package-structure)
- [🔧 Tech Stack](#-tech-stack)
- [🌟 Why Fork-It?](#-why-fork-it)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 💡 Core Philosophy

> [!IMPORTANT]
> Every great project starts somewhere. Why start from zero when you can start from 80%?

Got an idea? Before you type a single line of code, search GitHub first. There's probably a project that already does a big chunk of what you want. **Fork it.** Now it's yours. Tear it apart, reshape it, inject your own ideas — no PRs, no waiting, no asking permission. That's the beauty of open source.

You're not "reinventing the wheel." You're standing on it to reach higher.

---

## 🎯 What is this?

Fork-It is an **AI Assistant Skill** that helps you discover the best open-source starting points on GitHub — projects you can fork then customize into your own vision.

### What It Does

| Step | Description |
|------|-------------|
| 🔍 **Search** | Finds the most relevant open-source projects for your idea |
| 📊 **Analyze** | Checks activity, community health, and how close the match is |
| 🚀 **Fork & Go** | Points you to the best fork-worthy candidates, no strings attached |

---

## 🚀 Quick Start

### Installation

Download the latest skill package from [Release](https://github.com/GDWhisper/Fork-It.skill/releases):

| Version | File |
|---------|------|
| 🇨🇳 Chinese | `Fork-It_zh.skill` |
| 🇺🇸 English | `Fork-It_en.skill` |

Extract and place the `fork-it` folder into the Claude Skills directory:

```bash
# Windows
C:\Users\<YourUsername>\.claude\skills\fork-it

# macOS/Linux
~/.claude/skills/fork-it
```

### Configure GitHub Token (Recommended)

> [!TIP]
> A personal access token gives you 5,000 requests/hour instead of 60:

```bash
export GITHUB_TOKEN="ghp_your_token_here"
```

| Rate Limit | Requests/hour |
|------------|---------------|
| ⬛ Unauthenticated | 60 |
| ✅ Authenticated | 5,000 |

---

## 📖 Usage

### How to Trigger

Just talk about your idea in Claude. Fork-It picks up on it naturally:

- "I want to build a..."
- "I'm thinking of making..."
- "Has anyone built something like..."
- Or invoke directly: `/fork-it`

### Example

> **Input:**
> ```
> I want to build a Windows cache auto-cleanup tool
> ```

> **Output:**
> ```
> Here are some solid starting points you can fork and make your own:
>
> 🐙 Results
>
> | Project | Stars | Language | What It Gives You |
> |---------|-------|----------|-------------------|
> | BleachBit | 4.7k | Python | Full-featured cross-platform cleaner, fork it and add your own rules |
> | Winapp2 | 905 | VB.NET | Rich cleaning rules database, fork it as your rule engine |
> | WindowsCleanerUtility | 105 | Batch | Minimal script, fork it if you want a lightweight starting point |
>
> 💡 BleachBit gives you the most complete foundation. Fork it, strip what you
> don't need, and build your own cleaner on top.
> ```

---

## 🤖 How It Works

### When Fork-It Chimes In

When you're forming a new project idea — not when you're fixing bugs, learning, or asking about specific functions.

**Good candidates for Fork-It:**
- "I want to build a chat app..."
- "I want to create a markdown editor..."
- "I want to make a cron job scheduler..."

**Fork-It stays quiet when:**
- You're debugging existing code
- You're learning how something works
- You're asking about a specific algorithm or regex
- You're modifying an existing project

### Workflow

```
graph TD
    A[You Have an Idea] --> B{Fork-It Checks}
    B -->|New Project Idea| C[Search GitHub]
    B -->|Debug / Learn / Tweak| D[Carry On]
    C --> E[Find Best Matches]
    E --> F{How Close Is the Match?}
    F -->|Great Match 🎯| G[Fork It & Customize]
    F -->|Partial Match 🔧| H[Fork It & Extend]
    F -->|Reference Only 📝| I[Study It, Then Build]
    F -->|Nothing Fits ✨| J[Build Fresh — Go For It]
```

### Decision Guide

| Match | Path | What This Means |
|-------|------|-----------------|
| 🎯 Great | **Fork & Customize** | The project does most of what you need. Fork it, tweak it, ship it. |
| 🔧 Partial | **Fork & Extend** | Core is solid but missing your feature. Fork it and add your piece. |
| 📝 Reference | **Learn, Then Build** | Different enough that forking isn't the shortcut. Study the approach. |
| ✨ None | **Build Fresh** | You're doing something new. Go build it — and consider open-sourcing it! |

### Output Format

Scripts return a unified JSON structure:

```json
{
  "lang": "en",
  "status": "ok",
  "query": "pomodoro timer",
  "total_count": 1234,
  "returned_count": 10,
  "items": [
    {
      "rank": 1,
      "full_name": "user/repo",
      "description": "A pomodoro timer app",
      "url": "https://github.com/user/repo",
      "stars": 12300,
      "forks": 1200,
      "language": "TypeScript",
      "pushed_days_ago": 3,
      "created_at": "2024-01-01",
      "topics": ["productivity", "timer"],
      "license": "MIT"
    }
  ]
}
```

**AI Display Rules:**

| Field | Rule |
|-------|------|
| `lang: "en"` | AI translates to user's language before displaying |
| `pushed_days_ago: 3` | AI converts to "3 days ago" or localized format |
| `stars: 12300` | AI formats as "12.3k" |
| `status: "error"` | AI generates a friendly error message from `code` and `message` |

---

## 📦 Package Structure

```
Fork-It/
├── Fork-It_zh/                # Chinese version
│   └── SKILL.md              # Skill definition (Chinese)
├── Fork-It_en/                # English version
│   └── SKILL.md              # Skill definition (English)
├── scripts/                  # Shared scripts
│   ├── github-search.mjs
│   └── repo-detail.mjs
├── _meta.json                # Project metadata
├── README.md                 # English documentation
├── README_zh.md             # Chinese documentation
└── release_script.py         # Release script
```

---

## 🔧 Tech Stack

| Component | Technology |
|-----------|------------|
| Language | JavaScript (ES Modules) |
| API | GitHub Search API v3, GitHub REST API |
| Runtime | Node.js |

---

## 🌟 Why Fork-It?

| Benefit | Description |
|---------|-------------|
| 🏃 **Jump Start** | Start from a working codebase instead of a blank file |
| 🎨 **Full Creative Control** | Fork it and it's yours — no PRs, no waiting, no gatekeepers |
| 👀 **Learn by Reading** | Even if you don't fork, studying real projects teaches you fast |
| ⚡ **Ship Faster** | Spend time on YOUR ideas, not on boilerplate someone already wrote |

---

## 🤝 Contributing

We welcome contributions of all kinds:

| Area | Description |
|------|-------------|
| 🐛 Bug fixes | Fix issues and improve stability |
| ✨ New features | Add new capabilities |
| 📝 Documentation | Improve docs and examples |
| 🌍 Translation | Enhance bilingual support |

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details

---

<div align="center">

**Made with ❤️ by the Fork-It Team**

⭐ If Fork-It helps you launch faster, give us a star!

</div>
