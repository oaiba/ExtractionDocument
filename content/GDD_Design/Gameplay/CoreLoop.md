---
title: "Core Gameplay Loop & Progression"
type: docs
weight: 1
---

## The Extraction Loop

The core engagement loop is designed to create a "Hero's Journey" in miniature, built on the cycle of **Risk Assessment, Execution, and Consequence**. Every raid follows five distinct phases, each with its own emotional arc and mechanical purpose.

> See [Core Gameplay Mechanics](../../GameDesign/CoreGameplay/) for the detailed per-minute match timeline, combat system numbers, and control scheme specifications.

### Session Length & Pacing

**Target session:** 15–20 minutes (mobile-friendly). Standard raid timer is 25–30 minutes so that a typical run (infiltrate, loot, extract) fits within one session; players who extract early or die early can queue again within the target window. An optional **Quick Raid** mode (e.g. 15-minute raid timer, smaller map or reduced objectives) may be offered for players who want a guaranteed short session. Design pillars: [Design Pillars](../../ProjectScope/design-pillars-enhanced.md). Mechanics benchmark: [Gameplay Review Checklist](Gameplay_Review_Checklist.md).

**Design decisions (re-planning):** Medical depth is kept (full body-part health, bleed, fracture, pain, blacked limb) for tactical identity. Operator abilities use cooldowns only (no per-raid charge limit); maximum ~2 signature uses per 20-minute raid.

**Cross-platform:** Same rules on all platforms (PC, console, mobile). Input and UX vary by device (e.g. hold E vs tap-and-hold for extract, keybinds vs touch layout); see [Controls](../../GameDesign/Controls.md) and [Gameplay Review Checklist](Gameplay_Review_Checklist.md).

---

## Phase 1: Preparation (Safety & Investment)

The preparation phase is the player's last moment of safety. Every decision made here sets the stakes for the entire raid.

### Loadout Philosophy

Players fall on a spectrum between two archetypal playstyles:

| Playstyle | Budget | Gear Philosophy | Risk Tolerance | Goal |
| :-------- | :----- | :-------------- | :------------- | :--- |
| **Rat** (Low Risk) | $5,000-10,000 | Cheap weapons, minimal armor, pistol runs | Low — minimize loss on death | Sneak, loot, avoid fights, extract quietly |
| **Standard** (Balanced) | $15,000-25,000 | Mid-tier weapons, medium armor, full meds | Medium — calculated engagements | Complete quests, loot efficiently, fight when advantageous |
| **Chad** (High Risk) | $40,000-60,000 | Best-in-slot weapons, heavy armor, full kit | High — hunt other players | Dominate the lobby, chase PvP, extract with enemy gear |

<!-- REF_IMAGE: Loadout Selection Screen — showing the three loadout tiers side by side with gear and cost breakdown -->

### Key Decisions

- **Budget vs. Confidence**: "Can I afford to lose this loadout? Do I trust my skill to justify the investment?"
- **Objective Selection**: Choosing between high-traffic quest areas, mid-risk loot runs, or perimeter scavenging.
- **Consumable Packing**: Balancing medical supplies, food, water, and grenades against available inventory space for loot.
- **Insurance Consideration**: Paying 10-20% of loadout value for a chance to recover gear if the body is not looted by other players.

### Risk Tolerance Profiles

```
Conservative Player ("Rat")
  Gear value:  < $10,000
  Decision:    Extract early, dodge fights
  Frequency:   80% survive, low per-raid value
  Long-term:   Slow, steady net positive

Balanced Player ("Standard")
  Gear value:  $15,000-25,000
  Decision:    Fight if advantaged, extract at 50% timer
  Frequency:   55-65% survive, moderate per-raid value
  Long-term:   Healthy growth curve

Aggressive Player ("Chad")
  Gear value:  > $40,000
  Decision:    Seek fights, stay until late extract
  Frequency:   35-45% survive, high per-raid value (when surviving)
  Long-term:   Volatile, feast-or-famine economy
```

**Design Intent**: All three playstyles must be viable. The economy must support rats without making chad gameplay feel unrewarding. Insurance acts as a safety net that scales with investment.

---

## Phase 2: Infiltration (Tension & Information)

The infiltration phase begins the moment the player spawns into the raid. This is when anticipation transitions into action.

### Spawn System

- **Random Insertion**: Players spawn at the edges of the map at randomized points. No two players spawn within 50m of each other.
- **10-Second Spawn Protection**: Brief invulnerability to prevent immediate spawn kills.
- **Initial Orientation**: Players must quickly identify their location using landmarks — there is no persistent minimap marker at spawn.

### Sound Discipline

Sound is the most critical information tool in the infiltration phase:

- **Walking** generates low noise (audible at ~15m)
- **Sprinting** generates high noise (audible at ~30m)
- **Crouching** generates minimal noise (audible at ~5m)
- Moving slowly to listen for enemy footsteps is the primary defensive skill. *Silence is the first weapon.*

