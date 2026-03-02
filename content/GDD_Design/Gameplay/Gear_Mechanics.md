---
title: "Gear Mechanics"
type: docs
weight: 3
---

## Overview

Gear is a primary gameplay lever: every loadout choice affects mobility, capacity, survivability, and risk. This document describes **how equipment interacts with the raid** — movement, stamina, looting, extraction, and combat flow — rather than item specifications (armor and storage specs: [Gears](../../Gears/) — ArmorGear & StorageGear; inventory system overview: [Inventory & Gear](../../Inventory_Gear/)).

**Core principles:**

- **Weight has consequences:** Heavier loadouts reduce speed and increase stamina drain; see [Movement & Stamina](Movement_and_Stamina.md).
- **Tactical ergonomics:** Where you store items (rig vs backpack) determines hotkey access and search speed; see [Looting & Inventory](Looting_Interactions.md).
- **Loadout philosophy:** Rat, Standard, and Chad playstyles map to distinct gear choices and extraction behavior; see [Core Gameplay Loop](CoreLoop.md).
- **Gear rarity and economy:** Higher-tier gear costs more, offers better stats, but amplifies loss on death — the risk/reward engine.

Design pillars behind this: *Weight Has Consequences* and *Tactical Ergonomics* from the [Inventory & Gear design philosophy](../../Inventory_Gear/).

---

## Weight and Mobility

Total carried weight (rig, armor, backpack, weapons, ammo, meds, loot) directly affects movement speed, stamina drain, noise, and combat capability. Exact numbers are defined in [Movement & Stamina](Movement_and_Stamina.md); this section shows how they translate into gameplay.

### Weight Tiers

| Tier | Weight Range | Speed | Stamina Drain | Noise | Sprint | Jump | Inertia | Top-down camera feel |
| :--- | :----------- | :---- | :------------ | :---- | :----- | :--- | :------ | :------------------- |
| **Light** | 0–15 kg | 100% | 1.0x | Normal | Yes | Yes | Minimal | Responsive, snappy turns |
| **Medium** | 15–25 kg | 90% | 1.2x | Slightly louder | Yes | Yes | Slight delay on direction change | Standard feel |
| **Heavy** | 25–35 kg | 75% | 1.5x | Equipment rattle (audible 15 m) | Yes (limited duration) | Reduced height | Noticeable turn lag | Heavier, sluggish |
| **Critical** | 35–45 kg | 60% | 2.0x | Loud (audible 20 m) | **No** | Reduced | High — hard to reverse | Tank-like |
| **Overweight** | 45+ kg | 45% | No recovery while moving | Very loud (audible 25 m) | **No** | **No** | Extreme | Near-immobile |

### Inertia System (Top-Down Specific)

Top-down perspective makes directional changes highly visible. Inertia scales with weight:

| Weight Tier | Direction change delay | Slide distance after stopping | Effect on dodge/strafe |
| :---------- | :-------------------- | :---------------------------- | :--------------------- |
| Light | 0.05 s | 0.2 m | Can strafe effectively |
| Medium | 0.10 s | 0.5 m | Slight overshoot |
| Heavy | 0.20 s | 1.0 m | Commit to direction |
| Critical | 0.35 s | 1.5 m | Cannot dodge reliably |
| Overweight | 0.50 s | 2.0 m | Stuck on course |

**Design intent:** In a top-down view, players can see enemies approaching from all directions. Inertia prevents heavy players from reacting as quickly as their camera allows — creating a gap between information (I see the enemy) and execution (I can turn in time). Lightweight players retain the ability to juke and dodge, rewarding the risk of bringing less gear.

### Weight Budget Calculator (Example Loadouts)

| Component | Rat build | Standard build | Chad build |
| :-------- | :-------- | :------------- | :--------- |
| Primary weapon | Glock 17 (0.9 kg) | M4A1 (3.0 kg) | AK-47 (3.3 kg) + M4A1 (3.0 kg) |
| Armor | None (0 kg) | Class 3 vest (5.0 kg) | Class 5 plate carrier (10.0 kg) |
| Helmet | None (0 kg) | Class 3 (1.2 kg) | Class 4 + visor (2.5 kg) |
| Rig | Light 2×3 (0.4 kg) | Heavy 3×4 (0.8 kg) | Heavy 3×4 (0.8 kg) |
| Backpack | Small 3×3 (0.5 kg) | Medium 4×4 (1.0 kg) | Large 5×5 (2.0 kg) |
| Meds | Bandage ×2 (0.2 kg) | IFAK + Bandage ×2 (0.8 kg) | Grizzly + IFAK + Stim (2.5 kg) |
| Ammo | 2 mags (0.5 kg) | 4 mags (1.2 kg) | 6 mags + grenades (2.8 kg) |
| **Total (entry)** | **~2.5 kg (Light)** | **~13.0 kg (Light/Medium)** | **~24.9 kg (Medium/Heavy)** |
| Room for loot before Heavy | ~32.5 kg of loot | ~22 kg | ~10 kg |

