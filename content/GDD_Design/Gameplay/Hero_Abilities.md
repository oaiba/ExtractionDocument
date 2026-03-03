---
title: "Hero Abilities (Operators)"
type: docs
weight: 5
---

## Overview

Operators are the hero layer of the extraction shooter: each has a **class**, a **passive trait**, one or two **active abilities** (gadgets/skills), and a **signature** (ultimate) ability. Abilities add identity and team composition depth without replacing the core loop of loadout, loot, and extract. All operators are earnable through progression; no pay-to-win.

**Design pillars:**

- **Gunplay first:** Abilities support and complement gunplay — they never one-shot or replace weapons as the primary kill tool.
- **Meaningful cooldowns:** Each ability use is a deliberate decision. Abilities are impactful but not spammable.
- **Full counterplay:** Every ability has a telegraph (audio/visual), a counter, and a weakness. No undodgeable effects.
- **Extraction-aware:** Ability rules change near extraction zones (healing abilities cancel extract timer).
- **Cross-platform parity:** Abilities work identically on PC and mobile; only input method differs.

For high-level operator choice in pre-raid planning, see [Core Gameplay Loop](CoreLoop.md). For scope (Alpha 3 operators, Beta 5), see [MVP Scope](../../ProjectScope/MVP.md). For pillar alignment (Task-Driven Agency, Persistent Progression), see [Design Pillars](../../ProjectScope/design-pillars-enhanced.md).

---

## Class Roster and Base Stats

Each class has inherent stat modifiers that define their role before any ability or gear is applied.


| Class          | Role                | HP Modifier   | Speed Modifier | Base carry weight bonus | Rig restriction            | Availability |
| -------------- | ------------------- | ------------- | -------------- | ----------------------- | -------------------------- | ------------ |
| **Assault**    | Entry / aggression  | 100% (440 HP) | 100%           | 0 kg                    | Any rig                    | Alpha        |
| **Scout**      | Recon / mobility    | 90% (396 HP)  | 105%           | -2 kg (lighter loadout) | Light or Standard rig only | Alpha        |
| **Support**    | Sustain / utility   | 100% (440 HP) | 95%            | +5 kg (extra carry)     | Any rig                    | Alpha        |
| **Tank**       | Anchor / durability | 115% (506 HP) | 90%            | +3 kg (extra carry)     | Heavy or Armored rig only  | Beta         |
| **Specialist** | Tech / gadget       | 95% (418 HP)  | 100%           | 0 kg                    | Any rig                    | Beta         |


**Alpha** (technical test): Assault, Scout, Support — 3 operators.
**Beta** (soft launch): Add Tank, Specialist — total 5 operators.
**Launch and beyond:** 8+ operators, 2 per class (see [MVP](../../ProjectScope/MVP.md) feature matrix).

---

## Ability Structure

Each operator has three layers of abilities. Numbers below are first-pass design values (will be adjusted in balance passes).

### Layer 1: Passive Trait

- **Always active** — no cooldown, no input required.
- **Small, consistent effect** — +5–15% to a single stat, or a conditional trigger (e.g. "on kill").
- **Identity-defining** — tells the player "this is what this operator does differently."
- Does not dominate fights; supports class fantasy and mastery.

### Layer 2: Active Abilities (1–2 per operator)

- **Activated via ability button** (PC: Q/E or custom bind; Mobile: on-screen buttons).
- **Cooldown: 30–90 seconds** depending on impact. Cooldown starts after effect ends.
- **Resource cost (optional):** Some abilities consume a physical item (e.g. drone charges) in addition to cooldown.
- **Telegraphed:** Activation produces a sound cue (audible at 15–20 m) and a visual indicator (smoke trail, device deploy animation 0.5–1.0 s).
- **Interruptible:** Getting hit or stunned during the 0.5–1.0 s cast animation cancels the ability and triggers 50% cooldown.

### Layer 3: Signature Ability (Ultimate)

- **1 per operator.** Stronger effect, longer cooldown.
- **Cooldown: 120–240 seconds**, OR **charge-based** (charge builds via kills +25%, assists +10%, damage dealt +1% per 50 damage, time alive +1% per 30s).
- **Maximum 2 uses per 20-minute raid** at best (ensures rarity and impact).
- **Defines operator identity** — the "hero moment" — but never fight-ending alone.
- **Telegraphed:** Loud audio cue (audible at 25 m), distinct visual effect (glow, aura, particles).

### Ability Economy: Cooldown Philosophy


| Impact level                         | Cooldown range      | Example                                 |
| ------------------------------------ | ------------------- | --------------------------------------- |
| Low (intel, minor buff)              | 30–45 s             | Spotter pulse, weapon swap speed buff   |
| Medium (area denial, heal, blind)    | 45–75 s             | Flashbang, smoke, medkit drop, drone    |
| High (team-wide buff, area lockdown) | 75–90 s             | Fortify zone, team speed boost          |
| Signature (ultimate)                 | 120–240 s or charge | Cloak, overdrive, group heal, area scan |


---

## Full Operator Specifications

### Assault — "Mamba"

> *"First in, last standing."*

**Identity:** Aggressive entry operator. Rewards kills with tempo advantages. Best when pushing into contested areas.


