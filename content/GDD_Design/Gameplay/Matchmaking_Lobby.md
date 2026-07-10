---
title: Matchmaking & Lobby System
type: docs
weight: 13
---


### Overview

The matchmaking and lobby system is the gateway between the stash (out-of-raid hub) and the live raid. It determines how players are grouped, how servers are allocated, how the pre-raid preparation flow works, and how failure cases (disconnections, low population) are handled. A good matchmaking experience is invisible — players simply press "Deploy" and find themselves in a balanced, fair raid without waiting.

> **Cross-References:** [Core Gameplay Loop](CoreLoop.md) — Phase 1 Preparation; [Extraction Mechanics](Extraction_Mechanics.md) — disconnection timeout rule; [Controls](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Controls.md) — platform-specific lobby UI input; [Hero Abilities](Hero_Abilities.md) — operator selection before deploy.

***

### Raid Configuration

#### Squad Sizes

| Mode      | Min Players | Max Players | Notes                                           |
| --------- | ----------- | ----------- | ----------------------------------------------- |
| **Solo**  | 1           | 1           | Full raid access; solo-viable by design         |
| **Duo**   | 2           | 2           | Friends only (no solo fill into duo)            |
| **Squad** | 2           | 3           | Standard team size. Can deploy with 2/3 filled. |

**Design decision:** No 4- or 5-player squads. The 3-player maximum is deliberate — balances cooperation without creating overwhelming firepower asymmetry against solo players. See [Core Gameplay Loop](CoreLoop.md) for squad philosophy.

#### Players per Server Instance

| Instance Type                    |  Player Count | Rationale                                                        |
| -------------------------------- | :-----------: | ---------------------------------------------------------------- |
| **Standard Raid**                | 16–20 players | Dense enough for encounters; sparse enough for stealth viability |
| **Quick Raid** (15-min mode)     | 12–16 players | Smaller map, shorter timer, fewer players                        |
| **Solo Match** (future optional) |  8–12 players | If solo mode gains dedicated server pool                         |

**Fill logic:** Server instances deploy when ≥80% of capacity is filled OR when the matchmaking queue holds 8+ players for >45 seconds (whichever comes first). Partial-fill raids are valid — a 12-player of 20 raid is balanced and preferred over extended wait times.

***

### Queue System

#### Queue Types

| Queue                   | Description                                                                                                                                              | Priority                   |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| **Standard**            | Default — all players together in regional pool                                                                                                          | Primary                    |
| **Friends Only**        | Invite-only private raid. No strangers. Full server population must be filled by invites.                                                                | Optional (private session) |
| **Training / Tutorial** | AI-only server. No other players. Tutorial-exclusive.                                                                                                    | Forced for first-timer     |
| **Ranked**              | Rated matchmaking pool (separate from casual). See [RankedMode](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/RankedMode.md). | Separate pool              |

#### Matchmaking Assumptions

Matchmaking is a design contract, not only a technical queue. The player should know what rules they are entering before the server is reserved.

| Assumption | Rule | Player-Facing Requirement |
| :--- | :--- | :--- |
| Regional-first queue | Best-ping region is preferred before expansion | Show region and estimated latency when queue starts |
| Soft new-player protection | First raids can be weighted toward lower-density or tutorial-safe pools | Do not label this as easy mode; present it as onboarding protection only if needed |
| Gear value is not MMR | Expensive kits do not force high-skill lobbies | Avoid implying paid or expensive gear changes matchmaking |
| Party leader owns queue selection | Leader chooses mode, map, squad fill, and region | Squad members see the selected contract before readying |
| Low-pop fallback is allowed | Queue may start lower-density rather than wait indefinitely | Show "lower-density raid" if it changes expected player count materially |
| Ranked and event pools are separate | Ranked/event rules do not silently mix with casual rules | Mode card must show pool, penalties, rewards, and special extraction rules |
| Tutorial pool is protected | First tutorial is AI-only unless explicitly replaying with a squad | Standard queue remains locked until tutorial exit condition is met |
| Reconnect before loss | Disconnect creates a reconnect window before MIA resolution | Loading/reconnect UI must show remaining window and consequence |
| Server crash rollback | Invalid server result restores pre-raid loadout snapshot | Debrief uses rollback copy, not KIA/MIA copy |

