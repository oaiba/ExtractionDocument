---
title: "Design Pillars & Core Philosophy - Enhanced Edition"
linkTitle: Design Pillars
type: docs
weight: 7
version: 2
last_updated: 2026-02-11T00:00:00.000Z
---

> **Living tài liệu Status**: This tài liệu evolves với the game. All tính năng must align với these pillars.\
> **Authority Level**: Ultimate - These pillars override all other design quyết định.\
> **Review Cadence**: Monthly validation, quarterly deep review

***

### tài liệu Structure

```
1. Genre Foundation (What defines extraction shooters)
2. Our Five Core Pillars (How we differentiate)
3. Player Experience Goals (What players should feel)
4. Core Gameplay Loops (Macro & Micro)
5. Pillar Conflict Resolution (Decision framework)
6. Quality Checklist (Gate for all features)
```

***

### Genre Pillars (Extraction Shooter DNA)

These six foundational pillars define the extraction shooter genre based on industry analysis of Tarkov, Hunt: Showdown, Arena Breakout, ARC Raiders, và Dark và Darker. **Every extraction shooter must have these** - they are non-negotiable genre yêu cầu.

| Pillar                | Genre định nghĩa                                                            | Our Implementation                                                                              | Innovation Point                                                                          |
| --------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Risk of Loss**      | Constant awareness that progress can be lost. Dying = losing equipped gear. | **Full Loot Drop:** Everything equipped is at risk. tạo cảm xúc investment in each raid.  | **Insurance hệ thống:** 70% return rate for unlooted gear sau 24h (anti-frustration)      |
| **Survival Priority** | Survival prioritized over unnecessary combat. Avoiding fights is valid.     | **máu Scarcity:** Meds are expensive. Every engagement drains resources. Stealth is viable.  | **Sound-First Design:** Footsteps audible 20m+, silencers viable, prone reduces noise 80% |
| **Progression Tree**  | Permanent, learnable advantages that persist thông qua death.                 | **Safe House & Trader Rep:** XP và reputation unlock better gear và passive buffs.            | **Skill Mastery:** vũ khí-cụ thể expertise (recoil reduction, reload speed) persists    |
| **Resource Heavy**    | Strong emphasis on inventory management và looting.                        | **Tetris Grid:** Spatial puzzle. đạn tracking manual (mag checking). Weight affects movement.  | **Smart Inventory AI:** Optional "suggest discard" highlights low-giá trị items khi full   |
| **Task Driven**       | rõ objectives guide quyết định beyond "kill everyone."                    | **Faction Quests:** cụ thể goals (mark territory, retrieve data, eliminate HVT).              | **Dynamic Objectives:** Quest difficulty scales với người chơi count in zone                 |
| **thời gian Pressure**     | Staying longer increases Risk & Reward.                                   | **Match Timer & Scav Waves:** 25-30min raids. Late-game scav spawn. Extracts close dynamically. | **Hot Zones:** High-giá trị loot spawns announce globally, tạo PvP magnets             |

#### Genre Analysis Insights

**What works across all successful extraction shooters:**

*  Asymmetric risk (you can lose more than you gain)
*  Knowledge-based advantage (map knowledge >> gear)
*  Sound as primary information (not visuals)
*  Looting as vulnerable trạng thái (tradeoff)
*  Extract camping as valid tactic (controversial nhưng accepted)

**What divides the genre:**

*  PvP intensity (Hunt: high, ARC Raiders: medium, Helldivers: low)
*  Realism level (Tarkov: hardcore, Arena Breakout: arcade)
*  Solo viability (Vigor: solo-friendly, Dark và Darker: squad-focused)
*  Session length (DMZ: 15min, Tarkov: 45min)

**Our positioning:**

* **Perspective**: Top-down (hero shooter looter extraction; operators với classes/abilities).
* **Target Session**: 15-20 minutes (mobile-friendly)
* **PvP Intensity**: Medium-High (not Tarkov hardcore, not CoD casual)
* **Realism**: Tactical (believable, not simulator)
* **Solo/Squad**: Balanced (both viable với different strategies)

***

### The Five cốt lõi Pillars (Our Identity)

Every design quyết định, cơ chế, và line of code must serve **at least one** of these five cốt lõi pillars. nếu a tính năng doesn't support any pillar, it phải được cut hoặc reworked. These pillars are **immutable** - they define what makes our game unique.

***

#### 1 High-Stakes Tension (Risk of Loss & Reward)

**Mantra:** _"Fear of Loss drives the Thrill of Gain."_

**Philosophy:**\
The game is defined by what you stand to lose. Progression is not linear; it is a wager. The tension comes from the imbalance between your vulnerability và the giá trị of your inventory. Every quyết định is a risk calculation.

**cốt lõi cơ chế That Embody This:**

| cơ chế               | Implementation                                           | Tension Created                         | Innovation                                |
| ---------------------- | -------------------------------------------------------- | --------------------------------------- | ----------------------------------------- |
| **Full Loot hệ thống**   | Death = lose all equipped gear (except secure container) | Fear of engagement, cautious play       | Insurance mitigates full loss             |
| **Crunchy Soundscape** | Footsteps audible 20m, gunshots echo realistically       | Paranoia, constant alertness            | Dynamic audio mixer (headsets modify mix) |
| **Low TTK**            | 2-4 shots to kill (head), 4-8 (torso)                    | Every fight is lethal, skill expression | giáp zones tạo variance               |
| **Inventory Tetris**   | Looting blocks vision, takes thời gian                        | Vulnerability trong khi reward phase       | Smart auto-sort learns preferences        |
| **Extract Camping**    | Người chơi có thể ambush extract points                        | Final tension spike trước safety       | Multiple extract options per raid         |

**Design Guidelines:**

*  Every action should have a consequence
*  Safety is an illusion (even in "safe" zones)
*  Loot giá trị phải được hiển thị rõ to tạo temptation
*  thời gian investment increases cảm xúc stakes
*  No bullet sponges (breaks immersion)
*  No "secure loot all" button (removes vulnerability)
*  No arcade movement (breaks tactical feel)

