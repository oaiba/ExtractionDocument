---
title: "Lore Delivery Systems"
type: docs
weight: 5
---

## Lore Delivery Overview

This document defines **how** narrative content reaches the player. For **what** the story contains, see [Backstory](../Backstory/). For **writing standards**, see [Narrative Design Bible](../Narrative/).

### Lore Channel Taxonomy

Every piece of lore is delivered through exactly one primary channel:

| Channel | Player Effort | Persistence | Replayable | Example |
| :------ | :------------ | :---------- | :--------- | :------ |
| **Environmental Props** | Passive observation | In-world only | Yes (always present) | Skeleton near an exit with packed bags |
| **Audio Logs** | Active interaction | Codex entry on first listen | Yes (replayable from Codex) | Dr. Chen's Lab recordings |
| **Text Documents** | Active reading | Codex entry on first read | Yes (replayable from Codex) | Nexus Corp internal memos |
| **NPC Dialogue** | Quest engagement | Not replayable in-game | No (one-time delivery) | Viktor Koval's quest briefings |
| **Item Descriptions** | Inventory inspection | Persistent when item owned | Yes (inspect item anytime) | Weapon flavor text |
| **Loading Screen Tips** | Passive reading | Rotating pool | Random per session | In-character tips from various factions |
| **Codex Entries** | Menu navigation | Permanently unlocked | Yes (always accessible) | Compiled lore articles |

---

## Audio Log Production

### Overview

Audio logs are the **primary active lore delivery method**. They are 30-60 second recordings found at specific locations throughout the Exclusion Zone, activated by interacting with physical objects (recorders, radios, terminals).

> For placement guidelines and per-map allocation, see [Environmental Narrative](../../World/EnvironmentalNarrative/).

### Voice Acting Tone Per Faction

| Speaker Identity | Recording Quality | Vocal Tone | Background Sounds |
| :--------------- | :---------------- | :--------- | :---------------- |
| Nexus Corporate | Clean, studio quality | Professional, increasingly panicked | Office ambiance, muffled alarms |
| Military | Crackling radio quality | Terse, procedural, breaking under stress | Static, gunfire, radio squelch |
| Factory Workers | Moderate quality handheld recorder | Scared, confused, personal | Industrial noise, dripping, distant explosions |
| Medical Staff | Clear but strained | Clinical shifting to emotional | Beeping monitors, screaming, running footsteps |
| Survivors (post-Collapse) | Poor quality, degraded | Exhausted, resigned, occasionally hopeful | Wind, wildlife, fire crackling |
| Unknown (Prometheus subjects) | Distorted, inhuman processing | Monotone with glitches of human emotion | Electronic interference, low hum |

### Script Structure Template

Every audio log follows this structure:

```
AUDIO LOG SCRIPT
================

Log ID: [MAP-ZONE-###] (e.g., SEC7-LAB-003)
Title: "[Evocative Name]"
Speaker: [Name, former role]
Duration: [30-60 seconds]
Location: [Specific POI, floor, room]
Trigger Object: [What player interacts with — recorder, terminal, phone]
Recording Quality: [Clean / Moderate / Poor / Distorted]

---

SCRIPT:
[Speaker establishes identity — 1 sentence]
[Context — what was happening when they recorded this — 1-2 sentences]
[Core information — the lore this log delivers — 3-5 sentences]
[Emotional beat — fear, anger, sadness, resignation — 1-2 sentences]
[Ending — cut off dramatically OR trail into silence OR conscious sign-off]

---

LORE DELIVERED:
- [Point 1: What does the player learn?]
- [Point 2: What does this connect to?]

QUEST CONNECTION: [Does finding this log affect any quest? Trigger any hidden quest?]
CODEX ENTRY: [Which Codex category does this unlock? What entry title?]
```

### Audio Log Best Practices

**DO:**
- Start with the speaker identifying themselves — helps players immediately contextualize
- Include at least one concrete proper noun (person, place, project name) for lore anchoring
- End logs with ambiguity — leave the player wanting more
- Vary emotional tone across logs in the same location (not every log should be terrified)
- Include environmental sounds that match the recording location

**DON'T:**
- Make logs longer than 60 seconds — players are in danger during playback
- Require players to listen to the full log for quest-critical information — put key data in the first 15 seconds
- Make two logs in the same area sound identical in tone or content
- Expose major plot twists in single audio logs — buildups require multiple logs across locations

---

## Epistolary Framework

### Unreliable Narrators

Inspired by Hunt: Showdown's "Book of Monsters," the game uses **conflicting written accounts** to create mystery:

