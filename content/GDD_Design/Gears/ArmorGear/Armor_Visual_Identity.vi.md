---
title: "giáp Visual Identity"
type: docs
weight: 6
---

## Tổng Quan

Tài liệu này định nghĩa **top-down silhouette**, **rarity color-coding**, **damage trạng thái visuals**, và **UI icons** for giáp so that class và condition are dễ đọc in a top-down extraction shooter. For class và item list Xem [giáp & Ballistics](giáp.md) và [giáp Master Database](Armor_Master_Database.md).

---

## Top-Down Silhouette Guide

In top-down view, giáp phải được dễ đọc from above. Differentiation is achieved via shoulder profile, color hint, và helmet shape.

| giáp class | Shoulder profile | Color hint | Helmet shape | Readability distance |
| :---------- | :--------------- | :--------- | :----------- | :------------------- |
| None | Slim, fabric | Neutral | None | N/A |
| Class 1–2 | Slim, slight pad | Light tan | Open bowl | ~3 tiles |
| Class 3 | Medium, plates | Olive / gray | Covered ears | ~4 tiles |
| Class 4 | Medium+, carrier | Dark green | Military | ~5 tiles |
| Class 5 | Wide, full plate | Dark gray | Full + visor | ~6 tiles |
| Class 6 | Very wide, tank | Black / dark | Enclosed | ~7 tiles |

**Design intent:** At combat range, Người chơi có thể estimate threat level (giáp tier) và choose engagement hoặc reposition. Heavier giáp is visually “bigger” và darker.

---

## Rarity Color-Coding

- **Ground loot:** Rarity shown by **outline glow** (e.g. White / Green / Blue / Purple / Orange) so Người chơi có thể prioritize mà không opening inventory.
- **Equipped:** No glow — equipped giáp is read by **silhouette và color hint** only, to avoid clutter và keep identification skill-based.

Rarity palette should match the rest of the game (e.g. Common = white, Uncommon = green, Rare = blue, Epic = purple, Legendary = orange).

---

## Damage trạng thái Visual

giáp condition (durability %) nên được hiển thị rõ on the nhân vật và in UI.

| Durability band | Visual on nhân vật | ghi chú |
| :-------------- | :------------------ | :---- |
| 100–75% | Clean | No damage cues |
| 74–50% | Scuff marks, slight discoloration | Clearly used |
| 49–25% | hiển thị rõ cracks/tears, darker | Clearly damaged |
| 24–0% | Heavy damage, red/dark overlay | Near-destroyed |

Helmets: visor cracks at low durability can obscure vision (Xem [giáp & Ballistics](giáp.md) — visors). Vests: torn fabric hoặc plate damage on the model.

---

## UI Icons

- **Inventory icon:** 2D icon với rõ outline, **class number badge** (1–6), và **durability bar** (e.g. green → yellow → red).
- **Tooltip:** Full stat preview — class, zones, hiện tại/max durability, material, weight, giá trị. Optional: “Effective class” khi durability is below 100% (e.g. “~Class 3.5” at 70% durability).

Icons nên được nhất quán in size và style với vũ khí và other gear; class badge ensures quick scan in stash và loot màn hình.

---

## Tham Chiếu Chéo

- [giáp Master Database](Armor_Master_Database.md) — Per-item class, weight, rarity.
- [vũ khí Visual & Audio Identity](../../vũ khí/Weapon_Visual_Audio_Identity.md) — Rarity và readability standards (align với vũ khí).
- [Visuals — Style Guide](../../Visuals/StyleGuide.md) — Color và UI consistency nếu present.