### Information Gathering

| Source | Range | Reliability | Risk |
| :----- | :---- | :---------- | :--- |
| Footstep audio | 15-30m | High | None — passive |
| Gunshot audio | 100m+ | High | None — passive |
| Visual spotting | Line of sight | High | None if concealed |
| Looting sounds | 5-10m | Medium | None — passive |
| Loot beam (Rare+ items) | 30m | High | Reveals your position if looting |

**Squad shared vision:** The minimap uses merged visibility from the whole squad — any area seen by at least one teammate (or by intel abilities like Spotter Drone, Tactical Overlay) is revealed for the team. Fog of war shows explored-but-unseen areas; pings and marks from teammates persist in fog as last-known info. See [LOS, Fog of War & Visibility](LOS_Fog_Visibility.md) for full specification.

**Operator intel roles:** Hawk (Scout) and Glitch (Specialist) provide vision proxies and intel (drone, sensor, overlay) to clear fog and reveal enemies for the whole team; smoke (Obsidian/Recon) and deployable cover (Bastion) can block LOS. Details in [LOS, Fog of War & Visibility](LOS_Fog_Visibility.md) and [Hero Abilities](Hero_Abilities.md).

**Design Intent**: The infiltration phase teaches players that information is more valuable than firepower. A player who listens carefully has a significant advantage over one who sprints carelessly. Shared team vision rewards coordination: one scout can clear fog for the squad and feed intel without everyone being in the same room.

<!-- REF_IMAGE: Sound propagation diagram — concentric circles showing audible ranges for different actions overlaid on a map section -->

---

## Phase 3: Execution (The Peak)

The execution phase is the emotional peak of the raid. Combat encounters, high-value loot discoveries, and quest completions all happen here.

### The Engagement Decision

Every player encounter triggers a rapid mental calculation:

```
DETECTION
    |
  Can I win this fight?
  What gear do they have?
  Am I healthy/well-positioned?
    |
  +----YES----+----NO----+
  |           |          |
ENGAGE      FLEE      OBSERVE
  |           |          |
  Win/Lose  Reposition  Wait for opportunity
```

### The "Greed Check"

This is the single most important psychological mechanic in the game. After acquiring valuable loot, the player faces a binary choice:

- **Extract now** — Secure guaranteed profit, but miss potential gains.
- **Push one more room** — Risk everything for incremental reward.

The greed check intensifies as inventory value increases. A player carrying $50,000 in loot feels the weight of potential loss far more than one carrying $5,000.

**Design Levers:**
- Visible loot value counter on the HUD reinforces awareness of what is at stake
- Proximity pings ("Gunshots nearby") increase perceived danger
- Timer warnings create artificial urgency
- Quest item notifications ("Found 1/3 needed items") tempt the player to stay

### Loot Discovery

The dopamine reward for finding rare loot must be carefully calibrated:

| Rarity | Visual Feedback | Audio Feedback | Emotional Response |
| :----- | :-------------- | :------------- | :----------------- |
| Common | Minimal highlight | Quiet pick-up sound | Neutral |
| Uncommon | Soft glow | Subtle chime | Mild satisfaction |
| Rare | Visible beam (30m) | Distinct tone | Excitement — "Nice find" |
| Epic | Bright beam + particle | Rising musical sting | Adrenaline — "I need to extract NOW" |
| Legendary | Pulsing beam + glow | Full musical phrase | Panic — "Everyone can see this" |

<!-- REF_IMAGE: HUD mockup showing loot value counter, inventory weight indicator, and remaining raid timer during the execution phase -->

---

## Phase 4: Extraction (The Climax)

Extraction is the emotional climax of every raid. The player must navigate to a designated zone, survive a countdown timer, and escape with their loot.

### Extraction Types

| Type | Timer | Availability | Risk Level | Notes |
| :--- | :---- | :----------- | :--------- | :---- |
| Standard | 30s | Always active, 3-4 per map | High — known locations, heavily contested | Most common exit |
| Emergency | 15s | Requires key/quest item, 1-2 per map | Medium — hidden, but single-use | Faster but harder to access |
| Vehicle | 45s | Limited capacity (4 players), 1 per map | Very High — arrival noise draws attention | First-come-first-served |
| Cooperative | 20s | Requires 2+ players from different factions | Low — rewards trust | Reputation bonus for cooperation |

> See [Extraction Mechanics](../Extraction_Mechanics/) for the full interaction design, interruption rules, and counter-play systems.

### The Anxiety Arc

```
Approaching Extraction Zone
  Tension: 70% — "Am I being followed?"
      |
Enter Zone, Start Timer
  Tension: 90% — "30 seconds. Don't move."
      |
Timer at 15 seconds
  Tension: 95% — "Halfway there. Hearing footsteps?"
      |
Timer at 5 seconds
  Tension: 100% — "Almost out. Please..."
      |
EXTRACTION SUCCESSFUL
  Tension: 0% — Massive dopamine release
```

