---
title: "Clan & Guild System"
type: docs
weight: 20
---

## Overview

The Clan System provides a **persistent social organization layer** above squads — a shared identity, progression, and community hub that transforms individual players into a lasting faction. Clans reward long-term cooperation and create the social bonds that drive retention.

> **Cross-References:** [Home Screen & Lobby](HomeScreen_Design.md) — Clan tag + banner visible on operator nameplate; [Player Profile & Career Stats](PlayerProfile.md) — Clan membership shown on public profile; [Ranked Mode](RankedMode.md) — Clan leaderboards; [Live Ops](LiveOps.md) — Clan vs. Clan events (Faction Wars).

---

## 1. Design Philosophy

**Why Clans?** Solo players churn. Players with 3+ in-game friends retain at 2× the rate. Clans formalize friendships into a shared identity, creating:

- **Social accountability** — Log in for your clan, not just yourself
- **Shared goals** — Clan missions give purpose beyond personal gain
- **Status signaling** — Clan tag visible in-game → motivation to represent well
- **Long-term investment** — Clan upgrades over weeks/months → strong retention anchor

**Anti-patterns we avoid:**
-  Clan-gated content (non-clan players must feel complete without a clan)
-  Pay-to-win clan upgrades (all clan upgrades cosmetic or convenience, never power)
-  Mandatory clan activity (auto-kick never triggers without clear warning)

---

## 2. Clan Creation & Basics

### Requirements to Create a Clan

| Requirement | Value |
| :---------- | :---- |
| Account Level | 10+ |
| Clan creation cost | 5,000 Credits (one-time) |
| Clan Tag | 2–5 uppercase characters (e.g., [APEX], [WOLF]) |
| Clan Name | 3–24 characters; unique globally |
| Min members to keep tag | 2 (founder alone cannot benefit from clan perks) |
| Max members | 30 (expandable to 50 via Clan HQ upgrade) |

### Clan Profile

| Element | Content |
| :------ | :------ |
| **Clan Banner** | Choose from 12 base banners; unlock additional via milestones/shop |
| **Clan Emblem** | Layered icon builder (background + icon + overlay) |
| **Description** | Up to 280 characters — recruiting message, language, style |
| **Playstyle Tag** | Casual / Tactical / Competitive / Grinders (publicly shown) |
| **Privacy** | Open (auto-join) / Application (founder approves) / Closed (invite only) |
| **Region/Language** | Optional — helps search and TZ alignment |

---

## 3. Clan Ranks & Permissions

| Rank | Slot Limit | Permissions |
| :--- | :--------- | :---------- |
| **Founder** | 1 | All permissions; transfer or disband clan |
| **Co-Leader** | Up to 3 | Approve members, kick non-leaders, start clan missions |
| **Officer** | Up to 6 | Invite players, update MOTD |
| **Veteran** | Unlimited | Access Clan Bank; use Clan Buffs |
| **Member** | Unlimited | Standard — chat, play together, view clan stats |
| **Recruit** | Unlimited | Probation — clan chat only; cannot use Clan Bank for 48h |

**Transitions:**
- Founder manually promotes/demotes
- Founder inactive 30 days → Co-Leader auto-promoted to Founder (with notification)
- Members inactive 21 days → Auto-tagged "Inactive"; founder can mass-kick inactives

---

## 4. Clan Progression & Milestones

Clans earn **Clan XP** through member activity and shared achievements.

### Clan XP Sources

| Activity | Clan XP Earned |
| :------- | :------------- |
| Member completes a raid (any mode) | +5 per member |
| Member extracts successfully | +15 per member |
| Member kills boss | +30 per event |
| Clan mission completed | +200–1,000 |
| Clan event participation (Faction Wars) | +500 |
| Daily active members >50% | +100 bonus/day |

### Clan Level Milestones

