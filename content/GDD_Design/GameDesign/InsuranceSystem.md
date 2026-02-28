---
title: "Insurance System Design"
type: docs
weight: 18
---

## Overview

The Insurance System is one of the defining mechanics of the extraction genre — it transforms catastrophic gear loss from a pure punishment into a **calculated risk mitigation tool**. Designed correctly, insurance teaches players to value their gear, encourages bold play, and deepens strategic thinking about every loadout decision.

**Core loop:** Insure gear before raid → Die → Hope others don't loot your gear → Items returned after delay.

> **Cross-References:** [Loadout Preparation](LoadoutPreparation.md) — Insurance UI integrated into prep screen; [Economy](Economy.md) — Insurance costs scaled to credit values; [Hideout & Crafting](../Gameplay/Hideout_Crafting.md) — Insurance inbox accessed via Hideout mail station; [Traders](../Gameplay/Quest_Objective_System.md) — Viktor and Ada are traders who also offer insurance.

---

## 1. Design Philosophy

### Why Insurance Exists

| Without Insurance | With Insurance |
| :---------------- | :------------- |
| Death = Total loss (punishing) | Death = Conditional loss (strategic) |
| Players overly cautious, avoid fights | Players take calculated risks |
| New players quit after losing first good kit | New players rebuild with insured returns |
| No recovery mechanic — pure punishment loop | Recovery arc — loss becomes a setback, not a reset |

**Key insight from Tarkov:** Insurance is one of the most loved mechanics — players describe the moment their items return as a "small victory" even after a loss. The **anticipation of return** replaces some of the sting of death.

### What Insurance Does NOT Do

- ❌ Guarantee return — if another player loots your insured item, it is **gone**
- ❌ Cover non-insurable items (secure container, quest items, consumables, ammo)
- ❌ Return items lost to the contamination zone (match timer expired)
- ❌ Cover items that go MIA (Missing In Action — disconnected mid-raid)

### The "Insurance Fraud" Design Space

Players can intentionally **hide their gear** in obscure locations before dying or extracting — planning to let their insurance "return" the item while they extract with different high-value loot. This is:
- ✅ **Intentional design** — a form of advanced strategic play
- ✅ Fun emergent behavior we support
- ⚠ Countered by other players learning to check common hiding spots

---

## 2. Insurer NPCs

Two traders offer insurance services, each with distinct tradeoffs:

### Viktor Kozlov — Salvage Corps

| Attribute | Value |
| :-------- | :---- |
| **Unlock** | Available from Account Level 1 |
| **Insurance cost** | 15% of item base credit value |
| **Return time** | 12–16 hours (after raid ends) |
| **Hold time** | Items held in inbox for 4 days before discarded |
| **Payment method** | Credits |
| **Special rule** | First insurance ever is FREE (new player onboarding) |
| **Flavor** | "I'll get it back. Costs extra for speed." |

**Best for:** Active daily players who run raids frequently and want fast returns on high-value gear.

---

### Ada Chen — Tech Syndicate

| Attribute | Value |
| :-------- | :---- |
| **Unlock** | Requires Trader Reputation: Friendly (1,000 rep) with Tech Syndicate |
| **Insurance cost** | 8% of item base credit value |
| **Return time** | 36–48 hours (after raid ends) |
| **Hold time** | Items held in inbox for 2 days before discarded |
| **Payment method** | Credits |
| **Special rule** | Items insured with Ada retain more durability on return (10% repair bonus) |
| **Flavor** | "Slower process. Cheaper. Take it or leave it." |

**Best for:** Budget players, casual players who log in every 1–2 days, or when insuring large numbers of lower-cost items.

---

### Insurer Comparison Table

| Factor | Viktor | Ada |
| :----- | :----- | :-- |
| Cost | 15% | 8% |
| Speed | ★★★★★ (12–16h) | ★★☆☆☆ (36–48h) |
| Hold period | 4 days | 2 days |
| Unlock requirement | None | Syndicate Friendly |
| Durability on return | Normal | +10% bonus |
| Best for | Frequent players | Budget/casual |

**Design rule:** Players should never feel forced into one insurer — each has a valid use case across different playstyles. We avoid a single "obviously correct" choice.

---

## 3. What Can and Cannot Be Insured

### ✅ Insurable Items

| Category | Examples |
| :------- | :------- |
| Weapons (primary) | Rifles, SMGs, LMGs, DMRs, shotguns |
| Weapons (secondary) | Pistols, revolvers |
| Weapon attachments | Scopes, suppressors, grips, barrels, stocks |
| Body armor | Plate carriers, vests |
| Helmets | All classes |
| Backpacks | All sizes |
| Ear protection / headsets | Tactical headsets |
| Melee weapons | Knives, hatchets |
| High-value containers | Weapon cases, item cases |

### ❌ Non-Insurable Items

