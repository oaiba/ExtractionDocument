---
title: "Hideout & Crafting System"
type: docs
weight: 15
---

## Overview

The Hideout is the player's **persistent base of operations** — the bridge between raids that holds their stash, unlocks crafting, generates passive income, and provides the core meta-progression outside of combat. Investment in the hideout creates a material stake in the game beyond moment-to-moment loot, turning the long-term goal of an "upgraded base" into the primary Persistent Progression driver referenced in the [Design Pillars](../../ProjectScope/design-pillars-enhanced.md).

> **Cross-References:** [Core Gameplay Loop](CoreLoop.md) — Phase 5 Recovery; economy faucets/sinks; passive income; [Looting & Inventory](Looting_Interactions.md) — barter item categories (electronics, mechanical parts, provisions); [GameDesign/Economy](../../GameDesign/Economy.md) — macro-economy balance; [GameDesign/Progression](../../GameDesign/Progression.md) — hideout as long-term progression gate.

---

## Design Philosophy

- **Meaningful investment, not pay-to-win.** Hideout upgrades are bought with raid-earned materials. Real money cannot accelerate hideout upgrades.
- **Passive without being idle-game.** The hideout produces income while players are offline, but the production ceiling is gated by active play (materials must be looted, quests completed).
- **Upgrade order matters.** Modules have prerequisites — forcing players to plan an upgrade path, not just "buy everything."
- **Consequence of loss.** A player who dies repeatedly cannot farm hideout materials. The hideout naturally falls behind, motivating better play (or more conservative loadouts).

---

## Hideout Modules

### Module Overview

| Module | Function | Max Level | Unlocks |
| :----- | :------- | :-------: | :------ |
| **Stash** | Increases item storage size (grid) | 4 | Core; starts at Level 1 |
| **Workbench** | Weapon crafting and modification | 3 | Level 2 unlocks weapon modding |
| **Medical Station** | Medical item crafting, stimulant creation | 3 | Required for Medic quest chain |
| **Generator** | Powers other modules; determines active module count | 3 | Required before any other upgrade |
| **Scav Box** | Passive low-tier loot generation | 3 | Poor-man's passive income |
| **Bitcoin Farm** | Converts electronics into currency over time | 3 | Main passive income engine |
| **Nutrition Unit** | Food/water crafting for raid provisioning | 2 | Crafts Purified Water, Hot Meal |
| **Intelligence Center** | Reduces quest search time, unlocks bonus quests | 2 | Unlocks trader barter discounts |
| **Shooting Range** | Offline aim training + minor XP bonus | 1 | Quality of life |
| **Rest Space** | Reduces Scav cooldown (20 min → 12 min at max) | 2 | Economy optimization |
| **Vents** | Reduces hideout maintenance cost (filters, fuel) | 2 | Economy sink mitigation |

---

## Module Details

### Stash

The stash is the central inventory repository. All out-of-raid items, loot, and gear are stored here.

| Level | Grid Size | Unlock Cost | Prerequisite |
| :---- | :-------- | :---------- | :----------- |
| 1 (Starting) | 10×28 (280 slots) | Free | None |
| 2 | 10×38 (380 slots) | $50,000 + 20 Bolts + 10 Wires | Generator Lvl 1 |
| 3 | 10×48 (480 slots) | $150,000 + 3 GPU + 5 Circuit Boards | Generator Lvl 2 |
| 4 | 10×62 (620 slots) | $400,000 + 5 GPU + 10 Mechanical Parts + quest chain | Generator Lvl 3 |

*Slots = total stash capacity (cells).*

### Generator

Powers all other modules. Required before any upgrade path.

| Level | Active Modules | Fuel Consumption | Unlock Cost |
| :---- | :------------- | :--------------- | :---------- |
| 1 | 1 module active | 1 Fuel Can / 24h | Free (starting) |
| 2 | 3 modules active | 1 Fuel Can / 36h | $30,000 + 5 Wires + 3 Car Batteries |
| 3 | All modules active | 1 Fuel Can / 48h | $80,000 + 3 Spark Plugs + 2 Metal Pipes |

**Fuel management:** Fuel Cans are a recurring resource found in-raid or purchased from traders (expensive). Running out of fuel disables all passive modules — nothing produces offline. This is the primary **economy sink** for the hideout system. See [Economy](../../GameDesign/Economy.md).

### Bitcoin Farm

The primary passive income generator. Requires significant electronics investment.