**người chơi Testimonial mục tiêu:**\
&#xNAN;_"My heart was pounding khi I extracted với a full bag of loot. I've never been this stressed in a mobile game."_ - Target người chơi Review

**Metrics:**

* Heart rate increase trong khi extract: +20-30 BPM (via smartwatch data)
* người chơi-reported "sweaty palms" moments: >3 per raid
* Extract success rate: 60-70% (not too punishing, not too easy)
* Gear loss cảm xúc impact: 7/10 (hurts nhưng not rage-quit)

***

#### 2 Tactical Fluidity (Survival & Tactical Depth)

**Mantra:** _"Control the Operator, not the Interface."_

**Philosophy:**\
Complexity should come from the situation, not the inputs. While the game simulates realistic ballistics và movement, the controls must respond **instantly** to người chơi intent. Mastery comes from quyết định-making, not button combos. Survival is a skill, not a grind.

**cốt lõi cơ chế:**

| hệ thống        | Realistic Simulation                       | Accessible Control                        | người chơi Mastery                        |
| ------------- | ------------------------------------------ | ----------------------------------------- | ------------------------------------- |
| **Movement**  | Inertia, momentum, weight penalties        | One-stick movement, instant sprint toggle | Reading terrain, positioning          |
| **Gunplay**   | Ballistics, recoil patterns, bullet drop   | Tap-to-aim, auto-lean, smart cover        | Recoil compensation, đạn management  |
| **Healing**   | Zone-based injuries, bleeding, fractures   | Drag-drop med on body part, auto-apply    | Resource conservation, timing         |
| **Inventory** | Grid spatial puzzle, weight hệ thống         | Tap-to-loot, auto-stack, smart discard    | Tetris optimization, giá trị assessment |
| **Sound**     | Realistic propagation, occlusion, headsets | Auto-balance, threat indicators           | Audio awareness, stealth tactics      |

**Action Chaining Examples:**

*  Reload while sprinting (reduced speed, animation blends)
*  Slide into cover while healing (slower heal, vulnerable)
*  Quick-peek corners while ADSing (vũ khí sway penalty)
*  Swap vũ khí while vaulting (equip delay, animation priority)

**Mobile-cụ thể Optimizations:**

* **Auto-Lean**: nhân vật auto-leans khi near cover edges
* **Smart Reload**: Auto-reloads khi mag empty + in cover
* **Tap-to-Loot**: Single tap to grab highlighted items
* **Gyro Aim**: Subtle phone tilt for precision (optional)
* **Haptic Feedback**: vũ khí recoil, hit confirmation, footstep proximity

**Design Guidelines:**

*  Every control should feel responsive (<100ms input lag)
*  Complexity from hệ thống interaction, not button count
*  Simulation fidelity where it matters (ballistics, audio)
*  Simplify where it doesn't (auto-reload in cover)
*  No animation locks for critical actions (healing, vũ khí swap)
*  No artificial input delay (feels laggy on mobile)
*  No mandatory button combos (accessibility concern)

**người chơi Testimonial mục tiêu:**\
&#xNAN;_"Controls feel buttery smooth. I can focus on tactics, not fighting the UI."_ - Target người chơi Review

**Metrics:**

* Input-to-action latency: <80ms (p95)
* người chơi-reported control frustration: <10%
* First-thời gian người chơi tutorial completion: >85%
* Control sơ đồ customization usage: <30% (default is good)

***

#### 3 Environmental Narratives (The Living World)

**Mantra:** _"Aethelgard is the First địch."_

**Philosophy:**\
Aethelgard (our world) is a nhân vật, not a backdrop. History is told thông qua the placement of objects, dead bodies, và lighting - **not text logs**. The world feels lived-in và abandoned, not built for a game. Người chơi nên learn the lore thông qua exploration, not cutscenes.

**World-Building Principles:**

| Principle                      | Execution                                     | người chơi trải nghiệm                | Example                                                                     |
| ------------------------------ | --------------------------------------------- | -------------------------------- | --------------------------------------------------------------------------- |
| **Logical Loot**               | Items spawn where they logically belong       | Rewards map knowledge            | Medkits in ambulances, đạn in checkpoints, food in kitchens                |
| **Environmental Storytelling** | Visual dioramas tell micro-stories            | Curiosity, immersion             | Barricaded room (trapped inside), abandoned camp (hasty exit), blood trails |
| **Atmospheric Guidance**       | Lighting guides người chơi mà không UI            | Exploration mà không hand-holding | Emergency red lights, flickering sparks, distant fires                      |
| **Dynamic Weather**            | Weather affects tactics (visibility, sound)   | Tactical adaptation              | Rain muffles footsteps, fog reduces sightlines, wind affects ballistics     |
| **thời gian of Day**                | Day/night cycle changes spawns và difficulty | Replayability, strategy          | Night = more loot, harder AI, NVG advantage                                 |

**Aethelgard Lore (High-Level):**

* **Setting**: Post-conflict industrial zone, 20 years sau "The Collapse"
* **Factions**: Military remnants, corporate scavengers, local militia
* **Conflict**: Resource scarcity, territorial disputes, tech salvage
* **người chơi Role**: Independent contractor (PMC) hired by factions
* **Mystery**: What caused The Collapse? (revealed thông qua exploration)

**Environmental chi tiết:**

**Industrial Zone (Launch Map):**

* Abandoned factories với active machinery (hazards)
* Makeshift refugee camps in warehouses
* Military checkpoints overgrown với vegetation
* Underground bunker hệ thống (tight CQB)
* Rooftop sniper nests (long sightlines)

**Audio Atmosphere:**

* Distant gunfire (other người chơi)
* Wind thông qua broken windows
* Machinery grinding intermittently
* Footsteps echo in metal structures
* Wildlife sounds (crows, rats) for ambiance

**Visual Language:**

* **Red Lighting**: Danger, high loot, AI presence
* **Flickering Lights**: Unstable area, ambush potential
* **Green Fog**: Chemical hazard, reduced visibility
* **Blue Glow**: Extraction point proximity
* **Yellow Sparks**: Interactive objects (doors, crates)

