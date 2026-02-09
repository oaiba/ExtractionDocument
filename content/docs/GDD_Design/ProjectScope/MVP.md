# MVP Scope - Minimum Viable Product

**[← Back to Project Scope](./NonGoals.md)** | **[Index](../README.md)** | **[Next: Risk Analysis →](./Risks.md)**

---

## 📅 Critical Milestones & Targets

| Milestone                | Target Date | Key Deliverable                              | Dependency        |
| :----------------------- | :---------- | :------------------------------------------- | :---------------- |
| **Project Start**        | T-Minus 0   | Core Team Assembled                          | Budget Approval   |
| **M1: Prototype**        | Month 2     | Playable Greybox Loop (Server Authoritative) | UE5 Mobile Setup  |
| **M2: Vertical Slice**   | Month 4     | One Polished Zone + Full Combat Loop         | Asset Production  |
| **M3: Alpha (Internal)** | Month 5     | Full Map 1 + 3 Operators                     | Backend Stability |
| **M4: Beta (Closed)**    | Month 7     | Economy + Quest System                       | Alpha Feedback    |
| **M5: Soft Launch**      | Month 9     | Store + Live Ops Pipeline                    | Platform Cert     |
| **M6: Global Launch**    | Month 11    | Marketing Push + Events                      | Soft Launch Data  |

---

## 🔗 Technical Dependencies

*   **Server Architecture:** Dedicated servers (Agones/K8s) must be validated by **M2**.
*   **Asset Pipeline:** Mobile optimization workflow (LODs, imposter system) established by **M1**.
*   **Backend Services:** Auth, Inventory, and Matchmaking APIs ready for load testing by **M3**.

---

## 🎯 Alpha Scope (Technical Test)

**Objective:** Validate core gameplay loop and server stability.

### Features Included
*   **Map:** Industrial Zone (Small version - "The Factory" only)
*   **Game Loop:** Spawn -> Loot -> Fight/Sneak -> Extract
*   **Operators:** 3 Basic Classes (Assault, Scout, Support)
*   **Weapons:** 
    *   AR: AK-47, M4A1
    *   SMG: MP5
    *   Sidearm: Glock 17
*   **Enemies:** Basic AI (Patrol behavior only)
*   **Inventory:** Grid system, basic drag-and-drop
*   **Metagame:** Stash, Basic Vendor (Sell only)

### Features Excluded (For Beta)
*   Quest System
*   Crafting/Modding
*   complex AI behaviors
*   Friends/Party System
*   Monetization Store

---

## 🚀 Beta Scope (Soft Launch)

**Objective:** Validate economy, retention, and progression.

### Features Added
*   **Map:** Industrial Zone (Full) + Early Urban Zone
*   **Operators:** Added Tank and Specialist (Total 5)
*   **Weapons:** Added Shotguns, Snipers, DMRs
*   **Systems:**
    *   Gunsmith (Weapon modding)
    *   Market (Trading with NPCs)
    *   Quests (Daily + Main Story Ch.1)
    *   Wounds/Status Effects
*   **Social:** Party System, Friend List

---

## 📦 Feature Comparison Matrix

| Feature Category | Prototype |    Alpha    |          Beta          |    Launch     |
| :--------------- | :-------: | :---------: | :--------------------: | :-----------: |
| **Maps**         |  Greybox  | 1 (Partial) | 1 (Full) + 1 (Partial) |    3 Maps     |
| **Operators**    | 1 (Dummy) |      3      |           5            |      8+       |
| **Weapons**      |     2     |      5      |          15+           |      30+      |
| **AI Types**     |  Static   |   Patrol    |    Flanking, Cover     | Bosses, Elite |
| **Loot System**  |  Random   |   Tables    |        Dynamic         |  Event-based  |
| **Questing**     |     ❌     |      ❌      |         Basic          |   Campaign    |
| **Progression**  |  Session  |    Wipe     |       Persistent       |    Seasons    |
| **Monetization** |     ❌     |      ❌      |       Test Store       |  Full Store   |

---

## 🛑 Cut Content (Backlog)

*   **Vehicles:** Deferred to Year 2
*   **Clan System:** Deferred to Post-Launch
*   **Weather System:** Deferred to First Major Update
*   **Spectator Mode:** Deferred to esports update

---

---

## 📝 Document Ownership & Changelog

| Role            | Owner              | Approver           |
| :-------------- | :----------------- | :----------------- |
| **Author**      | Lead Producer      | Executive Producer |
| **Tech Review** | Technical Director | CTO                |

**Recent Changes:**
*   **v1.1 (2026-02-09):** Refined Milestones with specific deliverable targets and dependencies.
*   **v1.0 (2026-02-07):** Initial MVP definition.

---

**[← Back to Project Scope](./NonGoals.md)** | **[Index](../README.md)** | **[Next: Risk Analysis →](./Risks.md)**
