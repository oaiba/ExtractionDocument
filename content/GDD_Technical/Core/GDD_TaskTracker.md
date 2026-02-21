---
title: "GDD Task Tracker"
type: docs
---

# GDD Task Tracker

> **Purpose:** A comprehensive project-wide task tracking document broken down by Phase, Month, and Week. Every task includes: Priority, Difficulty, Risk, Estimate, Status, Review checklist, and Reference Documents.
>
> **Core Principle:** GDD Doc Tasks (DOC-XXX) are strict prerequisites for Feature Tasks (TASK-XXX). Implementation must not begin until the associated GDD section is officially approved.

---

## Status Dashboard

| Field | Value |
|---|---|
| Project | Extraction Shooter |
| Current Phase | Phase 1: Core Development |
| Current Sprint | Sprint 0 — Project Setup |
| Start Date | 2026-03-02 |
| Last Updated | 2026-02-21 |
| Team Size | TBD |

---

## Legend

### Priority
| Value | Meaning |
|---|---|
| Critical | Blocker — must be completed before anything else can proceed |
| High | Core feature — directly impacts upcoming milestones |
| Medium | Important but does not block progress |
| Low | Nice-to-have, can be deferred if necessary |

### Difficulty
| Value | Meaning |
|---|---|
| Very Easy | Routine task, no research required |
| Easy | Familiar implementation, low technical risk |
| Medium | Requires planning, presents some risks |
| Hard | Complex implementation, requires deep expertise |
| Very Hard | R&D level, high risk, requires prototyping first |

### Risk Level
| Value | Meaning |
|---|---|
| Critical | Could delay the entire project |
| High | Could impact milestones if realized |
| Medium | Manageable within the current sprint |
| Low | Minimal impact |

### Status
| Value | Meaning |
|---|---|
| Not Started | Work has not begun |
| In Progress | Currently being worked on |
| Blocked | Blocked by an external dependency |
| In Review | Pending review or QA testing |
| Done | Fully completed and verified |
| Deferred | Pushed to a future phase or sprint |

### Task Type
| Prefix | Meaning |
|---|---|
| DOC-XXX | GDD Document task — must be completed before the associated TASK |
| TASK-XXX | Feature implementation task |
| INFRA-XXX | Infrastructure / DevOps task |
| TEST-XXX | Testing / QA milestone review task |

---

## Phase 1: Core Development — March to June 2026

**Objective:** Build a complete technical foundation, culminating in a Playable Prototype by the end of the phase.
**Milestones:** M1 — Prototype (End of Month 2), M2 — Vertical Slice (End of Month 4)
**Duration:** 4 months (March — June 2026)

---

### Month 1 — March 2026: Foundation & Project Setup

**Monthly Goal:** Establish all project infrastructure, development environments, coding standards, and begin the Core Character System.

---

#### Week 1 — March 02 to March 07, 2026: Project Infrastructure

**Sprint Goal:** Project compiles and runs successfully on all team members' machines.

---

