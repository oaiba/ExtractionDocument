---
title: "Quest System & Quest Lines"
type: docs
weight: 4
---

## Quest System Overview

### Quest Philosophy

Quests serve three simultaneous purposes:

1. **Motivation**: Give players a reason to enter dangerous zones beyond pure loot
2. **Narrative Vehicle**: Deliver story content through objectives, not cutscenes
3. **Progression Gate**: Structure the player's journey from newcomer to veteran

### Integration with Extraction Loop

Quests are completed **during raids**, not in menus. Every objective requires entering the Exclusion Zone.

```
ACCEPT QUEST (Safe Zone)
     |
ENTER RAID with quest objective
     |
COMPLETE OBJECTIVE (discover, kill, retrieve, deliver)
     |
SURVIVE AND EXTRACT with relevant items
     |
RETURN TO NPC to claim reward
```

**Critical design rule**: A failed extraction means quest items are lost. Quest progress for "discover" and "kill" objectives is retained if the objective was completed before death.

---

## Quest Categories

| Category | Source | Availability | Purpose | Example |
| :------- | :----- | :------------ | :------ | :------ |
| **Main Story** | Game system | Sequential unlock (level-gated) | Core narrative progression | "Enter Lab Alpha and retrieve Dr. Chen's research files" |
| **Faction Quests** | Faction NPCs | After reaching faction rep thresholds | Faction reputation, unique rewards, faction lore | "Deliver supply crates to 3 Salvage outposts in Sector 7" |
| **Daily Quests** | Rotating board | 24-hour cycle, 3 per day | Daily engagement, basic rewards | "Extract with 3 weapon modifications" |
| **Weekly Quests** | Rotating board | 7-day cycle, 2 per week | Larger engagement goals, significant rewards | "Successfully extract 10 times this week" |
| **Challenge Quests** | Achievement system | Permanently available, one-time completion | Mastery rewards, cosmetics, bragging rights | "Kill a boss using only a pistol" |
| **Hidden Quests** | Environmental triggers | Triggered by finding specific items/locations | Deep lore, unique rewards, player discovery | "Finding all 5 of Dr. Chen's audio logs unlocks a hidden quest" |

---

## Main Story Quest Line

### Overview

The main story unfolds across 5 chapters, each gated by player level and previous chapter completion:

```
Chapter 1: "New Arrival" (Lv. 1-10)
  ↓
Chapter 2: "Deeper Roots" (Lv. 10-20)
  ↓
Chapter 3: "Unburied Secrets" (Lv. 20-30)
  ↓
Chapter 4: "The Broker's Game" (Lv. 30-40)
  ↓
Chapter 5: "Endgame" (Lv. 40+)
```

### Quest Dependency Graph

<!-- REF_IMAGE: Quest dependency flowchart — showing Chapter 1-5 main story quests as nodes with prerequisite arrows, branching decisions marked with diamond shapes, and side-quest entry points -->

---

### Chapter 1: New Arrival (Season 1)

**Narrative Arc**: Player arrives in the Exclusion Zone as a new Contractor. Learn the basics, meet the factions, discover that something deeper is wrong.

| Quest | Objective | NPC | Reward | Unlocks |
| :---- | :-------- | :-- | :----- | :------ |
| 1.1 "First Steps" | Extract from your first raid with any loot | Tutorial NPC | Starter gear pack | Quest 1.2, faction vendor access |
| 1.2 "Meet the Bosses" | Visit all 4 faction NPCs in the Safe Zone | Tutorial NPC | 500 credits, faction quest access | Quest 1.3, all faction quest lines |
| 1.3 "Supply Run" | Retrieve 3 food rations from Warehouse District | Viktor Koval | Salvage Corps rep +500, Worker's Backpack | Quest 1.4 |
| 1.4 "The Signal" | Find the source of a mysterious radio broadcast in District 14 | Quest board | 1,000 credits, experience | Quest 1.5 |
| 1.5 "Lab Rat" | Enter Lab Alpha and recover any research document | The Broker (voice) | 2,000 credits, Prometheus Codex Entry #1 | Chapter 2 |

**Decision Point at 1.5**: The Broker offers to buy the research document. Viktor also wants it. **Player chooses** who to give it to, affecting early reputation with both.

---

### Chapter 2: Deeper Roots (Season 1)

**Narrative Arc**: The factions are more complex than they seemed. Project Prometheus details emerge. Something in the labs is still active.

