---
title: "Design Pillars & Core Philosophy - Enhanced Edition"
linkTitle: "Design Pillars"
type: docs
weight: 7
version: 2.0
last_updated: 2026-02-11
---

> **Living Document Status**: This document evolves with the game. All features must align with these pillars.  
> **Authority Level**: Ultimate - These pillars override all other design decisions.  
> **Review Cadence**: Monthly validation, quarterly deep review

---

## 📊 Document Structure

```
1. Genre Foundation (What defines extraction shooters)
2. Our Five Core Pillars (How we differentiate)
3. Player Experience Goals (What players should feel)
4. Core Gameplay Loops (Macro & Micro)
5. Pillar Conflict Resolution (Decision framework)
6. Quality Checklist (Gate for all features)
```

---

## 🏛️ Genre Pillars (Extraction Shooter DNA)

These six foundational pillars define the extraction shooter genre based on industry analysis of Tarkov, Hunt: Showdown, Arena Breakout, ARC Raiders, and Dark and Darker. **Every extraction shooter must have these** - they are non-negotiable genre requirements.

| Pillar               | Genre Definition | Our Implementation | Innovation Point |
| :------------------- | :--------------- | :----------------- | :--------------- |
| **Risk of Loss** | Constant awareness that progress can be lost. Dying = losing equipped gear. | **Full Loot Drop:** Everything equipped is at risk. Creates emotional investment in each raid. | **Insurance System:** 70% return rate for unlooted gear after 24h (anti-frustration) |
| **Survival Priority** | Survival prioritized over unnecessary combat. Avoiding fights is valid. | **Health Scarcity:** Meds are expensive. Every engagement drains resources. Stealth is viable. | **Sound-First Design:** Footsteps audible 20m+, silencers viable, prone reduces noise 80% |
| **Progression Tree** | Permanent, learnable advantages that persist through death. | **Hideout & Trader Rep:** XP and reputation unlock better gear and passive buffs. | **Skill Mastery:** Weapon-specific expertise (recoil reduction, reload speed) persists |
| **Resource Heavy** | Strong emphasis on inventory management and looting. | **Tetris Grid:** Spatial puzzle. Ammo tracking manual (mag checking). Weight affects movement. | **Smart Inventory AI:** Optional "suggest discard" highlights low-value items when full |
| **Task Driven** | Clear objectives guide decisions beyond "kill everyone." | **Faction Quests:** Specific goals (mark territory, retrieve data, eliminate HVT). | **Dynamic Objectives:** Quest difficulty scales with player count in zone |
| **Time Pressure** | Staying longer increases risk and reward. | **Match Timer & Scav Waves:** 25-30min raids. Late-game scav spawn. Extracts close dynamically. | **Hot Zones:** High-value loot spawns announce globally, creating PvP magnets |

### Genre Analysis Insights

**What works across all successful extraction shooters:**
- ✅ Asymmetric risk (you can lose more than you gain)
- ✅ Knowledge-based advantage (map knowledge >> gear)
- ✅ Sound as primary information (not visuals)
- ✅ Looting as vulnerable state (tradeoff)
- ✅ Extract camping as valid tactic (controversial but accepted)

**What divides the genre:**
- ⚠️ PvP intensity (Hunt: high, ARC Raiders: medium, Helldivers: low)
- ⚠️ Realism level (Tarkov: hardcore, Arena Breakout: arcade)
- ⚠️ Solo viability (Vigor: solo-friendly, Dark and Darker: squad-focused)
- ⚠️ Session length (DMZ: 15min, Tarkov: 45min)

**Our positioning:**
- **Perspective**: Top-down (hero shooter looter extraction; operators with classes/abilities).
- **Target Session**: 15-20 minutes (mobile-friendly)
- **PvP Intensity**: Medium-High (not Tarkov hardcore, not CoD casual)
- **Realism**: Tactical (believable, not simulator)
- **Solo/Squad**: Balanced (both viable with different strategies)

---

## 🗿 The Five Core Pillars (Our Identity)

Every design decision, mechanic, and line of code must serve **at least one** of these five core pillars. If a feature doesn't support any pillar, it must be cut or reworked. These pillars are **immutable** - they define what makes our game unique.

---

### 1️⃣ High-Stakes Tension (Risk of Loss & Reward)

**Mantra:** *"Fear of Loss drives the Thrill of Gain."*

**Philosophy:**  
The game is defined by what you stand to lose. Progression is not linear; it is a wager. The tension comes from the imbalance between your vulnerability and the value of your inventory. Every decision is a risk calculation.

**Core Mechanics That Embody This:**

| Mechanic | Implementation | Tension Created | Innovation |
|:---------|:--------------|:----------------|:-----------|
| **Full Loot System** | Death = lose all equipped gear (except secure container) | Fear of engagement, cautious play | Insurance mitigates full loss |
| **Crunchy Soundscape** | Footsteps audible 20m, gunshots echo realistically | Paranoia, constant alertness | Dynamic audio mixer (headsets modify mix) |
| **Low TTK** | 2-4 shots to kill (head), 4-8 (torso) | Every fight is lethal, skill expression | Armor zones create variance |
| **Inventory Tetris** | Looting blocks vision, takes time | Vulnerability during reward phase | Smart auto-sort learns preferences |
| **Extract Camping** | Players can ambush extract points | Final tension spike before safety | Multiple extract options per raid |