#### Matchmaking Algorithm

The standard queue uses **regional pool matching** with a progressive expansion timeout:

```
Queue enters
    |
 Phase 1 (0–30s): Match players in same region with similar recent raid outcomes
    |── No match found → Phase 2
    |
 Phase 2 (30–60s): Expand to same region, any recent outcomes
    |── No match found → Phase 3
    |
 Phase 3 (60–90s): Cross-region join nearest available server
    |── No match → Phase 4
    |
 Phase 4 (90s+): Place in sub-optimal fill session or force-start lower-density raid
```

**No strict SBMM (Skill-Based Matchmaking):** Extraction shooters structurally resist SBMM because gear disparity is intentional. A "Rat" player with cheap gear can outplay a "Chad" with skill. True SBMM would undermine the economy-driven risk system. We use **soft behavioral grouping** instead:

| Behavioral Signal                                | Action                                                                                                |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| Player's last 5 raids: all died within 2 minutes | May preferentially fill low-density servers (fewer total players per instance — learning environment) |
| Player's recent gear value > $80,000 average     | No change — gear value is not a matchmaking signal                                                    |
| Player account < 10 raids total                  | Routed to Tutorial server; cannot join standard queue                                                 |
| Player flagged for cheating                      | Isolated matchmaking pool (honeypot server)                                                           |

This is the **Aggression-Based Matchmaking (ABMM)** concept inspired by ARC Raiders — not a binary split, but a softer signal to help early players without protecting them indefinitely.

***

### Lobby Screen Flow

#### Pre-Raid Flow

```
MAIN STASH SCREEN
    |
 [1] Player clicks "Deploy to Raid"
    |
 [2] MAP SELECTION (if multiple maps available)
     - Map preview (thumbnail, loot density badge, weather info)
     - Expected raid timer shown
     - Approximate queue time shown
    |
 [3] LOADOUT CONFIRMATION
     - Current equipped loadout displayed
     - Insurance status confirmed (insured / not insured)
     - Operator selection (change allowed here)
     - "Edit Loadout" button returns to stash
    |
 [4] FINDING MATCH (queue spinner)
     - Timer shows queue duration
     - Cancel button available (full cancel, no penalty)
     - Squad members' ready status shown
    |
 [5] MATCH FOUND — DEPLOY BRIEFING
     - Weather at deployment: shown (see Environmental_Hazards.md briefing rule)
     - Time of day: shown
     - Squad confirmed: shown
     - 10-second countdown before deployment (can cancel in this window)
    |
 [6] LOADING SCREEN (L4_LobbyToMatch)
     - Loading type: L4_LobbyToMatch per [Loading Screen Design](../UI_UX/LoadingScreen_Design.md)
     - Map-specific loading screen art (full-bleed background)
     - Tactical tips, fun facts, lore (rotate every 8s; manual paging)
     - Map intro text (e.g., "Sector 7 — Industrial Decay")
     - Squad status widget (ready indicators)
     - Progress bar + server region displayed
     - Optional: map flythrough video
    |
 [7] IN-RAID SPAWN
```

#### Lobby Screen — Squad Integration

| Feature                     | Behavior                                                                                                                              |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Party creation**          | From Friends list or in-game social screen. Party leader controls map and queue type selection.                                       |
| **Party size limit**        | 3 players maximum.                                                                                                                    |
| **Loadout visibility**      | Squad members CAN see each other's operator choice but NOT detailed gear/inventory (privacy).                                         |
| **Ready-up**                | Required from all members before departure. If one member is not ready after 60s, deploy continues without them (partial squad join). |
| **Squad communication**     | Voice and text chat active in lobby. Same channels as in-raid.                                                                        |
| **Operator duplicate rule** | Same operator CAN be used by multiple squad members. Ability stacking rule applies in-raid per [Hero Abilities](Hero_Abilities.md).   |