| Quest | Objective | NPC | Reward | Unlocks |
| :---- | :-------- | :-- | :----- | :------ |
| 2.1 "The Foreman's Favor" | Complete 3 Salvage Corps faction quests | Viktor Koval | Rep +1,000, unique weapon mod | Quest 2.2 |
| 2.2 "Data Recovery" | Hack 2 terminals in Tech Labs to download Prometheus files | Seo-Yun Park | Tech Syndicate rep +1,000, Codex entries | Quest 2.3 |
| 2.3 "Underground Currents" | Complete a dead-drop delivery for the Underground Network | Rat King | Underground rep +1,000, Smuggler's Map | Quest 2.4 |
| 2.4 "Order of Operations" | Escort a Peacekeeper patrol through a contested zone | Captain Reyes | Peacekeeper rep +1,000, Tactical Vest access | Quest 2.5 |
| 2.5 "The Subject" | Enter the Reactor Tower and discover Subject 7's containment cell | The Broker (voice) | 5,000 credits, Prometheus Codex Entry #2-5, Chapter 3 access | Chapter 3 (Season 2) |

**Decision Point at 2.5**: Evidence found in the cell implicates Director Park. Player can:
- **Tell the Peacekeepers** → +2,000 Peacekeeper rep, -1,000 Tech rep, Park sends angry encrypted message
- **Confront Park directly** → +2,000 Tech rep, Park reveals partial truth about Prometheus (exclusive dialogue)
- **Tell no one** → +1,000 Underground rep, The Broker is pleased with player's discretion

---

### Chapter 3: Unburied Secrets (Season 2)

**Narrative Arc**: The truth about The Collapse surfaces. Faction alliances shift. Director Park's past catches up with her.

| Quest | Objective | NPC | Reward | Unlocks |
| :---- | :-------- | :-- | :----- | :------ |
| 3.1 "The Server Farm" | Discover the contested server farm (new POI) | Automated signal | Prometheus Codex Entry #6-8 | Quest 3.2 |
| 3.2 "Pick a Side" | Complete 2 quests for either Salvage OR Tech during the Resource War event | Viktor or Park | Faction-specific weapon, +2,000 rep with chosen side | Quest 3.3 |
| 3.3 "The CFO's Legacy" | Find James Thompson's financial records in Office Complex | The Broker | 8,000 credits, Nexus Corp Codex entries | Quest 3.4 |
| 3.4 "The Scientist" | Defeat the boss in Tech Labs. Recover Dr. Chen's final recording | Game system | Legendary weapon, major lore reveal | Quest 3.5 |
| 3.5 "Prometheus Unbound" | Present all evidence to a faction leader of your choice | Player choice | Chapter 4 access, major reputation shift based on choice | Chapter 4 (Season 3) |

**Decision Point at 3.5**: Who receives the full truth about Project Prometheus?
- **Viktor Koval** → Salvage Corps becomes the moral authority. Peacekeepers lose influence
- **Commander Vance** → Peacekeepers launch an investigation. Tech Syndicate becomes hostile
- **The Broker** → Information leaked to all factions simultaneously. Chaos, but maximum transparency

---

### Chapter 4: The Broker's Game (Season 3)

**Narrative Arc**: Who is The Broker? What do they really want? Firebase Delta opens — the military knew everything.

| Quest | Objective | NPC | Reward | Unlocks |
| :---- | :-------- | :-- | :----- | :------ |
| 4.1 "Firebase" | Gain access to Firebase Delta (new map) | Commander Vance | Exclusive access, military loot | Quest 4.2 |
| 4.2 "The Nuclear Option" | Find the recording of the nuclear fail-safe debate | General Li Wei's terminal | Codex Entry: "The Last Resort" | Quest 4.3 |
| 4.3 "The Broker Speaks" | Answer The Broker's encrypted summons (first direct meeting?) | The Broker | Major lore dump, first identity hints | Quest 4.4 |
| 4.4 "Clean House" | Eliminate a rogue Nexus AI defense system in Firebase Delta | Game system | Prototype weapon, keycard access | Quest 4.5 |
| 4.5 "The Truth" | Decision quest — what to do with everything you've learned | Player choice | Chapter 5 access, world state changes | Chapter 5 (Year 2) |

---

### Chapter 5: Endgame (Year 2+)

**Narrative Arc**: Player agency reaches its peak. Community-driven narrative events. The Broker's identity resolved. Cure possibility explored.

- Detailed quest design will follow Year 2 planning
- Chapter 5 is designed as an evolving, seasonal quest line rather than a fixed set
- Community vote events will influence major story decisions
- Multiple endings possible based on cumulative player choices across Chapters 1-4

---