| Layer         | Ability         | Effect                                                                                                                                              | Duration                    | Cooldown | Audio tell                       | Visual tell                           |
| ------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------- | -------------------------------- | ------------------------------------- |
| **Passive**   | Adrenaline Rush | On kill: +12% move speed, +8% reload speed for 5 s. Stacks up to 2x.                                                                                | 5 s per stack               | N/A      | Heartbeat SFX (self only)        | Subtle red vignette on Mamba's screen |
| **Active 1**  | Flashbang       | Throw flashbang grenade. Enemies in 5 m radius: blinded 2.5 s, deafened 1.5 s. Allies in radius: minor flash 0.8 s.                                 | Instant (2.5 s effect)      | 60 s     | Pin-pull click + loud detonation | Bright white flash sphere             |
| **Active 2**  | Frag Charge     | Place directional explosive on surface. Detonates on proximity (2 m trigger) or manual trigger. 65 damage in 3 m cone.                              | Until triggered (max 120 s) | 75 s     | Beep when armed (audible 5 m)    | Small blinking red light              |
| **Signature** | Overdrive       | +20% move speed, +15% rate of fire, -10% recoil for 10 s. Taking lethal damage during Overdrive leaves Mamba at 1 HP instead (once per activation). | 10 s                        | 180 s    | War cry voice line + bass rumble | Red aura glow around character        |


**LOS/Visibility:** Flashbang — vision denial: blinds enemies 2.5 s in 5 m radius (no fog clear, no shared intel).

**Synergy notes:** Mamba's Flashbang enables aggressive pushes for the entire squad. Overdrive is best used to close distance or win a 1v2. Frag Charge covers flanks or extract zones.

---

### Scout — "Hawk"

> *"Information is ammunition."*

**Identity:** Intel and stealth operator. Excels at scouting ahead, marking enemies, and disengaging. Lower HP and rig restriction incentivize avoidance over direct combat.