**Design Guidelines:**
- ✅ Every action should have a consequence
- ✅ Safety is an illusion (even in "safe" zones)
- ✅ Loot value must be visible to create temptation
- ✅ Time investment increases emotional stakes
- ❌ No bullet sponges (breaks immersion)
- ❌ No "secure loot all" button (removes vulnerability)
- ❌ No arcade movement (breaks tactical feel)

**Player Testimonial Goal:**  
*"My heart was pounding when I extracted with a full bag of loot. I've never been this stressed in a mobile game."* - Target Player Review

**Metrics:**
- Heart rate increase during extract: +20-30 BPM (via smartwatch data)
- Player-reported "sweaty palms" moments: >3 per raid
- Extract success rate: 60-70% (not too punishing, not too easy)
- Gear loss emotional impact: 7/10 (hurts but not rage-quit)

---

### 2️⃣ Tactical Fluidity (Survival & Tactical Depth)

**Mantra:** *"Control the Operator, not the Interface."*

**Philosophy:**  
Complexity should come from the situation, not the inputs. While the game simulates realistic ballistics and movement, the controls must respond **instantly** to player intent. Mastery comes from decision-making, not button combos. Survival is a skill, not a grind.

**Core Mechanics:**

| System | Realistic Simulation | Accessible Control | Player Mastery |
|:-------|:--------------------|:-------------------|:---------------|
| **Movement** | Inertia, momentum, weight penalties | One-stick movement, instant sprint toggle | Reading terrain, positioning |
| **Gunplay** | Ballistics, recoil patterns, bullet drop | Tap-to-aim, auto-lean, smart cover | Recoil compensation, ammo management |
| **Healing** | Zone-based injuries, bleeding, fractures | Drag-drop med on body part, auto-apply | Resource conservation, timing |
| **Inventory** | Grid spatial puzzle, weight system | Tap-to-loot, auto-stack, smart discard | Tetris optimization, value assessment |
| **Sound** | Realistic propagation, occlusion, headsets | Auto-balance, threat indicators | Audio awareness, stealth tactics |

**Action Chaining Examples:**
- ✅ Reload while sprinting (reduced speed, animation blends)
- ✅ Slide into cover while healing (slower heal, vulnerable)
- ✅ Quick-peek corners while ADSing (weapon sway penalty)
- ✅ Swap weapons while vaulting (equip delay, animation priority)

**Mobile-Specific Optimizations:**
- **Auto-Lean**: Character auto-leans when near cover edges
- **Smart Reload**: Auto-reloads when mag empty + in cover
- **Tap-to-Loot**: Single tap to grab highlighted items
- **Gyro Aim**: Subtle phone tilt for precision (optional)
- **Haptic Feedback**: Weapon recoil, hit confirmation, footstep proximity

**Design Guidelines:**
- ✅ Every control should feel responsive (<100ms input lag)
- ✅ Complexity from systems interaction, not button count
- ✅ Simulation fidelity where it matters (ballistics, audio)
- ✅ Simplify where it doesn't (auto-reload in cover)
- ❌ No animation locks for critical actions (healing, weapon swap)
- ❌ No artificial input delay (feels laggy on mobile)
- ❌ No mandatory button combos (accessibility concern)

**Player Testimonial Goal:**  
*"Controls feel buttery smooth. I can focus on tactics, not fighting the UI."* - Target Player Review

**Metrics:**
- Input-to-action latency: <80ms (p95)
- Player-reported control frustration: <10%
- First-time player tutorial completion: >85%
- Control scheme customization usage: <30% (default is good)

---

### 3️⃣ Environmental Narratives (The Living World)

**Mantra:** *"Aethelgard is the First Enemy."*

**Philosophy:**  
Aethelgard (our world) is a character, not a backdrop. History is told through the placement of objects, dead bodies, and lighting - **not text logs**. The world feels lived-in and abandoned, not built for a game. Players should learn the lore through exploration, not cutscenes.

**World-Building Principles:**

| Principle | Execution | Player Experience | Example |
|:----------|:----------|:------------------|:--------|
| **Logical Loot** | Items spawn where they logically belong | Rewards map knowledge | Medkits in ambulances, ammo in checkpoints, food in kitchens |
| **Environmental Storytelling** | Visual dioramas tell micro-stories | Curiosity, immersion | Barricaded room (trapped inside), abandoned camp (hasty exit), blood trails |
| **Atmospheric Guidance** | Lighting guides players without UI | Exploration without hand-holding | Emergency red lights, flickering sparks, distant fires |
| **Dynamic Weather** | Weather affects tactics (visibility, sound) | Tactical adaptation | Rain muffles footsteps, fog reduces sightlines, wind affects ballistics |
| **Time of Day** | Day/night cycle changes spawns and difficulty | Replayability, strategy | Night = more loot, harder AI, NVG advantage |

**Aethelgard Lore (High-Level):**
- **Setting**: Post-conflict industrial zone, 20 years after "The Collapse"
- **Factions**: Military remnants, corporate scavengers, local militia
- **Conflict**: Resource scarcity, territorial disputes, tech salvage
- **Player Role**: Independent contractor (PMC) hired by factions
- **Mystery**: What caused The Collapse? (revealed through exploration)

**Environmental Details:**

**Industrial Zone (Launch Map):**
- Abandoned factories with active machinery (hazards)
- Makeshift refugee camps in warehouses
- Military checkpoints overgrown with vegetation
- Underground bunker system (tight CQB)
- Rooftop sniper nests (long sightlines)

