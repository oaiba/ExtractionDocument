---
title: "Combat Feel — Top-Down"
type: docs
weight: 19
---

## Tổng Quan

Combat in a top-down extraction shooter presents unique design challenges not present in FPS hoặc third-person games. The overhead perspective changes how người chơi perceive distance, cover, aim direction, và bullet travel. This tài liệu specifies the visual feedback hệ thống, recoil model, cover interactions, suppression, và the overall combat feel targets that distinguish this game from its competitors.

> **Cross-References:** [Movement & Stamina](Movement_and_Stamina.md) — movement trạng thái trong khi combat; [Gear cơ chế](Gear_Mechanics.md) — giáp penetration, vũ khí tiers; [Hero Abilities](Hero_Abilities.md) — ability interactions với combat; [LOS, Fog & Visibility](LOS_Fog_Visibility.md) — LOS trong khi combat; [Camera hệ thống](Camera_System.md) — combat camera altitude (+1m boost); [Environmental Hazards](Environmental_Hazards.md) — weather effects on combat visibility.

---

## Combat Feel Targets

The cốt lõi feel words for combat:

| Feel Target | Description |
| :---------- | :---------- |
| **Deliberate** | Shots have weight; full-auto spray is punished. Burst fire is king. |
| **dễ đọc** | Every combat action is visually rõ from overhead — no "mystery deaths." |
| **Tactical** | Cover matters. Flanking is rewarded. Rushing is punished. |
| **Consequential** | One mistake costs HP that is hard to recover. Death proximity is always felt. |
| **Satisfying** | rõ hit feedback, distinct kill feel, audible differences between vũ khí tiers. |

---

## vũ khí Firing & Recoil

### Recoil in Top-Down Context

In a standard FPS, recoil manifests as camera kick — the màn hình moves up. In top-down, the nhân vật is viewed from above, so recoil is represented differently:

