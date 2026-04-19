# NoReinventWheel.skill

## Stop reinventing the wheel — Focus on truly valuable innovation

[🇨🇳 简体中文](./README_zh.md)

---

## 📋 Table of Contents

- [💡 Core Philosophy](#-core-philosophy)
- [🎯 What is this?](#-what-is-this)
- [🚀 Quick Start](#-quick-start)
- [📖 Usage](#-usage)
- [🤖 AI Integration](#-ai-integration--how-it-works)
- [📦 Package Structure](#-package-structure)
- [🔧 Tech Stack](#-tech-stack)
- [🌟 Why Choose NoReinventWheel?](#-why-choose-noreinventwheel)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 💡 Core Philosophy

> [!IMPORTANT]
> The AI era has made reinventing the wheel effortless, leading to a flood of duplicate projects. Take a step back and stop wasting your tokens!

Before acting on a flash of inspiration, check GitHub first to see if an open-source project already aligns with your idea. Instead of creating copycats, we should contribute to and improve existing projects—unless your design philosophy is fundamentally different.

---

## 🎯 What is this?

NoReinventWheel is an **AI Assistant Skill** designed to help developers search for mature open-source solutions on GitHub before starting new projects, avoiding redundant work and improving development efficiency.

### Key Features

| Feature | Description |
|---------|-------------|
| 🔍 **Smart Search** | Automatically search for related open-source projects on GitHub |
| 📊 **Result Analysis** | Evaluate project match level, activity, and community support |
| 💡 **Decision Guidance** | Recommend the best path: reuse, modify, or build from scratch |
| 🌐 **Bilingual Support** | Complete documentation and output in both Chinese and English |

---

## 🚀 Quick Start

### Installation

Download the latest skill package from [Release](https://github.com/GDWhisper/NoReinventWheel.skill/releases):

| Version | File |
|---------|------|
| 🇨🇳 Chinese | `NoReinventWheel_zh.skill` |
| 🇺🇸 English | `NoReinventWheel_en.skill` |

Extract the archive and place the `no-reinvent-wheel` folder into the Claude Skills directory:

```bash
# Windows
C:\Users\<YourUsername>\.claude\skills\no-reinvent-wheel

# macOS/Linux
~/.claude/skills/no-reinvent-wheel
```

### Configure GitHub Token (Recommended)

> [!TIP]
> To increase API rate limits, configure a personal access token:

```bash
export GITHUB_TOKEN="ghp_your_token_here"
```

| Rate Limit | Requests/hour |
|------------|---------------|
| ⬛ Unauthenticated | 60 |
| ✅ Authenticated | 5,000 |

---

## 📖 Usage

### Basic Usage

Simply express your development intent in Claude to trigger the search:

- "I want to develop..."
- "I want to build a... project"
- "Any similar projects?"
- Directly invoke `/no-reinvent-wheel` or `/wheel`

### Usage Example

> **Input:**
> ```
> I want to develop a Windows cache auto-cleanup tool
> ```

> **Output:**
> ```
> There are already mature similar projects on GitHub. Here's the research report:
>
> 🐙 Research Results
>
> | Project | Stars | Language | Positioning |
> |---------|-------|----------|-------------|
> | BleachBit | 4.7k | Python | Mature open-source software, cross-platform for Windows/Linux, most comprehensive features |
> | Winapp2 | 905 | VB.NET | Cleaning rules database, provides extension definitions for CCleaner/BleachBit |
> | WindowsCleanerUtility | 105 | Batch | Minimalist batch script for cleaning temporary files |
>
> 💡 My Judgment
>
> BleachBit is already a mature open-source benchmark. If you want to build a general-purpose
> "Windows cache cleanup tool", it basically covers all mainstream scenarios.
> ```

---

## 🤖 AI Integration & How It Works

### Trigger Scenarios

Automatically trigger search when users express these intents:

- "I want to build..."
- "I'm developing..."
- "Any similar projects?"
- Directly invoke `/no-reinvent-wheel` or `/wheel`

### Strong Trigger Words (Intercept Immediately)

<details>
<summary>These words indicate the user explicitly intends to "build a complete thing from scratch":</summary>

#### "From scratch / Hand-write / Implement myself" Series
- "Help me write a... **from scratch**"
- "No third-party libraries, **hand-write** a..."
- "I don't want external dependencies, **implement my own**..."

#### "Project / Module / System" Series
- "Help me **create a project** that implements..."
- "Write a complete **module** for..."
- "Design a **system** that can..."

#### "I want to / I'm going to" Series
- "I have an idea, I want to build a..."
- "I'm going to develop a..."
</details>

### High-Frequency Wheel-Making Areas

Trigger when user's instruction contains "code-writing action" + "one of these high-frequency areas":

| Category | Keywords |
|----------|----------|
| **Auth & Permissions** | login/register/auth/JWT/permission/OAuth |
| **Data Parsing** | crawler/parser/export Excel/read PDF/parse XML |
| **Infrastructure** | chat room/WebSocket/cron job/queue/logging system |
| **Common Business** | shopping cart/payment API/pagination component/rich text editor/file upload |
| **Algorithm Utils** | calendar/countdown/encryption/image compression |

### When NOT to Trigger

Do NOT trigger (answer normally) in these cases:

- ✅ User explicitly says "for learning/teaching purposes"
- ✅ User is just asking about a function's usage and parameters
- ✅ User is debugging/fixing a Bug in existing code
- ✅ User is asking about regex, specific algorithm logic, or other very granular questions
- ✅ User's "write" is modifying existing code, not generating from scratch

### Workflow

```
graph TD
    A[User Request] --> B{Identify Intent}
    B -->|Complete Functionality Needed| C[Trigger Search]
    B -->|Learning/Debugging/Granular| D[Answer Directly]
    C --> E[Execute GitHub Search]
    E --> F[Analyze Search Results]
    F --> G{Match Level Assessment}
    G -->|✅ Full Match| H[Recommend Use/Fork]
    G -->|🔧 Partial Match| I[Recommend Build on Top]
    G -->|📝 Reference Value| J[Learning Reference Only]
    G -->|❌ No Suitable Projects| K[Confirm Build from Scratch]
    H --> L[End]
    I --> L
    J --> L
    K --> L
```

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
NoReinventWheel/
├── NoReinventWheel_zh/       # Chinese version
│   └── SKILL.md              # Skill definition (Chinese)
├── NoReinventWheel_en/       # English version
│   └── SKILL.md              # Skill definition (English)
├── scripts/                  # Shared scripts
│   ├── github-search.mjs
│   └── repo-detail.mjs
├── _meta.json                # Project metadata
├── README.md                 # Chinese documentation
├── README_EN.md              # English documentation
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

## 🌟 Why Choose NoReinventWheel?

### Value for Developers

| Benefit | Description |
|---------|-------------|
| ⏱️ **Save Time** | Avoid reinventing the wheel, quickly find mature solutions |
| ✅ **Improve Quality** | Use stable projects validated by the community |
| 🤝 **Promote Collaboration** | Encourage contribution over copying, drive open-source ecosystem growth |
| 💰 **Reduce Waste** | Save AI tokens and development resources |

### Contribution to Open Source Community

- 🔄 Reduce the proliferation of homogeneous projects
- 🤝 Encourage developers to participate in existing projects
- 📈 Increase visibility of high-quality projects
- 💪 Build a healthier open-source ecosystem

---

## 🤝 Contributing

We welcome contributions of all kinds!

### Contribution Areas

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

**Made with ❤️ by the NoReinventWheel Team**

⭐ If this project helps you, please give us a star!

</div>