## Faction Quest Lines

### Quest Structure Per Faction

Each faction has 5 tiers of quests corresponding to reputation levels:

```
Tier 1 (Rep 1-2): Introduction
  3-5 simple quests establishing faction identity
    ↓
Tier 2 (Rep 2-3): Trust Building
  5-7 quests of increasing difficulty
    ↓
Tier 3 (Rep 3-4): Faction Storyline
  5-7 narrative-heavy quests revealing faction secrets
    ↓
Tier 4 (Rep 4-5): Inner Circle
  3-5 high-difficulty quests with major lore payoffs
    ↓
Tier 5 (Rep 5): Legendary
  1-2 ultimate quests with unique legendary rewards
```

### Salvage Corps Quest Progression

| Tier | Quest Name | Objective | Mechanic Focus |
| :--: | :--------- | :-------- | :------------- |
| 1 | "Spare Parts" | Collect 5 mechanical components from Sector 7 | Looting |
| 1 | "Pest Control" | Eliminate 10 scavengers near the workshops | Combat (easy) |
| 1 | "Power Up" | Restore power to a Salvage relay station | Interact |
| 2 | "Heavy Lifting" | Extract with 30kg of materials in a single raid | Weight management |
| 2 | "Yuri's Prototype" | Find specific rare components for Yuri's project | Targeted looting |
| 2 | "Supply Line" | Deliver supplies to 3 Salvage outposts in one raid | Navigation, survival |
| 3 | "The Forge" | Discover a hidden Nexus workshop in Sector 7 | Exploration |
| 3 | "Mama Rosa's Secret" | Help Rosa establish a supply route to orphan camp | Escort, stealth option |
| 4 | "Foreman's Trust" | Investigate the Nexus systems beneath the factory | Major lore quest |
| 5 | "Builder's Legacy" | Restore a critical piece of infrastructure | Multi-session legendary |

### Tech Syndicate Quest Progression

| Tier | Quest Name | Objective | Mechanic Focus |
| :--: | :--------- | :-------- | :------------- |
| 1 | "Signal Strength" | Place 3 signal boosters in Sector 7 | Placement objectives |
| 1 | "Data Mine" | Retrieve USB drives from 5 locations | Collection |
| 1 | "Ghost Protocol" | Complete a raid without being detected by any AI | Stealth |
| 2 | "Zero's Test" | Hack a secure terminal in under 90 seconds | Timed puzzle |
| 2 | "The Archive" | Photograph 5 Nexus documents without removing them | Stealth, non-lethal |
| 2 | "Countermeasures" | Disable 3 automated defense systems | Technical combat |
| 3 | "Director's Past" | Discover evidence of Park's role in Prometheus | Exploration, major lore |
| 3 | "Glitch's Ghosts" | Help Glitch confront a location from her past | Narrative, dialogue |
| 4 | "The Core" | Access the central Nexus data server | Multi-stage heist |
| 5 | "Prometheus Redux" | Decision: destroy or preserve the Prometheus data | World-state changing |

### Underground Network Quest Progression

| Tier | Quest Name | Objective | Mechanic Focus |
| :--: | :--------- | :-------- | :------------- |
| 1 | "Dead Drop" | Deliver a package to a marked location | Navigation |
| 1 | "Fence" | Sell 10 items through the Underground market | Economy |
| 1 | "Lookout" | Observe a Peacekeeper patrol route and report | Stealth, recon |
| 2 | "Rat Run" | Complete a delivery through the sewer network | Navigation, hazards |
| 2 | "Insurance Job" | Plant evidence to frame a rival trader | Moral gray area |
| 2 | "Big Bear's Burden" | Assist Big Bear in "convincing" a debtor | Intimidation, combat |
| 3 | "Madame X's List" | Eliminate 3 high-value targets | Combat, assassination |
| 3 | "Network Node" | Establish a new underground safehouse | Construction, defense |
| 4 | "Broker's Call" | First direct Broker communication. Complete a multi-objective heist | Multi-stage, high difficulty |
| 5 | "Shadow King" | Either replace The Broker or secure their position forever | World-state changing |

### Peacekeeper Quest Progression