**Audio Atmosphere:**
- Distant gunfire (other players)
- Wind through broken windows
- Machinery grinding intermittently
- Footsteps echo in metal structures
- Wildlife sounds (crows, rats) for ambiance

**Visual Language:**
- **Red Lighting**: Danger, high loot, AI presence
- **Flickering Lights**: Unstable area, ambush potential
- **Green Fog**: Chemical hazard, reduced visibility
- **Blue Glow**: Extraction point proximity
- **Yellow Sparks**: Interactive objects (doors, crates)

**Design Guidelines:**
- ✅ Every prop has a reason to exist (no random clutter)
- ✅ Loot placement tells a story (who was here? why?)
- ✅ Environmental hazards are telegraphed visually
- ✅ Sound design matches materials (metal, concrete, wood)
- ❌ No symmetrical "esports" arenas (breaks immersion)
- ❌ No nonsense loot (high-tech in primitive contexts)
- ❌ No floating quest markers (use environment instead)

**Player Testimonial Goal:**  
*"I spent 10 minutes just exploring, finding hidden stories. This world feels REAL."* - Target Player Review

**Metrics:**
- Exploration time before first combat: >3 minutes (curiosity)
- Environmental detail appreciation: >60% (survey)
- Lore engagement (reading notes, etc.): >40%
- Map knowledge retention: >70% after 10 raids

---

### 4️⃣ Task-Driven Agency (Meaningful Choices)

**Mantra:** *"Choose your Wager, Define your Goal."*

**Philosophy:**  
Players should never be "just wandering." Every action is driven by a quest, a resource need, or a tactical choice. Meaningful agency means the player's decisions (greed vs. safety, aggression vs. stealth) result in **direct emotional consequences**. The game respects player choice.

**Decision Frameworks:**

**Pre-Raid Planning:**

| Decision | Options | Consequences | Emotional Weight |
|:---------|:--------|:-------------|:----------------|
| **Loadout Choice** | Budget (cheap gear) / Standard / Chad (expensive) | Economic risk vs combat power | Fear of loss vs confidence |
| **Quest Selection** | Main (story), Daily (grind), Faction (reputation) | Objective focus, loot priority | Achievement vs reward |
| **Solo vs Squad** | Solo (stealthy), Duo (balanced), Squad (loud) | Tactics, loot split, coordination | Independence vs safety |
| **Operator Choice** | Assault, Scout, Support, Medic, Engineer | Playstyle, team composition | Identity, mastery |
| **Time of Day** | Day (easier), Night (harder but more loot) | Risk/reward balance | Confidence vs greed |

**In-Raid Decisions:**

| Situation | Options | Immediate Result | Long-Term Impact |
|:----------|:--------|:----------------|:-----------------|
| **Enemy Encounter** | Fight / Flee / Sneak / Parley (VOIP) | Combat outcome, loot, XP | Reputation, skill growth |
| **Loot Container** | Search (time) / Ignore (speed) / Trap Check (safety) | Inventory fill, time loss | Gear progression |
| **Extract Choice** | Safe (far) / Risky (close) / Vehicle (expensive) | Extract success, time saved | Economic efficiency |
| **Wounded Ally** | Revive (risky) / Loot (greedy) / Leave (safe) | Squad morale, loot value | Social reputation |
| **Hot Zone** | Enter (risk) / Avoid (safety) / Observe (intel) | High reward vs death | Wealth accumulation |

**Quest System Design:**

**Main Quests (Story-Driven):**
- 5-10 hours of narrative content
- Unlock new zones and operators
- Cannot be failed, but can be delayed
- Provide lore and world context
- **Example**: *"Investigate the Reactor Meltdown Site"*

**Daily Quests (Engagement Loop):**
- Refresh every 24 hours
- Quick 10-15 minute objectives
- Provide steady income and XP
- Encourage diverse playstyles
- **Example**: *"Extract with 5 Medkits"*, *"Kill 3 enemies with headshots"*

**Faction Quests (Reputation Grind):**
- Multiple tiers per faction (Friendly, Honored, Exalted)
- Unlock faction-specific gear and traders
- Often conflict with other factions (choice!)
- High difficulty, high reward
- **Example**: *"Mark 3 enemy supply drops for airstrike"*

**Dynamic Objectives (Emergent):**
- Spawn mid-raid based on world events
- Optional but highly rewarding
- Create PvP hotspots
- Announced globally (risk/reward transparency)
- **Example**: *"Supply drop inbound in 5 minutes at Factory Roof"*

**Design Guidelines:**
- ✅ Every quest must have a meaningful choice
- ✅ Objectives should encourage map exploration
- ✅ Failure is okay (no mandatory success)
- ✅ Rewards scale with difficulty and risk
- ❌ No mandatory linear paths (player freedom)
- ❌ No fetch quests without context (boring)
- ❌ No "collect 50 items" grinds (respect time)

**Player Testimonial Goal:**  
*"Every raid feels different. I'm always working toward something, but I choose HOW."* - Target Player Review

**Metrics:**
- Quest completion rate: >70% (main), >50% (daily), >30% (faction)
- Player-reported "felt like I had a purpose": >80%
- Choice regret moments (good sign of weight): >2 per raid
- Loadout variance: >60% (players experiment)

---

### 5️⃣ Persistent Progression (Account & World Growth)