**Design Intent**: The extraction timer must feel like an eternity. The audio design — helicopter approaching, timer beeping, distant gunshots — creates a crescendo of anxiety that makes survival feel earned.

<!-- REF_IMAGE: Extraction zone aerial view — showing player position, extraction timer, helicopter approach vector, and possible enemy approach routes -->

---

## Phase 5: Recovery (The Aftermath)

The recovery phase bridges one raid to the next. It transforms raw loot into progression and sets the stage for the next cycle.

### Post-Raid Workflow

1. **Result Screen** — Display survival time, kills, loot acquired, XP earned
2. **Stash Management** — Organize the "Tetris" inventory, decide what to keep vs. sell
3. **Market Interaction** — Sell excess loot to NPC traders or list on the player flea market
4. **Hideout Upgrades** — Invest materials into passive bonuses (Bitcoin Farm, Medical Station, Workbench)
5. **Quest Turn-In** — Complete quest objectives, unlock new trader tiers
6. **Next Raid Prep** — The loop restarts

### The "One More Raid" Trigger

After a successful extraction, players experience a confidence boost that drives re-engagement:

```
Successful Extract
    |
"I'm on a hot streak"  →  Queue again immediately
    |
Second Raid Result
    |
  +---------+---------+
  |                   |
  Win Again          Death
  |                   |
"Unstoppable"      "I need to win that back"
  |                   |
  Queue again        Queue again (loss aversion)
```

Both outcomes drive re-engagement. This is the core retention mechanic.

---

## Psychological Hooks

Why do players come back? The extraction loop leverages multiple proven psychological mechanisms:

| Hook | Concept | Implementation |
| :--- | :------ | :------------- |
| **Variable Ratio Reinforcement** | "The Slot Machine" | Loot containers have random contents. You pull the lever (open the box) hoping for a jackpot. Most times it is junk, but the *chance* keeps you searching. |
| **Loss Aversion** | "It's Mine Now" | Once you loot an item, you feel ownership. Dying feels like having it *stolen*. This anger drives the "one more game" mentality to reclaim losses. |
| **Sunk Cost Fallacy** | "I'm Committed" | Upgrading the hideout requires massive resource investment. Players play to "justify" the time and money already spent. |
| **Mastery Curve** | "I'm Getting Better" | Learning map angles, recoil patterns, and spawn timings is a permanent skill that persists through death and seasonal wipes. |
| **Endowment Effect** | "This Is Worth More To Me" | Players overvalue items they found themselves vs. identical items bought from traders. Found-in-raid status reinforces this. |
| **Near-Miss Design** | "So Close..." | Dying with $50,000 in loot at the extraction door is devastating — but it guarantees the player will queue again to "make up for it." |

---

## Economy Design: Faucets and Sinks

To prevent hyper-inflation (where every player has best-in-slot gear), the economy uses a strict Faucet/Sink model.

### Faucets (Resource Inflow)

These inject value into the economy:

| Faucet | Description | Balancing Lever |
| :----- | :---------- | :-------------- |
| Raid Loot | Server-spawned items in containers and on AI enemies | Control spawn tables per map per patch |
| Scav Mode | Free zero-risk runs with random loadouts | Limit frequency (1 per 20 min cooldown), moderate loot quality |
| Passive Income | Hideout modules (Bitcoin Farm, Scav Case) generate currency over time | Cap output, require significant investment to build |
| Trader Stock | Infinite supply of basic ammo, meds, food from NPC vendors | Price floor prevents value collapse |
| Quest Rewards | Credits and items for completing objectives | One-time per quest line |

### Sinks (Resource Destruction)

These remove value to maintain scarcity:

| Sink | Description | Impact |
| :--- | :---------- | :----- |
| Death Loss | Uninsured gear is permanently deleted if not looted by another player | Primary sink — drives the entire economy |
| Consumables | Ammo, meds, food, grenades are one-time use | High-tier ammo is the biggest recurring money sink |
| Insurance Fees | 10-20% of item value for a *chance* of recovery | Only returns items not looted by others |
| Market Tax | Progressive tax on flea market transactions | Prevents infinite money circulation |
| Hideout Costs | Massive material dumps required for upgrades | Long-term progression sink |
| Repair Degradation | Armor and weapons lose max durability when repaired, eventually becoming scrap | Forces gear rotation, prevents hoarding |

### Dynamic Balancing ("The Invisible Hand")

- **Trader Barter Adjustments**: If a resource (e.g., Gunpowder) becomes too common, traders demand more of it for high-tier barters, artificially increasing demand.
- **Scarcity Events**: Limited-time events ("Fuel Shortage") reduce specific item spawn rates, draining player reserves as they panic-buy.
- **Seasonal Wipe Cycle**: Periodic economy resets (every 3-6 months) prevent terminal inflation and give all players a fresh start.

<!-- REF_IMAGE: Economy flow diagram — Machinations-style graph showing faucet and sink connections with flow rates -->
