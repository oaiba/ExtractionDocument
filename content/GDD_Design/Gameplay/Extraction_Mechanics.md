---
title: "Extraction Mechanics"
type: docs
weight: 6
---

## Overview

Extraction is the climax of every raid. It is the singular moment where all accumulated risk, loot, and decisions converge into a binary outcome: escape with everything, or lose it all. The extraction system is designed to create maximum tension through a combination of location commitment, time vulnerability, and environmental signaling.

> See [Core Gameplay Mechanics](../../GameDesign/CoreGameplay/) for the raw extraction process specification and zone type parameters. This document focuses on the interaction design, player psychology, and counter-play dynamics.

---

## Extraction Zone Types

### Standard Extraction

| Property | Detail |
| :------- | :----- |
| Count per Map | 3-4 zones |
| Availability | Always active from raid start to raid end |
| Timer | 30 seconds once activated |
| Capacity | Unlimited — any number of players can extract simultaneously |
| Location | Fixed, known locations marked on map (green helicopter icon) |
| Noise | Helicopter approach audio at timer start. Audible at 80m+ |
| Risk Level | High — known locations are frequently watched and camped |

<!-- REF_IMAGE: Standard extraction zone layout — aerial view showing the zone boundary, helicopter landing pad, common approach routes, and typical camping positions -->

### Emergency Extraction

| Property | Detail |
| :------- | :----- |
| Count per Map | 1-2 zones |
| Availability | Requires a specific key or quest item to unlock |
| Timer | 15 seconds (faster extraction) |
| Capacity | Single use — zone closes after one successful extraction |
| Location | Hidden or unmarked. Players must discover through exploration or map knowledge |
| Noise | Quiet extraction (no helicopter). Faint radio static audio (audible at 20m) |
| Risk Level | Medium — harder to find, so less likely to be camped. But reaching it may require traversing dangerous areas |

### Vehicle Extraction

| Property | Detail |
| :------- | :----- |
| Count per Map | 1 per map |
| Availability | Always active, but limited capacity |
| Timer | 45 seconds (vehicle must arrive and load) |
| Capacity | Maximum 4 players. First-come-first-served |
| Location | Road or dock. Vehicle drives/arrives during the timer |
| Noise | Very High — engine rumble, horn blast. Audible across most of the map |
| Risk Level | Very High — longest timer, loudest signal. Attracts every nearby player |

### Cooperative Extraction

| Property | Detail |
| :------- | :----- |
| Count per Map | 1 per map |
| Availability | Requires 2+ players from different factions to activate simultaneously |
| Timer | 20 seconds |
| Capacity | 2-4 players from mixed factions |
| Location | Neutral zone. Special door/gate that requires simultaneous activation from both sides |
| Noise | Moderate — gate mechanism sound (audible at 30m) |
| Reward | Reputation bonus with both factions. XP multiplier for cooperation |
| Risk Level | Low combat risk (cooperation), but high trust risk (the other player could betray you after the gate opens) |

### Paid Extraction (Future Feature)

| Property | Detail |
| :------- | :----- |
| Count per Map | 1 per map |
| Availability | Requires in-raid currency payment (e.g., $5,000 Credits found during the raid) |
| Timer | 25 seconds |
| Location | Metro station, underground passage |
| Noise | Low — underground, muffled |
| Risk Level | Low-Medium — cost barrier prevents casual use. Underground location limits camping angles |

---

## Extraction Process Flow

### Step-by-Step Interaction