**Mantra:** *"Lose the Raid, Build the War."*

**Philosophy:**  
While individual raids carry the risk of loss, the **account's power and influence grow persistently**. Your actions today improve your capabilities tomorrow through the Hideout, Traders, and Reputation. Even failure teaches lessons (XP, unlocks). This creates the "one more raid" loop.

**Progression Layers:**

| Layer | Persistence | Reset Conditions | Player Value |
|:------|:-----------|:----------------|:------------|
| **Stash (Inventory)** | Permanent | Death (lost gear), Extract (saved gear) | Economic wealth, gear variety |
| **Account Level** | Permanent | Never (seasonal soft reset) | Skill unlocks, prestige |
| **Hideout Upgrades** | Permanent | Never | Passive bonuses, crafting |
| **Trader Reputation** | Permanent | Rare (faction betrayal) | Gear availability, discounts |
| **Operator Mastery** | Permanent | Never | Combat effectiveness, specialization |
| **Weapon Proficiency** | Permanent | Never | Recoil reduction, reload speed |
| **Map Knowledge** | Player Memory | Never (brain-based!) | Tactical advantage, loot efficiency |
| **Season Pass** | Seasonal | Every 3 months | Cosmetics, exclusive loot |

**Hideout System (Meta-Game Hub):**

**Purpose**: Persistent base that provides passive bonuses and crafting

**Modules:**

| Module | Level 1 | Level 2 | Level 3 | Cost Scaling |
|:-------|:--------|:--------|:--------|:-------------|
| **Stash** | 10×28 grid | 10×38 grid | 10×48 grid | 2M → 5M → 10M |
| **Medstation** | +10% heal speed | +20%, craft bandages | +30%, craft surgery kits | 500K → 1.5M → 3M |
| **Workshop** | Repair weapons | Modify weapons | Craft attachments | 750K → 2M → 4M |
| **Intelligence** | Trader rep +5% | Quest XP +10% | Unlock rare quests | 1M → 3M → 6M |
| **Generator** | Powers all modules | Reduced fuel cost | Solar backup (free) | 300K → 1M → 2.5M |
| **Shooting Range** | Practice recoil | Unlock weapon challenges | Gain proficiency XP | Free → 500K → 1.5M |

**Trader Reputation System:**

**Tiers:**
- **Neutral** (0-1000 rep): Basic gear available
- **Friendly** (1001-3000): Discounts 10%, mid-tier gear
- **Honored** (3001-6000): Discounts 20%, high-tier gear
- **Exalted** (6001+): Discounts 30%, exclusive gear, special quests

**Reputation Gain:**
- Complete faction quests: +50-200 rep
- Extract with faction items: +10-30 rep
- Kill faction enemies: +5-15 rep
- Betray faction: -500 rep (severe penalty)

**Reputation Loss:**
- Kill faction members: -50 rep
- Fail faction quests: -20 rep
- Trade with rival factions: -10 rep

**Operator Mastery:**

**Per-Operator Stats:**
- **Level**: 1-50 (XP from raids while playing operator)
- **Passive Bonus**: +1% to operator specialty per 5 levels
- **Unlocks**: New skins, voice lines, signature weapons

**Examples:**
- **Assault Operator (Viper)**: +10% sprint speed at Lvl 50
- **Scout Operator (Hawk)**: +20% ADS speed at Lvl 50
- **Medic Operator (Cross)**: +30% heal speed at Lvl 50

**Weapon Proficiency System:**

**How It Works:**
- Every weapon family has a proficiency level (1-20)
- Gain XP by: Kills, Headshots, Successful Raids with weapon
- Each level provides +2% recoil reduction, +1% reload speed

**Weapon Families:**
- Assault Rifles (AK, M4, SCAR)
- SMGs (MP5, UMP, Vector)
- Sniper Rifles (SVD, M700, AWM)
- Shotguns (Saiga, M870, AA-12)
- Pistols (Glock, 1911, Deagle)

**Seasonal Content:**

**Season Structure** (3 months per season):
- New Battle Pass (100 tiers)
- Seasonal quest line (5-8 hours)
- Limited-time event (week 6-8)
- Meta shake-up (weapon balance, map changes)
- Soft reset (rank reset, leaderboards)

**What DOESN'T Reset:**
- Hideout levels
- Trader reputation
- Operator mastery
- Weapon proficiency
- Stash items (partial reset option for hardcore players)

**Design Guidelines:**
- ✅ Always reward time invested (even failed raids)
- ✅ Permanent unlocks feel meaningful
- ✅ Short-term loss (gear) balanced by long-term gain (XP)
- ✅ Multiple progression paths (choose focus)
- ❌ No total account wipes (outside seasonal opt-in)
- ❌ No pay-to-skip progression (monetization boundary)
- ❌ No mandatory daily login rewards (respects player time)

**Player Testimonial Goal:**  
*"I lost my best gear today, but I unlocked Level 2 Hideout and got closer to Honored with the Militia. Still feels like progress."* - Target Player Review

**Metrics:**
- Average account level after 1 month: 25-30
- Hideout module upgrade rate: >2 per week
- Operator mastery diversity: >3 operators at Lvl 10+
- Player-reported "feels rewarding even when losing": >65%
- Retention (30-day): >50% (strong progression hook)

---

## ⚖️ Pillar Conflict Resolution Framework

When core pillars contradict each other, use this **hierarchy** to decide:

