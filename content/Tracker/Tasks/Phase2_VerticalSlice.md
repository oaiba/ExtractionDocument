---
title: "Phase 2: Vertical Slice"
type: docs
weight: 20
---

### Month 3 — May 2026:
Inventory, Loot & AI

**Monthly Goal:** Establish functional grid inventory, functional loot generation systems, and fundamental AI routines to test the comprehensive gameplay loop.

---

#### Week 9-10 — April 28 to May 09, 2026: Inventory System

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>DOC-009: Complete GDD — Inventory & Item System</b></summary>

| Field | Value |
|---|---|
| Difficulty | Hard |
| Estimate | 3 days |
| Owner | Game Designer |
| Output | Detailed InventorySystem.md and Items.md: grid parameters, item types, specific weight values, and slot restriction rules |
| Refs | [Gameplay/InventorySystem.md](../Gameplay/InventorySystem.md), [GDD_Design/Inventory_System/](../../GDD_Design/Inventory_System/), [GDD_Design/Combat/Items.md](../../GDD_Design/Combat/Items.md) |

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>TASK-012: Implement UInventoryComponent (Grid-based)</b></summary>

| Field | Value |
|---|---|
| Difficulty | Very Hard |
| Risk | High — Grid logic is intrinsically complex; bugs related to item overlaps and invalid placements are notoriously difficult to resolve later |
| Estimate | 6 days |
| Owner | Senior Programmer |
| Dependencies | DOC-009 |
| Review | `[ ]` Correct item insertion/removal  `[ ]` Exact overlap detection  `[ ]` Weight limit tracking works  `[ ]` Secure container functions properly  `[ ]` Code review pass  `[ ]` QA stress test completion |
| Refs | [Gameplay/InventorySystem.md](../Gameplay/InventorySystem.md), [GDD_Design/Combat/Items.md](../../GDD_Design/Combat/Items.md) |

**Description:**
- Build grid-based inventory mechanics (N x M cell layout)
- Support items occupying multiple spaces (e.g., 1x1, 1x2, 2x3 configurations)
- Implement 90° item rotation logic
- Core grid functions: Add, remove, and relocate internally
- Overarching weight tracking system subject to carry limits
- Dedicated secure container logic (items retained upon death)
- Define fundamental `FItemData` structure: ItemID, Size parameters, Weight, Rarity tier, Base Stats

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="High" color="orange" >}} <b>TASK-013: Implement Inventory UI (Widget)</b></summary>

| Field | Value |
|---|---|
| Difficulty | Hard |
| Risk | Medium — Complex UI but does not strictly block underlying core gameplay testing |
| Estimate | 5 days |
| Owner | UI Programmer |
| Dependencies | TASK-012, DOC-009 |
| Review | `[ ]` Drag-and-drop mechanics function  `[ ]` Tooltips accurately display item data  `[ ]` Transfers between distinct inventories successful  `[ ]` Mobile-friendly interaction test |
| Refs | [Systems/UISystem.md](../Systems/UISystem.md), [GDD_Design/UI_UX/](../../GDD_Design/UI_UX/), [GDD_Design/Inventory_System/](../../GDD_Design/Inventory_System/) |

**Description:**
- Develop base widgets for the player inventory screen and external loot containers
- Implement functional Drag-and-drop utilizing UMG frameworks
- Implement context-sensitive item tooltips on hover
- Build system for transferring items between the player grid and container grid
- Global weight capacity indicator
- Emphasize functional implementation over final art for now

</details>

---

#### Week 11-12 — May 12 to May 23, 2026: Loot System & Item Database

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="High" color="orange" >}} <b>DOC-010: Complete GDD — Loot Tables & Rarity System</b></summary>

| Field | Value |
|---|---|
| Difficulty | Medium |
| Estimate | 2 days |
| Owner | Game Designer |
| Output | Finalize loot tables representing the Alpha map, assign specific rarity weights, and detail zone-based distribution rules |
| Refs | [Systems/MapSystem.md](../Systems/MapSystem.md), [GDD_Design/Inventory_System/](../../GDD_Design/Inventory_System/), [GDD_Design/World/MapDesign.md](../../GDD_Design/World/MapDesign.md) |

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="High" color="orange" >}} <b>TASK-014: Implement Item Database & Loot System</b></summary>

