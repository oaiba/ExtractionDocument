---
title: "Weapon Visual & Audio Identity"
type: docs
weight: 7
---

## Overview

This document specifies how weapons are read from the top-down camera: silhouettes, muzzle flash, attachment visibility, audio signatures, kill feedback, and rarity presentation. Design goal: every combat action is readable and distinct from overhead. See [Combat Feel (Top-Down)](../Gameplay/Combat_Feel_Topdown.md) for aim cone and feedback systems.

> **Cross-References:** [Weapon Arsenal](../Gameplay/WeaponArsenal.md) — weapon list; [Weapon Attachment System](../Gameplay/Weapon_Attachment_System.md) — attachment types; [Audio — Sound Design](../Audio/SoundDesign.md) — overall audio philosophy.

---

## Combat Readability Feedback Contract

Weapon presentation must communicate role and combat result under pressure. Visual/audio identity is not only flavor; it is how players learn what happened.

| Feedback Family | Required Signal | Accessibility Requirement |
| :--- | :--- | :--- |
| Weapon class identity | Silhouette, cadence, muzzle flash scale, reload sound | Must remain readable with colorblind-safe labels/icons in inspect UI |
| Flesh hit | Soft impact, short hit marker, blood/cloth VFX | Distinct from armor hit by sound/shape, not color alone |
| Armor hit | Hard plate sound, spark/debris, armor marker | Death recap names armor zone if relevant |
| No penetration / ricochet | Deflect sound, glancing VFX, no-pen marker | Do not use silence as feedback |
| Suppression | Directional audio pressure, slight visual stress | Duration and intensity limited; settings reduce motion/flash |
| Low ammo / reload | Click, mag animation, ammo counter state | Text or icon state supports audio cue |
| Kill confirmation | Clean confirmation appropriate to mode | Never hides ongoing threats or extraction state |

## UX Tell Priority

| Priority | Tell | Reason |
| :--- | :--- | :--- |
| 1 | Incoming lethal damage / downed / death cause | Survival and learning |
| 2 | Armor blocked / armor broke / no penetration | Trust in ammo and gear systems |
| 3 | Suppression / low ammo / reload | Moment-to-moment combat decisions |
| 4 | Weapon rarity / cosmetic flourish | Flavor only; must not obscure combat |

---

## Weapon Silhouette Guide

From the top-down camera, each weapon class must be distinguishable by **length**, **width**, and **profile** so players can identify threats at a glance.

| Weapon Class | Relative Length | Width / Profile | Distinct Cues |
| :----------- | :-------------- | :-------------- | :------------- |
| Pistol | Short | Narrow | Small rectangle; holstered on thigh when not wielded |
| SMG | Medium-short | Narrow | Compact; magazine visible under receiver |
| Assault Rifle | Medium-long | Medium | Barrel + stock; mag well visible |
| DMR | Long | Medium | Longer barrel; scope bulge if equipped |
| Shotgun | Medium (pump) to long (auto) | Medium-wide | Tube or box mag; pump forend on pump-actions |
| Sniper Rifle | Very long | Medium | Long barrel; large scope silhouette |
| LMG | Very long | Wide | Belt/box; bipod legs when deployed |
| Melee | Short (knife) to medium (axe) | Thin | Blade or haft; no muzzle |

**Rules:** Silhouette is drawn from the **wielded** weapon model (first-person or third-person asset projected to top-down). Scale is consistent: e.g. 1 m real length ≈ fixed pixel length at default zoom. No weapon should be indistinguishable from another within the same class (e.g. M4 vs HK416 can share approximate size but differ in stock/barrel shape if possible).

---

## Muzzle Flash Scaling

Muzzle flash reveals shooter position. Size and duration scale by weapon class and attachment state.

| Weapon Class | Base Flash Radius (top-down) | Duration | With Suppressor |
| :----------- | :--------------------------- | :------ | :--------------- |
| Pistol | 0.4 m (visual) | 2 frames | 80% reduction; minimal glow |
| SMG | 0.5 m | 2 frames | 80% reduction |
| AR | 0.6 m | 2–3 frames | 80% reduction |
| DMR | 0.55 m | 2 frames | 80% reduction |
| Shotgun | 0.7 m | 3 frames | 70% reduction (larger bore) |
| Sniper | 0.65 m | 3 frames | 80% reduction |
| LMG | 0.75 m | 3 frames | 75% reduction |

**Visibility range:** Muzzle flash is visible to other players within LOS up to 80 m (or per [Movement & Stamina](../Gameplay/Movement_and_Stamina.md) audio/visual range). Night or dark zones: flash visible at 2× range per [Environmental Hazards](../Gameplay/Environmental_Hazards.md). Suppressor reduces both sound and flash to avoid contradicting stealth.

