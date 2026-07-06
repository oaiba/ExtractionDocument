---
title: "Tutorial Raid: \"Operation Zero\""
type: docs
---

##  Design Goal: "Teach to Survive"

The tutorial is **NOT** a shooting gallery. It is a **Safety Drill**.
Most players quit Extraction Shooters because they loot, get lost, and die to a camper without knowing why.
"Operation Zero" mimics a real raid but removes the punishment (Gear Fear).

**Tutorial covers five learning pillars:**
1. Movement & Noise awareness
2. Looting & Inventory management
3. Medical triage & healing
4. Operator selection & ability use
5. Economy, extraction, and the debrief loop

> **Cross-References:** [Core Gameplay Loop](../Gameplay/CoreLoop.md) — Phase 1–5 overview; [Hero Abilities](../Gameplay/Hero_Abilities.md) — operator selection; [Matchmaking & Lobby](../Gameplay/Matchmaking_Lobby.md) — tutorial routing; [Safe House Design](Safe_House_Design.md) — post-tutorial hideout introduction; [Post-Game Debrief](../Gameplay/Post_Game_Debrief.md) — first-run debrief experience.

---

##  Pre-Tutorial: Operator Selection Screen (Guided)

Before Operation Zero begins, the player is guided through the **Operator Selection screen** for the first time.

| Step | What Happens | UI State |
| :--- | :----------- | :------- |
| 1 | Welcome message: "Choose your Operator — each has unique skills." | Pulsing arrow pointing to operator grid |
| 2 | Three operators shown: **Mamba** (Assault), **Hawk** (Scout), **Glitch** (Specialist) | Other operators greyed — Beta+ |
| 3 | Player hovers each — ability preview appears (passive + active tooltip) | Tooltip shows simplified ability summary |
| 4 | Player selects one — confirmed with audio sting | Brief character voice line |
| 5 | "This is your Operator for this training raid. You can change before each real raid." | Fade into loadout screen |

**Locked loadout:** Tutorial provides a fixed loadout (M4A1 + Class 2 vest) regardless of operator selected. Operator choice affects only the ability tutorial segment.

---

##  The Mission Script (Expanded)

### Phase 1: The Crash (Movement)
- **Context:** You wake up near a crashed helicopter in a dense forest (safe start zone).
- **Action sequence:**
  1. **Slow Walk prompt:** "Hold [Walk key] — move quietly. Your noise range is shown on the minimap."
  2. **Crouch:** Under fallen debris — force-crouch tutorial, noise meter shows "Near Silent."
  3. **Vault:** Over a broken helicopter wing — vaulting input shown.
  4. **Scripted fall / Fracture:** Falling off wreckage causes a Leg Fracture (scripted).
  5. **Heal:** Use a Splint from pocket slot — medical menu tutorial. Shows body part diagram; Leg highlighted.
  6. **Movement penalty visible:** Walk speed reduced with fracture; heal resolves it — teaches consequence + recovery.

---

### Phase 2: The Scavenger Camp (Stealth / Combat / Ability)
- **Context:** 2 AI Scavs loot a campfire 30m away.
- **Choice presented:** UI prompt: "Approach quietly or engage directly?"

**Stealth path:**
1. Crouch-walk through tall grass — Noise Meter shows "1m range" in grass.
2. Pass within 5m of Scavs without alert — teaches stealth radius.
3. Silent takedown available in tutorial only (context-sensitive melee).

**Loud path:**
1. Shoot — Scavs alert. Third Scav appears from treeline (reinforcement mechanic).
2. Tutorial shows suppression ring when bullets land near player.
3. Kill all three — teaches combat feedback (hit marker, kill audio sting).

**Ability Tutorial (after combat):**
- After clearing camp: "You have a special skill. Press [Ability key] to use it."
- Short ability tutorial per operator:

| Operator chosen | Ability shown |
| :-------------- | :------------ |
| **Mamba** | Adrenaline Rush — sprint boost. "Use this to close distance fast or escape." |
| **Hawk** | Spotter Drone — deploy and view from drone. "Use this to scout before pushing." |
| **Glitch** | Tactical Overlay — minimap reveal. "Use this when enemies are hidden behind cover." |

- Ability cooldown explained: timer shown, "It recharges on its own — no resources needed."
- **Loot camp:** Scav bodies have food, ammo, and a Keycard (quest item). Quest item glow introduced.

---

### Phase 3: The Bunker (Looting & Inventory)
- **Context:** Use the Keycard to open a bunker door.
- **Action sequence:**
  1. **Interact:** Hold F / Circle on door with Keycard — lock animation plays.
  2. **Enter bunker:** Indoor camera transition per [Camera System](../Gameplay/Camera_System.md) — roof cuts away.
  3. **Loot weapon box:** Search bar appears — 5s timer. "This container takes time to search."
  4. **Inventory Tetris:** Box contains a large Plate Carrier (2×4). Current backpack has no space.
  5. **Rearrange tutorial:** UI highlights smaller items to drop. "Drag and drop to fit. Heavier gear = better protection, but slower movement."
  6. **Weight reminder:** Bar ticks up to Tier 2 (moderate) after equipping vest. Speed reduction noted.
  7. **Secure Container:** Tutorial shows a small Secure Container slot. "Items here survive any death. Put valuables here."

---

### Phase 4: The Minimap & Pings (Navigation)
- **Context:** Exiting the bunker — teammate joins (AI companion for solo tutorial).
- **Action sequence:**
  1. **Minimap introduction:** Compass ring, teammate icon, grid overlay explained.
  2. **Ping tutorial:** "Tap the Ping button to mark a location for your team."
     - Single tap → "Move here" marker placed.
     - Danger double-tap → Red danger placed on enemy position.
  3. **Ping wheel:** Hold ping → wheel appears → player selects "Looting."
  4. **Grid callout:** "Enemies in B4" — tutorial shows how grid overlays the tactical map.
  5. AI companion demonstrates pinging back: teammate marker appears on minimap.

---

### Phase 5: The Extraction (Pressure & Debrief)
- **Context:** Alarm triggers. "Contamination Rising. Extraction Active: 3 minutes."
- **Contamination preview:** Outer map boundary starts glowing red. Timer shown clearly.
- **Action sequence:**
  1. **Sprint to extraction:** Player must navigate using minimap — extraction zone now pulsing green.
  2. **Scripted encounter:** AI Sniper fires (scripted miss) — suppression effect plays. "Get to cover!"
  3. **Cover tutorial:** Crouch behind cargo crate — damage blocked. "Cover behind solid objects blocks incoming fire."
  4. **Extraction hold:** Walk into green zone — "Hold [Extract key] for 10 seconds."
  5. **Interruption test:** Tutorial AI fires once — timer resets. "Incoming damage resets your extraction timer! Eliminate threats first."
  6. **AI cleared by companion:** Player re-holds. Timer completes. Screen fades.

---

### Tutorial Outcome Screen (Custom Debrief)

After extraction, a special first-run debrief plays:

| Section | Content | Notes |
| :------ | :------ | :---- |
| **"You Made It"** | Large EXTRACTED banner | Same as normal debrief |
| **XP earned** | Guided tooltip on each XP line — "This is how you grow your operator." | First-run only: each line has explanation popup |
| **Loot kept** | Inventory shown — "These items are now in your Stash." | |
| **Starter Kit granted** | See reward table below | Auto-deposited into stash |
| **"Next Step" guidance** | "Visit your Safe House → then deploy on your first real raid." | Highlighted button |

---

##  Reward: "Starter Kit"

Completing the tutorial grants:

