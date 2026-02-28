---
title: "Hydration & Energy System"
type: docs
weight: 14
---

## Overview

Hydration and Energy are survival resource bars that deplete over the course of a raid. They add a secondary layer of tension beyond HP — a player can be fully healthy but still dying from dehydration. Unlike HP, Hydration and Energy cannot be restored by medical items (they require food and water). Managing these resources is part of the preparation phase and the ongoing risk calculus of staying in-raid versus extracting.

> **Cross-References:** [Medical System](Medical_System.md) — interactions between food/water items and toxicity; [Core Gameplay Loop](CoreLoop.md) — Phase 5 Recovery; [Looting & Inventory](Looting_Interactions.md) — food/water as barter category; [Environmental Hazards](Environmental_Hazards.md) — environment effects on depletion rate.

---

## Core Design Principles

- **Attrition, not punishment.** Hydration and Energy create a pressure toward extracting on time. They are not meant to kill players in normal raid durations — only in extended "camper" scenarios.
- **Pre-raid provisioning.** Players who prepare food and water items for their loadout trade inventory slots for survival time. This is a deliberate gear tradeoff.
- **Stomach damage link.** When the **Stomach** body part takes damage or is blacked, Hydration and Energy drain accelerates dramatically — creating a devastating but recoverable debuff.
- **Cross-platform parity.** Same bar values and drain rates on all platforms. HUD display adapts by platform.

---

## Resource Bars

### Hydration

| Property | Value |
| :------- | :---- |
| **Maximum** | 100 points |
| **Starting value (raid start)** | 90 points (slightly depleted — players have been active) |
| **Passive drain rate** | 0.5 points / minute (base in normal conditions) |
| **Max raid drain (25 min)** | 12.5 points (from 90 → 77.5 at standard pace) |
| **Effect of depletion** | See threshold table below |
| **Recovery** | Water items only. Stimulants do not restore hydration. |

### Energy

| Property | Value |
| :------- | :---- |
| **Maximum** | 100 points |
| **Starting value** | 85 points (mildly depleted) |
| **Passive drain rate** | 1.0 point / minute (faster than hydration — hunger pressure) |
| **Max raid drain (25 min)** | 25 points (from 85 → 60 at standard pace) |
| **Effect of depletion** | See threshold table below |
| **Recovery** | Food items only. |

> **Design note:** In a standard 25-minute raid, neither Hydration nor Energy will reach dangerous levels from passive drain alone. Danger occurs from **Stomach damage** or **extended Overweight movement** that accelerates drain.

---

## Threshold Effects

### Hydration Thresholds

| Level | Hydration | Effect |
| :---- | :-------- | :----- |
| **Normal** | 60–100 | No effect |
| **Thirsty** | 40–59 | Subtle screen vignette (blue tint edges). Stamina recovery rate −10%. |
| **Dehydrated** | 20–39 | Screen desaturation begins. Stamina recovery −25%. Intermittent blurred vision (0.5s every 30s). |
| **Critically Dehydrated** | 1–19 | Heavy screen desaturation. −2 HP/min damage (to Thorax). Aim tremors. Hard to hide audio cue: dry cough (audible 5m). |
| **Dry** | 0 | −5 HP/min. Severe aim penalty. Screen vignette pulses. Movement speed −15%. |

### Energy Thresholds

| Level | Energy | Effect |
| :----- | :----- | :----- |
| **Normal** | 50–100 | No effect |
| **Hungry** | 30–49 | Minor stamina recovery −5%. Small dark screen edges. |
| **Famished** | 10–29 | Stamina drain +20%. Leg Stamina max −10. Character movement "feels" heavier. |
| **Starving** | 1–9 | −3 HP/min. Stamina cannot recover above 70%. Occasional stumble animation (cosmetic, no gameplay impact). |
| **Collapse** | 0 | −8 HP/min. Cannot sprint. Stamina bar locked at 0. |

---

## Accelerated Drain Conditions

| Condition | Hydration Drain | Energy Drain | Source |
| :-------- | :-------------- | :----------- | :----- |
| **Stomach blacked** | ×8 drain (4/min) | ×4 drain (4/min) | Limb damage per [Medical System](Medical_System.md) |
| **Overweight movement (45+ kg)** | ×1.5 | ×2.0 | Physical exertion |
| **Hot environment / Summer event** | ×1.5 | ×1.2 | [Environmental Hazards](Environmental_Hazards.md) — seasonal |
| **Stimulant injectors (active)** | −15 per injection (immediate) | No effect | Toxicity trade-off per [Medical System](Medical_System.md) |
| **Adrenaline injector** | −20 per use | No effect | High cost drug |

**Stomach blacked scenario:** A player who blacks their stomach (Stomach HP = 0) will lose Hydration at roughly 4 points/minute (8× base). At 90 starting Hydration, the player has approximately 22 minutes before "Dry" state. This creates an urgent need to either use a CMS/Surv12 surgery kit or extract immediately.

---

## Food & Water Items

### Water Items (Hydration)

