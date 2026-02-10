---
title: "Consumables & Meds"
weight: 4
type: docs
---

## Medical System

Health is limb-based, not just a total HP pool. Different injuries require specific medical items.

### Injury Types
1.  **Light Bleeding:** Lose HP slowly. Leaves blood trail.
    *   *Fix:* Bandage.
2.  **Heavy Bleeding:** Lose HP fast. Screen desaturates.
    *   *Fix:* Tourniquet / Hemostat. (Bandages barely help).
3.  **Fracture:**
    *   *Leg:* Can't run, limping (loud).
    *   *Arm:* Shaky aim, slow searching.
    *   *Fix:* Splint.
4.  **Blacked Limb (0 HP):**
    *   Limb is useless. Taking damage to it spreads to other body parts (Damage multiplier).
    *   *Fix:* Surgical Kit (CMS/Surv12). Reduces max HP of that limb.
5.  **Pain/Tremor:** Blurry vision.
    *   *Fix:* Painkillers.

### Med Item Types

| Item              | Slot Size | Capacity (HP) | Use Time | Cures                              |
| :---------------- | :-------- | :------------ | :------- | :--------------------------------- |
| **Aisle Bandage** | 1x1       | -             | 2s       | Light Bleed                        |
| **Army Bandage**  | 1x1       | -             | 2s       | Light/Heavy Bleed (2 charges)      |
| **Cheese (AI-2)** | 1x1       | 100           | 2s       | HP Only (No bleed fix)             |
| **Car FAK**       | 1x2       | 220           | 3s       | HP, Light Bleed                    |
| **Salewa Kit**    | 1x2       | 400           | 3s       | HP, Light/Heavy Bleed              |
| **Grizzly Kit**   | 2x2       | 1800          | 5s       | Everything (HP, Bleeds, Fractures) |
| **Analgin**       | 1x1       | 4 uses        | 1s       | Pain (Effect: 200s)                |
| **Morphine**      | 1x1       | 1 use         | instant  | Pain (Effect: 400s)                |

---

## Stimulants (Combat Drugs)

Injectors usually provide strong buffs with delayed debuffs (side effects).

*   **Green Stim (Regen):** Heals HP over time. *Side effect: High energy drain.*
*   **Blue Stim (Stamina):** Infinite stamina for 60s. *Side effect: Hand tremors.*
*   **Purple Stim (M.U.L.E):** Increases carry weight limit by +50%. *Side effect: You take damage over time.*
*   **Propital:** Removes pain + slight regen. Common combat stim.

---

## Food & Hydration

Survival mechanics.

*   **Energy (Food):** Drops over time. At 0, stamina doesn't regen, health ticks down.
    *   *Items:* Tushonka, Crackers, MRE.
*   **Hydration (Drink):** Drops faster than energy. Heavy armor/activity drains it faster. At 0, rapid death.
    *   *Items:* Water Bottle, Juice, Milk.
*   **Metabolism:**
    *   Eating dry food (Crackers) reduces Hydration.
    *   Taking painkillers reduces Hydration.
    *   Stomach blacked out = Rapid energy/hydration loss.
