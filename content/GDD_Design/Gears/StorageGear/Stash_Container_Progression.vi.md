---
title: "Stash & Container Progression"
type: docs
weight: 5
---

## Tổng Quan

Tài liệu này định nghĩa **stash size** by edition và Safe House level, **container unlock path** (order và method), và **secure container upgrade path**. For container specs Xem [Storage Master Database](Storage_Master_Database.md). For full Stash design Xem [Stash Design](../../Stash_Design.md).

---

## Stash Size Progression

Stash is the người chơi’s persistent out-of-raid storage. **Stash capacity = total cells** (single grid; 10×28 = 280 cells, etc.). Grid size can increase với edition hoặc Safe House upgrades.

| Edition / source | Stash grid | Total cells | Unlock chi phí / note |
| :--------------- | :--------- | :---------: | :------------------ |
| Standard Edition | 10×28 | 280 | Free |
| Safe House Lvl 2 | 10×38 | 380 | 3.5M + materials |
| Safe House Lvl 3 | 10×48 | 480 | 8.5M + materials |
| Safe House Lvl 4 | 10×68 | 680 | 15M + materials |
| Premium Edition | 10×48 | 480 | Free (start) |
| Ultimate Edition | 10×68 | 680 | Free (start) |

All editions can reach the same maximum (e.g. 10×68) via Safe House; premium/ultimate start với a larger grid.

---

## Container Unlock Path

Order in which stash-only containers và chính tools become available. Exact levels và quest names are placeholders. Container unlock phase maps to **Storage Tier** in [Gear Tier hệ thống](../Gear_Tier_System.md) for consistency với loot và economy.

| Phase | Container (examples) | How to unlock | Estimated level |
| :---- | :------------------- | :------------ | :-------------- |
| Early | Keytool, Docs Case | Trader Lvl 1 purchase | 1–5 |
| Early–Mid | đạn Case, Scav Junkbox | Trader Lvl 2 hoặc craft | 10–15 |
| Mid | Med Case, Magazine Case | Trader Lvl 2 / quest | 15–20 |
| Mid–Late | vũ khí Case | Trader Lvl 3 / quest chain | 20–30 |
| Late | Items Case | Trader Lvl 3 / barter | 30–40 |
| Endgame | THICC Items, THICC vũ khí | Trader Lvl 4 / quest chain | 40+ |

---

## Secure Container upgrade Path

Secure container size is upgraded via quests hoặc edition; it is not purchased as a consumable. **Cells** in the bảng below = **total capacity** (Xem [Storage Master Database](Storage_Master_Database.md)).

| Container | Grid | Cells (total capacity) | Unlock method |
| :-------- | :--: | :---: | :------------ |
| Alpha | 2×2 | 4 | Default (all editions) |
| Beta | 2×3 | 6 | Quest (e.g. Punisher line, mid-game) |
| Gamma | 3×3 | 9 | Premium Edition hoặc quest (e.g. The Collector, late-game) |
| Kappa | 3×4 | 12 | Quest: complete all main quests (endgame prestige) |

Standard-edition Người chơi có thể reach Gamma/Kappa by progression; premium gives Gamma from the start. Kappa is progression-only (no edition shortcut).

---

## Tham Chiếu Chéo

- [Gear Tier hệ thống](../Gear_Tier_System.md) — Storage Tier (1–4) định nghĩa; container unlock phase maps to Tier.
- [Storage Master Database](Storage_Master_Database.md) — Secure containers, stash-only cases, values.
- [Inventory & Gear — Stash](../../Inventory_System/_index.md#8-stash--containers) — Stash overview, organization tips.
- [Safe House Design](../../GameDesign/Safe_House_Design.md) — Safe House levels, upgrade costs.
- [Progression](../../GameDesign/Progression.md) — người chơi và trader level framework.
- [Quest Objective hệ thống](../../Gameplay/Quest_Objective_System.md) — Quest gates for containers và secure upgrades.
