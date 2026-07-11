---
title: "Combat Feel — Top-Down"
type: docs
weight: 19
---

## Overview

Combat in a top-down extraction shooter presents unique design challenges not present in FPS or third-person games. The overhead perspective changes how players perceive distance, cover, aim direction, and bullet travel. This document specifies the visual feedback systems, recoil model, cover interactions, suppression, and the overall combat feel targets that distinguish this game from its competitors.

> **Cross-References:** [Movement & Stamina](movement_and_stamina/index.html) — movement states during combat; [Gear Mechanics](gear_mechanics/index.html) — armor penetration, weapon tiers; [Hero Abilities](hero_abilities/index.html) — ability interactions with combat; [LOS, Fog & Visibility](los_fog_visibility/index.html) — LOS during combat; [Camera System](camera_system/index.html) — combat camera altitude (+1m boost); [Environmental Hazards](environmental_hazards/index.html) — weather effects on combat visibility.

---

## Combat Feel Targets

The core feel words for combat:

| Feel Target | Description |
| :---------- | :---------- |
| **Deliberate** | Shots have weight; full-auto spray is punished. Burst fire is king. |
| **Readable** | Every combat action is visually clear from overhead — no "mystery deaths." |
| **Tactical** | Cover matters. Flanking is rewarded. Rushing is punished. |
| **Consequential** | One mistake costs HP that is hard to recover. Death proximity is always felt. |
| **Satisfying** | Clear hit feedback, distinct kill feel, audible differences between weapon tiers. |

---

## Weapon Firing & Recoil

### Recoil in Top-Down Context

In a standard FPS, recoil manifests as camera kick — the screen moves up. In top-down, the character is viewed from above, so recoil is represented differently:

