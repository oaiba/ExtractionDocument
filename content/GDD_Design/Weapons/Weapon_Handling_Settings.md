---
title: "Weapon Handling & Settings"
type: docs
weight: 1
---

## Overview

Weapon handling defines how quickly and smoothly players can ready, aim, and fire their weapons. These parameters are tuned per weapon class and are modified by attachments (ergonomics) and [Gear Mechanics](../Gameplay/Gear_Mechanics.md) (weight tier). Design reference: Tarkov ergonomics, Arena Breakout handling stats, Delta Force per-weapon progression.

> **Cross-References:** [Weapon Modding (Gunsmith)](../Inventory_Gear/Weapons_Modding.md) — ergonomics stat affecting ADS and stamina; [Weapon Attachment System](../Gameplay/Weapon_Attachment_System.md) — attachment weight and stat modifiers; [Combat Feel (Top-Down)](../Gameplay/Combat_Feel_Topdown.md) — aim cone and recoil recovery.

---

## Draw & Holster Times

Time to switch to a weapon (draw) or stow it (holster). Affects weapon-swap and sidearm usage in CQB.

| Weapon Class | Draw Time | Holster Time | Notes |
| :------------ | :-------: | :----------: | :---- |
| Pistol | 0.30 s | 0.25 s | Fastest; emergency sidearm |
| Melee | 0.35 s | 0.30 s | Quick deploy for backstab |
| SMG | 0.45 s | 0.40 s | Light, compact |
| Assault Rifle | 0.55 s | 0.50 s | Standard primary |
| DMR | 0.60 s | 0.55 s | Heavier than AR |
| Shotgun | 0.65 s | 0.55 s | Pump/action weight |
| Sniper Rifle | 0.70 s | 0.60 s | Long barrel, scope |
| LMG | 1.20 s | 1.00 s | Heavy; deliberate swap |

**Modifiers:** Ergonomics from [Weapon Modding](../Inventory_Gear/Weapons_Modding.md) adjusts draw/holster by ±10%. Weight tier (Heavy/Critical) adds +0.1–0.2 s to LMG and Sniper.

---

## ADS Timing

Time from hip-fire state to fully aimed (precision aim mode). In top-down, ADS tightens aim cone and may apply a slight camera zoom per [Camera System](../Gameplay/Camera_System.md).

| Weapon Class | Base ADS Time | With High Ergo (est) | With Low Ergo (est) |
| :----------- | :------------: | :------------------: | :-----------------: |
| Pistol | 0.15 s | 0.12 s | 0.20 s |
| SMG | 0.20 s | 0.16 s | 0.26 s |
| Assault Rifle | 0.25 s | 0.20 s | 0.32 s |
| DMR | 0.30 s | 0.24 s | 0.38 s |
| Shotgun | 0.28 s | 0.22 s | 0.35 s |
| Sniper Rifle | 0.45 s | 0.36 s | 0.55 s |
| LMG | 0.40 s | 0.32 s | 0.50 s |

Optics add a fixed ADS penalty (e.g. ACOG +0.10 s, 8× Sniper +0.15 s) as defined in [Weapon Attachment System](../Gameplay/Weapon_Attachment_System.md).

---

## Movement Speed Modifiers

Percentage speed reduction while the weapon is wielded (not stowed). Base movement from [Movement & Stamina](../Gameplay/Movement_and_Stamina.md).

| Weapon Class | Speed Modifier | Notes |
| :----------- | :------------: | :---- |
| Pistol | 0% | No penalty |
| Melee | 0% | No penalty |
| SMG | 0% | Full mobility |
| Assault Rifle | −5% | Slight slowdown |
| DMR | −7% | Heavier than AR |
| Shotgun | −5% | Short barrel typical |
| Sniper Rifle | −10% | Long, heavy |
| LMG | −15% | Heavy weapon |

Modifiers stack with weight tier from [Gear Mechanics](../Gameplay/Gear_Mechanics.md). A player in Heavy tier with an LMG has compounded slowdown.

---

## Weapon Sway

Idle sway amplitude (crosshair drift when stationary). Affects long-range precision and is influenced by stamina and ergonomics.

| Weapon Class | Base Sway (deg) | Low Stamina Multiplier | High Ergo Reduction |
| :----------- | :-------------: | :--------------------: | :-----------------: |
| Pistol | 0.4° | ×1.5 | −15% |
| SMG | 0.35° | ×1.4 | −20% |
| Assault Rifle | 0.5° | ×1.6 | −15% |
| DMR | 0.45° | ×1.5 | −20% |
| Shotgun | 0.6° | ×1.5 | −10% |
| Sniper Rifle | 0.3° | ×1.8 | −25% |
| LMG | 0.7° | ×1.7 | −10% |

Bipod (when prone/crouched) sets sway to 0.1° for LMG and Sniper. Sway is applied in top-down as a small random offset to the aim direction each frame.

---

## Hip-Fire vs ADS Behavior

