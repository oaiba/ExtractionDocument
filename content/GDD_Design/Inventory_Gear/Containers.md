---
title: "Containers & Storage"
weight: 2
type: docs
---

## Overview

Managing space is a core gameplay loop. Containers grant the ability to carry loot, but come with movement penalties and ergonomic downsides.

---

## 1. Backpacks

The primary method of bulk transport.

### Tier Examples

| Backpack Name        | Grid Size | Capacity | Speed Penalty | Profile | Notes                                       |
| :------------------- | :-------- | :------- | :------------ | :------ | :------------------------------------------ |
| **Sling Bag**        | 2x3 (6)   | 6 cells  | 0%            | Tiny    | Starter gear. No penalty.                   |
| **Berkut / Scav BP** | 4x5 (20)  | 20 cells | -3%           | Medium  | Standard issue. Good balance.               |
| **Tri-Zip**          | 5x6 (30)  | 30 cells | -10%          | Large   | Combat bag. Visible over cover.             |
| **Raid Backpack**    | 6x8 (48)  | 48 cells | -25%          | Massive | "Camel" profile. Severe turn speed penalty. |

### Mechanics
*   **Quick Drop:** Double-tapping `Z` (default) instantly drops the backpack to regain combat speed.
*   **Nesting:** Can put smaller bags inside big bags. *Restrictions apply to prevent infinite stacks.*

---

## 2. Tactical Rigs (Vests)

Worn on the chest. The **only** container from which weapons can reload magazines.

### Layout Logic
Rigs are defined by their slot configurations.
*   **1x1 Slot:** Grenades, loose ammo, meds.
*   **1x2 Slot:** Standard 30-round magazines.
*   **2x2 Slot:** Drum mags, large meds, helmets.
*   **1x3 Slot:** Extended magazines (45-60 rnd).

### Types
1.  **Recon Rigs:** High ergonomics, small capacity (10-14 slots), lightweight.
2.  **Assault Rigs:** Balanced (16-20 slots), medium weight.
3.  **Heavy Rigs:** Massive capacity (24+ slots), allows 2x2 drums, big movement penalty.
4.  **Armored Rigs:** See [Armor Section](Armor.md). Combines protection with storage.

---

## 3. Secure Containers

Unlootable storage. Items here are kept after death.

*   **Alpha (2x2):** Default. Good for a keytool + spare meds.
*   **Beta (2x3):** Mid-tier upgrade.
*   **Gamma/Kappa (3x3 / 3x4):** End-game goal. Allows carrying a "Survival Kit" (Surgery) + expensive ammo stacks.

**Restrictions:**
*   Cannot place Guns, Thermal Scopes, or Night Vision inside during a raid (prevents "hiding" gear when about to die).
*   Can always remove items *from* it.

---

## 4. Storage Cases (Stash Only)

Specialized containers to organize the player's global inventory (Stash).

*   **Weapon Case:** 5x2 (10) External -> 10x5 (50) Internal. *Only holds weapons.*
*   **Money Case:** Holds cash stacks (500k -> 50M capacity).
*   **Medcase:** Holds medical supplies.
*   **Lucky Scav Junkbox:** Very large capacity, but only accepts "Barter/Crafting" items.
*   **Keytool:** 1x1 item -> Holds 16 keys. Essential for key management.
