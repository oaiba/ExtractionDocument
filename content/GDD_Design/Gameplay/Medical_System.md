---
title: "Medical System"
type: docs
---

## ⚕️ System Overview

The medical system in **Aethelgard** prioritizes realistic injury management over arcade-style HP regeneration. Players must diagnose the specific type of injury and apply the correct counter-measure.
*   **Body Part Health:** Total HP (e.g., 440) is divided into Head, Thorax, Stomach, Right Arm, Left Arm, Right Leg, Left Leg.
*   **No Auto-Regen:** Health does not recover over time without specific "Stimulant" buffs.
*   **Animation Lock:** Using medical items prevents shooting. Players must seek cover before treating.

---

## 🩸 Status Effects & Injuries

| Status Effect    | Visual/Audio Cue                                                 | Gameplay Impact                                                           | Treatment                                  |
| :--------------- | :--------------------------------------------------------------- | :------------------------------------------------------------------------ | :----------------------------------------- |
| **Light Bleed**  | Minor blood drips on HUD, persistent dripping sound.             | Drains 0.8 HP/sec distributed across all limbs.                           | Bandage, Army Bandage, Medkits.            |
| **Heavy Bleed**  | Heavy blood splatter on screen, gushing sound.                   | Drains 4.0 HP/sec. Leaves a visible blood trail for enemies.              | Tourniquet (Esmarch/CAT), Hemostat.        |
| **Fracture**     | Cracking sound on impact. Character gasps upon movement.         | **Leg:** Can't run, speed -45%. **Arm:** Aim unsteady, search speed -30%. | Splints (Alu/Grizzly).                     |
| **Pain**         | Vision blurs/tunnel vision. Character moans (audible to others). | Visual distortion. Tremors in aim.                                        | Analgesics (Pills, Injectors).             |
| **Blacked Limb** | Limb icon turns black/red.                                       | **Leg:** Limp (slow speed). **Stomach:** Rapid dehydration/energy loss.   | Surgical Kit (CMS/Surv12) to restore 1 HP. |
| **Contusion**    | Ringing ears (Tinnitus), muffled audio.                          | Cannot hear footsteps for 20-60s.                                         | None (Time decay) or specific Stims.       |

---

## 💊 Medical Items Master List

### 1. Bleeding Control (Stop the Drain)
| Item Name              | Use Time | Usage | Effect                                                 | Animation                     |
| :--------------------- | :------: | :---: | :----------------------------------------------------- | :---------------------------- |
| **Aseptic Bandage**    |   2.0s   |  1/1  | Cures Light Bleed.                                     | Wrapping gauze around limb.   |
| **Army Bandage**       |   2.0s   |  2/2  | Cures Light Bleed.                                     | Wrapping olive-drab dressing. |
| **Esmarch Tourniquet** |   5.0s   |  1/1  | Cures Heavy Bleed.                                     | Tightening red rubber strap.  |
| **CAT Tourniquet**     |   3.0s   |  1/1  | Cures Heavy Bleed.                                     | Cranking plastic windlass.    |
| **Hemostatic Syringe** |   2.0s   |  3/3  | Cures Heavy Bleed causing minimal fresh damage (10hp). | Injecting coagulant granules. |

### 2. Trauma Kits (Restore HP)
*Note: Kits can be used to stop bleeds but consume significantly more durability than dedicated items.*

| Item Name           | Use Time | Capacity | Special Properties                                  |
| :------------------ | :------: | :------: | :-------------------------------------------------- |
| **AI-2 ("Cheese")** |   2.0s   |  100 HP  | Fast use. **Cannot** stop bleeds.                   |
| **Car First Aid**   |   3.0s   |  220 HP  | Stops Light Bleed (consumes 40 HP).                 |
| **Salewa Kit**      |   3.0s   |  400 HP  | Stops Light (45) & Heavy Bleed (175).               |
| **IFAK**            |   3.0s   |  300 HP  | Compact (1 slot). Stops Light (30) & Heavy (210).   |
| **AFAK**            |   3.0s   |  400 HP  | Mil-Spec. Stops Light (30) & Heavy (170).           |
| **Grizzly Kit**     |   5.0s   | 1800 HP  | Medical Backpack Item. Heals Fractures, Bleeds, HP. |

### 3. Fracture & Surgery (Fix the Frame)
| Item Name               | Use Time | Usage | Effect                                                                          |
| :---------------------- | :------: | :---: | :------------------------------------------------------------------------------ |
| **Immobilizing Splint** |   3.0s   |  1/1  | Removes Fracture.                                                               |
| **Alu Splint**          |   3.0s   |  5/5  | Removes Fracture. Lightweight aluminum.                                         |
| **CMS Kit**             |  16.0s   |  5/5  | Restores Blacked Limb to 40% Max HP. **Cannot** perform surgery on Head/Thorax. |
| **Surv12 Field Kit**    |  20.0s   | 15/15 | Restores Blacked Limb to 80% Max HP. Heals Fractures too.                       |

### 4. Injectors & Pills (Pain Management)
| Item Name               | Duration | Hydration Cost | Effect                                               |
| :---------------------- | :------: | :------------: | :--------------------------------------------------- |
| **Analgin Painkillers** |   80s    |      -15       | Removes Pain. Cheap, blister pack.                   |
| **Ibuprofen**           |   280s   |       -5       | Removes Pain. Bottle with 15 uses.                   |
| **Golden Star Balm**    |   350s   |  -5 (+Energy)  | Removes Pain + Regenerates Energy.                   |
| **Morphine Injector**   |   300s   |      -10       | Instant use (no animation delay). Removes Pain.      |
| **Propital**            |   240s   |       -5       | Removes Pain + Passive Health Regen (1HP/sec).       |
| **Adrenaline**          |   60s    |      -20       | Removes Pain + Str/Endurance boost. +Recoil Control. |

---

## 🧬 Toxicity & Overdose Mechanics
*   **Toxicity:** Overusing Injectors adds "Toxin" to blood. High toxicity causes tremors and eventual damage.
*   **Overdose:** Using 2+ Painkillers simultaneously causes vision blurring and rapid dehydration (-4 Hydration/sec).

---