Hip-fire uses a wider aim cone; ADS tightens it. Values align with [Combat Feel (Top-Down)](../Gameplay/Combat_Feel_Topdown.md).

| Weapon Class | Hip-Fire Cone Multiplier | ADS Cone Multiplier | Notes |
| :----------- | :----------------------: | :-----------------: | :---- |
| Pistol | ×2.0 | ×0.6 | Hip acceptable at close range |
| SMG | ×1.8 | ×0.65 | CQB hip-fire viable |
| Assault Rifle | ×2.2 | ×0.5 | ADS preferred 15 m+ |
| DMR | ×2.5 | ×0.4 | ADS required for effectiveness |
| Shotgun | ×1.0 (fixed spread) | ×0.9 | Spread pattern unchanged |
| Sniper Rifle | ×3.0 | ×0.35 | Hip-fire emergency only |
| LMG | ×2.4 | ×0.55 | Suppression hip-fire option |

Laser sight reduces hip-fire cone multiplier by 0.25 (e.g. AR 2.2 → 1.95).

---

## Reload Speeds

Full reload = empty mag replaced. Tactical reload = mag replaced with round in chamber (faster).

| Weapon Class | Full Reload | Tactical Reload | Magazine Type Note |
| :----------- | :---------: | :-------------: | :----------------- |
| Pistol | 1.4 s | 1.0 s | Standard 17–20 rd |
| SMG | 2.0 s | 1.5 s | 25–50 rd |
| Assault Rifle | 2.4 s | 1.8 s | 30 rd standard |
| DMR | 2.6 s | 2.0 s | 10–20 rd |
| Shotgun | 3.0 s (6 shells) | — | Pump/ tube load |
| Sniper Rifle | 2.2 s | 1.6 s | 5–10 rd |
| LMG | 6.0 s | 5.0 s | Belt/box; long animation |

Extended and drum magazines add +0.3–1.5 s to full reload per [Weapon Attachment System](../Gameplay/Weapon_Attachment_System.md). Fast Mag attachment reduces times by the documented percentage.

---

## Fire Mode Switching

Time to toggle between Semi / Burst / Auto (where available).

| Action | Time | Notes |
| :----- | :--- | :---- |
| Semi ↔ Auto | 0.4 s | Physical selector animation |
| Semi ↔ Burst | 0.4 s | Same as above |
| Burst ↔ Auto | 0.3 s | Same selector, shorter cue |

Not all weapons have all modes. ARs typically have Semi + Auto; some have Burst. LMGs are Auto only. Pistols are Semi (or burst for select models).

---

## Sprint-to-Fire Time

Time from sprint state to first accurate shot. Includes weapon ready + ADS if player holds aim.

| Weapon Class | Sprint-to-Fire (Hip) | Sprint-to-Fire (ADS) |
| :----------- | :------------------: | :-------------------: |
| Pistol | 0.35 s | 0.50 s |
| SMG | 0.40 s | 0.55 s |
| Assault Rifle | 0.50 s | 0.70 s |
| DMR | 0.55 s | 0.80 s |
| Shotgun | 0.55 s | 0.75 s |
| Sniper Rifle | 0.70 s | 1.00 s |
| LMG | 0.90 s | 1.20 s |

Design intent: punishes blind sprint into contact; rewards pre-aiming before peeking.

---

## Weapon Inspection

In-raid inspect: player views weapon model (cosmetic/condition). No gameplay effect.

| Action | Time | Notes |
| :----- | :--- | :---- |
| Start inspect | 0.5 s | Animation start |
| Inspect loop | 3.0 s | Repeatable idle |
| Cancel inspect | 0.2 s | Return to ready |

Inspect is disabled during sprint, reload, or use of abilities.

---

## Mobile-Specific Settings

Touch and gyro handling for cross-platform parity.

| Setting | Description | Default |
| :------ | :---------- | :------ |
| Gyro sensitivity (per weapon class) | Multiplier for gyro recoil compensation | AR: 1.0, SMG: 1.2, Sniper: 0.7 |
| Aim-assist cone width | Soft lock-in radius when target in cone (PvE only or configurable) | 0.5°–1.5° (tunable) |
| Auto-fire toggle | Hold to fire full-auto without tap | Off |
| Recoil compensation assist | Optional reduced vertical recoil (rewards manual control if off) | 0% (off) or 10–20% (accessibility) |
| Haptic intensity per shot | Feedback per weapon class | Light / Medium / Strong |

Mobile uses the same draw, ADS, and reload times as PC; only input and feedback differ.

---

## Cross-References

- [Weapon Modding (Gunsmith)](../Inventory_Gear/Weapons_Modding.md) — Ergonomics, recoil control, MOA.
- [Weapon Attachment System](../Gameplay/Weapon_Attachment_System.md) — Attachment effects on weight and handling.
- [Gear Mechanics](../Gameplay/Gear_Mechanics.md) — Weight tier and mobility.
- [Combat Feel (Top-Down)](../Gameplay/Combat_Feel_Topdown.md) — Aim cone, recoil bloom, recovery.