### Decision Tree

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

### Real-World Examples

**Example 1: Healing While Shooting**

**Conflict**: Tactical Fluidity (accessibility) vs High-Stakes Tension (vulnerability)

**Pillar Analysis:**
- Fluidity says: *Allow healing while shooting (mobile-friendly)*
- Tension says: *Healing must create vulnerability (risk)*

**Resolution**: **Tension wins** (Priority 1)
- **Decision**: Healing stops weapon use, slows movement 50%
- **Rationale**: Creates tactical choice (cover first, then heal)
- **Compensation**: Fast heal items (3 seconds) for accessibility

---

**Example 2: UI Quest Markers**

**Conflict**: Environmental Narrative (immersion) vs Task-Driven Agency (clarity)

**Pillar Analysis:**
- Narrative says: *No floating markers (breaks immersion)*
- Agency says: *Players need clear objectives (accessibility)*

**Resolution**: **Hybrid approach** (Both matter)
- **Decision**: Compass markers only (not in-world floaters)
- **Enhancement**: Environmental clues (smoke, lights) guide players
- **Accessibility**: Toggle "hint mode" for new players (first 10 raids)

---

**Example 3: Weapon Realism**

**Conflict**: Tactical Fluidity (responsive controls) vs Environmental Narrative (realism)

**Pillar Analysis:**
- Fluidity says: *Instant weapon swap (responsive)*
- Narrative says: *Realistic swap speed (heavy weapons slow)*

**Resolution**: **Fluidity wins** (Priority 2)
- **Decision**: Weapons swap faster than real life (2s → 1s)
- **Rationale**: Simulation fidelity matters for ballistics, not animations
- **Compromise**: Different weapon classes have variance (pistol 0.5s, LMG 1.5s)

---

**Example 4: Account Wipes**

**Conflict**: High-Stakes Tension (reset for freshness) vs Persistent Progression (respect time)

**Pillar Analysis:**
- Tension says: *Seasonal wipes keep economy fresh*
- Progression says: *Players hate losing months of work*

**Resolution**: **Progression wins** (Priority 5)
- **Decision**: Opt-in wipes only (hardcore mode)
- **Compromise**: Seasonal soft resets (ranks, leaderboards, not hideout)
- **Reward**: Exclusive cosmetics for wipe participants

---

## 🎯 Player Experience Goals (Emotional Targets)

### Target Emotions Per Raid Phase

| Phase | Duration | Target Emotion | Mechanic Driver |
|:------|:---------|:---------------|:----------------|
| **Pre-Raid Planning** | 2-3 min | Anticipation, Strategy | Loadout choice, quest selection |
| **Spawn & Early Loot** | 3-5 min | Curiosity, Greed | Exploration, container opening |
| **First Contact** | Variable | Fear, Adrenaline | Gunfight, sound cues |
| **Mid-Raid Looting** | 5-10 min | Tension, Decision Fatigue | Bag filling, Tetris puzzle |
| **Extract Decision** | 1-2 min | Paranoia, Calculation | Route choice, risk assessment |
| **Extraction Attempt** | 2-3 min | Peak Tension, Relief (if success) | Extract camping threat |
| **Post-Raid** | 2-3 min | Satisfaction / Disappointment | Loot sorting, progression gains |

### Emotional Spectrum Balance

```
Low Tension ←―――――――――――→ High Tension
         ↓
    [Sweet Spot]
    (70% of raids)
```

**Goal Distribution:**
- 10% raids: Low tension (easy wins, learning)
- 70% raids: Medium-high tension (close calls, sweaty palms)
- 20% raids: Extreme tension (near-death, massive loot)

**Metrics to Track:**
- Player-reported "heart racing" moments: >3 per raid
- Ragequit rate after death: <15% (frustration tolerable)
- Extract satisfaction: >8/10 (when successful)
- "One more raid" intent: >60% (addictive loop)

---

## 🔄 The Core Loops (Macro & Micro)

### Macro Loop (Long-Term Growth)

**30-Day Player Journey:**

```
Week 1: LEARN
- Tutorial completion
- First 10 raids (high death rate okay)
- Unlock 2-3 operators
- Basic loadout economy established

Week 2: OPTIMIZE
- Favorite weapon identified
- Main quests progressing
- First Hideout upgrade
- Map knowledge improving

Week 3: MASTER
- Extract rate 60%+
- Trader Friendly reached
- Operator mastery Lvl 10+
- Meta loadouts tested

Week 4: ENDGAME
- High-tier raids
- Faction quest grinding
- Hideout Level 2+
- Seasonal event participation
```

**Detailed Macro Loop:**

