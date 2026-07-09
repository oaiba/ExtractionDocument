---
title: "Extraction Mechanics"
type: docs
weight: 6
---

### Tổng Quan

Extraction is the climax of every raid. It is the singular moment where all accumulated risk, loot, và quyết định converge into a binary outcome: escape với everything, hoặc lose it all. The extraction hệ thống được thiết kế để tạo maximum tension thông qua a combination of location commitment, thời gian vulnerability, và environmental signaling.

> Xem [cốt lõi Gameplay cơ chế](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/CoreGameplay/README.md) for the raw extraction process specification và zone type parameters. This tài liệu focuses on the interaction design, người chơi psychology, và counter-play dynamics.

***

### Extraction Zone Types

#### Standard Extraction

| Property      | chi tiết                                                       |
| ------------- | ------------------------------------------------------------ |
| Count per Map | 3-4 zones                                                    |
| Availability  | Always active from raid start to raid end                    |
| Timer         | 30 seconds once activated                                    |
| Capacity      | Unlimited — any number of Người chơi có thể extract simultaneously |
| Location      | Fixed, known locations marked on map (green helicopter icon) |
| Noise         | Helicopter approach audio at timer start. Audible at 80m+    |
| Risk Level    | High — known locations are frequently watched và camped     |

#### Emergency Extraction

| Property      | chi tiết                                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------ |
| Count per Map | 1-2 zones                                                                                                    |
| Availability  | Requires a cụ thể chính hoặc quest item to unlock                                                              |
| Timer         | 15 seconds (faster extraction)                                                                               |
| Capacity      | Single cách dùng — zone closes sau one successful extraction                                                     |
| Location      | Hidden hoặc unmarked. người chơi must discover thông qua exploration hoặc map knowledge                               |
| Noise         | Quiet extraction (no helicopter). Faint radio static audio (audible at 20m)                                  |
| Risk Level    | Medium — harder to find, so less likely to be camped. nhưng reaching it may require traversing dangerous areas |

#### Vehicle Extraction

| Property      | chi tiết                                                                  |
| ------------- | ----------------------------------------------------------------------- |
| Count per Map | 1 per map                                                               |
| Availability  | Always active, nhưng limited capacity                                     |
| Timer         | 45 seconds (vehicle must arrive và load)                               |
| Capacity      | Maximum 4 người chơi. First-come-first-served                              |
| Location      | Road hoặc dock. Vehicle drives/arrives trong khi the timer                   |
| Noise         | Very High — engine rumble, horn blast. Audible across most of the map   |
| Risk Level    | Very High — longest timer, loudest signal. Attracts every nearby người chơi |

#### Cooperative Extraction

| Property      | chi tiết                                                                                                      |
| ------------- | ----------------------------------------------------------------------------------------------------------- |
| Count per Map | 1 per map                                                                                                   |
| Availability  | Requires 2+ người chơi from different factions to activate simultaneously                                      |
| Timer         | 20 seconds                                                                                                  |
| Capacity      | 2-4 người chơi from mixed factions                                                                             |
| Location      | Neutral zone. Special door/gate that requires simultaneous activation from both sides                       |
| Noise         | Moderate — gate mechanism sound (audible at 30m)                                                            |
| Reward        | Reputation bonus với both factions. XP multiplier for cooperation                                          |
| Risk Level    | Low combat risk (cooperation), nhưng high trust risk (the other người chơi could betray you sau the gate opens) |

#### Paid Extraction (Future tính năng)

| Property      | chi tiết                                                                                    |
| ------------- | ----------------------------------------------------------------------------------------- |
| Count per Map | 1 per map                                                                                 |
| Availability  | Requires in-raid currency payment (e.g., $5,000 Credits found trong khi the raid)            |
| Timer         | 25 seconds                                                                                |
| Location      | Metro station, underground passage                                                        |
| Noise         | Low — underground, muffled                                                                |
| Risk Level    | Low-Medium — chi phí barrier prevents casual cách dùng. Underground location limits camping angles |

***

### Extraction Process flow

#### Step-by-Step Interaction

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

#### Cross-Platform