---

## Rig and Backpack Choice

### Quick-Access vs Grid-Access

The distinction between rig and backpack is central to combat flow:

| Storage | Access method | Access time | Can use while: | Best for |
| :------ | :----------- | :---------- | :------------- | :------- |
| **Pockets** (1×4) | Instant | 0 s | Sprinting, fighting | Keys, cash, painkillers |
| **Tactical rig** | Hotkey (1–6) | 0.3–0.5 s (equip animation) | Walking, crouching, ADS | Magazines, meds, grenades |
| **Backpack** | Open inventory grid | 1.0+ s (grid opens, drag, close) | Standing still only; vulnerable | Loot, extra ammo, barter items |
| **Secure container** | Open inventory grid | 1.0+ s | Standing still only | Quest items, keys, high-value smalls |

### Rig Tiers

| Rig | Grid | Slots | Weight | Hotkey slots | Typical cost | Notes |
| :-- | :--- | :---- | :----- | :----------- | :----------- | :---- |
| Chest Harness | 2×2 | 4 | 0.3 kg | 2 | 2,000 | Minimal; scav default |
| Light Rig | 2×3 | 6 | 0.4 kg | 3 | 5,000 | Scout/rat standard |
| Standard Rig | 3×3 | 9 | 0.6 kg | 4 | 12,000 | Balanced |
| Heavy Rig | 3×4 | 12 | 0.8 kg | 6 | 25,000 | Full loadout; chad preferred |
| Armored Rig | 3×4 | 12 | 3.5 kg | 6 + Class 3 armor built-in | 45,000 | Combines rig + light armor; saves a slot |

### Backpack Tiers

| Backpack | Grid | Slots | Weight (empty) | Speed penalty | Noise | Typical cost |
| :------- | :--- | :---- | :------------- | :------------ | :---- | :----------- |
| Sling Bag | 2×3 | 6 | 0.3 kg | None | None | 1,500 |
| Small | 3×3 | 9 | 0.5 kg | None | None | 4,000 |
| Medium | 4×4 | 16 | 1.0 kg | -2% speed | Slight rustle | 10,000 |
| Large | 5×5 | 25 | 2.0 kg | -5% speed | Audible at 8 m (even empty) | 22,000 |
| Raid Pack | 5×6 | 30 | 2.5 kg | -8% speed | Audible at 12 m | 40,000 |

**Noise from backpacks** is independent of weight-tier noise and stacks additively. A player at 30 kg (Heavy tier, rattle at 15 m) with a Large backpack (8 m) is audible at ~18 m composite. This punishes max-capacity greed.

---

## Armor and Survivability vs Speed

Armor class, materials, and hit zones are defined in [Gears — Armor & Ballistics](../../Gears/ArmorGear/Armor.md). This section covers the gameplay trade-off.

### Armor Weight vs Protection

| Armor example | Class | Coverage | Weight | Effect on weight tier | Effective extra shots survived (vs 5.56 FMJ) |
| :------------ | :---- | :------- | :----- | :-------------------- | :-------------------------------------------- |
| PACA Soft Vest | 2 | Thorax | 1.9 kg | Negligible | +1 shot (pistol rounds only) |
| 6B13 Vest | 3 | Thorax, stomach | 5.0 kg | Pushes Rat→Medium | +2–3 shots |
| Trooper Plate | 4 | Thorax | 7.5 kg | Pushes Standard→Heavy | +3–5 shots |
| Redut-M | 5 | Thorax, stomach, sides | 10.0 kg | Pushes Standard→Heavy/Critical | +5–7 shots |
| Zabralo Mk.2 | 6 | Full torso + neck | 12.5 kg | Nearly guarantees Heavy+ | +8–10 shots; near-invulnerable to low-pen |

### Helmet Weight vs Headshot Survival

