---
title: "Tutorial Raid: Operation Zero"
type: docs
---

## Overview

Operation Zero is the first guided raid. It teaches extraction fundamentals through a controlled mission rather than a menu tutorial.

The tutorial should feel like the player's first mission, not a disconnected training room. It introduces risk, loot, combat, map reading, and extraction in a protected sequence so the player understands why the game is tense before they face real loss.

The design goal is confidence, not mastery. A new player should leave Operation Zero knowing how to move, loot, survive a simple fight, find extraction, and understand the post-match screen. Advanced economy, ranked, market, and deep squad rules can wait.

## Tutorial Goals

Each goal should be taught through action. The player learns looting by choosing what to pick up, not by reading a paragraph. The player learns extraction by carrying something valuable while the timer is visible, not by watching a cinematic.

| Goal | Player Learns |
| :--- | :--- |
| Move and camera | How to navigate top-down spaces |
| Loot | Why items matter and how inventory works |
| Combat | Cover, aim, abilities, and damage feedback |
| Map and pings | How to read objectives and extraction markers |
| Extraction | Why leaving alive matters |
| Debrief | How rewards, loss, stash, and next steps work |

## Tutorial Onboarding Model

Operation Zero should teach the raid loop in the same order the player will use it in normal play. The tutorial can protect the player from permanent loss, but it should not hide the existence of risk.

| Teaching Goal | Player Action | UI Support | Fail-Safe | Pass Condition | Next Unlock |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Movement and camera | Move through crash site, rotate/aim camera, use cover path | Objective marker, soft boundary, camera hint | Reset to last checkpoint if stuck | Reach first marker | Loot container |
| Looting and value | Search container, compare item, place in backpack | Loot panel, value badge, capacity hint | Pause threat while first loot panel is open | Take required item or skip with confirmation | Inventory lesson |
| Inventory basics | Move, rotate, equip, consume, and protect one item | Highlight valid slots, show blocked placement reason | Auto-place tutorial item after repeated failure | Inventory has required item in valid location | Combat encounter |
| Combat and cover | Fight simple AI using cover, reload, and ability | Enemy intent cue, hit feedback, health/armor HUD | Enemy accuracy reduced after repeated deaths | Enemy defeated or bypassed via taught route | Healing lesson |
| Healing and status | Use medkit after scripted damage | Status icon, quick-slot hint, safe cover | Damage stops until healed | Health stabilized | Map/objective lesson |
| Map and objective | Open map, read extraction/objective marker, set waypoint | Pulsing objective, extract marker, route hint | Re-ping objective after delay | Player follows route | Timed extraction |
| Extraction timer | Activate extraction, hold zone, defend or wait | Countdown, zone boundary, audio cue | Retry from nearby checkpoint if interrupted | Extraction completes | Debrief |
| Debrief and stash | Read outcome, move reward to stash, see next deploy CTA | Guided debrief, stash highlight, deploy path | No permanent loss, no blocking overflow | Player reaches Safe House onboarding | Standard queue |

## Mission Flow

The mission flow should escalate pressure gradually. Early steps are safe and explicit. Mid steps introduce enemies and inventory choices. The final extraction step adds time pressure but still allows checkpoint recovery if the player fails.

| Step | Phase | Teaches | Failure Policy | Unlocks |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Operator Selection | Class identity and ability preview | Cannot fail | Crash Site |
| 2 | Crash Site | Movement, camera, objective marker | Soft reset | Scavenger Camp |
| 3 | Scavenger Camp | Combat, cover, ability use | Retry checkpoint | Bunker |
| 4 | Bunker | Looting, inventory, item value | Guided prompts | Map and Pings |
| 5 | Map and Pings | Minimap, waypoint, squad signal | Repeat prompt | Timed Extraction |
| 6 | Timed Extraction | Timer, danger, reward | Retry checkpoint | Custom Debrief |
| 7 | Custom Debrief | Rewards, stash, and next step | Cannot fail | Safe House Onboarding |

## Tutorial Failure And Recovery Rules