***

### Reconnect & Disconnection

#### Disconnection Behavior

Per [Extraction Mechanics](Extraction_Mechanics.md): disconnect → 5-minute MIA timeout → gear lost. The lobby system augments this:

| Scenario                      | Behavior                                                                                                          |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Disconnect < 5 min**        | Server holds player's raid slot. Reconnect window active. Player spawns back in their last safe position.         |
| **Reconnect within 5 min**    | Player returns to raid. HP and status effects preserved. LOS fog reset (must re-scout).                           |
| **Reconnect failed (>5 min)** | Character is removed from raid as MIA. Gear loss rules apply.                                                     |
| **Squad member disconnects**  | Squad can continue. Disconnected player's character remains for 5 min. Squad cannot loot a disconnected ally.     |
| **Host migration**            | Sessions are server-authoritative. There is no "host." Disconnect of any player does not affect server stability. |
| **Server crash**              | Rare case — all players MIA. No gear loss (server-side rollback to pre-raid loadout). Exception case.             |

**Mobile-specific:** On mobile, background app suspension is treated as a short disconnect. If suspended <30s and reconnected, treated as connectivity hiccup — no MIA timer started. If suspended >30s, MIA timer begins.

***

### Cross-Platform Matchmaking

The game targets PC, Console, and Mobile players in shared pools:

| Scenario                               | Design Choice                                                                                                                                                |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **PC + Console + Mobile in same raid** | Yes — same rules, same server. No mechanical difference.                                                                                                     |
| **Aim assist on mobile**               | Mobile receives aim assist on ability targeting per [Hero Abilities](Hero_Abilities.md). Regular weapon aiming: aim assist enabled (adjustable in settings). |
| **PC players vs Mobile**               | No automatic separation. Players can opt-in to "Platform Restricted" mode (only own platform), accepting potentially longer queues.                          |
| **Input detection**                    | Server identifies input type for metrics only. Not used for matchmaking decisions.                                                                           |
| **Performance parity**                 | Server-authoritative validation prevents client-side advantage. Mobile and PC are identical in hit registration and LOS outcomes.                            |

***

### Server Region & Latency

| Region             | Server Location | Expected Ping (local) |
| ------------------ | --------------- | --------------------- |
| Southeast Asia     | Singapore       | <50ms                 |
| East Asia          | Tokyo / Seoul   | <60ms                 |
| Europe             | Frankfurt       | <50ms                 |
| North America East | Virginia        | <50ms                 |
| North America West | Oregon          | <50ms                 |
| South America      | São Paulo       | <80ms                 |
| Oceania            | Sydney          | <80ms                 |

**Auto-selection:** Default is best-ping region. Players can manually pin a specific region (accepts higher latency).

**Cross-region join:** When queue times exceed 90s (Phase 3), players are placed in the nearest adjacent region server with <150ms ping. Raids do not mix players across >150ms differential to prevent latency advantage.

***

### Private / Friends Raid

For content creators, clan practices, or private group play:

| Property                   | Value                                                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Unlock**                 | Account level 5 or Tutorial completed                                                                                    |
| **Minimum players**        | 2 (cannot solo a private raid — anti-economy exploit prevention)                                                         |
| **Maximum players**        | Full server capacity (20 standard, 16 quick)                                                                             |
| **AI presence**            | Full AI population (same as public raid)                                                                                 |
| **Economy impact**         | Loot and XP earned counts toward progression. Insurance applies.                                                         |
| **Restriction**            | Cannot complete faction quests in private raid (prevents coordinated farming).                                           |
| **Known player locations** | All players in private session see each other as "friendly" on minimap (optional: can disable for competitive practice). |

***