**Design Guidelines:**

*  Every prop has a reason to exist (no random clutter)
*  Loot placement tells a story (who was here? why?)
*  Environmental hazards are telegraphed visually
*  Sound design matches materials (metal, concrete, wood)
*  No symmetrical "esports" arenas (breaks immersion)
*  No nonsense loot (high-tech in primitive contexts)
*  No floating quest markers (cách dùng environment instead)

**người chơi Testimonial mục tiêu:**\
&#xNAN;_"I spent 10 minutes just exploring, finding hidden stories. This world feels REAL."_ - Target người chơi Review

**Metrics:**

* Exploration thời gian trước first combat: >3 minutes (curiosity)
* Environmental chi tiết appreciation: >60% (survey)
* Lore engagement (reading ghi chú, etc.): >40%
* Map knowledge retention: >70% sau 10 raids

***

#### 4 Task-Driven Agency (Meaningful Choices)

**Mantra:** _"Choose your Wager, Define your mục tiêu."_

**Philosophy:**\
Người chơi nên never be "just wandering." Every action is driven by a quest, a resource need, hoặc a tactical choice. Meaningful agency means the người chơi's quyết định (greed vs. safety, aggression vs. stealth) kết quả in **direct cảm xúc consequences**. The game respects người chơi choice.

**quyết định Frameworks:**

**Pre-Raid Planning:**

| quyết định            | Options                                           | Consequences                      | cảm xúc Weight           |
| ------------------- | ------------------------------------------------- | --------------------------------- | -------------------------- |
| **Loadout Choice**  | Budget (cheap gear) / Standard / Chad (expensive) | Economic risk vs combat power     | Fear of loss vs confidence |
| **Quest Selection** | Main (story), Daily (grind), Faction (reputation) | Objective focus, loot priority    | Achievement vs reward      |
| **Solo vs Squad**   | Solo (stealthy), Duo (balanced), Squad (loud)     | Tactics, loot split, coordination | Independence vs safety     |
| **Operator Choice** | Assault, Scout, Support, Medic, Engineer          | Playstyle, team composition       | Identity, mastery          |
| **thời gian of Day**     | Day (easier), Night (harder nhưng more loot)        | Risk/reward balance               | Confidence vs greed        |

**In-Raid quyết định:**

| Situation           | Options                                              | Immediate kết quả            | Long-Term Impact         |
| ------------------- | ---------------------------------------------------- | --------------------------- | ------------------------ |
| **địch Encounter** | Fight / Flee / Sneak / Parley (VOIP)                 | Combat outcome, loot, XP    | Reputation, skill growth |
| **Loot Container**  | Search (thời gian) / Ignore (speed) / Trap Check (safety) | Inventory fill, thời gian loss   | Gear progression         |
| **Extract Choice**  | Safe (far) / Risky (close) / Vehicle (expensive)     | Extract success, thời gian saved | Economic efficiency      |
| **Wounded Ally**    | Revive (risky) / Loot (greedy) / Leave (safe)        | Squad morale, loot giá trị    | Social reputation        |
| **Hot Zone**        | Enter (risk) / Avoid (safety) / Observe (intel)      | High reward vs death        | Wealth accumulation      |

**Quest hệ thống Design:**

**Main Quests (Story-Driven):**

* 5-10 hours of narrative content
* Unlock new zones và operators
* Cannot be failed, nhưng can be delayed
* Provide lore và world context
* **Example**: _"Investigate the Reactor Meltdown Site"_

**Daily Quests (Engagement Loop):**

* Refresh every 24 hours
* Quick 10-15 minute objectives
* Provide steady income và XP
* Encourage diverse playstyles
* **Example**: _"Extract với 5 Medkits"_, _"Kill 3 địch với headshots"_

**Faction Quests (Reputation Grind):**

* Multiple tiers per faction (Friendly, Honored, Exalted)
* Unlock faction-cụ thể gear và traders
* Often conflict với other factions (choice!)
* High difficulty, high reward
* **Example**: _"Mark 3 địch supply drops for airstrike"_

**Dynamic Objectives (Emergent):**

* Spawn mid-raid based on world events
* Optional nhưng highly rewarding
* tạo PvP hotspots
* Announced globally (risk/reward transparency)
* **Example**: _"Supply drop inbound in 5 minutes at Factory Roof"_

**Design Guidelines:**

*  Every quest must have a meaningful choice
*  Objectives should encourage map exploration
*  Failure is okay (no mandatory success)
*  Rewards scale với difficulty và risk
*  No mandatory linear paths (người chơi freedom)
*  No fetch quests mà không context (boring)
*  No "collect 50 items" grinds (respect thời gian)

**người chơi Testimonial mục tiêu:**\
&#xNAN;_"Every raid feels different. I'm always working toward something, nhưng I choose HOW."_ - Target người chơi Review

**Metrics:**

* Quest completion rate: >70% (main), >50% (daily), >30% (faction)
* người chơi-reported "felt like I had a mục đích": >80%
* Choice regret moments (good sign of weight): >2 per raid
* Loadout variance: >60% (người chơi experiment)

***

#### 5 Persistent Progression (Account & World Growth)

**Mantra:** _"Lose the Raid, Build the War."_

**Philosophy:**\
While individual raids carry the risk of loss, the **account's power và influence grow persistently**. Your actions today improve your capabilities tomorrow thông qua the Safe House, Traders, và Reputation. Even failure teaches lessons (XP, unlocks). This tạo the "one more raid" loop.

**Progression Layers:**