| Mechanic | FPS Implementation | Top-Down Implementation |
| :------- | :----------------- | :---------------------- |
| **Visual recoil** | Screen kick upward | Weapon "kick" animation (character model's arms pull back) |
| **Aim deviation** | Crosshair climbs | Crosshair jitters in a cone pattern; cone SIZE grows per shot |
| **Recoil pattern** | Vertical + horizontal drift | Full 360° cone bloom that expands per shot |
| **Recovery** | Mouse pull-down to compensate | Stop firing and wait for cone to close (no compensation needed) |

### Aim Cone Behavior

| State | Aim Cone Radius | Notes |
| :---- | :-------------- | :---- |
| Standing, not moving | 2° | Base accuracy |
| Crouching, stationary | 1° | Most accurate state |
| Prone, stationary | 0.5° | Pinpoint; very slow to move |
| Walking | 4° | Moderate; precision reduced |
| Sprinting | Cannot fire | Fire locked while sprinting |
| Full-auto fire (per bullet) | +0.5° per shot (up to 6° max) | Cone bloom accumulates |
| Post-burst (no fire, 1s) | Cone recovers at 3°/second | Release trigger = cone closes |

### Weapon Class Recoil Profiles

| Class | Base Cone | Full-Auto Bloom | Recovery Rate | Feel |
| :---- | :-------- | :-------------- | :------------ | :--- |
| Pistol | 2.5° | +0.3°/shot (max 5°) | 4°/s | Manageable; steady fire viable |
| Shotgun | 5° (fixed spread) | N/A (pump/semi) | Instant reset | Wide pattern; close range only |
| SMG | 2° | +0.4°/shot (max 7°) | 3°/s | Fast bloom, fast recovery |
| Assault Rifle | 2° | +0.5°/shot (max 6°) | 3°/s | Controlled bursts ideal |
| DMR | 1.5° | +0.8°/shot (max 4°, semi-auto) | 2°/s | Semi-auto precision |
| Sniper | 0.5° | N/A (bolt action) | Instant reset | Full reset between shots |
| LMG | 3° | +0.3°/shot (max 8°) | 1.5°/s | High sustained fire; very slow recovery |

---

## Visual Feedback Systems

### Bullet Visualization

| Element | Implementation | Platform parity |
| :------ | :------------- | :-------------- |
| **Tracer rounds** | Every 3rd bullet fires visible tracer (bright line, 0.05s duration). Player's own weapon always shows tracer; enemy weapon shows tracer only if visible to LOS. | Same PC/mobile/console |
| **Muzzle flash** | 2-frame bright flash at barrel. Visible overhead even for small pistols. | Same |
| **Hit sparks** | Spark VFX where bullet impacts environment (wall, floor, metal crate). 3 spark particles, 0.3s duration. | Slightly simplified on mobile |
| **Blood hit indicator** | Small red puff VFX on enemy body. Confirms hit. Scale based on damage. | Same |
| **Miss feedback** | If bullet travels >10m without hitting: small dust puff at landing point. Helps player see where shots land. | Same |
| **Critical hit (headshot)** | Larger blood pop + distinct audio `crit.wav`. Larger UI hit marker. | Same |

### Hit Marker (UI)

| Outcome | Marker Shape | Color | Duration |
| :------ | :----------- | :---- | :------- |
| Body hit | × (cross) | White | 0.2s |
| Headshot |  (star) | Orange | 0.3s |
| Armored hit (pen failed) | ○ (circle) | Grey | 0.15s |
| Kill | Large × | Red | 0.5s |
| Friendly fire | × | Blue | 0.3s |

**Mobile:** Hit markers are 1.5× larger for finger-display readability.

### Damage Number Pop-Ups

| Setting | Default | Notes |
| :------ | :------ | :---- |
| Damage numbers | OFF by default | Opt-in in settings — disabled by default to preserve immersion |
| Format | "24" or "ARMOR" | Plain number; armor bounce shows "ARMOR" text |
| Position | Floats above enemy for 0.5s | Does not obscure enemy model |

---

## Cover System

### Cover Mechanics in Top-Down

In FPS games, cover is depth-based (player leans behind a wall). In top-down, cover is a **footprint-based** system — being behind an object's 2D footprint blocks line-of-sight from that direction.

```
TOP-DOWN COVER DIAGRAM

Enemy (E)           Cover Object
   ↓         ██████████████████
              ██  Wall/Crate  ██
              ██████████████████
                        Player (P)
                           ↑
                    100% blocked by wall footprint
                    Enemy has NO LOS to Player
```

**Cover rules:**
- LOS from any point is calculated per [LOS, Fog & Visibility](los_fog_visibility/index.html). Cover blocks LOS and shots.
- Any object with collision (walls, crates, vehicles, debris) can be used as cover.
- Players in cover behind a **3m+ wall** segment receive a **movement speed boost of +5%** when crouching behind it (crouch-walk parallel to wall).
- Cover does NOT automatically protect if the player is taller than the cover object. Player height is modeled in top-down: standing behind a low crate only protects legs/torso, not head.

### Cover Object Heights

| Object | Height Modeled | Blocks (Standing) | Blocks (Crouch) | Blocks (Prone) |
| :----- | :------------- | :---------------- | :-------------- | :------------- |
| Full wall (2m+) | Full |  All |  All |  All |
| Cargo crate (1.2m) | Medium |  Torso/legs |  Full |  Full |
| Low barricade (0.7m) | Low |  Only feet |  Torso down |  Full |
| Vehicle body (1.1m) | Medium |  Torso/legs |  Full |  Full |
| Sandbag (0.5m) | Very low |  None |  Head exposed |  Full |

### Peek / Expose Mechanic

Players can expose only part of their character from cover:

| Action | How | Effect |
| :----- | :-- | :----- |
| **Lean out** (stationary) | Hold left/right while against cover | Character's weapon side extends into LOS; rest stays behind cover |
| **Crouch-peek** | Crouch while at cover edge | Smaller silhouette; harder target |
| **Prone-peek** | Prone at cover edge | Nearly invisible from overhead; extremely limited movement |

---

## Suppression System

Supression rewards firing near enemies even without hitting them, adding tactical depth to covering fire.

### Suppression Rules

| Trigger | Effect | Duration |
| :------ | :----- | :------- |
| Bullets land within **3m** of player (not hitting) | Player receives **Suppressed** status | Lasts while bullets continue; 1s decay after last near-miss |
| Suppressed status | Aim cone +2°; minimap vision radius −20%; movement speed −5% | Active while suppression status applies |
| Suppressed by full-auto fire | Effect scales to +3° aim cone at sustained fire | Punishes camping in open |
| Behind full cover (LOS blocked) | Suppression does NOT apply even if bullets hit cover | Taking cover nullifies suppression |

---

## Range & Accuracy Degradation

In top-down, "range" is the 2D horizontal distance between player and target. Bullet drop does not exist (too gamey for overhead view), but accuracy degrades with range:

| Range | Accuracy modifier | Practical effect |
| :---- | :---------------- | :--------------- |
| 0–8m | ×1.5 accuracy bonus | Near-guarantee hit on stationary target |
| 8–20m | ×1.0 (base) | Standard engagement range |
| 20–35m | ×0.75 | Noticeably reduced; burst fire recommended |
| 35–50m | ×0.50 | Challenging; single-shot weapons only |
| 50m+ | ×0.25 | Extreme range; snipers and LMG suppression only |

> Accuracy modifier multiplies the weapon's base aim cone radius.

---

## Environmental Combat Modifiers

| Environment | Combat Effect | Source |
| :---------- | :------------ | :----- |
| **Rain** | Footstep audio range −30%; suppression sound reduced | [Environmental Hazards](environmental_hazards/index.html) |
| **Night** | LOS range −20%; muzzle flashes are visible at 2× range (tactical tell) | [Environmental Hazards](environmental_hazards/index.html) |
| **Storm** | Aim cone +1° (wind); all sound range −50% | [Environmental Hazards](environmental_hazards/index.html) |
| **Smoke** | Aim cone +3° when shooting into smoke; own accuracy unaffected | [LOS, Fog & Visibility](los_fog_visibility/index.html) |
| **Radiation Zone** | No combat penalty; contamination tick while fighting | [Environmental Hazards](environmental_hazards/index.html) |

---

## Audio Combat Design Brief

| Sound | Distance | Priority |
| :---- | :------- | :------- |
| Own weapon fire | — | Critical — must feel punchy and distinct |
| Enemy weapon fire | 80m+ (per [Movement & Stamina](movement_and_stamina/index.html)) | Critical — directional 3D |
| Bullet crack overhead (near-miss) | 15m | High — signals suppression |
| Body hit impact | — | High — distinct per material (armor clank vs. flesh thud) |
| Kill audio sting | — | High — satisfying short tail |
| Reload sound | 5m (enemy reload audible indicator) | Medium — positional cue |
| Gun empty click | — | Critical — alerts player to reload |

---

## Cross-References

- [Movement & Stamina](movement_and_stamina/index.html) — Movement states during combat; surface sounds.
- [Gear Mechanics](gear_mechanics/index.html) — Armor class, penetration, weight penalty during combat.
- [Camera System](camera_system/index.html) — Combat camera altitude shift (+1m during active fire).
- [LOS, Fog & Visibility](los_fog_visibility/index.html) — LOS calculation for cover; smoke effects.
- [Hero Abilities](hero_abilities/index.html) — Flashbang (white-out), smoke, suppression interactions with abilities.
- [Environmental Hazards](environmental_hazards/index.html) — Weather modifiers on combat visibility and accuracy.
