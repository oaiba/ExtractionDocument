---
title: "Hero Abilities (Operators)"
type: docs
weight: 5
---

### Tổng Quan

Operators are the hero layer of the extraction shooter: each has a **class**, a **passive trait**, one hoặc two **active abilities** (gadgets/skills), và a **signature** (ultimate) ability. Abilities add identity và team composition depth mà không replacing the cốt lõi loop of loadout, loot, và extract. All operators are earnable thông qua progression; no pay-to-win.

**Design pillars:**

* **Gunplay first:** Abilities support và complement gunplay — they never one-shot hoặc replace vũ khí as the primary kill tool.
* **Meaningful cooldowns:** Each ability cách dùng is a deliberate quyết định. Abilities are impactful nhưng not spammable.
* **Full counterplay:** Every ability has a telegraph (audio/visual), a counter, và a weakness. No undodgeable effects.
* **Extraction-aware:** Ability rules change near extraction zones (healing abilities cancel extract timer).
* **Cross-platform parity:** Abilities work identically on PC và mobile; only input method differs.

For high-level operator choice in pre-raid planning, Xem [cốt lõi Gameplay Loop](coreloop/index.html). For scope (Alpha 3 operators, Beta 5), Xem [MVP Scope](https://github.com/oaiba/ExtractionDocument/blob/main/content/ProjectScope/MVP.md). For pillar alignment (Task-Driven Agency, Persistent Progression), Xem [Design Pillars](https://github.com/oaiba/ExtractionDocument/blob/main/content/ProjectScope/design-pillars-enhanced.md).

***

### Class Roster và Base Stats

Each class has inherent stat modifiers that define their role trước any ability hoặc gear is applied.

| Class          | Role                | HP Modifier   | Speed Modifier | Base carry weight bonus | Rig restriction            | Availability |
| -------------- | ------------------- | ------------- | -------------- | ----------------------- | -------------------------- | ------------ |
| **Assault**    | Entry / aggression  | 100% (440 HP) | 100%           | 0 kg                    | Any rig                    | Alpha        |
| **Scout**      | Recon / mobility    | 90% (396 HP)  | 105%           | -2 kg (lighter loadout) | Light hoặc Standard rig only | Alpha        |
| **Support**    | Sustain / utility   | 100% (440 HP) | 95%            | +5 kg (extra carry)     | Any rig                    | Alpha        |
| **Tank**       | Anchor / durability | 115% (506 HP) | 90%            | +3 kg (extra carry)     | Heavy hoặc Armored rig only  | Beta         |
| **Specialist** | Tech / gadget       | 95% (418 HP)  | 100%           | 0 kg                    | Any rig                    | Beta         |

**Alpha** (technical test): Assault, Scout, Support — 3 operators. **Beta** (soft launch): Add Tank, Specialist — total 5 operators. **Launch và beyond:** 8+ operators, 2 per class (Xem [MVP](https://github.com/oaiba/ExtractionDocument/blob/main/content/ProjectScope/MVP.md) tính năng matrix).

***

### Ability Structure

Each operator has three layers of abilities. thông số below are first-pass design values (will be adjusted in balance passes).

#### Layer 1: Passive Trait

* **Always active** — no cooldown, no input required.
* **Small, nhất quán effect** — +5–15% to a single stat, hoặc a conditional trigger (e.g. "on kill").
* **Identity-defining** — tells the người chơi "this is what this operator does differently."
* Does not dominate fights; supports class fantasy và mastery.

#### Layer 2: Active Abilities (1–2 per operator)

* **Activated via ability button** (PC: Q/E hoặc custom bind; Mobile: on-màn hình buttons).
* **Cooldown: 30–90 seconds** depending on impact. Cooldown starts sau effect ends.
* **Resource chi phí (optional):** Some abilities consume a physical item (e.g. drone charges) in addition to cooldown.
* **Telegraphed:** Activation produces a sound cue (audible at 15–20 m) và a visual indicator (smoke trail, device deploy animation 0.5–1.0 s).
* **Interruptible:** Getting hit hoặc stunned trong khi the 0.5–1.0 s cast animation cancels the ability và triggers 50% cooldown.

#### Layer 3: Signature Ability (Ultimate)

* **1 per operator.** Stronger effect, longer cooldown.
* **Cooldown: 120–240 seconds**, hoặc **charge-based** (charge builds via kills +25%, assists +10%, damage dealt +1% per 50 damage, thời gian alive +1% per 30s).
* **Maximum 2 uses per 20-minute raid** at best (ensures rarity và impact).
* **Defines operator identity** — the "hero moment" — nhưng never fight-ending alone.
* **Telegraphed:** Loud audio cue (audible at 25 m), distinct visual effect (glow, aura, particles).

#### Ability Economy: Cooldown Philosophy

| Impact level                         | Cooldown range      | Example                                 |
| ------------------------------------ | ------------------- | --------------------------------------- |
| Low (intel, minor buff)              | 30–45 s             | Spotter pulse, vũ khí swap speed buff   |
| Medium (area denial, heal, blind)    | 45–75 s             | Flashbang, smoke, medkit drop, drone    |
| High (team-wide buff, area lockdown) | 75–90 s             | Fortify zone, team speed boost          |
| Signature (ultimate)                 | 120–240 s hoặc charge | Cloak, overdrive, group heal, area scan |

***

### Full Operator Specifications

#### Assault — "Mamba"

> _"First in, last standing."_

**Identity:** Aggressive entry operator. Rewards kills với tempo advantages. Best khi pushing into contested areas.

| Layer         | Ability         | Effect                                                                                                                                              | Duration                    | Cooldown | Audio tell                       | Visual tell                           |
| ------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------- | -------------------------------- | ------------------------------------- |
| **Passive**   | Adrenaline Rush | On kill: +12% move speed, +8% reload speed for 5 s. Stacks up to 2x.                                                                                | 5 s per stack               | N/A      | Heartbeat SFX (self only)        | Subtle red vignette on Mamba's màn hình |
| **Active 1**  | Flashbang       | Throw flashbang grenade. địch in 5 m radius: blinded 2.5 s, deafened 1.5 s. Allies in radius: minor flash 0.8 s.                                 | Instant (2.5 s effect)      | 60 s     | Pin-pull click + loud detonation | Bright white flash sphere             |
| **Active 2**  | Frag Charge     | Place directional explosive on surface. Detonates on proximity (2 m trigger) hoặc manual trigger. 65 damage in 3 m cone.                              | Until triggered (max 120 s) | 75 s     | Beep khi armed (audible 5 m)    | Small blinking red light              |
| **Signature** | Overdrive       | +20% move speed, +15% rate of fire, -10% recoil for 10 s. Taking lethal damage trong khi Overdrive leaves Mamba at 1 HP instead (once per activation). | 10 s                        | 180 s    | War cry voice line + bass rumble | Red aura glow around nhân vật        |

**LOS/Visibility:** Flashbang — vision denial: blinds địch 2.5 s in 5 m radius (no fog rõ, no shared intel).

**Synergy ghi chú:** Mamba's Flashbang enables aggressive pushes for the entire squad. Overdrive is best used to close distance hoặc win a 1v2. Frag Charge covers flanks hoặc extract zones.

***

#### Scout — "Hawk"

> _"Information is ammunition."_

**Identity:** Intel và stealth operator. Excels at scouting ahead, marking địch, và disengaging. Lower HP và rig restriction incentivize avoidance over direct combat.

| Layer         | Ability       | Effect                                                                                                                                                            | Duration                      | Cooldown                                  | Audio tell                                    | Visual tell                |
| ------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ----------------------------------------- | --------------------------------------------- | -------------------------- |
| **Passive**   | Light Step    | -20% footstep audible range. Crouch-walk is near-silent (audible at 1 m instead of 2–4 m).                                                                        | Always on                     | N/A                                       | None (that's the point)                       | None                       |
| **Active 1**  | Spotter Drone | Deploy a hovering drone. Marks địch within 25 m radius for 8 s (hiển thị rõ to squad on HUD as red pings). Drone has 30 HP, can be shot down.                      | 8 s scan, then self-destructs | 75 s                                      | Buzzing motor sound (audible 20 m)            | Small drone hiển thị rõ in air |
| **Active 2**  | Motion Sensor | Place a ground sensor. Pings địch moving within 10 m radius (not crouching/prone địch). Lasts 90 s hoặc until destroyed (15 HP). Max 2 placed.                | 90 s                          | 45 s                                      | Soft click on deploy                          | Tiny device; hard to spot  |
| **Signature** | Ghost Cloak   | Become semi-invisible for 6 s. 70% transparency (shimmer hiển thị rõ within 8 m). Firing, using items, hoặc taking damage cancels cloak. Move speed +10% while cloaked. | 6 s                           | 210 s (hoặc charge: 80% from assists/scans) | Electrical crackle on activate (audible 15 m) | Shimmer/distortion effect  |

**Synergy ghi chú:** Hawk's intel feeds the entire squad's quyết định-making. Spotter Drone trước pushing a room eliminates blind spots. Ghost Cloak enables flanking hoặc emergency extraction escape.

**LOS/Visibility:** Spotter Drone — vision proxy 25 m (drone LOS); clears fog for squad; marks shared to squad. Motion Sensor — intel only (no LOS); pings moving địch in 10 m; shared to squad; does not rõ fog (ping only). Ghost Cloak — self-concealment; reduces visibility to địch (shimmer within 8 m); not a vision proxy for squad.

**Counterplay:** Shoot the drone (30 HP). Crouch/prone to avoid Motion Sensor. Watch for cloak shimmer within 8 m.

***

#### Support — "Cross"

> _"Nobody dies on my watch."_

**Identity:** Sustain và economy operator. Provides healing, extra carry capacity, và team utility. Slower speed nhưng compensated by team giá trị.

| Layer         | Ability        | Effect                                                                                                                                                            | Duration                      | Cooldown                                      | Audio tell                   | Visual tell                            |
| ------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | --------------------------------------------- | ---------------------------- | -------------------------------------- |
| **Passive**   | Pack Mule      | +5 kg carry weight threshold per tier. +1 rig hotkey slot (nếu rig supports it). Can search containers 15% faster.                                                 | Always on                     | N/A                                           | None                         | Slightly larger backpack visual        |
| **Active 1**  | Medkit Drop    | Drop a deployable medkit on the ground. Heals 1 người chơi for 80 HP over 5 s (must interact to cách dùng). Does not repair destroyed limbs — cách dùng surgery kit for that.     | available for 30 s sau drop | 60 s                                          | Pouch-open sound on drop     | Green medkit on ground với cross icon |
| **Active 2**  | Stim Shot      | Inject self hoặc adjacent ally. Removes pain effects, restores 15 Arm Stamina, reduces recoil -10% for 20 s. Does not restore HP.                                   | 20 s buff                     | 45 s                                          | Injection hiss               | Brief green flash on target            |
| **Signature** | Field Hospital | tạo a 4 m radius healing zone for 12 s. All allies in zone: +8 HP/s, pain suppressed, slow limb repair (+5 HP/s to damaged limbs). Zone is hiển thị rõ to địch. | 12 s                          | 240 s (hoặc charge: assists, heals, thời gian alive) | Generator hum (audible 20 m) | Green circular zone on ground          |

**Synergy ghi chú:** Cross sustains prolonged fights. Field Hospital near a defensive position lets the squad hold ground. Medkit Drop lets allies heal independently while Cross continues fighting.

**Counterplay:** Field Hospital zone is hiển thị rõ và audible — throw grenades hoặc push while địch are stationary healing. Stim Shot does not restore HP.

**LOS/Visibility:** Field Hospital — zone is hiển thị rõ to all (địch LOS not blocked); does not reveal hoặc block vision.

**Extraction interaction:** Medkit Drop và Field Hospital both count as _healing actions_ — **using them cancels extraction timer** nếu the user is in an extract zone. Cross must stop healing to extract.

***

#### Tank — "Bastion" (Beta)

> _"Hold this ground."_

**Identity:** Area denial và anchor operator. High HP, heavy giáp affinity, nhưng slowest speed. Excels at holding choke points và protecting extracting teammates.

| Layer         | Ability          | Effect                                                                                                                                           | Duration             | Cooldown | Audio tell                                  | Visual tell                                   |
| ------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- | -------- | ------------------------------------------- | --------------------------------------------- |
| **Passive**   | Hardened         | +15% giáp durability (giáp degrades 15% slower). Blunt damage from blocked rounds reduced by 30%.                                              | Always on            | N/A      | None                                        | Reinforced giáp visual (extra plate hiển thị rõ) |
| **Active 1**  | Deployable Cover | Place a waist-high ballistic shield on the ground. 300 HP, blocks bullets from one direction. Lasts 60 s hoặc until destroyed. Max 1 active.       | 60 s                 | 75 s     | Heavy metal clank on deploy (audible 15 m)  | hiển thị rõ metal barricade                       |
| **Active 2**  | Concussion Blast | Short-range (4 m cone) shockwave. địch hit: stagger 1.5 s, -30% move speed for 3 s, vũ khí sway +200% for 2 s. Costs 20 Arm Stamina.          | Instant (3 s effect) | 60 s     | Loud thump (audible 20 m)                   | hiển thị rõ shockwave ripple                      |
| **Signature** | Goliath Protocol | For 15 s: -50% incoming damage, cannot sprint (locked to walk speed), +30% accuracy (reduced sway). Allies within 5 m gain -20% incoming damage. | 15 s                 | 240 s    | Metallic activation sequence (audible 25 m) | Orange glow + energy shield visual            |

**Synergy ghi chú:** Bastion anchors a position while allies loot hoặc extract. Deployable Cover tạo instant defensive positions. Goliath Protocol trong khi extraction timer makes the squad much harder to kill.

**LOS/Visibility:** Deployable Cover — one-direction LOS blocker; blocks vision (và shots) from one side; does not reveal.

**Counterplay:** Deployable Cover only blocks one direction — flank it. Goliath Protocol locks Bastion to walk speed — disengage và reposition. Concussion Blast is short-range — maintain distance.

***

#### Specialist — "Glitch" (Beta)

> _"Knowledge is the vũ khí."_

**Identity:** Tech và disruption operator. Hacks, jams, và manipulates the battlefield. Versatile utility that scales với game knowledge và map awareness.

| Layer         | Ability          | Effect                                                                                                                                                                                                                                        | Duration               | Cooldown                                    | Audio tell                      | Visual tell                          |
| ------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------------------------------------- | ------------------------------- | ------------------------------------ |
| **Passive**   | Tech Savvy       | Interact với electronic devices 25% faster (doors, terminals, quest objectives). Can see trap devices (Motion Sensors, mines) within 8 m thông qua walls (UI highlight).                                                                       | Always on              | N/A                                         | None                            | Highlighted traps show thông qua walls |
| **Active 1**  | EMP Drone        | Launch a small drone that detonates at target location. 6 m radius EMP: disables địch gadgets (drones, sensors, turrets) for 15 s, disrupts địch HUD for 3 s (no compass, no stamina bar, no weight indicator). Drone has 20 HP mid-flight. | Instant (15 s disable) | 75 s                                        | Drone flight buzz + EMP crackle | Blue electric burst                  |
| **Active 2**  | Signal Jammer    | Place a device that prevents địch within 12 m radius from using active abilities for 10 s. Does not affect passives. Jammer has 25 HP và can be destroyed. Max 1 active.                                                                  | 10 s                   | 90 s                                        | Electronic whine (audible 10 m) | Small device với blue glow          |
| **Signature** | Tactical Overlay | For 10 s: reveal all địch within 40 m on the minimap for the entire squad. địch are shown as real-thời gian pings (update every 0.5 s). Does not reveal thông qua walls — shows last-known position nếu địch enters cover.                     | 10 s                   | 210 s (hoặc charge: assists, gadget destroys) | Radar ping sound (audible 20 m) | Blue scan wave emanates from Glitch  |

**Synergy ghi chú:** Glitch counters other operators' gadgets và provides decisive intel for squad pushes. EMP Drone trước a push disables Hawk's drones và Bastion's cover (electronics only — physical cover unaffected). Tactical Overlay enables coordinated squad assaults.

**LOS/Visibility:** Tech Savvy — see traps (Motion Sensors, mines) within 8 m thông qua walls (UI highlight); no địch reveal. Tactical Overlay — vision proxy 40 m; minimap reveal; last-known khi địch in cover; shared to squad.

**Counterplay:** EMP Drone is fragile (20 HP) — shoot it mid-flight. Signal Jammer is destroyable và audible. Tactical Overlay only reveals for 10 s và requires Glitch to be alive — kill Glitch to end the effect early.

***

### Ability Interaction Rules

#### trong khi Normal Raid

| Rule             | chi tiết                                                                                                                                                     |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Passive          | Always active. Unaffected by stuns, EMP, hoặc death (deactivates on death obviously).                                                                        |
| Active abilities | Usable khi off cooldown. 0.5–1.0 s cast animation — interruptible by damage/stun (50% cooldown refund).                                                   |
| Signature        | Usable khi charged hoặc off cooldown. 1.0 s activation animation — interruptible (75% cooldown/charge refund).                                              |
| Ability noise    | All active/signature abilities produce audio cues. Range varies per ability (see specs above).                                                             |
| Ability stacking | Same ability from two operators of the same class does NOT stack (prevents double-Mamba Overdrive). Different abilities from different operators DO stack. |
| Down trạng thái       | Downed người chơi cannot cách dùng abilities. Passive deactivates in down trạng thái.                                                                                    |

#### trong khi Extraction

Per [Extraction cơ chế](extraction_mechanics/index.html):

| Ability type                                                                      | Usable trong khi extract? | Cancels extract timer?    |
| --------------------------------------------------------------------------------- | ---------------------- | ------------------------- |
| Passive                                                                           | Yes (always on)        | No                        |
| Offensive active (Flashbang, Frag Charge, Concussion Blast, EMP Drone)            | Yes                    | No                        |
| Intel active (Spotter Drone, Motion Sensor, Signal Jammer, Tactical Overlay)      | Yes                    | No                        |
| **Healing active** (Medkit Drop, Stim Shot, Field Hospital)                       | Yes, nhưng...            | **Yes — cancels extract** |
| Signature (offensive: Overdrive, Ghost Cloak, Goliath Protocol, Tactical Overlay) | Yes                    | No                        |
| **Signature (healing: Field Hospital)**                                           | Yes, nhưng...            | **Yes — cancels extract** |

**Design rationale:** The extraction timer is a high-stakes moment. Offensive và utility abilities tạo exciting defense scenarios. Healing abilities cancel extract to force the choice: heal và reset timer, hoặc extract wounded. This prevents the "heal tank" exploit of endlessly healing trong khi extraction.

#### Interaction với Medical hệ thống

Operator healing abilities interact với the [Medical hệ thống](medical_system/index.html):

| Interaction                       | Rule                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Medkit Drop vs Surgery Kit        | Medkit Drop restores HP nhưng does NOT repair destroyed limbs. Surgery Kit (inventory item) is still required. |
| Field Hospital vs Destroyed Limbs | Field Hospital repairs damaged limbs (+5 HP/s) nhưng does NOT restore from 0 HP (destroyed).                   |
| Stim Shot vs Pain                 | Stim Shot suppresses pain (like painkillers) for 20 s nhưng does not heal.                                     |
| Ability healing vs Toxicity       | Ability heals contribute to toxicity accumulation the same as medical items (prevent healing spam).          |

#### Interaction với Gear Weight

Per [Gear cơ chế](gear_mechanics/index.html), some operators have gear constraints:

| Operator                             | Gear constraint                                                                                  | Reason                                                                    |
| ------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| Scout (Hawk)                         | Light hoặc Standard rig only (max 9 slots). Cannot equip Heavy rig hoặc Armored rig.                 | Maintains scout mobility identity; prevents scout from also being a tank. |
| Tank (Bastion)                       | Heavy hoặc Armored rig only (12 slots). Cannot equip Light rig. Must bring Class 3+ giáp.         | Enforces tank fantasy; prevents tank from being a fast flanker.           |
| Support (Cross)                      | +5 kg carry weight per tier (via Pack Mule passive). Starts at higher effective weight capacity. | Supports "team mule" và "loot carrier" roles.                            |
| Assault (Mamba), Specialist (Glitch) | No restrictions.                                                                                 | Flexibility as generalist / tech roles.                                   |

#### Interaction với LOS/Visibility

Per [LOS, Fog of War & Visibility](los_fog_visibility/index.html), abilities that reveal hoặc block vision integrate với the shared team vision hệ thống. Summary:

| Operator         | Ability          | LOS/Visibility role | Range/Radius | Fog clearing?   | shared to squad?       | Counterplay                        |
| ---------------- | ---------------- | ------------------- | ------------ | --------------- | ---------------------- | ---------------------------------- |
| Hawk             | Spotter Drone    | Vision proxy        | 25 m         | Yes (drone LOS) | Yes                    | Shoot drone (30 HP)                |
| Hawk             | Motion Sensor    | Intel               | 10 m         | No (ping only)  | Yes                    | Crouch/prone; destroy (15 HP)      |
| Hawk             | Ghost Cloak      | Self-conceal        | 8 m shimmer  | No              | No                     | Shimmer hiển thị rõ 8 m; damage breaks |
| Glitch           | Tech Savvy       | Exception (traps)   | 8 m          | No              | No (self)              | N/A                                |
| Glitch           | Tactical Overlay | Vision proxy        | 40 m         | Yes             | Yes                    | Kill Glitch; hard cover            |
| Obsidian (Recon) | Smoke            | Blocker             | 8 m radius   | No              | N/A                    | Avoid smoke; Thermal Block         |
| Mamba            | Flashbang        | Vision denial       | 5 m          | No              | No                     | Look away; cover                   |
| Bastion          | Deployable Cover | LOS blocker         | Directional  | No              | N/A                    | Flank; destroy (300 HP)            |
| Cross            | Field Hospital   | Zone hiển thị rõ        | 4 m zone     | No              | N/A (địch see zone) | N/A                                |

Passives such as **Light Step** (Hawk) và **Tech Savvy** (Glitch) affect visibility indirectly (reduced sound detection; see traps thông qua walls) nhưng do not tạo vision proxies for the squad. All intel và vision from the abilities above is merged into the squad's shared visibility trạng thái (minimap fog, HUD marks). Counterplay preserves fair visibility per design pillars.

***

### Squad Composition và Synergy

#### Recommended Compositions (3-người chơi squads)

| Composition        | Operators                    | Playstyle                          | Strengths                     | Weakness                                |
| ------------------ | ---------------------------- | ---------------------------------- | ----------------------------- | --------------------------------------- |
| **Balanced**       | Assault + Scout + Support    | Push, intel, sustain               | Covers all roles; nhất quán  | No exceptional strength                 |
| **Aggro Rush**     | Assault + Assault + Scout    | Fast push, double flash + intel    | High kill potential           | Low sustain; one bad fight = squad wipe |
| **Goliath**        | Tank + Support + Specialist  | Hold position, deny area, heal     | Near-impenetrable defense     | Slow rotation; vulnerable to flanks     |
| **Intel Dominant** | Scout + Specialist + Assault | Map control, information advantage | Always know where địch are | Less direct firepower và healing       |
| **Economy**        | Support + Scout + any        | High extract rate, carry more loot | Max loot extraction           | Weaker in direct PvP                    |

#### Operator Synergy matrix

|             | Mamba | Hawk                                  | Cross                     | Bastion                      | Glitch                       |
| ----------- | ----- | ------------------------------------- | ------------------------- | ---------------------------- | ---------------------------- |
| **Mamba**   | —     |  (flash + push on scanned địch) |  (heals sau aggro)    |  (breach while tank holds) |  (EMP then push)          |
| **Hawk**    |    | —                                     |  (intel for safe heals) |  (scout for anchor)        |  (double intel dominance) |
| **Cross**   |     |                                     | —                         |  (heal the tank)          |  (general utility)         |
| **Bastion** |     |                                     |                        | —                            |  (cover + jammer)          |
| **Glitch**  |    |                                    |                         |                            | —                            |

 = Low synergy |  = Moderate synergy |  = High synergy

***

### Balance Framework

#### Ability Damage Budget

Abilities are never the primary damage source. The damage budget constrains ability damage relative to vũ khí:

| Damage source          | Damage per second (rough target) | % of total kill contribution |
| ---------------------- | -------------------------------- | ---------------------------- |
| primary vũ khí         | 150–400 DPS (depending on tier)  | 70–85%                       |
| Grenades (inventory)   | 80–120 per grenade               | 5–15%                        |
| **Operator abilities** | **0–65 per activation**          | **5–15%**                    |
| Environmental / fall   | Variable                         | <5%                          |

#### Counterplay matrix

Every ability has at least one hard counter và one soft counter:

| Ability                    | Hard counter                                                | Soft counter                                                      |
| -------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------- |
| Flashbang (Mamba)          | Look away (reduces effect 70%)                              | Pre-positioned cover                                              |
| Frag Charge (Mamba)        | Glitch's Tech Savvy reveals it; shoot it (15 HP)            | Slow-walk to avoid proximity trigger                              |
| Spotter Drone (Hawk)       | Shoot it down (30 HP); EMP Drone destroys it                | Stay behind cover (drone marks LOS only)                          |
| Motion Sensor (Hawk)       | Crouch/prone avoids detection; Glitch sees it thông qua walls | Destroy it (15 HP)                                                |
| Ghost Cloak (Hawk)         | AoE damage reveals; shimmer hiển thị rõ at 8 m                  | Audio cue on activation; predict movement                         |
| Medkit Drop (Cross)        | Push while địch is healing (animation lock)                | Deny area where medkit dropped                                    |
| Field Hospital (Cross)     | Grenade into the zone; push stationary targets              | Disengage và wait out 12 s                                       |
| Deployable Cover (Bastion) | Flank around it; grenades over it                           | EMP disables? No — physical object; must destroy (300 HP)         |
| Concussion Blast (Bastion) | Stay beyond 4 m range                                       | Pre-aim trước entering range                                     |
| Goliath Protocol (Bastion) | Disengage — he can't chase (walk speed only)                | Focus fire allies instead                                         |
| EMP Drone (Glitch)         | Shoot it mid-flight (20 HP)                                 | Spread out to limit AoE                                           |
| Signal Jammer (Glitch)     | Destroy it (25 HP); push outside 12 m                       | Wait out 10 s duration                                            |
| Tactical Overlay (Glitch)  | Kill Glitch to end effect                                   | cách dùng hard cover to break LOS (shows last-known, not thông qua walls) |

***

### Progression: Operator Mastery

#### XP và Leveling

| Property                 | giá trị                                                                                                                                                     |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Max level per operator   | 50                                                                                                                                                        |
| XP sources               | Kills (+100), assists (+50), damage dealt (+1 per 10 dmg), survival thời gian (+2/min), extraction bonus (+150), quest completion while playing operator (+75) |
| XP curve                 | Linear 1–20 (1,000 XP/level), scaling 21–50 (2,000 + 200 × (level − 20) XP/level)                                                                         |
| Estimated thời gian to Lvl 50 | \~120–150 raids (60–75 hours)                                                                                                                             |

#### Mastery Rewards

| Level | Reward type                                               | Example                                   |
| ----- | --------------------------------------------------------- | ----------------------------------------- |
| 5     | Operator skin (uncommon)                                  | Alternate color sơ đồ                    |
| 10    | Passive bonus +1%                                         | Mamba: +1% sprint speed on kill           |
| 15    | Voice line pack                                           | Unique callouts                           |
| 20    | Passive bonus +2% (cumulative)                            | Hawk: +2% reduced footstep range          |
| 25    | Operator skin (rare)                                      | Tactical variant                          |
| 30    | Passive bonus +3% (cumulative)                            | Cross: +3% heal speed                     |
| 35    | Signature vũ khí skin                                     | Unique camo for operator's "canon" vũ khí |
| 40    | Passive bonus +4% (cumulative)                            | Bastion: +4% giáp durability             |
| 45    | Operator title + badge                                    | Displayed on squad loadout màn hình         |
| 50    | Passive bonus +5% (cumulative) + Mastery skin (legendary) | Final bonus; gold/prestige skin           |

**Cap:** +5% passive bonus at Lvl 50. This is small enough that a Lvl 1 người chơi với good aim beats a Lvl 50 người chơi với bad positioning.

**No vertical power beyond passive bonus:** No new abilities, no ability upgrades, no stat increases beyond the +5% passive. All mastery rewards past the passive bonus are cosmetic.

#### Operator Unlock Progression

| Operator              | Unlock method                         | Approximate thời gian                   |
| --------------------- | ------------------------------------- | ---------------------------------- |
| Assault (Mamba)       | Free — starting operator              | Immediate                          |
| Scout (Hawk)          | Free — starting operator              | Immediate                          |
| Support (Cross)       | Free — starting operator              | Immediate                          |
| Tank (Bastion)        | Account level 10 hoặc 50,000 currency   | \~15–20 hours played               |
| Specialist (Glitch)   | Account level 15 hoặc 75,000 currency   | \~25–30 hours played               |
| Future operators (8+) | Account level yêu cầu hoặc currency | Varies; never real-money exclusive |

***

### Cross-Platform Ability Balance

#### Mobile vs PC Considerations

| Aspect                                  | PC (mouse + keyboard)        | Mobile (touch)                                                           | Parity solution                                                                                |
| --------------------------------------- | ---------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| Ability activation                      | Dedicated keybinds (Q, E, Z) | On-màn hình buttons (thumb accessible)                                     | Same cooldowns, same cast times; mobile buttons positioned for ergonomic access                |
| Aiming abilities (Flashbang, EMP Drone) | Precise mouse throw          | Aim-assist for thrown abilities (soft lock to nearest địch at 30% pull) | Mobile gets aim assist on ability targeting; PC does not                                       |
| Drone control (Spotter Drone)           | Mouse cursor to position     | Auto-deploy at crosshair location                                        | Both: drone deploys at center-of-màn hình aim point; no manual drone flying                      |
| Signature timing                        | Quick reflexive activation   | Potential misclick risk                                                  | Signature requires confirm tap (double-tap on mobile, single press on PC) to prevent accidents |
| Counterplay (shooting drone)            | Easy với mouse aim          | Harder on mobile                                                         | Drone HP slightly higher on mobile lobbies? **No — maintain parity. Mobile người chơi learn.**    |

***

### Anti-Abuse Rules

| Rule                                                            | chi tiết                                                                                          | Reason                                    |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------- |
| Ability cooldown starts sau effect ends                       | Prevents pre-casting next ability trong khi hiện tại one                                            | Anti-spam                                 |
| Same-class ability stacking blocked                             | Two Vipers in a squad: only one Flashbang at a thời gian (second enters cooldown nếu first is active) | Prevents degenerate double-flash          |
| Healing trong khi extraction cancels timer                         | Field Hospital và Medkit Drop reset the 15–30 s extract timer                                  | Prevents infinite heal-tanking at extract |
| Signature charge does not carry between raids                   | Charge resets to 0 at raid start; must build in-raid                                            | Prevents pre-charged ultimate farming     |
| Abilities disabled in safe zones (Safe House, vendors)          | No ability cách dùng outside raids                                                                    | Prevents griefing / exploit in menus      |
| Ability damage does not contribute to insurance fraud detection | Intentional self-damage với abilities is flagged                                               | Anti-exploit                              |

***

### Reference: Competitor Ability Structures

| Game                  | Ability layers                                  | Cooldown range                         | ghi chú for our design                           |
| --------------------- | ----------------------------------------------- | -------------------------------------- | ---------------------------------------------- |
| Delta Force: Hawk Ops | Trait (passive) + Tactical (active) + 2 Gadgets | 15–45 s (shorter; more action-focused) | We cách dùng longer cooldowns for extraction tension |
| ARC Raiders           | No fixed classes; loadout-based roles + gadgets | Gadget charges (limited per raid)      | We combine class identity với cooldown model  |
| Shatterline           | Passive + Active + Perks                        | 20–60 s                                | Similar structure; we add signature layer      |
| Overwatch 2           | Passive + 2 Abilities + Ultimate (charge-based) | 5–15 s abilities, 60–120 s ult         | Too fast for extraction; we 3–5x cooldowns     |
| Deadlock              | 4 active abilities, scaling với items          | 8–35 s base, reduced by items          | MOBA hybrid; we keep it simpler (3 layers)     |

**Our positioning:** Longer cooldowns than hero shooters, shorter than pure mil-sim. Each ability cách dùng is a "moment" — not constant spam, not once-per-match.

***

### Operators 6–10 — Pipeline (Launch và Beyond)

> **Status:** Concept-level. thông số TBD in full design pass. These operators được thiết kế để expand the meta-game by countering patterns established by the Alpha/Beta roster và serving underrepresented playstyles.

#### Design Goals for Operators 6–10

| mục tiêu                                         | chi tiết                                                                                                     |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Expand class depth                           | Add a second Assault, second Scout, và a solo-viable class                                                |
| Counter existing meta                        | Each new operator should have at least one ability that naturally counters an existing operator's strength |
| No class duplication mà không differentiation | Two Assault-class operators must feel distinct — different fantasy, different counterplay                  |
| Solo-viability design                        | One operator specifically designed to feel strong in solo queue (reduced squad dependency)                 |
| Diversity in fantasy                         | Different visual/nhân vật fantasy from existing 5                                                         |

***

#### Operator 6 — "PHAEDRA" · Class: Sniper (NEW CLASS)

> _A precision contractor who turns information into lethal advantage. Patient. Methodical. Devastating at range._

| Layer              | Ability                                                                                                    | chi tiết                                                                                                                                              |
| ------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Passive**        | Eagle Eye                                                                                                  | Aims slow walk has no aim cone penalty (other operators have slight penalty at slow walk). Headshot kills grant +20% stamina recovery instantly.    |
| **Active 1**       | Spotter Round                                                                                              | Fires a non-lethal tagging bullet (30s cooldown). Tagged địch is revealed on squad minimap for 15s (shared vision). Does not interrupt the target. |
| **Active 2**       | Hold Breath                                                                                                | Activates for 4s: no aim cone drift while ADS (removes passive recoil bloom). Manual trigger, not passive. 45s cooldown.                            |
| **Signature**      | Steel Sight                                                                                                | For 8s, Phaedra's bullets ignore giáp (full damage to HP regardless of class). 180s cooldown. màn hình effect: silver HUD tint.                      |
| **Counter**        | Close range — Phaedra has no mobility tool và slowest sprint speed (95%). Flashbang disrupts Steel Sight. |                                                                                                                                                     |
| **Meta role**      | Long-range objective denial; boss fights from safe distance; punishes static người chơi.                      |                                                                                                                                                     |
| **Solo viability** | High — Phaedra được thiết kế để thrive với patience và positioning, not squad coordination.                |                                                                                                                                                     |

***

#### Operator 7 — "GHOST" · Class: Support (Support-B variant)

> _A field medic who believes no teammate should die within reach of her hands. Revision of planned support archetype với revive specialty._

| Layer         | Ability                                                                                                                                                     | chi tiết                                                                                                                                                                                                   |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Passive**   | Triage Instinct                                                                                                                                             | Automatically identifies teammates' most critical status effect (bleed, fracture, etc.) khi within 5m — overlaid HUD icon. Hands never shake trong khi medical cách dùng (no aim penalty while eating/drinking). |
| **Active 1**  | Field Medic                                                                                                                                                 | Revive speed reduced 8s → 5s. Second revive per session available trước 90s cooldown kicks in. (chính differentiator vs all other classes — Xem [Downstate & Revive](downstate_revive/index.html))                |
| **Active 2**  | Med Pack Toss                                                                                                                                               | Throws a medical item from inventory to a teammate (up to 8m range). No animation lock — can throw while crouching. 20s cooldown (per cách dùng).                                                              |
| **Signature** | Mass Stabilize                                                                                                                                              | 12m radius pulse: all squad members within range immediately have any Bleed status stopped (no healing, just bleed halt). Removes Pain briefly. 150s cooldown.                                           |
| **Counter**   | Ghost has lowest offensive capability of any operator. Reliant on squad proximity. Isolation = weakness. Bastion's aggression pushes Ghost out of position. |                                                                                                                                                                                                          |
| **Meta role** | Keeps squad alive thông qua firefights; enables second-chance play; essential in boss fights.                                                                 |                                                                                                                                                                                                          |

***

#### Operator 8 — "FUSE" · Class: Specialist (Specialist-B variant)

> _An explosive expert và saboteur. tạo zone denial that forces địch to move toward danger._

| Layer         | Ability                                                                                                                                                                  | chi tiết                                                                                                                                                                                               |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Passive**   | Demolitionist                                                                                                                                                            | Explosive radius +15%; Fuse does not receive self-damage from own explosives. Grenade throw range +20%.                                                                                              |
| **Active 1**  | Trip Mine                                                                                                                                                                | Places a proximity mine on any surface (floor, wall, door frame). Triggers on địch movement within 1m. Deals 80 damage + Fractures the nearest limb. Max 3 active at once. 30s cooldown per charge. |
| **Active 2**  | Breach Charge                                                                                                                                                            | Places a charge on a door hoặc wall section. Triggered remotely (no delay). tạo 3×3m breach hole (destroys thin walls only). Extremely loud (audible 60m). 60s cooldown.                           |
| **Signature** | Minefield                                                                                                                                                                | Instantly places 5 Trip Mines in a 6m radius pattern around Fuse's position. Area denial zone lasts 90s hoặc until all mines triggered. 200s cooldown.                                                 |
| **Counter**   | Slow-walk near mines — Fuse mines are triggered by sprint/walk (not prone). Prone người chơi move safely past mines. Hawk's Motion Sensor detects mine placement direction. |                                                                                                                                                                                                      |
| **Meta role** | Holds extraction zones, denies corridors, disrupts AI boss positioning. Strong in duo/solo.                                                                              |                                                                                                                                                                                                      |

***

#### Operator 9 — "IRONCLAD" · Class: Tank (Tank-B variant)

> _A bulldozer of a fighter. Built for punishment và pushing aggressively forward._

| Layer         | Ability                                                                                                                                                       | chi tiết                                                                                                                                                                           |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Passive**   | Juggernaut                                                                                                                                                    | Takes 10% less damage from explosives; breaking doors instantly (no crouch-interact needed). Movement speed penalty from giáp is halved.                                        |
| **Active 1**  | Suppressive Advance                                                                                                                                           | For 6s: moving forward at sprint speed generates a directional shield (front-arc only, -40% incoming damage from straight ahead). Cannot change direction. 70s cooldown.         |
| **Active 2**  | giáp Slam                                                                                                                                                    | Sprints into a door hoặc light cover piece và destroys it (wood doors, thin barricades), stunning any địch within 2m for 1.5s. 45s cooldown.                                     |
| **Signature** | Iron Tide                                                                                                                                                     | Ironclad và adjacent squadmates within 3m receive a 30s window where HP cannot be reduced below 1 (one-thời gian per signature). sau 30s, HP resumes normal damage. 240s cooldown. |
| **Counter**   | Flanking — Suppressive Advance only blocks frontal damage. Fuse's Trip Mines trigger trong khi Suppressive Advance sprint. Phaedra's Steel Sight bypasses giáp. |                                                                                                                                                                                  |
| **Meta role** | Objective pushing, boss fights front-line, extraction zone holding as anchor.                                                                                 |                                                                                                                                                                                  |

***

#### Operator 10 — "OBSIDIAN" · Class: Scout (Scout-B variant)

> _The ghost of the roster. Stealth, deception, và controlled chaos. No operator should know nếu Obsidian is in the raid until it's too late._

| Layer              | Ability                                                                                                                                                                                                                              | chi tiết                                                                                                                                                                                                |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Passive**        | Ghost Step                                                                                                                                                                                                                           | Slow-walking produces zero sound (0m audible range vs standard 4m). Moving thông qua foliage và soft surfaces produces no extra noise.                                                                 |
| **Active 1**       | Smoke Grenade                                                                                                                                                                                                                        | Throws a smoke grenade (8m cloud, 20s duration). Blocks LOS thông qua smoke per [LOS, Fog & Visibility](los_fog_visibility/index.html). Shoot-thông qua possible nhưng at −3° aim cone penalty. 35s cooldown.       |
| **Active 2**       | Decoy Ping                                                                                                                                                                                                                           | Places a fake người chơi-signature ping on the minimap at a target location (within 15m). Appears as a "người chơi detected" blip on địch' minimaps for 8s. 50s cooldown.                                  |
| **Signature**      | Phase Shift                                                                                                                                                                                                                          | Becomes fully invisible và silent for 6s. Any attack (shooting, using abilities) breaks cloak immediately. Movement speed is 90% while cloaked. 180s cooldown. màn hình effect: shimmer hiển thị rõ at 8m. |
| **Counter**        | Emerging from smoke hoặc cloak produces a brief shimmer (hiển thị rõ 8m top-down). Fuse's Trip Mines: Obsidian still triggers them (Phase Shift does not prevent mine trigger). Motion Sensor (Hawk) detects Obsidian thông qua Phase Shift. |                                                                                                                                                                                                       |
| **Meta role**      | Infiltration, quest objective completion, flanking địch trong khi firefights. Extreme skill ceiling.                                                                                                                                 |                                                                                                                                                                                                       |
| **Solo viability** | Very High — Obsidian is the premier solo operator; self-sufficient, evasive, never reliant on teammates.                                                                                                                             |                                                                                                                                                                                                       |

> **Note on "Obsidian" name:** This is the planned operator whose smoke ability was referenced in `LOS_Fog_Visibility.md`. The smoke reference in that tài liệu has been updated to reflect this as a future operator. See the `Gameplay_Review_Checklist.md` consistency fix §3.

***

### Tham Chiếu Chéo

* [cốt lõi Gameplay Loop](coreloop/index.html) — Operator choice in pre-raid preparation, loadout philosophy.
* [Extraction cơ chế](extraction_mechanics/index.html) — Rules trong khi extract (ability cách dùng allowed; healing cancels extract).
* [Medical hệ thống](medical_system/index.html) — Healing items và triage; heal abilities interact với same body-part và status rules.
* [Gear cơ chế](gear_mechanics/index.html) — Loadout và weight; operators have different rig/weight constraints.
* [Movement & Stamina](movement_and_stamina/index.html) — Speed modifiers, stamina interaction, inertia.
* [Downstate & Revive](downstate_revive/index.html) — Ghost's Field Medic unique revive cơ chế.
* [LOS, Fog & Visibility](los_fog_visibility/index.html) — Obsidian smoke, Phase Shift shimmer, Hawk detection.
* [Design Pillars](https://github.com/oaiba/ExtractionDocument/blob/main/content/ProjectScope/design-pillars-enhanced.md) — Operator Choice (Task-Driven Agency), Operator Mastery (Persistent Progression).
* [MVP Scope](https://github.com/oaiba/ExtractionDocument/blob/main/content/ProjectScope/MVP.md) — 3 operators Alpha, 5 Beta, 8+ Launch.