| Category | Reason |
| :------- | :----- |
| **Secure Container** | Always safe — insurance would be redundant |
| **Quest items (FIR)** | Found-In-Raid tagged items cannot be insured to prevent exploit |
| **Ammo** | Bulk commodity — insurance would trivialize ammo economy |
| **Consumables** (food, water, meds) | Single-use, low individual value |
| **Currency** (credits, tokens) | Would break economy balance |
| **Keys** (single-use) | Already consumed on use |
| **Event items** | Per-event rules defined in LiveOps |

---

## 4. Visual Indicators

Insurance status must be **visually obvious at all times** — in stash, in loadout screen, and in-raid.

### In Stash / Loadout Screen

| Status | Visual |
| :----- | :----- |
| Insured (Viktor) | 🛡 Blue shield icon — top-left corner of item tile |
| Insured (Ada) | 🛡 Grey shield icon — top-left corner of item tile |
| Not insured | No icon |
| Insurance pending (in queue) | 🕐 Clock icon overlay — item is currently being "processed" |
| Insurance returned (inbox) | 📬 Animated notification badge on Hideout mail button |

### Color Coding in Loadout Gear Slots

```
┌──────────────────────────────────────────────────────┐
│  PRIMARY WEAPON                                      │
│  ┌──────────────────────────────────────────────┐   │
│  │ 🛡 M4A1 (HK416 barrel, ACOG, comp)           │   │  ← Blue border = insured
│  │    Value: $14,200    Weight: 3.6 kg           │   │
│  └──────────────────────────────────────────────┘   │
│                                                      │
│  ARMOR                                               │
│  ┌──────────────────────────────────────────────┐   │
│  │ ⚠ Plate Carrier [Class 4]                    │   │  ← Yellow border = uninsured high-value
│  │    Value: $9,800     Weight: 6.1 kg           │   │
│  └──────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────┘
```

**Auto-warning:** If an equipped item's value exceeds $5,000 and it is not insured, a subtle ⚠ amber icon appears on the gear slot as a nudge (not a blocker).

---

## 5. Insurance Flow — Step-by-Step

### Before Raid (Insuring)

```
LOADOUT PREP SCREEN
    │
    ▼
Player clicks [Insure All Equipped — Viktor: $2,250]
    │
    ▼
System calculates: 15% × total insurable value
    │
    ▼
Confirmation: "Insure 8 items for $2,250 with Viktor?"
    [CONFIRM]  [PER ITEM REVIEW]  [CANCEL]
    │
    ▼
Credits deducted immediately from balance
    │
    ▼
Shield icons appear on all insured gear slots
    │
    ▼
[DEPLOY TO RAID]
```

### During Raid

- Insured gear behaves identically to uninsured gear
- If another player loots an insured item from your body, the insurance claim is **voided** for that item
- If your item remains on your body uncollected, the insurance claim is **valid**
- Contamination zone death: All items lost, **no insurance return** (match expired = MIA status)

### After Raid — Death Outcome

```
PLAYER KILLED IN ACTION
    │
    ▼
Server logs: which insured items were looted vs. uncollected
    │
    ▼
After [Return Time] (Viktor: 12–16h / Ada: 36–48h):
    │
    ├─ Uncollected items → Added to Insurance Inbox in Hideout
    └─ Looted items → Lost permanently (no return)
    │
    ▼
Player receives push notification: "3 items returned by Viktor"
    │
    ▼
Player visits Hideout Mail Station → Claims items to stash
```

### Insurance Inbox UI (Hideout Mail Station)

```
┌────────────────────────────────────────────────────────────┐
│  📬  INSURANCE INBOX                                        │
│  ─────────────────────────────────────────────────────────  │
│  [Viktor] — Returned 3 items (hold until: 3 days 14h left) │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ ✅ M4A1 (ACOG, comp)         — RETURNED             │   │
│  │ ✅ Plate Carrier [Class 4]   — RETURNED             │   │
│  │ ❌ HK416 barrel              — LOOTED (lost)        │   │
│  └─────────────────────────────────────────────────────┘   │
│  [ Claim All to Stash ]                                     │
│  ─────────────────────────────────────────────────────────  │
│  [Ada] — Processing... Returns in ~28 hours                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ ⏳ M/65 Helmet               — PENDING              │   │
│  │ ⏳ Standard Backpack         — PENDING              │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────┘
```

---

## 6. Insurance Cost Calculation

### Base Formula

```
Insurance Cost = Item Base Value × Insurer Rate × Condition Modifier

Where:
  Item Base Value = Credit value of item at 100% condition
  Insurer Rate = Viktor: 0.15 / Ada: 0.08
  Condition Modifier:
    100% condition → 1.0× (full base value)
    75%–99%        → 0.85× (slightly reduced cost)
    50%–74%        → 0.70× (moderate reduction)
    25%–49%        → 0.55× (heavy reduction)
    <25%           → 0.40× (nearly broken gear insured cheaply)
```

**Design intent:** Damaged gear costs less to insure — encourages insuring even worn gear rather than skipping insurance entirely.