| Document Source | Reliability | Bias | Example |
| :-------------- | :---------- | :--- | :------ |
| Nexus Corp memos | High factual, low ethical | Corporate spin, minimize blame | "The containment incident was within acceptable parameters" |
| Military reports | High tactical, low context | Need-to-know redactions | "06:00 — Perimeter breach at Sector 7-G. Response team deployed. [REDACTED] casualties" |
| Survivor journals | High emotional, variable factual | Personal experience, rumor, fear | "They say the labs created monsters. I believe them — I saw what came out of there" |
| Underground encoded messages | Variable | Transactional, coded language | "Package delivered. The chef is cooking something new. Stay away from the kitchen" |
| Project Prometheus logs | High scientific accuracy | Clinical detachment, ethical blindness | "Subject 7 demonstrates 340% baseline physical capacity. Neural degradation is within study tolerances" |

### Conflicting Information Design

For each major mystery, plant **at least two contradictory accounts**:

| Mystery | Account A | Account B | Truth |
| :------ | :-------- | :-------- | :---- |
| Cause of Crimson Flu | Nexus memo: "Natural mutation of existing pathogen" | Prometheus log: "Serum batch 7-C showed unexpected mutagenic properties" | Prometheus-related, but exact mechanism unknown even to researchers |
| Subject 7's escape | Military: "Security failure at 03:00" | Worker log: "Someone opened the doors from the outside" | Deliberate release by a Nexus insider (Season 3 reveal) |
| Dr. Chen's fate | Lab record: "Dr. Chen — deceased, containment failure" | Audio log: Chen's voice, post-Collapse, speaking coherently | Chen is alive as Subject 12 — self-administered Prometheus serum |

### Physical Document Types

| Type | Visual Style | Where Found | Content |
| :--- | :----------- | :---------- | :------ |
| **Corporate Memo** | Clean white paper, Nexus letterhead, partially burned | Offices, labs, executive areas | Business decisions, coverups, financial records |
| **Military Orders** | Green paper, stamped CLASSIFIED, some words blacked out | Military areas, checkpoints | Tactical decisions, chain-of-command communications |
| **Personal Journal** | Crumpled notebook paper, handwritten, stained | Residential areas, camps, random | Personal stories, rumors, emotional accounts |
| **Medical Records** | Clinical forms, partially filled, blood-stained | Hospitals, labs, medical tents | Patient records, experiment results, autopsy notes |
| **Graffiti** | Spray-painted on walls, scrawled in marker | Public spaces, tunnels, walls | Warnings, faction messages, survivor pleas |
| **Coded Messages** | Folded paper, cipher wheel nearby, invisible ink hints | Dead drops, hidden compartments | Underground Network communications |

---

## Collectible Codex System

### Overview

The Codex is a persistent, menu-accessible database that compiles all lore the player has discovered:

<!-- REF_IMAGE: Codex UI mockup — split-panel layout with category tree on left, content panel on right, completion percentage in header, map filter dropdown -->

### Codex Categories

| Category | Content | Unlock Method |
| :------- | :------ | :------------ |
| **History** | Timeline events, Pre-Collapse era, The Collapse | Audio logs, documents, main story quests |
| **Factions** | Faction profiles, NPC bios, relationship history | Meeting NPCs, completing faction quests, discovering documents |
| **Project Prometheus** | Research phases, subject profiles, facility maps | Lab exploration, specific quest chains, hidden documents |
| **Maps & Locations** | Zone descriptions, POI histories, hidden areas | Visiting locations, completing exploration objectives |
| **People** | Key historical figures, missing persons, deceased | Audio logs, quest completions, environmental discovery |
| **Science & Tech** | Nexus technology, military equipment, Crimson Flu data | Document collection, tech-faction quests |
| **The Broker's Files** | Encrypted entries that decode as player progresses | Main story progression, high Underground reputation |

### Completion Rewards

| Completion % | Category | Reward |
| :-----------: | :------- | :----- |
| 25% | Any category | Codex Badge (cosmetic) |
| 50% | Any category | Unique loading screen tip from that category's perspective |
| 75% | Any category | Exclusive cosmetic item themed to the category |
| 100% | Any category | Legendary title + hidden quest related to the category |
| 100% | ALL categories | Ultimate title: "Archivist" + unique operator skin |

### Codex Entry Template

```
CODEX ENTRY
===========

Entry ID: [CAT-###]
Category: [History / Factions / Prometheus / Maps / People / Tech / Broker]
Title: "[Entry Title]"
Unlock Method: [How does the player unlock this entry?]

---

ENTRY TEXT:
[300-500 words of in-universe documentation]
[Written from the perspective of a neutral historian or data compiler]
[Include cross-references to related entries: "See also: [Entry Title]"]

---

METADATA:
Related Audio Logs: [Log IDs]
Related Quests: [Quest IDs]
Related NPCs: [NPC names]
Map Location: [Where was this lore found?]
```

---

## Item Description Lore

### Overview

