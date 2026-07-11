---
title: "Safe House Design"
linkTitle: "Safe House"
type: docs
weight: 16
---

## Overview

The Safe House is the player's persistent out-of-raid base. It gives context to stash growth, crafting, upgrades, insurance claims, and long-term identity.

The Safe House should make out-of-raid progress feel grounded. Instead of presenting stash, crafting, traders, and insurance as disconnected menus, it frames them as parts of a base the player improves over time. This gives economic sinks a fiction and gives the player a place to return after success or failure.

The system should support long-term goals without blocking normal play. Upgrades can create efficiency, identity, and new options, but a player should not feel unable to raid because a module is incomplete.

## Module Dependency

Dependencies should teach the base gradually. Early modules support basic storage and claims. Powered modules introduce crafting and repairs. Radio-linked modules connect the player to factions, traders, and world events.

| Parent / Requirement | Module | Purpose |
| :--- | :--- | :--- |
| Safe House | Stash Room | Storage, sorting, and inventory expansion |
| Safe House | Generator | Powers advanced modules |
| Generator | Workbench | Crafting, repair, and modification support |
| Generator | Medical Station | Recovery and medical crafting support |
| Safe House | Radio | Faction contact and world updates |
| Radio | Trading Post | Trader access and insurance inbox context |
| Stash Room | Workbench | Supplies materials for crafting and upgrades |

## Functional Areas

Each area should have one obvious job. If a player wants to claim insurance, the Trading Post should be the answer. If they want to repair gear, the Workbench should be the answer. Avoid scattering the same action across multiple rooms unless there is a clear shortcut.

| Area | Purpose | Player Action |
| :--- | :--- | :--- |
| Stash Room | Inventory storage and sorting | Store, filter, expand |
| Trophy Vault | Identity and achievement display | View trophies, inspect milestones |
| Workbench | Crafting and repairs | Build, modify, repair |
| Radio | Faction contact and event briefing | Accept tasks, hear world updates |
| Trading Post | Traders and insurance inbox | Buy, sell, claim returns |
| Operator Lounge | Home screen context | Select operator, view status |

## Upgrade Rules

Upgrade rules protect motivation. Players should know what an upgrade changes before spending resources, and locked modules should show a visible path forward. Seasonal wipe policy must be announced early because base progression can represent significant player investment.

| Rule | Requirement |
| :--- | :--- |
| Clear benefit | Every module upgrade must state what changes |
| Economy sink | Upgrades consume credits, items, or reputation |
| No paid-only power | Upgrade materials must be earnable |
| Readable dependency | Locked modules show prerequisite path |
| Seasonal policy | Wipe behavior must be explicit before season launch |

## Out-Of-Raid Operator State

Operator state can add texture to recovery, but it should not become a punishment stack. Health, cooldown, and readiness systems should encourage planning and varied operators, not force players to wait instead of playing.

| State | Purpose | Notes |
| :--- | :--- | :--- |
| Health | Recovery pacing | Avoid excessive downtime |
| Energy / hydration | Light planning pressure | Optional depending on hardcore tuning |
| Cooldown | Prevent instant reuse after severe failure | Should not block all play |
| Morale / readiness | Future flavor system | Cosmetic or narrative first |

## Safe House Examples

After a failed raid, the player returns to claim insurance, repair damaged gear, and rebuild from stash. The Safe House should make that recovery loop feel intentional instead of like menu cleanup.

After a successful raid, the player sorts loot, starts a craft, upgrades a module, and chooses what to risk next. This converts extraction value into long-term identity and planning.

During a season event, the Radio can surface faction updates and event objectives while the Trading Post handles reward claims. The player should understand where seasonal actions live.

## Safe House Failure Cases

- If upgrades feel mandatory before normal raids, progression pressure is too high.
- If the same action appears in too many rooms, navigation becomes confusing.
- If stash expansion feels paid-only, monetization trust is damaged.
- If seasonal wipe policy is unclear, players may avoid investing in upgrades.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Economy sinks | [Economy](economy/index.html) |
| Insurance inbox | [Insurance System](insurancesystem/index.html) |
| Home Screen relation | [Home Screen & Lobby](homescreen_design/index.html) |
| Progression unlocks | [Progression](progression/index.html) |
