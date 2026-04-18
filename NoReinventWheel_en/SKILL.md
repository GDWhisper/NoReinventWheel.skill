---
name: no-reinvent-wheel
description: When user have a new development idea, search GitHub first for similar open-source projects. Avoid reinventing the wheel, prioritize reuse and contribution.
metadata:
  openclaw:
    emoji: "🐙"
    category: "research"
    tags: ["github", "opensource", "research", "reuse", "contribution"]
---

# No Reinvent the Wheel 🐙

The AI era has made reinventing the wheel effortless, leading to a flood of duplicate projects. Take a step back and stop wasting your tokens!

## Core Principles

**Whenever you sense the user wants to build something new, proactively intervene and remind them.**

When the user expresses any of these intents, search GitHub first before taking action:

- User says "Help me build..." or "I want to create/develop/write a XXX" (where XXX is a complete application or tool)
- User describes a complete functional requirement requiring multiple code components
- User asks "how to" build a complete project

**If any of the above applies, you MUST trigger the 【no-reinvent-wheel】 flow first:**

**Reminder Template:**
> "Before we start—GitHub may already have mature similar projects. Let me search for you first to save time on building from scratch."

**If any of the following applies, DO NOT trigger (answer normally):**
- User explicitly says "for learning/practice/teaching purposes"
- User is just asking about a function's implementation and parameters
- User is debugging/fixing existing code
- User is asking about regex, specific algorithm logic, or other very granular questions
- User's "write" is modifying existing code, not generating from scratch
- User has already selected a specific open-source project as the foundation

---

## Workflow

### 1. Identify Requirements

When the user expresses any of these intents, automatically trigger a search:

- "Help me build..." or "I want to create/develop a..."
- "Help me develop..." or "I'm going to build a..."
- "Are there any similar projects?"
- "Help me write a..." or "I want to code a..."
- Directly invoke `/no-reinvent-wheel`
- Directly invoke `/wheel`

### 2. Smart Search (Avoid Reinventing the Wheel)

**Always search first, then act!**

```bash
node scripts/github-search.mjs "keyword"
node scripts/github-search.mjs "pomodoro timer" --language javascript --min-stars 500
```

Search repositories by keyword in a specific domain, filter high-star and actively maintained projects, prioritize mature projects that can be directly reused.

### 3. Result Analysis

Evaluate match level for each project:

| Tag | Recommendation | Description |
|-----|----------------|-------------|
| ✅ Full Match | Use directly / Fork | Fork and contribute |
| 🔧 Partial Match | Build on top | Extend the original project |
| 📝 Reference Value | Learning only | Draw inspiration, design differentiated solution |

### 4. Decision Suggestions

- **Highly matching projects found** → Recommend reuse or contribution
- **Partially matching projects found** → Recommend building on top
- **No suitable projects** → Explain gaps, confirm whether to build from scratch

## Strong Trigger Words (Intercept Immediately)

**These words indicate the user explicitly intends to "build a complete thing from scratch":**

### "From scratch / Hand-write / Implement myself" Series (Extremely dangerous signals)
- "Help me write a... **from scratch**"
- "No third-party libraries, **hand-write** a..."
- "I don't want external dependencies, **implement my own**..."
- "No frameworks, **vanilla**..."

### "Project / Module / System" Series (Too large, definitely exists)
- "Help me **create a project** that implements..."
- "Write a complete **module** for..."
- "Design a **system** that can..."
- "Help me build a **backend/website/mini-program**..."

### "I want to / I'm going to" Series (Still in ideation stage, best interception point)
- "I have an idea, I want to build a..."
- "I'm going to develop a..."
- "How can I make a..."

## Scenario Trigger Words (High-Frequency Wheel-Making Areas)

**Trigger when user's instruction contains "code-writing action" + "one of these high-frequency areas":**

- **Auth & Permissions:** "write a" + `login/register/auth/JWT/permission management/OAuth`
- **Data Parsing:** "write a" + `crawler/parser/export Excel/read PDF/parse XML/regex extraction`
- **Infrastructure:** "write a" + `chat room/WebSocket/cron job/queue/logging system`
- **Common Business:** "write a" + `shopping cart/payment API/pagination component/rich text editor/file upload`
- **Algorithm Utils:** "write a" + `calendar widget/countdown/encryption-decryption/image compression`

*Example: "Help me write a JWT auth middleware with token refresh" → matches 【action: write】+【area: JWT auth】 → TRIGGER!*

## Negative Trigger Words (NEVER Trigger!)

**Don't interrupt when user is learning, fixing bugs, or genuinely innovating:**

- **Learning-oriented:** "To learn the principle, show me how to write...", "For teaching purposes, hand-write a..."
- **Extremely specific/custom:** "Write a regex matching `^a[b-c]{2}d$`" (no open-source project can match this specific need)
- **Modifying existing code:** "Help me see why this code is throwing an error", "Optimize this function's performance"
- **Low-level innovation:** "I want to design a new data structure", "Write a faster sorting algorithm than existing ones"
- **Local file search:** "Help me find if there's any... on my computer"

## Script Return Values

Scripts return a unified JSON structure with a `lang` field marking the output language:

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

**AI display rules**:

- `lang: "en"` → AI translates to user's language before displaying
- Date field `pushed_days_ago` → AI converts to "3 days ago" or localized format
- Number field `stars: 12300` → AI formats as "12.3k"
- On error `status: "error"` → AI generates a friendly error message from `code` and `message`

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `query` | Search keyword | Required |
| `--language, -l` | Programming language filter | None |
| `--min-stars` | Minimum stars | 100 |
| `--max-stars` | Maximum stars | No limit |
| `--updated-within` | Updated within N days | 365 |
| `--created-after` | Created after date | None |
| `--sort` | Sort by | stars |
| `--order` | Sort order | desc |
| `--limit, -n` | Result limit | 10 |

## Get Repository Details

```bash
node scripts/repo-detail.mjs "microsoft/autogen"
```

## API Limits

- **Unauthenticated Requests**: 60/hour
- **Authenticated Requests**: 5000/hour

```bash
export GITHUB_TOKEN="ghp_your_token_here"
```

## Data Sources

- GitHub Search API v3
- GitHub REST API

---

*Stop reinventing the wheel. Focus on truly valuable innovation. | NoReinventWheel v1.0*