| cơ chế | FPS Implementation | Top-Down Implementation |
| :------- | :----------------- | :---------------------- |
| **Visual recoil** | màn hình kick upward | vũ khí "kick" animation (nhân vật model's arms pull back) |
| **Aim deviation** | Crosshair climbs | Crosshair jitters in a cone pattern; cone SIZE grows per shot |
| **Recoil pattern** | Vertical + horizontal drift | Full 360° cone bloom that expands per shot |
| **Recovery** | Mouse pull-down to compensate | Stop firing và wait for cone to close (no compensation needed) |

### Aim Cone Behavior

| trạng thái | Aim Cone Radius | ghi chú |
| :---- | :-------------- | :---- |
| Standing, not moving | 2° | Base accuracy |
| Crouching, stationary | 1° | Most accurate trạng thái |
| Prone, stationary | 0.5° | Pinpoint; very slow to move |
| Walking | 4° | Moderate; precision reduced |
| Sprinting | Cannot fire | Fire locked while sprinting |
| Full-auto fire (per bullet) | +0.5° per shot (up to 6° max) | Cone bloom accumulates |
| Post-burst (no fire, 1s) | Cone recovers at 3°/second | Release trigger = cone closes |

### vũ khí Class Recoil Profiles

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

## Visual Feedback hệ thống

### Bullet Visualization

| Element | Implementation | Platform parity |
| :------ | :------------- | :-------------- |
| **Tracer rounds** | Every 3rd bullet fires hiển thị rõ tracer (bright line, 0.05s duration). người chơi's own vũ khí always shows tracer; địch vũ khí shows tracer only nếu hiển thị rõ to LOS. | Same PC/mobile/console |
| **Muzzle flash** | 2-frame bright flash at barrel. hiển thị rõ overhead even for small pistols. | Same |
| **Hit sparks** | Spark VFX where bullet impacts environment (wall, floor, metal crate). 3 spark particles, 0.3s duration. | Slightly simplified on mobile |
| **Blood hit indicator** | Small red puff VFX on địch body. Confirms hit. Scale based on damage. | Same |
| **Miss feedback** | nếu bullet travels >10m mà không hitting: small dust puff at landing point. giúp người chơi see where shots land. | Same |
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

| Setting | Default | ghi chú |
| :------ | :------ | :---- |
| Damage thông số | OFF by default | Opt-in in settings — disabled by default to preserve immersion |
| Format | "24" hoặc "giáp" | Plain number; giáp bounce shows "giáp" text |
| Position | Floats above địch for 0.5s | Does not obscure địch model |

---

## Cover hệ thống

### Cover cơ chế in Top-Down

In FPS games, cover is depth-based (người chơi leans behind a wall). In top-down, cover is a **footprint-based** hệ thống — being behind an object's 2D footprint blocks line-of-sight from that direction.

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
- LOS from any point is calculated per [LOS, Fog & Visibility](LOS_Fog_Visibility.md). Cover blocks LOS và shots.
- Any object với collision (walls, crates, vehicles, debris) can be used as cover.
- người chơi in cover behind a **3m+ wall** segment receive a **movement speed boost of +5%** khi crouching behind it (crouch-walk parallel to wall).
- Cover does NOT automatically protect nếu the người chơi is taller than the cover object. người chơi height is modeled in top-down: standing behind a low crate only protects legs/torso, not head.

### Cover Object Heights

| Object | Height Modeled | Blocks (Standing) | Blocks (Crouch) | Blocks (Prone) |
| :----- | :------------- | :---------------- | :-------------- | :------------- |
| Full wall (2m+) | Full |  All |  All |  All |
| Cargo crate (1.2m) | Medium |  Torso/legs |  Full |  Full |
| Low barricade (0.7m) | Low |  Only feet |  Torso down |  Full |
| Vehicle body (1.1m) | Medium |  Torso/legs |  Full |  Full |
| Sandbag (0.5m) | Very low |  None |  Head exposed |  Full |

### Peek / Expose cơ chế

Người chơi có thể expose only part of their nhân vật from cover:

| Action | How | Effect |
| :----- | :-- | :----- |
| **Lean out** (stationary) | Hold left/right while against cover | nhân vật's vũ khí side extends into LOS; rest stays behind cover |
| **Crouch-peek** | Crouch while at cover edge | Smaller silhouette; harder target |
| **Prone-peek** | Prone at cover edge | Nearly invisible from overhead; extremely limited movement |

---

## Suppression hệ thống

Supression rewards firing near địch even mà không hitting them, adding tactical depth to covering fire.

### Suppression Rules

| Trigger | Effect | Duration |
| :------ | :----- | :------- |
| Bullets land within **3m** of người chơi (not hitting) | người chơi receives **Suppressed** status | Lasts while bullets continue; 1s decay sau last near-miss |
| Suppressed status | Aim cone +2°; minimap vision radius −20%; movement speed −5% | Active while suppression status applies |
| Suppressed by full-auto fire | Effect scales to +3° aim cone at sustained fire | Punishes camping in open |
| Behind full cover (LOS blocked) | Suppression does NOT apply even nếu bullets hit cover | Taking cover nullifies suppression |

---

## Range & Accuracy Degradation

In top-down, "range" is the 2D horizontal distance between người chơi và target. Bullet drop does not exist (too gamey for overhead view), nhưng accuracy degrades với range:

| Range | Accuracy modifier | Practical effect |
| :---- | :---------------- | :--------------- |
| 0–8m | ×1.5 accuracy bonus | Near-guarantee hit on stationary target |
| 8–20m | ×1.0 (base) | Standard engagement range |
| 20–35m | ×0.75 | Noticeably reduced; burst fire recommended |
| 35–50m | ×0.50 | Challenging; single-shot vũ khí only |
| 50m+ | ×0.25 | Extreme range; snipers và LMG suppression only |

> Accuracy modifier multiplies the vũ khí's base aim cone radius.

---

## Environmental Combat Modifiers

| Environment | Combat Effect | source |
| :---------- | :------------ | :----- |
| **Rain** | Footstep audio range −30%; suppression sound reduced | [Environmental Hazards](Environmental_Hazards.md) |
| **Night** | LOS range −20%; muzzle flashes are hiển thị rõ at 2× range (tactical tell) | [Environmental Hazards](Environmental_Hazards.md) |
| **Storm** | Aim cone +1° (wind); all sound range −50% | [Environmental Hazards](Environmental_Hazards.md) |
| **Smoke** | Aim cone +3° khi shooting into smoke; own accuracy unaffected | [LOS, Fog & Visibility](LOS_Fog_Visibility.md) |
| **Radiation Zone** | No combat penalty; contamination tick while fighting | [Environmental Hazards](Environmental_Hazards.md) |

---

## Audio Combat Design Brief

| Sound | Distance | Priority |
| :---- | :------- | :------- |
| Own vũ khí fire | — | Critical — must feel punchy và distinct |
| địch vũ khí fire | 80m+ (per [Movement & Stamina](Movement_and_Stamina.md)) | Critical — directional 3D |
| Bullet crack overhead (near-miss) | 15m | High — signals suppression |
| Body hit impact | — | High — distinct per material (giáp clank vs. flesh thud) |
| Kill audio sting | — | High — satisfying short tail |
| Reload sound | 5m (địch reload audible indicator) | Medium — positional cue |
| Gun empty click | — | Critical — alerts người chơi to reload |

---

## Tham Chiếu Chéo

- [Movement & Stamina](Movement_and_Stamina.md) — Movement trạng thái trong khi combat; surface sounds.
- [Gear cơ chế](Gear_Mechanics.md) — giáp class, penetration, weight penalty trong khi combat.
- [Camera hệ thống](Camera_System.md) — Combat camera altitude shift (+1m trong khi active fire).
- [LOS, Fog & Visibility](LOS_Fog_Visibility.md) — LOS calculation for cover; smoke effects.
- [Hero Abilities](Hero_Abilities.md) — Flashbang (white-out), smoke, suppression interactions với abilities.
- [Environmental Hazards](Environmental_Hazards.md) — Weather modifiers on combat visibility và accuracy.
