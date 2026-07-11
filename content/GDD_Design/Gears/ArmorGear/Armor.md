---
title: "Armor & Ballistics"
weight: 1
type: docs
---

## Armor System Philosophy

Armor in our game is designed to be realistic and simulation-heavy, not just a flat damage reduction percentage. It acts as a physical barrier that projectiles must penetrate to deal damage.

## Armor Classes (Tier System)

We follow a 6-tier classification system (GOST standard equivalent):

| Class | Stops Ammo Type     | Example Threat                     | Protection Level         |
| :---- | :------------------ | :--------------------------------- | :----------------------- |
| **1** | Pistol / Buckshot   | 9x18mm, 12ga Buckshot              | Very Low (Ricochet only) |
| **2** | High-Power Pistol   | 9x19mm PST, .45 ACP                | Low                      |
| **3** | Intermediate (Soft) | 5.54x39mm (Basic), 5.56x45mm (FMJ) | Medium (Anti-Scav)       |
| **4** | AP Rifle            | 7.62x39mm PS, 5.56x45mm M855       | High (Standard Military) |
| **5** | Heavy AP            | 7.62x54mm LPS, M855A1              | Very High (Elite)        |
| **6** | Anti-Materiel       | .338 Lapua, 7.62x54mm SNB          | Extreme (Juggernaut)     |

### Mapping Armor Class to Display Value

For UI, economy, and legacy compatibility, armor class maps to a **display value** and **headshot reduction**. Ballistics and penetration use **Class** and durability; display/tooltips can show Value. See [Caliber & Ballistics System](../../weapons/caliber_ballistics_system/index.html) for penetration math.

| Class | Armor Value (Display) | Headshot Reduction | Typical Pen Threshold (PP) |
| :---- | :-------------------: | :----------------: | :-----------------------: |
| 1     | 15                    | 10%                | PP &lt; 10                |
| 2     | 30                    | 25%                | PP &lt; 20                |
| 3     | 50                    | 40%                | PP &lt; 35                |
| 4     | 75                    | 50%                | PP &lt; 45                |
| 5     | 90                    | 55%                | PP &lt; 55                |
| 6     | 100                   | 60%                | PP &lt; 65                |

Full item specs (per-vest, per-helmet) are in [Armor Master Database](armor_master_database/index.html).

## Hitboxes & Coverage Zones

Armor does not cover the entire torso magically. It protects specific **Collider Zones**.

### Body Armor Zones
1.  **Thorax (Upper Chest):** Vital zone. 0 HP = Death.
2.  **Stomach:** Non-vital. 0 HP = High dehydration/energy loss + "coughing" (noise).
3.  **Sides/Ribs:** Often unprotected by Plate Carriers, protected by Soft Armor wraps.
4.  **Neck:** Lethal zone. Requires specific "Neck Guard" attachments.

### Helmet Zones
1.  **Top of Head:** Standard helmet coverage.
2.  **Nape (Back):** Protected by most military helmets.
3.  **Ears:** Requires helmets with ear guards (often blocks headsets).
4.  **Eyes/Jaws:** Requires **Face Shield** (Glass) or **Mandible**.
    *   *Visors:* Have their own Armor Class (usually lower, 1-3). Cracks obscure vision when hit.

## Material Properties

Material determines durability loss and repair efficiency.

| Material      | Durability | Repairability | Weight     | Destructibility    |
| :------------ | :--------- | :------------ | :--------- | :----------------- |
| **Aramid**   | Low        | Great         | Very Light | Low                |
| **UHMWPE**   | High       | Good          | Light      | Medium             |
| **Titanium** | High       | Good          | Medium     | Low                |
| **Aluminium**| Medium     | Bad           | Medium     | High               |
| **Steel**    | Very High  | Very Good     | Heavy      | Low                |
| **Ceramic**  | High       | Terrible      | Medium     | Extreme (Shatters) |

## Damage Mechanics

### 1. Penetration Check
When a bullet hits armor, the server compares **Bullet Penetration Power** vs. **Armor Current Durability %** & **Class**.
*   **Result A (Penetration):** Bullet passes through. Damage is reduced by ~10-40% depending on residual energy. Armor takes durability damage.
*   **Result B (Block):** Bullet is stopped. Armor takes significant durability damage.

### 2. Blunt Damage
Even if a bullet is stopped, the impact transfers energy.
*   **Calculation:** `Damage * BluntFactor * (1 - Durability%)`
*   Result: Player takes 1-5 HP damage and minor stamina drain even on non-pen.

### 3. Ricochet
Helmets (and some armor) have a `Ricochet Chance` (Low/Med/High). Even a high-pen bullet can bounce off a round helmet at a shallow angle, causing "concussion" (ringing ears, blurry vision) but 0 HP damage.

## Armored Rigs

Some **tactical rigs** include built-in armor (armored rigs). They occupy the rig slot and provide both storage and body protection; they replace a separate body armor vest. For grid layout, slot count, and hotkey mapping see [Storage Gear — Storage Master Database](../storagegear/storage_master_database/index.html) and [Storage Slot Layouts](../storagegear/storage_slot_layouts/index.html). For armor class, zones, and material of each armored rig, see [Armor Master Database](Armor_Master_Database.md#armored-rigs).