| Layer         | Ability       | Effect                                                                                                                                                            | Duration                      | Cooldown                                  | Audio tell                                    | Visual tell                |
| ------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ----------------------------------------- | --------------------------------------------- | -------------------------- |
| **Passive**   | Light Step    | -20% footstep audible range. Crouch-walk is near-silent (audible at 1 m instead of 2–4 m).                                                                        | Always on                     | N/A                                       | None (that's the point)                       | None                       |
| **Active 1**  | Spotter Drone | Deploy a hovering drone. Marks enemies within 25 m radius for 8 s (visible to squad on HUD as red pings). Drone has 30 HP, can be shot down.                      | 8 s scan, then self-destructs | 75 s                                      | Buzzing motor sound (audible 20 m)            | Small drone visible in air |
| **Active 2**  | Motion Sensor | Place a ground sensor. Pings enemies moving within 10 m radius (not crouching/prone enemies). Lasts 90 s or until destroyed (15 HP). Max 2 placed.                | 90 s                          | 45 s                                      | Soft click on deploy                          | Tiny device; hard to spot  |
| **Signature** | Ghost Cloak   | Become semi-invisible for 6 s. 70% transparency (shimmer visible within 8 m). Firing, using items, or taking damage cancels cloak. Move speed +10% while cloaked. | 6 s                           | 210 s (or charge: 80% from assists/scans) | Electrical crackle on activate (audible 15 m) | Shimmer/distortion effect  |


**Synergy notes:** Hawk's intel feeds the entire squad's decision-making. Spotter Drone before pushing a room eliminates blind spots. Ghost Cloak enables flanking or emergency extraction escape.

**LOS/Visibility:** Spotter Drone — vision proxy 25 m (drone LOS); clears fog for squad; marks shared to squad. Motion Sensor — intel only (no LOS); pings moving enemies in 10 m; shared to squad; does not clear fog (ping only). Ghost Cloak — self-concealment; reduces visibility to enemies (shimmer within 8 m); not a vision proxy for squad.

**Counterplay:** Shoot the drone (30 HP). Crouch/prone to avoid Motion Sensor. Watch for cloak shimmer within 8 m.

---

### Support — "Cross"

> *"Nobody dies on my watch."*

**Identity:** Sustain and economy operator. Provides healing, extra carry capacity, and team utility. Slower speed but compensated by team value.


| Layer         | Ability        | Effect                                                                                                                                                            | Duration                      | Cooldown                                      | Audio tell                   | Visual tell                            |
| ------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | --------------------------------------------- | ---------------------------- | -------------------------------------- |
| **Passive**   | Pack Mule      | +5 kg carry weight threshold per tier. +1 rig hotkey slot (if rig supports it). Can search containers 15% faster.                                                 | Always on                     | N/A                                           | None                         | Slightly larger backpack visual        |
| **Active 1**  | Medkit Drop    | Drop a deployable medkit on the ground. Heals 1 player for 80 HP over 5 s (must interact to use). Does not repair destroyed limbs — use surgery kit for that.     | Available for 30 s after drop | 60 s                                          | Pouch-open sound on drop     | Green medkit on ground with cross icon |
| **Active 2**  | Stim Shot      | Inject self or adjacent ally. Removes pain effects, restores 15 Arm Stamina, reduces recoil -10% for 20 s. Does not restore HP.                                   | 20 s buff                     | 45 s                                          | Injection hiss               | Brief green flash on target            |
| **Signature** | Field Hospital | Create a 4 m radius healing zone for 12 s. All allies in zone: +8 HP/s, pain suppressed, slow limb repair (+5 HP/s to damaged limbs). Zone is visible to enemies. | 12 s                          | 240 s (or charge: assists, heals, time alive) | Generator hum (audible 20 m) | Green circular zone on ground          |


**Synergy notes:** Cross sustains prolonged fights. Field Hospital near a defensive position lets the squad hold ground. Medkit Drop lets allies heal independently while Cross continues fighting.

**Counterplay:** Field Hospital zone is visible and audible — throw grenades or push while enemies are stationary healing. Stim Shot does not restore HP.

**LOS/Visibility:** Field Hospital — zone is visible to all (enemy LOS not blocked); does not reveal or block vision.

**Extraction interaction:** Medkit Drop and Field Hospital both count as *healing actions* — **using them cancels extraction timer** if the user is in an extract zone. Cross must stop healing to extract.

---

### Tank — "Bastion" (Beta)

> *"Hold this ground."*

**Identity:** Area denial and anchor operator. High HP, heavy armor affinity, but slowest speed. Excels at holding choke points and protecting extracting teammates.


| Layer         | Ability           | Effect                                                                                                                                           | Duration             | Cooldown | Audio tell                                  | Visual tell                                   |
| ------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- | -------- | ------------------------------------------- | --------------------------------------------- |
| **Passive**   | Hardened          | +15% armor durability (armor degrades 15% slower). Blunt damage from blocked rounds reduced by 30%.                                              | Always on            | N/A      | None                                        | Reinforced armor visual (extra plate visible) |
| **Active 1**  | Deployable Cover  | Place a waist-high ballistic shield on the ground. 300 HP, blocks bullets from one direction. Lasts 60 s or until destroyed. Max 1 active.       | 60 s                 | 75 s     | Heavy metal clank on deploy (audible 15 m)  | Visible metal barricade                       |
| **Active 2**  | Concussion Blast  | Short-range (4 m cone) shockwave. Enemies hit: stagger 1.5 s, -30% move speed for 3 s, weapon sway +200% for 2 s. Costs 20 Arm Stamina.          | Instant (3 s effect) | 60 s     | Loud thump (audible 20 m)                   | Visible shockwave ripple                      |
| **Signature** | Goliath Protocol | For 15 s: -50% incoming damage, cannot sprint (locked to walk speed), +30% accuracy (reduced sway). Allies within 5 m gain -20% incoming damage. | 15 s                 | 240 s    | Metallic activation sequence (audible 25 m) | Orange glow + energy shield visual            |


**Synergy notes:** Bastion anchors a position while allies loot or extract. Deployable Cover creates instant defensive positions. Goliath Protocol during extraction timer makes the squad much harder to kill.

**LOS/Visibility:** Deployable Cover — one-direction LOS blocker; blocks vision (and shots) from one side; does not reveal.

**Counterplay:** Deployable Cover only blocks one direction — flank it. Goliath Protocol locks Bastion to walk speed — disengage and reposition. Concussion Blast is short-range — maintain distance.

---

### Specialist — "Glitch" (Beta)

> *"Knowledge is the weapon."*

**Identity:** Tech and disruption operator. Hacks, jams, and manipulates the battlefield. Versatile utility that scales with game knowledge and map awareness.


| Layer         | Ability          | Effect                                                                                                                                                                                                                                        | Duration               | Cooldown                                    | Audio tell                      | Visual tell                          |
| ------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------------------------------------- | ------------------------------- | ------------------------------------ |
| **Passive**   | Tech Savvy       | Interact with electronic devices 25% faster (doors, terminals, quest objectives). Can see trap devices (Motion Sensors, mines) within 8 m through walls (UI highlight).                                                                       | Always on              | N/A                                         | None                            | Highlighted traps show through walls |
| **Active 1**  | EMP Drone        | Launch a small drone that detonates at target location. 6 m radius EMP: disables enemy gadgets (drones, sensors, turrets) for 15 s, disrupts enemy HUD for 3 s (no compass, no stamina bar, no weight indicator). Drone has 20 HP mid-flight. | Instant (15 s disable) | 75 s                                        | Drone flight buzz + EMP crackle | Blue electric burst                  |
| **Active 2**  | Signal Jammer    | Place a device that prevents enemies within 12 m radius from using active abilities for 10 s. Does not affect passives. Jammer has 25 HP and can be destroyed. Max 1 active.                                                                  | 10 s                   | 90 s                                        | Electronic whine (audible 10 m) | Small device with blue glow          |
| **Signature** | Tactical Overlay | For 10 s: reveal all enemies within 40 m on the minimap for the entire squad. Enemies are shown as real-time pings (update every 0.5 s). Does not reveal through walls — shows last-known position if enemy enters cover.                     | 10 s                   | 210 s (or charge: assists, gadget destroys) | Radar ping sound (audible 20 m) | Blue scan wave emanates from Glitch  |


**Synergy notes:** Glitch counters other operators' gadgets and provides decisive intel for squad pushes. EMP Drone before a push disables Hawk's drones and Bastion's cover (electronics only — physical cover unaffected). Tactical Overlay enables coordinated squad assaults.

**LOS/Visibility:** Tech Savvy — see traps (Motion Sensors, mines) within 8 m through walls (UI highlight); no enemy reveal. Tactical Overlay — vision proxy 40 m; minimap reveal; last-known when enemy in cover; shared to squad.

**Counterplay:** EMP Drone is fragile (20 HP) — shoot it mid-flight. Signal Jammer is destroyable and audible. Tactical Overlay only reveals for 10 s and requires Glitch to be alive — kill Glitch to end the effect early.

---

## Ability Interaction Rules

### During Normal Raid


| Rule             | Detail                                                                                                                                                     |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Passive          | Always active. Unaffected by stuns, EMP, or death (deactivates on death obviously).                                                                        |
| Active abilities | Usable when off cooldown. 0.5–1.0 s cast animation — interruptible by damage/stun (50% cooldown refund).                                                   |
| Signature        | Usable when charged or off cooldown. 1.0 s activation animation — interruptible (75% cooldown/charge refund).                                              |
| Ability noise    | All active/signature abilities produce audio cues. Range varies per ability (see specs above).                                                             |
| Ability stacking | Same ability from two operators of the same class does NOT stack (prevents double-Mamba Overdrive). Different abilities from different operators DO stack. |
| Down state       | Downed players cannot use abilities. Passive deactivates in down state.                                                                                    |


### During Extraction

Per [Extraction Mechanics](Extraction_Mechanics.md):


| Ability type                                                                       | Usable during extract? | Cancels extract timer?    |
| ---------------------------------------------------------------------------------- | ---------------------- | ------------------------- |
| Passive                                                                            | Yes (always on)        | No                        |
| Offensive active (Flashbang, Frag Charge, Concussion Blast, EMP Drone)             | Yes                    | No                        |
| Intel active (Spotter Drone, Motion Sensor, Signal Jammer, Tactical Overlay)       | Yes                    | No                        |
| **Healing active** (Medkit Drop, Stim Shot, Field Hospital)                        | Yes, but...            | **Yes — cancels extract** |
| Signature (offensive: Overdrive, Ghost Cloak, Goliath Protocol, Tactical Overlay) | Yes                    | No                        |
| **Signature (healing: Field Hospital)**                                            | Yes, but...            | **Yes — cancels extract** |


**Design rationale:** The extraction timer is a high-stakes moment. Offensive and utility abilities create exciting defense scenarios. Healing abilities cancel extract to force the choice: heal and reset timer, or extract wounded. This prevents the "heal tank" exploit of endlessly healing during extraction.

### Interaction with Medical System

Operator healing abilities interact with the [Medical System](Medical_System.md):


| Interaction                       | Rule                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Medkit Drop vs Surgery Kit        | Medkit Drop restores HP but does NOT repair destroyed limbs. Surgery Kit (inventory item) is still required. |
| Field Hospital vs Destroyed Limbs | Field Hospital repairs damaged limbs (+5 HP/s) but does NOT restore from 0 HP (destroyed).                   |
| Stim Shot vs Pain                 | Stim Shot suppresses pain (like painkillers) for 20 s but does not heal.                                     |
| Ability healing vs Toxicity       | Ability heals contribute to toxicity accumulation the same as medical items (prevent healing spam).          |


### Interaction with Gear Weight

Per [Gear Mechanics](Gear_Mechanics.md), some operators have gear constraints:


| Operator                             | Gear constraint                                                                                  | Reason                                                                    |
| ------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| Scout (Hawk)                         | Light or Standard rig only (max 9 slots). Cannot equip Heavy rig or Armored rig.                 | Maintains scout mobility identity; prevents scout from also being a tank. |
| Tank (Bastion)                       | Heavy or Armored rig only (12 slots). Cannot equip Light rig. Must bring Class 3+ armor.         | Enforces tank fantasy; prevents tank from being a fast flanker.           |
| Support (Cross)                      | +5 kg carry weight per tier (via Pack Mule passive). Starts at higher effective weight capacity. | Supports "team mule" and "loot carrier" roles.                            |
| Assault (Mamba), Specialist (Glitch) | No restrictions.                                                                                 | Flexibility as generalist / tech roles.                                   |


### Interaction with LOS/Visibility

Per [LOS, Fog of War & Visibility](LOS_Fog_Visibility.md), abilities that reveal or block vision integrate with the shared team vision system. Summary:

| Operator | Ability | LOS/Visibility role | Range/Radius | Fog clearing? | Shared to squad? | Counterplay |
| :------- | :------ | :------------------ | :------------ | :------------ | :---------------- | :---------- |
| Hawk | Spotter Drone | Vision proxy | 25 m | Yes (drone LOS) | Yes | Shoot drone (30 HP) |
| Hawk | Motion Sensor | Intel | 10 m | No (ping only) | Yes | Crouch/prone; destroy (15 HP) |
| Hawk | Ghost Cloak | Self-conceal | 8 m shimmer | No | No | Shimmer visible 8 m; damage breaks |
| Glitch | Tech Savvy | Exception (traps) | 8 m | No | No (self) | N/A |
| Glitch | Tactical Overlay | Vision proxy | 40 m | Yes | Yes | Kill Glitch; hard cover |
| Obsidian (Recon) | Smoke | Blocker | 8 m radius | No | N/A | Avoid smoke; Thermal Block |
| Mamba | Flashbang | Vision denial | 5 m | No | No | Look away; cover |
| Bastion | Deployable Cover | LOS blocker | Directional | No | N/A | Flank; destroy (300 HP) |
| Cross | Field Hospital | Zone visible | 4 m zone | No | N/A (enemies see zone) | N/A |

Passives such as **Light Step** (Hawk) and **Tech Savvy** (Glitch) affect visibility indirectly (reduced sound detection; see traps through walls) but do not create vision proxies for the squad. All intel and vision from the abilities above is merged into the squad's shared visibility state (minimap fog, HUD marks). Counterplay preserves fair visibility per design pillars.


---

## Squad Composition and Synergy

### Recommended Compositions (3-player squads)


| Composition        | Operators                    | Playstyle                          | Strengths                     | Weakness                                |
| ------------------ | ---------------------------- | ---------------------------------- | ----------------------------- | --------------------------------------- |
| **Balanced**       | Assault + Scout + Support    | Push, intel, sustain               | Covers all roles; consistent  | No exceptional strength                 |
| **Aggro Rush**     | Assault + Assault + Scout    | Fast push, double flash + intel    | High kill potential           | Low sustain; one bad fight = squad wipe |
| **Goliath**       | Tank + Support + Specialist  | Hold position, deny area, heal     | Near-impenetrable defense     | Slow rotation; vulnerable to flanks     |
| **Intel Dominant** | Scout + Specialist + Assault | Map control, information advantage | Always know where enemies are | Less direct firepower and healing       |
| **Economy**        | Support + Scout + any        | High extract rate, carry more loot | Max loot extraction           | Weaker in direct PvP                    |


### Operator Synergy Matrix


|             | Mamba | Hawk                                  | Cross                     | Bastion                      | Glitch                       |
| ----------- | ----- | ------------------------------------- | ------------------------- | ---------------------------- | ---------------------------- |
| **Mamba**   | —     | ★★★ (flash + push on scanned enemies) | ★★ (heals after aggro)    | ★★ (breach while tank holds) | ★★★ (EMP then push)          |
| **Hawk**    | ★★★   | —                                     | ★★ (intel for safe heals) | ★★ (scout for anchor)        | ★★★ (double intel dominance) |
| **Cross**   | ★★    | ★★                                    | —                         | ★★★ (heal the tank)          | ★★ (general utility)         |
| **Bastion** | ★★    | ★★                                    | ★★★                       | —                            | ★★ (cover + jammer)          |
| **Glitch**  | ★★★   | ★★★                                   | ★★                        | ★★                           | —                            |


★ = Low synergy | ★★ = Moderate synergy | ★★★ = High synergy

---

## Balance Framework

### Ability Damage Budget

Abilities are never the primary damage source. The damage budget constrains ability damage relative to weapons:


| Damage source          | Damage per second (rough target) | % of total kill contribution |
| ---------------------- | -------------------------------- | ---------------------------- |
| Primary weapon         | 150–400 DPS (depending on tier)  | 70–85%                       |
| Grenades (inventory)   | 80–120 per grenade               | 5–15%                        |
| **Operator abilities** | **0–65 per activation**          | **5–15%**                    |
| Environmental / fall   | Variable                         | <5%                          |


### Counterplay Matrix

Every ability has at least one hard counter and one soft counter:


| Ability                     | Hard counter                                                | Soft counter                                                      |
| --------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------- |
| Flashbang (Mamba)           | Look away (reduces effect 70%)                              | Pre-positioned cover                                              |
| Frag Charge (Mamba)         | Glitch's Tech Savvy reveals it; shoot it (15 HP)            | Slow-walk to avoid proximity trigger                              |
| Spotter Drone (Hawk)        | Shoot it down (30 HP); EMP Drone destroys it                | Stay behind cover (drone marks LOS only)                          |
| Motion Sensor (Hawk)        | Crouch/prone avoids detection; Glitch sees it through walls | Destroy it (15 HP)                                                |
| Ghost Cloak (Hawk)          | AoE damage reveals; shimmer visible at 8 m                  | Audio cue on activation; predict movement                         |
| Medkit Drop (Cross)         | Push while enemy is healing (animation lock)                | Deny area where medkit dropped                                    |
| Field Hospital (Cross)      | Grenade into the zone; push stationary targets              | Disengage and wait out 12 s                                       |
| Deployable Cover (Bastion)  | Flank around it; grenades over it                           | EMP disables? No — physical object; must destroy (300 HP)         |
| Concussion Blast (Bastion)  | Stay beyond 4 m range                                       | Pre-aim before entering range                                     |
| Goliath Protocol (Bastion) | Disengage — he can't chase (walk speed only)                | Focus fire allies instead                                         |
| EMP Drone (Glitch)          | Shoot it mid-flight (20 HP)                                 | Spread out to limit AoE                                           |
| Signal Jammer (Glitch)      | Destroy it (25 HP); push outside 12 m                       | Wait out 10 s duration                                            |
| Tactical Overlay (Glitch)   | Kill Glitch to end effect                                   | Use hard cover to break LOS (shows last-known, not through walls) |


---

## Progression: Operator Mastery

### XP and Leveling


| Property                 | Value                                                                                                                                                     |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Max level per operator   | 50                                                                                                                                                        |
| XP sources               | Kills (+100), assists (+50), damage dealt (+1 per 10 dmg), survival time (+2/min), extraction bonus (+150), quest completion while playing operator (+75) |
| XP curve                 | Linear 1–20 (1,000 XP/level), scaling 21–50 (2,000 + 200 × (level − 20) XP/level)                                                                         |
| Estimated time to Lvl 50 | ~120–150 raids (60–75 hours)                                                                                                                              |


### Mastery Rewards


| Level | Reward type                                               | Example                                   |
| ----- | --------------------------------------------------------- | ----------------------------------------- |
| 5     | Operator skin (uncommon)                                  | Alternate color scheme                    |
| 10    | Passive bonus +1%                                         | Mamba: +1% sprint speed on kill           |
| 15    | Voice line pack                                           | Unique callouts                           |
| 20    | Passive bonus +2% (cumulative)                            | Hawk: +2% reduced footstep range          |
| 25    | Operator skin (rare)                                      | Tactical variant                          |
| 30    | Passive bonus +3% (cumulative)                            | Cross: +3% heal speed                     |
| 35    | Signature weapon skin                                     | Unique camo for operator's "canon" weapon |
| 40    | Passive bonus +4% (cumulative)                            | Bastion: +4% armor durability             |
| 45    | Operator title + badge                                    | Displayed on squad loadout screen         |
| 50    | Passive bonus +5% (cumulative) + Mastery skin (legendary) | Final bonus; gold/prestige skin           |


**Cap:** +5% passive bonus at Lvl 50. This is small enough that a Lvl 1 player with good aim beats a Lvl 50 player with bad positioning.

**No vertical power beyond passive bonus:** No new abilities, no ability upgrades, no stat increases beyond the +5% passive. All mastery rewards past the passive bonus are cosmetic.

### Operator Unlock Progression


| Operator              | Unlock method                         | Approximate time                   |
| --------------------- | ------------------------------------- | ---------------------------------- |
| Assault (Mamba)       | Free — starting operator              | Immediate                          |
| Scout (Hawk)          | Free — starting operator              | Immediate                          |
| Support (Cross)       | Free — starting operator              | Immediate                          |
| Tank (Bastion)        | Account level 10 OR 50,000 currency   | ~15–20 hours played                |
| Specialist (Glitch)   | Account level 15 OR 75,000 currency   | ~25–30 hours played                |
| Future operators (8+) | Account level requirement OR currency | Varies; never real-money exclusive |


---

## Cross-Platform Ability Balance

### Mobile vs PC Considerations


| Aspect                                  | PC (mouse + keyboard)        | Mobile (touch)                                                           | Parity solution                                                                                |
| --------------------------------------- | ---------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| Ability activation                      | Dedicated keybinds (Q, E, Z) | On-screen buttons (thumb accessible)                                     | Same cooldowns, same cast times; mobile buttons positioned for ergonomic access                |
| Aiming abilities (Flashbang, EMP Drone) | Precise mouse throw          | Aim-assist for thrown abilities (soft lock to nearest enemy at 30% pull) | Mobile gets aim assist on ability targeting; PC does not                                       |
| Drone control (Spotter Drone)           | Mouse cursor to position     | Auto-deploy at crosshair location                                        | Both: drone deploys at center-of-screen aim point; no manual drone flying                      |
| Signature timing                        | Quick reflexive activation   | Potential misclick risk                                                  | Signature requires confirm tap (double-tap on mobile, single press on PC) to prevent accidents |
| Counterplay (shooting drone)            | Easy with mouse aim          | Harder on mobile                                                         | Drone HP slightly higher on mobile lobbies? **No — maintain parity. Mobile players learn.**    |


---

## Anti-Abuse Rules


| Rule                                                            | Detail                                                                                          | Reason                                    |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------- |
| Ability cooldown starts after effect ends                       | Prevents pre-casting next ability during current one                                            | Anti-spam                                 |
| Same-class ability stacking blocked                             | Two Vipers in a squad: only one Flashbang at a time (second enters cooldown if first is active) | Prevents degenerate double-flash          |
| Healing during extraction cancels timer                         | Field Hospital and Medkit Drop reset the 15–30 s extract timer                                  | Prevents infinite heal-tanking at extract |
| Signature charge does not carry between raids                   | Charge resets to 0 at raid start; must build in-raid                                            | Prevents pre-charged ultimate farming     |
| Abilities disabled in safe zones (Safe House, vendors)             | No ability use outside raids                                                                    | Prevents griefing / exploit in menus      |
| Ability damage does not contribute to insurance fraud detection | Intentional self-damage with abilities is flagged                                               | Anti-exploit                              |


---

## Reference: Competitor Ability Structures


| Game                  | Ability layers                                  | Cooldown range                         | Notes for our design                           |
| --------------------- | ----------------------------------------------- | -------------------------------------- | ---------------------------------------------- |
| Delta Force: Hawk Ops | Trait (passive) + Tactical (active) + 2 Gadgets | 15–45 s (shorter; more action-focused) | We use longer cooldowns for extraction tension |
| ARC Raiders           | No fixed classes; loadout-based roles + gadgets | Gadget charges (limited per raid)      | We combine class identity with cooldown model  |
| Shatterline           | Passive + Active + Perks                        | 20–60 s                                | Similar structure; we add signature layer      |
| Overwatch 2           | Passive + 2 Abilities + Ultimate (charge-based) | 5–15 s abilities, 60–120 s ult         | Too fast for extraction; we 3–5x cooldowns     |
| Deadlock              | 4 active abilities, scaling with items          | 8–35 s base, reduced by items          | MOBA hybrid; we keep it simpler (3 layers)     |


**Our positioning:** Longer cooldowns than hero shooters, shorter than pure mil-sim. Each ability use is a "moment" — not constant spam, not once-per-match.

---

## Operators 6–10 — Pipeline (Launch and Beyond)

> **Status:** Concept-level. Numbers TBD in full design pass. These operators are designed to expand the meta-game by countering patterns established by the Alpha/Beta roster and serving underrepresented playstyles.

### Design Goals for Operators 6–10

| Goal | Detail |
| :--- | :----- |
| Expand class depth | Add a second Assault, second Scout, and a solo-viable class |
| Counter existing meta | Each new operator should have at least one ability that naturally counters an existing operator's strength |
| No class duplication without differentiation | Two Assault-class operators must feel distinct — different fantasy, different counterplay |
| Solo-viability design | One operator specifically designed to feel strong in solo queue (reduced squad dependency) |
| Diversity in fantasy | Different visual/character fantasy from existing 5 |

---

### Operator 6 — "PHAEDRA" · Class: Sniper (NEW CLASS)

> *A precision contractor who turns information into lethal advantage. Patient. Methodical. Devastating at range.*

| Layer | Ability | Detail |
| :---- | :------ | :----- |
| **Passive** | Eagle Eye | Aims slow walk has no aim cone penalty (other operators have slight penalty at slow walk). Headshot kills grant +20% stamina recovery instantly. |
| **Active 1** | Spotter Round | Fires a non-lethal tagging bullet (30s cooldown). Tagged enemy is revealed on squad minimap for 15s (shared vision). Does not interrupt the target. | 
| **Active 2** | Hold Breath | Activates for 4s: no aim cone drift while ADS (removes passive recoil bloom). Manual trigger, not passive. 45s cooldown. |
| **Signature** | Steel Sight | For 8s, Phaedra's bullets ignore armor (full damage to HP regardless of class). 180s cooldown. Screen effect: silver HUD tint. |
| **Counter** | Close range — Phaedra has no mobility tool and slowest sprint speed (95%). Flashbang disrupts Steel Sight. |
| **Meta role** | Long-range objective denial; boss fights from safe distance; punishes static players. |
| **Solo viability** | High — Phaedra is designed to thrive with patience and positioning, not squad coordination. |

---

### Operator 7 — "GHOST" · Class: Support (Support-B variant)

> *A field medic who believes no teammate should die within reach of her hands. Revision of planned support archetype with revive specialty.*

| Layer | Ability | Detail |
| :---- | :------ | :----- |
| **Passive** | Triage Instinct | Automatically identifies teammates' most critical status effect (bleed, fracture, etc.) when within 5m — overlaid HUD icon. Hands never shake during medical use (no aim penalty while eating/drinking). |
| **Active 1** | Field Medic | Revive speed reduced 8s → 5s. Second revive per session available before 90s cooldown kicks in. (Key differentiator vs all other classes — see [Downstate & Revive](Downstate_Revive.md)) |
| **Active 2** | Med Pack Toss | Throws a medical item from inventory to a teammate (up to 8m range). No animation lock — can throw while crouching. 20s cooldown (per use). |
| **Signature** | Mass Stabilize | 12m radius pulse: all squad members within range immediately have any Bleed status stopped (no healing, just bleed halt). Removes Pain briefly. 150s cooldown. |
| **Counter** | Ghost has lowest offensive capability of any operator. Reliant on squad proximity. Isolation = weakness. Bastion's aggression pushes Ghost out of position. |
| **Meta role** | Keeps squad alive through firefights; enables second-chance play; essential in boss fights. |

---

### Operator 8 — "FUSE" · Class: Specialist (Specialist-B variant)

> *An explosive expert and saboteur. Creates zone denial that forces enemies to move toward danger.*

| Layer | Ability | Detail |
| :---- | :------ | :----- |
| **Passive** | Demolitionist | Explosive radius +15%; Fuse does not receive self-damage from own explosives. Grenade throw range +20%. |
| **Active 1** | Trip Mine | Places a proximity mine on any surface (floor, wall, door frame). Triggers on enemy movement within 1m. Deals 80 damage + Fractures the nearest limb. Max 3 active at once. 30s cooldown per charge. |
| **Active 2** | Breach Charge | Places a charge on a door or wall section. Triggered remotely (no delay). Creates 3×3m breach hole (destroys thin walls only). Extremely loud (audible 60m). 60s cooldown. |
| **Signature** | Minefield | Instantly places 5 Trip Mines in a 6m radius pattern around Fuse's position. Area denial zone lasts 90s or until all mines triggered. 200s cooldown. |
| **Counter** | Slow-walk near mines — Fuse mines are triggered by sprint/walk (not prone). Prone players move safely past mines. Hawk's Motion Sensor detects mine placement direction. |
| **Meta role** | Holds extraction zones, denies corridors, disrupts AI boss positioning. Strong in duo/solo. |

---

### Operator 9 — "IRONCLAD" · Class: Tank (Tank-B variant)

> *A bulldozer of a fighter. Built for punishment and pushing aggressively forward.*

| Layer | Ability | Detail |
| :---- | :------ | :----- |
| **Passive** | Juggernaut | Takes 10% less damage from explosives; breaking doors instantly (no crouch-interact needed). Movement speed penalty from armor is halved. |
| **Active 1** | Suppressive Advance | For 6s: moving forward at sprint speed generates a directional shield (front-arc only, -40% incoming damage from straight ahead). Cannot change direction. 70s cooldown. |
| **Active 2** | Armor Slam | Sprints into a door or light cover piece and destroys it (wood doors, thin barricades), stunning any enemy within 2m for 1.5s. 45s cooldown. |
| **Signature** | Iron Tide | Ironclad and adjacent squadmates within 3m receive a 30s window where HP cannot be reduced below 1 (one-time per signature). After 30s, HP resumes normal damage. 240s cooldown. |
| **Counter** | Flanking — Suppressive Advance only blocks frontal damage. Fuse's Trip Mines trigger during Suppressive Advance sprint. Phaedra's Steel Sight bypasses armor. |
| **Meta role** | Objective pushing, boss fights front-line, extraction zone holding as anchor. |

---

### Operator 10 — "OBSIDIAN" · Class: Scout (Scout-B variant)

> *The ghost of the roster. Stealth, deception, and controlled chaos. No operator should know if Obsidian is in the raid until it's too late.*

| Layer | Ability | Detail |
| :---- | :------ | :----- |
| **Passive** | Ghost Step | Slow-walking produces zero sound (0m audible range vs standard 4m). Moving through foliage and soft surfaces produces no extra noise. |
| **Active 1** | Smoke Grenade | Throws a smoke grenade (8m cloud, 20s duration). Blocks LOS through smoke per [LOS, Fog & Visibility](LOS_Fog_Visibility.md). Shoot-through possible but at −3° aim cone penalty. 35s cooldown. |
| **Active 2** | Decoy Ping | Places a fake player-signature ping on the minimap at a target location (within 15m). Appears as a "player detected" blip on enemies' minimaps for 8s. 50s cooldown. |
| **Signature** | Phase Shift | Becomes fully invisible and silent for 6s. Any attack (shooting, using abilities) breaks cloak immediately. Movement speed is 90% while cloaked. 180s cooldown. Screen effect: shimmer visible at 8m. |
| **Counter** | Emerging from smoke or cloak produces a brief shimmer (visible 8m top-down). Fuse's Trip Mines: Obsidian still triggers them (Phase Shift does not prevent mine trigger). Motion Sensor (Hawk) detects Obsidian through Phase Shift. |
| **Meta role** | Infiltration, quest objective completion, flanking enemies during firefights. Extreme skill ceiling. |
| **Solo viability** | Very High — Obsidian is the premier solo operator; self-sufficient, evasive, never reliant on teammates. |

> **Note on "Obsidian" name:** This is the planned operator whose smoke ability was referenced in `LOS_Fog_Visibility.md`. The smoke reference in that document has been updated to reflect this as a future operator. See the `Gameplay_Review_Checklist.md` consistency fix §3.

---

## Cross-References

- [Core Gameplay Loop](CoreLoop.md) — Operator choice in pre-raid preparation, loadout philosophy.
- [Extraction Mechanics](Extraction_Mechanics.md) — Rules during extract (ability use allowed; healing cancels extract).
- [Medical System](Medical_System.md) — Healing items and triage; heal abilities interact with same body-part and status rules.
- [Gear Mechanics](Gear_Mechanics.md) — Loadout and weight; operators have different rig/weight constraints.
- [Movement & Stamina](Movement_and_Stamina.md) — Speed modifiers, stamina interaction, inertia.
- [Downstate & Revive](Downstate_Revive.md) — Ghost's Field Medic unique revive mechanic.
- [LOS, Fog & Visibility](LOS_Fog_Visibility.md) — Obsidian smoke, Phase Shift shimmer, Hawk detection.
- [Design Pillars](../../ProjectScope/design-pillars-enhanced.md) — Operator Choice (Task-Driven Agency), Operator Mastery (Persistent Progression).
- [MVP Scope](../../ProjectScope/MVP.md) — 3 operators Alpha, 5 Beta, 8+ Launch.


