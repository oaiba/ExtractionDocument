---
title: "vũ khí Attachment hệ thống"
type: docs
weight: 23
---

## Tổng Quan

The vũ khí Attachment hệ thống allows người chơi to modify their vũ khí trước raids (in the Stash và Workbench) và — to a limited degree — in-raid với found attachments. Attachments tạo meaningful gear customization that reinforces the game's **Preparation Phase** và provides giá trị for high-tier loot found trong khi raids.

> **Cross-References:** [Gear cơ chế](Gear_Mechanics.md) — vũ khí weight contribution to encumbrance; [Looting & Inventory](Looting_Interactions.md) — attachments as loot category (FIR status); [Safe House Design](../GameDesign/Safe_House_Design.md) — Workbench crafting of attachments; [Loot bảng Design](Loot_Table_Design.md) — attachment spawn rates by zone tier; [Combat Feel (Top-Down)](Combat_Feel_Topdown.md) — aim cone, recoil hệ thống that attachments directly modify; [Quest & Objective hệ thống](Quest_Objective_System.md) — Viktor quest chain unlocks vũ khí mod blueprints.

---

## Nguyên Tắc Thiết Kế

- **Every attachment has trade-offs.** No attachment is a pure upgrade. Adding a suppressor reduces velocity; adding a heavy barrel improves accuracy nhưng increases weight. người chơi make deliberate choices.
- **Top-down visibility matters.** vũ khí length, muzzle flash size, và suppressor barrel extension are hiển thị rõ in the top-down camera. Visual feedback reinforces the modification's mục đích.
- **Workbench dependency.** Full vũ khí modding requires Workbench Lvl 1+ in the Safe House. Người chơi có thể swap attachments freely in stash; fabrication requires the Workbench.
- **In-raid scavenging.** Compatible attachments found in-raid can be installed on the vũ khí at a 5-second interaction chi phí. This is high-risk (standing still) nhưng high-reward (free upgrade mid-raid).
- **Durability tracking.** Attachments degrade với cách dùng. A suppressed vũ khí sau heavy fire will have a worn suppressor — reducing effectiveness until repaired at Workbench.

---

## Attachment Slots (Per vũ khí)

Not all vũ khí have all slots. Slot availability is per vũ khí type và model.

| Slot | Attachment Category | Affects |
| :--- | :------------------ | :------ |
| **Muzzle** | Suppressor, Muzzle Brake, Compensator, Flash Hider | Sound (range audible), recoil, muzzle flash visibility |
| **Barrel** | Short Barrel, Standard Barrel, Heavy Barrel, Lined Barrel | Accuracy, velocity, vũ khí length (visual) |
| **Stock** | Folded Stock, Standard Stock, Heavy Stock | Recoil recovery rate, aim stability, vũ khí weight |
| **Grip** | Vertical Grip, Angled Grip, Folded Grip, No Grip | Recoil horizontal control, stability on hipfire |
| **Rail (Top)** | Iron Sights, Red Dot, Holographic Sight, ACOG, Night Vision Scope | Zoom level, ADS clarity, low-light operations |
| **Rail (Side)** | Tactical Flashlight, Laser Sight | Aim cone at hipfire (laser), ambient lighting (flashlight — limited in top-down) |
| **Underbarrel** | Grenade Launcher, Bipod, Foregrip | Special (GL), prone accuracy (bipod), stability (foregrip) |
| **Magazine** | Standard, Extended, Drum, Compact | đạn capacity, vũ khí weight, reload speed |

> **Pistols** have fewer slots: Muzzle, Grip, Sight, Magazine only.
> **Bolt-action snipers** lack Grip và Stock variety; emphasis on Barrel và Sight.

---

## Attachment Types — Full Reference

### Muzzle Attachments

| Attachment | Sound Range Effect | Recoil Effect | Weight | Visual (Top-Down) |
| :--------- | :----------------- | :------------ | :----- | :---------------- |
| **Suppressor (9mm)** | −60% audible range (from 40m → 16m) | +0.5° base cone (velocity loss) | +0.3 kg | Extended barrel hiển thị rõ; no flash |
| **Suppressor (5.56)** | −50% audible range | +0.3° base cone | +0.4 kg | Same |
| **Suppressor (7.62)** | −45% audible range | +0.2° base cone | +0.6 kg | Larger suppressor silhouette |
| **Muzzle Brake** | No change (loud) | −1° max recoil bloom | +0.1 kg | Short stubby end piece; full flash |
| **Compensator** | No change | −0.3°/shot horizontal drift | +0.1 kg | Small vented cone; full flash |
| **Flash Hider** | No change | −0.2° random bloom | +0.1 kg | Forked tip; flash reduced 50% |
| **No Muzzle (bare)** | Full sound range | Base stats | 0 kg | Short barrel, large flash |

