---
title: "GDD Technical"
type: docs
---

## Purpose

This document focuses on **technical implementation, enums, codenames, and feature TODOs**. This is the primary reference for:
- Developers implementing game systems
- Programmers writing code
- Technical Artists setting up pipelines
- DevOps configuring infrastructure

**Does not include:** Deep code implementations, algorithms, detailed pseudo-code (focus on structure and contracts)

---

### 📐 Standards & Conventions
Coding patterns, naming rules, and project organization

- **[Coding & Asset Standards](./CodingStandards.md)** - C++ naming conventions (Epic standard), UE5 asset naming, content folder structure, module architecture, UPROPERTY/UFUNCTION guidelines, Gameplay Tags, Blueprint standards, source control conventions

---

## 📚 Documentation Structure

### 🏗️ Core Systems
Foundation architecture and networking

{{< cards cols="3" >}}
  {{< card link="Core/Architecture" title="Architecture" icon="server" subtitle="System architecture, tech stack, module structure" >}}
  {{< card link="Core/NetworkingSystem" title="Networking" icon="globe" subtitle="Client-server model, sync, matchmaking" >}}
  {{< card link="Core/DevelopmentRoadmap" title="Roadmap" icon="map" subtitle="Sprint planning, milestones, priorities" >}}
{{< /cards >}}

---

### 🎮 Gameplay Systems
Character, combat, inventory, and UI mechanics

{{< cards cols="3" >}}
  {{< card link="Gameplay/CharacterSystem" title="Character System" icon="user" subtitle="Operator classes, abilities, stats" >}}
  {{< card link="Gameplay/WeaponSystem" title="Weapon System" icon="fire" subtitle="Weapons, attachments, ballistics" >}}
  {{< card link="Gameplay/InventorySystem" title="Inventory System" icon="briefcase" subtitle="Grid system, items, stash, loot" >}}
  {{< card link="Gameplay/ControlSystem" title="Control System" icon="cursor-click" subtitle="Input abstraction, movement logic" >}}
  {{< card link="Systems/SettingsSystem" title="Settings System" icon="cog" subtitle="Scalability, audio, persistence" >}}
  {{< card link="Systems/UISystem" title="UI System" icon="template" subtitle="HUD, menus, widgets, touch controls" >}}
{{< /cards >}}

---

### 🤖 AI & World Systems
AI behavior, map, and narrative

{{< cards cols="3" >}}
  {{< card link="Systems/AISystem" title="AI System" icon="chip" subtitle="Enemy behavior, combat AI, bosses" >}}
  {{< card link="Systems/MapSystem" title="Map System" icon="location-marker" subtitle="Zones, extraction, hazards, loot containers" >}}
  {{< card link="Systems/NarrativeSystem" title="Narrative System" icon="book-open" subtitle="Quests, factions, dialogue, story" >}}
{{< /cards >}}

---

### 👥 Social & Competitive Systems
Multiplayer, ranked, progression, and community

{{< cards cols="3" >}}
  {{< card link="Systems/SocialSystem" title="Social System" icon="users" subtitle="Squads, voice/text chat, clans, friends" >}}
  {{< card link="Systems/RankedSystem" title="Ranked System" icon="star" subtitle="RP, matchmaking, seasons, anti-cheat" >}}
  {{< card link="Systems/ProgressionSystem" title="Progression" icon="trending-up" subtitle="XP, leveling, currencies, Battle Pass" >}}
  {{< card link="Systems/LiveOpsSystem" title="Live Ops" icon="calendar" subtitle="Events, challenges, shop, notifications" >}}
{{< /cards >}}

---

### ♿ Platform & Accessibility
Localization, accessibility, persistence, and audio

{{< cards cols="3" >}}
  {{< card link="Systems/LocalizationSystem" title="Localization" icon="translate" subtitle="Languages, text, RTL, voice" >}}
  {{< card link="Systems/AccessibilitySystem" title="Accessibility" icon="eye" subtitle="Colorblind, subtitles, aim assist" >}}
  {{< card link="Systems/AudioSystem" title="Audio System" icon="volume-up" subtitle="Sound, music, voice lines, mixing" >}}
  {{< card link="Systems/SaveSystem" title="Save System" icon="cloud-upload" subtitle="Save/load, cloud sync, persistence" >}}
  {{< card link="Systems/TutorialSystem" title="Tutorial System" icon="academic-cap" subtitle="Onboarding, hints, training mode" >}}
{{< /cards >}}

---

### ⚡ Performance & Optimization
Mobile optimization and profiling

{{< cards cols="3" >}}
  {{< card link="Performance/Optimization" title="Optimization" icon="lightning-bolt" subtitle="Mobile performance, memory, profiling" >}}
{{< /cards >}}

---

## 📖 How to Use This Document

