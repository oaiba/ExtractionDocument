---
title: Anti-Cheat & Fair Play
type: docs
weight: 20
---


### Overview

An extraction shooter with persistent economy and PvP stakes is a high-value target for cheating. A single cheater in a raid affects 15–20 other players' session and economy. This document specifies the anti-cheat architecture, exploit prevention design patterns, player reporting system, and escalating punishment model. Anti-cheat is not only a technical system — it is a core design philosophy embedded in the game's server architecture.

> **Cross-References:** [LOS, Fog & Visibility](los_fog_visibility/index.html) — server-authoritative LOS (anti-wallhack); [Matchmaking & Lobby](matchmaking_lobby/index.html) — suspect matchmaking isolation pool; [Camera System](camera_system/index.html) — altitude cap prevents client-side reveal; [Looting & Inventory](looting_interactions/index.html) — item duplication prevention; [GameDesign/LiveOps](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/LiveOps.md) — ban waves and community communication.

***

### Design Philosophy

* **Server-first, client-display.** The server is always the source of truth for positions, LOS, damage, and item state. The client renders — it does not decide.
* **Frustrate, don't just ban.** Unknown ban states and isolation matching ("chicken dinner" cheating pools) are more effective than immediate bans at revealing cheat tool behavior.
* **Reward reporting.** Players are partners in cheat detection. Reporting must be frictionless and reporting confirmed cheaters yields small in-game rewards.
* **Transparent enforcement.** Ban stats are published monthly. Players see the system working.

***

### Server-Authoritative Architecture

#### What the Server Validates

Every critical game action is server-validated before taking effect:

| System                        | Server Validation                                                                                                                                                                 |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Player position**           | Server maintains authoritative position. Client sends input; server moves character and confirms. Client prediction for latency compensation only.                                |
| **Bullet hit registration**   | Server calculates hit geometry using server-side character positions, not client-reported positions. Lag compensation applied within ±150ms tolerance.                            |
| **LOS / Visibility**          | Server calculates which objects and players are visible to each client. Client receives only data it is authorized to render. See [LOS, Fog & Visibility](los_fog_visibility/index.html). |
| **Item pickup / interaction** | Server confirms item still exists at location before authorizing pickup. No client-side item state.                                                                               |
| **Ability use**               | Server validates cooldown, range, and target eligibility before applying effects. Client animation plays optimistically; server corrects if invalid.                              |
| **Extraction**                | Server runs timer and validates player presence in zone at each tick. Client cannot self-report extraction success.                                                               |
| **Damage application**        | Server adds all damage; calculates HP result; sends update to client. Client HP display is read-only.                                                                             |

***

### Cheat Vector Prevention

#### Wallhack / ESP Prevention

| Method                         | Implementation                                                                                                                                                              |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Server-side entity culling** | Clients only receive position data for entities within their LOS. Enemies not in LOS are not transmitted to client (no data to hack).                                       |
| **LOS check frequency**        | Every 50ms per player. Cost is managed server-side; client receives result.                                                                                                 |
| **Camera altitude gate**       | Server caps maximum world-state transmission to altitude-equivalent zone (26m). Client cannot request world state beyond that range. See [Camera System](camera_system/index.html). |
| **Encrypted entity payloads**  | Position and health data packets are encrypted and session-keyed. Packet injection cannot fabricate valid position data.                                                    |

#### Aimbot Prevention

| Method                            | Implementation                                                                                                                                            |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Aim angle validation**          | Server compares last N aim vectors (50ms samples) for inhuman snap patterns. Snap >90° in <30ms to enemy hitbox flags anomaly.                            |
| **Hit rate anomaly**              | Server tracks per-player headshot rate, hit rate at 30m+, and kill rate per raid. A player with >85% headshot rate across 5+ raids is flagged for review. |
| **Pixel-perfect tracking**        | Input delta smoothness check — aimbot inputs are unnaturally smooth. Human inputs have micro-variance. Statistical deviation flagged.                     |
| **Recoil compensation detection** | If client-reported aim exactly compensates for server-side recoil every frame, anomaly flag raised.                                                       |

#### Speed Hack Prevention

