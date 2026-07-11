---
title: "Hydration & Energy hệ thống"
type: docs
weight: 14
---

## Tổng Quan

Hydration và Energy are survival resource bars that deplete over the course of a raid. They add a secondary layer of tension beyond HP — a người chơi can be fully healthy nhưng still dying from dehydration. Unlike HP, Hydration và Energy cannot be restored by medical items (they require food và water). Managing these resources is part of the preparation phase và the ongoing risk calculus of staying in-raid versus extracting.

> **Cross-References:** [Medical hệ thống](medical_system/index.html) — interactions between food/water items và toxicity; [cốt lõi Gameplay Loop](coreloop/index.html) — Phase 5 Recovery; [Looting & Inventory](looting_interactions/index.html) — food/water as barter category; [Environmental Hazards](environmental_hazards/index.html) — environment effects on depletion rate.

---

## cốt lõi Design Principles

- **Attrition, not punishment.** Hydration và Energy tạo a pressure toward extracting on thời gian. They are not meant to kill người chơi in normal raid durations — only in extended "camper" scenarios.
- **Pre-raid provisioning.** người chơi who prepare food và water items for their loadout trade inventory slots for survival thời gian. This is a deliberate gear tradeoff.
- **Stomach damage link.** khi the **Stomach** body part takes damage hoặc is blacked, Hydration và Energy drain accelerates dramatically — tạo a devastating nhưng recoverable debuff.
- **Cross-platform parity.** Same bar values và drain rates on all platforms. HUD display adapts by platform.

---

## Resource Bars

### Hydration

| Property | giá trị |
| :------- | :---- |
| **Maximum** | 100 points |
| **Starting giá trị (raid start)** | 90 points (slightly depleted — người chơi have been active) |
| **Passive drain rate** | 0.5 points / minute (base in normal conditions) |
| **Max raid drain (25 min)** | 12.5 points (from 90 → 77.5 at standard pace) |
| **Effect of depletion** | See threshold bảng below |
| **Recovery** | Water items only. Stimulants do not restore hydration. |

### Energy

| Property | giá trị |
| :------- | :---- |
| **Maximum** | 100 points |
| **Starting giá trị** | 85 points (mildly depleted) |
| **Passive drain rate** | 1.0 point / minute (faster than hydration — hunger pressure) |
| **Max raid drain (25 min)** | 25 points (from 85 → 60 at standard pace) |
| **Effect of depletion** | See threshold bảng below |
| **Recovery** | Food items only. |

> **Design note:** In a standard 25-minute raid, neither Hydration nor Energy will reach dangerous levels from passive drain alone. Danger occurs from **Stomach damage** hoặc **extended Overweight movement** that accelerates drain.

---

## Threshold Effects

### Hydration Thresholds

| Level | Hydration | Effect |
| :---- | :-------- | :----- |
| **Normal** | 60–100 | No effect |
| **Thirsty** | 40–59 | Subtle màn hình vignette (blue tint edges). Stamina recovery rate −10%. |
| **Dehydrated** | 20–39 | màn hình desaturation begins. Stamina recovery −25%. Intermittent blurred vision (0.5s every 30s). |
| **Critically Dehydrated** | 1–19 | Heavy màn hình desaturation. −2 HP/min damage (to Thorax). Aim tremors. Hard to hide audio cue: dry cough (audible 5m). |
| **Dry** | 0 | −5 HP/min. Severe aim penalty. màn hình vignette pulses. Movement speed −15%. |

### Energy Thresholds

| Level | Energy | Effect |
| :----- | :----- | :----- |
| **Normal** | 50–100 | No effect |
| **Hungry** | 30–49 | Minor stamina recovery −5%. Small dark màn hình edges. |
| **Famished** | 10–29 | Stamina drain +20%. Leg Stamina max −10. nhân vật movement "feels" heavier. |
| **Starving** | 1–9 | −3 HP/min. Stamina cannot recover above 70%. Occasional stumble animation (cosmetic, no gameplay impact). |
| **Collapse** | 0 | −8 HP/min. Cannot sprint. Stamina bar locked at 0. |

---

