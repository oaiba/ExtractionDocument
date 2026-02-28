---
title: "Post-Game Debrief & Replay"
type: docs
weight: 21
---

## Overview

The Post-Game Debrief is the screen that appears immediately after a raid ends — whether through successful extraction, death, disconnection, or server end. It is the **most read screen in the game** after the stash: players spend significant time reviewing their performance, examining loot value, and understanding how they died. A well-designed debrief provides closure, learning, and motivation to queue again.

> **Cross-References:** [Core Gameplay Loop](CoreLoop.md) — Phase 5 Recovery; [Extraction Mechanics](Extraction_Mechanics.md) — extraction result codes; [Medical System](Medical_System.md) — body part HP summary in debrief; [Camera System](Camera_System.md) — death cam into debrief transition; [GameDesign/Progression](../../GameDesign/Progression.md) — XP gains displayed in debrief.

---

## Design Philosophy

- **Show the numbers, but make them feel earned.** Every XP point earned has a source — show it. Players who know why they earned XP are more likely to chase it next raid.
- **Death is a teacher, not a wall.** The debrief must answer "why did I die?" clearly. Death replay is the most important tool for player improvement.
- **Quick to leave.** Players who want to queue immediately should reach "Deploy Again" in ≤2 taps/clicks. Never lock the player in the debrief.
- **Calm and focused.** Post-raid is recovery time. The debrief UI should feel quieter than in-raid — dark theme, subdued music, no animations that demand attention.

---

## Debrief Sections

### 1. Outcome Banner

The first thing displayed — large, readable, emotive.

| Outcome | Banner Text | Color |
| :------ | :---------- | :---- |
| Extracted successfully | **"EXTRACTED"** | Gold |
| Died to enemy player | **"K.I.A."** | Red |
| Died to AI | **"ELIMINATED"** | Orange |
| Died to environment (bleed, contamination) | **"LOST"** | Dark red |
| MIA (disconnection/timeout) | **"MIA"** | Grey |
| Survived raid end (no extraction) | **"TIME OUT"** | Purple |

Below the banner: **survival time** (e.g., "14:32 survived") and **cause** (e.g., "Headshot by [Player Name]" or "AI Rifle · Industrial Zone").

---

### 2. XP Breakdown

Every XP source itemized in a scrollable list:

| XP Source | Example Value | Explanation |
| :-------- | :-----------: | :---------- |
| Raid survival bonus | +200 XP | Alive for 10+ minutes |
| Kills — AI (per kill) | +15 XP each | Standard AI reward |
| Kills — Boss | +300 XP | One-time per boss |
| Kills — Player (per kill) | +50 XP each | PvP reward |
| Extraction bonus | +500 XP | Only on successful extract |
| Quest objective completed | +250 XP each | Per objective (not per quest) |
| Damage dealt total | +1 XP per 10 damage | Traceable participation |
| Teammate revived | +150 XP per revive | Co-op reward |
| First extract of session | +100 XP | Daily first-extract bonus |
| **TOTAL** | **XXX XP** | Rolls up at bottom |

**XP bar animation:** After all line items display, the XP bar fills from current to new value. If leveling up, large level-up celebration plays.

---

### 3. Loot Summary

Items extracted this raid, with economy context:

| Column | Content |
| :----- | :------ |
| Item icon | 32×32 icon |
| Item name | Full item name |
| Qty | Stack count |
| Condition | % durability for gear items |
| Est. Value | Server's current flea market average (or trader buy price) |
| FIR status | ✅ (FIR) or ❌ (not FIR) |

**Total estimated value:** Sum of all extracted loot displayed at bottom of list.  
**Sort options:** By value (desc), by name, by category.

If the player **died** (no extraction): the list shows "LOST ITEMS" — everything that was in their inventory that was not in a Secure Container. Same format but highlighted red. Secure container items are shown separately as "KEPT" in green.

---

### 4. Combat Stats

Summary of in-raid combat performance:

| Stat | Description |
| :--- | :---------- |
| Kills (AI) | Total AI killed |
| Kills (Player) | Total player kills |
| Deaths | 0 (alive) or 1 (dead) |
| Damage Dealt | Total damage output |
| Damage Received | Total damage taken |
| Headshot % | Headshots / total hits × 100 |
| Longest kill | Distance of furthest confirmed kill |
| Accuracy | Shots landed / shots fired × 100 |
| Suppressed duration | Total seconds spent in suppressed state |
| Distance traveled | Total meters moved this raid |

