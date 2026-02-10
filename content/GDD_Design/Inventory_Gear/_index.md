---
title: "Inventory & Gear Systems"
linkTitle: "Inventory & Gear"
type: docs
weight: 60
---

## 1. Inventory Philosophy

**Core Design Pillars:**
1.  **"Tetris" Spatial Management:** Inventory space is a puzzle. Items have physical dimensions (e.g., a 1x1 grenade vs. a 2x5 sniper rifle) requiring spatial reasoning to organize efficiently.
2.  **Weight Consequences:** Everything has mass. Overburdening drastically affects stamina, inertia, and movement speed, ensuring players cannot perform "Call of Duty movement" while carrying 60kg of loot.
3.  **Risk-Reward Loadout:** Bringing high-tier gear increases survival odds but risks significant economic loss on death.
4.  **Tactical Ergonomics:** Access to items is governed by where they are stored. Magazines in a backpack cannot be unused for a quick reload; they must be in a Tactical Rig or Pockets.

**References:** *Escape from Tarkov, Arena Breakout, Delta Force: Hawk Ops, Gray Zone Warfare.*

---

## 2. The Character Loadout (Paper Doll)

The primary interface for equipping the character before a raid. It visually represents the operator with specific slots surrounding their 3D model.

### Equipment Slots Breakdown

| Slot Name            | Grid Size | Hotkey Accessible? | Function & Notes                                                                                   |
| :------------------- | :-------- | :----------------- | :------------------------------------------------------------------------------------------------- |
| **Headset**          | 1 slot    | No                 | **Critical:** Modifies audio mix. Compresses gunshots and amplifies footsteps.                     |
| **Helmet**           | 2x2 (typ) | No                 | Provides protection to specific **Hitboxes** (Top, Nape, Ears, Eyes, Jaws). Can mount NVGs/Visors. |
| **Face Cover**       | 1 slot    | No                 | Hides identity and reduces skin reflection. Some provide minor flash protection or low-tier armor. |
| **Body Armor**       | Variable  | No                 | *If equipping Armor Vest.* Protects Thorax/Stomach zones. Does NOT provide storage.                |
| **Tactical Rig**     | Variable  | **YES**            | Stores magazines/meds. Required for `R` reload. Can be *Armored* (replacing Body Armor slot).      |
| **Primary 1**        | Weapon    | **YES (1)**        | Main weapon on sling.                                                                              |
| **Primary 2**        | Weapon    | **YES (2)**        | Secondary main weapon on back. Harder to switch to.                                                |
| **Sidearm**          | Weapon    | **YES (3)**        | Pistol in holster. Fastest switch speed.                                                           |
| **Scabbard**         | Weapon    | **YES (V)**        | Melee weapon. Used for breaking glass or silent kills.                                             |
| **Pockets**          | 4x1 (typ) | **YES (4-0)**      | Built-in storage. Good for keys, loose meds. Hotkey assignments (`4`, `5`...).                     |
| **Backpack**         | Variable  | No                 | Main loot storage. Items here **cannot** be quick-used.                                            |
| **Secure Container** | Variable  | No                 | Gear is safe even on death. *Anti-Abuse:* Cannot place weapons/thermal scopes inside in-raid.      |
| **Armband**          | 1 slot    | No                 | purely cosmetic/identification.                                                                    |

---

## 3. The Equipment System

### Armor & Ballistics Mechanics
Armor is not a simple health bar; it protects specific *zones* on the body.

*   **Armor Class (Tier):** Determines penetration resistance.
    *   *Class 1-2:* Protects against shrapnel, pistols.
    *   *Class 3-4:* Standard rifle protection.
    *   *Class 5-6:* High-end AP protection.
*   **Coverage Zones:** An armor vest might protect the "Trauma Plate" area (Heart/Lungs) heavily but leave the "Soft Armor" area (Stomach/Sides) with lower protection.
*   **Materials:**
    *   *Ceramic:* High protection but breaks rapidly (low durability). Cheap repairs.
    *   *Steel:* Heavy, high durability, repairs well.
    *   *Aramid/Kevlar:* Low protection, high durability (Soft armor).
*   **Blunt Damage:** Even if a bullet doesn't penetrate, the impact causes minor damage (bruising) based on the armor's material softness.

### Tactical Rigs vs. Armored Rigs
Players must choose between flexibility and efficiency.

1.  **Chest Rig (Unarmored):**
    *   Worn *over* Body Armor.
    *   Purely for storage (Ammo/Meds).
    *   *Advantage:* Can swap Rigs without losing protection. High slot count.
2.  **Armored Rig:**
    *   Combines Armor + Storage.
    *   Occupies *Body Armor* slot (cannot wear Vest + Armored Rig).
    *   *Advantage:* lighter weight than separate combo, good for budget runs.
    *   *Disadvantage:* Usually lower durability and fewer slots than high-end separate combos.

### Headsets (Tactical Audio)
Sound is information. Headsets are considered "Meta" gear.

*   **Function:** Active noise cancelling.
    *   *Compression:* Reduces deafening sounds (Explosions, own Gunfire).
    *   *Amplification:* Boosts high-frequency ambient sounds (Footsteps on wood/metal, removing pins).
*   **Variety:** Different headsets have different EQ profiles (e.g., *GSSH-01* is crunchy/treble-heavy, *ComTac 4* is bassy/warm).

### Quick Slots & Hotkeys
*   **Interaction:** Dragging an item to the hotbar (4-9, 0) or hovering and pressing the number key.
*   **Requirement:** Item MUST be in **Pockets** or **Tactical Rig**.
*   **Backpack Limitation:** Items in backpack cannot be hotkeyed (simulates reaching behind back).
*   **Usage Types:**
    *   *Press:* Use item (Bandage).
    *   *Hold:* Inspection wheel / Throw mode (Grenades).
    *   *Double Tap:* Emergency use (Stim).