| Level | GPU Slots | BTC per 12h | Profit Rate | Unlock Cost |
| :---- | :-------: | :---------: | :---------- | :---------- |
| 1 | 10 GPUs | 0.05 BTC | ~$2,000/12h | $200,000 + 5 GPU + 10 Circuit Boards + Gen Lvl 2 |
| 2 | 25 GPUs | 0.11 BTC | ~$4,400/12h | $500,000 + 15 GPU + 20 Circuit Boards + Workbench Lvl 2 |
| 3 | 50 GPUs | 0.2 BTC | ~$8,000/12h | $1,200,000 + 30 GPU + 40 Circuit Boards + Intel Lvl 2 |

**BTC value:** 1 BTC = $40,000–50,000 (market variable; trader buys at $40,000 fixed, flea market varies).  
**GPU acquisition:** GPUs are rare loot items found in electronics-category containers (labs, server rooms). Heavy demand creates competitive PvP around GPU spawn locations.

### Workbench

Enables weapon modification and basic crafting recipes.

| Level | Unlock | Key Recipe Added |
| :---- | :----- | :--------------- |
| 1 | $20,000 + 5 Bolts + 3 Wires + Gen Lvl 1 | Basic suppressor craft; ammo recasing |
| 2 | $60,000 + 10 Bolts + 5 Metal Pipes + Stash Lvl 2 | Weapon modification; magazine craft |
| 3 | $150,000 + 20 Mechanical Parts + 5 Bearings + quest | Tier 3–4 weapon mod recipes; grenade crafting |

### Medical Station

Enables medical item crafting and stimulant synthesis.

| Level | Unlock | Key Recipe Added |
| :---- | :----- | :--------------- |
| 1 | $25,000 + 5 Saline + 3 Surgical Instruments + Gen Lvl 1 | Basic meds (AI-2, Bandage ×5) |
| 2 | $70,000 + 10 Saline + 5 Blood Sets + Stash Lvl 2 | IFAK craft; painkiller synthesis |
| 3 | $200,000 + Rare Chemicals + Vents Lvl 2 + quest | Stimulant synthesis (Adrenaline, Propital, Grizzly) |

### Scav Box

A low-investment passive loot generator. Produces random Tier 1–2 items on a timer.

| Level | Output per 6h | Unlock Cost |
| :---- | :------------ | :---------- |
| 1 | 2–4 Tier 1 items | $10,000 + 10 Wires + Gen Lvl 1 |
| 2 | 3–5 Tier 1–2 items | $30,000 + 20 Wires + Stash Lvl 2 |
| 3 | 4–6 Tier 2 items (rare Tier 3) | $80,000 + 30 Wires + Circuit Boards ×5 + Intel Lvl 1 |

**Design cap:** Scav Box never produces Tier 4 items. Its output is supplemental, not a replacement for raiding.

---

## Crafting System

### Crafting Flow

```
1. Open Hideout screen
2. Navigate to module with crafting recipes (Workbench, Medical Station, Nutrition Unit)
3. Select recipe
4. Confirm: required items shown, check availability in stash
5. Start craft → timer begins
6. Return when timer completes, collect item from output slot
   (max 3 items queue up per module before must be collected)
```

### Recipe Structure

Each recipe has:
- **Input items** (consumed from stash)
- **Craft time** (real-time clock, same whether online or offline)
- **Output item** (placed in output slot when complete)
- **Module level requirement**

### Sample Crafting Recipes

**Workbench**

| Recipe | Inputs | Craft Time | Output |
| :----- | :------ | :--------: | :----- |
| 5.56 AP Ammo (20 rounds) | Brass ×10 + Gunpowder ×5 + Bolts ×2 | 45 min | 20× 5.56 AP rounds |
| Suppressor (9mm) | Metal Pipe ×2 + Springs ×3 | 2h | 1× 9mm suppressor |
| Frag Grenade | Bolts ×5 + Gunpowder ×8 + Metal Pipe ×1 | 1.5h | 2× Frag Grenades |

**Medical Station**

| Recipe | Inputs | Craft Time | Output |
| :----- | :------ | :--------: | :----- |
| IFAK Kit | Bandage ×3 + Saline ×2 | 30 min | 1× IFAK |
| Painkiller (Analgin) | Chemical Supply ×2 | 20 min | 5× Analgin |
| Adrenaline Injector | Rare Chemical ×3 + Saline ×1 | 4h | 1× Adrenaline |

**Nutrition Unit**