1. **PREPARE** (2-3 minutes):
   - Assess economic situation (can I afford to lose this loadout?)
   - Build loadout based on quest objectives
   - Accept faction tasks aligned with playstyle
   - Select operator and time of day
   - Mental prep (where will I land? what's my route?)

2. **RAID** (15-20 minutes):
   - Spawn → Orient → Move to objective
   - Loot containers en route (opportunity cost)
   - Complete quests (primary goal)
   - Engage/avoid enemies (tactical choice)
   - Fill inventory (greed vs mobility)
   - Monitor time (extract urgency)

3. **EXTRACT** (2-3 minutes):
   - Choose extract point (risk calculation)
   - Final loot decisions (discard low-value)
   - Navigate to extract under pressure
   - Survive extract timer (15 seconds vulnerable)
   - Breath held until "Extracted" screen

4. **PROGRESS** (2-3 minutes):
   - Sell loot to traders (economy management)
   - Repair damaged gear (durability system)
   - Upgrade Hideout (long-term investment)
   - Increase Trader Reputation (quest turn-ins)
   - Check progression stats (dopamine hit)
   - Plan next raid (loop restart)

**Loop Timing:**
- Full cycle: 22-31 minutes per raid
- Ideal session: 3-4 raids (1-2 hours)
- Hardcore session: 6-8 raids (3-4 hours)

---

### Micro Loop (Immediate Tension)

**OODA Loop (Military Decision-Making):**

```
OBSERVE → ORIENT → DECIDE → ACT → ADAPT
   ↑                                    ↓
   └────────────────────────────────────┘
           (Continuous Loop)
```

**Detailed Breakdown:**

1. **OBSERVE** (0.5-2 seconds):
   - **Sound Cues**: Footsteps, gunshots, door opens, mag check
   - **Visual Glints**: Scope reflections, muzzle flash, movement
   - **Environmental Traces**: Blood trails, open containers, corpses
   - **Intel**: Map pings (squad), quest markers, extract timers

2. **ORIENT** (1-3 seconds):
   - **Threat Assessment**: How many enemies? What gear?
   - **Cover Check**: Nearest hard cover, concealment, escape routes
   - **Objective Check**: Quest priority, loot value, time remaining
   - **Resource Check**: Ammo count, med availability, stamina

3. **DECIDE** (0.5-1 second):
   - **Fight**: Engage if advantageous (better position, gear, surprise)
   - **Flight**: Retreat if outmatched (low HP, outnumbered, bad position)
   - **Sneak**: Avoid if unnecessary (quest focus, resource conservation)
   - **Parley**: Communicate via VOIP (rare, high-risk trust scenario)

4. **ACT** (1-5 seconds):
   - **Execute Tactical Maneuver**: Flank, suppress, advance, retreat
   - **Weapon Handling**: Aim, fire, reload, swap, mag check
   - **Consumable Use**: Heal, painkiller, grenade, utility
   - **Movement**: Sprint, slide, prone, vault, door breach

5. **ADAPT** (0.5-1 second):
   - **Review Results**: Hit/miss, enemy down, took damage, position revealed
   - **Adjust Plan**: New cover, different angle, weapon swap, retreat
   - **Reset Loop**: Back to OBSERVE with updated information
   - **Mental Note**: Learn enemy behavior, weapon effectiveness

**Micro Loop Timing:**
- Full cycle: 3-12 seconds per engagement
- Fastest (instinct): 3-5 seconds (close range, high skill)
- Tactical (methodical): 8-12 seconds (long range, team coordination)

**Decision Speed Hierarchy:**

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
- ✅ Information should be actionable (sound = direction)
- ✅ Decisions should have clear consequences (fight = risk)
- ✅ Actions should feel responsive (instant input)
- ✅ Adaptation should be rewarded (learning AI behavior)
- ❌ No information overload (too many UI elements)
- ❌ No forced waiting (animation locks during combat)
- ❌ No unclear threats (enemy visibility must be fair)

---

## 🎮 Game Feel Goals (Sensory Experience)

### "Crunchy" Combat (Weighty Impact)

**Audio Design:**

| Element | Implementation | Player Perception |
|:--------|:---------------|:------------------|
| **Gunshots** | Bass-heavy, reverb based on environment (indoor/outdoor) | Powerful, real |
| **Impacts** | Material-based sounds (metal, wood, flesh) | Satisfying hits |
| **Explosions** | Tinnitus effect (ringing), screen shake, audio compression | Disorienting danger |
| **Footsteps** | Surface-specific (metal clang, wood creak, dirt crunch) | Tactical intel |
| **Ambient** | Environmental layers (wind, machinery, distant combat) | Living world |

**Visual Design:**

| Effect | Trigger | Duration | Purpose |
|:-------|:--------|:---------|:--------|
| **Debris** | Bullet impacts, explosions | 2-5 seconds | Convey power |
| **Sparks** | Metal surfaces hit | 0.5-1 second | Visual feedback |
| **Blood** | Flesh hits | Persistent (decals) | Confirm damage |
| **Muzzle Flash** | Weapon fire | 1 frame | Reveal position |
| **Screen Shake** | Taking damage, explosions | 0.2-0.5 seconds | Visceral feedback |
| **Lens Effects** | Scope glint, NVG blur | Persistent | Realism, balance |

**Haptic Feedback (Mobile):**

| Event | Vibration Pattern | Intensity |
|:------|:------------------|:----------|
| **Weapon Fire** | Short burst (100ms), varies by weapon | Medium-High |
| **Taking Damage** | Long pulse (300ms), direction-based | High |
| **Footstep Near** | Subtle pulse (50ms), distance-based | Low |
| **Grenade Throw** | Tap (50ms) | Low |
| **Reload Complete** | Double tap (50ms + 50ms) | Low |
| **Enemy Killed** | Success pulse (200ms) | Medium |

**Input Feel:**

| System | Responsiveness | Precision | Mastery |
|:-------|:---------------|:----------|:--------|
| **Recoil** | Predictable patterns (learnable), no RNG spray | High | Muscle memory compensation |
| **Hit Stop** | 0.1s freeze on melee impact, headshot | High | Confirms kill |
| **Aim Assist** | Subtle magnetism (10% drag), tap-to-snap option | Medium | Accessibility without auto-aim |

---

### "Weighty" Movement (Grounded Feel)

**Inertia System:**

| Weight Tier | Acceleration Time | Deceleration Time | Turn Speed | Jump Height |
|:------------|:------------------|:------------------|:-----------|:------------|
| **Light (0-25kg)** | 0.1s | 0.1s | Instant | 100% |
| **Medium (25-40kg)** | 0.3s | 0.2s | 0.2s delay | 75% |
| **Heavy (40-55kg)** | 0.5s | 0.4s | 0.5s delay | 40% |
| **Critical (55kg+)** | 0.8s | 0.6s | 1.0s delay | 0% |

**Momentum Preservation:**

| Action | Momentum Carry | Speed Modifier | Duration |
|:-------|:---------------|:---------------|:---------|
| **Sprint → Slide** | 100% carry | +10% speed | 2 seconds |
| **Jump from Sprint** | 80% carry | -20% air control | Until land |
| **Vault Over Obstacle** | 60% carry | -30% during vault | 1 second |
| **Crouch While Moving** | 40% carry | -50% speed | Persistent |

**Camera & Animation:**

| System | Effect | Purpose | Intensity |
|:-------|:-------|:--------|:----------|
| **Head Bob** | Vertical sway synced to footsteps | Grounding, feedback | Subtle (5% screen height) |
| **Weapon Sway** | Breathing pattern, stamina affects intensity | Realism, skill gap | Medium (2% screen width) |
| **Landing Impact** | Screen dip, audio crunch, brief slowdown | Weight feedback | High (10% screen height, 0.3s) |
| **Sprint Tilt** | Slight forward lean, peripheral blur | Speed sensation | Subtle (3° tilt) |

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
- ✅ Movement should feel responsive but not floaty
- ✅ Weight should be palpable without being frustrating
- ✅ Momentum adds skill expression (slide-jumps, etc.)
- ✅ Camera effects enhance immersion without nausea
- ❌ No artificial "slow walk" animations (player controls speed)
- ❌ No exaggerated head bob (motion sickness concern)
- ❌ No permanent movement penalties (temporary stamina okay)

---

## ✅ Quality Assurance Checklist (Feature Gate)

Use this checklist for **every new feature request**. If a feature fails 3+ checks, it should be reconsidered or reworked.

### Pillar Validation

| # | Question | Pass Criteria | Red Flags |
|:--|:---------|:--------------|:----------|
| 1 | Does it increase **Tension** or **Tactical Depth**? | Adds meaningful risk/reward or tactical choice | Removes consequences, simplifies choices |
| 2 | Does it respect the **Flow (Fluidity)** of controls? | Feels responsive, doesn't lock inputs | Animation locks, artificial delays |
| 3 | Does it make sense in the **Context of Aethelgard**? | Logically fits world, enhances narrative | Breaks immersion, generic design |
| 4 | Does it provide the player with a **Meaningful Choice**? | Actual agency with consequences | Illusion of choice, mandatory actions |
| 5 | Does it contribute to **Persistent Progression**? | Rewards time invested, long-term value | Pure session-based, no account impact |

### Implementation Validation

| # | Question | Pass Criteria | Red Flags |
|:--|:---------|:--------------|:----------|
| 6 | Can it be built within scope/budget? | Realistic estimate, proven tech | Requires new engine features, unclear feasibility |
| 7 | Does it conflict with other systems? | Clean integration, no breaking changes | Requires major refactor, dependency hell |
| 8 | Is it testable and balanceable? | Clear metrics, tuning parameters | Black box behavior, no dials to adjust |
| 9 | Does it work on mobile hardware? | 60 FPS on mid-range devices | Performance concerns, battery drain |
| 10 | Is it monetization-safe? | No pay-to-win implications | Could be sold for competitive advantage |

### Player Experience Validation

| # | Question | Pass Criteria | Red Flags |
|:--|:---------|:--------------|:----------|
| 11 | Does it enhance fun without removing challenge? | Adds options, maintains skill ceiling | Removes difficulty entirely, hand-holding |
| 12 | Is it accessible to new players? | Clear tutorial, forgiving learning curve | Requires 10+ hours to understand |
| 13 | Does it add depth for veterans? | Mastery potential, optimization possibilities | Ceiling too low, "solved" immediately |
| 14 | Would it generate positive community sentiment? | Addresses pain points, adds requested features | Community backlash likely, controversial |
| 15 | Does it align with our market positioning? | Fits "tactical mobile extraction shooter" | Too casual, too hardcore, wrong genre |

### Decision Matrix

**Pass All 15 Checks:**
- ✅ Greenlight - Add to roadmap

**Pass 12-14 Checks:**
- 🟡 Conditional - Rework failing areas, re-evaluate

**Pass 9-11 Checks:**
- ⚠️ Reconsider - Likely not worth the effort

**Pass <9 Checks:**
- ❌ Reject - Does not align with core vision

---

## 📈 Metrics & Success Criteria

### Pillar-Specific KPIs

**1. High-Stakes Tension:**
- Extract success rate: 60-70% (balanced challenge)
- Player-reported "heart racing": >3 moments/raid
- Gear loss emotional impact: 7/10 (hurts but doesn't rage-quit)
- Extract camping encounters: 10-15% of extracts

**2. Tactical Fluidity:**
- Input latency: <80ms (p95)
- Control frustration: <10% of players
- First-time tutorial completion: >85%
- Movement mastery (advanced tech usage): >40% at 50 hours

**3. Environmental Narratives:**
- Exploration time before first combat: >3 minutes
- Lore engagement: >40% read environmental notes
- Map knowledge retention: >70% after 10 raids
- Player-reported "world feels real": >60%

**4. Task-Driven Agency:**
- Quest completion rate: >70% (main), >50% (daily)
- Loadout variance: >60% (experimentation)
- Regret moments: >2/raid (meaningful choices)
- "Felt purposeful": >80% of raids

**5. Persistent Progression:**
- 30-day retention: >50%
- Average account level at 1 month: 25-30
- Hideout upgrade frequency: >2/week
- "Rewarding even when losing": >65%

### Holistic Success Metrics

**Engagement:**
- DAU/MAU ratio: >0.3 (sticky game)
- Average session length: 1-2 hours
- Sessions per week: 8-12 (highly engaged)
- Lifetime value (LTV): >$30 (at 6 months)

**Sentiment:**
- App Store rating: >4.2 stars
- NPS (Net Promoter Score): >40
- Community toxicity: <15% (supportive playerbase)
- Creator/streamer adoption: >100 active streamers

**Competitive:**
- Market share (mobile extraction shooters): Top 3
- Retention vs competitors: +15% above average
- Revenue per user: Top quartile
- Critical reception: >80/100 Metacritic

---

## 📝 Document Ownership & Maintenance

### Ownership

| Role | Responsibility | Authority |
|:-----|:---------------|:----------|
| **Creative Director** | Pillar definition, vision alignment | Final say on pillar conflicts |
| **Lead Game Designer** | Pillar implementation, feature validation | Veto features that violate pillars |
| **Studio Head** | Budget, scope, timeline | Can delay/cut features, not change pillars |
| **Community Manager** | Player feedback integration | Advocate for player sentiment in pillar reviews |

### Review Cadence

**Monthly Validation:**
- Playtest sessions against pillar goals
- Metrics review (are we hitting targets?)
- Feature gate audit (any exceptions granted? why?)
- Team survey (do pillars still resonate?)

**Quarterly Deep Review:**
- External playtest with target audience
- Competitor analysis (how are we positioning?)
- Pivot assessment (do pillars need refinement?)
- Stakeholder alignment (exec, investors, partners)

**Major Update:**
- Version number bump (v2.0, v3.0, etc.)
- Full changelog with rationale
- Team-wide review and sign-off
- Public communication (if appropriate)

### Change Control

**How to Propose a Pillar Change:**

1. **Submit RFC (Request for Comment)**:
   - Document: Why change? What's broken? What's the fix?
   - Evidence: Metrics, player feedback, competitive pressure
   - Impact: What systems would need to change?

2. **Leadership Review**:
   - Creative Director + Lead Designer + Studio Head
   - Decision within 2 weeks

3. **Team Discussion**:
   - If approved, full team workshop
   - Address concerns, refine language
   - Build consensus (not unanimity, but buy-in)

4. **Implementation**:
   - Update this document
   - Cascade changes to all dependent docs
   - Communicate to team and community (if public)

**When to Change Pillars:**
- ❌ NEVER: Based on one bad playtest
- ❌ RARELY: Due to market trends (we lead, not follow)
- ✅ SOMETIMES: When persistent data shows fundamental flaw
- ✅ DEFINITELY: If core vision shifts (rare, existential)

---

## 🔗 Related Documents

**Core GDD Suite:**
- [Project Scope & Vision](project-scope-enhanced.md) - High-level game definition
- [MVP Scope](mvp-enhanced.md) - What we're building first
- [Non-Goals](non-goals-enhanced.md) - What we're explicitly NOT doing
- [Inventory & Gear Systems](inventory-gear-systems-enhanced.md) - Deep dive on loot mechanics

**Implementation Guides:**
- [Competitive Analysis](competitive-analysis-extraction-shooters.md) - Market positioning

**Player-Facing:**
- Game Trailer (Hook: "Fear of Loss, Thrill of Gain")
- Tutorial Design (Teach pillars through play)
- Community Guidelines (Toxicity = violation of "Task-Driven Agency" pillar)

---

## 📚 Changelog

| Version | Date | Author | Changes |
|:--------|:-----|:-------|:--------|
| **v1.0** | 2026-02-07 | Creative Director | Initial philosophy definition |
| **v1.1** | 2026-02-09 | Lead Designer | Added Genre Pillars from industry research |
| **v1.2** | 2026-02-09 | Creative Director | Unified to Five Core Pillars, standardized Aethelgard |
| **v2.0** | 2026-02-11 | Claude AI (Consultant) | **MAJOR UPDATE**: Enhanced with 2024-2026 best practices, detailed metrics, conflict resolution framework, player experience goals, quality checklist, and comprehensive examples. Researched modern GDD standards and extraction shooter genre analysis. |

---

**END OF DOCUMENT**

*"These pillars are not suggestions. They are the laws by which we build this world."* - Creative Director

---

**Next Steps for Implementation:**
1. Share with full team for feedback (1 week review period)
2. Conduct pillar validation workshop (all hands, 4 hours)
3. Update all feature requests in backlog against new checklist
4. Create pillar-based onboarding for new team members
5. Quarterly review scheduled (May 11, 2026)