| Level | Required XP | Unlock |
| :---- | :---------- | :----- |
| 1 | 0 | Clan created; basic banner; 30-member cap |
| 5 | 10,000 | Clan MOTD (message of the day) in-game |
| 10 | 30,000 | Clan Lounge (shared cosmetic space in home screen) |
| 15 | 75,000 | Clan Bank unlock (shared resource pool) |
| 20 | 150,000 | Expand cap to 50 members |
| 25 | 300,000 | Clan-exclusive cosmetic unlocked (unique banner + charm) |
| 30 | 500,000 | "Legendary Clan" title — exclusive animated banner |

---

## 5. Clan Missions

Clan Missions are cooperative challenges that require collective member contributions.

### Mission Types

| Type | Example | Duration | Reward |
| :--- | :------ | :------- | :----- |
| **Extraction Challenge** | "Clan extracts 50 times this week" | 7 days | Clan XP + Credits for all |
| **Boss Hunt** | "Kill 10 bosses as a squad" | 3 days | Rare weapon skin (clan-exclusive) |
| **Wealth Run** | "Extract $1,000,000 total loot in 5 days" | 5 days | Clan XP + economic rewards |
| **Combat Challenge** | "Clan members get 200 kills combined" | 7 days | Clan XP + operator charm |
| **Elite Mission** | "All squad extractions in 1 day — no deaths" | 24 hours | Legendary Clan XP boost |

**Mission rules:**
- 2 missions active simultaneously (Veteran+ rank chooses from 3 offered options)
- Progress updates in real-time on Clan Dashboard
- Members see each other's contributions ("Kai_V contributed 8 extractions")

---

## 6. Clan Bank

*Unlocks at Clan Level 15.*

A shared resource pool that Officers/Veterans can deposit into and members can request withdrawals from.

| Feature | Detail |
| :------ | :----- |
| **Deposit** | Any member can donate Credits to the Clan Bank |
| **Withdraw** | Requires Officer approval (or Auto-grant if below 5,000 credits) |
| **Max Balance** | 500,000 Credits (expandable with Clan Level) |
| **Audit Log** | Full history of deposits and withdrawals visible to all Officers |
| **Anti-abuse** | New members (Recruits) cannot withdraw for 48h; single withdrawal limit 10,000 Credits/day |

**Design intent:** Clan Bank enables clan-sponsored loadouts for members who died poorly equipped — reinforces "we take care of our own" culture.

---

## 7. Clan vs. Clan — Faction Wars Integration

Faction Wars (see [Live Ops](LiveOps.md)) is the primary competitive clan event:

| Step | Detail |
| :--- | :----- |
| **Choose faction** | Clan Leader aligns clan to a faction before event starts |
| **Contribution** | Each member's raids contribute points to faction score |
| **Clan leaderboard** | Separate leaderboard: "Top Clans by Contribution" |
| **Clan reward** | Top 3 contributing clans in winning faction → clan-exclusive banner |
| **Individual reward** | Members still earn personal rewards from faction placement |

**Clan Rivalry:** Two clans can declare each other a "Rival" — displays opponent's logo in clan dashboard; special notification when both squads are in the same match.

---

## 8. Clan UI Touchpoints

| Location | Clan UI |
| :------- | :------ |
| **Home Screen** | Clan tag [WOLF] under operator name; clan member count badge |
| **Loadout Prep** | Squad slots show clan tag if squadmates are clanmates |
| **In-Game** | Clan tag visible above operator nameplate |
| **Player Profile** | Clan emblem, rank, join date, contribution stats |
| **Leaderboards** | Clan rank shown next to player RP |
| **Post-Game Debrief** | Clan XP earned from this raid shown in results screen |

---

## Cross-References

- [Home Screen & Lobby](HomeScreen_Design.md) — Clan tag, banner, and member online count visible in home screen social panel.
- [Player Profile & Career Stats](PlayerProfile.md) — Clan membership, rank, and contribution visible on public career profile.
- [Ranked Mode](RankedMode.md) — Clan leaderboard tracks combined ranked RP; Squad Synergy Bonus applies to clanmates.
- [Live Ops](LiveOps.md) — Faction Wars event is the primary clan-vs-clan competition; clan missions align with event themes.
- [Economy](Economy.md) — Clan Bank uses Credits; clan cosmetics available in shop; clan creation cost = Credit sink.
