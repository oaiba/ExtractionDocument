---
title: "Documentation Standards"
type: docs
weight: 2
---

## 📝 Documentation Standards for AI Agents

These rules govern how AI agents should write and format GDD documentation, technical docs, and inline comments across the project.

---

### 📋 General Rules

| Rule | Description |
|:-----|:------------|
| **Language** | All documentation must be in **English** (U.S. spelling) |
| **Format** | All documents use **Markdown** (`.md` files) |
| **Tone** | Professional, concise, technical. No fluff or filler |
| **Audience** | Assume the reader is a game developer with UE5 experience |
| **Tense** | Use present tense for describing systems, past tense for changelogs |

---

### 📁 File Structure

#### Frontmatter (Required)

Every documentation `.md` file must have YAML frontmatter:

```yaml
---
title: "Document Title"
type: docs
weight: 1        # Controls sort order in navigation
---
```

#### Document Architecture

```markdown
---
title: "System Name"
type: docs
weight: N
---

## Overview
Brief description of what this system does and why it exists.

## Core Concepts
Key terminology, design pillars, and fundamental principles.

## Features
### Feature A
Detailed description, parameters, rules.

### Feature B
...

## Technical Notes
Implementation details, data structures, enums.

## Reference
Links to related documents, image placeholders, inspiration games.
```

---

### 🖼️ Image Placeholders

When a visual reference is needed but not yet available, use this exact format:

```html
<!-- 📸 IMAGE PLACEHOLDER: [Description of what the image should show] -->
```

**Examples:**

```html
<!-- 📸 IMAGE PLACEHOLDER: Wireframe of the inventory grid UI with item dragging -->
<!-- 📸 IMAGE PLACEHOLDER: Flowchart showing matchmaking queue logic -->
<!-- 📸 IMAGE PLACEHOLDER: Screenshot reference from Escape from Tarkov's stash system -->
```

**Rules:**
- One placeholder per distinct visual concept
- Be specific about what should be shown
- Place near the text the image supports
- Prefix with the camera emoji `📸` for easy searching

---

### 📊 Tables

Use tables for structured data (stats, comparisons, enums):

```markdown
| Item | Type | Rarity | Weight |
|:-----|:-----|:-------|:-------|
| AK-47 | Assault Rifle | Rare | 3.5 kg |
| M4A1 | Assault Rifle | Uncommon | 3.2 kg |
```

**Table rules:**
- Left-align text columns (`:---`)
- Right-align numbers (`:---:` or `---:`)
- Always include a header row
- Keep columns concise

---

### 📐 ASCII Wireframes

For UI mockups within documentation, use ASCII art:

```
┌──────────────────────────────────────────┐
│  SCREEN TITLE                    [✕]     │
├──────────────────────────────────────────┤
│                                          │
│  Content area                            │
│                                          │
│  [Button A]  [Button B]  [Button C]      │
└──────────────────────────────────────────┘
```

**Rules:**
- Use Unicode box-drawing characters (`┌ ┐ └ ┘ ├ ┤ │ ─ ┬ ┴ ┼`)
- Enclose in Markdown code blocks (\`\`\`)
- Label interactive elements with `[brackets]`
- Keep width ≤ 70 characters for readability

---

### 🏷️ Section Emojis

Use consistent emojis for section headers:

| Emoji | Usage |
|:------|:------|
| 📋 | Overview, Summary |
| 🎯 | Goals, Objectives |
| ⚙️ | Configuration, Settings |
| 🔧 | Technical, Implementation |
| 🎮 | Gameplay, Mechanics |
| 🤖 | AI, Automation |
| 👥 | Social, Multiplayer |
| 🎨 | Art, Visual, UI |
| 🔊 | Audio, Sound |
| 📊 | Data, Analytics, Stats |
| ⚖️ | Balance, Economy |
| 🗺️ | Maps, World |
| 📚 | Reference, Links |
| ⚠️ | Warnings, Caution |
| 💡 | Tips, Notes |

---

### 📝 Hugo/Hextra Callouts

When using the Hugo documentation framework, use shortcode callouts:

```markdown
{{< callout type="info" >}}
Informational note for the reader.
{{< /callout >}}

{{< callout type="warning" >}}
Important warning about a constraint or risk.
{{< /callout >}}
```

Available types: `info`, `warning`, `error`

---

### 🔗 Cross-References

Link to other documents using relative paths:

```markdown
See [Inventory System](../Systems/InventorySystem.md) for item data structures.
Refer to [Coding Standards](../../GDD_Technical/CodingStandards.md) for naming rules.
```

**Rules:**
- Always use relative paths (never absolute)
- Link text should be descriptive (not "click here")
- Verify link targets exist before referencing

---

### 📅 Changelog Format

When updating documents, add to the changelog table at the bottom:

```markdown
## 📅 Update Log

| Date       | Section    | Changes                          | Updated By |
| ---------- | ---------- | -------------------------------- | ---------- |
| 2026-02-13 | Karma      | Added karma tier consequences    | Agent      |
| 2026-02-12 | VOIP       | Added spatial audio details      | Agent      |
```

---

### 🚫 Anti-Patterns

| Don't Do This | Do This Instead |
|:--------------|:----------------|
| Write in Vietnamese without being asked | Always write in English |
| Use vague headers like "More Info" | Use specific, searchable headers |
| Write walls of text | Use tables, lists, and headers |
| Duplicate content across documents | Cross-reference with links |
| Add placeholder text like "TBD" without context | Add TODO with priority: `TODO(P2): Define loot tables` |
| Use first person ("I think...") | Use third person or imperative |