| Tier | Quest Name | Objective | Mechanic Focus |
| :--: | :--------- | :-------- | :------------- |
| 1 | "Patrol Duty" | Clear 3 zones of hostile activity | Combat |
| 1 | "Field Medic" | Heal 5 NPC casualties | Medical system |
| 1 | "Checkpoint" | Establish a temporary checkpoint at a designated location | Defense |
| 2 | "Stone's Challenge" | Eliminate a mini-boss without using healing items | Skill check |
| 2 | "Dr. Wells' Request" | Retrieve medical supplies from a contaminated zone | Hazard navigation |
| 2 | "Rules of Engagement" | Complete a raid without killing non-combatant NPCs | Restraint |
| 3 | "The Informant" | Extract an Underground informant from a hostile area | Escort, stealth |
| 3 | "Vance's Regret" | Investigate a location tied to Vance's past | Major lore quest |
| 4 | "Firebase Recon" | Scout Firebase Delta for the Commander | High-difficulty recon |
| 5 | "Justice Undone" | Confront evidence of Vance's "necessary evils" — report or protect her | World-state changing |

---

## Daily and Weekly Quests

### Daily Quest Pool (3 per day, random selection)

| Category | Examples |
| :------- | :------- |
| **Extraction** | "Extract 2 times" / "Extract from [specific zone]" |
| **Combat** | "Kill 15 enemies" / "Get 3 headshot kills" |
| **Looting** | "Extract with items worth 5,000 credits" / "Find 3 medical supplies" |
| **Survival** | "Survive for 20 minutes in a single raid" / "Extract without using any healing" |
| **Exploration** | "Visit 5 different POIs in a single raid" / "Open 10 containers" |

**Daily Rewards**: 200-500 credits, 100-250 experience, chance for a Bonus Card (consumable)

### Weekly Quest Pool (2 per week, random selection)

| Category | Examples |
| :------- | :------- |
| **Cumulative** | "Extract 10 times this week" / "Kill 50 enemies this week" |
| **Challenge** | "Extract with over 50,000 credits worth of loot in a single raid" |
| **Faction** | "Complete 5 faction quests from any faction" |
| **Social** | "Successfully extract with a squad 3 times" |

**Weekly Rewards**: 2,000-5,000 credits, 1,000-2,500 experience, guaranteed rare item

---

## Hidden Quest System

### How Hidden Quests Work

Hidden quests have **no quest markers or NPC prompts**. They activate automatically when specific conditions are met:

| Trigger Type | Example | Activates |
| :----------- | :------ | :-------- |
| **Collect all** | Find all 5 of Dr. Chen's audio logs | "The Last Experiment" — follow Chen's trail to a secret lab |
| **Environmental** | Interact with 3 specific terminals in sequence | "Emergency Protocol" — activate a hidden evacuation route |
| **Reputation** | Reach Rep 3 with all 4 factions simultaneously | "The Mediator" — all factions request your help with a shared problem |
| **Item** | Find a unique key item (random ultra-rare drop) | "Room 217" — access a previously locked area with unique lore |
| **Time** | Be in a specific location at a specific in-game time | "The Midnight Broadcast" — intercept a coded radio transmission |

### Design Guidelines for Hidden Quests

- **Discovery should feel earned**, not accidental
- Provide subtle environmental hints (graffiti pointing to related items, NPC throwaway lines)
- Rewards should be unique — cosmetics, lore entries, or items not available any other way
- **Never** gate critical story content behind hidden quests — they are bonuses for thorough players

---

## Narrative Branching Framework

### Decision Impact System

Player choices in main story quests accumulate values on hidden tracks:

| Track | Affected By | Impact |
| :---- | :---------- | :----- |
| **Transparency** | Who receives information, whether player shares findings | Determines available endings (transparent vs. secretive) |
| **Faction Loyalty** | Which faction's quests are completed most, who receives main quest decisions | Determines which NPCs support the player in endgame |
| **Morality** | Quest completion method (kill vs. spare, steal vs. negotiate) | Determines NPC dialogue tone and available solutions |

### Branching Rules

1. **No wrong answers**: Every choice leads to interesting content. No choice should make the player feel they've been tricked
2. **Delayed consequences**: The impact of a choice should not be immediately obvious. It should manifest 2-3 quests later
3. **Recoverable but costly**: Bad relationships can be rebuilt, but it takes significant effort and new content
4. **No perfect outcome**: The "best" ending requires difficult trade-offs. Players who try to please everyone will discover that's impossible

---

## Quest Balance Guidelines

### Difficulty Curve

