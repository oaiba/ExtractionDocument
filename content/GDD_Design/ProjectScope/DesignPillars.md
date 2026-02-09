---
title: "Design Pillars & Core Philosophy"
type: docs
---
# Design Pillars & Core Philosophy

**[← Back to Index](../README.md)**

---

# Design Pillars & Core Philosophy

**[← Back to Index](../README.md)**

## 🏗️ Genre Pillars (Extraction Shooter Core)

These six foundational pillars define the extraction shooter genre. Our design choices directly support these concepts to ensure an authentic experience.

| Pillar               | Definition                                    | Implementation in Our Game                                                                                                           |
| :------------------- | :-------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| **Risk of Loss**     | Constant awareness that progress can be lost. | **Full Loot Drop:** Dying means losing everything equipped. This drives the "High-Stakes Tension" pillar.                            |
| **Survival**         | Survival prioritized over unnecessary combat. | **Health Scarcity:** Meds are valuable. Engaging every enemy drains resources, making stealth and avoidance viable tactical choices. |
| **Progression Tree** | Permanent, learnable advantages.              | **Hideout & Trader Levels:** Even if you lose gear, you gain XP and reputation, unlocking better shop items and passive base buffs.  |
| **Resource Heavy**   | Strong emphasis on inventory management.      | **Tetris Inventory:** Managing grid space requires decision-making. Ammo tracking is manual (mag checking), not just a UI number.    |
| **Task Driven**      | Clear objectives that guide decisions.        | **Faction Quests:** Players depoy with specific goals (mark territory, retrieve intel) rather than just "killing everyone."          |
| **Time**             | Staying longer increases risk and reward.     | **Match Timer & Events:** As the match progresses, player scavengers spawn, and extracts may close, forcing movement.                |

---

## 🏛️ The Five Core Pillars

Every design decision, mechanic, and line of code must serve one of these five core pillars. If a feature does not support at least one, it should be cut or reworked.

### 1. High-Stakes Tension (Risk of Loss & Reward)
**Mantra:** *"Fear of Loss drives the Thrill of Gain."*

*   **Core Concept:** The game is defined by what you stand to lose. Progression is not linear; it is a wager. The tension comes from the imbalance between your vulnerability and the value of your inventory.
*   **Execution Examples:**
    *   **The "Crunchy" Soundscape:** Footsteps are distinct and terrifying. Silence is heavy. Gunshots decay realistically indoors vs. outdoors, giving positional intel.
    *   **Lethality:** Time-to-Kill (TTK) is low. A well-placed shot from a cheap pistol can kill a fully geared operator (the "David vs. Goliath" possibility).
    *   **Inventory Tetris:** Looting takes time and blocks vision. Players must physically arrange items, creating vulnerability during the "reward" phase.
*   **Anti-Patterns:** Bullet Sponges, excessive "secure containers," Arcade movement.

### 2. Tactical Fluidity (Survival & Tactical Depth)
**Mantra:** *"Control the Operator, not the Interface."*

*   **Core Concept:** Complexity should come from the situation, not the inputs. While the game simulates realistic ballistics and movement, the controls must respond instantly to player intent. Survival is prioritized over unnecessary combat.
*   **Execution Examples:**
    *   **Action Chaining:** Reload while sprinting (at cost of speed), or slide into cover while checking a mag. Actions flow into one another.
    *   **Resource Management:** Manual mag checking, limited med availability, and weight-based movement penalties.
    *   **Weapon Feedback:** Learnable recoil patterns and crisp aim response despite "heavy" weapon feel.
*   **Anti-Patterns:** Animation locks for critical actions, artificial input delay, over-binding controls.

### 3. Environmental Narratives (The Living World)
**Mantra:** *"Aethelgard is the First Enemy."*

*   **Core Concept:** Aethelgard is a character, not a backdrop. History is told through the placement of objects, dead bodies, and lighting, not text logs. The world feels lived-in and abandoned, not built for a game.
*   **Execution Examples:**
    *   **Logical Loot:** Medkits in ambulances, ammo in checkposts. Rewards map knowledge and logic.
    *   **Visual Storytelling:** Environmental dioramas (e.g., a room barricaded from the inside) tell stories without dialogue.
    *   **Atmospheric Guidance:** Using lighting (emergency red lights, flickering sparks) to guide players instead of UI markers.
*   **Anti-Patterns:** Symmetrical "esports" arenas, nonsense loot (high-tech items in primitive contexts).