| Layer                   | Persistence   | Reset Conditions                        | người chơi giá trị                         |
| ----------------------- | ------------- | --------------------------------------- | ------------------------------------ |
| **Stash (Inventory)**   | Permanent     | Death (lost gear), Extract (saved gear) | Economic wealth, gear variety        |
| **Account Level**       | Permanent     | Never (seasonal soft reset)             | Skill unlocks, prestige              |
| **Safe House Upgrades** | Permanent     | Never                                   | Passive bonuses, crafting            |
| **Trader Reputation**   | Permanent     | Rare (faction betrayal)                 | Gear availability, discounts         |
| **Operator Mastery**    | Permanent     | Never                                   | Combat effectiveness, specialization |
| **vũ khí Proficiency**  | Permanent     | Never                                   | Recoil reduction, reload speed       |
| **Map Knowledge**       | người chơi Memory | Never (brain-based!)                    | Tactical advantage, loot efficiency  |
| **Season Pass**         | Seasonal      | Every 3 months                          | Cosmetics, exclusive loot            |

**Safe House hệ thống (Meta-Game Hub):**

**mục đích**: Persistent base that provides passive bonuses và crafting

**Modules:**

| Module             | Level 1            | Level 2                  | Level 3                  | chi phí Scaling       |
| ------------------ | ------------------ | ------------------------ | ------------------------ | ------------------ |
| **Stash**          | 10×28 grid         | 10×38 grid               | 10×48 grid               | 2M → 5M → 10M      |
| **Medstation**     | +10% heal speed    | +20%, craft bandages     | +30%, craft surgery kits | 500K → 1.5M → 3M   |
| **Workshop**       | Repair vũ khí     | Modify vũ khí           | Craft attachments        | 750K → 2M → 4M     |
| **Intelligence**   | Trader rep +5%     | Quest XP +10%            | Unlock rare quests       | 1M → 3M → 6M       |
| **Generator**      | Powers all modules | Reduced fuel chi phí        | Solar backup (free)      | 300K → 1M → 2.5M   |
| **Shooting Range** | Practice recoil    | Unlock vũ khí challenges | Gain proficiency XP      | Free → 500K → 1.5M |

**Trader Reputation hệ thống:**

**Tiers:**

* **Neutral** (0-1000 rep): Basic gear available
* **Friendly** (1001-3000): Discounts 10%, mid-tier gear
* **Honored** (3001-6000): Discounts 20%, high-tier gear
* **Exalted** (6001+): Discounts 30%, exclusive gear, special quests

**Reputation Gain:**

* Complete faction quests: +50-200 rep
* Extract với faction items: +10-30 rep
* Kill faction địch: +5-15 rep
* Betray faction: -500 rep (severe penalty)

**Reputation Loss:**

* Kill faction members: -50 rep
* Fail faction quests: -20 rep
* Trade với rival factions: -10 rep

**Operator Mastery:**

**Per-Operator Stats:**

* **Level**: 1-50 (XP from raids while playing operator)
* **Passive Bonus**: +1% to operator specialty per 5 levels
* **Unlocks**: New skins, voice lines, signature vũ khí

**Examples:**

* **Assault Operator (Mamba)**: +10% sprint speed at Lvl 50
* **Scout Operator (Hawk)**: +20% ADS speed at Lvl 50
* **Medic Operator (Cross)**: +30% heal speed at Lvl 50

**vũ khí Proficiency hệ thống:**

**How It Works:**

* Every vũ khí family has a proficiency level (1-20)
* Gain XP by: Kills, Headshots, Successful Raids với vũ khí
* Each level provides +2% recoil reduction, +1% reload speed

**vũ khí Families:**

* Assault Rifles (AK, M4, SCAR)
* SMGs (MP5, UMP, Vector)
* Sniper Rifles (SVD, M700, AWM)
* Shotguns (Saiga, M870, AA-12)
* Pistols (Glock, 1911, Deagle)

**Seasonal Content:**

**Season Structure** (3 months per season):

* New Battle Pass (100 tiers)
* Seasonal quest line (5-8 hours)
* Limited-thời gian event (week 6-8)
* Meta shake-up (vũ khí balance, map changes)
* Soft reset (rank reset, leaderboards)

**What DOESN'T Reset:**

* Safe House levels
* Trader reputation
* Operator mastery
* vũ khí proficiency
* Stash items (partial reset option for hardcore người chơi)

**Design Guidelines:**

*  Always reward thời gian invested (even failed raids)
*  Permanent unlocks feel meaningful
*  Short-term loss (gear) balanced by long-term gain (XP)
*  Multiple progression paths (choose focus)
*  No total account wipes (outside seasonal opt-in)
*  No pay-to-skip progression (monetization boundary)
*  No mandatory daily login rewards (respects người chơi thời gian)

**người chơi Testimonial mục tiêu:**\
&#xNAN;_"I lost my best gear today, nhưng I unlocked Level 2 Safe House và got closer to Honored với the Militia. Still feels like progress."_ - Target người chơi Review

**Metrics:**

* Average account level sau 1 month: 25-30
* Safe House module upgrade rate: >2 per week
* Operator mastery diversity: >3 operators at Lvl 10+
* người chơi-reported "feels rewarding even khi losing": >65%
* Retention (30-day): >50% (strong progression hook)

***

### Pillar Conflict Resolution Framework

khi cốt lõi pillars contradict each other, cách dùng this **hierarchy** to decide:

#### quyết định Tree

```
1. Does it affect TENSION (safety vs risk)?
   YES → Prioritize Tension over all else
   NO → Continue

2. Does it affect FLUIDITY (controls, responsiveness)?
   YES → Prioritize Fluidity over Realism/Narrative
   NO → Continue

3. Does it affect NARRATIVE (world consistency)?
   YES → Ensure it serves Tension or Agency
   NO → Continue

4. Does it affect AGENCY (player choice)?
   YES → Ensure choices are meaningful, not illusion
   NO → Continue

5. Does it affect PROGRESSION (account growth)?
   YES → Balance short-term loss with long-term gain
   NO → Continue
```

#### Real-World Examples

**Example 1: Healing While Shooting**

**Conflict**: Tactical Fluidity (accessibility) vs High-Stakes Tension (vulnerability)

**Pillar Analysis:**

* Fluidity says: _Allow healing while shooting (mobile-friendly)_
* Tension says: _Healing must tạo vulnerability (risk)_

