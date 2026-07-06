---
title: MVP Scope - Minimum Viable Product
type: docs
---

# MVP Scope - Minimum Viable Product

###  Critical Milestones & Targets

| Milestone                | Target Date | Key Deliverable                              | Dependency        |
| ------------------------ | ----------- | -------------------------------------------- | ----------------- |
| **Project Start**        | T-Minus 0   | Core Team Assembled                          | Budget Approval   |
| **M1: Prototype**        | Month 2     | Playable Greybox Loop (Server Authoritative) | UE5 Mobile Setup  |
| **M2: Vertical Slice**   | Month 4     | One Polished Zone + Full Combat Loop         | Asset Production  |
| **M3: Alpha (Internal)** | Month 5     | Full Map 1 + 3 Operators                     | Backend Stability |
| **M4: Beta (Closed)**    | Month 7     | Economy + Quest System                       | Alpha Feedback    |
| **M5: Soft Launch**      | Month 9     | Store + Live Ops Pipeline                    | Platform Cert     |
| **M6: Global Launch**    | Month 11    | Marketing Push + Events                      | Soft Launch Data  |

***

###  MVP ↔ Quarterly Roadmap

Mapping milestones to quarters for stakeholder reporting and alignment with genre benchmarks (e.g. HAWKED, Tarkov). _See_ [_Scope Review & Planning_](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/ProjectScope/project-scope-review-and-planning.html) _for full planning._

| Quarter | Milestones                       | Content theme    | Key deliverables (high-level)                                                                          |
| ------- | -------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------ |
| **Q1**  | M1 Prototype, M2 Vertical Slice  | Foundation       | Playable greybox, one polished zone, full combat loop; server-authoritative validated; asset pipeline. |
| **Q2**  | M3 Alpha (Internal)              | Core loop        | Map 1 full, 3 operators, Scav AI, inventory/stash, vendor "The Fixer".                                 |
| **Q3**  | M4 Beta (Closed), M5 Soft Launch | Economy & social | Economy, quests, 5 operators, gunsmith, squad; store + live ops pipeline.                              |
| **Q4**  | M6 Global Launch                 | Launch           | Marketing push, events, platform cert complete.                                                        |

***

###  Technical Dependencies

* **Server Architecture:** Dedicated servers (Agones/K8s) must be validated by **M2**.
* **Asset Pipeline:** Mobile optimization workflow (LODs, imposter system) established by **M1**.
* **Backend Services:** Auth, Inventory, and Matchmaking APIs ready for load testing by **M3**.

***

###  Alpha Scope (Technical Test)

**Objective:** Validate core gameplay loop, server stability, and "Game Feel".

#### Features Included

* **Map:** "Industrial Zone" (Small, focused map \~500x500m)
  * 3 Extraction Points (1 Always Open, 1 Conditional/Paid, 1 Chance)
  * High-Density Loot Areas vs. Low-Density Transit Routes
* **Game Loop:** Spawn -> Loot/Explore -> Combat/Sneak -> Extract/Die
* **Operators:** 3 Basic Classes (Archetypes)
  * **Assault:** Balanced stats, standard rig capacity.
  * **Scout:** High stamina, lower health, light rig only.
  * **Support:** Slow movement, high carry weight, medical bonuses.
* **Combat Mechanics:**
  * **Ballistics:** Projectile-based shooting (not hitscan) with bullet drop.
  * **Recoil:** Pattern-based recoil with randomization.
  * **Damage:** Location-based damage (Head, Thorax, Stomach, Limbs).
* **Weapons:**
  * **AR:** AK-47 (High recoil, high damage), M4A1 (Moddable, stable).
  * **SMG:** MP5 (Close quarters, low pen).
  * **Sidearm:** Glock 17 (Emergency backup).
* **Enemies:** Basic AI (Scavs)
  * Behaviors: Patrol, Investigate Noise, Take Cover, Shout Callouts.
  * Spawn logic: Wave-based or zone-triggered.
* **Inventory:**
  * **Grid System:** Different items take different shapes (1x1, 2x3).
  * **Containers:** Backpacks and Rigs have internal grids.
* **Metagame:**
  * **Stash:** Persistent storage outside of raid.
  * **Vendor:** "The Fixer" (Buy basic ammo/meds, Sell loot for Credits).

#### Features Excluded (For Beta)

* Complex Quest System (Tasks, Multi-stage missions)
* Advanced Gunsmithing (only basic slot attachments for Alpha)
* Advanced AI (Bosses, Raiders, Flanking tactics)
* Party System / Squad Matchmaking (Solo only for Alpha stability)
* Real-money Store

***

###  Beta Scope (Soft Launch)

**Objective:** Validate economy balance, retention loops, and social systems.

#### Features Added

* **Map:** "Industrial Zone" (Expanded) + "Urban Ruins" (Early WIP)
* **Operators:** Added Tank (Heavy Armor) and Specialist (Tech/Gadget) - Total 5.
* **Weapons:** Shotguns (entry level), DMRs (mid-range), Snipers (high tier).
* **Systems:**
  * **Gunsmith:** Deep weapon modding (Muzzles, Stocks, Grips affect handling stats).
  * **Market:** Dynamic pricing or Player-to-NPC trading adjustments.
  * **Quests:** Daily Contracts + Main Story Chapter 1 (Tutorialization).
  * **Health System:** Bleeding (Light/Heavy), Fractures, Pain (Screen effects).
* **Social:** Squad System (Up to 3 players), Friend List, Basic Spectator (Teammate only).

***

###  Feature Comparison Matrix

| Feature Category | Prototype |    Alpha    |          Beta          |     Launch    |
| ---------------- | :-------: | :---------: | :--------------------: | :-----------: |
| **Maps**         |  Greybox  | 1 (Partial) | 1 (Full) + 1 (Partial) |     3 Maps    |
| **Operators**    | 1 (Dummy) |      3      |            5           |       8+      |
| **Weapons**      |     2     |      5      |           15+          |      30+      |
| **AI Behaviors** |   Static  |    Patrol   |      Cover, Flank      | Bosses, Elite |
| **Loot System**  |   Random  |    Tables   |         Dynamic        |  Event-based  |
| **Questing**     |          |            |          Basic         |    Campaign   |
| **Progression**  |  Session  |     Wipe    |       Persistent       |    Seasons    |
| **Monetization** |          |            |       Test Store       |   Full Store  |

***

###  Cut Content (Backlog)

* **Vehicles:** Deferred to Year 2 (Requires physics overhaul).
* **Clan System:** Deferred to Post-Launch.
* **Dynamic Weather:** Deferred to First Major Update (Performance risk).
* **Killcam:** Deferred to esports update (Technical complexity/Anti-cheat risk).

***

###  Document Ownership & Changelog

| Role            | Owner              | Approver           |
| --------------- | ------------------ | ------------------ |
| **Author**      | Lead Producer      | Executive Producer |
| **Tech Review** | Technical Director | CTO                |

**Recent Changes:**

* **v1.3 (2026-02-12):** Aligned with [Scope Review & Planning](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/ProjectScope/project-scope-review-and-planning.html): added MVP ↔ Quarterly Roadmap (Q1–Q4), content themes.
* **v1.2 (2026-02-11):** Expanded Alpha/Beta features with specific mechanics (Ammo types, Health states).
* **v1.1 (2026-02-09):** Refined Milestones with specific deliverable targets and dependencies.
* **v1.0 (2026-02-07):** Initial MVP definition.
