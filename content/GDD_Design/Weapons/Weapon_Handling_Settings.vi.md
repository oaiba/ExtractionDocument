---
title: "vũ khí Handling & Settings"
type: docs
weight: 1
---

## Tổng Quan

vũ khí handling defines how quickly và smoothly Người chơi có thể ready, aim, và fire their vũ khí. These parameters are tuned per vũ khí class và are modified by attachments (ergonomics) và [Gear cơ chế](../Gameplay/Gear_Mechanics.md) (weight tier). Design reference: Tarkov ergonomics, Arena Breakout handling stats, Delta Force per-vũ khí progression.

> **Cross-References:** [vũ khí Modding (Gunsmith)](../Inventory_System/Gunsmith_System.md) — ergonomics stat affecting ADS và stamina; [vũ khí Attachment hệ thống](../Gameplay/Weapon_Attachment_System.md) — attachment weight và stat modifiers; [Combat Feel (Top-Down)](../Gameplay/Combat_Feel_Topdown.md) — aim cone và recoil recovery.

---

## Recoil / Spread / Handling Contract

Handling là biểu hiện moment-to-moment của weapon role. Nó phải làm intended range và counterplay readable trước khi damage math resolve.

| Behavior | Rule | Player-Facing Feedback |
| :--- | :--- | :--- |
| First-shot accuracy | Cao cho precision weapons, vừa cho AR, thấp hơn từ sprint/hip-fire | Reticle settle, ADS readiness, movement bloom |
| Sustained recoil | Tăng khi bắn liên tục; recovery theo role | Muzzle climb, reticle expansion, audio cadence |
| Spread bloom | Hip-fire và movement expand spread nhanh nhất | Reticle size và bullet impact pattern |
| Recovery | Burst discipline trả accuracy nhanh hơn spray | Reticle contract rõ sau pause |
| Movement penalty | Sprint, strafe, vault, overweight, suppression giảm handling | Movement icon, stamina/weight linkage |
| Stance / cover | Stable stance hoặc cover giảm sway/spread nếu support | Reticle stability và animation subtle |
| Suppression impact | Incoming volume disrupt aim/focus nhưng không mất agency | Short aim pressure, audio ducking, duration readable |

## Attachment Trade-Off Rules

Attachment modify handling nhưng không được tạo pure upgrade stack.

| Attachment Family | Can Improve | Must Trade Against |
| :--- | :--- | :--- |
| Muzzle / suppressor | Noise, recoil, flash | Length, cost, weight, durability, bullet crack limits |
| Grip / handguard | Recoil recovery, hip control | Weight, ADS time, slot conflict |
| Stock | Stability, recoil, shoulder speed | Mobility, draw time, storage footprint |
| Optic | Target readability, precision | ADS time, close-range clutter, glint/visibility cho high magnification |
| Magazine | Capacity, reload cadence | Weight, reload speed, handling, stash footprint |
| Barrel | Range, velocity, spread | Weight, ADS, noise, CQB handling |

---

## Draw & Holster Times

thời gian to switch to a vũ khí (draw) hoặc stow it (holster). Affects vũ khí-swap và sidearm usage in CQB.

| vũ khí Class | Draw thời gian | Holster thời gian | ghi chú |
| :------------ | :-------: | :----------: | :---- |
| Pistol | 0.30 s | 0.25 s | Fastest; emergency sidearm |
| Melee | 0.35 s | 0.30 s | Quick deploy for backstab |
| SMG | 0.45 s | 0.40 s | Light, compact |
| Assault Rifle | 0.55 s | 0.50 s | Standard primary |
| DMR | 0.60 s | 0.55 s | Heavier than AR |
| Shotgun | 0.65 s | 0.55 s | Pump/action weight |
| Sniper Rifle | 0.70 s | 0.60 s | Long barrel, scope |
| LMG | 1.20 s | 1.00 s | Heavy; deliberate swap |

**Modifiers:** Ergonomics from [vũ khí Modding](../Inventory_System/Gunsmith_System.md) adjusts draw/holster by ±10%. Weight tier (Heavy/Critical) adds +0.1–0.2 s to LMG và Sniper.

---

## ADS Timing

thời gian from hip-fire trạng thái to fully aimed (precision aim mode). In top-down, ADS tightens aim cone và may apply a slight camera zoom per [Camera hệ thống](../Gameplay/Camera_System.md).

| vũ khí Class | Base ADS thời gian | với High Ergo (est) | với Low Ergo (est) |
| :----------- | :------------: | :------------------: | :-----------------: |
| Pistol | 0.15 s | 0.12 s | 0.20 s |
| SMG | 0.20 s | 0.16 s | 0.26 s |
| Assault Rifle | 0.25 s | 0.20 s | 0.32 s |
| DMR | 0.30 s | 0.24 s | 0.38 s |
| Shotgun | 0.28 s | 0.22 s | 0.35 s |
| Sniper Rifle | 0.45 s | 0.36 s | 0.55 s |
| LMG | 0.40 s | 0.32 s | 0.50 s |

Optics add a fixed ADS penalty (e.g. ACOG +0.10 s, 8× Sniper +0.15 s) as defined in [vũ khí Attachment hệ thống](../Gameplay/Weapon_Attachment_System.md).

---

## Movement Speed Modifiers

Percentage speed reduction while the vũ khí is wielded (not stowed). Base movement from [Movement & Stamina](../Gameplay/Movement_and_Stamina.md).

| vũ khí Class | Speed Modifier | ghi chú |
| :----------- | :------------: | :---- |
| Pistol | 0% | No penalty |
| Melee | 0% | No penalty |
| SMG | 0% | Full mobility |
| Assault Rifle | −5% | Slight slowdown |
| DMR | −7% | Heavier than AR |
| Shotgun | −5% | Short barrel typical |
| Sniper Rifle | −10% | Long, heavy |
| LMG | −15% | Heavy vũ khí |