**Resolution**: **Tension wins** (Priority 1)

* **quyết định**: Healing stops vũ khí cách dùng, slows movement 50%
* **Rationale**: tạo tactical choice (cover first, then heal)
* **Compensation**: Fast heal items (3 seconds) for accessibility

***

**Example 2: UI Quest Markers**

**Conflict**: Environmental Narrative (immersion) vs Task-Driven Agency (clarity)

**Pillar Analysis:**

* Narrative says: _No floating markers (breaks immersion)_
* Agency says: _Players need rõ objectives (accessibility)_

**Resolution**: **Hybrid approach** (Both matter)

* **quyết định**: Compass markers only (not in-world floaters)
* **Enhancement**: Environmental clues (smoke, lights) guide người chơi
* **Accessibility**: Toggle "hint mode" for new người chơi (first 10 raids)

***

**Example 3: vũ khí Realism**

**Conflict**: Tactical Fluidity (responsive controls) vs Environmental Narrative (realism)

**Pillar Analysis:**

* Fluidity says: _Instant vũ khí swap (responsive)_
* Narrative says: _Realistic swap speed (heavy vũ khí slow)_

**Resolution**: **Fluidity wins** (Priority 2)

* **quyết định**: vũ khí swap faster than real life (2s → 1s)
* **Rationale**: Simulation fidelity matters for ballistics, not animations
* **Compromise**: Different vũ khí classes have variance (pistol 0.5s, LMG 1.5s)

***

**Example 4: Account Wipes**

**Conflict**: High-Stakes Tension (reset for freshness) vs Persistent Progression (respect thời gian)

**Pillar Analysis:**

* Tension says: _Seasonal wipes keep economy fresh_
* Progression says: _Players hate losing months of work_

**Resolution**: **Progression wins** (Priority 5)

* **quyết định**: Opt-in wipes only (hardcore mode)
* **Compromise**: Seasonal soft resets (ranks, leaderboards, not Safe House)
* **Reward**: Exclusive cosmetics for wipe participants

***

### người chơi trải nghiệm Goals (cảm xúc Targets)

#### Target Emotions Per Raid Phase

| Phase                  | Duration | Target Emotion                    | cơ chế Driver                 |
| ---------------------- | -------- | --------------------------------- | ------------------------------- |
| **Pre-Raid Planning**  | 2-3 min  | Anticipation, Strategy            | Loadout choice, quest selection |
| **Spawn & Early Loot** | 3-5 min  | Curiosity, Greed                  | Exploration, container opening  |
| **First Contact**      | Variable | Fear, Adrenaline                  | Gunfight, sound cues            |
| **Mid-Raid Looting**   | 5-10 min | Tension, quyết định Fatigue         | Bag filling, Tetris puzzle      |
| **Extract quyết định**   | 1-2 min  | Paranoia, Calculation             | Route choice, risk assessment   |
| **Extraction Attempt** | 2-3 min  | Peak Tension, Relief (nếu success) | Extract camping threat          |
| **Post-Raid**          | 2-3 min  | Satisfaction / Disappointment     | Loot sorting, progression gains |

#### cảm xúc Spectrum Balance

```
Low Tension ←―――――――――――→ High Tension
         ↓
    [Sweet Spot]
    (70% of raids)
```

**mục tiêu Distribution:**

* 10% raids: Low tension (easy wins, learning)
* 70% raids: Medium-high tension (close calls, sweaty palms)
* 20% raids: Extreme tension (near-death, massive loot)

**Metrics to Track:**

* người chơi-reported "heart racing" moments: >3 per raid
* Ragequit rate sau death: <15% (frustration tolerable)
* Extract satisfaction: >8/10 (khi successful)
* "One more raid" intent: >60% (addictive loop)

***

### The cốt lõi Loops (Macro & Micro)

#### Macro Loop (Long-Term Growth)

**30-Day người chơi Journey:**

```
Week 1: LEARN
- Tutorial completion
- First 10 raids (high death rate okay)
- Unlock 2-3 operators
- Basic loadout economy established

Week 2: OPTIMIZE
- Favorite weapon identified
- Main quests progressing
- First Safe House upgrade
- Map knowledge improving

Week 3: MASTER
- Extract rate 60%+
- Trader Friendly reached
- Operator mastery Lvl 10+
- Meta loadouts tested

Week 4: ENDGAME
- High-tier raids
- Faction quest grinding
- Safe House Level 2+
- Seasonal event participation
```

**chi tiết Macro Loop:**