Every item in the game has two description lines:

1. **Functional**: What it does mechanically (damage, weight, capacity)
2. **Flavor**: One sentence of world-building context

### Flavor Text Guidelines

| Item Category | Tone | Example |
| :------------ | :--- | :------ |
| Weapons (common) | Practical, factual | "Mass-produced before The Collapse. Still fires. That's all that matters." |
| Weapons (rare) | Historical, specific | "Custom-built by Yuri from salvaged Nexus defense parts. Serial number filed off." |
| Weapons (legendary) | Ominous, unique | "Recovered from Subject 19's containment cell. The grip is warm to the touch." |
| Armor | Protective, worn | "Standard-issue Peacekeeper vest. The bloodstains aren't yours." |
| Medical | Clinical, urgent | "Auto-injector loaded with adrenaline. Don't read the expiration date." |
| Food/Water | Scarce, precious | "Canned peaches, 2028 vintage. Worth killing for in the Zone." |
| Key/Access | Mysterious, anticipatory | "Card reads 'Lab Gamma — Level 3.' Whatever's behind that door, they didn't want you finding it." |
| Quest items | Lore-rich, contextual | "Dr. Chen's USB drive. The encryption will take days to crack. The data inside might crack everything else." |
| Cosmetics | Character, identity | "Hand-stitched from old military canvas. Somewhere between uniform and uniform protest." |

### Writing Rules for Item Descriptions

- Maximum 2 sentences for flavor text
- Must contain at least one world-building reference (faction, event, person, location)
- Never break the fourth wall
- Prioritize personality over information
- Legendary items should hint at their origin story without fully explaining it

---

## Loading Screen Lore

### Overview

Loading screen tips are **in-character statements** attributed to specific factions or individuals. They serve as passive lore delivery and atmosphere reinforcement.

### Format

```
"[Statement]"
— [Attribution: faction name, NPC name, or "Unknown Contractor"]
```

### Category Distribution

| Category | Percentage | Purpose |
| :------- | :--------: | :------ |
| Gameplay tips (in-character) | 40% | Teach mechanics through world voice |
| Lore fragments | 30% | Deliver small lore bites |
| Faction philosophy | 20% | Reinforce faction identities |
| Dark humor / atmosphere | 10% | Tone and personality |

### Examples

**Gameplay tips (in-character):**
- *"Heavy bags make heavy noise. The Zone punishes greed."* — Salvage Corps field manual
- *"If you hear a click and nothing happens, run. The second click won't be as quiet."* — Underground survival guide

**Lore fragments:**
- *"Day 1,247. The radio still plays Nexus Corp's automated welcome message. Nobody's listening."* — Recovered journal
- *"The reactor hasn't been serviced in five years. It shouldn't still be running. That's what worries me."* — Engineer's note

**Faction philosophy:**
- *"Every Contractor starts as a stranger. Every stranger is a threat until proven otherwise."* — Peacekeeper orientation manual
- *"Data is the only currency that doesn't depreciate. Protect your data."* — Tech Syndicate internal memo

**Dark humor:**
- *"Tip: If you find a room full of dead bodies and one open door, don't use that door."* — Unknown Contractor
- *"The expiration date on the canned food is a suggestion. The expiration date on the medicine is a prayer."* — Dr. Wells

---

## Lore Gating

### Gating by Player Level

| Player Level | Lore Access | Design Purpose |
| :----------- | :---------- | :------------- |
| 1-10 | Basic world context only — The Collapse happened, factions exist, Zone is dangerous | Don't overwhelm new players |
| 10-20 | Faction depths, early Prometheus hints, regional history details | Reward continued play with deeper context |
| 20-30 | Major revelations — Prometheus subjects, corporate culpability, military involvement | Narrative payoffs for invested players |
| 30-40 | The Broker's secrets, endgame lore, cross-faction hidden truths | Reserved for veterans |
| 40+ | Meta-narrative content — unreliable narrator reveals, "true history" contradictions | Deep engagement rewards |

### Gating by Season

| Season | New Lore Available | Design Purpose |
| :----- | :----------------- | :------------- |
| Launch | Foundation — world state, factions, basic history | Establish the world |
| Season 2 | Prometheus details, The Collapse causes, faction conflicts | Deepen the mystery |
| Season 3 | Major truth reveals, Firebase Delta lore, Director Park's past | Climactic revelations |
| Season 4+ | Broker identity, cure plotline, external threats | Evolving world |

### Anti-Spoiler Rules

- **Main story lore is never fully dataminable** — final quest dialogue is server-side until the quest becomes available
- **Seasonal lore is drip-fed** — new audio logs and documents appear as the season progresses, not all at launch
- **Community discussion is encouraged** — deliberately create moments where players need to share information to piece together the full picture (e.g., different logs found in different raids)