| Helmet example | Class | Zones covered | Weight | Ricochet | Trade-off |
| :------------- | :---- | :------------ | :----- | :------- | :-------- |
| SSh-68 (Steel) | 3 | Top, nape | 1.5 kg | High | Heavy; good ricochet but no ears/face |
| ULACH | 4 | Top, nape, ears | 1.8 kg | Medium | Standard military choice |
| Altyn | 5 | Full + face shield | 2.5 kg | Low | Stops most rounds; blocks headset slot (no enhanced audio) |

**The headset trade-off:** Helmets that cover ears prevent wearing tactical headsets. Headsets amplify footstep audio range by ~30%. Players wearing an Altyn gain head protection but lose audio intelligence — a defining trade-off in a sound-critical extraction shooter.

### Armor Durability and Mid-Raid Degradation

Armor degrades during the raid as it absorbs hits. Effective protection drops:

| Durability remaining | Effective class reduction | Gameplay consequence |
| :------------------- | :----------------------- | :------------------- |
| 100–75% | None | Full protection |
| 74–50% | -0.5 class (blended) | Some rounds start penetrating |
| 49–25% | -1 class | Significant protection loss |
| 24–1% | -2 class | Barely functional; false sense of security |
| 0% | Destroyed | No protection; weight remains until dropped |

**Design intent:** Players cannot rely on a single set of armor for an entire raid. Taking multiple fights degrades armor, encouraging either extraction or finding replacement armor from killed players.

---

## Weapon Tier and Economy Risk

Weapons follow a tiered economy that amplifies the risk/reward loop:

| Tier | Cost range | Damage class | Availability | Economy risk on death |
| :--- | :--------- | :----------- | :----------- | :-------------------- |
| **Tier 1** (Scav) | 2,000–8,000 | Low: pistols, basic SMGs | Vendor Lvl 1 | Minimal — easy to replace |
| **Tier 2** (Standard) | 10,000–25,000 | Medium: ARs, shotguns | Vendor Lvl 2 | Moderate — 2–3 successful raids to recoup |
| **Tier 3** (Military) | 30,000–60,000 | High: modded ARs, DMRs | Vendor Lvl 3 or found in raid | Significant — insurance recommended |
| **Tier 4** (Elite) | 70,000–120,000 | Very high: rare sniper, LMG, full-mod meta | Vendor Lvl 4 (Exalted) or boss loot | Severe — loss sets back economy days |

**Weapon modification** adds 5,000–40,000 to weapon value (grips, optics, suppressors, muzzle devices). A fully modded Tier 3 AR can match Tier 4 base stats but costs near-Tier-4 prices — another cost vs performance decision.

---

## Loadout Philosophy in Action

### Example Raid Scenarios

**Scenario 1: The Rat (Quest Run)**

```
Loadout: Glock 17, no armor, light rig, small backpack
Entry weight: ~2.5 kg (Light)
Goal: Complete "Mark 3 supply crates" quest in Industrial Zone
Strategy: Crouch-walk, avoid fights, mark objectives, extract at first open zone
Mid-raid weight: ~8 kg after picking up incidental loot
Extraction: Sprint to nearest extract; timer 30s, no contest
Risk: ~3,000 lost on death
Reward: Quest XP + faction rep + 5,000–10,000 incidental loot
```

**Scenario 2: The Standard (Balanced)**

```
Loadout: M4A1, Class 3 vest, heavy rig, medium backpack
Entry weight: ~13 kg (Light/Medium)
Goal: Loot the Foundry (high-tier zone) + Daily quest "Extract with 5 medkits"
Strategy: Move cautiously, fight when advantaged, loot selectively
Mid-raid weight: ~28 kg (Heavy) after filling backpack
Extraction: Must choose: drop low-value loot to stay Medium, or accept Heavy and walk to extract
Risk: ~25,000 lost on death
Reward: 40,000–80,000 in loot + quest rewards
```

**Scenario 3: The Chad (PvP Hunt)**

```
Loadout: AK-47 (full mod) + M4A1, Class 5 plate, full meds, large backpack
Entry weight: ~25 kg (Medium/Heavy)
Goal: Hunt players at high-traffic zones, take their gear
Strategy: Push aggressively, use superior armor to win gunfights, loot enemy gear
Mid-raid weight: ~40 kg (Critical) after looting 2–3 players
Extraction: Cannot sprint at 40 kg; must plan route with minimal exposure
Risk: ~90,000 lost on death
Reward: Enemy loadouts (potentially 100,000–200,000 total value) + dominance XP
```