Tutorial failure is allowed only when it teaches the next attempt. It should never create account loss, lock the player in repeated long sections, or obscure why the player failed.

| Failure | Recovery | Copy Requirement |
| :--- | :--- | :--- |
| Player dies in combat | Restart at combat checkpoint with ammo/health restored | Explain cover, healing, or reload lesson |
| Player runs out of ammo | Spawn tutorial ammo and highlight reload | "Pick up ammo and reload before pushing." |
| Player cannot solve inventory placement | Offer auto-place after two failed attempts | "Auto-place item" must be optional |
| Player misses extraction timer | Restart near extraction with route hint | "Stay inside the zone until timer completes." |
| Player disconnects | Resume tutorial checkpoint, not MIA | "Tutorial progress restored." |
| Player skips tutorial | Allowed only for returning accounts or explicit skip path | Show which systems may still be unfamiliar |

## First Real Raid Handoff

After Operation Zero, the first standard raid should feel familiar but no longer protected. The handoff must show what changes:

| System | Tutorial | First Standard Raid |
| :--- | :--- | :--- |
| Gear loss | No permanent loss | Loadout can be lost |
| Enemy pressure | Scripted AI only | PvPvE with real players |
| Extraction | Guided route and retry | Multiple extracts, no checkpoint retry |
| Loot | Curated items | Full loot table and FIR rules |
| Death | Checkpoint recovery | KIA/MIA debrief and rebuild |
| Matchmaking | Training pool | Soft protected standard pool for early raids |

## Starter Kit

The starter kit should support the first real raid without removing early scarcity. It gives the player enough tools to try again, but not enough value to skip learning the economy, insurance, or loadout preparation.

| Item | Purpose |
| :--- | :--- |
| Basic weapon | Enables first real raid |
| Light armor | Reduces early frustration |
| Medkit | Teaches recovery |
| Small backpack | Teaches loot capacity |
| Credits | Lets player buy a small upgrade |

## Anti-Frustration Rules

Anti-frustration rules are strongest in the tutorial because the player has not yet chosen risk. Once the player enters normal raids, loss can become meaningful. During Operation Zero, failure should teach and reset quickly.

| Rule | Reason |
| :--- | :--- |
| No permanent loss during tutorial | Avoid first-session punishment |
| Checkpoints after each lesson | Reduces repetition |
| Clear objective marker | Prevents navigation failure |
| Optional reminders | Helps new mobile players |
| Skip option for returning players | Respects experienced players |

## Tutorial Examples

The first loot interaction should give the player a small but visible reward, then show how that item appears in inventory. The lesson is value recognition, not inventory mastery.

The first combat encounter should use cover and readable enemy behavior. The player should learn that positioning matters before facing real PvP pressure.

The extraction finale should make the player carry something worth saving. The timer, marker, and audio cue should teach why leaving alive is the point of the genre.

## Tutorial Failure Cases

- If players can finish without understanding extraction, the mission teaches the wrong genre.
- If prompts solve every step automatically, players leave without confidence.
- If failure repeats long sections, frustration replaces learning.
- If experienced players cannot skip or accelerate, replay friction increases.

## Tutorial QA Checklist

- Player can move, aim, loot, heal, open map, activate extraction, and read debrief without external instruction.
- Player sees at least one valuable item before extraction so the genre promise is clear.
- Player understands tutorial loss protection does not apply to normal raids.
- Tutorial can be resumed after disconnect without MIA or gear loss.
- Skip/replay rules are visible and do not block returning players.
- First standard raid deploy screen repeats gear loss, insurance, and extraction stakes.

## Cross-References

| Topic | Page |
| :--- | :--- |
| Core loop | [Core Gameplay](coregameplay/index.html) |
| Controls | [Controls](controls/index.html) |
| Loadout onboarding | [Loadout Preparation](loadoutpreparation/index.html) |
| Safe House | [Safe House Design](safe_house_design/index.html) |
| Accessibility | [Accessibility](accessibility/index.html) |
