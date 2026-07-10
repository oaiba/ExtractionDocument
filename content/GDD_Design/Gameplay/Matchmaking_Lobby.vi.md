---
title: "Matchmaking & Lobby hệ thống"
type: docs
weight: 13
---

### Tổng Quan

The matchmaking và lobby hệ thống is the gateway between the stash (out-of-raid hub) và the live raid. It determines how người chơi are grouped, how servers are allocated, how the pre-raid preparation flow works, và how failure cases (disconnections, low population) are handled. A good matchmaking trải nghiệm is invisible — người chơi simply press "Deploy" và find themselves in a balanced, fair raid mà không waiting.

> **Cross-References:** [cốt lõi Gameplay Loop](CoreLoop.md) — Phase 1 Preparation; [Extraction cơ chế](Extraction_Mechanics.md) — disconnection timeout rule; [Controls](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Controls.md) — platform-cụ thể lobby UI input; [Hero Abilities](Hero_Abilities.md) — operator selection trước khi deploy.

***

### Raid Configuration

#### Squad Sizes

| Mode      | Min người chơi | Max người chơi | ghi chú                                           |
| --------- | ----------- | ----------- | ----------------------------------------------- |
| **Solo**  | 1           | 1           | Full raid access; solo-viable by design         |
| **Duo**   | 2           | 2           | Friends only (no solo fill into duo)            |
| **Squad** | 2           | 3           | Standard team size. Can deploy với 2/3 filled. |

**Design quyết định:** No 4- hoặc 5-người chơi squads. The 3-người chơi maximum is deliberate — balances cooperation mà không tạo overwhelming firepower asymmetry against solo người chơi. Xem [cốt lõi Gameplay Loop](CoreLoop.md) for squad philosophy.

#### người chơi per Server Instance

| Instance Type                    |  người chơi Count | Rationale                                                        |
| -------------------------------- | :-----------: | ---------------------------------------------------------------- |
| **Standard Raid**                | 16–20 người chơi | Dense enough for encounters; sparse enough for stealth viability |
| **Quick Raid** (15-min mode)     | 12–16 người chơi | Smaller map, shorter timer, fewer người chơi                        |
| **Solo Match** (future optional) |  8–12 người chơi | nếu solo mode gains dedicated server pool                         |

**Fill logic:** Server instances deploy khi ≥80% of capacity is filled hoặc khi the matchmaking queue holds 8+ người chơi for >45 seconds (whichever comes first). Partial-fill raids are valid — a 12-người chơi of 20 raid is balanced và preferred over extended wait times.

***

### Queue hệ thống

#### Queue Types

| Queue                   | Description                                                                                                                                              | Priority                   |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| **Standard**            | Default — all người chơi together in regional pool                                                                                                          | primary                    |
| **Friends Only**        | Invite-only private raid. No strangers. Full server population phải được filled by invites.                                                                | Optional (private session) |
| **Training / Tutorial** | AI-only server. No other người chơi. Tutorial-exclusive.                                                                                                    | Forced for first-timer     |
| **Ranked**              | Rated matchmaking pool (separate from casual). Xem [RankedMode](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/RankedMode.md). | Separate pool              |

#### Matchmaking Assumptions

Matchmaking là design contract, không chỉ là technical queue. Player phải biết rule nào họ đang vào trước khi server được reserve.

| Assumption | Rule | Player-Facing Requirement |
| :--- | :--- | :--- |
| Regional-first queue | Ưu tiên best-ping region trước khi expand | Show region và estimated latency khi queue starts |
| Soft new-player protection | Những raid đầu có thể weighted về lower-density hoặc tutorial-safe pools | Không gọi là easy mode; chỉ present như onboarding protection khi cần |
| Gear value is not MMR | Kit đắt không ép player vào high-skill lobby | Tránh imply paid/expensive gear đổi matchmaking |
| Party leader owns queue selection | Leader chọn mode, map, squad fill, và region | Squad members thấy selected contract trước khi ready |
| Low-pop fallback is allowed | Queue có thể start lower-density thay vì chờ quá lâu | Show "lower-density raid" nếu expected player count đổi đáng kể |
| Ranked and event pools are separate | Ranked/event rules không silently mix với casual rules | Mode card phải show pool, penalties, rewards, và special extraction rules |
| Tutorial pool is protected | First tutorial là AI-only trừ khi replay rõ ràng với squad | Standard queue vẫn locked đến khi tutorial exit condition đạt |
| Reconnect before loss | Disconnect tạo reconnect window trước MIA resolution | Loading/reconnect UI phải show remaining window và consequence |
| Server crash rollback | Invalid server result restore pre-raid loadout snapshot | Debrief dùng rollback copy, không dùng KIA/MIA copy |