| Player Level | Quest Type | Enemies | Time Pressure | Expected Completion Rate |
| :----------- | :--------- | :------ | :------------ | :----------------------- |
| 1-5 | Tutorial / Introduction | Tier 1 AI, low density | Generous | 90%+ |
| 5-10 | Standard faction T1 | Tier 1-2 AI, moderate density | Normal | 75-85% |
| 10-20 | Standard faction T2-T3 | Tier 2-3 AI, high density | Normal | 60-75% |
| 20-30 | Advanced / Main Story | Tier 3-4 AI, bosses | Moderate pressure | 50-65% |
| 30-40 | Veteran / Inner Circle | Tier 4 AI, enhanced bosses, PvP hotspots | Tight | 35-50% |
| 40+ | Endgame / Legendary | Maximum difficulty | Very tight | 20-35% |

### Reward Scaling

| Quest Difficulty | Credit Reward | XP Reward | Item Rarity | Rep Reward |
| :--------------- | :-----------: | :-------: | :---------- | :--------: |
| Easy | 200-500 | 100-250 | Common | 100-200 |
| Medium | 500-2,000 | 250-750 | Uncommon | 200-500 |
| Hard | 2,000-5,000 | 750-1,500 | Rare | 500-1,000 |
| Very Hard | 5,000-15,000 | 1,500-3,000 | Epic | 1,000-2,000 |
| Legendary | 15,000+ | 3,000+ | Legendary (unique) | 2,000+ |

---

## Anti-Frustration Design

### Quest Item Rules

| Rule | Purpose |
| :--- | :------ |
| Quest items drop from specific containers with a **minimum 30% spawn rate** | Prevent excessive grinding for rare quest drops |
| Quest kill targets are **guaranteed to spawn** when quest is active | Prevent "target not found" wasted raids |
| Items for active quests have a **subtle visual indicator** in the game world | Help players identify relevant items without hand-holding |
| Quest items can be stored in the secure container | Prevent quest progress loss on death (for collection quests) |

### Fail-State Handling

| Scenario | What Happens | Design Rationale |
| :------- | :----------- | :--------------- |
| Player dies with quest items | Items are lost (unless in secure container). Quest can be reattempted | Core extraction tension maintained |
| Player dies during "kill" objective after completing it | Kill is counted. Quest progress saved | Prevent punishing success |
| Player dies during "discover" quest after viewing objective | Discovery is recorded. Quest progress saved | Information discovered cannot be "undiscovered" |
| Player abandons quest | Quest can be re-accepted immediately. No penalty | Freedom to change priorities |
| Quest NPC is killed during raid (by other players) | NPC respawns next raid cycle. Quest remains active | NPCs are persistent world elements |

### Quest Softlock Prevention

- **No quest requires a unique, one-time item that can be permanently lost**
- All locked doors with quest objectives have alternative entry methods (vents, window, destructible walls)
- Timed quest objectives always have a buffer of at least 30% more time than the expected completion speed
- Multi-part quests save progress per part, never requiring full restart

---

## Quest Design Template

### For Narrative Designers

When creating new quests, fill in the following template:

```
QUEST DOCUMENT
==============

Quest ID: [FSC-T2-003] (Faction abbreviation - Tier - Number)
Quest Name: "[Name]"
Category: [Main Story / Faction / Daily / Weekly / Hidden]
Prerequisite: [Previous quest ID or reputation level]
Level Range: [Recommended player level]

NARRATIVE
---------
Context: [Why does this quest exist in the world? What's the backstory?]
Objective Summary: [One sentence player-facing description]
Lore References: [Which Backstory.md events or Codex entries does this connect to?]
Post-Quest World Change: [Does anything change in the world after completion?]

OBJECTIVES
----------
Primary:
  1. [Action verb + specific target + location]
  2. [Action verb + specific target + location]

Optional:
  1. [Bonus objective for extra reward]

REWARDS
-------
Credits: [Amount]
Experience: [Amount]
Reputation: [Faction +/- Amount]
Items: [Specific items or item pool]
Lore Unlock: [Codex entries or quest chains]

NPC DIALOGUE
------------
Quest Accept:
  "[Full dialogue script — refer to Narrative.md dialogue guidelines]"

Quest Turn-In (Success):
  "[Full dialogue script]"

Quest Turn-In (Optional Complete):
  "[Additional dialogue acknowledging bonus objective]"

ENVIRONMENTAL SETUP
-------------------
Required Props: [Items, terminals, NPCs that must exist in the world]
Audio Logs: [Any new audio logs placed for this quest]
Visual Changes: [Any environmental changes triggered by quest state]

DESIGN NOTES
------------
Estimated Completion Time: [Minutes]
Expected Difficulty: [Easy / Medium / Hard / Very Hard]
PvP Risk Level: [Low / Medium / High — based on quest location traffic]
Common Failure Points: [Where will players struggle?]
Anti-Frustration: [How do we prevent frustration at each failure point?]
```
