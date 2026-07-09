---
title: "giáp & Ballistics"
weight: 1
type: docs
---

## giáp hệ thống Philosophy

giáp in our game được thiết kế để be realistic và simulation-heavy, not just a flat damage reduction percentage. It acts as a physical barrier that projectiles must penetrate to deal damage.

## giáp Classes (Tier hệ thống)

We follow a 6-tier classification hệ thống (GOST standard equivalent):

| Class | Stops đạn Type     | Example Threat                     | Protection Level         |
| :---- | :------------------ | :--------------------------------- | :----------------------- |
| **1** | Pistol / Buckshot   | 9x18mm, 12ga Buckshot              | Very Low (Ricochet only) |
| **2** | High-Power Pistol   | 9x19mm PST, .45 ACP                | Low                      |
| **3** | Intermediate (Soft) | 5.54x39mm (Basic), 5.56x45mm (FMJ) | Medium (Anti-Scav)       |
| **4** | AP Rifle            | 7.62x39mm PS, 5.56x45mm M855       | High (Standard Military) |
| **5** | Heavy AP            | 7.62x54mm LPS, M855A1              | Very High (Elite)        |
| **6** | Anti-Materiel       | .338 Lapua, 7.62x54mm SNB          | Extreme (Juggernaut)     |

### Mapping giáp Class to Display giá trị

For UI, economy, và legacy compatibility, giáp class maps to a **display giá trị** và **headshot reduction**. Ballistics và penetration cách dùng **Class** và durability; display/tooltips can show giá trị. Xem [Caliber & Ballistics hệ thống](../../vũ khí/Caliber_Ballistics_System.md) for penetration math.

| Class | giáp giá trị (Display) | Headshot Reduction | Typical Pen Threshold (PP) |
| :---- | :-------------------: | :----------------: | :-----------------------: |
| 1     | 15                    | 10%                | PP &lt; 10                |
| 2     | 30                    | 25%                | PP &lt; 20                |
| 3     | 50                    | 40%                | PP &lt; 35                |
| 4     | 75                    | 50%                | PP &lt; 45                |
| 5     | 90                    | 55%                | PP &lt; 55                |
| 6     | 100                   | 60%                | PP &lt; 65                |

Full item specs (per-vest, per-helmet) are in [giáp Master Database](Armor_Master_Database.md).

## Hitboxes & Coverage Zones

giáp does not cover the entire torso magically. It protects cụ thể **Collider Zones**.

### Body giáp Zones
1.  **Thorax (Upper Chest):** Vital zone. 0 HP = Death.
2.  **Stomach:** Non-vital. 0 HP = High dehydration/energy loss + "coughing" (noise).
3.  **Sides/Ribs:** Often unprotected by Plate Carriers, protected by Soft giáp wraps.
4.  **Neck:** Lethal zone. Requires cụ thể "Neck Guard" attachments.

### Helmet Zones
1.  **Top of Head:** Standard helmet coverage.
2.  **Nape (Back):** Protected by most military helmets.
3.  **Ears:** Requires helmets với ear guards (often blocks headsets).
4.  **Eyes/Jaws:** Requires **Face Shield** (Glass) hoặc **Mandible**.
    *   *Visors:* Have their own giáp Class (usually lower, 1-3). Cracks obscure vision khi hit.

## Material Properties

Material determines durability loss và repair efficiency.

| Material      | Durability | Repairability | Weight     | Destructibility    |
| :------------ | :--------- | :------------ | :--------- | :----------------- |
| **Aramid**   | Low        | Great         | Very Light | Low                |
| **UHMWPE**   | High       | Good          | Light      | Medium             |
| **Titanium** | High       | Good          | Medium     | Low                |
| **Aluminium**| Medium     | Bad           | Medium     | High               |
| **Steel**    | Very High  | Very Good     | Heavy      | Low                |
| **Ceramic**  | High       | Terrible      | Medium     | Extreme (Shatters) |

## Damage cơ chế

### 1. Penetration Check
khi a bullet hits giáp, the server compares **Bullet Penetration Power** vs. **giáp hiện tại Durability %** & **Class**.
*   **kết quả A (Penetration):** Bullet passes thông qua. Damage is reduced by ~10-40% depending on residual energy. giáp takes durability damage.
*   **kết quả B (Block):** Bullet is stopped. giáp takes significant durability damage.

### 2. Blunt Damage
Even nếu a bullet is stopped, the impact transfers energy.
*   **Calculation:** `Damage * BluntFactor * (1 - Durability%)`
*   kết quả: người chơi takes 1-5 HP damage và minor stamina drain even on non-pen.

### 3. Ricochet
Helmets (và some giáp) have a `Ricochet Chance` (Low/Med/High). Even a high-pen bullet can bounce off a round helmet at a shallow angle, causing "concussion" (ringing ears, blurry vision) nhưng 0 HP damage.

## Armored Rigs

Some **tactical rigs** include built-in giáp (armored rigs). They occupy the rig slot và provide both storage và body protection; they replace a separate body giáp vest. For grid layout, slot count, và hotkey mapping Xem [Storage Gear — Storage Master Database](../StorageGear/Storage_Master_Database.md) và [Storage Slot Layouts](../StorageGear/Storage_Slot_Layouts.md). For giáp class, zones, và material of each armored rig, Xem [giáp Master Database](Armor_Master_Database.md#armored-rigs).
