---
title: "GDD Technical"
type: docs
---

# Technical Game Design Document
## Extraction Topdown Mobile Multiplayer

**For:** Developers, Programmers, Technical Artists, DevOps

**[← Back to Main](/)** | **[View High-Level GDD →](/GDD_Design/)**

---

## Purpose

This document focuses on **technical implementation, enums, codenames, and feature TODOs**. This is the primary reference for:
- Developers implementing game systems
- Programmers writing code
- Technical Artists setting up pipelines
- DevOps configuring infrastructure

**Does not include:** Deep code implementations, algorithms, detailed pseudo-code (focus on structure and contracts)

---

## 📚 Documentation Structure

### 🏗️ Core Systems
Foundation architecture and networking

- **[Architecture](./Core/Architecture.md)** - System architecture, tech stack, module structure
- **[Networking System](./Core/NetworkingSystem.md)** - Client-server model, sync, matchmaking
- **[Development Roadmap](./Core/DevelopmentRoadmap.md)** - Sprint planning, milestones, priorities

---

### 🎮 Gameplay Systems
Character, combat, inventory, and UI mechanics

- **[Character System](./Gameplay/CharacterSystem.md)** - Operator classes, abilities, stats (enums & codenames)
- **[Weapon System](./Gameplay/WeaponSystem.md)** - Weapons, attachments, combat mechanics (enums & codenames)
- **[Inventory System](./Gameplay/InventorySystem.md)** - Grid system, items, stash (enums & codenames)
- **[Control System](./Gameplay/ControlSystem.md)** - Input abstraction, cross-platform controls, movement logic
- **[UI System](./Systems/UISystem.md)** - HUD, menus, widgets, touch controls, notifications

---

### 🤖 AI & World Systems
AI behavior, map, and narrative

- **[AI System](./Systems/AISystem.md)** - Enemy types, behavior trees, perception, combat AI, bosses
- **[Map System](./Systems/MapSystem.md)** - Zones, extraction, containers, supply drops, contamination, hazards
- **[Narrative System](./Systems/NarrativeSystem.md)** - Quests, factions, dialogue, collectibles, operator stories

---

### 👥 Social & Competitive Systems
Multiplayer, ranked, progression, and community features

- **[Social System](./Systems/SocialSystem.md)** - Squads, voice/text chat, clans, friends, reporting
- **[Ranked System](./Systems/RankedSystem.md)** - RP, matchmaking, seasons, leaderboards, anti-cheat
- **[Progression System](./Systems/ProgressionSystem.md)** - XP, leveling, currencies, quests, Battle Pass
- **[Live Ops System](./Systems/LiveOpsSystem.md)** - Events, challenges, shop, notifications

---

### ♿ Platform & Accessibility
Localization, accessibility, persistence, and audio features

- **[Localization System](./Systems/LocalizationSystem.md)** - Languages, text, fonts, RTL, voice localization
- **[Accessibility System](./Systems/AccessibilitySystem.md)** - Colorblind, subtitles, aim assist, motor/cognitive
- **[Audio System](./Systems/AudioSystem.md)** - Sound, music, voice lines, 3D audio, mixing
- **[Save System](./Systems/SaveSystem.md)** - Save/load, cloud sync, data persistence, migration
- **[Tutorial System](./Systems/TutorialSystem.md)** - Onboarding, hints, tooltips, training mode

---

### ⚡ Performance & Optimization
Mobile optimization and profiling

- **[Optimization](./Performance/Optimization.md)** - Mobile performance, memory, battery, profiling

---

## 📖 How to Use This Document

**For Developers:**
- Reference enum/codename definitions
- Check TODO lists for implementation status
- Understand system contracts and interfaces
- Follow architecture guidelines

**For Technical Artists:**
- Understand data structures for assets
- Reference naming conventions
- Check performance budgets
- Coordinate with system requirements

**For DevOps:**
- Review infrastructure requirements
- Understand scaling needs
- Check deployment pipeline
- Monitor performance metrics

---

## 🎯 Technical Philosophy

**Clean Architecture:**
- Separation of concerns
- Dependency injection
- Interface-driven design
- Testable components

**Mobile-First:**
- Performance budgets enforced
- Memory constraints respected
- Battery efficiency prioritized
- Touch-optimized controls

**Scalable:**
- Modular system design
- Easy to extend
- Minimal coupling
- Clear contracts

---

## 🔧 Tech Stack

### Client (Unity)
- **Engine:** Unity 2022 LTS
- **Language:** C#
- **Networking:** Mirror / Photon (TBD)
- **UI:** Unity UI / UI Toolkit
- **Platform:** iOS, Android

### Server
- **Language:** Node.js / Go (TBD)
- **Database:** PostgreSQL (main), Redis (cache)
- **Hosting:** AWS / GCP (TBD)
- **CDN:** CloudFlare

### Tools
- **Version Control:** Git
- **CI/CD:** GitHub Actions / Jenkins
- **Analytics:** Firebase Analytics
- **Crash Reporting:** Crashlytics

---

## 📝 Naming Conventions

### Enums
```csharp
// PascalCase with namespace prefix
public enum EWeaponType { ... }
public enum EOperatorClass { ... }
public enum ERarity { ... }
```

### Code Names (Identifiers)
```csharp
// Format: CATEGORY_SUBCATEGORY_NAME
// Examples:
WPN_AR_AK47          // Weapon - Assault Rifle - AK47
ITEM_MED_BANDAGE     // Item - Medical - Bandage
OPER_CLASS_ASSAULT   // Operator - Class - Assault
ATT_OPTIC_REDDOT     // Attachment - Optic - RedDot
```

### TODO Format
```csharp
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

**New Systems:**
- AI & enemies → [AI System](./Systems/AISystem.md)
- Map & extraction → [Map System](./Systems/MapSystem.md)
- Quests & story → [Narrative System](./Systems/NarrativeSystem.md)
- Multiplayer & squads → [Social System](./Systems/SocialSystem.md)
- Ranked & matchmaking → [Ranked System](./Systems/RankedSystem.md)
- XP & leveling → [Progression System](./Systems/ProgressionSystem.md)
- Events & Battle Pass → [Live Ops System](./Systems/LiveOpsSystem.md)
- Sound & music → [Audio System](./Systems/AudioSystem.md)
- HUD & menus → [UI System](./Systems/UISystem.md)
- Save & cloud → [Save System](./Systems/SaveSystem.md)
- Onboarding → [Tutorial System](./Systems/TutorialSystem.md)
- Localization → [Localization System](./Systems/LocalizationSystem.md)
- Accessibility → [Accessibility System](./Systems/AccessibilitySystem.md)

---

## 📅 Update Log

| Date       | Section   | Changes                            | Updated By |
| ---------- | --------- | ---------------------------------- | ---------- |
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

---

**[← Back to Main](/)** | **[View High-Level GDD →](/GDD_Design/)**