---

### 5. Squad Summary

Shows squadmates' outcomes (even if they disconnected/died):

| Column | Content |
| :----- | :------ |
| Name | Player name |
| Status | Extracted / KIA / MIA |
| Operator | Operator used |
| Kills | AI + Player kills |
| Revives given | Times they revived a teammate |
| XP earned | Total XP this raid |

---

### 6. Death Replay ("How I Died")

Available only for players who died this raid. Server-generated, not client-generated (cannot be modified).

| Element | Detail |
| :------ | :----- |
| **Replay source** | Server-side tick recording. 10-second window before death + 3 seconds after. |
| **Perspective** | Top-down camera from player's position, standard in-game view. Player's LOS applies — cannot see the enemy before they were visible. |
| **Enemy shown** | Enemy is revealed in replay after death occurs — 2 seconds of showing who/what killed the player. |
| **Enemy info** | Shows: operator class; hit location; weapon type (not equipment details). Does NOT show enemy HP, inventory, or stash. |
| **Causes highlighted** | Hit marker overlays on replay timeline show each hit. Cause of death indicated. |
| **Skip** | Player can skip replay at any time. |
| **Save** | "Save this clip" button saves 13-second server replay to player's account (up to 10 clips stored). |

**Replay Unavailable Cases:**
- MIA death (disconnect — no death event to replay)
- Zone contamination death (replay shows contamination damage tick; no enemy to show)
- Server crash (no replay data)

---

### 7. Tips Contextual Panel

A single-line tip, contextually based on how the player died or performed:

| Death Cause | Tip Shown |
| :---------- | :-------- |
| Headshot (no helmet) | "Tip: Helmets reduce headshot damage significantly. Class 3 helmets stop most pistol rounds." |
| Bleed-out | "Tip: Carry a Bandage in your pockets for fast access during combat — you don't need to open inventory." |
| Extraction timer interrupted | "Tip: Incoming fire during extraction resets the timer. Use abilities or smokes to buy time." |
| AI boss kill | "Tip: Boss [Name] has a weak side — flank from the north entrance to avoid their forward fire arc." |
| Overweight at death | "Tip: Dropping low-value loot before extracting can move you to a lighter weight tier — and saving your run." |

Tips shown once per scenario — suppressed after player has seen it 3 times (settings reset available).

---

## Navigation & Flow

### Debrief Button Layout (PC)

| Button | Action | Location |
| :----- | :----- | :------- |
| **Deploy Again** | Immediately enters matchmaking with same loadout (if stash allows) | Bottom-right, primary |
| **Return to Stash** | Goes to main stash screen | Bottom-center |
| **Watch Replay** | Opens death replay (if available) | Bottom-left |
| **Share Clip** | Opens clip sharing UI for saved replay | Below replay button |
| **Report Player** | Opens report form pre-filled with killer info | Top-right (small) |

### Debrief Flow (Mobile)

Same sections; scrollable single column. Tabs at top: Summary / Loot / Stats / Replay. Deploy button always pinned to screen bottom.

---

## Economy Integration

The moment the debrief loads, item transfer is immediate:
- **Extracted items** are already in stash — shown with "NEW" badge.
- **Insurance** returns are scheduled; ETA shown in debrief (e.g., "Standard insurance returns in 22 hours").
- **Quest turn-in** items are flagged with quest name in loot list — click takes player to trader screen.
- **Trader XP** gained this raid shown in debrief header badge.

---

## Cross-References

- [Core Gameplay Loop](CoreLoop.md) — Phase 5 Recovery; debrief as start of next loop.
- [Extraction Mechanics](Extraction_Mechanics.md) — Extraction outcome codes; MIA rule.
- [Medical System](Medical_System.md) — Body part damage summary (in death context).
- [Camera System](Camera_System.md) — Death cam transition into debrief screen.
- [GameDesign/Progression](../../GameDesign/Progression.md) — XP values, level thresholds, XP bar.
- [Quest & Objective System](Quest_Objective_System.md) — Quest objectives flagged in debrief loot list.
- [Anti-Cheat & Fair Play](Anti_Cheat_Fair_Play.md) — Report player button in debrief.