**Suppressor durability:** Suppressors degrade at 1 durability per 15 shots. At 50% durability: −20% sound reduction (50m → 30m). At 20%: minimal effect. Replace hoặc repair at Workbench.

---

### Barrel Attachments

| Attachment | Accuracy | Bullet Velocity | Range Penalty | Weight | ghi chú |
| :--------- | :------- | :-------------- | :------------ | :----- | :---- |
| **Short Barrel** | −1° aim cone | −15% velocity → slight damage drop at range | −0 (shorter vũ khí, easier indoor cách dùng) | −0.2 kg | Best for CQB; poor at 35m+ |
| **Standard Barrel** | Base | Base | Base | 0 kg | Default; balanced |
| **Heavy Barrel** | +0.5° accuracy improvement (tighter cone) | +10% velocity → flatter trajectory | None | +0.3 kg | Best at range; heavier |
| **Lined Barrel** | +0.3° accuracy | No velocity change | None | +0.4 kg | Compensated accuracy via rifling; premium option |

---

### Stock Attachments

| Attachment | Recoil Recovery | Aim Stability (moving) | Weight | ghi chú |
| :--------- | :-------------- | :--------------------- | :----- | :---- |
| **No Stock (folded/removed)** | −30% recovery rate | −2° additional cone while moving | −0.3 kg | Extreme CQB; fast movement priority |
| **Standard Stock** | Base | Base | 0 kg | Balanced |
| **Heavy Stock** | +20% recovery rate | +1° stability (less bloom trong khi sustained fire) | +0.4 kg | Best for LMG/DMR sustained; slows movement |
| **Folding Stock (expanded)** | +10% recovery | Base | +0.1 kg | Slight improvement; no downside |

---

### Sight / Optics

| Sight | Zoom Level | ADS Clarity | thời gian to ADS | Weight | ghi chú |
| :---- | :--------: | :---------- | :---------- | :----- | :---- |
| **Iron Sights** | ×1.0 | Standard | Fastest (0.15s) | 0 kg | Default; no obscured FOV |
| **Red Dot Sight** | ×1.2 | rõ | 0.2s | +0.1 kg | Best all-round; no magnification |
| **Holographic** | ×1.3 | Very rõ | 0.2s | +0.15 kg | Wider field; premium clarity |
| **ACOG (×4)** | ×4.0 | Magnified | 0.35s | +0.3 kg | Mid-long range; tunnel-vision close |
| **Sniper Scope (×8)** | ×8.0 | Full zoom | 0.5s | +0.4 kg | Sniper-only; Xem [Camera hệ thống](Camera_System.md) zoom interaction |
| **Night Vision Scope** | ×2.0 / NV | NV-only at night | 0.4s | +0.5 kg | Night raids only; useless in daylight |

> **Top-down ADS:** In top-down perspective, "ADS" functions as the người chơi entering "precision aim" mode. The camera does not zoom in like FPS. Instead, the aim cone tightens và the cursor anchors more firmly. Optic zoom affects the vũ khí overlay reticle và a slight camera zoom (+1 level) per [Camera hệ thống](Camera_System.md).

---

### Magazine Attachments

| Magazine | Capacity | Reload Speed | Weight | ghi chú |
| :------- | :------: | :----------- | :----- | :---- |
| **Compact Magazine** | −30% rounds | −0.4s reload | −0.2 kg | CQB builds; smaller profile |
| **Standard Magazine** | Base capacity | Base (2.4s AR) | 0 kg | Default |
| **Extended Magazine** | +50% rounds | +0.5s reload (heavier) | +0.2 kg | Sustained fire; useful for LMG builds |
| **Drum Magazine** | ×2.5 rounds | +1.5s reload (very slow) | +0.5 kg | High-risk, high-capacity; LMG specialty |
| **Quad-Stack** | +30% rounds | +0.3s reload | +0.15 kg | AR mid-range option |

---

### Underbarrel Attachments

| Attachment | Function | Restrictions | Weight |
| :--------- | :------- | :----------- | :----- |
| **Vertical Grip** | −0.3° horizontal recoil per shot | Requires underbarrel rail | +0.2 kg |
| **Angled Grip** | −15% ADS thời gian; +0.2° cone at hipfire | Requires underbarrel rail | +0.15 kg |
| **Bipod** | Prone only: aim cone becomes 0.2° (pinpoint) | phải được prone to deploy | +0.3 kg |
| **Grenade Launcher (M203)** | Fires 1 grenade round (explosive); separate đạn slot | AR-class only; Workbench Lvl 3 to craft | +0.8 kg |

---

## In-Raid Attachment Swapping

Người chơi có thể install found attachments trong khi a raid:

