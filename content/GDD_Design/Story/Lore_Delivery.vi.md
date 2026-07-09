---
title: "Lore Delivery hệ thống"
type: docs
weight: 5
---

### Lore Delivery Overview

Tài liệu này định nghĩa **how** narrative content reaches the người chơi. For **what** the story contains, Xem [Backstory](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Backstory/README.md). For **writing standards**, Xem [Narrative Design Bible](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Narrative/README.md).

#### Lore Channel Taxonomy

Every piece of lore is delivered thông qua exactly one primary channel:

| Channel                 | người chơi Effort        | Persistence                 | Replayable                  | Example                                 |
| ----------------------- | -------------------- | --------------------------- | --------------------------- | --------------------------------------- |
| **Environmental Props** | Passive observation  | In-world only               | Yes (always present)        | Skeleton near an exit với packed bags  |
| **Audio Logs**          | Active interaction   | Codex entry on first listen | Yes (replayable from Codex) | Dr. Chen's Lab recordings               |
| **Text Documents**      | Active reading       | Codex entry on first read   | Yes (replayable from Codex) | Nexus Corp internal memos               |
| **NPC Dialogue**        | Quest engagement     | Not replayable in-game      | No (one-thời gian delivery)      | Viktor Koval's quest briefings          |
| **Item Descriptions**   | Inventory inspection | Persistent khi item owned  | Yes (kiểm tra item anytime)  | vũ khí flavor text                      |
| **loading màn hình Tips** | Passive reading      | Rotating pool               | Random per session          | In-nhân vật tips from various factions |
| **Codex Entries**       | Menu navigation      | Permanently unlocked        | Yes (always accessible)     | Compiled lore articles                  |

***

### Audio Log Production

#### Tổng Quan

Audio logs are the **primary active lore delivery method**. They are 30-60 second recordings found at cụ thể locations throughout the Exclusion Zone, activated by interacting với physical objects (recorders, radios, terminals).

