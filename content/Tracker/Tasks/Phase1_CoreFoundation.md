---
title: "Phase 1: Core Foundation & Prototyping"
type: docs
weight: 10
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

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>INFRA-001: Initialize UE5 Project</b></summary>

| Field | Value |
|---|---|
| Difficulty | Easy |
| Risk | Medium — Choosing the wrong mobile template could impact future structure |
| Estimate | 1 day |
| Owner | Tech Lead |
| Review | `[ ]` Project builds successfully  `[ ]` Opens on all team machines  `[ ]` CI pass |
| Refs | [Architecture.md](../Core/Architecture.md), [UE5 Documentation](https://docs.unrealengine.com/5.0/en-US/) |

**Description:**
- Create a UE5 project using the Blank C++ template (avoid default mobile templates)
- Configure Target Platforms: PC (Development), Android (Future)
- Setup project directory structure: Source/, Content/, Config/
- Commit the initial template build

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>INFRA-002: Setup Version Control (Git + LFS)</b></summary>

| Field | Value |
|---|---|
| Difficulty | Easy |
| Risk | Low |
| Estimate | 1 day |
| Owner | Tech Lead / DevOps |
| Review | `[ ]` .gitignore correct for UE5  `[ ]` LFS tracks .uasset & .umap  `[ ]` Push/Pull test pass |
| Refs | [CodingStandards.md](../Core/CodingStandards.md) |

**Description:**
- Initialize Git repository
- Configure .gitignore for UE5 (Binaries, Intermediate, DerivedDataCache, Saved)
- Install and configure Git LFS for .uasset, .umap, .wav, .png
- Document branching strategy: main / develop / feature/*

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="High" color="orange" >}} <b>INFRA-003: Setup Build Pipeline (Basic CI/CD)</b></summary>

| Field | Value |
|---|---|
| Difficulty | Medium |
| Risk | Medium — Continuous CI failures will slow down workflow |
| Estimate | 2 days |
| Owner | DevOps |
| Review | `[ ]` Auto-builds trigger on push  `[ ]` Build reports sent to Slack/Discord |
| Refs | [Architecture.md](../Core/Architecture.md) |

**Description:**
- Setup GitHub Actions or Jenkins
- Trigger: build and compile C++ on push to the develop branch
- Report build status (Success / Fail + logs)
- Packaging is not required yet; only a successful compile pass is needed

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="High" color="orange" >}} <b>DOC-001: Complete GDD — Coding Standards & Project Structure</b></summary>

| Field | Value |
|---|---|
| Difficulty | Easy |
| Estimate | 1 day |
| Owner | Tech Lead |
| Output | Fully documented CodingStandards.md, reviewed and approved by the entire team |
| Refs | [CodingStandards.md](../Core/CodingStandards.md), [Architecture.md](../Core/Architecture.md) |

**Description:**
- Review and finalize naming conventions (C++, Blueprints, Assets)
- Confirm module architecture layers (Layer 0, 1, 2)
- Document the exact folder structure within Content/
- Distribute for team-wide review

</details>

---

#### Week 2 — March 10 to March 14, 2026: Architecture & Module Setup

**Sprint Goal:** Clean module architecture, GameplayTags system ready, base classes available for derivation.

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="High" color="orange" >}} <b>DOC-002: Complete GDD — Detailed Architecture</b></summary>

| Field | Value |
|---|---|
| Difficulty | Easy |
| Estimate | 1 day |
| Owner | Tech Lead |
| Output | Architecture.md features a clear class hierarchy and is ready for development |
| Refs | [Architecture.md](../Core/Architecture.md), [GDD_Technical/_index.md](../_index.md) |

**Description:**
- Confirm core class hierarchy: ExtractionCharacter → ExtractionPlayerCharacter / ExtractionAICharacter
- Clearly document module dependencies
- Validate tech stack choices (UE5.4+, EOS, PostgreSQL/Redis)

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>TASK-001: Implement Module Structure & GameplayTags</b></summary>

| Field | Value |
|---|---|
| Difficulty | Medium |
| Risk | High — GameplayTags act as the system backbone; early mistakes are extremely difficult to refactor |
| Estimate | 3 days |
| Owner | Tech Lead |
| Dependencies | DOC-002, INFRA-001 |
| Review | `[ ]` Modules compile without errors  `[ ]` GameplayTag catalog documented  `[ ]` Code review pass |
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

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>TASK-002: Implement Base UE5 Skeleton (GameMode, GameState, PlayerState)</b></summary>

| Field | Value |
|---|---|
| Difficulty | Easy |
| Risk | Low |
| Estimate | 2 days |
| Owner | Programmer |
| Dependencies | TASK-001 |
| Review | `[ ]` Classes compile successfully  `[ ]` Blueprint children easily created  `[ ]` Code review pass |
| Refs | [Architecture.md](../Core/Architecture.md), [Core/NetworkingSystem.md](../Core/NetworkingSystem.md) |

**Description:**
- Create `AExtractionGameMode` (derived from AGameModeBase)
- Create `AExtractionGameState` (derived from AGameStateBase)
- Create `AExtractionPlayerState` (derived from APlayerState)
- Create `AExtractionPlayerController` (derived from APlayerController)
- Stub out basic interfaces for match flow

</details>

---

#### Week 3 — March 17 to March 21, 2026: Character System

**Sprint Goal:** Character can move, crouch, and take damage within PIE (Play In Editor).

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>DOC-003: Complete GDD — Detailed Character System</b></summary>

| Field | Value |
|---|---|
| Difficulty | Medium |
| Estimate | 2 days |
| Owner | Game Designer + Tech Lead |
| Output | CharacterSystem.md includes complete stats (HP, Speed, Stamina), movement specs, and animation states |
| Refs | [Gameplay/CharacterSystem.md](../Gameplay/CharacterSystem.md), [GDD_Design/Characters/](../../GDD_Design/Characters/), [GDD_Design/GameDesign/CoreGameplay.md](../../GDD_Design/GameDesign/CoreGameplay.md) |

**Description:**
- Finalize base stats for each Operator archetype (HP, Speed, Stamina, Carry Weight)
- Define movement states: Walk, Sprint, Crouch, ADS
- Define the animation state machine design
- Document damage location multipliers (Head, Thorax, Stomach, Limbs)

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>TASK-003: Implement AExtractionCharacter Base Class</b></summary>

| Field | Value |
|---|---|
| Difficulty | Medium |
| Risk | High — Errors in the base character class will ripple throughout the entire system |
| Estimate | 3 days |
| Owner | Senior Programmer |
| Dependencies | DOC-003, TASK-002 |
| Review | `[ ]` Character spawns correctly  `[ ]` Movement functional  `[ ]` Animations blend properly  `[ ]` Code review pass |
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

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>TASK-004: Implement UMobileInputComponent & Top-Down Input</b></summary>

| Field | Value |
|---|---|
| Difficulty | Hard |
| Risk | High — Top-down input abstraction is complex and requires rigorous testing on both PC and mobile targets |
| Estimate | 4 days |
| Owner | Senior Programmer |
| Dependencies | DOC-003, TASK-003 |
| Review | `[ ]` WASD / joystick movement works  `[ ]` Mouse aiming works  `[ ]` Aim assist functions properly  `[ ]` Code review pass |
| Refs | [Gameplay/ControlSystem.md](../Gameplay/ControlSystem.md), [GDD_Design/GameDesign/Controls.md](../../GDD_Design/GameDesign/Controls.md) |

**Description:**
- Implement the Enhanced Input system
- Map Actions: Move, Aim, Fire, Reload, Interact, Crouch
- Implement top-down mouse projection (raycast to ground plane)
- Stub out virtual joystick logic for mobile (full implementation later)
- Implement basic aim assist: snap assist with distance-based falloff

</details>

---

#### Week 4 — March 24 to March 28, 2026: Animation & End-of-Month Review

**Sprint Goal:** Character features full animation coverage, Milestone 1 review passed successfully.

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="High" color="orange" >}} <b>DOC-004: Complete GDD — Animation State Machine</b></summary>

| Field | Value |
|---|---|
| Difficulty | Easy |
| Estimate | 1 day |
| Owner | Tech Artist + Game Designer |
| Output | Comprehensive definition of all animation states and transition rules |
| Refs | [Gameplay/CharacterSystem.md](../Gameplay/CharacterSystem.md), [GDD_Design/Visuals/ArtDirection.md](../../GDD_Design/Visuals/ArtDirection.md) |

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="High" color="orange" >}} <b>TASK-005: Setup Animation Blueprint (Top-Down)</b></summary>

| Field | Value |
|---|---|
| Difficulty | Medium |
| Risk | Medium — Placeholder animations are acceptable now; the true risk lies in an incorrect ABP structure |
| Estimate | 3 days |
| Owner | Tech Artist / Programmer |
| Dependencies | DOC-004, TASK-003 |
| Review | `[ ]` Idle/Walk/Sprint blend correctly  `[ ]` Crouch animation active  `[ ]` Death animation triggers  `[ ]` Code review pass |
| Refs | [Gameplay/CharacterSystem.md](../Gameplay/CharacterSystem.md) |

**Description:**
- Create the primary Animation Blueprint for `ExtractionCharacter`
- Core State Machine: Idle → Walk → Sprint; Idle → Crouch
- Implement speed-based locomotion blendspaces
- Trigger death animation via the `OnDead` event
- Utilize placeholder Mannequin assets for this phase

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>TEST-001: End-of-Month 1 Review & Integration Test</b></summary>

| Field | Value |
|---|---|
| Difficulty | Easy |
| Risk | Low |
| Estimate | 1 day |
| Owner | Team Lead + QA |
| Dependencies | TASK-001 through TASK-005 |
| Review | `[ ]` All INFRA passes  `[ ]` Character moves correctly  `[ ]` CI Build succeeds  `[ ]` Team retrospective completed |
| Refs | [DevelopmentRoadmap.md](../Core/DevelopmentRoadmap.md), [ProjectScope/MVP.md](../../GDD_Design/ProjectScope/MVP.md) |

**Description:**
- Internal Demo: Character spawning, movement, taking damage, and dying
- Tracking missing checklist issues
- Complete Sprint retrospective
- Update DevelopmentRoadmap.md with actual statuses

</details>

---

### Month 2 — April 2026: Combat System & Networking Foundation

**Monthly Goal:** Establish a complete core combat loop (fire, hit, damage) and baseline network replication. Achieve Milestone M1 — Prototype.

---

#### Week 5 — March 31 to April 04, 2026: Weapon System Foundation

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>DOC-005: Complete GDD — Detailed Weapon System</b></summary>

| Field | Value |
|---|---|
| Difficulty | Medium |
| Estimate | 2 days |
| Owner | Game Designer |
| Output | WeaponSystem.md includes complete details: weapon classes, stats, ballistics, and recoil patterns for Alpha weapons (AK47, M4A1, MP5, Glock) |
| Refs | [Gameplay/WeaponSystem.md](../Gameplay/WeaponSystem.md), [GDD_Design/Combat/Weapons.md](../../GDD_Design/Combat/Weapons.md) |

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>TASK-006: Implement AExtractionWeapon Base Class</b></summary>

| Field | Value |
|---|---|
| Difficulty | Hard |
| Risk | High — The weapon system is the core gameplay loop; bugs here are difficult to debug after scaling up the arsenal |
| Estimate | 4 days |
| Owner | Senior Programmer |
| Dependencies | DOC-005, TASK-003 |
| Review | `[ ]` Firing logic works  `[ ]` Ammo tracked correctly  `[ ]` Reload functions properly  `[ ]` Weapon equip/unequip works  `[ ]` Code review pass |
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

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="High" color="orange" >}} <b>TASK-007: Implement Alpha Weapons (AK47, M4A1, MP5, Glock)</b></summary>

| Field | Value |
|---|---|
| Difficulty | Medium |
| Risk | Medium — Weapon balancing is the primary risk; requires multiple iteration cycles |
| Estimate | 3 days |
| Owner | Programmer + Game Designer |
| Dependencies | TASK-006, DOC-005 |
| Review | `[ ]` All 4 weapons fire using correct stats  `[ ]` Recoil visuals align  `[ ]` Damage values match DataTable specifications  `[ ]` QA test pass |
| Refs | [Gameplay/WeaponSystem.md](../Gameplay/WeaponSystem.md), [GDD_Design/Combat/Weapons.md](../../GDD_Design/Combat/Weapons.md) |

**Description:**
- Implement 4 Alpha weapons reading from DataTables:
- AK-47: High damage output, severe recoil
- M4A1: Balanced profile, highly moddable slots
- MP5: Fast CQB focus, low armor penetration
- Glock 17: Reliable sidearm fallback
- Utilize placeholder meshes (Standard Mannequin configurations)
- Establish visual recoil tracking to monitor mismatch issues

</details>

---

#### Week 6 — April 07 to April 11, 2026: Hit Detection & Health System

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>TASK-008: Implement Hit Detection & Damage System</b></summary>

| Field | Value |
|---|---|
| Difficulty | Hard |
| Risk | Critical — Flawed hit detection in online games is catastrophic; server validation must be robust from day one |
| Estimate | 4 days |
| Owner | Senior Programmer |
| Dependencies | TASK-006, TASK-003 |
| Review | `[ ]` Line trace correctly hits zones  `[ ]` Damage multipliers apply correctly (Head 2x, Thorax 1x, Limb 0.7x)  `[ ]` Server validates all hits  `[ ]` Zero false-positive test cases  `[ ]` Code review pass |
| Refs | [Gameplay/CharacterSystem.md](../Gameplay/CharacterSystem.md), [GDD_Design/Combat/Weapons.md](../../GDD_Design/Combat/Weapons.md) |

**Description:**
- Configure line traces using custom UE5 physics collision channels
- Implement distinct hit zone detection: Head, Thorax, Stomach, Arms, Legs
- Apply damage multipliers retrieved from DataTables
- Essential server-authoritative logic: client sends hit request, server confirms valid intersection
- Route damage to `UHealthComponent` and broadcast `OnDamageTaken`, `OnDead`
- Implement initial visual feedback: hit marker UI

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="High" color="orange" >}} <b>DOC-006: Complete GDD — Health & Status Effect System</b></summary>

| Field | Value |
|---|---|
| Difficulty | Easy |
| Estimate | 1 day |
| Owner | Game Designer |
| Output | Health states fully defined for Alpha (HP, Death); beta states (Bleeding, Fractures) documented but queued for later implementation |
| Refs | [GDD_Design/GameDesign/CoreGameplay.md](../../GDD_Design/GameDesign/CoreGameplay.md), [Gameplay/CharacterSystem.md](../Gameplay/CharacterSystem.md) |

</details>

---

#### Week 7 — April 14 to April 18, 2026: Network Foundation

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>DOC-007: Complete GDD — Networking Architecture & Replication Plan</b></summary>

| Field | Value |
|---|---|
| Difficulty | Medium |
| Estimate | 2 days |
| Owner | Tech Lead |
| Output | NetworkingSystem.md features a clear replication strategy: defining server-replicated vs. locally predicted elements |
| Refs | [Core/NetworkingSystem.md](../Core/NetworkingSystem.md) |

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>TASK-009: Setup Dedicated Server Architecture</b></summary>

| Field | Value |
|---|---|
| Difficulty | Very Hard |
| Risk | Critical — Incorrect server setup will block all subsequent multiplayer feature testing |
| Estimate | 5 days |
| Owner | Senior Programmer + DevOps |
| Dependencies | DOC-007, TASK-002 |
| Review | `[ ]` Dedicated Server builds successfully  `[ ]` Client successfully connects to local server instance  `[ ]` Local ping registers < 50ms  `[ ]` Code review pass |
| Refs | [Core/NetworkingSystem.md](../Core/NetworkingSystem.md), [Core/Architecture.md](../Core/Architecture.md) |

**Description:**
- Configure UE5 Dedicated Server project build targets
- Separate and optimize client and server build profiles
- Implement base connection handling and session management logic
- Ensure Listen Server mode is functional for rapid local testing
- Complete the server deployment guide document

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>TASK-010: Implement Character & Combat Replication</b></summary>

| Field | Value |
|---|---|
| Difficulty | Very Hard |
| Risk | Critical — Replication bugs cause immediate desync and break gameplay; requires rigorous testing with at least 2 connected clients |
| Estimate | 5 days |
| Owner | Senior Programmer |
| Dependencies | TASK-009, TASK-003, TASK-008 |
| Review | `[ ]` Movement prediction functions smoothly  `[ ]` Combat events replicate correctly  `[ ]` Health syncs accurately  `[ ]` 2-client live test passes fully  `[ ]` Code review pass |
| Refs | [Core/NetworkingSystem.md](../Core/NetworkingSystem.md) |

**Description:**
- Replicate variables: Position, Rotation, Velocity (Client-Predicted for responsiveness)
- Replicate variables: Health, Armor levels (Strictly Server Authoritative)
- Replicate events: Weapon firing visuals/audio (Multicast RPC)
- Implement baseline lag compensation mechanisms
- Required 2-client local test: Client A shoots Client B, hit registers correctly on both screens

</details>

---

#### Week 8 — April 21 to April 25, 2026: GameMode Flow & Milestone M1

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="High" color="orange" >}} <b>DOC-008: Complete GDD — Match Flow & Game Rules</b></summary>

| Field | Value |
|---|---|
| Difficulty | Easy |
| Estimate | 1 day |
| Owner | Game Designer |
| Output | Clear match lifecycle defined: WaitingForPlayers → InProgress → Ended |
| Refs | [GDD_Design/GameDesign/CoreGameplay.md](../../GDD_Design/GameDesign/CoreGameplay.md), [Core/Architecture.md](../Core/Architecture.md) |

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="High" color="orange" >}} <b>TASK-011: Implement Match Flow (GameMode)</b></summary>

| Field | Value |
|---|---|
| Difficulty | Medium |
| Risk | Medium — Managing underlying state logic is more complex than it appears due to cross-system dependencies |
| Estimate | 3 days |
| Owner | Programmer |
| Dependencies | DOC-008, TASK-009 |
| Review | `[ ]` Proper match start/end triggers  `[ ]` Players appropriately spawned  `[ ]` Win conditions trigger correctly  `[ ]` Code review pass |
| Refs | [GDD_Design/GameDesign/CoreGameplay.md](../../GDD_Design/GameDesign/CoreGameplay.md) |

**Description:**
- Update `AExtractionGameMode` states: WaitingForPlayers → InProgress → Results
- Implement spawn manager using PlayerStart actors
- Implement placeholder win condition: last player alive
- Implement global match timer tracking within GameState

</details>

---

<details><summary>{{< badge content="Not Started" color="gray" >}} {{< badge content="Critical" color="red" >}} <b>TEST-002: Milestone M1 — Prototype Review</b></summary>

| Field | Value |
|---|---|
| Difficulty | Easy |
| Risk | High — Failing this milestone necessitates immediate adjustment to the Phase 1 scope and schedule |
| Estimate | 2 days |
| Owner | Team Lead |
| Dependencies | All tasks from Weeks 5-7 |
| Review | `[ ]` 2 connected players online  `[ ]` Combat engagements possible  `[ ]` Accurate damage registration  `[ ]` Complete match start/end cycle  `[ ]` Zero critical crashes during a 30-minute play session |
| Refs | [ProjectScope/MVP.md](../../GDD_Design/ProjectScope/MVP.md), [DevelopmentRoadmap.md](../Core/DevelopmentRoadmap.md) |

</details>

---