1. **PREPARE** (2-3 minutes):
   * Assess economic situation (can I afford to lose this loadout?)
   * Build loadout based on quest objectives
   * Accept faction tasks aligned với playstyle
   * Select operator và thời gian of day
   * Mental prep (where will I land? what's my route?)
2. **RAID** (15-20 minutes):
   * Spawn → Orient → Move to objective
   * Loot containers en route (opportunity chi phí)
   * Complete quests (primary mục tiêu)
   * Engage/avoid địch (tactical choice)
   * Fill inventory (greed vs mobility)
   * Monitor thời gian (extract urgency)
3. **EXTRACT** (2-3 minutes):
   * Choose extract point (risk calculation)
   * Final loot quyết định (discard low-giá trị)
   * Navigate to extract under pressure
   * Survive extract timer (15 seconds vulnerable)
   * Breath held until "Extracted" màn hình
4. **PROGRESS** (2-3 minutes):
   * Sell loot to traders (economy management)
   * Repair damaged gear (durability hệ thống)
   * upgrade Safe House (long-term investment)
   * Increase Trader Reputation (quest turn-ins)
   * Check progression stats (dopamine hit)
   * Plan next raid (loop restart)

**Loop Timing:**

* Full cycle: 22-31 minutes per raid
* Ideal session: 3-4 raids (1-2 hours)
* Hardcore session: 6-8 raids (3-4 hours)

***

#### Micro Loop (Immediate Tension)

**OODA Loop (Military quyết định-Making):**

```
OBSERVE → ORIENT → DECIDE → ACT → ADAPT
   ↑                                    ↓
   └────────────────────────────────────┘
           (Continuous Loop)
```

**chi tiết Breakdown:**

1. **OBSERVE** (0.5-2 seconds):
   * **Sound Cues**: Footsteps, gunshots, door opens, mag check
   * **Visual Glints**: Scope reflections, muzzle flash, movement
   * **Environmental Traces**: Blood trails, open containers, corpses
   * **Intel**: Map pings (squad), quest markers, extract timers
2. **ORIENT** (1-3 seconds):
   * **Threat Assessment**: How many địch? What gear?
   * **Cover Check**: Nearest hard cover, concealment, escape routes
   * **Objective Check**: Quest priority, loot giá trị, thời gian remaining
   * **Resource Check**: đạn count, med availability, stamina
3. **DECIDE** (0.5-1 second):
   * **Fight**: Engage nếu advantageous (better position, gear, surprise)
   * **Flight**: Retreat nếu outmatched (low HP, outnumbered, bad position)
   * **Sneak**: Avoid nếu unnecessary (quest focus, resource conservation)
   * **Parley**: Communicate via VOIP (rare, high-risk trust scenario)
4. **ACT** (1-5 seconds):
   * **Execute Tactical Maneuver**: Flank, suppress, advance, retreat
   * **vũ khí Handling**: Aim, fire, reload, swap, mag check
   * **Consumable cách dùng**: Heal, painkiller, grenade, utility
   * **Movement**: Sprint, slide, prone, vault, door breach
5. **ADAPT** (0.5-1 second):
   * **Review Results**: Hit/miss, địch down, took damage, position revealed
   * **Adjust Plan**: New cover, different angle, vũ khí swap, retreat
   * **Reset Loop**: Back to OBSERVE với updated information
   * **Mental Note**: Learn địch behavior, vũ khí effectiveness

**Micro Loop Timing:**

* Full cycle: 3-12 seconds per engagement
* Fastest (instinct): 3-5 seconds (close range, high skill)
* Tactical (methodical): 8-12 seconds (long range, team coordination)

**quyết định Speed Hierarchy:**

```
PANIC RESPONSE (0-1s):
└─ Incoming fire → COVER

TRAINED RESPONSE (1-3s):
├─ Gunshot sound → LOCATE + AIM
└─ Footsteps close → AIM + WAIT

TACTICAL ANALYSIS (3-10s):
├─ Enemy spotted → ASSESS + FLANK
├─ Objective near → APPROACH + LOOT
└─ Time low → ROUTE + EXTRACT

STRATEGIC PLANNING (10s+):
├─ Multiple enemies → RETREAT + REGROUP
├─ Low resources → EXTRACT + CONSERVE
└─ Quest complete → EXIT + SUCCEED
```

**Design Guidelines for Micro Loop:**

*  Information nên được actionable (sound = direction)
*  quyết định should have rõ consequences (fight = risk)
*  Actions should feel responsive (instant input)
*  Adaptation nên được rewarded (learning AI behavior)
*  No information overload (too many UI elements)
*  No forced waiting (animation locks trong khi combat)
*  No unclear threats (địch visibility phải được fair)

***

### Game Feel Goals (Sensory trải nghiệm)

#### "Crunchy" Combat (Weighty Impact)

**Audio Design:**

| Element        | Implementation                                             | người chơi Perception   |
| -------------- | ---------------------------------------------------------- | ------------------- |
| **Gunshots**   | Bass-heavy, reverb based on environment (indoor/outdoor)   | Powerful, real      |
| **Impacts**    | Material-based sounds (metal, wood, flesh)                 | Satisfying hits     |
| **Explosions** | Tinnitus effect (ringing), màn hình shake, audio compression | Disorienting danger |
| **Footsteps**  | Surface-cụ thể (metal clang, wood creak, dirt crunch)    | Tactical intel      |
| **Ambient**    | Environmental layers (wind, machinery, distant combat)     | Living world        |

**Visual Design:**

| Effect           | Trigger                    | Duration            | mục đích           |
| ---------------- | -------------------------- | ------------------- | ----------------- |
| **Debris**       | Bullet impacts, explosions | 2-5 seconds         | Convey power      |
| **Sparks**       | Metal surfaces hit         | 0.5-1 second        | Visual feedback   |
| **Blood**        | Flesh hits                 | Persistent (decals) | Confirm damage    |
| **Muzzle Flash** | vũ khí fire                | 1 frame             | Reveal position   |
| **màn hình Shake** | Taking damage, explosions  | 0.2-0.5 seconds     | Visceral feedback |
| **Lens Effects** | Scope glint, NVG blur      | Persistent          | Realism, balance  |

**Haptic Feedback (Mobile):**

| Event               | Vibration Pattern                     | Intensity   |
| ------------------- | ------------------------------------- | ----------- |
| **vũ khí Fire**     | Short burst (100ms), varies by vũ khí | Medium-High |
| **Taking Damage**   | Long pulse (300ms), direction-based   | High        |
| **Footstep Near**   | Subtle pulse (50ms), distance-based   | Low         |
| **Grenade Throw**   | Tap (50ms)                            | Low         |
| **Reload Complete** | Double tap (50ms + 50ms)              | Low         |
| **địch Killed**    | success pulse (200ms)                 | Medium      |

**Input Feel:**

| hệ thống         | Responsiveness                                  | Precision | Mastery                        |
| -------------- | ----------------------------------------------- | --------- | ------------------------------ |
| **Recoil**     | Predictable patterns (learnable), no RNG spray  | High      | Muscle memory compensation     |
| **Hit Stop**   | 0.1s freeze on melee impact, headshot           | High      | Confirms kill                  |
| **Aim Assist** | Subtle magnetism (10% drag), tap-to-snap option | Medium    | Accessibility mà không auto-aim |

***

#### "Weighty" Movement (Grounded Feel)

**Inertia hệ thống:**

| Weight Tier          | Acceleration thời gian | Deceleration thời gian | Turn Speed | Jump Height |
| -------------------- | ----------------- | ----------------- | ---------- | ----------- |
| **Light (0-25kg)**   | 0.1s              | 0.1s              | Instant    | 100%        |
| **Medium (25-40kg)** | 0.3s              | 0.2s              | 0.2s delay | 75%         |
| **Heavy (40-55kg)**  | 0.5s              | 0.4s              | 0.5s delay | 40%         |
| **Critical (55kg+)** | 0.8s              | 0.6s              | 1.0s delay | 0%          |

**Momentum Preservation:**

| Action                  | Momentum Carry | Speed Modifier    | Duration   |
| ----------------------- | -------------- | ----------------- | ---------- |
| **Sprint → Slide**      | 100% carry     | +10% speed        | 2 seconds  |
| **Jump from Sprint**    | 80% carry      | -20% air control  | Until land |
| **Vault Over Obstacle** | 60% carry      | -30% trong khi vault | 1 second   |
| **Crouch While Moving** | 40% carry      | -50% speed        | Persistent |

**Camera & Animation:**

| hệ thống             | Effect                                       | mục đích             | Intensity                      |
| ------------------ | -------------------------------------------- | ------------------- | ------------------------------ |
| **Head Bob**       | Vertical sway synced to footsteps            | Grounding, feedback | Subtle (5% màn hình height)      |
| **vũ khí Sway**    | Breathing pattern, stamina affects intensity | Realism, skill gap  | Medium (2% màn hình width)       |
| **Landing Impact** | màn hình dip, audio crunch, brief slowdown     | Weight feedback     | High (10% màn hình height, 0.3s) |
| **Sprint Tilt**    | Slight forward lean, peripheral blur         | Speed sensation     | Subtle (3° tilt)               |

**Stamina Integration:**

```
Stamina Pool: 100 points

Actions:
- Sprint: -10/s
- Jump: -15
- Melee: -20
- Hold Breath (ADS): -5/s

Regeneration:
- Standing Still: +20/s
- Walking: +10/s
- Crouched: +15/s
- Prone: +25/s

Weight Modifiers:
- Light: 1.0x regen
- Medium: 0.75x regen
- Heavy: 0.5x regen
- Critical: 0x regen (drain -5/s)
```

**Design Guidelines:**

*  Movement should feel responsive nhưng not floaty
*  Weight nên được palpable mà không being frustrating
*  Momentum adds skill expression (slide-jumps, etc.)
*  Camera effects enhance immersion mà không nausea
*  No artificial "slow walk" animations (người chơi controls speed)
*  No exaggerated head bob (motion sickness concern)
*  No permanent movement penalties (temporary stamina okay)

***

### Quality Assurance checklist (tính năng Gate)

cách dùng this checklist for **every new tính năng request**. nếu a tính năng fails 3+ checks, it nên được reconsidered hoặc reworked.

#### Pillar Validation

| # | Question                                                 | Pass Criteria                                  | Red Flags                                |
| - | -------------------------------------------------------- | ---------------------------------------------- | ---------------------------------------- |
| 1 | Does it increase **Tension** hoặc **Tactical Depth**?      | Adds meaningful risk/reward hoặc tactical choice | Removes consequences, simplifies choices |
| 2 | Does it respect the **flow (Fluidity)** of controls?     | Feels responsive, doesn't lock inputs          | Animation locks, artificial delays       |
| 3 | Does it make sense in the **Context of Aethelgard**?     | Logically fits world, enhances narrative       | Breaks immersion, generic design         |
| 4 | Does it provide the người chơi với a **Meaningful Choice**? | Actual agency với consequences                | Illusion of choice, mandatory actions    |
| 5 | Does it contribute to **Persistent Progression**?        | Rewards thời gian invested, long-term giá trị         | Pure session-based, no account impact    |

#### Implementation Validation

| #  | Question                             | Pass Criteria                          | Red Flags                                         |
| -- | ------------------------------------ | -------------------------------------- | ------------------------------------------------- |
| 6  | Can it be built within scope/budget? | Realistic estimate, proven tech        | Requires new engine tính năng, unclear feasibility |
| 7  | Does it conflict với other hệ thống? | Clean integration, no breaking changes | Requires major refactor, dependency hell          |
| 8  | Is it testable và balanceable?      | rõ metrics, tuning parameters       | Black box behavior, no dials to adjust            |
| 9  | Does it work on mobile hardware?     | 60 FPS on mid-range devices            | Performance concerns, battery drain               |
| 10 | Is it monetization-safe?             | No pay-to-win implications             | Could be sold for competitive advantage           |

#### người chơi trải nghiệm Validation

| #  | Question                                        | Pass Criteria                                  | Red Flags                                 |
| -- | ----------------------------------------------- | ---------------------------------------------- | ----------------------------------------- |
| 11 | Does it enhance fun mà không removing challenge? | Adds options, maintains skill ceiling          | Removes difficulty entirely, hand-holding |
| 12 | Is it accessible to new người chơi?                | rõ tutorial, forgiving learning curve       | Requires 10+ hours to understand          |
| 13 | Does it add depth for veterans?                 | Mastery potential, optimization possibilities  | Ceiling too low, "solved" immediately     |
| 14 | Would it generate positive community sentiment? | Addresses pain points, adds requested tính năng | Community backlash likely, controversial  |
| 15 | Does it align với our market positioning?      | Fits "tactical mobile extraction shooter"      | Too casual, too hardcore, wrong genre     |

#### quyết định matrix

**Pass All 15 Checks:**

*  Greenlight - Add to roadmap

**Pass 12-14 Checks:**

*  Conditional - Rework failing areas, re-evaluate

**Pass 9-11 Checks:**

*  Reconsider - Likely not worth the effort

**Pass <9 Checks:**

*  Reject - Does not align với cốt lõi vision

***

### Metrics & success Criteria

#### Pillar-cụ thể KPIs

**1. High-Stakes Tension:**

* Extract success rate: 60-70% (balanced challenge)
* người chơi-reported "heart racing": >3 moments/raid
* Gear loss cảm xúc impact: 7/10 (hurts nhưng doesn't rage-quit)
* Extract camping encounters: 10-15% of extracts

**2. Tactical Fluidity:**

* Input latency: <80ms (p95)
* Control frustration: <10% of người chơi
* First-thời gian tutorial completion: >85%
* Movement mastery (advanced tech usage): >40% at 50 hours

**3. Environmental Narratives:**

* Exploration thời gian trước first combat: >3 minutes
* Lore engagement: >40% read environmental ghi chú
* Map knowledge retention: >70% sau 10 raids
* người chơi-reported "world feels real": >60%

**4. Task-Driven Agency:**

* Quest completion rate: >70% (main), >50% (daily)
* Loadout variance: >60% (experimentation)
* Regret moments: >2/raid (meaningful choices)
* "Felt purposeful": >80% of raids

**5. Persistent Progression:**

* 30-day retention: >50%
* Average account level at 1 month: 25-30
* Safe House upgrade frequency: >2/week
* "Rewarding even khi losing": >65%

#### Holistic success Metrics

**Engagement:**

* DAU/MAU ratio: >0.3 (sticky game)
* Average session length: 1-2 hours
* Sessions per week: 8-12 (highly engaged)
* Lifetime giá trị (LTV): >$30 (at 6 months)

**Sentiment:**

* App Store rating: >4.2 stars
* NPS (Net Promoter Score): >40
* Community toxicity: <15% (supportive playerbase)
* Creator/streamer adoption: >100 active streamers

**Competitive:**

* Market share (mobile extraction shooters): Top 3
* Retention vs competitors: +15% above average
* Revenue per user: Top quartile
* Critical reception: >80/100 Metacritic

***

### tài liệu Ownership & Maintenance

#### Ownership

| Role                   | Responsibility                            | Authority                                       |
| ---------------------- | ----------------------------------------- | ----------------------------------------------- |
| **Creative Director**  | Pillar định nghĩa, vision alignment       | Final say on pillar conflicts                   |
| **Lead Game Designer** | Pillar implementation, tính năng validation | Veto tính năng that violate pillars              |
| **Studio Head**        | Budget, scope, timeline                   | Can delay/cut tính năng, not change pillars      |
| **Community Manager**  | người chơi feedback integration               | Advocate for người chơi sentiment in pillar reviews |

#### Review Cadence

**Monthly Validation:**

* Playtest sessions against pillar goals
* Metrics review (are we hitting targets?)
* tính năng gate audit (any exceptions granted? why?)
* Team survey (do pillars still resonate?)

**Quarterly Deep Review:**

* External playtest với target audience
* Competitor analysis (how are we positioning?)
* Pivot assessment (do pillars need refinement?)
* Stakeholder alignment (exec, investors, partners)

**Major Update:**

* Version number bump (v2.0, v3.0, etc.)
* Full changelog với rationale
* Team-wide review và sign-off
* Public communication (nếu appropriate)

#### Change Control

**How to Propose a Pillar Change:**

1. **Submit RFC (Request for Comment)**:
   * tài liệu: Why change? What's broken? What's the fix?
   * Evidence: Metrics, người chơi feedback, competitive pressure
   * Impact: What hệ thống would need to change?
2. **Leadership Review**:
   * Creative Director + Lead Designer + Studio Head
   * quyết định within 2 weeks
3. **Team Discussion**:
   * nếu approved, full team workshop
   * Address concerns, refine language
   * Build consensus (not unanimity, nhưng mua-in)
4. **Implementation**:
   * Update this tài liệu
   * Cascade changes to all dependent docs
   * Communicate to team và community (nếu public)

**khi to Change Pillars:**

*  NEVER: Based on one bad playtest
*  RARELY: Due to market trends (we lead, not follow)
*  SOMETIMES: khi persistent data shows fundamental flaw
*  DEFINITELY: nếu cốt lõi vision shifts (rare, existential)

***

### Related Documents

**cốt lõi GDD Suite:**

* [Project Scope & Vision](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/ProjectScope/project-scope-enhanced.md) - High-level game định nghĩa
* [MVP Scope](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/ProjectScope/mvp-enhanced.md) - What we're building first
* [Non-Goals](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/ProjectScope/non-goals-enhanced.md) - What we're explicitly NOT doing
* [Inventory & Gear hệ thống](inventory-gear-hệ thống-enhanced.md) - Deep dive on loot cơ chế

**Implementation Guides:**

* [Competitive Analysis](competitive-analysis-extraction-shooters.md) - Market positioning

**người chơi-Facing:**

* Game Trailer (Hook: "Fear of Loss, Thrill of Gain")
* Tutorial Design (Teach pillars thông qua play)
* Community Guidelines (Toxicity = violation of "Task-Driven Agency" pillar)

***

### Changelog

| Version  | Date       | Author                 | Changes                                                                                                                                                                                                                                                   |
| -------- | ---------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **v1.0** | 2026-02-07 | Creative Director      | Initial philosophy định nghĩa                                                                                                                                                                                                                             |
| **v1.1** | 2026-02-09 | Lead Designer          | Added Genre Pillars from industry research                                                                                                                                                                                                                |
| **v1.2** | 2026-02-09 | Creative Director      | Unified to Five cốt lõi Pillars, standardized Aethelgard                                                                                                                                                                                                     |
| **v2.0** | 2026-02-11 | Claude AI (Consultant) | **MAJOR UPDATE**: Enhanced với 2024-2026 best practices, chi tiết metrics, conflict resolution framework, người chơi trải nghiệm goals, quality checklist, và comprehensive examples. Researched modern GDD standards và extraction shooter genre analysis. |

***

**END OF tài liệu**

_"These pillars are not suggestions. They are the laws by which we build this world."_ - Creative Director

***

**Next Steps for Implementation:**

1. Share với full team for feedback (1 week review period)
2. Conduct pillar validation workshop (all hands, 4 hours)
3. Update all tính năng requests in backlog against new checklist
4. tạo pillar-based onboarding for new team members
5. Quarterly review scheduled (May 11, 2026)