| Step | chi tiết |
| :--- | :----- |
| 1 | Find a compatible attachment in a container (FIR status — can be used in quest later) |
| 2 | Open inventory — drag attachment to vũ khí slot |
| 3 | Compatibility check: vũ khí model phải được compatible (shown as green slot hoặc red X) |
| 4 | nếu compatible: 5-second installation animation (người chơi is stationary và vulnerable) |
| 5 | Old attachment (nếu any) goes to người chơi inventory; new one installed |
| 6 | On death: all attachments on vũ khí are loot-able as separate items hoặc as vũ khí-với-attachments |

**Incompatibility:** Each vũ khí has a defined list of compatible attachment models. A 5.56 suppressor does not fit a 9mm barrel. Mounting type matters (NATO rail vs. proprietary mount).

---

## vũ khí Preset hệ thống (Pre-Raid)

Người chơi có thể save **named vũ khí presets** in the stash:

| tính năng | chi tiết |
| :------ | :----- |
| **Save preset** | Name + hiện tại attachment configuration saved for that vũ khí base model |
| **Load preset** | One-click applies saved attachment config (requires attachments to be in stash) |
| **Missing attachment cảnh báo** | nếu a saved preset component is missing (used, sold, hoặc lost), that slot shows "MISSING" với an orange badge |
| **Max presets** | 20 presets total (across all vũ khí) at Stash Level 2; 10 at Stash Level 1 |
| **Import/export** | Presets can be shared as text codes (import tính năng) — community sharing of builds |

---

## Crafting Attachments (Workbench)

Per [Safe House Design](../GameDesign/Safe_House_Design.md) Workbench recipes:

| Workbench Level | Craftable Attachments |
| :-------------- | :-------------------- |
| **Level 1** | Basic suppressor (9mm), Standard magazines, Iron sights |
| **Level 2** | Compensator, Extended magazines, Red Dot Sight, Vertical Grip |
| **Level 3** | Heavy Barrel, ACOG scope, Drum Magazine, Grenade Launcher, Night Vision Scope |

Attachment crafting consumes cụ thể materials per [Loot bảng Design](Loot_Table_Design.md) — cơ chế parts, wires, metal pipes, springs.

---

## Attachment Compatibility Chart (Sample — AR Class)

| vũ khí Model | Compatible Suppressor | Compatible Barrels | Compatible Rails |
| :----------- | :-------------------- | :------------------ | :------------- |
| M4A1 | 5.56 Suppressor, Flash Hider, Comp | Standard, Heavy, Short, Lined | NATO Picatinny (all sights/grips) |
| AK-74M | 7.62 Suppressor, Muzzle Brake | Standard, Short, Heavy | AK Side Rail (limited sights) |
| HK416 | 5.56 Suppressor, Flash Hider | All barrel types | NATO Picatinny (all sights/grips) |
| SIG MCX | 5.56 Suppressor | Standard, Short, Lined | M-LOK (requires adapter for NATO) |

> Full compatibility bảng per vũ khí to be chi tiết in the **vũ khí & Firearms GDD** (planned, linked from Combat section).

---

## Weight Contribution to Loadout

All attachments add weight to the vũ khí, which counts toward total encumbrance per [Gear cơ chế](Gear_Mechanics.md):

| Build Type | Typical Attachment Weight | Total vũ khí Weight (AR) |
| :--------- | :------------------------: | :----------------------: |
| **Bare minimum** (iron sights, no extras) | +0 kg | ~3.5 kg |
| **CQB build** (suppressor, short barrel, compact mag) | +0.5 kg | ~4.0 kg |
| **Balanced build** (red dot, standard, comp) | +0.6 kg | ~4.1 kg |
| **Heavy DMR build** (ACOG, heavy barrel, bipod) | +1.0 kg | ~4.5 kg |
| **Full chad** (NV scope, suppressor, drum, GL) | +2.2 kg | ~5.7 kg |

A heavy-modded vũ khí can push a người chơi from Tier 2 (moderate) to Tier 3 (heavy) carry weight — directly affecting sprint speed và stamina.

---

## Tham Chiếu Chéo

- [Gear cơ chế](Gear_Mechanics.md) — vũ khí weight contribution to total encumbrance và weight tier.
- [Combat Feel (Top-Down)](Combat_Feel_Topdown.md) — Aim cone bloom, recoil recovery rates modified by attachments.
- [Looting & Inventory](Looting_Interactions.md) — Attachments as separate loot items; FIR status; inventory slots.
- [Safe House Design](../GameDesign/Safe_House_Design.md) — Workbench crafting of attachments; level gates.
- [Loot bảng Design](Loot_Table_Design.md) — Attachment spawn rates; tier 3/4 zones for rare attachments.
- [Quest & Objective hệ thống](Quest_Objective_System.md) — Viktor quest chain unlocks vũ khí mod blueprints.
- [Camera hệ thống](Camera_System.md) — vũ khí zoom interaction với optics in top-down perspective.