## Accelerated Drain Conditions

| Condition | Hydration Drain | Energy Drain | source |
| :-------- | :-------------- | :----------- | :----- |
| **Stomach blacked** | ×8 drain (4/min) | ×4 drain (4/min) | Limb damage per [Medical hệ thống](medical_system/index.html) |
| **Overweight movement (45+ kg)** | ×1.5 | ×2.0 | Physical exertion |
| **Hot environment / Summer event** | ×1.5 | ×1.2 | [Environmental Hazards](environmental_hazards/index.html) — seasonal |
| **Stimulant injectors (active)** | −15 per injection (immediate) | No effect | Toxicity trade-off per [Medical hệ thống](medical_system/index.html) |
| **Adrenaline injector** | −20 per cách dùng | No effect | High chi phí drug |

**Stomach blacked scenario:** A người chơi who blacks their stomach (Stomach HP = 0) will lose Hydration at roughly 4 points/minute (8× base). At 90 starting Hydration, the người chơi has approximately 22 minutes trước "Dry" trạng thái. This tạo an urgent need to either cách dùng a CMS/Surv12 surgery kit hoặc extract immediately.

---

## Food & Water Items

### Water Items (Hydration)

| Item | Hydration Restored | Duration | cách dùng thời gian | Inventory Size | ghi chú |
| :--- | :---------------: | :------: | :------: | :------------- | :---- |
| Water Bottle (small) | +20 | Instant | 2.0 s | 1×1 | Budget option; common loot |
| Water Bottle (large) | +45 | Instant | 2.5 s | 1×2 | Best standalone hydration item |
| Juice Box | +15 | Instant | 1.5 s | 1×1 | Compact; weak |
| Sports Drink | +35 | Instant | 2.0 s | 1×2 | Higher tier; some Energy bonus (+5) |
| IV Saline (Medical crossover) | +50 | Instant | 4.0 s | 1×2 | Medical item; double cách dùng. Also removes minor dehydration effect instantly |
| Purified Water (Safe House craft) | +60 | Instant | 2.5 s | 1×2 | Best in category; craftable |

### Food Items (Energy)

| Item | Energy Restored | Hydration Effect | cách dùng thời gian | Inventory Size | ghi chú |
| :--- | :-------------: | :--------------: | :------: | :------------- | :---- |
| Crouton | +8 | −3 (salty) | 1.5 s | 1×1 | Ultra-compact; low giá trị |
| Canned Beef Stew | +30 | −5 | 3.0 s | 1×2 | Common stash item |
| MRE (Meal, Ready-to-Eat) | +50 | +10 (includes drink) | 4.0 s | 2×2 | All-in-one; bulky |
| Energy Bar | +20 | 0 | 2.0 s | 1×1 | Compact; good ratio |
| Hot Meal (Safe House cook) | +60 | +15 | 3.5 s | 2×2 | Crafted; best food item |
| Golden Star Balm (crossover) | +15 Energy | 0 | 2.0 s | 1×1 | Pain remover + Energy; per [Medical hệ thống](medical_system/index.html) |

### Consumption Rules

- Eating và drinking requires **standing still hoặc walking** (no sprinting mid-consumption).
- Consumption produces **audible sounds**: drinking (slurping at 5m), eating (chewing at 3m). Not stealth-compatible in close quarters.
- Consumption is **not animation-locked** for shooting — người chơi CAN eat và shoot. However, the eat animation uses the left hand, slightly reducing aim stability (−5% accuracy) for the duration.
- Food/water items have **no weight penalty** (they are 0.1–0.3 kg per item; accounted for in standard weight tables in [Gear cơ chế](gear_mechanics/index.html)).

---

## Interaction với Medical hệ thống

### Toxicity Does Not Affect Hydration/Energy

Toxicity accumulation from stimulant injectors (per [Medical hệ thống](medical_system/index.html)) is a separate bar. However, stimulant items DO drain Hydration as a side effect (see accelerated drain bảng above).

### Compatibility bảng