#### Matchmaking Algorithm

The standard queue uses **regional pool matching** với a progressive expansion timeout:

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

**No strict SBMM (Skill-Based Matchmaking):** Extraction shooters structurally resist SBMM vì gear disparity is intentional. A "Rat" người chơi với cheap gear can outplay a "Chad" với skill. True SBMM would undermine the economy-driven risk hệ thống. We cách dùng **soft behavioral grouping** instead:

| Behavioral Signal                                | Action                                                                                                |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| người chơi's last 5 raids: all died within 2 minutes | May preferentially fill low-density servers (fewer total người chơi per instance — learning environment) |
| người chơi's recent gear giá trị > $80,000 average     | No change — gear giá trị is not a matchmaking signal                                                    |
| người chơi account < 10 raids total                  | Routed to Tutorial server; cannot join standard queue                                                 |
| người chơi flagged for cheating                      | Isolated matchmaking pool (honeypot server)                                                           |

This is the **Aggression-Based Matchmaking (ABMM)** concept inspired by ARC Raiders — not a binary split, nhưng a softer signal to giúp early người chơi mà không protecting them indefinitely.

***

### Lobby màn hình flow

#### Pre-Raid flow

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

#### Lobby màn hình — Squad Integration

| tính năng                     | Behavior                                                                                                                              |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Party creation**          | From Friends list hoặc in-game social màn hình. Party leader controls map và queue type selection.                                       |
| **Party size limit**        | 3 người chơi maximum.                                                                                                                    |
| **Loadout visibility**      | Squad members CAN see each other's operator choice nhưng NOT chi tiết gear/inventory (privacy).                                         |
| **Ready-up**                | Required from all members trước departure. nếu one member is not ready sau 60s, deploy continues mà không them (partial squad join). |
| **Squad communication**     | Voice và text chat active in lobby. Same channels as in-raid.                                                                        |
| **Operator duplicate rule** | Same operator CAN be used by multiple squad members. Ability stacking rule applies in-raid per [Hero Abilities](Hero_Abilities.md).   |

***

### Reconnect & Disconnection

#### Disconnection Behavior

Per [Extraction cơ chế](Extraction_Mechanics.md): disconnect → 5-minute MIA timeout → gear lost. The lobby hệ thống augments this:

| Scenario                      | Behavior                                                                                                          |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Disconnect < 5 min**        | Server holds người chơi's raid slot. Reconnect window active. người chơi spawns back in their last safe position.         |
| **Reconnect within 5 min**    | người chơi returns to raid. HP và status effects preserved. LOS fog reset (must re-scout).                           |
| **Reconnect failed (>5 min)** | nhân vật is removed from raid as MIA. Gear loss rules apply.                                                     |
| **Squad member disconnects**  | Squad can continue. Disconnected người chơi's nhân vật remains for 5 min. Squad cannot loot a disconnected ally.     |
| **Host migration**            | Sessions are server-authoritative. There is no "host." Disconnect of any người chơi does not affect server stability. |
| **Server crash**              | Rare case — all người chơi MIA. No gear loss (server-side rollback to pre-raid loadout). Exception case.             |

**Mobile-cụ thể:** On mobile, background app suspension is treated as a short disconnect. nếu suspended <30s và reconnected, treated as connectivity hiccup — no MIA timer started. nếu suspended >30s, MIA timer begins.

***

### Cross-Platform Matchmaking

The game targets PC, Console, và Mobile người chơi in shared pools:

| Scenario                               | Design Choice                                                                                                                                                |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **PC + Console + Mobile in same raid** | Yes — same rules, same server. No cơ chế difference.                                                                                                     |
| **Aim assist on mobile**               | Mobile receives aim assist on ability targeting per [Hero Abilities](Hero_Abilities.md). Regular vũ khí aiming: aim assist enabled (adjustable in settings). |
| **PC người chơi vs Mobile**               | No automatic separation. Người chơi có thể opt-in to "Platform Restricted" mode (only own platform), accepting potentially longer queues.                          |
| **Input detection**                    | Server identifies input type for metrics only. Not used for matchmaking quyết định.                                                                           |
| **Performance parity**                 | Server-authoritative validation prevents client-side advantage. Mobile và PC are identical in hit registration và LOS outcomes.                            |

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

**Auto-selection:** Default is best-ping region. Người chơi có thể manually pin a cụ thể region (accepts higher latency).

**Cross-region join:** khi queue times exceed 90s (Phase 3), người chơi are placed in the nearest adjacent region server với <150ms ping. Raids do not mix người chơi across >150ms differential to prevent latency advantage.

***

### Private / Friends Raid

For content creators, clan practices, hoặc private group play:

| Property                   | giá trị                                                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Unlock**                 | Account level 5 hoặc Tutorial completed                                                                                    |
| **Minimum người chơi**        | 2 (cannot solo a private raid — anti-economy exploit prevention)                                                         |
| **Maximum người chơi**        | Full server capacity (20 standard, 16 quick)                                                                             |
| **AI presence**            | Full AI population (same as public raid)                                                                                 |
| **Economy impact**         | Loot và XP earned counts toward progression. Insurance applies.                                                         |
| **Restriction**            | Cannot complete faction quests in private raid (prevents coordinated farming).                                           |
| **Known người chơi locations** | All người chơi in private session see each other as "friendly" on minimap (optional: can disable for competitive practice). |

***

### Tutorial / First-thời gian Matchmaking

New accounts (0 raids) are routed differently:

| Step                             | Behavior                                                                                                                                        |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Account created                  | Forced into Tutorial Raid trước standard queue access                                                                                          |
| Tutorial Raid                    | AI-only server. No other người chơi. Xem [TutorialRaid](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/TutorialRaid.md). |
| Tutorial Raid exit (any outcome) | Standard queue unlocked.                                                                                                                        |
| First 5 standard raids           | Soft-weighted toward lower-density instances. Not enforced — just weighted.                                                                     |
| Account level 5                  | All matchmaking restrictions lifted. Full access to all queues.                                                                                 |

***

### Anti-Abuse in Matchmaking

| Abuse Vector                      | Prevention                                                                                                  |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Alt-account griefing**          | New accounts can only hold Tier 1 gear for first 5 raids. Cannot bring $80k loadouts to harass new người chơi. |
| **Queue dodging**                 | Cancel-và-rejoin within 60s causes a 2-minute queue cooldown.                                              |
| **IP abuse (VPN region exploit)** | Region is determined by server ping validation, not self-report. VPN cannot fake low-ping region access.    |
| **Smurf accounts**                | Behavioral signals (high XP-per-minute khi account is "new") can flag for review. Not auto-penalized.      |
| **Private raid economy exploit**  | Quest completions disabled in private raids. Loot still earnable to prevent complete restriction.           |

***

### Lobby UI Specifications

#### PC / Console Layout

| Section              | Position           | Content                                                           |
| -------------------- | ------------------ | ----------------------------------------------------------------- |
| **Map selection**    | Center             | Map thumbnail, weather, timer, queue count                        |
| **Loadout summary**  | Right panel        | Operator icon, vũ khí thumbnails, giáp, weight, insurance status |
| **Operator select**  | Right panel top    | 3 operator slots; hiện tại equipped shown                          |
| **Insurance toggle** | Right panel bottom | chi phí display; toggle per-item hoặc blanket                          |
| **Squad panel**      | Left panel         | Squad member cards: name, operator, status (ready/not ready)      |
| **Queue status**     | Top center         | "Searching...", timer, region                                     |
| **Deploy button**    | Bottom center      | Large, prominent. Requires all squad ready.                       |
| **Cancel queue**     | Bottom right       | Small; available at any point trước deployment countdown         |

***

### Summary of chính quyết định

| Topic                    | quyết định                                                                  |
| ------------------------ | ------------------------------------------------------------------------- |
| **Max squad size**       | 3 người chơi. No 4- hoặc 5-người chơi squads.                                      |
| **người chơi per instance** | 16–20 (standard); 12–16 (quick raid).                                     |
| **SBMM**                 | No strict SBMM. Soft behavioral weighting for new người chơi only.           |
| **Cross-platform**       | Same pool for PC/Console/Mobile. Optional platform restriction available. |
| **Private raids**        | available at account level 5. Quests disabled in private.                 |
| **Disconnect**           | 5-min reconnect window. Server holds slot. Mobile background: 30s grace.  |
| **Queue expansion**      | 4-phase: regional → cross-regional. Force-starts at 90s nếu needed.        |

***

### Tham Chiếu Chéo

* [loading màn hình Design](../UI_UX/LoadingScreen_Design.md) — L4\_LobbyToMatch taxonomy, content types, layout.
* [cốt lõi Gameplay Loop](CoreLoop.md) — Preparation phase; loadout philosophy.
* [Extraction cơ chế](Extraction_Mechanics.md) — Disconnection MIA rule; reconnect behavior.
* [Hero Abilities](Hero_Abilities.md) — Operator selection; ability stacking rule for same-class duplicates.
* [Environmental Hazards](Environmental_Hazards.md) — Weather shown at briefing màn hình.
* [Controls](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Controls.md) — Platform-cụ thể lobby input.
* [GameDesign/RankedMode](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/RankedMode.md) — Ranked queue pool và yêu cầu.
* [GameDesign/TutorialRaid](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/TutorialRaid.md) — First-thời gian người chơi routing.
