---
title: "vũ khí Visual & Audio Identity"
type: docs
weight: 7
---

## Tổng Quan

This tài liệu specifies how vũ khí are read from the top-down camera: silhouettes, muzzle flash, attachment visibility, audio signatures, kill feedback, và rarity presentation. Design mục tiêu: every combat action is dễ đọc và distinct from overhead. Xem [Combat Feel (Top-Down)](../Gameplay/Combat_Feel_Topdown.md) for aim cone và feedback hệ thống.

> **Cross-References:** [vũ khí Arsenal](../Gameplay/WeaponArsenal.md) — vũ khí list; [vũ khí Attachment hệ thống](../Gameplay/Weapon_Attachment_System.md) — attachment types; [Audio — Sound Design](../Audio/SoundDesign.md) — overall audio philosophy.

---

## vũ khí Silhouette Guide

From the top-down camera, each vũ khí class phải được distinguishable by **length**, **width**, và **profile** so Người chơi có thể identify threats trong một nhịp nhìn.

| vũ khí Class | Relative Length | Width / Profile | Distinct Cues |
| :----------- | :-------------- | :-------------- | :------------- |
| Pistol | Short | Narrow | Small rectangle; holstered on thigh khi not wielded |
| SMG | Medium-short | Narrow | Compact; magazine hiển thị rõ under receiver |
| Assault Rifle | Medium-long | Medium | Barrel + stock; mag well hiển thị rõ |
| DMR | Long | Medium | Longer barrel; scope bulge nếu equipped |
| Shotgun | Medium (pump) to long (auto) | Medium-wide | Tube hoặc box mag; pump forend on pump-actions |
| Sniper Rifle | Very long | Medium | Long barrel; large scope silhouette |
| LMG | Very long | Wide | Belt/box; bipod legs khi deployed |
| Melee | Short (knife) to medium (axe) | Thin | Blade hoặc haft; no muzzle |

**Rules:** Silhouette is drawn from the **wielded** vũ khí model (first-person hoặc third-person asset projected to top-down). Scale is nhất quán: e.g. 1 m real length ≈ fixed pixel length at default zoom. No vũ khí nên được indistinguishable from another within the same class (e.g. M4 vs HK416 can share approximate size nhưng differ in stock/barrel shape nếu possible).

---

## Muzzle Flash Scaling

Muzzle flash reveals shooter position. Size và duration scale by vũ khí class và attachment trạng thái.

| vũ khí Class | Base Flash Radius (top-down) | Duration | với Suppressor |
| :----------- | :--------------------------- | :------ | :--------------- |
| Pistol | 0.4 m (visual) | 2 frames | 80% reduction; minimal glow |
| SMG | 0.5 m | 2 frames | 80% reduction |
| AR | 0.6 m | 2–3 frames | 80% reduction |
| DMR | 0.55 m | 2 frames | 80% reduction |
| Shotgun | 0.7 m | 3 frames | 70% reduction (larger bore) |
| Sniper | 0.65 m | 3 frames | 80% reduction |
| LMG | 0.75 m | 3 frames | 75% reduction |

**Visibility range:** Muzzle flash is hiển thị rõ to other người chơi within LOS up to 80 m (hoặc per [Movement & Stamina](../Gameplay/Movement_and_Stamina.md) audio/visual range). Night hoặc dark zones: flash hiển thị rõ at 2× range per [Environmental Hazards](../Gameplay/Environmental_Hazards.md). Suppressor reduces both sound và flash to avoid contradicting stealth.

---

## Attachment Visibility

Which attachments are hiển thị rõ from the top-down view khi the vũ khí is wielded hoặc on the ground.

| Attachment Slot | hiển thị rõ from Top-Down | ghi chú |
| :-------------- | :-------------------- | :---- |
| Muzzle (suppressor, comp, brake) | Yes | Length change; suppressor extends barrel silhouette |
| Barrel (short, heavy, extended) | Partially | Length change hiển thị rõ; profile similar |
| Stock | Yes | Folded vs extended; heavy stock bulkier |
| Optics / sight | Yes | Scope tube và housing; red dot smaller |
| Underbarrel (grip, bipod, GL) | Yes | Grip và bipod legs; GL tube |
| Magazine | Yes | Drum vs stick; extended mag length |
| Laser / light | Yes (khi active) | Laser dot on surface; light cone in dark |