| Item | Hydration Restored | Duration | Use Time | Inventory Size | Notes |
| :--- | :---------------: | :------: | :------: | :------------- | :---- |
| Water Bottle (small) | +20 | Instant | 2.0 s | 1×1 | Budget option; common loot |
| Water Bottle (large) | +45 | Instant | 2.5 s | 1×2 | Best standalone hydration item |
| Juice Box | +15 | Instant | 1.5 s | 1×1 | Compact; weak |
| Sports Drink | +35 | Instant | 2.0 s | 1×2 | Higher tier; some Energy bonus (+5) |
| IV Saline (Medical crossover) | +50 | Instant | 4.0 s | 1×2 | Medical item; double use. Also removes minor dehydration effect instantly |
| Purified Water (Hideout craft) | +60 | Instant | 2.5 s | 1×2 | Best in category; craftable |

### Food Items (Energy)

| Item | Energy Restored | Hydration Effect | Use Time | Inventory Size | Notes |
| :--- | :-------------: | :--------------: | :------: | :------------- | :---- |
| Crouton | +8 | −3 (salty) | 1.5 s | 1×1 | Ultra-compact; low value |
| Canned Beef Stew | +30 | −5 | 3.0 s | 1×2 | Common stash item |
| MRE (Meal, Ready-to-Eat) | +50 | +10 (includes drink) | 4.0 s | 2×2 | All-in-one; bulky |
| Energy Bar | +20 | 0 | 2.0 s | 1×1 | Compact; good ratio |
| Hot Meal (Hideout cook) | +60 | +15 | 3.5 s | 2×2 | Crafted; best food item |
| Golden Star Balm (crossover) | +15 Energy | 0 | 2.0 s | 1×1 | Pain remover + Energy; per [Medical System](Medical_System.md) |

### Consumption Rules

- Eating and drinking requires **standing still or walking** (no sprinting mid-consumption).
- Consumption produces **audible sounds**: drinking (slurping at 5m), eating (chewing at 3m). Not stealth-compatible in close quarters.
- Consumption is **not animation-locked** for shooting — player CAN eat and shoot. However, the eat animation uses the left hand, slightly reducing aim stability (−5% accuracy) for the duration.
- Food/water items have **no weight penalty** (they are 0.1–0.3 kg per item; accounted for in standard weight tables in [Gear Mechanics](Gear_Mechanics.md)).

---

## Interaction with Medical System

### Toxicity Does Not Affect Hydration/Energy

Toxicity accumulation from stimulant injectors (per [Medical System](Medical_System.md)) is a separate bar. However, stimulant items DO drain Hydration as a side effect (see accelerated drain table above).

### Compatibility Table

| Effect | Interaction |
| :----- | :---------- |
| Morphine painkiller | −10 Hydration |
| Propital | −5 Hydration +1 HP/sec (passive regen) |
| Adrenaline | −20 Hydration; short-term boost |
| Golden Star Balm | +15 Energy; removes Pain |
| IV Saline (medical use) | +50 Hydration; medical primary use |
| Grizzly Kit | No direct Hydration/Energy effect |

---

## HUD Display

| Platform | Display Location | Format |
| :------- | :--------------- | :----- |
| **PC** | Bottom-left, below HP bars | Two icons (droplet, lightning bolt) with fill meters + numeric value |
| **Console** | Same as PC | Same |
| **Mobile** | Bottom-right, compact row | Icon + thin bar only (no numeric unless tapped) |

**Warning indicators:**
- At 40 Hydration or 30 Energy: bar color shifts to **yellow**.
- At 20 Hydration or 10 Energy: bar turns **red** and pulses slowly.
- At 0 Hydration/Energy: bar blinks and small skull icon appears. Audio cue plays (ragged breathing for dehydration; growling stomach for energy).

**Hide in settings:** PCs and console players can elect to hide the resource bars from the HUD — they still receive audio/visual threshold warnings. This is for players who find them distracting.

---

## Cross-Platform Considerations

| Aspect | PC | Mobile | Console |
| :----- | :- | :----- | :------ |
| Drain rates | Identical | Identical | Identical |
| Recovery items | Same items, same values | Same | Same |
| HUD bar | Full (icon + bar + numbers) | Compact (icon + bar) | Full, adapted controller layout |
| Warning cues | Visual + audio | Visual + audio + haptic vibration | Visual + audio |

---

## Design Rationale

### Why Add Hydration/Energy to an Extraction Shooter?

1. **Anti-camp pressure:** Players who sit in a corner waiting to ambush others will deplete faster (no movement = passive drain accumulates uninterrupted). Not punishing enough alone, but combined with contamination, creates full-raid time pressure.
2. **Loadout depth:** Adding food and water to the pre-raid packing decision means players who spend 5 minutes planning their loadout have a meaningful edge over those who just grab a gun and deploy.
3. **Loot value:** Finding clean water in a contaminated raid zone has tangible gameplay value — not just barter value.
4. **Stomach damage consequence:** Without a tied survival system, blacking the stomach is "take −4/sec energy/hydration... and what?" With this system, stomach damage creates real urgency.

---

## Cross-References

- [Medical System](Medical_System.md) — Body part HP (Stomach = depletion multiplier); toxicity system; stimulant item effects.
- [Looting & Inventory](Looting_Interactions.md) — Food/water as Provisions barter category.
- [Gear Mechanics](Gear_Mechanics.md) — Food/water item weight in loadout budget.
- [Core Gameplay Loop](CoreLoop.md) — Phase 1 preparation; loadout packing decisions.
- [Environmental Hazards](Environmental_Hazards.md) — Hot environment accelerated drain.
