---
title: "Gameplay"
linkTitle: "Gameplay"
type: docs
weight: 1
---

##  Gameplay Systems

Core mechanics defining the moment-to-moment experience: movement, combat, interaction, and progression.

{{< cards cols="2" >}}
  {{< card link="CharacterSystem" title="Character System" icon="user" subtitle="Operator classes, abilities, attributes (Health, Stamina), and state machines." >}}
  {{< card link="WeaponSystem" title="Weapon System" icon="fire" subtitle="Ballistics, attachments, recoil patterns, and damage models." >}}
  {{< card link="InventorySystem" title="Inventory System" icon="briefcase" subtitle="Grid-based inventory, looting, stash management, and item data." >}}
  {{< card link="ControlSystem" title="Control System" icon="cursor-click" subtitle="Input abstraction, movement logic, and cross-platform controls." >}}
{{< /cards >}}

---

### Key Concepts

*   **Ability System:** Built on GAS (Gameplay Ability System) for modularity.
*   **Server Authoritative:** All critical gameplay logic (damage, movement, loot) runs on the server.
*   **Data-Driven:** Weapons, items, and abilities are defined via Data Assets for easy tuning.