Extraction rules are identical on PC, console, và mobile. **Activate extraction:** PC/console cách dùng hold (e.g. Hold E); mobile may cách dùng tap-và-hold hoặc a dedicated button với the same 1.5 s commit. **Timer visibility:** The countdown và zone boundary are shown on HUD on all platforms; layout và size may adapt (Xem [Controls](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Controls.md) và [User Interface](https://github.com/oaiba/ExtractionDocument/blob/main/content/Visuals/UserInterface.md)). Same interruption rules apply regardless of input method.

***

### Interruption Rules

The extraction timer resets to zero under the following conditions:

| Interruption Trigger                      | Reset Behavior                     | Design Reason                                                                   |
| ----------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------- |
| người chơi leaves zone boundary (even 1 step) | Full reset                         | Prevents người chơi from hopping in và out of the zone                            |
| người chơi takes ANY damage (even 1 HP)       | Full reset                         | tạo counter-play. Attackers can deny extraction với a single bullet        |
| người chơi uses a healing item                | Full reset                         | Forces a choice: heal first, then extract. Cannot do both simultaneously        |
| Teammate dies within the zone             | Full reset (squad extraction mode) | Squad phải được complete to extract together. Dead teammate = abort hoặc leave them |
| Grenade/ability lands in the zone         | Full reset for all người chơi in zone | AOE denial is a valid extraction disruption tactic                              |

#### Interruption Counter-Measures

* **Smoke Grenades**: Deploying smoke in the extraction zone blocks line-of-sight, preventing accurate shots from outside
* **Decoy Abilities**: Some operators have decoy hoặc distraction abilities that can redirect địch attention
* **Pre-Clearing**: Sweep the extraction area trước activating. Check common camping spots
* **Staggered Extraction**: In squads, one người chơi defends outside the zone while others extract. The defender extracts last

***

### Counter-Play Design

#### Exit Camping

Exit camping (waiting near extraction zones to ambush extracting người chơi) is a legitimate strategy that tạo tension nhưng phải được balanced:

**For the Camper:**

* Advantage: Knows exactly where người chơi will go
* Disadvantage: Must wait (boredom factor), other người chơi may approach from behind, extraction notification reveals their area

**For the Extractor:**

* Advantage: Multiple extraction zones available; can choose a different one
* Disadvantage: Must commit to a 30-second timer while stationary

#### Anti-Camping Design Elements

| Mechanism                 | How It Works                                                                                                               |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Multiple extraction zones | 3-4+ standard zones per map ensures campers cannot cover all exits                                                         |
| Varied approach routes    | Each extraction zone has 3+ entry routes với different cover options                                                      |
| Zone visibility changes   | Some zones have configurable cover (deployable sandbags, smoke)                                                            |
| Noise symmetry            | Campers in hiding still generate noise khi shifting position. Patient extractors can detect them                          |
| Map notification          | "A người chơi is extracting at \[zone]" alerts campers nhưng also alerts potential third-party người chơi who may attack the camper |
| Contamination pressure    | At 12:00+, campers must also extract hoặc die. Late-game camping becomes self-defeating                                      |

**Design Philosophy**: Exit camping nên được a viable nhưng risky strategy. The game không nên eliminate it (it tạo tension), nhưng should provide enough tools for extractors to counter it.

***

### Extraction Notifications

#### Information Broadcasting

| Event                         | Who Sees It               | What They Xem                                             | Sound                                          |
| ----------------------------- | ------------------------- | --------------------------------------------------------- | ---------------------------------------------- |
| người chơi enters extraction zone | Zone-nearby người chơi (50m) | No UI notification, nhưng can hear entry footsteps          | Footstep audio                                 |
| người chơi activates extraction   | All người chơi on map        | Map notification: "\[Zone Name] — Extraction in progress" | Helicopter/vehicle approach audio              |
| Extraction successful         | All người chơi on map        | Map notification: "\[Zone Name] — người chơi extracted"       | Helicopter departure / vehicle engine fading   |
| Extraction interrupted        | Zone-nearby người chơi (80m) | No map notification                                       | Helicopter abort audio (engines powering down) |

#### Information Asymmetry Design

* **The extractor** knows exactly how long they must survive (timer hiển thị rõ)
* **The attacker** knows where the extraction is happening (map notification) nhưng not how much thời gian is left
* The **third-party người chơi** (neither extracting nor camping) sees the notification và must decide: investigate (risk) hoặc ignore (safety)

This three-way dynamic tạo emergent gameplay. A camper might be ambushed by a third party while watching for the extractor.

***

### failed Extraction Outcomes

#### Death in Raid

| Cause                   | Outcome                 | Items Lost                      | Items Saved                                 |
| ----------------------- | ----------------------- | ------------------------------- | ------------------------------------------- |
| Killed by người chơi        | KIA                     | All equipped và backpack items | Secure Container contents (lose FIR status) |
| Killed by AI            | KIA                     | All equipped và backpack items | Secure Container contents (lose FIR status) |
| Timer expired           | MIA (Missing in Action) | All equipped và backpack items | Secure Container contents (lose FIR status) |
| Contamination death     | MIA                     | All equipped và backpack items | Secure Container contents (lose FIR status) |
| Disconnection (timeout) | MIA sau 5 minutes     | All equipped và backpack items | Secure Container contents                   |

#### Insurance Recovery

* nếu a người chơi dies và their body is **not looted** by another người chơi, insured items have a chance to be returned:
  * **Standard Insurance**: 24-hour return delay, 70% recovery chance, costs 10% of item giá trị
  * **Premium Insurance**: 12-hour return delay, 90% recovery chance, costs 20% of item giá trị
  * **Insurance covers**: All equipped gear và items stored in rig và backpack (both are insured). Items in the Secure Container do not need insurance — they are always kept.
  * **Insurance does NOT cover**: Items explicitly removed from the body by another người chơi (nếu looted, insurance is void for that cụ thể item)
  * nếu an địch loots the item from the body, insurance is void for that cụ thể item

***

### Cooperative Extraction Design

#### Scav-PMC Cooperation

The Cooperative Extraction zone encourages unlikely alliances:

* A PMC người chơi và a Scav người chơi (hoặc người chơi from opposing factions) must both be present
* Both người chơi interact với their respective sides of a dual-mechanism gate
* 20-second timer starts khi both sides are activated simultaneously
* nếu either người chơi attacks the other trong khi the timer, the extraction is canceled và both receive a reputation penalty

#### Trust cơ chế

| Action                                                  | Reputation Effect                                                           |
| ------------------------------------------------------- | --------------------------------------------------------------------------- |
| Successful cooperative extraction                       | +0.5 reputation với opposing faction. +200 bonus XP                        |
| Betrayal trong khi cooperative extraction (attack partner) | -1.0 reputation với opposing faction. Marked as "hostile" for next 3 raids |
| Multiple successful cooperations                        | Unlocks special barter deals với the opposing faction's traders            |

**Design Intent**: Cooperative extraction adds a social layer to the game. It rewards người chơi who take risks on trust và tạo memorable emergent stories: "We were địch, nhưng we needed each other to get out."

***

### Design Rationale

#### Why Extraction Is the cốt lõi Identity

The extraction cơ chế is what separates this genre from battle royales, arena shooters, và looter-shooters:

| Genre                  | End Condition                                   | người chơi Agency                                  |
| ---------------------- | ----------------------------------------------- | ---------------------------------------------- |
| Battle Royale          | Last team standing (forced to fight)            | Low — must fight to win                        |
| Arena Shooter          | Score hoặc thời gian limit                             | Low — continuous combat                        |
| Looter-Shooter         | Mission complete (always extractable)           | High — nhưng no risk                             |
| **Extraction Shooter** | **Voluntary extraction (choose khi to leave)** | **Maximum — every raid ends by người chơi choice** |

The voluntary extraction cơ chế means **every raid is a story the người chơi tells themselves**: "I could have left earlier, nhưng I pushed for one more room." This narrative ownership is the primary retention driver.

#### Extraction Zone Placement Guidelines

* Zones nên được placed at **map edges** và **distinct landmarks** (helipad, dock, train station)
* Each zone must have **multiple approach routes** (minimum 3)
* No zone nên được within **100m of a high-giá trị loot area** (prevents camp-from-loot-room strategies)
* At least one zone per map nên được in a **naturally defensible position** (building, elevated platform) to give extractors a fair chance