| Item | Detail |
| :--- | :----- |
| M4A1 (Standard) | 3 magazines included |
| Class 2 Soft Vest | Damaged (70% durability) — teaches that gear degrades |
| IFAK Kit ×2 | Basic healing — teaches stash provisioning |
| Water Bottle ×2 | Hydration for first real raid |
| $5,000 | Enough for 1 insurance + basic ammo purchase |
| **Operator Unlock** | The operator selected in tutorial is unlocked at Level 1 |

> *This gear is yours. If you lose it in the next raid, it's gone forever. Welcome to the Zone.*

---

##  Post-Tutorial: Safe House Onboarding

After the tutorial debrief, the player is guided through the Safe House for the first time:

| Step | Prompt | What's Shown |
| :--- | :----- | :----------- |
| 1 | "This is your Safe House — your base between raids." | Full Safe House view |
| 2 | "Your Stash holds everything you've kept." | Stash grid with starter kit items highlighted |
| 3 | "The Generator powers your Safe House. Keep it fueled." | Generator module, fuel icon |
| 4 | "The Scav Box generates passive loot over time." | Scav Box, 6h timer |
| 5 | "Visit Viktor to get your first mission." | Trader highlight — Viktor |
| 6 | "Ready to deploy? Use the Deploy button when prepared." | Deploy button pulsing |

Each step is dismissible — players who know extraction games can skip the tour.

---

##  "Soft" Tutorials (Loading Screen Tips)

Don't rely just on the raid. Use the downtime:

- *"Sound is your radar. If you can hear them, they can hear you."*
- *"Don't peek the same angle twice."*
- *"Loot is heavy. Stamina drains faster when over 30kg."*
- *"If you find an Injector, check the description. Some kill you."*
- *"The Secure Container always saves its contents — even on death."*
- *"Bleed damage ignores armor. Stop the bleed first."*
- *"Overweight movement is loud. Drop low-value loot before extracting."*
- *"Extraction zones are discovered by proximity — explore to find more options."*
- *"Abilities recharge automatically. Using them is always correct."*

---

##  Anti-Frustration Features

| Feature | Detail |
| :------ | :----- |
| **God Mode (HP floor)** | Player HP cannot drop below 1 during tutorial. Screen turns red, but no restart needed. |
| **Infinite Ammo** | Magazines refill instantly in tutorial only. |
| **Waypoint Markers** | 3D UI guide markers active (disabled in main game). |
| **Ability always cooled down** | Ability cooldown removed during tutorial — player can use ability freely to experiment. |
| **No FIR penalty** | Tutorial loot is marked with special "Tutorial" tag — no barter/quest value, prevents economy exploit. |
| **No death state** | Downstate does not activate in tutorial. Player cannot die. |
| **Restart available** | Player can restart Operation Zero from the main menu any time. No cost or penalty. |

---

##  Cross-References

- [Core Gameplay Loop](../Gameplay/CoreLoop.md) — Full 5-phase loop overview that tutorial teaches in compressed form.
- [Hero Abilities](../Gameplay/Hero_Abilities.md) — Operator classes, ability structures, cooldown rules.
- [Medical System](../Gameplay/Medical_System.md) — Injury types and treatment demonstrated in Phase 1.
- [Looting & Inventory](../Gameplay/Looting_Interactions.md) — Container search time, Secure Container, Tetris inventory.
- [Extraction Mechanics](../Gameplay/Extraction_Mechanics.md) — Extraction hold, timer reset on damage, zone types.
- [Camera System](../Gameplay/Camera_System.md) — Indoor camera transition in Phase 3 Bunker.
- [Matchmaking & Lobby](../Gameplay/Matchmaking_Lobby.md) — Tutorial routing; new accounts auto-routed to tutorial once.
- [Safe House Design](Safe_House_Design.md) — Safe House onboarding step after tutorial debrief.
- [Post-Game Debrief](../Gameplay/Post_Game_Debrief.md) — Tutorial uses custom version of debrief; normal version first-run after.
- [NavigationAndMap](NavigationAndMap.md) — Minimap and ping system taught in Phase 4.