##### INFRA-001: Initialize UE5 Project

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Easy |
| Risk | Medium — Choosing the wrong mobile template could impact future structure |
| Estimate | 1 day |
| Status | Not Started |
| Owner | Tech Lead |
| Review | [ ] Project builds successfully  [ ] Opens on all team machines  [ ] CI pass |
| Refs | [Architecture.md](../Core/Architecture.md), [UE5 Documentation](https://docs.unrealengine.com/5.0/en-US/) |

**Description:**
- Create a UE5 project using the Blank C++ template (avoid default mobile templates)
- Configure Target Platforms: PC (Development), Android (Future)
- Setup project directory structure: Source/, Content/, Config/
- Commit the initial template build

---

##### INFRA-002: Setup Version Control (Git + LFS)

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Easy |
| Risk | Low |
| Estimate | 1 day |
| Status | Not Started |
| Owner | Tech Lead / DevOps |
| Review | [ ] .gitignore correct for UE5  [ ] LFS tracks .uasset & .umap  [ ] Push/Pull test pass |
| Refs | [CodingStandards.md](../Core/CodingStandards.md) |

**Description:**
- Initialize Git repository
- Configure .gitignore for UE5 (Binaries, Intermediate, DerivedDataCache, Saved)
- Install and configure Git LFS for .uasset, .umap, .wav, .png
- Document branching strategy: main / develop / feature/*

---

##### INFRA-003: Setup Build Pipeline (Basic CI/CD)

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Medium |
| Risk | Medium — Continuous CI failures will slow down workflow |
| Estimate | 2 days |
| Status | Not Started |
| Owner | DevOps |
| Review | [ ] Auto-builds trigger on push  [ ] Build reports sent to Slack/Discord |
| Refs | [Architecture.md](../Core/Architecture.md) |

**Description:**
- Setup GitHub Actions or Jenkins
- Trigger: build and compile C++ on push to the develop branch
- Report build status (Success / Fail + logs)
- Packaging is not required yet; only a successful compile pass is needed

---

##### DOC-001: Complete GDD — Coding Standards & Project Structure

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Easy |
| Estimate | 1 day |
| Owner | Tech Lead |
| Status | Not Started |
| Output | Fully documented CodingStandards.md, reviewed and approved by the entire team |
| Refs | [CodingStandards.md](../Core/CodingStandards.md), [Architecture.md](../Core/Architecture.md) |

**Description:**
- Review and finalize naming conventions (C++, Blueprints, Assets)
- Confirm module architecture layers (Layer 0, 1, 2)
- Document the exact folder structure within Content/
- Distribute for team-wide review

---

#### Week 2 — March 10 to March 14, 2026: Architecture & Module Setup

**Sprint Goal:** Clean module architecture, GameplayTags system ready, base classes available for derivation.

---

##### DOC-002: Complete GDD — Detailed Architecture

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Easy |
| Estimate | 1 day |
| Owner | Tech Lead |
| Status | Not Started |
| Output | Architecture.md features a clear class hierarchy and is ready for development |
| Refs | [Architecture.md](../Core/Architecture.md), [GDD_Technical/_index.md](../_index.md) |

**Description:**
- Confirm core class hierarchy: ExtractionCharacter → ExtractionPlayerCharacter / ExtractionAICharacter
- Clearly document module dependencies
- Validate tech stack choices (UE5.4+, EOS, PostgreSQL/Redis)

---

##### TASK-001: Implement Module Structure & GameplayTags

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Medium |
| Risk | High — GameplayTags act as the system backbone; early mistakes are extremely difficult to refactor |
| Estimate | 3 days |
| Status | Not Started |
| Owner | Tech Lead |
| Dependencies | DOC-002, INFRA-001 |
| Review | [ ] Modules compile without errors  [ ] GameplayTag catalog documented  [ ] Code review pass |
| Refs | [Architecture.md](../Core/Architecture.md), [CodingStandards.md](../CodingStandards.md) |

**Description:**
- Create the `ExtractionGame` runtime module
- Configure `ExtractionGame.Build.cs` with the correct dependencies
- Setup primary GameplayTags:
  - `Extraction.Character.*` — character states
  - `Extraction.Weapon.*` — weapon states
  - `Extraction.UI.*` — UI states
  - `Extraction.Gameplay.*` — general game states
- Create the base `UExtractionGameInstance`
- Document the tag catalog in CodingStandards.md

---

##### TASK-002: Implement Base UE5 Skeleton (GameMode, GameState, PlayerState)

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Easy |
| Risk | Low |
| Estimate | 2 days |
| Status | Not Started |
| Owner | Programmer |
| Dependencies | TASK-001 |
| Review | [ ] Classes compile successfully  [ ] Blueprint children easily created  [ ] Code review pass |
| Refs | [Architecture.md](../Core/Architecture.md), [Core/NetworkingSystem.md](../Core/NetworkingSystem.md) |

**Description:**
- Create `AExtractionGameMode` (derived from AGameModeBase)
- Create `AExtractionGameState` (derived from AGameStateBase)
- Create `AExtractionPlayerState` (derived from APlayerState)
- Create `AExtractionPlayerController` (derived from APlayerController)
- Stub out basic interfaces for match flow

---

#### Week 3 — March 17 to March 21, 2026: Character System

**Sprint Goal:** Character can move, crouch, and take damage within PIE (Play In Editor).

---

##### DOC-003: Complete GDD — Detailed Character System

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Medium |
| Estimate | 2 days |
| Owner | Game Designer + Tech Lead |
| Status | Not Started |
| Output | CharacterSystem.md includes complete stats (HP, Speed, Stamina), movement specs, and animation states |
| Refs | [Gameplay/CharacterSystem.md](../Gameplay/CharacterSystem.md), [GDD_Design/Characters/](../../GDD_Design/Characters/), [GDD_Design/GameDesign/CoreGameplay.md](../../GDD_Design/GameDesign/CoreGameplay.md) |

**Description:**
- Finalize base stats for each Operator archetype (HP, Speed, Stamina, Carry Weight)
- Define movement states: Walk, Sprint, Crouch, ADS
- Define the animation state machine design
- Document damage location multipliers (Head, Thorax, Stomach, Limbs)

---

##### TASK-003: Implement AExtractionCharacter Base Class

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Medium |
| Risk | High — Errors in the base character class will ripple throughout the entire system |
| Estimate | 3 days |
| Status | Not Started |
| Owner | Senior Programmer |
| Dependencies | DOC-003, TASK-002 |
| Review | [ ] Character spawns correctly  [ ] Movement functional  [ ] Animations blend properly  [ ] Code review pass |
| Refs | [Gameplay/CharacterSystem.md](../Gameplay/CharacterSystem.md), [GDD_Design/Characters/](../../GDD_Design/Characters/) |

**Description:**
- Create `AExtractionCharacter` derived from ACharacter
- Implement core movement logic (walk, sprint, crouch)
- Implement `UHealthComponent`:
  - HP tracking and replication
  - Damage calculation utilizing location multipliers
  - Death handling logic and `OnDead` delegate
- Implement `UStaminaComponent`:
  - Stamina regeneration and drain mechanics
  - Sprint interruption when stamina is depleted
- Integrate Character Stats DataTable references

---

##### TASK-004: Implement UMobileInputComponent & Top-Down Input

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Hard |
| Risk | High — Top-down input abstraction is complex and requires rigorous testing on both PC and mobile targets |
| Estimate | 4 days |
| Status | Not Started |
| Owner | Senior Programmer |
| Dependencies | DOC-003, TASK-003 |
| Review | [ ] WASD / joystick movement works  [ ] Mouse aiming works  [ ] Aim assist functions properly  [ ] Code review pass |
| Refs | [Gameplay/ControlSystem.md](../Gameplay/ControlSystem.md), [GDD_Design/GameDesign/Controls.md](../../GDD_Design/GameDesign/Controls.md) |

**Description:**
- Implement the Enhanced Input system
- Map Actions: Move, Aim, Fire, Reload, Interact, Crouch
- Implement top-down mouse projection (raycast to ground plane)
- Stub out virtual joystick logic for mobile (full implementation later)
- Implement basic aim assist: snap assist with distance-based falloff

---

#### Week 4 — March 24 to March 28, 2026: Animation & End-of-Month Review

**Sprint Goal:** Character features full animation coverage, Milestone 1 review passed successfully.

---

##### DOC-004: Complete GDD — Animation State Machine

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Easy |
| Estimate | 1 day |
| Owner | Tech Artist + Game Designer |
| Status | Not Started |
| Output | Comprehensive definition of all animation states and transition rules |
| Refs | [Gameplay/CharacterSystem.md](../Gameplay/CharacterSystem.md), [GDD_Design/Visuals/ArtDirection.md](../../GDD_Design/Visuals/ArtDirection.md) |

---

##### TASK-005: Setup Animation Blueprint (Top-Down)

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Medium |
| Risk | Medium — Placeholder animations are acceptable now; the true risk lies in an incorrect ABP structure |
| Estimate | 3 days |
| Status | Not Started |
| Owner | Tech Artist / Programmer |
| Dependencies | DOC-004, TASK-003 |
| Review | [ ] Idle/Walk/Sprint blend correctly  [ ] Crouch animation active  [ ] Death animation triggers  [ ] Code review pass |
| Refs | [Gameplay/CharacterSystem.md](../Gameplay/CharacterSystem.md) |

**Description:**
- Create the primary Animation Blueprint for `ExtractionCharacter`
- Core State Machine: Idle → Walk → Sprint; Idle → Crouch
- Implement speed-based locomotion blendspaces
- Trigger death animation via the `OnDead` event
- Utilize placeholder Mannequin assets for this phase

---

##### TEST-001: End-of-Month 1 Review & Integration Test

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Easy |
| Risk | Low |
| Estimate | 1 day |
| Status | Not Started |
| Owner | Team Lead + QA |
| Dependencies | TASK-001 through TASK-005 |
| Review | [ ] All INFRA passes  [ ] Character moves correctly  [ ] CI Build succeeds  [ ] Team retrospective completed |
| Refs | [DevelopmentRoadmap.md](../Core/DevelopmentRoadmap.md), [ProjectScope/MVP.md](../../GDD_Design/ProjectScope/MVP.md) |

**Description:**
- Internal Demo: Character spawning, movement, taking damage, and dying
- Tracking missing checklist issues
- Complete Sprint retrospective
- Update DevelopmentRoadmap.md with actual statuses

---

### Month 2 — April 2026: Combat System & Networking Foundation

**Monthly Goal:** Establish a complete core combat loop (fire, hit, damage) and baseline network replication. Achieve Milestone M1 — Prototype.

---

#### Week 5 — March 31 to April 04, 2026: Weapon System Foundation

---

##### DOC-005: Complete GDD — Detailed Weapon System

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Medium |
| Estimate | 2 days |
| Owner | Game Designer |
| Status | Not Started |
| Output | WeaponSystem.md includes complete details: weapon classes, stats, ballistics, and recoil patterns for Alpha weapons (AK47, M4A1, MP5, Glock) |
| Refs | [Gameplay/WeaponSystem.md](../Gameplay/WeaponSystem.md), [GDD_Design/Combat/Weapons.md](../../GDD_Design/Combat/Weapons.md) |

---

##### TASK-006: Implement AExtractionWeapon Base Class

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Hard |
| Risk | High — The weapon system is the core gameplay loop; bugs here are difficult to debug after scaling up the arsenal |
| Estimate | 4 days |
| Status | Not Started |
| Owner | Senior Programmer |
| Dependencies | DOC-005, TASK-003 |
| Review | [ ] Firing logic works  [ ] Ammo tracked correctly  [ ] Reload functions properly  [ ] Weapon equip/unequip works  [ ] Code review pass |
| Refs | [Gameplay/WeaponSystem.md](../Gameplay/WeaponSystem.md), [GDD_Design/Combat/Weapons.md](../../GDD_Design/Combat/Weapons.md) |

**Description:**
- Create the `AExtractionWeapon` base class
- Implement fundamental firing mechanics:
  - Supported Fire modes: Semi, Auto
  - Line trace hit detection (no physical projectiles for the Alpha build)
  - Hit validation (server authority)
- Ammo system: Magazine size limits, ammo pool types
- Reload system: Animation-linked, allows for interruption
- Weapon switching configuration: primary / secondary slots
- Integrate DataTable-driven stats (damage, fire rate, effective range, recoil)

---

##### TASK-007: Implement Alpha Weapons (AK47, M4A1, MP5, Glock)

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Medium |
| Risk | Medium — Weapon balancing is the primary risk; requires multiple iteration cycles |
| Estimate | 3 days |
| Status | Not Started |
| Owner | Programmer + Game Designer |
| Dependencies | TASK-006, DOC-005 |
| Review | [ ] All 4 weapons fire using correct stats  [ ] Recoil visuals align  [ ] Damage values match DataTable specifications  [ ] QA test pass |
| Refs | [Gameplay/WeaponSystem.md](../Gameplay/WeaponSystem.md), [GDD_Design/Combat/Weapons.md](../../GDD_Design/Combat/Weapons.md) |

**Description:**
- Implement 4 Alpha weapons reading from DataTables:
  - AK-47: High damage output, severe recoil
  - M4A1: Balanced profile, highly moddable slots
  - MP5: Fast CQB focus, low armor penetration
  - Glock 17: Reliable sidearm fallback
- Utilize placeholder meshes (Standard Mannequin configurations)
- Establish visual recoil tracking to monitor mismatch issues

---

#### Week 6 — April 07 to April 11, 2026: Hit Detection & Health System

---

##### TASK-008: Implement Hit Detection & Damage System

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Hard |
| Risk | Critical — Flawed hit detection in online games is catastrophic; server validation must be robust from day one |
| Estimate | 4 days |
| Status | Not Started |
| Owner | Senior Programmer |
| Dependencies | TASK-006, TASK-003 |
| Review | [ ] Line trace correctly hits zones  [ ] Damage multipliers apply correctly (Head 2x, Thorax 1x, Limb 0.7x)  [ ] Server validates all hits  [ ] Zero false-positive test cases  [ ] Code review pass |
| Refs | [Gameplay/CharacterSystem.md](../Gameplay/CharacterSystem.md), [GDD_Design/Combat/Weapons.md](../../GDD_Design/Combat/Weapons.md) |

**Description:**
- Configure line traces using custom UE5 physics collision channels
- Implement distinct hit zone detection: Head, Thorax, Stomach, Arms, Legs
- Apply damage multipliers retrieved from DataTables
- Essential server-authoritative logic: client sends hit request, server confirms valid intersection
- Route damage to `UHealthComponent` and broadcast `OnDamageTaken`, `OnDead`
- Implement initial visual feedback: hit marker UI

---

##### DOC-006: Complete GDD — Health & Status Effect System

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Easy |
| Estimate | 1 day |
| Owner | Game Designer |
| Status | Not Started |
| Output | Health states fully defined for Alpha (HP, Death); beta states (Bleeding, Fractures) documented but queued for later implementation |
| Refs | [GDD_Design/GameDesign/CoreGameplay.md](../../GDD_Design/GameDesign/CoreGameplay.md), [Gameplay/CharacterSystem.md](../Gameplay/CharacterSystem.md) |

---

#### Week 7 — April 14 to April 18, 2026: Network Foundation

---

##### DOC-007: Complete GDD — Networking Architecture & Replication Plan

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Medium |
| Estimate | 2 days |
| Owner | Tech Lead |
| Status | Not Started |
| Output | NetworkingSystem.md features a clear replication strategy: defining server-replicated vs. locally predicted elements |
| Refs | [Core/NetworkingSystem.md](../Core/NetworkingSystem.md) |

---

##### TASK-009: Setup Dedicated Server Architecture

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Very Hard |
| Risk | Critical — Incorrect server setup will block all subsequent multiplayer feature testing |
| Estimate | 5 days |
| Status | Not Started |
| Owner | Senior Programmer + DevOps |
| Dependencies | DOC-007, TASK-002 |
| Review | [ ] Dedicated Server builds successfully  [ ] Client successfully connects to local server instance  [ ] Local ping registers < 50ms  [ ] Code review pass |
| Refs | [Core/NetworkingSystem.md](../Core/NetworkingSystem.md), [Core/Architecture.md](../Core/Architecture.md) |

**Description:**
- Configure UE5 Dedicated Server project build targets
- Separate and optimize client and server build profiles
- Implement base connection handling and session management logic
- Ensure Listen Server mode is functional for rapid local testing
- Complete the server deployment guide document

---

##### TASK-010: Implement Character & Combat Replication

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Very Hard |
| Risk | Critical — Replication bugs cause immediate desync and break gameplay; requires rigorous testing with at least 2 connected clients |
| Estimate | 5 days |
| Status | Not Started |
| Owner | Senior Programmer |
| Dependencies | TASK-009, TASK-003, TASK-008 |
| Review | [ ] Movement prediction functions smoothly  [ ] Combat events replicate correctly  [ ] Health syncs accurately  [ ] 2-client live test passes fully  [ ] Code review pass |
| Refs | [Core/NetworkingSystem.md](../Core/NetworkingSystem.md) |

**Description:**
- Replicate variables: Position, Rotation, Velocity (Client-Predicted for responsiveness)
- Replicate variables: Health, Armor levels (Strictly Server Authoritative)
- Replicate events: Weapon firing visuals/audio (Multicast RPC)
- Implement baseline lag compensation mechanisms
- Required 2-client local test: Client A shoots Client B, hit registers correctly on both screens

---

#### Week 8 — April 21 to April 25, 2026: GameMode Flow & Milestone M1

---

##### DOC-008: Complete GDD — Match Flow & Game Rules

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Easy |
| Estimate | 1 day |
| Owner | Game Designer |
| Status | Not Started |
| Output | Clear match lifecycle defined: WaitingForPlayers → InProgress → Ended |
| Refs | [GDD_Design/GameDesign/CoreGameplay.md](../../GDD_Design/GameDesign/CoreGameplay.md), [Core/Architecture.md](../Core/Architecture.md) |

---

##### TASK-011: Implement Match Flow (GameMode)

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Medium |
| Risk | Medium — Managing underlying state logic is more complex than it appears due to cross-system dependencies |
| Estimate | 3 days |
| Status | Not Started |
| Owner | Programmer |
| Dependencies | DOC-008, TASK-009 |
| Review | [ ] Proper match start/end triggers  [ ] Players appropriately spawned  [ ] Win conditions trigger correctly  [ ] Code review pass |
| Refs | [GDD_Design/GameDesign/CoreGameplay.md](../../GDD_Design/GameDesign/CoreGameplay.md) |

**Description:**
- Update `AExtractionGameMode` states: WaitingForPlayers → InProgress → Results
- Implement spawn manager using PlayerStart actors
- Implement placeholder win condition: last player alive
- Implement global match timer tracking within GameState

---

##### TEST-002: Milestone M1 — Prototype Review

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Easy |
| Risk | High — Failing this milestone necessitates immediate adjustment to the Phase 1 scope and schedule |
| Estimate | 2 days |
| Status | Not Started |
| Owner | Team Lead |
| Dependencies | All tasks from Weeks 5-7 |
| Review | [ ] 2 connected players online  [ ] Combat engagements possible  [ ] Accurate damage registration  [ ] Complete match start/end cycle  [ ] Zero critical crashes during a 30-minute play session |
| Refs | [ProjectScope/MVP.md](../../GDD_Design/ProjectScope/MVP.md), [DevelopmentRoadmap.md](../Core/DevelopmentRoadmap.md) |

---

### Month 3 — May 2026: Inventory, Loot & AI

**Monthly Goal:** Establish functional grid inventory, functional loot generation systems, and fundamental AI routines to test the comprehensive gameplay loop.

---

#### Week 9-10 — April 28 to May 09, 2026: Inventory System

---

##### DOC-009: Complete GDD — Inventory & Item System

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Hard |
| Estimate | 3 days |
| Owner | Game Designer |
| Status | Not Started |
| Output | Detailed InventorySystem.md and Items.md: grid parameters, item types, specific weight values, and slot restriction rules |
| Refs | [Gameplay/InventorySystem.md](../Gameplay/InventorySystem.md), [GDD_Design/Inventory_Gear/](../../GDD_Design/Inventory_Gear/), [GDD_Design/Combat/Items.md](../../GDD_Design/Combat/Items.md) |

---

##### TASK-012: Implement UInventoryComponent (Grid-based)

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Very Hard |
| Risk | High — Grid logic is intrinsically complex; bugs related to item overlaps and invalid placements are notoriously difficult to resolve later |
| Estimate | 6 days |
| Status | Not Started |
| Owner | Senior Programmer |
| Dependencies | DOC-009 |
| Review | [ ] Correct item insertion/removal  [ ] Exact overlap detection  [ ] Weight limit tracking works  [ ] Secure container functions properly  [ ] Code review pass  [ ] QA stress test completion |
| Refs | [Gameplay/InventorySystem.md](../Gameplay/InventorySystem.md), [GDD_Design/Combat/Items.md](../../GDD_Design/Combat/Items.md) |

**Description:**
- Build grid-based inventory mechanics (N x M cell layout)
- Support items occupying multiple spaces (e.g., 1x1, 1x2, 2x3 configurations)
- Implement 90° item rotation logic
- Core grid functions: Add, remove, and relocate internally
- Overarching weight tracking system subject to carry limits
- Dedicated secure container logic (items retained upon death)
- Define fundamental `FItemData` structure: ItemID, Size parameters, Weight, Rarity tier, Base Stats

---

##### TASK-013: Implement Inventory UI (Widget)

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Hard |
| Risk | Medium — Complex UI but does not strictly block underlying core gameplay testing |
| Estimate | 5 days |
| Status | Not Started |
| Owner | UI Programmer |
| Dependencies | TASK-012, DOC-009 |
| Review | [ ] Drag-and-drop mechanics function  [ ] Tooltips accurately display item data  [ ] Transfers between distinct inventories successful  [ ] Mobile-friendly interaction test |
| Refs | [Systems/UISystem.md](../Systems/UISystem.md), [GDD_Design/UI_UX/](../../GDD_Design/UI_UX/), [GDD_Design/Inventory_Gear/](../../GDD_Design/Inventory_Gear/) |

**Description:**
- Develop base widgets for the player inventory screen and external loot containers
- Implement functional Drag-and-drop utilizing UMG frameworks
- Implement context-sensitive item tooltips on hover
- Build system for transferring items between the player grid and container grid
- Global weight capacity indicator
- Emphasize functional implementation over final art for now

---

#### Week 11-12 — May 12 to May 23, 2026: Loot System & Item Database

---

##### DOC-010: Complete GDD — Loot Tables & Rarity System

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Medium |
| Estimate | 2 days |
| Owner | Game Designer |
| Status | Not Started |
| Output | Finalize loot tables representing the Alpha map, assign specific rarity weights, and detail zone-based distribution rules |
| Refs | [Systems/MapSystem.md](../Systems/MapSystem.md), [GDD_Design/Inventory_Gear/](../../GDD_Design/Inventory_Gear/), [GDD_Design/World/MapDesign.md](../../GDD_Design/World/MapDesign.md) |

---

##### TASK-014: Implement Item Database & Loot System

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Hard |
| Risk | Medium — Loot economy balance is a critical gameplay risk; requires extensive iterative playtesting |
| Estimate | 5 days |
| Status | Not Started |
| Owner | Programmer + Game Designer |
| Dependencies | DOC-010, TASK-012 |
| Review | [ ] Items correctly spawn in assigned zones  [ ] Rarity weighting probabilities function accurately  [ ] Container generation eliminates empty containers  [ ] Full inventory insertion integration |
| Refs | [Systems/MapSystem.md](../Systems/MapSystem.md), [GDD_Design/Combat/Items.md](../../GDD_Design/Combat/Items.md) |

**Description:**
- Build Item Database using DataTables (ItemID, Base Name, Category Type, Rarity Tier, Stats, Loot Probability)
- Develop `ALootContainer` actor logic: handle player interaction, and generate loot payload on container open
- Build logic for zone-based loot spawning (e.g., High Risk zones yield Rare loot, Low Risk yields Common)
- Implement dynamic, heavily weighted loot tables based on rarity values
- Ground item pickup logic → dynamically check available grid space → add item to inventory or reject/drop it back

---

#### Week 13-14 — May 26 to June 06, 2026: AI System

---

##### DOC-011: Complete GDD — AI Behavior & Enemy Design

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Hard |
| Estimate | 3 days |
| Owner | Game Designer + AI Programmer |
| Status | Not Started |
| Output | Detailed AISystem.md and EnemyBehavior.md: precise behavior states, defined perception ranges, and combat stats required for Alpha Scav enemies |
| Refs | [AI/AISystem.md](../AI/AISystem.md), [GDD_Design/AI/EnemyBehavior.md](../../GDD_Design/AI/EnemyBehavior.md) |

---

##### TASK-015: Implement AI Character & Controller (Scav)

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Very Hard |
| Risk | High — AI is a highly complex feature; tuning the behavior tree requires significant dedicated time |
| Estimate | 8 days |
| Status | Not Started |
| Owner | AI Programmer |
| Dependencies | DOC-011, TASK-003 |
| Review | [ ] Routine patrol follows waypoints accurately  [ ] Player detection works within specific ranges  [ ] Chase state triggers properly  [ ] Active combat state (firing accurately at player)  [ ] Utilizes cover logic  [ ] Code review pass |
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

---

### Month 4 — June 2026: Extraction Loop, Prototype Map & M2 Milestone

**Monthly Goal:** Finalize the core Extraction mechanic, deliver a playable end-to-end prototype map, and successfully clear Milestone M2 — Vertical Slice.

---

#### Week 15-16 — June 09 to June 20, 2026: Extraction Zone & Match Flow

---

##### DOC-012: Complete GDD — Extraction Zone & Match Events

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Medium |
| Estimate | 2 days |
| Owner | Game Designer |
| Status | Not Started |
| Output | Updated MapSystem.md and CoreGameplay.md explicitly defining rules for extraction zones, contamination spreading mechanics, and logic for supply drops |
| Refs | [Systems/MapSystem.md](../Systems/MapSystem.md), [GDD_Design/World/MapDesign.md](../../GDD_Design/World/MapDesign.md), [GDD_Design/GameDesign/CoreGameplay.md](../../GDD_Design/GameDesign/CoreGameplay.md) |

---

##### TASK-016: Implement AExtractionZone

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Medium |
| Risk | Medium — Event interrupt logic (e.g., taking hit damage while attempting extraction) frequently triggers problematic edge cases |
| Estimate | 4 days |
| Status | Not Started |
| Owner | Programmer |
| Dependencies | DOC-012, TASK-011 |
| Review | [ ] Proper Zone activation delays  [ ] Accurate extraction countdown timers  [ ] Player successfully extracts state change  [ ] Immediate timer interruption when hit  [ ] Code review pass |
| Refs | [Systems/MapSystem.md](../Systems/MapSystem.md), [GDD_Design/GameDesign/CoreGameplay.md](../../GDD_Design/GameDesign/CoreGameplay.md) |

**Description:**
- Create the `AExtractionZone` base actor
- Differentiate Zone types: Always Open, Conditional (Paid entry), Chance-based (Random open probability)
- Trigger activation parameters: purely Timer-based
- Core extraction flow: 30-second countdown timer, hard-interruptible if the player sustains damage
- Define player tracking logic: Overlap event → initiate timer → server confirms extraction result
- Route server broadcast event: `OnPlayerExtracted` → GameMode handles and rewards result

---

##### TASK-017: Implement Supply Drop & Match Events

| Field | Value |
|---|---|
| Priority | Medium |
| Difficulty | Medium |
| Risk | Low — Categorized as nice-to-have for the initial prototype; viable for deferral if timelines tighten |
| Estimate | 3 days |
| Status | Not Started |
| Owner | Programmer |
| Dependencies | TASK-016 |
| Review | [ ] Supply drops correctly spawn at predefined locations  [ ] Contained loot properly populates  [ ] Server-wide audio/UI event announcement broadcast |
| Refs | [GDD_Design/GameDesign/CoreGameplay.md](../../GDD_Design/GameDesign/CoreGameplay.md) |

---

#### Week 17-18 — June 23 to July 04, 2026: Prototype Map & M2 Review

---

##### DOC-013: Complete GDD — Alpha Map Design Document

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Medium |
| Estimate | 3 days |
| Owner | Level Designer + Game Designer |
| Status | Not Started |
| Output | Final MapDesign.md specifically for the "Industrial Zone": detailed layout, tier-based zone division, exact extraction points, designated AI spawn locations, and a comprehensive loot density heat-map |
| Refs | [GDD_Design/World/MapDesign.md](../../GDD_Design/World/MapDesign.md), [Systems/MapSystem.md](../Systems/MapSystem.md) |

---

##### TASK-018: Build Prototype Map "Industrial Zone" (Greybox)

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Hard |
| Risk | High — The map represents the direct environment players test; structural layout errors directly result in flawed gameplay feedback |
| Estimate | 8 days |
| Status | Not Started |
| Owner | Level Designer |
| Dependencies | DOC-013, TASK-016, TASK-014, TASK-015 |
| Review | [ ] Map compiles flawlessly  [ ] Adequate player spawn points  [ ] 3 Extraction Zones accurately placed  [ ] AI spawn points function under test  [ ] Loot spawns correlate to density map  [ ] Full internal playtest pass |
| Refs | [GDD_Design/World/MapDesign.md](../../GDD_Design/World/MapDesign.md), [ProjectScope/MVP.md](../../GDD_Design/ProjectScope/MVP.md) |

**Description:**
- Establish base dimensions: ~500x500m (utilizing simplified topology)
- Strictly employ Greybox materials; defer full art passes until later development phases
- Position 3 core Extraction Zones: 1 Always Open, 1 Conditional, 1 Chance based
- Layout High-density loot zones against designated low-risk transit routes
- Set strategic spawn points for players (distributed along map boundaries)
- Assign complex AI Scav spawn zones (including basic patrol routes)
- Ensure accurate collision layers; rigorously test for map holes or geometry stuck spots

---

##### TEST-003: Milestone M2 — Vertical Slice Review

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Medium |
| Risk | High — M2 acts as the fundamental gate dictating project progression to Phase 2 |
| Estimate | 3 days |
| Status | Not Started |
| Owner | Team Lead + Project Stakeholders |
| Dependencies | TASK-018 and all preceding Phase 1 TASKs |
| Review | [ ] Successful full match sequence: Spawn → Loot → Combat → Extract  [ ] AI Scavs functional and lethal  [ ] 2 connected players without technical crashes  [ ] Fully functional inventory interaction  [ ] Baseline performance maintains > 30 FPS on minimum target devices  [ ] Official Stakeholder sign-off |
| Refs | [ProjectScope/MVP.md](../../GDD_Design/ProjectScope/MVP.md), [DevelopmentRoadmap.md](../Core/DevelopmentRoadmap.md) |

---

## Phase 2: Content Creation — July to September 2026

**Objective:** Inject substantial core content: Full roster Operators, Expansive Arsenal, Map art polishing, polished UI/UX experiences, and preliminary Economy layers.
**Milestones:** M3 — Alpha Internal (End of Month 5), M4 — Beta Closed (End of Month 7)

> **Note:** July tasks are detailed deeply; August-September remain intentionally outlined, awaiting expansion pending M2 milestone passage.

---

### Month 5 — July 2026: Operators & UI

---

#### Week 19-20: Operator System Implementation

---

##### DOC-014: Complete GDD — Operator Classes & Abilities (Alpha Trio)

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Hard |
| Estimate | 3 days |
| Owner | Game Designer |
| Status | Not Started |
| Output | Finalize CharacterSystem.md and the specific Operators documents for the Assault, Scout, and Support archetypes: detailing stats, unique abilities, and strict cooldown parameters |
| Refs | [GDD_Design/Characters/](../../GDD_Design/Characters/), [Gameplay/CharacterSystem.md](../Gameplay/CharacterSystem.md) |

---

##### TASK-019: Implement Operator Class System (3 Alpha Operators)

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Very Hard |
| Risk | High — Ability system balance invariably requires multiple intensive iteration cycles; carries significant scope creep risk |
| Estimate | 10 days |
| Status | Not Started |
| Owner | Senior Programmer + Game Designer |
| Dependencies | DOC-014, TASK-003 |
| Review | [ ] All 3 Operators spawn bearing correct stats  [ ] Unique abilities trigger and activate correctly  [ ] Cooldown timers sync accurately across target networks  [ ] Comprehensive balance playtest conducted |
| Refs | [Gameplay/CharacterSystem.md](../Gameplay/CharacterSystem.md), [GDD_Design/Characters/](../../GDD_Design/Characters/) |

**Sub-tasks:**
- Construct foundation `UOperatorAbility` class and integrated Cooldown manager
- Implement Assault ability: Combat Stim (Applying speed boost + damage boost for 10s window)
- Implement Scout ability: UAV Scan (Highlight enemy signatures within set operational range)
- Implement Support ability: Healing Drone (Deploy physical drone to emit healing aura for teammates)
- Design and integrate the pre-match Operator selection UI screen
- Ensure robust network replication of complex ability state effects

---

#### Week 21-22: Weapon Expansion & Attachments

---

##### DOC-015: Complete GDD — Full Weapon Roster & Attachment System

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Medium |
| Estimate | 2 days |
| Owner | Game Designer |
| Status | Not Started |
| Output | Updated WeaponSystem.md reflecting expansion specifications for 15+ weapons alongside intricate attachment system logic design |
| Refs | [Gameplay/WeaponSystem.md](../Gameplay/WeaponSystem.md), [GDD_Design/Combat/Weapons.md](../../GDD_Design/Combat/Weapons.md) |

---

##### TASK-020: Implement 10+ Additional Weapons

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Medium |
| Risk | Medium — Expansive arsenals require careful balancing; highly susceptible to power creep issues |
| Estimate | 7 days |
| Status | Not Started |
| Owner | Programmer + Game Designer |
| Dependencies | DOC-015, TASK-006 |
| Review | [ ] New weapons appropriately load data from target DataTables  [ ] Initial rough balance pass verified  [ ] Dedicated QA test sequence passes without crashes |
| Refs | [Gameplay/WeaponSystem.md](../Gameplay/WeaponSystem.md) |

---

#### Week 23-24: HUD & Main Menu UI

---

##### DOC-016: Complete GDD — UI/UX Screens Specification

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Medium |
| Estimate | 3 days |
| Owner | UI/UX Designer |
| Status | Not Started |
| Output | Finalize UISystem.md including high-fidelity wireframes encompassing: Main Menu, combat HUD, full Inventory screen setup, and final Post-match results screen |
| Refs | [Systems/UISystem.md](../Systems/UISystem.md), [GDD_Design/UI_UX/](../../GDD_Design/UI_UX/), [GDD_Design/Visuals/UserInterface.md](../../GDD_Design/Visuals/UserInterface.md) |

---

##### TASK-021: Implement In-Game HUD

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Medium |
| Risk | Low |
| Estimate | 5 days |
| Status | Not Started |
| Owner | UI Programmer |
| Dependencies | DOC-016 |
| Review | [ ] HP/Armor bars reflect correct persistent data  [ ] Minimap displays properly  [ ] Functional active ammo counters  [ ] Extraction timers distinctly visualize when player occupies zone |
| Refs | [Systems/UISystem.md](../Systems/UISystem.md), [GDD_Design/UI_UX/](../../GDD_Design/UI_UX/) |

---

##### TASK-022: Implement Main Menu & Operator Selection

| Field | Value |
|---|---|
| Priority | High |
| Difficulty | Medium |
| Risk | Low |
| Estimate | 5 days |
| Status | Not Started |
| Owner | UI Programmer |
| Dependencies | DOC-016, TASK-019 |
| Review | [ ] Main menu screens navigate cleanly  [ ] Operator selection locks properly  [ ] Global settings options easily accessible |
| Refs | [Systems/UISystem.md](../Systems/UISystem.md) |

---

##### TEST-004: Alpha Internal (M3) Review

| Field | Value |
|---|---|
| Priority | Critical |
| Difficulty | Medium |
| Risk | High |
| Estimate | 3 days |
| Status | Not Started |
| Owner | Team Lead + Dedicated QA |
| Review | [ ] Map fully operational utilizing basic art pass  [ ] All 3 feature Operators playable effectively  [ ] Arsenal confirms 10+ Weapons functional  [ ] Complete on-screen HUD  [ ] Full internal team playtest over a 1-week period completes successfully |
| Refs | [ProjectScope/MVP.md](../../GDD_Design/ProjectScope/MVP.md) |

---

### Month 6 — August 2026: Economy, Progression & Bug Fixes [OUTLINE]

> Intended scope details to be firmly added post M3 clearance.

**Key Tasks (Outline):**
- DOC-017: GDD — Progression System Architecture (XP rules, leveling curves, specific unlocks)
- DOC-018: GDD — Global Economy System (multi-currency handling, vendor NPC stock rules, stash limits)
- TASK-023: Implement Game Progression System (XP tracking, strict Level gates, dynamic Unlock rewards)
- TASK-024: Implement Match Economy (Backend Credits logic, Vendor NPC interactions, persistent player Stash)
- TASK-025: Implement Core Quest System (Focusing explicitly on Alpha quests: simple daily contracts)
- TASK-026: Map 1 — Full Art Pass (Overhauling 'Industrial Zone': finalize detailed meshes, materials pass, comprehensive lighting setups)
- TEST-005: Closed Beta infrastructure readiness preparation (Scale 50 testers → 100, finalize telemetry tracking system setup)

---

### Month 7 — September 2026: Social Systems & Beta Readiness [OUTLINE]

**Key Tasks (Outline):**
- DOC-019: GDD — In-depth Squad System protocols & corresponding Matchmaking logic
- TASK-027: Squad System implementation (Develop 3-player squad linking, stable invite pipelines, coordinated squad drop matchmaking)
- TASK-028: Persistent Matchmaking backend implementation (utilizing EOS services)
- TASK-029: Baseline Anti-cheat deployment (hardening aggressive server-validation logic hooks)
- TASK-030: Holistic Performance optimization passes (Directly targeting stringent mobile metrics)
- TEST-006: Milestone M4 — Official Closed Beta Launch Readiness Evaluation

---

## Phase 3: Testing & QA — October to December 2026

> **Outline** — Detailed task expansion will accompany the completion of Phase 2 objectives.

### Month 10 — October 2026: Closed Alpha [OUTLINE]
- Deploy Alpha testing infrastructure to accommodate 50-100 external players
- Activate comprehensive telemetry and gameplay analytics hooks
- Configure unified Bug tracking systems (Integrating Jira/GitHub Issues workflow pipelines)
- Formalize actionable feedback collection pipeline channels
- **Primary Focus:** Assessing Core gameplay loop integrity, overarching network session stability, and profound weapon/economy balance issues

### Month 11 — November 2026: Open Beta [OUTLINE]
- Execute public beta software release (Scaling support upwards of 1000+ players)
- Execute rigorous server infrastructure stress tests under simulated heavy loads
- Iterate aggressively on Anti-cheat hardening protocols
- Advanced Performance Optimization procedures (Conduct detailed low-end device rendering passes)
- Perform live-production test of the integrated Monetization store features

### Month 12 — December 2026: Pre-Launch Polish [OUTLINE]
- Final sweep addressing isolated bug fixes (Strictly prioritizing Critical + High severity only)
- Finalization of lingering Content completeness (finalize remaining art assets, voice-over recordings, text localization)
- Execute formal Platform Store submission protocols (complying strictly with App Store and Google Play guidelines)
- Finalize and distribute primary Marketing campaign materials
- Milestone M5 — Formalize and lock down the Release Candidate deployment

---

## Phase 4: Launch & Live Ops — January 2027 onwards

> **Outline** — Precise operational detail will be finalized leading directly up to the official Launch window.

### Month 13 — January 2027: Soft Launch [OUTLINE]
- Coordinate limited specific region release deployment
- Aggressive Real-time KPI metrics monitoring implementation
- Finalize testing parameters of the rapid Hotfix deployment pipeline
- Live Ops overarching system dry-run scenario execution

### Month 14 — February 2027: Global Launch [OUTLINE]
- Execute full Worldwide release operation
- Coordinate global marketing campaign strategies alongside game launch
- Launch primary live events concurrent with the targeted Battle Pass Season 1 deployment
- Milestone M6 — Post-action review of Global Launch success metrics

### Post-Launch: Live Operations [OUTLINE]
- Establish reliable weekly schedule for weapon and ability balance patches
- Secure reliable monthly content update shipments (featuring new operators, expanded weapon rosters, and cosmetic skin additions)
- Run planned Seasonal event instances
- Dedicated, proactive Community management pipeline workflows

---

## Risk Register

| Risk ID | Recognized Risk Element | Probability | Potential Impact | Assessed Level | Planned Actionable Mitigation Strategy | Designated Owner |
|---|---|---|---|---|---|---|
| R-001 | Persistent Network replication bugs yielding severe player desync instances | Medium | Critical | Critical | Strictly enforce server-authoritative logic universally from inception; conduct aggressive early network stability playtesting | Tech Lead |
| R-002 | Highly complex AI behavior trees unexpectedly drastically exceeding time estimates | High | High | High | Aggressively limit the scope of Alpha AI; formally defer complex Boss entity logic structures into deeper Phase 2 cycles | AI Programmer |
| R-003 | Inventory grid system edge-case bugs that prove exceedingly difficult to systematically reproduce | Medium | High | High | Write robust Unit test structures governing all grid insertion logic; enforce strict CI build coverage metrics | Senior Programmer |
| R-004 | Pervasive Scope creep concerning added features slipping into stringent Phase 1 timeframes | High | Medium | High | Maintain severe strictness over the product backlog; rigorously enforce a stringent rule deferring 'nice-to-have' requests | Product Management / Team Lead |
| R-005 | Unexpected shortage concerning available direct technical personnel resources | Medium | High | High | Implement phased hiring strategies targeting crucial roles; readily outsource specialized tasks such as advanced animation | Product Management |
| R-006 | Extended iteration times necessary to accurately balance core combat gameplay (Weapon TTK vs. HP profiles) | High | Medium | Medium | Institute aggressive early playtest schedules immediately launching in Month 3; design DataTables explicitly maximizing iteration speed capabilities | Game Designer |
| R-007 | Target lowest-end Mobile performance benchmarks consistently failing to attain stable 30 FPS playback | Medium | High | High | Firmly dictate and enforce performance metrics budgets directly starting from Week 1; schedule a comprehensive, unyielding profiling dedicated sprint firmly before M2 milestone completion | Tech Lead |
| R-008 | Implemented 'GDD Doc' definitions lacking the requisite deep implementation clarification detail required preceding direct development implementation | Medium | High | High | Non-negotiable enforcement ensuring mandatory DOC completion tasks clear review checks explicitly before allowing associated feature TASK implementation; establish strict document review gate policies | Team Lead |
| R-009 | Emergence of a highly similar, formidable competitor title abruptly entering the direct market sector during our development cycle | Low | Medium | Medium | Resolutely focus design prioritization toward polishing our game's unique top-down perspective advantages and differentiating structural combat elements | Design Lead |

---

## Review Schedule

| Meeting | Frequency Schedule | Allotted Duration | Requisite Participants | Primary Meeting Purpose |
|---|---|---|---|---|
| Daily Standup | Weekday occurrences | 15 minutes | Full Team | Synchronize individual progress over the last 24 hours, rapidly surface any blocking issues |
| Sprint Planning | Bimonthly (Held on Monday) | 2 hours | Team Lead + Relevant Developers | Diligently plan, size, and assign upcoming sprint tasks utilizing backlog priority |
| Sprint Review | Bimonthly (Held on Friday) | 1 hour | Full Team | Visually demo work effectively 'Done' within the sprint; maintain team-wide alignment |
| Sprint Retro | Bimonthly (Held on Friday) | 45 minutes | Full Team | Analyze workflows; collectively identify what went correctly, and surface required procedural improvements |
| GDD Formal Review | Ad-hoc (Upon DOC task completion) | 1 hour | Designated Designer + Tech Lead | Formally review and grant official sign-off approving a GDD section for commencement into active development |
| Milestone Gate Review | Scheduled exclusively at the end of each predefined Phase cycle | Half-day session | Full Team + External Key Stakeholders | Exhaustive project review; decisive decision point determining strict Go/No-Go actions necessary to progress toward the subsequent project Phase |

---

## Document Update Log

| Specific Date | Current Version | Annotated Document Changes | Responsible Author |
|---|---|---|---|
| 2026-02-21 | 1.0.1 | Translated the initial complete GDD Task Tracker fully into professional English targeting an International Game Design structural orientation. | Team |

---

*This document receives critical actionable updates exclusively following every scheduled sprint review. All proposed modifications fundamentally altering the established scope must receive explicit approval clearance personally authorized by the designated Team Lead before officially reflecting within this tracking record.*