| Method                  | Implementation                                                                                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Position delta cap**  | Server rejects any position update where distance traveled exceeds max possible speed for character's current weight tier + 10% latency buffer. Character "rubber-bands" back. |
| **Teleport detection**  | Position delta > 5m in single tick (16ms) = teleport flag. Instant server log; 3 occurrences in same session = kick.                                                           |
| **Phase-through walls** | Server validates that position path between two points does not cross solid collision geometry. Invalid path = reject + log.                                                   |

#### Item Duplication Prevention

| Method                       | Implementation                                                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Unique item instance IDs** | Every item in the game has a globally unique ID. No item can exist in two locations simultaneously. Server enforces this.                  |
| **Transfer validation**      | When items move (loot, trade, craft, insure), server atomically deducts from source before adding to destination. No window for duplicate. |
| **Stash write-ahead log**    | All stash operations are logged before commit. Rollback-capable in case of server crash. No items created outside of defined faucets.      |
| **Insurance validation**     | Insurance returns are generated by server on a verified death event. Cannot be triggered by client.                                        |

#### Teaming / Alt-Account Detection

Teaming is when solo-queue players coordinate with supposed enemies to farm kills:

| Signal                                                                                  | Detection                                                                    |
| --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Two "enemy" accounts never damage each other across 10+ shared raids                    | Flagged for review                                                           |
| Kill-then-revive pattern (one account "kills" another, retrieves their gear, transfers) | Server flags asymmetric kill patterns between frequently co-raiding accounts |
| Account age mismatch with gear value                                                    | New account week 1 with Tier 4 loadout triggers gear-source audit            |

***

### Client Integrity

| Layer                            | Implementation                                                                                                                   |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Game file integrity**          | On launch, game client hash-validates all binaries and assets. Modified client = auto-kick on next server auth challenge.        |
| **Anti-tamper**                  | Runtime memory scanning via third-party kernel-level AC (e.g., BattlEye or equivalent). Hooks and injectors detected.            |
| **Kernel-level AC scope**        | Only active during session (not background when game is not running). Opt-out = cannot join online sessions.                     |
| **Screenshot/replay validation** | If player reports death replay, server-side replay is canonical. Client cannot submit modified death replay.                     |
| **VPN detection**                | Ping-based region validation (not IP-based). VPN cannot fake low-ping access as per [Matchmaking & Lobby](matchmaking_lobby/index.html). |

***

### Reporting System

#### How Players Report

1. **In-session** (after death): Death screen shows "Report Player" button. One tap/click — opens pre-filled report with kill metadata.
2. **Post-game debrief**: Results screen has a flag icon next to each player who killed you or your squad.
3. **Friends list**: Can report a player from encounter history up to 24h after the session.
4. **In-Raid ping** (squad-only): Squad leader can flag a suspicious player mid-raid with a special ping type (adds to review queue but no in-raid effect).

#### Report Form

| Field                 | Type              | Notes                                                |
| --------------------- | ----------------- | ---------------------------------------------------- |
| Cheat type (dropdown) | Required          | Aimbot, Wallhack, Speed, Duplication, Teaming, Other |
| Session ID            | Auto-filled       | System grabs current/recent session                  |
| Description           | Optional text     | Max 280 chars                                        |
| Evidence (optional)   | Screenshot upload | Auto-attach server-side replay clip if available     |

#### Report Reward System

| Event                               | Reward                                                 |
| ----------------------------------- | ------------------------------------------------------ |
| Submitted report reviewed by system | No reward (reduces spam)                               |
| Report leads to confirmed ban       | $2,000 in-game + "Community Defender" badge (one-time) |
| Report marked as false/spam (3×)    | Reporting privileges suspended 7 days                  |

***

### Punishment Model

#### Escalating Ban Ladder

| Violation Level    | Action                                          | Duration                                      |
| ------------------ | ----------------------------------------------- | --------------------------------------------- |
| **Warning**        | Auto-flagged anomaly, human review pending      | No action yet; on watch list                  |
| **Soft Isolation** | Player silently placed in cheater-matching pool | Until reviewed (days–weeks)                   |
| **Temporary Ban**  | Account suspended                               | 14 days (first confirmed offense)             |
| **Permanent Ban**  | Account permanently suspended                   | Confirmed or second offense                   |
| **Hardware Ban**   | All accounts on device banned                   | Cheat tool detection or third offense pattern |