---

## Attachment Visibility

Which attachments are visible from the top-down view when the weapon is wielded or on the ground.

| Attachment Slot | Visible from Top-Down | Notes |
| :-------------- | :-------------------- | :---- |
| Muzzle (suppressor, comp, brake) | Yes | Length change; suppressor extends barrel silhouette |
| Barrel (short, heavy, extended) | Partially | Length change visible; profile similar |
| Stock | Yes | Folded vs extended; heavy stock bulkier |
| Optics / sight | Yes | Scope tube and housing; red dot smaller |
| Underbarrel (grip, bipod, GL) | Yes | Grip and bipod legs; GL tube |
| Magazine | Yes | Drum vs stick; extended mag length |
| Laser / light | Yes (when active) | Laser dot on surface; light cone in dark |

**Ground loot:** Weapon on ground shows full silhouette including attachments. Rarity glow (see below) applies to weapon outline, not to each attachment separately.

---

## Audio Signature Per Weapon

Each weapon (or caliber family) has a **distinct report** so players can identify threat type by sound. Distance attenuation and occlusion apply.

| Caliber / Family | Report Character | Audible Range (approx) | Suppressed Range |
| :--------------- | :--------------- | :---------------------- | :--------------- |
| 9×19 / .45 pistol | Crack; short tail | 40 m | 12–16 m |
| 5.56 / 5.7 | Sharp crack; medium tail | 60 m | 20–25 m |
| 7.62×39 | Deeper thump; medium tail | 55 m | 18–22 m |
| 7.62×51 / 54R | Heavy crack; long tail | 70 m | 22–28 m |
| .338 / .50 | Very heavy; long tail | 90 m | 28–35 m |
| 12 Gauge | Boom; short tail | 50 m | 15–20 m |

**Rules:** Same caliber can share base sound with pitch/body variation per weapon (e.g. M4 vs HK416 slightly different). Reload, bolt cycle, and empty click are also distinct per weapon class. See [Audio — Sound Design](../Audio/SoundDesign.md) and [Tactical Audio](../Audio/TacticalAudio.md) for integration.

---

## Kill Feedback Design

Death animation and feedback vary by **killing weapon class** to reinforce weapon identity and satisfaction.

| Killing Weapon Class | Victim Feedback | Shooter Feedback |
| :------------------- | :-------------- | :--------------- |
| Shotgun | Knockback; heavy stagger; ragdoll possible at close range | Heavy impact sound; large hit marker |
| Sniper | Instant drop; minimal stagger; clean kill | Distinct kill sting; headshot chime if head |
| SMG | Stagger; multiple small hits | Rapid hit markers; kill confirm tone |
| AR | Moderate stagger; 2–4 hit reaction | Standard kill tone |
| LMG | Sustained stagger; suppression death | Sustained fire + final kill tone |
| DMR | 1–2 shot drop; moderate stagger | Precision kill tone |
| Pistol | Light stagger; slower collapse | Sidearm kill tone (different from primary) |
| Melee (backstab) | Instant collapse; silent | Satisfying "thunk"; no gun sound |

**Design intent:** Readable from top-down: player can tell "I was killed by a shotgun" or "I got headshot by a sniper" from feedback alone. No mystery deaths.

---

## Weapon Color-Coding (Rarity Glow)

**Ground loot and container contents:** Weapons display a **rarity outline or glow** so players can prioritize loot at a glance.

| Rarity | Color | Glow / Outline |
| :----- | :---- | :------------- |
| Common | White | No glow or subtle white outline |
| Uncommon | Green | Soft green outline |
| Rare | Blue | Blue outline |
| Epic | Purple | Purple glow |
| Legendary | Gold | Gold glow; subtle pulse |

**In-hand / equipped:** The weapon the player is holding does **not** show a rarity glow on the character model (immersion). Rarity is visible in HUD (weapon name, icon) and in inventory only.

**Enemy-held weapons:** No glow on enemy weapons (prevents "shoot the gold gun first" meta). Rarity is only visible on loot.

---

## Cross-References

- [Combat Feel (Top-Down)](../Gameplay/Combat_Feel_Topdown.md) — Hit markers, tracers, aim cone, suppression.
- [Weapon Arsenal](../Gameplay/WeaponArsenal.md) — Weapon list and categories.
- [Weapon Attachment System](../Gameplay/Weapon_Attachment_System.md) — Attachment types and slots.
- [Audio — Sound Design](../Audio/SoundDesign.md) — Gunshot and combat audio.
- [Environmental Hazards](../Gameplay/Environmental_Hazards.md) — Night and weather effects on visibility.