| Effect | Interaction |
| :----- | :---------- |
| Morphine painkiller | −10 Hydration |
| Propital | −5 Hydration +1 HP/sec (passive regen) |
| Adrenaline | −20 Hydration; short-term boost |
| Golden Star Balm | +15 Energy; removes Pain |
| IV Saline (medical cách dùng) | +50 Hydration; medical primary cách dùng |
| Grizzly Kit | No direct Hydration/Energy effect |

---

## HUD Display

| Platform | Display Location | Format |
| :------- | :--------------- | :----- |
| **PC** | Bottom-left, below HP bars | Two icons (droplet, lightning bolt) với fill meters + numeric giá trị |
| **Console** | Same as PC | Same |
| **Mobile** | Bottom-right, compact row | Icon + thin bar only (no numeric unless tapped) |

**cảnh báo indicators:**
- At 40 Hydration hoặc 30 Energy: bar color shifts to **yellow**.
- At 20 Hydration hoặc 10 Energy: bar turns **red** và pulses slowly.
- At 0 Hydration/Energy: bar blinks và small skull icon appears. Audio cue plays (ragged breathing for dehydration; growling stomach for energy).

**Hide in settings:** PCs và console Người chơi có thể elect to hide the resource bars from the HUD — they still receive audio/visual threshold cảnh báo. This is for người chơi who find them distracting.

---

## Cross-Platform Considerations

| Aspect | PC | Mobile | Console |
| :----- | :- | :----- | :------ |
| Drain rates | Identical | Identical | Identical |
| Recovery items | Same items, same values | Same | Same |
| HUD bar | Full (icon + bar + thông số) | Compact (icon + bar) | Full, adapted controller layout |
| cảnh báo cues | Visual + audio | Visual + audio + haptic vibration | Visual + audio |

---

## Design Rationale

### Why Add Hydration/Energy to an Extraction Shooter?

1. **Anti-camp pressure:** người chơi who sit in a corner waiting to ambush others will deplete faster (no movement = passive drain accumulates uninterrupted). Not punishing enough alone, nhưng combined với contamination, tạo full-raid thời gian pressure.
2. **Loadout depth:** Adding food và water to the pre-raid packing quyết định means người chơi who spend 5 minutes planning their loadout have a meaningful edge over those who just grab a gun và deploy.
3. **Loot giá trị:** Finding clean water in a contaminated raid zone has tangible gameplay giá trị — not just barter giá trị.
4. **Stomach damage consequence:** mà không a tied survival hệ thống, blacking the stomach is "take −4/sec energy/hydration... và what?" với this hệ thống, stomach damage tạo real urgency.

---

## Out-of-Raid Recovery in Safe House

Between raids, người chơi restore Energy và Hydration in the [Safe House](../gamedesign/safe_house_design/index.html):

- **Consume from Stash:** Food và water items in the Stash can be consumed in the Safe House trước deploying. Consumed items restore Energy/Hydration; starting values (90 Hydration, 85 Energy) reflect the Operator's trạng thái khi entering the next raid.
- **Nutrition Unit:** Crafts Purified Water (+60 Hydration) và Hot Meal (+60 Energy, +15 Hydration) for provisioning.
- **Pre-raid provisioning:** người chơi who consume food/water in Safe House trước raid start enter với higher values; those who skip enter at default (hoặc depleted nếu they died với low values).

Xem [Safe House Design — Out-of-Raid Operator trạng thái](../GameDesign/Safe_House_Design.md#3-out-of-raid-operator-trạng thái) for full chi tiết.

---

## Tham Chiếu Chéo

- [Medical hệ thống](medical_system/index.html) — Body part HP (Stomach = depletion multiplier); toxicity hệ thống; stimulant item effects.
- [Looting & Inventory](looting_interactions/index.html) — Food/water as Provisions barter category.
- [Gear cơ chế](gear_mechanics/index.html) — Food/water item weight in loadout budget.
- [cốt lõi Gameplay Loop](coreloop/index.html) — Phase 1 preparation; loadout packing quyết định.
- [Environmental Hazards](environmental_hazards/index.html) — Hot environment accelerated drain.
- [Safe House Design](../gamedesign/safe_house_design/index.html) — Out-of-raid Energy/Hydration recovery.