### Attachment Insurance

When a weapon is insured, its equipped attachments are **automatically included** in the insurance:
- All currently mounted attachments insured under the weapon's insurance entry
- If attachment is removed in-raid and left on body → each attachment checked individually
- Per-item insurance lets players selectively include/exclude specific attachments

### Example Calculation

| Item | Condition | Base Value | Insurer | Rate | Modifier | Cost |
| :--- | :-------- | :--------- | :------ | :--- | :------- | :--- |
| M4A1 (modded) | 100% | $12,000 | Viktor | 15% | 1.0 | **$1,800** |
| Plate Carrier | 72% | $8,000 | Viktor | 15% | 0.70 | **$840** |
| M/65 Helmet | 88% | $2,500 | Ada | 8% | 0.85 | **$170** |
| Standard Backpack | 100% | $2,000 | Ada | 8% | 1.0 | **$160** |
| **Total** | — | **$24,500** | Mixed | — | — | **$2,970** |

---

## 7. Insurance Edge Cases & Rules

| Scenario | Outcome |
| :------- | :------ |
| Player **extracts successfully** with insured gear | Insurance claim auto-cancelled; no return needed; **credits refunded** (minus 2% processing fee) |
| Player **kills** another player and loots their insured item | Looted item lost to original owner; insurance void; **killer keeps item permanently** |
| Player **hides** their gear and dies without it being found | Item considered "not looted" → insurance returns it |
| Player **dies in contamination zone** (match timer expired) | All items marked MIA → **No insurance return** |
| Player **disconnects mid-raid** (MIA) | Items marked MIA → **No insurance return** for 5 minutes; if player reconnects and survives/extracts, normal rules apply |
| **Container with items** (weapon case) insured | Container insured; items inside the container **not individually insured** (players must insure inside items separately) |
| **Double insurance** (insuring same item twice) | System prevents duplicate — second insurance request rejected with warning |
| **Insurance on a quest item** | System prevents — quest items shown as uninsurable with tooltip |
| **Teammate loots your insured gear** | Treated identically to enemy looting — item lost; insurance void (no friendly exceptions) |
| **Level-up unlocks Ada** during active Viktor insurance | Active Viktor claims unaffected; future raids can use Ada |

---

## 8. Advanced Strategy Notes

### "Ghost Insuring" (Player Tactic)

1. Insure a cheap weapon ($3,000 SMG for $450)
2. Go to raid
3. Find or kill for a better uninsured weapon ($15,000 rifle)
4. Drop the insured SMG in a hidden room
5. Extract with the $15,000 rifle
6. SMG returns via insurance 16 hours later → **Player gains new weapon while keeping insured one**

**Design response:** This is intentional — it teaches players to think creatively about the economy. We do not patch this.

### "Budget Kit + Full Insurance" (Recommended New Player Strategy)

- Budget kit: $8,000
- Insurance cost: ~$1,200
- If you die and items return: Net loss = $1,200 (the insurance cost only)
- If you extract: Insurance refunded minus 2% = minimal loss

**Teaching moment:** Insurance makes cheap loadouts nearly risk-free. We explicitly show this calculation in the first-raid onboarding.

---

## 9. Progression Unlocks for Insurance

| Unlock | Condition | Effect |
| :----- | :-------- | :----- |
| Ada insurance | Tech Syndicate Friendly (1,000 rep) | Access to cheaper, slower insurance |
| Viktor Tier 2 | Salvage Corps Honored (5,000 rep) | Return time reduced: 12h → 10h |
| Viktor Tier 3 | Salvage Corps Revered (15,000 rep) | Return time reduced: 10h → 8h; hold time extended to 5 days |
| Ada Tier 2 | Tech Syndicate Honored (5,000 rep) | Durability bonus on return: 10% → 20% |
| Hideout: Insurance Office Level 1 | Hideout upgrade | Hold time +1 day for all insurers |
| Hideout: Insurance Office Level 2 | Hideout upgrade | Can insure containers — items inside automatically included |
| Hideout: Insurance Office Level 3 | Hideout upgrade | Insurance refund on successful extract increased: 2% fee → 0% (full refund) |

---

## Cross-References

- [Loadout Preparation](LoadoutPreparation.md) — Insurance UI and insurer selection integrated into the pre-raid prep screen.
- [Economy](Economy.md) — Insurance costs draw from Credits; credit sinks and balance considerations.
- [Hideout & Crafting](../Gameplay/Hideout_Crafting.md) — Insurance Office upgrade module; mail station for claiming returned items.
- [Quest & Objective System](../Gameplay/Quest_Objective_System.md) — Quest items flagged as FIR are excluded from insurance; trader reputation required to unlock Ada.
- [Gear Mechanics](../Gameplay/Gear_Mechanics.md) — Item condition/durability system used in insurance cost calculation.
- [Post-Game Debrief](../Gameplay/Post_Game_Debrief.md) — Death screen shows which items were looted vs. insured; links to insurance inbox.