| Field | Value |
|---|---|
| Difficulty | Hard |
| Risk | Medium — Loot economy balance is a critical gameplay risk; requires extensive iterative playtesting |
| Estimate | 5 days |
| Owner | Programmer + Game Designer |
| Dependencies | DOC-010, TASK-012 |
| Review | `[ ]` Items correctly spawn in assigned zones  `[ ]` Rarity weighting probabilities function accurately  `[ ]` Container generation eliminates empty containers  `[ ]` Full inventory insertion integration |
| Refs | [Systems/MapSystem.md](../Systems/MapSystem.md), [GDD_Design/Combat/Items.md](../../GDD_Design/Combat/Items.md) |

**Description:**
- Build Item Database using DataTables (ItemID, Base Name, Category Type, Rarity Tier, Stats, Loot Probability)
- Develop `ALootContainer` actor logic: handle player interaction, and generate loot payload on container open
- Build logic for zone-based loot spawning (e.g., High Risk zones yield Rare loot, Low Risk yields Common)
- Implement dynamic, heavily weighted loot tables based on rarity values
- Ground item pickup logic → dynamically check available grid space → add item to inventory or reject/drop it back

</details>

---

#### Week 13-14 — May 26 to June 06, 2026: AI System

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>DOC-011: Complete GDD — AI Behavior & Enemy Design</b></summary>

| Field | Value |
|---|---|
| Difficulty | Hard |
| Estimate | 3 days |
| Owner | Game Designer + AI Programmer |
| Output | Detailed AISystem.md and EnemyBehavior.md: precise behavior states, defined perception ranges, and combat stats required for Alpha Scav enemies |
| Refs | [AI/AISystem.md](../AI/AISystem.md), [GDD_Design/AI/EnemyBehavior.md](../../GDD_Design/AI/EnemyBehavior.md) |

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>TASK-015: Implement AI Character & Controller (Scav)</b></summary>

| Field | Value |
|---|---|
| Difficulty | Very Hard |
| Risk | High — AI is a highly complex feature; tuning the behavior tree requires significant dedicated time |
| Estimate | 8 days |
| Owner | AI Programmer |
| Dependencies | DOC-011, TASK-003 |
| Review | `[ ]` Routine patrol follows waypoints accurately  `[ ]` Player detection works within specific ranges  `[ ]` Chase state triggers properly  `[ ]` Active combat state (firing accurately at player)  `[ ]` Utilizes cover logic  `[ ]` Code review pass |
| Refs | [AI/AISystem.md](../AI/AISystem.md), [GDD_Design/AI/EnemyBehavior.md](../../GDD_Design/AI/EnemyBehavior.md) |

**Description:**
- Inherit `AExtractionAICharacter` from base `AExtractionCharacter`
- Setup primary `AExtractionAIController` with accompanying Behavior Tree parameters
- Define Blackboard keys: Target Actor, LastKnownLocation vector, IsAlerted boolean
- Develop specific enemy behaviors:
- Base Patrol (waypoint-driven routes)
- Investigate anomaly (triggered by noise/sight)
- Chase target (within defined detection cone/range)
- Combat execution (shoot at player, reposition, take basic cover)
- Broaden audio cues: Shout specific callouts
- Structure AI Perception: Sight variables (cone angle, distance), Sound variables (radius)
- Hook up AI Scav variables to stats pulled directly from the DOC-011 DataTable

</details>

---

### Month 4 — June 2026: Extraction Loop, Prototype Map & M2 Milestone

**Monthly Goal:** Finalize the core Extraction mechanic, deliver a playable end-to-end prototype map, and successfully clear Milestone M2 — Vertical Slice.

---

#### Week 15-16 — June 09 to June 20, 2026: Extraction Zone & Match Flow

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>DOC-012: Complete GDD — Extraction Zone & Match Events</b></summary>

| Field | Value |
|---|---|
| Difficulty | Medium |
| Estimate | 2 days |
| Owner | Game Designer |
| Output | Updated MapSystem.md and CoreGameplay.md explicitly defining rules for extraction zones, contamination spreading mechanics, and logic for supply drops |
| Refs | [Systems/MapSystem.md](../Systems/MapSystem.md), [GDD_Design/World/MapDesign.md](../../GDD_Design/World/MapDesign.md), [GDD_Design/GameDesign/CoreGameplay.md](../../GDD_Design/GameDesign/CoreGameplay.md) |

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>TASK-016: Implement AExtractionZone</b></summary>

| Field | Value |
|---|---|
| Difficulty | Medium |
| Risk | Medium — Event interrupt logic (e.g., taking hit damage while attempting extraction) frequently triggers problematic edge cases |
| Estimate | 4 days |
| Owner | Programmer |
| Dependencies | DOC-012, TASK-011 |
| Review | `[ ]` Proper Zone activation delays  `[ ]` Accurate extraction countdown timers  `[ ]` Player successfully extracts state change  `[ ]` Immediate timer interruption when hit  `[ ]` Code review pass |
| Refs | [Systems/MapSystem.md](../Systems/MapSystem.md), [GDD_Design/GameDesign/CoreGameplay.md](../../GDD_Design/GameDesign/CoreGameplay.md) |

