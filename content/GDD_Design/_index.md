---
title: GDD Design
type: docs
---

# GDD Design

### Purpose

This document focuses on **game design, art direction, and player experience**. This is the primary reference for:

* Game Designers designing mechanics and balance
* Artists creating visual assets
* Level Designers building maps
* Sound Designers creating audio experience
* UI/UX Designers designing interfaces

**Does not include:** Implementation details, code, technical specifications (see [Technical GDD](https://github.com/oaiba/ExtractionDocument/blob/main/GDD_Technical/README.md))

***

### 📚 Documentation Structure

#### 🎮 Game Design

Core game design, mechanics, progression, and monetization systems

* [**Overview**](GameDesign/Overview.md) - Game concept, pillars, target audience, competitive analysis
* [**Core Gameplay**](GameDesign/CoreGameplay.md) - Gameplay loop, phases, player psychology, session flow
* [**Controls & UX**](GameDesign/Controls.md) - Design philosophy, cross-platform strategy, accessibility
* [**Progression**](GameDesign/Progression.md) - Player progression, XP, quests, battle pass
* [**Economy**](GameDesign/Economy.md) - Monetization, currencies, pricing, marketplace, anti-fraud
* [**Ranked Mode**](GameDesign/RankedMode.md) - Ranking system, matchmaking, competitive integrity, season rewards
* [**Live Ops**](GameDesign/LiveOps.md) - Events, content calendar, monetization events, community management
* [**Accessibility**](GameDesign/Accessibility.md) - Visual, auditory, motor, cognitive accessibility features
* [**Localization**](GameDesign/Localization.md) - Supported languages, text guidelines, cultural adaptation
* [**Safe House**](GameDesign/Safe_House_Design.md) - Operator base, Stash Room, Trophy Vault, Workbench, crafting, meta-game hub
* [**Stash**](Stash_Design.md) - Permanent storage for extracted items, grid system, containers, progression

***

#### 📖 Story & Narrative

World lore, factions, and character backstories

* [**Narrative**](Story/Narrative.md) - World lore, The Collapse, factions, operator backstories, environmental storytelling

***

#### 👥 Social & Multiplayer

Squad systems, clans, karma, communication, and community features

* [**Multiplayer**](Social/Multiplayer.md) - Squad system, VOIP (spatial proximity chat), ping system, karma & trust, emotes & gestures, LFG, clans, friends, matchmaking (MMR/SBMM), social hub (Safe House), dynamic in-raid interactions, anti-toxicity, post-match flow, cross-platform (EOS)

***

#### ⚔️ Combat Systems

Weapon design, items, and combat mechanics

* [**Weapons**](Combat/Weapons.md) - Weapon categories, modifications, combat mechanics, balance
* [**Items & Economy**](Combat/Items.md) - Item systems, loot, inventory, trading marketplace

***

#### 👤 Characters

Character design and abilities

* [**Operators**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Operators.md) - Operator classes, abilities, progression, synergies, cosmetics

***

#### 🤖 AI & Enemies

Enemy design, behavior systems, and difficulty

* [**Enemy Behavior**](AI/EnemyBehavior.md) - Enemy types, behavior systems, boss design, AI balancing

***

#### 🗺️ World Design

Maps, environments, and level design

* [**Map Design**](World/MapDesign.md) - Map structure, zones, loot distribution, environmental storytelling

***

#### 🎨 Visual Design

Art direction and user interface

* [**Art Direction**](Visuals/ArtDirection.md) - Visual style, color palette, character/environment art, VFX, animation
* [**User Interface**](Visuals/UserInterface.md) - UI/UX design, screen layouts, controls, accessibility

***

#### 🔊 Audio Design

Sound and music

* [**Sound Design**](Audio/SoundDesign.md) - Audio vision, combat audio, environmental audio, music, voice lines

***

#### 📋 Project Scope

Risks, boundaries, and project management

* [**Risks**](ProjectScope/Risks.md) - Design, technical, business, and operational risks with mitigation
* [**Non-Goals**](ProjectScope/NonGoals.md) - Explicit exclusions and what we intentionally won't build

***

### 📖 How to Use This Document

**For Game Designers:**

* Read entirely to understand game vision
* Reference when designing new mechanics
* Update when there are balance changes

**For Artists:**

* Focus on Visuals section (Art Direction, UI)
* Reference Characters and World for context
* Follow guidelines when creating assets

**For Level Designers:**

* Deep dive into World → Map Design
* Understand Core Gameplay Loop to design flow
* Coordinate with Artists on visual style

**For Sound Designers:**

* Follow Audio → Sound Design guidelines
* Reference Core Gameplay to understand audio cues
* Coordinate with Game Designers on feedback

**For UI/UX Designers:**

* Follow Visuals → User Interface guidelines
* Understand User Flow and player journey
* Coordinate with Developers on technical constraints

***

### 🎯 Design Philosophy

**Player-First Design:**

* Every design decision must benefit player experience
* Fair and balanced gameplay
* Respect player's time and effort

**Mobile-Optimized:**

* Controls must be intuitive and responsive
* Matches designed for short sessions (10-15 minutes)
* Performance across multiple devices

**Depth Through Simplicity:**

* Easy to learn, hard to master
* Clear mechanics with deep strategy
* Progressive complexity

***

### 📝 Glossary

**Core Terms:**

* **Extraction:** Process of leaving map with loot
* **Hot Zone:** High-risk, high-reward areas
* **Operator:** Playable character class
* **Stash:** Permanent storage for extracted items
* **MMR:** Matchmaking Rating
* **POI:** Point of Interest
* **TTK:** Time to Kill
* **DPS:** Damage Per Second

***

### 📅 Update Log

| Date       | Section      | Changes                                                     | Updated By |
| ---------- | ------------ | ----------------------------------------------------------- | ---------- |
| 2026-02-07 | GameDesign   | Added Accessibility.md (visual, auditory, motor, cognitive) | Team       |
| 2026-02-07 | GameDesign   | Added Localization.md (languages, cultural adaptation)      | Team       |
| 2026-02-07 | ProjectScope | Added Risks.md (design, tech, business risks)               | Team       |
| 2026-02-07 | ProjectScope | Added NonGoals.md (explicit exclusions)                     | Team       |
| 2026-02-07 | AI           | Added EnemyBehavior.md (enemy types, behavior, bosses)      | Team       |
| 2026-02-07 | GameDesign   | Added RankedMode.md (ranking, matchmaking, competitive)     | Team       |
| 2026-02-07 | GameDesign   | Added LiveOps.md (events, content calendar, monetization)   | Team       |
| 2026-02-07 | Story        | Added Narrative.md (lore, factions, backstories)            | Team       |
| 2026-02-07 | GameDesign   | Added Economy.md (monetization, currencies, anti-fraud)     | Team       |
| 2026-02-07 | Social       | Added Multiplayer.md (squads, clans, communication)         | Team       |
| 2026-02-07 | Controls     | Expanded with controller support, keyboard options          | Team       |
| 2026-02-06 | Structure    | Reorganized to folder-based system                          | Team       |
| 2026-02-06 | Combat       | Added Weapons & Items documents                             | Team       |
| 2026-02-06 | All          | Initial documentation                                       | Team       |

***

### 🔗 Quick Navigation

**Start Here:**

* New to project? → [Overview](GameDesign/Overview.md)
* Understanding gameplay? → [Core Gameplay](GameDesign/CoreGameplay.md)
* Designing characters? → [Operators](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/Operators.md)

**World & Story:**

* World lore & factions → [Narrative](Story/Narrative.md)
* Multiplayer & social → [Multiplayer](Social/Multiplayer.md)
* AI & enemies → [Enemy Behavior](AI/EnemyBehavior.md)

**Competitive:**

* Ranked system → [Ranked Mode](GameDesign/RankedMode.md)
* Events & live ops → [Live Ops](GameDesign/LiveOps.md)

**Economy & Monetization:**

* Currencies & pricing → [Economy](GameDesign/Economy.md)
* Items & marketplace → [Items](Combat/Items.md)
* Stash & storage → [Stash Design](Stash_Design.md)
* Safe House & crafting → [Safe House Design](GameDesign/Safe_House_Design.md)

**Platform & Accessibility:**

* Accessibility features → [Accessibility](GameDesign/Accessibility.md)
* Localization strategy → [Localization](GameDesign/Localization.md)

**Project Management:**

* Project risks → [Risks](ProjectScope/Risks.md)

**Deep Dives:**