### 4. Task-Driven Agency (Meaningful Choices)
**Mantra:** *"Choose your Wager, Define your Goal."*

*   **Core Concept:** Players should never be "just wandering." Every action is driven by a quest, a resource need, or a tactical choice. Meaningful agency means the player's decisions (greed vs. safety) result in direct emotional consequences.
*   **Execution Examples:**
    *   **Loadout Strategy:** Choosing "Cheap" vs "Expensive" loadouts based on mission risk.
    *   **Dynamic Extraction:** Choosing which extraction point to risk based on current health and loot value.
    *   **Faction Quests:** Objectives that force players into interesting tactical situations (e.g., marking territory in high-risk zones).
*   **Anti-Patterns:** Mandatory linear paths, lack of meaningful choices in how to complete objectives.

### 5. Persistent Progression (Account & World Growth)
**Mantra:** *"Lose the Raid, Build the War."*

*   **Core Concept:** While individual raids carry the risk of loss, the account's power and influence grow persistently. Your actions today improve your capabilities tomorrow through the Hideout, Traders, and Reputation.
*   **Execution Examples:**
    *   **Hideout Upgrades:** Passive bonuses (healing speed, stash size) that persist regardless of raid outcomes.
    *   **Trader Reputation:** Unlocking high-tier gear availability through successful quest completion.
    *   **Operator Mastery:** Earning specific expertise with characters that remains even after death.
*   **Anti-Patterns:** Total account wipes (outside of season resets), lack of significant permanent rewards for successful play.

---

## ⚖️ Pillar Conflict Resolution
When core pillars contradict each other, use this hierarchy to decide:

1.  **High-Stakes Tension** beats **Tactical Fluidity** (e.g., Healing *must* stop you from shooting to create vulnerability).
2.  **Tactical Fluidity** beats **Realism** (e.g., We simulate ballistics, but we don't make the control scheme impossible).
3.  **Environmental Narrative** serves **Tension** (e.g., Add flickering lights to dark corners to create silhouettes for balance).
4.  **Task-Driven Agency** informs **Progression** (e.g., Quests should reward permanent account growth or reputation).

---

## 🎯 Game Feel Goals

### "Crunchy" Combat
*   **Audio:** Environmental bass/reverb, tinnitus effects after explosions.
*   **Visuals:** Debris, sparks, physical reaction to hits (stagger/flinch).
*   **Input:** Predictable recoil, "hit stop" for melee impacts.

### "Weighty" Movement
*   **Inertia:** Micro-acceleration/deceleration.
*   **Momentum:** Sliding preserves speed; jumping from sprint carries momentum.
*   **Grounding:** Camera bob and footstep sync to ground terrain.

---

## 🔄 The Core Loops

### Macro Loop (Long-Term Growth)
1.  **PREPARE**: Assess risk, build loadout, accept faction tasks.
2.  **RAID**: Enter Aethelgard, survive, loot, complete tasks.
3.  **EXTRACT**: Secure gear and data.
4.  **PROGRESS**: Upgrade Hideout, increase Reputation, unlock gear.

### Micro Loop (Immediate Tension)
1.  **OBSERVE**: Sound cues, visual glints, environmental traces.
2.  **ORIENT**: Threat assessment, cover check, objective check.
3.  **DECIDE**: Fight, flight, or sneak?
4.  **ACT**: Execute tactical maneuver.
5.  **ADAPT**: Review results and reset.

---

## ✅ Quality Assurance Checklist
Use this checklist for every new feature request:

1.  [ ] Does it increase **Tension** or **Tactical Depth**?
2.  [ ] Does it respect the **Flow (Fluidity)** of movement?
3.  [ ] Does it make sense in the **Context of Aethelgard**?
4.  [ ] Does it provide the player with a **Meaningful Choice**?
5.  [ ] Does it contribute to **Persistent Progression**?

---

## 📝 Document Ownership & Changelog

| Role            | Owner             | Approver           |
| :-------------- | :---------------- | :----------------- |
| **Author**      | Creative Director | Studio Head        |
| **Tech Review** | N/A               | Lead Game Designer |

**Recent Changes:**
*   **v1.2 (2026-02-09):** Unified Pillars to 'Five Core Pillars' and standardized world name to 'Aethelgard'.
*   **v1.1 (2026-02-09):** Added "Genre Pillars" section based on industry research.
*   **v1.0 (2026-02-07):** Initial philosophy definition.

---