> For placement guidelines và per-map allocation, Xem [Environmental Narrative](https://github.com/oaiba/ExtractionDocument/blob/main/content/World/EnvironmentalNarrative/README.md).

#### Voice Acting Tone Per Faction

| Speaker Identity              | Recording Quality                  | Vocal Tone                                | Background Sounds                              |
| ----------------------------- | ---------------------------------- | ----------------------------------------- | ---------------------------------------------- |
| Nexus Corporate               | Clean, studio quality              | Professional, increasingly panicked       | Office ambiance, muffled alarms                |
| Military                      | Crackling radio quality            | Terse, procedural, breaking under stress  | Static, gunfire, radio squelch                 |
| Factory Workers               | Moderate quality handheld recorder | Scared, confused, personal                | Industrial noise, dripping, distant explosions |
| Medical Staff                 | rõ nhưng strained                 | Clinical shifting to cảm xúc            | Beeping monitors, screaming, running footsteps |
| Survivors (post-Collapse)     | Poor quality, degraded             | Exhausted, resigned, occasionally hopeful | Wind, wildlife, fire crackling                 |
| Unknown (Prometheus subjects) | Distorted, inhuman processing      | Monotone với glitches of human emotion   | Electronic interference, low hum               |

#### Script Structure Template

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

#### Audio Log Best Practices

**DO:**

* Start với the speaker identifying themselves — giúp người chơi immediately contextualize
* Include at least one concrete proper noun (person, place, project name) for lore anchoring
* End logs với mơ hồ — leave the người chơi wanting more
* Vary cảm xúc tone across logs in the same location (not every log nên được terrified)
* Include environmental sounds that match the recording location

**DON'T:**

* Make logs longer than 60 seconds — người chơi are in danger trong khi playback
* Require người chơi to listen to the full log for quest-critical information — put chính data in the first 15 seconds
* Make two logs in the same area sound identical in tone hoặc content
* Expose major plot twists in single audio logs — buildups require multiple logs across locations

***

### Epistolary Framework

#### Unreliable Narrators

Inspired by Hunt: Showdown's "Book of Monsters," the game uses **conflicting written accounts** to tạo mystery:

| tài liệu source              | Reliability                      | Bias                                   | Example                                                                                                 |
| ---------------------------- | -------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Nexus Corp memos             | High factual, low ethical        | Corporate spin, minimize blame         | "The containment incident was within acceptable parameters"                                             |
| Military reports             | High tactical, low context       | Need-to-know redactions                | "06:00 — Perimeter breach at Sector 7-G. Response team deployed. \[REDACTED] casualties"                |
| Survivor journals            | High cảm xúc, variable factual | Personal trải nghiệm, rumor, fear       | "They say the labs created monsters. I believe them — I saw what came out of there"                     |
| Underground encoded messages | Variable                         | Transactional, coded language          | "Package delivered. The chef is cooking something new. Stay away from the kitchen"                      |
| Project Prometheus logs      | High scientific accuracy         | Clinical detachment, ethical blindness | "Subject 7 demonstrates 340% baseline physical capacity. Neural degradation is within study tolerances" |

#### Conflicting Information Design

For each major mystery, plant **at least two contradictory accounts**:

| Mystery              | Account A                                              | Account B                                                                | Truth                                                               |
| -------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Cause of Crimson Flu | Nexus memo: "Natural mutation of existing pathogen"    | Prometheus log: "Serum batch 7-C showed unexpected mutagenic properties" | Prometheus-related, nhưng exact mechanism unknown even to researchers |
| Subject 7's escape   | Military: "Security failure at 03:00"                  | Worker log: "Someone opened the doors from the outside"                  | Deliberate release by a Nexus insider (Season 3 reveal)             |
| Dr. Chen's fate      | Lab record: "Dr. Chen — deceased, containment failure" | Audio log: Chen's voice, post-Collapse, speaking coherently              | Chen is alive as Subject 12 — self-administered Prometheus serum    |

#### Physical tài liệu Types

| Type                 | Visual Style                                            | Where Found                      | Content                                             |
| -------------------- | ------------------------------------------------------- | -------------------------------- | --------------------------------------------------- |
| **Corporate Memo**   | Clean white paper, Nexus letterhead, partially burned   | Offices, labs, executive areas   | Business quyết định, coverups, financial records     |
| **Military Orders**  | Green paper, stamped CLASSIFIED, some words blacked out | Military areas, checkpoints      | Tactical quyết định, chain-of-command communications |
| **Personal Journal** | Crumpled notebook paper, handwritten, stained           | Residential areas, camps, random | Personal stories, rumors, cảm xúc accounts        |
| **Medical Records**  | Clinical forms, partially filled, blood-stained         | Hospitals, labs, medical tents   | Patient records, experiment results, autopsy ghi chú  |
| **Graffiti**         | Spray-painted on walls, scrawled in marker              | Public spaces, tunnels, walls    | cảnh báo, faction messages, survivor pleas          |
| **Coded Messages**   | Folded paper, cipher wheel nearby, invisible ink hints  | Dead drops, hidden compartments  | Underground Network communications                  |

***

### Collectible Codex hệ thống

#### Tổng Quan

The Codex is a persistent, menu-accessible database that compiles all lore the người chơi has discovered:

#### Codex Categories

| Category               | Content                                                | Unlock Method                                                  |
| ---------------------- | ------------------------------------------------------ | -------------------------------------------------------------- |
| **History**            | Timeline events, Pre-Collapse era, The Collapse        | Audio logs, documents, main story quests                       |
| **Factions**           | Faction profiles, NPC bios, relationship history       | Meeting NPCs, completing faction quests, discovering documents |
| **Project Prometheus** | Research phases, subject profiles, facility maps       | Lab exploration, cụ thể quest chains, hidden documents       |
| **Maps & Locations**   | Zone descriptions, POI histories, hidden areas         | Visiting locations, completing exploration objectives          |
| **People**             | chính historical figures, missing persons, deceased      | Audio logs, quest completions, environmental discovery         |
| **Science & Tech**     | Nexus technology, military equipment, Crimson Flu data | tài liệu collection, tech-faction quests                       |
| **The Broker's Files** | Encrypted entries that decode as người chơi progresses     | Main story progression, high Underground reputation            |

#### Completion Rewards

| Completion % | Category       | Reward                                                     |
| :----------: | -------------- | ---------------------------------------------------------- |
|      25%     | Any category   | Codex Badge (cosmetic)                                     |
|      50%     | Any category   | Unique loading màn hình tip from that category's perspective |
|      75%     | Any category   | Exclusive cosmetic item themed to the category             |
|     100%     | Any category   | Legendary title + hidden quest related to the category     |
|     100%     | ALL categories | Ultimate title: "Archivist" + unique operator skin         |

#### Codex Entry Template

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

***

### Item Description Lore

#### Tổng Quan

Every item in the game has two description lines:

1. **Functional**: What it does mechanically (damage, weight, capacity)
2. **Flavor**: One sentence of world-building context

#### Flavor Text Guidelines

| Item Category       | Tone                     | Example                                                                                                      |
| ------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| vũ khí (common)    | Practical, factual       | "Mass-produced trước The Collapse. Still fires. That's all that matters."                                   |
| vũ khí (rare)      | Historical, cụ thể     | "Custom-built by Yuri from salvaged Nexus defense parts. Serial number filed off."                           |
| vũ khí (legendary) | Ominous, unique          | "Recovered from Subject 19's containment cell. The grip is warm to the touch."                               |
| giáp               | Protective, worn         | "Standard-issue Peacekeeper vest. The bloodstains aren't yours."                                             |
| Medical             | Clinical, urgent         | "Auto-injector loaded với adrenaline. Don't read the expiration date."                                      |
| Food/Water          | Scarce, precious         | "Canned peaches, 2028 vintage. Worth killing for in the Zone."                                               |
| chính/Access          | Mysterious, anticipatory | "Card reads 'Lab Gamma — Level 3.' Whatever's behind that door, they didn't want you finding it."            |
| Quest items         | Lore-rich, contextual    | "Dr. Chen's USB drive. The encryption will take days to crack. The data inside might crack everything else." |
| Cosmetics           | nhân vật, identity      | "Hand-stitched from old military canvas. Somewhere between uniform và uniform protest."                     |

#### Writing Rules for Item Descriptions

* Maximum 2 sentences for flavor text
* Must contain at least one world-building reference (faction, event, person, location)
* Never break the fourth wall
* Prioritize personality over information
* Legendary items should hint at their origin story mà không fully explaining it

***

### loading màn hình Lore

#### Tổng Quan

loading màn hình tips are **in-nhân vật statements** attributed to cụ thể factions hoặc individuals. They serve as passive lore delivery và atmosphere reinforcement.

> **Full specification:** Xem [loading màn hình Design](../UI_UX/LoadingScreen_Design.md) for loading type taxonomy, content type mapping, và layout mockups.

#### Content Types (by loading màn hình)

| Content Type | loading Types | Description                                                      |
| ------------ | ------------- | ---------------------------------------------------------------- |
| **Tips**     | L3, L4, L6    | Gameplay cơ chế in-nhân vật (tactical, economy, exploration) |
| **Fun Fact** | L3, L4        | Light lore, trivia, world-building snippets                      |
| **Intro**    | L4, L7        | Map/zone name và brief context                                  |
| **Lore**     | L3, L4, L6    | Faction philosophy, lore fragments, dark humor                   |

#### Format

```
"[Statement]"
— [Attribution: faction name, NPC name, or "Unknown Contractor"]
```

#### Category Distribution

| Category                     | Percentage | mục đích                             |
| ---------------------------- | :--------: | ----------------------------------- |
| Gameplay tips (in-nhân vật) |     40%    | Teach cơ chế thông qua world voice |
| Lore fragments               |     30%    | Deliver small lore bites            |
| Faction philosophy           |     20%    | Reinforce faction identities        |
| Dark humor / atmosphere      |     10%    | Tone và personality                |

#### Ví Dụ

**Gameplay tips (in-nhân vật):**

* _"Heavy bags make heavy noise. The Zone punishes greed."_ — Salvage Corps field manual
* _"nếu you hear a click và nothing happens, run. The second click won't be as quiet."_ — Underground survival guide

**Lore fragments:**

* _"Day 1,247. The radio still plays Nexus Corp's automated welcome message. Nobody's listening."_ — Recovered journal
* _"The reactor hasn't been serviced in five years. It shouldn't still be running. That's what worries me."_ — Engineer's note

**Faction philosophy:**

* _"Every Contractor starts as a stranger. Every stranger is a threat until proven otherwise."_ — Peacekeeper orientation manual
* _"Data is the only currency that doesn't depreciate. Protect your data."_ — Tech Syndicate internal memo

**Dark humor:**

* _"Tip: nếu you find a room full of dead bodies và one open door, don't cách dùng that door."_ — Unknown Contractor
* _"The expiration date on the canned food is a suggestion. The expiration date on the medicine is a prayer."_ — Dr. Wells

***

### Lore Gating

#### Gating by người chơi Level

| người chơi Level | Lore Access                                                                          | Design mục đích                            |
| ------------ | ------------------------------------------------------------------------------------ | ----------------------------------------- |
| 1-10         | Basic world context only — The Collapse happened, factions exist, Zone is dangerous  | Don't overwhelm new người chơi               |
| 10-20        | Faction depths, early Prometheus hints, regional history chi tiết                     | Reward continued play với deeper context |
| 20-30        | Major revelations — Prometheus subjects, corporate culpability, military involvement | Narrative payoffs for invested người chơi    |
| 30-40        | The Broker's secrets, endgame lore, cross-faction hidden truths                      | Reserved for veterans                     |
| 40+          | Meta-narrative content — unreliable narrator reveals, "true history" contradictions  | Deep engagement rewards                   |

#### Gating by Season

| Season    | New Lore available                                             | Design mục đích        |
| --------- | -------------------------------------------------------------- | --------------------- |
| Launch    | Foundation — world trạng thái, factions, basic history              | Establish the world   |
| Season 2  | Prometheus chi tiết, The Collapse causes, faction conflicts     | Deepen the mystery    |
| Season 3  | Major truth reveals, Firebase Delta lore, Director Park's past | Climactic revelations |
| Season 4+ | Broker identity, cure plotline, external threats               | Evolving world        |

#### Anti-Spoiler Rules

* **Main story lore is never fully dataminable** — final quest dialogue is server-side until the quest becomes available
* **Seasonal lore is drip-fed** — new audio logs và documents appear as the season progresses, not all at launch
* **Community discussion is encouraged** — deliberately tạo moments where người chơi need to share information to piece together the full picture (e.g., different logs found in different raids)