#### Soft Isolation Pool ("Cheater Jail")

Rather than banning immediately (which reveals detection methods to cheat developers), confirmed suspects are silently placed in a pool where they only match against other suspects. This:

* Keeps legitimate players in clean sessions.
* Allows monitoring of cheat behavior in a controlled environment.
* Cheaters "notice" degraded experience (longer queues, other cheaters, weird behavior) before the ban.

***

### Fair Play Rules (Non-Technical)

| Rule                            | Policy                                                                                                                                               |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **No real-money trading (RMT)** | Selling in-game items for real currency is prohibited. Account flagged for unusual sell volume or pricing patterns.                                  |
| **No account boosting**         | Accounts found to be deliberately losing for payment or allowing others to play (mule accounts) are banned.                                          |
| **Stream sniping**              | Not technically detectable, but coordinated stream sniping against a specific individual is a bannable harassment offense if reported with evidence. |
| **Bug exploitation**            | Deliberately exploiting known bugs for gain (duping, geometry clipping) results in a 14-day ban and item rollback for first offense.                 |
| **Toxic behavior**              | Voice/text chat harassment: mute, then 7-day suspension depending on severity. Hate speech: permanent.                                               |

***

### Transparency & Communication

| Topic                          | Action                                                                                         |
| ------------------------------ | ---------------------------------------------------------------------------------------------- |
| **Monthly ban report**         | Publish count of bans by type (aimbot, wallhack, etc.) in patch notes                          |
| **Appeal process**             | In-app appeal form with 14-day review SLA                                                      |
| **False positive protocol**    | False bans reversed within 48h of appeal; player receives compensation (Operator XP, currency) |
| **Cheat tool partner program** | Work with trusted AC firms to share detection signatures                                       |
| **Known exploit disclosure**   | Patch notes confirm known exploits are fixed; do not describe exploit mechanics                |

***

### Fair Play Production Contract

Anti-cheat behavior must be visible enough to build trust without exposing detection implementation. The following contract applies to every networked system and player-facing enforcement flow.

| Area | Required rule |
| :--- | :--- |
| Server authority | Position, damage, visibility, extraction, item transfer, reward, and entitlement are server-authoritative |
| Evidence | Suspicious behavior is recorded with session, action, and confidence context; a single noisy signal is not an automatic permanent ban |
| Player communication | Kicks, restrictions, rollbacks, and compensation explain the outcome at a readable level and provide the correct support route |
| Recovery | Crash, rollback, disconnect, and false-positive handling preserve a deterministic audit trail |
| Privacy | Reports and telemetry collect only data needed for enforcement, safety, and appeal review |
| Economy safety | Duplication, RMT, boosting, and abuse cannot create unbounded items, currency, or progression |

#### Enforcement QA Checklist

- [ ] A legitimate high-skill player is not punished by a single anomaly signal.
- [ ] Every automatic restriction has an audit record and appeal path.
- [ ] Item, currency, reward, and insurance rollback is idempotent.
- [ ] Report submission works from death, debrief, and encounter history surfaces.
- [ ] Error, offline, and reconnect states do not silently discard a report or appeal.
- [ ] Ban communication does not reveal detection thresholds or bypass methods.
- [ ] Monthly transparency reporting uses aggregate data and preserves player privacy.

### Cross-References

* [LOS, Fog & Visibility](los_fog_visibility/index.html) — Server-authoritative LOS, anti-wallhack design.
* [Matchmaking & Lobby](matchmaking_lobby/index.html) — Soft isolation pool integration; flag during queue.
* [Camera System](camera_system/index.html) — Server-side altitude gate prevents world-state reveal.
* [Looting & Inventory](looting_interactions/index.html) — Item unique IDs; duplication prevention.
* [GameDesign/LiveOps](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/LiveOps.md) — Monthly ban transparency reports.