**Description:**
- Create the `AExtractionZone` base actor
- Differentiate Zone types: Always Open, Conditional (Paid entry), Chance-based (Random open probability)
- Trigger activation parameters: purely Timer-based
- Core extraction flow: 30-second countdown timer, hard-interruptible if the player sustains damage
- Define player tracking logic: Overlap event → initiate timer → server confirms extraction result
- Route server broadcast event: `OnPlayerExtracted` → GameMode handles and rewards result

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Medium" color="yellow" >}} <b>TASK-017: Implement Supply Drop & Match Events</b></summary>

| Field | Value |
|---|---|
| Difficulty | Medium |
| Risk | Low — Categorized as nice-to-have for the initial prototype; viable for deferral if timelines tighten |
| Estimate | 3 days |
| Owner | Programmer |
| Dependencies | TASK-016 |
| Review | `[ ]` Supply drops correctly spawn at predefined locations  `[ ]` Contained loot properly populates  `[ ]` Server-wide audio/UI event announcement broadcast |
| Refs | [GDD_Design/GameDesign/CoreGameplay.md](../../GDD_Design/GameDesign/CoreGameplay.md) |

</details>

---

#### Week 17-18 — June 23 to July 04, 2026: Prototype Map & M2 Review

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>DOC-013: Complete GDD — Alpha Map Design Document</b></summary>

| Field | Value |
|---|---|
| Difficulty | Medium |
| Estimate | 3 days |
| Owner | Level Designer + Game Designer |
| Output | Final MapDesign.md specifically for the "Industrial Zone": detailed layout, tier-based zone division, exact extraction points, designated AI spawn locations, and a comprehensive loot density heat-map |
| Refs | [GDD_Design/World/MapDesign.md](../../GDD_Design/World/MapDesign.md), [Systems/MapSystem.md](../Systems/MapSystem.md) |

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>TASK-018: Build Prototype Map "Industrial Zone" (Greybox)</b></summary>

| Field | Value |
|---|---|
| Difficulty | Hard |
| Risk | High — The map represents the direct environment players test; structural layout errors directly result in flawed gameplay feedback |
| Estimate | 8 days |
| Owner | Level Designer |
| Dependencies | DOC-013, TASK-016, TASK-014, TASK-015 |
| Review | `[ ]` Map compiles flawlessly  `[ ]` Adequate player spawn points  `[ ]` 3 Extraction Zones accurately placed  `[ ]` AI spawn points function under test  `[ ]` Loot spawns correlate to density map  `[ ]` Full internal playtest pass |
| Refs | [GDD_Design/World/MapDesign.md](../../GDD_Design/World/MapDesign.md), [ProjectScope/MVP.md](../../GDD_Design/ProjectScope/MVP.md) |

**Description:**
- Establish base dimensions: ~500x500m (utilizing simplified topology)
- Strictly employ Greybox materials; defer full art passes until later development phases
- Position 3 core Extraction Zones: 1 Always Open, 1 Conditional, 1 Chance based
- Layout High-density loot zones against designated low-risk transit routes
- Set strategic spawn points for players (distributed along map boundaries)
- Assign complex AI Scav spawn zones (including basic patrol routes)
- Ensure accurate collision layers; rigorously test for map holes or geometry stuck spots

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>TEST-003: Milestone M2 — Vertical Slice Review</b></summary>

| Field | Value |
|---|---|
| Difficulty | Medium |
| Risk | High — M2 acts as the fundamental gate dictating project progression to Phase 2 |
| Estimate | 3 days |
| Owner | Team Lead + Project Stakeholders |
| Dependencies | TASK-018 and all preceding Phase 1 TASKs |
| Review | `[ ]` Successful full match sequence: Spawn → Loot → Combat → Extract  `[ ]` AI Scavs functional and lethal  `[ ]` 2 connected players without technical crashes  `[ ]` Fully functional inventory interaction  `[ ]` Baseline performance maintains > 30 FPS on minimum target devices  `[ ]` Official Stakeholder sign-off |
| Refs | [ProjectScope/MVP.md](../../GDD_Design/ProjectScope/MVP.md), [DevelopmentRoadmap.md](../Core/DevelopmentRoadmap.md) |

</details>

---