**Ground loot:** vũ khí on ground shows full silhouette including attachments. Rarity glow (see below) applies to vũ khí outline, not to each attachment separately.

---

## Audio Signature Per vũ khí

Each vũ khí (hoặc caliber family) has a **distinct report** so Người chơi có thể identify threat type by sound. Distance attenuation và occlusion apply.

| Caliber / Family | Report nhân vật | Audible Range (approx) | Suppressed Range |
| :--------------- | :--------------- | :---------------------- | :--------------- |
| 9×19 / .45 pistol | Crack; short tail | 40 m | 12–16 m |
| 5.56 / 5.7 | Sharp crack; medium tail | 60 m | 20–25 m |
| 7.62×39 | Deeper thump; medium tail | 55 m | 18–22 m |
| 7.62×51 / 54R | Heavy crack; long tail | 70 m | 22–28 m |
| .338 / .50 | Very heavy; long tail | 90 m | 28–35 m |
| 12 Gauge | Boom; short tail | 50 m | 15–20 m |

**Rules:** Same caliber can share base sound với pitch/body variation per vũ khí (e.g. M4 vs HK416 slightly different). Reload, bolt cycle, và empty click are also distinct per vũ khí class. Xem [Audio — Sound Design](../Audio/SoundDesign.md) và [Tactical Audio](../Audio/TacticalAudio.md) for integration.

---

## Kill Feedback Design

Death animation và feedback vary by **killing vũ khí class** to reinforce vũ khí identity và satisfaction.

| Killing vũ khí Class | Victim Feedback | Shooter Feedback |
| :------------------- | :-------------- | :--------------- |
| Shotgun | Knockback; heavy stagger; ragdoll possible at close range | Heavy impact sound; large hit marker |
| Sniper | Instant drop; minimal stagger; clean kill | Distinct kill sting; headshot chime nếu head |
| SMG | Stagger; multiple small hits | Rapid hit markers; kill confirm tone |
| AR | Moderate stagger; 2–4 hit reaction | Standard kill tone |
| LMG | Sustained stagger; suppression death | Sustained fire + final kill tone |
| DMR | 1–2 shot drop; moderate stagger | Precision kill tone |
| Pistol | Light stagger; slower collapse | Sidearm kill tone (different from primary) |
| Melee (backstab) | Instant collapse; silent | Satisfying "thunk"; no gun sound |

**Design intent:** dễ đọc from top-down: người chơi can tell "I was killed by a shotgun" hoặc "I got headshot by a sniper" from feedback alone. No mystery deaths.

---

## vũ khí Color-Coding (Rarity Glow)

**Ground loot và container contents:** vũ khí display a **rarity outline hoặc glow** so Người chơi có thể prioritize loot trong một nhịp nhìn.

| Rarity | Color | Glow / Outline |
| :----- | :---- | :------------- |
| Common | White | No glow hoặc subtle white outline |
| Uncommon | Green | Soft green outline |
| Rare | Blue | Blue outline |
| Epic | Purple | Purple glow |
| Legendary | Gold | Gold glow; subtle pulse |

**In-hand / equipped:** The vũ khí the người chơi is holding does **not** show a rarity glow on the nhân vật model (immersion). Rarity is hiển thị rõ in HUD (vũ khí name, icon) và in inventory only.

**địch-held vũ khí:** No glow on địch vũ khí (prevents "shoot the gold gun first" meta). Rarity is only hiển thị rõ on loot.

---

## Tham Chiếu Chéo

- [Combat Feel (Top-Down)](../Gameplay/Combat_Feel_Topdown.md) — Hit markers, tracers, aim cone, suppression.
- [vũ khí Arsenal](../Gameplay/WeaponArsenal.md) — vũ khí list và categories.
- [vũ khí Attachment hệ thống](../Gameplay/Weapon_Attachment_System.md) — Attachment types và slots.
- [Audio — Sound Design](../Audio/SoundDesign.md) — Gunshot và combat audio.
- [Environmental Hazards](../Gameplay/Environmental_Hazards.md) — Night và weather effects on visibility.