### Loadout Cost vs Extract Rate vs Net Gain

| Profile | Avg loadout cost | Extract rate | Avg loot gained (on extract) | Net gain/raid | Break-even after loss |
| :------ | :--------------- | :----------- | :--------------------------- | :------------ | :-------------------- |
| Rat | 3,000 | ~80% | 8,000 | +5,400 avg | 1 raid |
| Standard | 25,000 | ~60% | 50,000 | +17,500 avg | 2 raids |
| Chad | 90,000 | ~40% | 150,000 | +15,000 avg | 3 raids |

**Design intent:** All three profiles converge to similar hourly income, ensuring no single playstyle is economically dominant. Rats win by volume and consistency; Chads win by peak value but suffer harder crashes.

---

## Gear and Extraction Interaction

### Extract Readiness Flowchart

```
CHECK WEIGHT TIER
    |
  Light/Medium (<25 kg)?
    |── YES → Sprint to any extract. ~15s travel for 100m.
    |          Comfortable against extract campers.
    |
    NO (Heavy/Critical/Overweight)
    |
  Can I drop loot to reach Medium?
    |── YES → Evaluate: loot value vs survival.
    |          Drop low-value items? Or risk slow extract?
    |
    NO (armor + weapons alone put me at Heavy)
    |
  Must walk to extract at 60–75% speed.
  Choose nearest extract.
  Use smoke / flashbang / operator ability to defend timer.
  Accept higher risk.
```

### Gear Lost on Death vs Kept

| Item location | Lost on death | Recoverable via insurance |
| :------------ | :------------ | :------------------------ |
| Equipped (weapon, armor, rig, backpack) | Yes | Yes (if body not looted by other players; 70% return rate after 24h) |
| Items in rig and backpack | Yes | Yes (same insurance rules) |
| Items in secure container | **No — always kept** | N/A |
| Items in pockets | Yes | Yes |

### Insurance Economics

| Loadout cost | Insurance cost (15%) | Expected return | When worth it |
| :----------- | :------------------- | :-------------- | :------------ |
| 3,000 (Rat) | 450 | ~2,100 (70% of 3,000) | Almost always — cheap |
| 25,000 (Standard) | 3,750 | ~17,500 | Recommended |
| 90,000 (Chad) | 13,500 | ~63,000 | Essential — uninsured loss is devastating |

---

## Cross-Platform Considerations (Top-Down)

### Mobile vs PC Gear Interaction

Since the game targets cross-platform (PC + mobile), gear mechanics must account for input differences:

| Mechanic | PC (mouse + keyboard) | Mobile (touch) | Cross-platform parity solution |
| :------- | :-------------------- | :------------- | :----------------------------- |
| Inventory management | Drag-and-drop, precise | Tap-to-transfer, less precise | Auto-sort; tap-to-quick-equip; rig hotkeys work on both |
| Rig hotkey usage | Number keys 1–6 | On-screen buttons | Same cooldown/animation; mobile buttons sized per platform UX |
| Armor impact on combat | Aiming precise, armor matters less | Aim assist compensates; armor matters more | Balance aim-assist separately; armor stats identical |
| Weight awareness | HUD indicator | HUD indicator + haptic vibration at thresholds | Identical weight mechanics; mobile adds haptic feedback |

---

## Cross-References

- [Core Gameplay Loop](CoreLoop.md) — Loadout philosophy, preparation phase, risk tolerance.
- [Movement & Stamina](Movement_and_Stamina.md) — Weight thresholds, speed and stamina numbers, inertia, exhaustion.
- [Looting & Inventory](Looting_Interactions.md) — Grid dimensions, rig/backpack sizes, secure container.
- [Extraction Mechanics](Extraction_Mechanics.md) — Extraction process, timer, rules during extract.
- [Hero Abilities](Hero_Abilities.md) — Operator-specific gear constraints (Scout light rig only, Tank armor affinity).
- [Medical System](Medical_System.md) — Med item weights, heal timing, animation lock.
- [Gears](../../Gears/) — Armor and storage gear specs: [ArmorGear](../../Gears/ArmorGear/) (classes, zones, materials, master database), [StorageGear](../../Gears/StorageGear/) (rigs, backpacks, secure containers, slot layouts).
- [Inventory & Gear](../../Inventory_Gear/) — Inventory system overview, paper doll, grid, encumbrance.

For per-minute match timeline and raw balance numbers, see [Core Gameplay Mechanics](../../GameDesign/CoreGameplay/) if available.
