---
title: "MVP Scope - Minimum Viable Product"
type: docs
---

### Critical Milestones & Targets

| Milestone | Target Date | Key Deliverable | Dependency |
| ------------------------ | ----------- | -------------------------------------------- | ----------------- |
| **Project Start** | T-Minus 0 | Core Team Assembled | Budget Approval |
| **M1: Prototype** | Month 2 | Playable Greybox Loop (Server Authoritative) | UE5 Mobile Setup |
| **M2: Vertical Slice** | Month 4 | One Polished Zone + Full Combat Loop | Asset Production |
| **M3: Alpha (Internal)** | Month 5 | Full Map 1 + 3 Operators | Backend Stability |
| **M4: Beta (Closed)** | Month 7 | Economy + Quest System | Alpha Feedback |
| **M5: Soft Launch** | Month 9 | Store + Live Ops Pipeline | Platform Cert |
| **M6: Global Launch** | Month 11 | Marketing Push + Events | Soft Launch Data |

***

### MVP <-> Quarterly Roadmap

Map milestone sang quarter để báo cáo stakeholder và canh với benchmark genre (ví dụ HAWKED, Tarkov). _Xem_ [_Scope Review & Planning_](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/ProjectScope/project-scope-review-and-planning.html) _cho planning đầy đủ._

| Quarter | Milestones | Content theme | Key deliverables (high-level) |
| ------- | -------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------ |
| **Q1** | M1 Prototype, M2 Vertical Slice | Foundation | Playable greybox, một zone polished, full combat loop; server-authoritative validated; asset pipeline. |
| **Q2** | M3 Alpha (Internal) | Core loop | Map 1 full, 3 operators, Scav AI, inventory/stash, vendor "The Fixer". |
| **Q3** | M4 Beta (Closed), M5 Soft Launch | Economy & social | Economy, quest, 5 operators, gunsmith, squad; store + live ops pipeline. |
| **Q4** | M6 Global Launch | Launch | Marketing push, event, platform cert complete. |

***

### Technical Dependencies

* **Server Architecture:** Dedicated servers (Agones/K8s) phải được validate trước **M2**.
* **Asset Pipeline:** Mobile optimization workflow (LOD, imposter system) thiết lập trước **M1**.
* **Backend Services:** Auth, Inventory, và Matchmaking API sẵn sàng load test trước **M3**.

***

### Alpha Scope (Technical Test)

**Objective:** Validate core gameplay loop, server stability, và "Game Feel".

#### Features Included

* **Map:** "Industrial Zone" (map nhỏ, tập trung khoảng 500x500m)
  * 3 Extraction Points (1 Always Open, 1 Conditional/Paid, 1 Chance)
  * High-Density Loot Areas vs. Low-Density Transit Routes
* **Game Loop:** Spawn -> Loot/Explore -> Combat/Sneak -> Extract/Die
* **Operators:** 3 Basic Classes (Archetypes)
  * **Assault:** Stat cân bằng, rig capacity standard.
  * **Scout:** Stamina cao, health thấp hơn, chỉ light rig.
  * **Support:** Movement chậm, carry weight cao, medical bonus.
* **Combat Mechanics:**
  * **Ballistics:** Projectile-based shooting (không hitscan) có bullet drop.
  * **Recoil:** Recoil theo pattern có randomization.
  * **Damage:** Damage theo location (Head, Thorax, Stomach, Limbs).
* **Weapons:**
  * **AR:** AK-47 (recoil cao, damage cao), M4A1 (moddable, ổn định).
  * **SMG:** MP5 (close quarters, low pen).
  * **Sidearm:** Glock 17 (emergency backup).
* **Enemies:** Basic AI (Scavs)
  * Behavior: Patrol, Investigate Noise, Take Cover, Shout Callouts.
  * Spawn logic: Wave-based hoặc zone-triggered.
* **Inventory:**
  * **Grid System:** Item khác nhau chiếm shape khác nhau (1x1, 2x3).
  * **Containers:** Backpack và Rig có internal grid.
* **Metagame:**
  * **Stash:** Persistent storage ngoài raid.
  * **Vendor:** "The Fixer" (mua ammo/med cơ bản, bán loot lấy Credits).

#### Features Excluded (For Beta)

* Complex Quest System (Task, mission nhiều stage)
* Advanced Gunsmithing (Alpha chỉ có basic slot attachment)
* Advanced AI (Boss, Raider, flanking tactic)
* Party System / Squad Matchmaking (Alpha solo-only để ổn định)
* Real-money Store

***

### Beta Scope (Soft Launch)

**Objective:** Validate economy balance, retention loop, và social system.

#### Features Added

* **Map:** "Industrial Zone" (Expanded) + "Urban Ruins" (Early WIP)
* **Operators:** Thêm Tank (Heavy Armor) và Specialist (Tech/Gadget) - tổng 5.
* **Weapons:** Shotgun (entry level), DMR (mid-range), Sniper (high tier).
* **Systems:**
  * **Gunsmith:** Weapon modding sâu (Muzzle, Stock, Grip ảnh hưởng handling stat).
  * **Market:** Dynamic pricing hoặc Player-to-NPC trading adjustment.
  * **Quests:** Daily Contracts + Main Story Chapter 1 (Tutorialization).
  * **Health System:** Bleeding (Light/Heavy), Fracture, Pain (screen effect).
* **Social:** Squad System (tối đa 3 người), Friend List, Basic Spectator (chỉ teammate).

***

### Feature Comparison Matrix

| Feature Category | Prototype | Alpha | Beta | Launch |
| ---------------- | :-------: | :---------: | :--------------------: | :-----------: |
| **Maps** | Greybox | 1 (Partial) | 1 (Full) + 1 (Partial) | 3 Maps |
| **Operators** | 1 (Dummy) | 3 | 5 | 8+ |
| **Weapons** | 2 | 5 | 15+ | 30+ |
| **AI Behaviors** | Static | Patrol | Cover, Flank | Bosses, Elite |
| **Loot System** | Random | Tables | Dynamic | Event-based |
| **Questing** | | | Basic | Campaign |
| **Progression** | Session | Wipe | Persistent | Seasons |
| **Monetization** | | | Test Store | Full Store |

***

### Cut Content (Backlog)

* **Vehicles:** Defer sang Year 2 (cần physics overhaul).
* **Clan System:** Defer post-launch.
* **Dynamic Weather:** Defer tới First Major Update (performance risk).
* **Killcam:** Defer tới esports update (technical complexity/anti-cheat risk).

***

### Document Ownership & Changelog

| Role | Owner | Approver |
| --------------- | ------------------ | ------------------ |
| **Author** | Lead Producer | Executive Producer |
| **Tech Review** | Technical Director | CTO |

**Recent Changes:**

* **v1.3 (2026-02-12):** Aligned với [Scope Review & Planning](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/ProjectScope/project-scope-review-and-planning.html): thêm MVP <-> Quarterly Roadmap (Q1-Q4), content theme.
* **v1.2 (2026-02-11):** Mở rộng Alpha/Beta features với mechanic cụ thể (Ammo type, Health state).
* **v1.1 (2026-02-09):** Refine milestone với deliverable target và dependency cụ thể.
* **v1.0 (2026-02-07):** Định nghĩa MVP ban đầu.
