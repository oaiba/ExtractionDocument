---
title: "Loading Screen Data Schema"
type: docs
---

## Overview

This document defines the data structures for the Async Loading Screen system. Used by LoadingManager and ContentProvider to serve tips, fun facts, and configuration per loading type.

> **Design reference:** [Loading Screen Design](../../gdd_design/ui_ux/loadingscreen_design/index.html)

---

## 1. LoadingTip / LoadingContent

Stores individual loading screen content items (tips, fun facts, lore fragments).

### Schema (Data Table Row)

| Field | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| `id` | string | Yes | Unique identifier (e.g., `TIP_TACTICAL_001`) |
| `contentType` | enum | Yes | `Tip`, `FunFact`, `Intro`, `Lore` |
| `text` | string (localized) | Yes | Display text; use localization key |
| `attribution` | string (localized) | No | "— Salvage Corps" / "— Unknown Contractor" |
| `loadingTypes` | array\<LoadingType\> | Yes | Which loading screens show this: `[L3, L4, L6]` |
| `playerLevelMin` | int | No | Minimum account level to show (0 = all) |
| `category` | enum | Yes | `Tactical`, `Economy`, `Exploration`, `Operator`, `Lore`, `Faction` |
| `operatorId` | string | No | If category=Operator, which operator (e.g., `Mamba`) |
| `mapId` | string | No | If Intro, which map (e.g., `Sector7`) |

### ContentType Enum

| Value | Description |
| :---- | :---------- |
| `Tip` | Gameplay mechanic advice (in-character) |
| `FunFact` | Light lore, trivia |
| `Intro` | Map/zone name and brief context |
| `Lore` | Faction philosophy, lore fragments |

### Category Enum

| Value | Description |
| :---- | :---------- |
| `Tactical` | Combat, cover, flanking |
| `Economy` | Insurance, traders, selling |
| `Exploration` | Loot zones, map callouts, extraction |
| `Operator` | Operator-specific ability tips |
| `Lore` | Lore fragments, world-building |
| `Faction` | Faction philosophy |

### Example (JSON)

```json
{
  "id": "TIP_TACTICAL_001",
  "contentType": "Tip",
  "text": "Heavy bags make heavy noise. The Zone punishes greed.",
  "attribution": "— Salvage Corps field manual",
  "loadingTypes": ["L3", "L4", "L6"],
  "playerLevelMin": 0,
  "category": "Tactical"
}
```

```json
{
  "id": "FUNFACT_LORE_042",
  "contentType": "FunFact",
  "text": "Day 1,247. The radio still plays Nexus Corp's automated welcome message. Nobody's listening.",
  "attribution": "— Recovered journal",
  "loadingTypes": ["L3", "L4"],
  "playerLevelMin": 5,
  "category": "Lore"
}
```

---

## 2. LoadingScreenConfig

Per-loading-type configuration. One row per LoadingType.

### Schema (Data Table Row)

| Field | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| `loadingType` | enum | Yes | `L1`, `L2`, `L3`, `L4`, `L5`, `L6`, `L7`, `L8` |
| `minDisplayTime` | float | No | Minimum seconds to show (prevents flicker); default 1.0 |
| `backgroundImagePool` | array\<AssetRef\> | No | Image assets for background |
| `allowVideo` | bool | No | Whether video trailer is allowed; default false |
| `videoAssetRef` | AssetRef | No | Optional video asset (season/map trailer) |
| `tipRotationInterval` | float | No | Seconds between auto tip rotation; default 8.0 |
| `progressStyle` | enum | Yes | `Bar`, `Spinner`, `Percentage` |
| `showSquadWidget` | bool | No | Show squad status (L4 only); default false |
| `skipAllowed` | bool | No | Allow skip (L2 only); default true |
| `skipDelaySeconds` | float | No | Seconds before skip enabled (L2); default 1.0 |

### ProgressStyle Enum

| Value | Description |
| :---- | :---------- |
| `Bar` | Horizontal progress bar |
| `Spinner` | Circular spinner |
| `Percentage` | Numeric percentage only |

### Example (JSON)

```json
{
  "loadingType": "L4",
  "minDisplayTime": 2.0,
  "backgroundImagePool": ["Map_Sector7_Loading", "Map_District14_Loading"],
  "allowVideo": true,
  "tipRotationInterval": 8.0,
  "progressStyle": "Bar",
  "showSquadWidget": true
}
```

```json
{
  "loadingType": "L2",
  "minDisplayTime": 1.0,
  "progressStyle": "Spinner",
  "skipAllowed": true,
  "skipDelaySeconds": 1.0
}
```

---

## 3. Asset References

- **Background images:** 1920×1080 or 16:9; format PNG/JPEG
- **Video:** MP4, max 30s loop; muted by default
- **Localization:** All `text` and `attribution` use keys (e.g., `LOADING_TIP_TACTICAL_001`)

---

## 4. Cross-References

- [Loading Screen Design](../../gdd_design/ui_ux/loadingscreen_design/index.html) — Taxonomy, layouts, content mapping
- [Lore Delivery](../../gdd_design/story/lore_delivery/index.html) — Loading screen tip format and examples
- [UI System](../systems/uisystem/index.html) — LoadingType enum, ScreenType mapping