```
1. APPROACH EXTRACTION ZONE
   - Zone boundary is visible on minimap (green circle)
   - UI prompt appears at zone edge: "Enter Extraction Zone"

2. ENTER ZONE BOUNDARY
   - On-screen message: "Hold [E] to Call Extraction"
   - Timer does NOT start until player activates

3. ACTIVATE EXTRACTION
   - Player holds interaction button for 1.5 seconds
   - Timer begins: 30-second countdown (varies by zone type)
   - Audio: Helicopter engines starting / vehicle approaching / radio confirmation
   - Visual: Smoke grenade deployed (automatic), flares lit
   - MAP NOTIFICATION: "A player is extracting at [Zone Name]"

4. DEFEND POSITION (Timer Running)
   - Player must remain within the zone boundary
   - Player CAN shoot, use abilities, throw grenades
   - Player CAN crouch, go prone, and use cover within the zone
   - Player CANNOT heal (healing cancels extraction)
   - Teammates must also be within the zone boundary for squad extraction

5. EXTRACTION COMPLETE
   - Fade to black. Helicopter dust effect / vehicle departure
   - Transition to Victory Screen with loot summary

   OR

   EXTRACTION FAILED (timer interrupted)
   - Timer resets to 0. Player must re-activate
   - No penalty for failed activation (other than lost time)
```

<!-- REF_IMAGE: Extraction timer HUD mockup — showing the 30-second countdown, zone boundary indicator, and the "Extracting..." status bar with helicopter silhouette approaching -->

---

## Interruption Rules

The extraction timer resets to zero under the following conditions:

| Interruption Trigger | Reset Behavior | Design Reason |
| :------------------- | :------------- | :------------ |
| Player leaves zone boundary (even 1 step) | Full reset | Prevents players from hopping in and out of the zone |
| Player takes ANY damage (even 1 HP) | Full reset | Creates counter-play. Attackers can deny extraction with a single bullet |
| Player uses a healing item | Full reset | Forces a choice: heal first, then extract. Cannot do both simultaneously |
| Teammate dies within the zone | Full reset (squad extraction mode) | Squad must be complete to extract together. Dead teammate = abort or leave them |
| Grenade/ability lands in the zone | Full reset for all players in zone | AOE denial is a valid extraction disruption tactic |

### Interruption Counter-Measures

- **Smoke Grenades**: Deploying smoke in the extraction zone blocks line-of-sight, preventing accurate shots from outside
- **Decoy Abilities**: Some operators have decoy or distraction abilities that can redirect enemy attention
- **Pre-Clearing**: Sweep the extraction area before activating. Check common camping spots
- **Staggered Extraction**: In squads, one player defends outside the zone while others extract. The defender extracts last

---

## Counter-Play Design

### Exit Camping

Exit camping (waiting near extraction zones to ambush extracting players) is a legitimate strategy that creates tension but must be balanced:

**For the Camper:**
- Advantage: Knows exactly where players will go
- Disadvantage: Must wait (boredom factor), other players may approach from behind, extraction notification reveals their area

**For the Extractor:**
- Advantage: Multiple extraction zones available; can choose a different one
- Disadvantage: Must commit to a 30-second timer while stationary

### Anti-Camping Design Elements

| Mechanism | How It Works |
| :-------- | :----------- |
| Multiple extraction zones | 3-4+ standard zones per map ensures campers cannot cover all exits |
| Varied approach routes | Each extraction zone has 3+ entry routes with different cover options |
| Zone visibility changes | Some zones have configurable cover (deployable sandbags, smoke) |
| Noise symmetry | Campers in hiding still generate noise when shifting position. Patient extractors can detect them |
| Map notification | "A player is extracting at [zone]" alerts campers but also alerts potential third-party players who may attack the camper |
| Contamination pressure | At 12:00+, campers must also extract or die. Late-game camping becomes self-defeating |

**Design Philosophy**: Exit camping should be a viable but risky strategy. The game should not eliminate it (it creates tension), but should provide enough tools for extractors to counter it.

<!-- REF_IMAGE: Extraction zone tactical analysis — top-down map view of one extraction zone showing approach routes (green), common camping positions (red), and cover positions within the zone (blue) -->

---

## Extraction Notifications

### Information Broadcasting

| Event | Who Sees It | What They See | Sound |
| :---- | :---------- | :------------ | :---- |
| Player enters extraction zone | Zone-nearby players (50m) | No UI notification, but can hear entry footsteps | Footstep audio |
| Player activates extraction | All players on map | Map notification: "[Zone Name] — Extraction in progress" | Helicopter/vehicle approach audio |
| Extraction successful | All players on map | Map notification: "[Zone Name] — Player extracted" | Helicopter departure / vehicle engine fading |
| Extraction interrupted | Zone-nearby players (80m) | No map notification | Helicopter abort audio (engines powering down) |