| Recipe | Inputs | Craft Time | Output |
| :----- | :------ | :--------: | :----- |
| Purified Water | Water Bottle (dirty) ×2 + Filter ×1 | 1h | 1× Purified Water (+60 Hydration) |
| Hot Meal Pack | Canned Beef ×2 + Provisions ×2 + MRE ×1 | 1.5h | 1× Hot Meal (+60 Energy, +15 Hydration) |

---

## Upgrade Prerequisites (Tech Tree)

```
Generator Lvl 1 (free start)
    ├── Stash Lvl 2 (⁋ Stash improvements)
    │       └── Stash Lvl 3
    │               └── Stash Lvl 4 [Generator Lvl 3 req]
    ├── Workbench Lvl 1
    │       ├── Workbench Lvl 2 [Stash Lvl 2 req]
    │       │       └── Workbench Lvl 3 [quest req]
    │       └── Bitcoin Farm Lvl 1 [Generator Lvl 2 req]
    │               ├── Bitcoin Farm Lvl 2 [Workbench Lvl 2 req]
    │               │       └── Bitcoin Farm Lvl 3 [Intel Lvl 2 req]
    ├── Medical Station Lvl 1
    │       ├── Medical Station Lvl 2 [Stash Lvl 2 req]
    │       │       └── Medical Station Lvl 3 [Vents Lvl 2 req + quest]
    ├── Scav Box Lvl 1
    │       ├── Scav Box Lvl 2 [Stash Lvl 2 req]
    │       │       └── Scav Box Lvl 3 [Intel Lvl 1 req]
    ├── Rest Space Lvl 1 [Stash Lvl 2 req]
    │       └── Rest Space Lvl 2
    └── Generator Lvl 2 (required for more active modules)
            ├── Intelligence Center Lvl 1 [Workbench Lvl 1 req]
            │       └── Intelligence Center Lvl 2
            ├── Nutrition Unit Lvl 1
            │       └── Nutrition Unit Lvl 2
            ├── Vents Lvl 1
            │       └── Vents Lvl 2
            └── Generator Lvl 3 (all modules active)
                    └── Shooting Range Lvl 1
```

---

## Seasonal Wipe Cycle

Per [Core Gameplay Loop](CoreLoop.md), a **seasonal wipe** every 3–6 months resets:
- All player inventory (stash items)
- All hideout module levels (back to starting state)
- Economy currency

**What is NOT reset:**
- Operator Mastery XP (cosmetic progress preserved)
- Account-level badges and titles
- Cosmetic items purchased or earned

**Wipe reward:** Players who reach a high hideout level before wipe receive exclusive cosmetic rewards (weapon skins, operator badges) as wipe season prestige items.

---

## Mobile / Offline Consideration

All hideout timers run on the **server clock**, not the client device. This means:
- Crafting and passive income continue while the game is closed.
- Mobile players get the full benefit of offline progression.
- Push notifications alert players when crafts complete or when passive income is ready to collect (opt-in).
- **Collection required:** Items in output slots and passive income must be manually collected. They do not auto-deposit after 48h to discourage fully idle gameplay.

---

## Summary of Key Decisions

| Topic | Decision |
| :---- | :------- |
| **Module levels** | Max 3 levels per production module; max 4 for Stash |
| **Tech tree** | Linear prerequisites — must build Generator before anything; Stash before most upgrades |
| **Bitcoin Farm** | Main passive income; GPU-gated; real-money purchase cannot accelerate |
| **Fuel system** | Recurring fuel cost; running dry disables all passive modules |
| **Seasonal wipe** | Full inventory and hideout reset 3–6 months; cosmetics preserved |
| **Craft timers** | Server-clock; offline progression; push notification opt-in |
| **Economy gating** | Hideout Lvl 3 upgrades require quest completion, not just currency |

---

## Cross-References

- [Core Gameplay Loop](CoreLoop.md) — Phase 5 Recovery; economy faucets (Bitcoin Farm, Scav Case); sinks (hideout costs).
- [Looting & Inventory](Looting_Interactions.md) — Input item categories (electronics, mechanical, provisions).
- [Hydration & Energy](Hydration_Energy.md) — Nutrition Unit output items.
- [Medical System](Medical_System.md) — Medical Station output items; toxicity system.
- [GameDesign/Economy](../../GameDesign/Economy.md) — Macro economy balance; faucet/sink calibration.
- [GameDesign/Progression](../../GameDesign/Progression.md) — Hideout level as progression milestone.
- [AI Enemy Behavior](AI_Enemy_Behavior.md) — Scav Box output mirrors AI Scav loot quality.