### Tutorial / First-Time Matchmaking

New accounts (0 raids) are routed differently:

| Step                             | Behavior                                                                                                                                        |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Account created                  | Forced into Tutorial Raid before standard queue access                                                                                          |
| Tutorial Raid                    | AI-only server. No other players. See [TutorialRaid](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/TutorialRaid.md). |
| Tutorial Raid exit (any outcome) | Standard queue unlocked.                                                                                                                        |
| First 5 standard raids           | Soft-weighted toward lower-density instances. Not enforced — just weighted.                                                                     |
| Account level 5                  | All matchmaking restrictions lifted. Full access to all queues.                                                                                 |

***

### Anti-Abuse in Matchmaking

| Abuse Vector                      | Prevention                                                                                                  |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Alt-account griefing**          | New accounts can only hold Tier 1 gear for first 5 raids. Cannot bring $80k loadouts to harass new players. |
| **Queue dodging**                 | Cancel-and-rejoin within 60s causes a 2-minute queue cooldown.                                              |
| **IP abuse (VPN region exploit)** | Region is determined by server ping validation, not self-report. VPN cannot fake low-ping region access.    |
| **Smurf accounts**                | Behavioral signals (high XP-per-minute when account is "new") can flag for review. Not auto-penalized.      |
| **Private raid economy exploit**  | Quest completions disabled in private raids. Loot still earnable to prevent complete restriction.           |

***

### Lobby UI Specifications

#### PC / Console Layout

| Section              | Position           | Content                                                           |
| -------------------- | ------------------ | ----------------------------------------------------------------- |
| **Map selection**    | Center             | Map thumbnail, weather, timer, queue count                        |
| **Loadout summary**  | Right panel        | Operator icon, weapon thumbnails, armor, weight, insurance status |
| **Operator select**  | Right panel top    | 3 operator slots; current equipped shown                          |
| **Insurance toggle** | Right panel bottom | Cost display; toggle per-item or blanket                          |
| **Squad panel**      | Left panel         | Squad member cards: name, operator, status (ready/not ready)      |
| **Queue status**     | Top center         | "Searching...", timer, region                                     |
| **Deploy button**    | Bottom center      | Large, prominent. Requires all squad ready.                       |
| **Cancel queue**     | Bottom right       | Small; available at any point before deployment countdown         |

***

### Summary of Key Decisions

| Topic                    | Decision                                                                  |
| ------------------------ | ------------------------------------------------------------------------- |
| **Max squad size**       | 3 players. No 4- or 5-player squads.                                      |
| **Players per instance** | 16–20 (standard); 12–16 (quick raid).                                     |
| **SBMM**                 | No strict SBMM. Soft behavioral weighting for new players only.           |
| **Cross-platform**       | Same pool for PC/Console/Mobile. Optional platform restriction available. |
| **Private raids**        | Available at account level 5. Quests disabled in private.                 |
| **Disconnect**           | 5-min reconnect window. Server holds slot. Mobile background: 30s grace.  |
| **Queue expansion**      | 4-phase: regional → cross-regional. Force-starts at 90s if needed.        |

***

### Cross-References

* [Loading Screen Design](../UI_UX/LoadingScreen_Design.md) — L4\_LobbyToMatch taxonomy, content types, layout.
* [Core Gameplay Loop](CoreLoop.md) — Preparation phase; loadout philosophy.
* [Extraction Mechanics](Extraction_Mechanics.md) — Disconnection MIA rule; reconnect behavior.
* [Hero Abilities](Hero_Abilities.md) — Operator selection; ability stacking rule for same-class duplicates.
* [Environmental Hazards](Environmental_Hazards.md) — Weather shown at briefing screen.
* [Controls](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Controls.md) — Platform-specific lobby input.
* [GameDesign/RankedMode](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/RankedMode.md) — Ranked queue pool and requirements.
* [GameDesign/TutorialRaid](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/TutorialRaid.md) — First-time player routing.