{{< cards cols="3" >}}
  {{< card title="For Developers" icon="code" subtitle="Reference enum/codenames, check TODOs, follow architecture." >}}
  {{< card title="For Tech Artists" icon="color-swatch" subtitle="Check asset structures, naming conventions, performance budgets." >}}
  {{< card title="For DevOps" icon="server" subtitle="Review infra requirements, scaling, deployment pipelines." >}}
{{< /cards >}}

---

## 🎯 Technical Philosophy

{{< cards cols="3" >}}
  {{< card title="Clean Architecture" icon="cube" subtitle="Separation of concerns, DI, interface-driven, testable." >}}
  {{< card title="Mobile-First" icon="device-mobile" subtitle="Performance budgets, battery efficiency, touch inputs." >}}
  {{< card title="Scalable" icon="trending-up" subtitle="Modular design, easy to extend, minimal coupling." >}}
{{< /cards >}}

---

## 🔧 Tech Stack

### Client (Unreal Engine 5)
- **Engine:** Unreal Engine 5.4+
- **Language:** C++ (primary), Blueprints (prototyping & design)
- **Networking:** Unreal Replication, EOS (Epic Online Services)
- **UI:** UMG (Unreal Motion Graphics), Slate (editor tools)
- **Platform:** PC (primary), Console (future)
- **Voice Chat:** Vivox / EOS Voice

### Server
- **Dedicated Server:** UE5 Dedicated Server builds
- **Backend Services:** EOS for matchmaking, authentication, social
- **Database:** PostgreSQL (persistent), Redis (cache, sessions)
- **Hosting:** AWS / GCP (TBD)
- **CDN:** CloudFlare

### Tools
- **Version Control:** Git (with Git LFS for assets)
- **CI/CD:** GitHub Actions / Jenkins
- **Analytics:** Epic Analytics / Firebase
- **Crash Reporting:** Crashlytics / Sentry

---

## 📝 Naming Conventions

### Enums
```cpp
// PascalCase with namespace prefix
public enum EWeaponType { ... }
public enum EOperatorClass { ... }
public enum ERarity { ... }
```

### Code Names (Identifiers)
```cpp
// Format: CATEGORY_SUBCATEGORY_NAME
// Examples:
WPN_AR_AK47          // Weapon - Assault Rifle - AK47
ITEM_MED_BANDAGE     // Item - Medical - Bandage
OPER_CLASS_ASSAULT   // Operator - Class - Assault
ATT_OPTIC_REDDOT     // Attachment - Optic - RedDot
```

### TODO Format
```cpp
// TODO(priority): Description
// Priority: P0 (critical), P1 (high), P2 (medium), P3 (low)
// TODO(P0): Implement core movement system
// TODO(P1): Add weapon recoil patterns
// TODO(P2): Optimize render pipeline
```

---

## 🔗 Quick Navigation

**Start Here:**
- New developer? → [Architecture](./Core/Architecture.md)
- Setting up networking? → [Networking System](./Core/NetworkingSystem.md)
- Implementing gameplay? → [Character System](./Gameplay/CharacterSystem.md)

**Common Tasks:**
- Adding new weapon → [Weapon System](./Gameplay/WeaponSystem.md)
- Adding new item → [Inventory System](./Gameplay/InventorySystem.md)
- Optimizing performance → [Optimization](./Performance/Optimization.md)

---

## 📅 Update Log

| Date       | Section   | Changes                            | Updated By |
| ---------- | --------- | ---------------------------------- | ---------- |
| 2026-02-13 | Structure | Converted lists to card layout     | Agent      |
| 2026-02-07 | Systems   | Added ProgressionSystem.md         | Team       |
| 2026-02-07 | Systems   | Added SaveSystem.md                | Team       |
| 2026-02-07 | Systems   | Added TutorialSystem.md            | Team       |
| 2026-02-07 | Systems   | Added UISystem.md                  | Team       |
| 2026-02-07 | Systems   | Added AudioSystem.md               | Team       |
| 2026-02-07 | Systems   | Added NarrativeSystem.md           | Team       |
| 2026-02-07 | Systems   | Added LiveOpsSystem.md             | Team       |
| 2026-02-07 | Systems   | Major expansion of MapSystem.md    | Team       |
| 2026-02-07 | Systems   | Added AccessibilitySystem.md       | Team       |
| 2026-02-07 | Systems   | Added LocalizationSystem.md        | Team       |
| 2026-02-07 | Systems   | Added RankedSystem.md              | Team       |
| 2026-02-07 | Systems   | Added SocialSystem.md              | Team       |
| 2026-02-07 | Systems   | Major expansion of AISystem.md     | Team       |
| 2026-02-07 | Gameplay  | Updated ControlSystem.md           | Team       |
| 2026-02-06 | Structure | Reorganized to folder-based system | Team       |
| 2026-02-06 | All       | Focused on enums, codenames, TODOs | Team       |
| 2026-02-06 | Core      | Initial documentation              | Team       |