---

## 4. The Grid System Mechanics

### Item Physicality
*   **Dimensions:** Every item has `Width x Height`.
    *   *Examples:* 1x1 (Ammo), 1x2 (Mag), 2x2 (Helmet), 2x3 (Armor).
*   **Rotation:** Players can rotate items 90° (`R` key) to fit tight spaces.
*   **Stacking:**
    *   **Ammo:** Stacks based on caliber (e.g., 60 rounds/stack).
    *   **Currency:** Stacks up to 500k.
    *   **Trade Items:** Some small items (screws, bolts) do not stack to encourage bag fullness.

### Nesting (Bag-in-Bag)
*   **Rule:** Backpacks can be placed inside other backpacks if there is space.
*   **Restriction:** "Dimensional Slapping" prevents infinite loops. A container cannot be placed inside a container of the same ID grouping (e.g., can't put a *Beta Backpack* inside another *Beta Backpack* if it's full).
*   **Stacking Penalty:** Weight is cumulative. Stacking 10 bags calculates the weight of *all* bags + contents.

### Folding & Collapsing
*   **Weapons:** Stocks can be folded (Right-click -> Fold) to reduce width (e.g., `2x4` -> `2x3`).
*   **Stocks:** Folded weapons have horrible recoil/ergonomics if used in that state.
*   **Containers:** Empty backpacks can sometimes be "rolled" to take up less space (e.g., 3x3 rolled, 5x6 open).

---

## 5. Encumbrance & Math System

Total weight is the sum of all equipment + inventory contents.

**Base Stats (Reference):**
*   **Max Carry Weight (No Penalty):** 25kg
*   **Max Walking Weight:** 60kg
*   **Absolute Max:** 75kg

### Weight Threshold Penalties

| Weight Tier  | Range (kg) | Movement Speed | Sprint Stamina Drain | Inertia (Input Lag) | Jump Height           |
| :----------- | :--------- | :------------- | :------------------- | :------------------ | :-------------------- |
| **Light**    | 0 - 25     | 100%           | 1.0x (Normal)        | Low                 | 100%                  |
| **Medium**   | 25 - 40    | 85%            | 1.5x                 | Medium              | 75%                   |
| **Heavy**    | 40 - 55    | 60%            | 2.5x                 | High                | 40% (No Sprint Regen) |
| **Critical** | 55+        | 30%            | N/A (Cannot Sprint)  | Very High           | 0% (Cannot Jump)      |

*   **Inertia:** The time it takes to accelerate/decelerate. Heavy players feel "boat-like" and cannot "A-D strafe" effectively.
*   **Noise:** Heavier players make louder footsteps and gear-rattle noises.

---

## 6. In-Raid Interactions & UX

### Looting Mechanics
1.  **Vicinity Search:** When opening inventory (`Tab`), the UI shows a "Vicinity" pane on the left, displaying loose items on the floor within 1.5m.
2.  **Container Search:**
    *   Containers (Dead bodies, crates) start **Unsearched** (Content hidden, blacked out).
    *   **Action:** Player must click "Search". A progress bar runs (speed depends on Perception skill).
    *   **Reveal:** Items appear one by one as the bar fills.
3.  **Unknown Items:**
    *   New items appear with `?` icon.
    *   Must be "Examined" (Middle Click) to reveal identity and stats.
    *   Gains tiny XP amount.

### Shortcuts (Keybinds)
*   `Ctrl + Click`: Instant move to available open space (Loot -> Bag).
*   `Alt + Click`: Instant equip (Loot -> Body Slot).
*   `Del`: Drop item.
*   `R` (While Dragging): Rotate.
*   `Middle Mouse`: Examine / Fold Stock.

---

## 7. Weapon Modding (Gunsmith)

A dedicated UI for modifying weapons, distinct from the grid.

*   **Node System:** The gun is visually exploded into nodes (Receiver, Barrel, Muzzle, Stock, Grip, Mag).
*   **Compatibility Logic:**
    *   Ghost slots show valid attachments available in stash.
    *   Prevents conflicts (e.g., "Muzzle device blocks Suppressor").
*   **Live Stats:** Ergonomics and Recoil stats update real-time as parts are swapped.
*   **Preset Assembly:** Players can save "Meta Builds" and "Assemble" them instantly if they have the parts/money to buy them.

---

## 8. Stash Management (Meta-Game)

The "Stash" is the permanent inventory outside of raids.

*   **Grid Size:** Depends on Game Edition / Hideout Upgrades. Starts small (10x28), expands to huge (10x68).
*   **Containers (The Solution to Hoarding):**
    *   *Scav Junkbox:* massive internal space, but ONLY holds barter items.
    *   *Weapon Case:* Holds weapons/ammo.
    *   *Medcase:* Holds meds.
    *   *Keytool/Docs Case:* Tiny 1x1 or 1x2 items that hold many keys/maps.
*   **Auto-Sort:** A controversial button.
    *   *Logic:* Categories (Weapons top, Armor mid, Barter bottom) -> Size (Big to small).

## 9. Development Implementation Notes

*   **Data Structure:**
    ```json
    {
      "itemID": "guid_123",
      "tpl": "template_id_m4a1",
      "location": { "x": 0, "y": 0, "r": 0 }, // r = rotation (0: horizontal, 1: vertical)
      "parentId": "backpack_guid",
      "slotId": "main" // or "hideout", "pockets"
    }
    ```
*   **Validation:** Server must validate every move to prevent "item overlapping" or "weight hacking".
*   **Drag & Drop Library:** Use a robust grid library (e.g., Unreal's Slate DragDrop or Unity's `IDragHandler`) with strict cell-checking logic.