### Information Asymmetry Design

- **The extractor** knows exactly how long they must survive (timer visible)
- **The attacker** knows where the extraction is happening (map notification) but not how much time is left
- The **third-party player** (neither extracting nor camping) sees the notification and must decide: investigate (risk) or ignore (safety)

This three-way dynamic creates emergent gameplay. A camper might be ambushed by a third party while watching for the extractor.

---

## Failed Extraction Outcomes

### Death in Raid

| Cause | Outcome | Items Lost | Items Saved |
| :---- | :------ | :--------- | :---------- |
| Killed by player | KIA | All equipped and backpack items | Secure Container contents (lose FIR status) |
| Killed by AI | KIA | All equipped and backpack items | Secure Container contents (lose FIR status) |
| Timer expired | MIA (Missing in Action) | All equipped and backpack items | Secure Container contents (lose FIR status) |
| Contamination death | MIA | All equipped and backpack items | Secure Container contents (lose FIR status) |
| Disconnection (timeout) | MIA after 5 minutes | All equipped and backpack items | Secure Container contents |

### Insurance Recovery

- If a player dies and their body is **not looted** by another player, insured items have a chance to be returned:
  - **Standard Insurance**: 24-hour return delay, 70% recovery chance, costs 10% of item value
  - **Premium Insurance**: 12-hour return delay, 90% recovery chance, costs 20% of item value
  - **Insurance does NOT cover**: Items placed in backpack loot (only equipped gear)
  - If an enemy loots the item from the body, insurance is void for that specific item

---

## Cooperative Extraction Design

### Scav-PMC Cooperation

The Cooperative Extraction zone encourages unlikely alliances:

- A PMC player and a Scav player (or players from opposing factions) must both be present
- Both players interact with their respective sides of a dual-mechanism gate
- 20-second timer starts when both sides are activated simultaneously
- If either player attacks the other during the timer, the extraction is canceled and both receive a reputation penalty

### Trust Mechanics

| Action | Reputation Effect |
| :----- | :---------------- |
| Successful cooperative extraction | +0.5 reputation with opposing faction. +200 bonus XP |
| Betrayal during cooperative extraction (attack partner) | -1.0 reputation with opposing faction. Marked as "hostile" for next 3 raids |
| Multiple successful cooperations | Unlocks special barter deals with the opposing faction's traders |

**Design Intent**: Cooperative extraction adds a social layer to the game. It rewards players who take risks on trust and creates memorable emergent stories: "We were enemies, but we needed each other to get out."

<!-- REF_IMAGE: Cooperative extraction gate — illustration showing two players on opposite sides of a heavy gate, each holding an activation lever, with the shared timer counting down overhead -->

---

## Design Rationale

### Why Extraction Is the Core Identity

The extraction mechanic is what separates this genre from battle royales, arena shooters, and looter-shooters:

| Genre | End Condition | Player Agency |
| :---- | :------------ | :------------ |
| Battle Royale | Last team standing (forced to fight) | Low — must fight to win |
| Arena Shooter | Score or time limit | Low — continuous combat |
| Looter-Shooter | Mission complete (always extractable) | High — but no risk |
| **Extraction Shooter** | **Voluntary extraction (choose when to leave)** | **Maximum — every raid ends by player choice** |

The voluntary extraction mechanic means **every raid is a story the player tells themselves**: "I could have left earlier, but I pushed for one more room." This narrative ownership is the primary retention driver.

### Extraction Zone Placement Guidelines

- Zones should be placed at **map edges** and **distinct landmarks** (helipad, dock, train station)
- Each zone must have **multiple approach routes** (minimum 3)
- No zone should be within **100m of a high-value loot area** (prevents camp-from-loot-room strategies)
- At least one zone per map should be in a **naturally defensible position** (building, elevated platform) to give extractors a fair chance
