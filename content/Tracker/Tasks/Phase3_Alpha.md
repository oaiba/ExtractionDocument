---
title: 'Phase 3: Alpha (Content Production)'
type: docs
weight: 30
---

# Phase 2: Content Creation — July to September 2026

**Objective:** Inject substantial core content: Full roster Operators, Expansive Arsenal, Map art polishing, polished UI/UX experiences, and preliminary Economy layers. **Milestones:** M3 — Alpha Internal (End of Month 5), M4 — Beta Closed (End of Month 7)

> **Note:** July tasks are detailed deeply; August-September remain intentionally outlined, awaiting expansion pending M2 milestone passage.

***

## Month 5 — July 2026: Operators & UI

***

### Week 19-20: Operator System Implementation

***

<details>

<summary>{{&#x3C; badge content="Not Started" color="gray" >}} {{&#x3C; badge content="Critical" color="red" >}} DOC-014: Complete GDD — Operator Classes &#x26; Abilities (Alpha Trio)</summary>

| Field      | Value                                                                                                                                                                                                                                                      |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Difficulty | Hard                                                                                                                                                                                                                                                       |
| Estimate   | 3 days                                                                                                                                                                                                                                                     |
| Owner      | Game Designer                                                                                                                                                                                                                                              |
| Output     | Finalize CharacterSystem.md and the specific Operators documents for the Assault, Scout, and Support archetypes: detailing stats, unique abilities, and strict cooldown parameters                                                                         |
| Refs       | [GDD\_Design/Characters/](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/README.md), [Gameplay/CharacterSystem.md](https://github.com/oaiba/ExtractionDocument/blob/main/content/Tracker/Gameplay/CharacterSystem.md) |

</details>

***

<details>

<summary>{{&#x3C; badge content="Not Started" color="gray" >}} {{&#x3C; badge content="Critical" color="red" >}} TASK-019: Implement Operator Class System (3 Alpha Operators)</summary>

| Field        | Value                                                                                                                                                                                                                                                      |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Difficulty   | Very Hard                                                                                                                                                                                                                                                  |
| Risk         | High — Ability system balance invariably requires multiple intensive iteration cycles; carries significant scope creep risk                                                                                                                                |
| Estimate     | 10 days                                                                                                                                                                                                                                                    |
| Owner        | Senior Programmer + Game Designer                                                                                                                                                                                                                          |
| Dependencies | DOC-014, TASK-003                                                                                                                                                                                                                                          |
| Review       | `[ ]` All 3 Operators spawn bearing correct stats `[ ]` Unique abilities trigger and activate correctly `[ ]` Cooldown timers sync accurately across target networks `[ ]` Comprehensive balance playtest conducted                                        |
| Refs         | [Gameplay/CharacterSystem.md](https://github.com/oaiba/ExtractionDocument/blob/main/content/Tracker/Gameplay/CharacterSystem.md), [GDD\_Design/Characters/](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Characters/README.md) |

**Sub-tasks:**

* Construct foundation `UOperatorAbility` class and integrated Cooldown manager
* Implement Assault ability: Combat Stim (Applying speed boost + damage boost for 10s window)
* Implement Scout ability: UAV Scan (Highlight enemy signatures within set operational range)
* Implement Support ability: Healing Drone (Deploy physical drone to emit healing aura for teammates)
* Design and integrate the pre-match Operator selection UI screen
* Ensure robust network replication of complex ability state effects

</details>

***

### Week 21-22: Weapon Expansion & Attachments

***

<details>

<summary>{{&#x3C; badge content="Not Started" color="gray" >}} {{&#x3C; badge content="High" color="orange" >}} DOC-015: Complete GDD — Full Weapon Roster &#x26; Attachment System</summary>

| Field      | Value                                                                                                                                                                                           |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Difficulty | Medium                                                                                                                                                                                          |
| Estimate   | 2 days                                                                                                                                                                                          |
| Owner      | Game Designer                                                                                                                                                                                   |
| Output     | Updated WeaponSystem.md reflecting expansion specifications for 15+ weapons alongside intricate attachment system logic design                                                                  |
| Refs       | [Gameplay/WeaponSystem.md](https://github.com/oaiba/ExtractionDocument/blob/main/content/Tracker/Gameplay/WeaponSystem.md), [GDD\_Design/Combat/Weapons.md](../../gdd_design/combat/weapons/index.html) |

</details>

***

<details>

<summary>{{&#x3C; badge content="Not Started" color="gray" >}} {{&#x3C; badge content="High" color="orange" >}} TASK-020: Implement 10+ Additional Weapons</summary>

| Field        | Value                                                                                                                                                              |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Difficulty   | Medium                                                                                                                                                             |
| Risk         | Medium — Expansive arsenals require careful balancing; highly susceptible to power creep issues                                                                    |
| Estimate     | 7 days                                                                                                                                                             |
| Owner        | Programmer + Game Designer                                                                                                                                         |
| Dependencies | DOC-015, TASK-006                                                                                                                                                  |
| Review       | `[ ]` New weapons appropriately load data from target DataTables `[ ]` Initial rough balance pass verified `[ ]` Dedicated QA test sequence passes without crashes |
| Refs         | [Gameplay/WeaponSystem.md](https://github.com/oaiba/ExtractionDocument/blob/main/content/Tracker/Gameplay/WeaponSystem.md)                                         |

</details>

***

### Week 23-24: HUD & Main Menu UI

***

<details>

<summary>{{&#x3C; badge content="Not Started" color="gray" >}} {{&#x3C; badge content="High" color="orange" >}} DOC-016: Complete GDD — UI/UX Screens Specification</summary>

| Field      | Value                                                                                                                                                                                                                                                                                                                |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Difficulty | Medium                                                                                                                                                                                                                                                                                                               |
| Estimate   | 3 days                                                                                                                                                                                                                                                                                                               |
| Owner      | UI/UX Designer                                                                                                                                                                                                                                                                                                       |
| Output     | Finalize UISystem.md including high-fidelity wireframes encompassing: Main Menu, combat HUD, full Inventory screen setup, and final Post-match results screen                                                                                                                                                        |
| Refs       | [Systems/UISystem.md](https://github.com/oaiba/ExtractionDocument/blob/main/content/Tracker/Systems/UISystem.md), [GDD\_Design/UI\_UX/](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/UI_UX/README.md), [GDD\_Design/Visuals/UserInterface.md](../../gdd_design/visuals/userinterface/index.html) |

</details>

***

<details>

<summary>{{&#x3C; badge content="Not Started" color="gray" >}} {{&#x3C; badge content="High" color="orange" >}} TASK-021: Implement In-Game HUD</summary>

| Field        | Value                                                                                                                                                                                                                             |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Difficulty   | Medium                                                                                                                                                                                                                            |
| Risk         | Low                                                                                                                                                                                                                               |
| Estimate     | 5 days                                                                                                                                                                                                                            |
| Owner        | UI Programmer                                                                                                                                                                                                                     |
| Dependencies | DOC-016                                                                                                                                                                                                                           |
| Review       | `[ ]` HP/Armor bars reflect correct persistent data `[ ]` Minimap displays properly `[ ]` Functional active ammo counters `[ ]` Extraction timers distinctly visualize when player occupies zone                                  |
| Refs         | [Systems/UISystem.md](https://github.com/oaiba/ExtractionDocument/blob/main/content/Tracker/Systems/UISystem.md), [GDD\_Design/UI\_UX/](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/UI_UX/README.md) |

</details>

***

<details>

<summary>{{&#x3C; badge content="Not Started" color="gray" >}} {{&#x3C; badge content="High" color="orange" >}} TASK-022: Implement Main Menu &#x26; Operator Selection</summary>

| Field        | Value                                                                                                                            |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| Difficulty   | Medium                                                                                                                           |
| Risk         | Low                                                                                                                              |
| Estimate     | 5 days                                                                                                                           |
| Owner        | UI Programmer                                                                                                                    |
| Dependencies | DOC-016, TASK-019                                                                                                                |
| Review       | `[ ]` Main menu screens navigate cleanly `[ ]` Operator selection locks properly `[ ]` Global settings options easily accessible |
| Refs         | [Systems/UISystem.md](https://github.com/oaiba/ExtractionDocument/blob/main/content/Tracker/Systems/UISystem.md)                 |

</details>

***

<details>

<summary>{{&#x3C; badge content="Not Started" color="gray" >}} {{&#x3C; badge content="Critical" color="red" >}} TEST-004: Alpha Internal (M3) Review</summary>

| Field      | Value                                                                                                                                                                                                                                                            |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Difficulty | Medium                                                                                                                                                                                                                                                           |
| Risk       | High                                                                                                                                                                                                                                                             |
| Estimate   | 3 days                                                                                                                                                                                                                                                           |
| Owner      | Team Lead + Dedicated QA                                                                                                                                                                                                                                         |
| Review     | `[ ]` Map fully operational utilizing basic art pass `[ ]` All 3 feature Operators playable effectively `[ ]` Arsenal confirms 10+ Weapons functional `[ ]` Complete on-screen HUD `[ ]` Full internal team playtest over a 1-week period completes successfully |
| Refs       | [ProjectScope/MVP.md](../../gdd_design/projectscope/mvp/index.html)                                                                                                                                                                                                      |

</details>

***

## Month 6 — August 2026: Economy, Progression & Bug Fixes \[OUTLINE]

> Intended scope details to be firmly added post M3 clearance.

**Key Tasks (Outline):**

* DOC-017: GDD — Progression System Architecture (XP rules, leveling curves, specific unlocks)
* DOC-018: GDD — Global Economy System (multi-currency handling, vendor NPC stock rules, stash limits)
* TASK-023: Implement Game Progression System (XP tracking, strict Level gates, dynamic Unlock rewards)
* TASK-024: Implement Match Economy (Backend Credits logic, Vendor NPC interactions, persistent player Stash)
* TASK-025: Implement Core Quest System (Focusing explicitly on Alpha quests: simple daily contracts)
* TASK-026: Map 1 — Full Art Pass (Overhauling 'Industrial Zone': finalize detailed meshes, materials pass, comprehensive lighting setups)
* TEST-005: Closed Beta infrastructure readiness preparation (Scale 50 testers → 100, finalize telemetry tracking system setup)

***

## Month 7 — September 2026: Social Systems & Beta Readiness \[OUTLINE]

**Key Tasks (Outline):**

* DOC-019: GDD — In-depth Squad System protocols & corresponding Matchmaking logic
* TASK-027: Squad System implementation (Develop 3-player squad linking, stable invite pipelines, coordinated squad drop matchmaking)
* TASK-028: Persistent Matchmaking backend implementation (utilizing EOS services)
* TASK-029: Baseline Anti-cheat deployment (hardening aggressive server-validation logic hooks)
* TASK-030: Holistic Performance optimization passes (Directly targeting stringent mobile metrics)
* TEST-006: Milestone M4 — Official Closed Beta Launch Readiness Evaluation

***