Modifiers stack với weight tier from [Gear cơ chế](../Gameplay/Gear_Mechanics.md). A người chơi in Heavy tier với an LMG has compounded slowdown.

---

## vũ khí Sway

Idle sway amplitude (crosshair drift khi stationary). Affects long-range precision và is influenced by stamina và ergonomics.

| vũ khí Class | Base Sway (deg) | Low Stamina Multiplier | High Ergo Reduction |
| :----------- | :-------------: | :--------------------: | :-----------------: |
| Pistol | 0.4° | ×1.5 | −15% |
| SMG | 0.35° | ×1.4 | −20% |
| Assault Rifle | 0.5° | ×1.6 | −15% |
| DMR | 0.45° | ×1.5 | −20% |
| Shotgun | 0.6° | ×1.5 | −10% |
| Sniper Rifle | 0.3° | ×1.8 | −25% |
| LMG | 0.7° | ×1.7 | −10% |

Bipod (khi prone/crouched) sets sway to 0.1° for LMG và Sniper. Sway is applied in top-down as a small random offset to the aim direction each frame.

---

## Hip-Fire vs ADS Behavior

Hip-fire uses a wider aim cone; ADS tightens it. Values align với [Combat Feel (Top-Down)](../Gameplay/Combat_Feel_Topdown.md).

| vũ khí Class | Hip-Fire Cone Multiplier | ADS Cone Multiplier | ghi chú |
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

Full reload = empty mag replaced. Tactical reload = mag replaced với round in chamber (faster).

| vũ khí Class | Full Reload | Tactical Reload | Magazine Type Note |
| :----------- | :---------: | :-------------: | :----------------- |
| Pistol | 1.4 s | 1.0 s | Standard 17–20 rd |
| SMG | 2.0 s | 1.5 s | 25–50 rd |
| Assault Rifle | 2.4 s | 1.8 s | 30 rd standard |
| DMR | 2.6 s | 2.0 s | 10–20 rd |
| Shotgun | 3.0 s (6 shells) | — | Pump/ tube load |
| Sniper Rifle | 2.2 s | 1.6 s | 5–10 rd |
| LMG | 6.0 s | 5.0 s | Belt/box; long animation |

Extended và drum magazines add +0.3–1.5 s to full reload per [vũ khí Attachment hệ thống](../Gameplay/Weapon_Attachment_System.md). Fast Mag attachment reduces times by the documented percentage.

---

## Fire Mode Switching

thời gian to toggle between Semi / Burst / Auto (where available).

| Action | thời gian | ghi chú |
| :----- | :--- | :---- |
| Semi ↔ Auto | 0.4 s | Physical selector animation |
| Semi ↔ Burst | 0.4 s | Same as above |
| Burst ↔ Auto | 0.3 s | Same selector, shorter cue |

Not all vũ khí have all modes. ARs typically have Semi + Auto; some have Burst. LMGs are Auto only. Pistols are Semi (hoặc burst for select models).

---

## Sprint-to-Fire thời gian

thời gian from sprint trạng thái to first accurate shot. Includes vũ khí ready + ADS nếu người chơi holds aim.

| vũ khí Class | Sprint-to-Fire (Hip) | Sprint-to-Fire (ADS) |
| :----------- | :------------------: | :-------------------: |
| Pistol | 0.35 s | 0.50 s |
| SMG | 0.40 s | 0.55 s |
| Assault Rifle | 0.50 s | 0.70 s |
| DMR | 0.55 s | 0.80 s |
| Shotgun | 0.55 s | 0.75 s |
| Sniper Rifle | 0.70 s | 1.00 s |
| LMG | 0.90 s | 1.20 s |

Design intent: punishes blind sprint into contact; rewards pre-aiming trước peeking.

---

## vũ khí Inspection

In-raid kiểm tra: người chơi views vũ khí model (cosmetic/condition). No gameplay effect.

| Action | thời gian | ghi chú |
| :----- | :--- | :---- |
| Start kiểm tra | 0.5 s | Animation start |
| kiểm tra loop | 3.0 s | Repeatable idle |
| Cancel kiểm tra | 0.2 s | Return to ready |

kiểm tra is disabled trong khi sprint, reload, hoặc cách dùng of abilities.

---

## Mobile-cụ thể Settings

Touch và gyro handling for cross-platform parity.

| Setting | Description | Default |
| :------ | :---------- | :------ |
| Gyro sensitivity (per vũ khí class) | Multiplier for gyro recoil compensation | AR: 1.0, SMG: 1.2, Sniper: 0.7 |
| Aim-assist cone width | Soft lock-in radius khi target in cone (PvE only hoặc configurable) | 0.5°–1.5° (tunable) |
| Auto-fire toggle | Hold to fire full-auto mà không tap | Off |
| Recoil compensation assist | Optional reduced vertical recoil (rewards manual control nếu off) | 0% (off) hoặc 10–20% (accessibility) |
| Haptic intensity per shot | Feedback per vũ khí class | Light / Medium / Strong |

Mobile uses the same draw, ADS, và reload times as PC; only input và feedback differ.

---

## Tham Chiếu Chéo

- [vũ khí Modding (Gunsmith)](../Inventory_System/Gunsmith_System.md) — Ergonomics, recoil control, MOA.
- [vũ khí Attachment hệ thống](../Gameplay/Weapon_Attachment_System.md) — Attachment effects on weight và handling.
- [Gear cơ chế](../Gameplay/Gear_Mechanics.md) — Weight tier và mobility.
- [Combat Feel (Top-Down)](../Gameplay/Combat_Feel_Topdown.md) — Aim cone, recoil bloom, recovery.
