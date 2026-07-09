---
title: "Anti-Cheat & Fair Play"
type: docs
weight: 20
---

### Tổng Quan

An extraction shooter với persistent economy và PvP stakes is a high-giá trị target for cheating. A single cheater in a raid affects 15–20 other người chơi' session và economy. This tài liệu specifies the anti-cheat architecture, exploit prevention design patterns, người chơi reporting hệ thống, và escalating punishment model. Anti-cheat is not only a technical hệ thống — it is a cốt lõi design philosophy embedded in the game's server architecture.

> **Cross-References:** [LOS, Fog & Visibility](LOS_Fog_Visibility.md) — server-authoritative LOS (anti-wallhack); [Matchmaking & Lobby](Matchmaking_Lobby.md) — suspect matchmaking isolation pool; [Camera hệ thống](Camera_System.md) — altitude cap prevents client-side reveal; [Looting & Inventory](Looting_Interactions.md) — item duplication prevention; [GameDesign/LiveOps](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/LiveOps.md) — ban waves và community communication.

***

### Design Philosophy

* **Server-first, client-display.** The server is always the source of truth for positions, LOS, damage, và item trạng thái. The client renders — it does not decide.
* **Frustrate, don't just ban.** Unknown ban trạng thái và isolation matching ("chicken dinner" cheating pools) are more effective than immediate bans at revealing cheat tool behavior.
* **Reward reporting.** người chơi are partners in cheat detection. Reporting phải được frictionless và reporting confirmed cheaters yields small in-game rewards.
* **Transparent enforcement.** Ban stats are published monthly. người chơi see the hệ thống working.

***

### Server-Authoritative Architecture

#### What the Server Validates

Every critical game action is server-validated trước taking effect:

| hệ thống                        | Server Validation                                                                                                                                                                 |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **người chơi position**           | Server maintains authoritative position. Client sends input; server moves nhân vật và confirms. Client prediction for latency compensation only.                                |
| **Bullet hit registration**   | Server calculates hit geometry using server-side nhân vật positions, not client-reported positions. Lag compensation applied within ±150ms tolerance.                            |
| **LOS / Visibility**          | Server calculates which objects và người chơi are hiển thị rõ to each client. Client receives only data it is authorized to render. Xem [LOS, Fog & Visibility](LOS_Fog_Visibility.md). |
| **Item pickup / interaction** | Server confirms item still exists at location trước authorizing pickup. No client-side item trạng thái.                                                                               |
| **Ability cách dùng**               | Server validates cooldown, range, và target eligibility trước applying effects. Client animation plays optimistically; server corrects nếu invalid.                              |
| **Extraction**                | Server runs timer và validates người chơi presence in zone at each tick. Client cannot self-report extraction success.                                                               |
| **Damage application**        | Server adds all damage; calculates HP kết quả; sends update to client. Client HP display is read-only.                                                                             |

***

### Cheat Vector Prevention

#### Wallhack / ESP Prevention

| Method                         | Implementation                                                                                                                                                              |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Server-side entity culling** | Clients only receive position data for entities within their LOS. địch not in LOS are not transmitted to client (no data to hack).                                       |
| **LOS check frequency**        | Every 50ms per người chơi. chi phí is managed server-side; client receives kết quả.                                                                                                 |
| **Camera altitude gate**       | Server caps maximum world-trạng thái transmission to altitude-equivalent zone (26m). Client cannot request world trạng thái beyond that range. Xem [Camera hệ thống](Camera_System.md). |
| **Encrypted entity payloads**  | Position và máu data packets are encrypted và session-keyed. Packet injection cannot fabricate valid position data.                                                    |

#### Aimbot Prevention

| Method                            | Implementation                                                                                                                                            |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Aim angle validation**          | Server compares last N aim vectors (50ms samples) for inhuman snap patterns. Snap >90° in <30ms to địch hitbox flags anomaly.                            |
| **Hit rate anomaly**              | Server tracks per-người chơi headshot rate, hit rate at 30m+, và kill rate per raid. A người chơi với >85% headshot rate across 5+ raids is flagged for review. |
| **Pixel-perfect tracking**        | Input delta smoothness check — aimbot inputs are unnaturally smooth. Human inputs have micro-variance. Statistical deviation flagged.                     |
| **Recoil compensation detection** | nếu client-reported aim exactly compensates for server-side recoil every frame, anomaly flag raised.                                                       |

#### Speed Hack Prevention

| Method                  | Implementation                                                                                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Position delta cap**  | Server rejects any position update where distance traveled exceeds max possible speed for nhân vật's hiện tại weight tier + 10% latency buffer. nhân vật "rubber-bands" back. |
| **Teleport detection**  | Position delta > 5m in single tick (16ms) = teleport flag. Instant server log; 3 occurrences in same session = kick.                                                           |
| **Phase-thông qua walls** | Server validates that position path between two points does not cross solid collision geometry. Invalid path = reject + log.                                                   |

#### Item Duplication Prevention

| Method                       | Implementation                                                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Unique item instance IDs** | Every item in the game has a globally unique ID. No item can exist in two locations simultaneously. Server enforces this.                  |
| **Transfer validation**      | khi items move (loot, trade, craft, insure), server atomically deducts from source trước adding to điểm đến. No window for duplicate. |
| **Stash write-ahead log**    | All stash operations are logged trước commit. Rollback-capable in case of server crash. No items created outside of defined faucets.      |
| **Insurance validation**     | Insurance returns are generated by server on a verified death event. Cannot be triggered by client.                                        |

#### Teaming / Alt-Account Detection

Teaming is khi solo-queue người chơi coordinate với supposed địch to farm kills:

| Signal                                                                                  | Detection                                                                    |
| --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Two "địch" accounts never damage each other across 10+ shared raids                    | Flagged for review                                                           |
| Kill-then-revive pattern (one account "kills" another, retrieves their gear, transfers) | Server flags asymmetric kill patterns between frequently co-raiding accounts |
| Account age mismatch với gear giá trị                                                    | New account week 1 với Tier 4 loadout triggers gear-source audit            |

***

### Client Integrity

| Layer                            | Implementation                                                                                                                   |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Game file integrity**          | On launch, game client hash-validates all binaries và assets. Modified client = auto-kick on next server auth challenge.        |
| **Anti-tamper**                  | Runtime memory scanning via third-party kernel-level AC (e.g., BattlEye hoặc equivalent). Hooks và injectors detected.            |
| **Kernel-level AC scope**        | Only active trong khi session (not background khi game is not running). Opt-out = cannot join online sessions.                     |
| **Screenshot/replay validation** | nếu người chơi reports death replay, server-side replay is canonical. Client cannot submit modified death replay.                     |
| **VPN detection**                | Ping-based region validation (not IP-based). VPN cannot fake low-ping access as per [Matchmaking & Lobby](Matchmaking_Lobby.md). |

***

### Reporting hệ thống

#### How người chơi Report

1. **In-session** (sau death): Death màn hình shows "Report người chơi" button. One tap/click — opens pre-filled report với kill metadata.
2. **Post-game debrief**: Results màn hình has a flag icon next to each người chơi who killed you hoặc your squad.
3. **Friends list**: Can report a người chơi from encounter history up to 24h sau the session.
4. **In-Raid ping** (squad-only): Squad leader can flag a suspicious người chơi mid-raid với a special ping type (adds to review queue nhưng no in-raid effect).

#### Report Form

| Field                 | Type              | ghi chú                                                |
| --------------------- | ----------------- | ---------------------------------------------------- |
| Cheat type (dropdown) | Required          | Aimbot, Wallhack, Speed, Duplication, Teaming, Other |
| Session ID            | Auto-filled       | hệ thống grabs hiện tại/recent session                  |
| Description           | Optional text     | Max 280 chars                                        |
| Evidence (optional)   | Screenshot upload | Auto-attach server-side replay clip nếu available     |

#### Report Reward hệ thống

| Event                               | Reward                                                 |
| ----------------------------------- | ------------------------------------------------------ |
| Submitted report reviewed by hệ thống | No reward (reduces spam)                               |
| Report leads to confirmed ban       | $2,000 in-game + "Community Defender" badge (one-thời gian) |
| Report marked as false/spam (3×)    | Reporting privileges suspended 7 days                  |

***

### Punishment Model

#### Escalating Ban Ladder

| Violation Level    | Action                                          | Duration                                      |
| ------------------ | ----------------------------------------------- | --------------------------------------------- |
| **cảnh báo**        | Auto-flagged anomaly, human review pending      | No action yet; on watch list                  |
| **Soft Isolation** | người chơi silently placed in cheater-matching pool | Until reviewed (days–weeks)                   |
| **Temporary Ban**  | Account suspended                               | 14 days (first confirmed offense)             |
| **Permanent Ban**  | Account permanently suspended                   | Confirmed hoặc second offense                   |
| **Hardware Ban**   | All accounts on device banned                   | Cheat tool detection hoặc third offense pattern |

#### Soft Isolation Pool ("Cheater Jail")

Rather than banning immediately (which reveals detection methods to cheat developers), confirmed suspects are silently placed in a pool where they only match against other suspects. This:

* Keeps legitimate người chơi in clean sessions.
* Allows monitoring of cheat behavior in a controlled environment.
* Cheaters "notice" degraded trải nghiệm (longer queues, other cheaters, weird behavior) trước the ban.

***

### Fair Play Rules (Non-Technical)

| Rule                            | Policy                                                                                                                                               |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **No real-money trading (RMT)** | Selling in-game items for real currency is prohibited. Account flagged for unusual sell volume hoặc pricing patterns.                                  |
| **No account boosting**         | Accounts found to be deliberately losing for payment hoặc allowing others to play (mule accounts) are banned.                                          |
| **Stream sniping**              | Not technically detectable, nhưng coordinated stream sniping against a cụ thể individual is a bannable harassment offense nếu reported với evidence. |
| **Bug exploitation**            | Deliberately exploiting known bugs for gain (duping, geometry clipping) results in a 14-day ban và item rollback for first offense.                 |
| **Toxic behavior**              | Voice/text chat harassment: mute, then 7-day suspension depending on severity. Hate speech: permanent.                                               |

***

### Transparency & Communication

| Topic                          | Action                                                                                         |
| ------------------------------ | ---------------------------------------------------------------------------------------------- |
| **Monthly ban report**         | Publish count of bans by type (aimbot, wallhack, etc.) in patch ghi chú                          |
| **Appeal process**             | In-app appeal form với 14-day review SLA                                                      |
| **False positive protocol**    | False bans reversed within 48h of appeal; người chơi receives compensation (Operator XP, currency) |
| **Cheat tool partner program** | Work với trusted AC firms to share detection signatures                                       |
| **Known exploit disclosure**   | Patch ghi chú confirm known exploits are fixed; do not describe exploit cơ chế                |

***

### Tham Chiếu Chéo

* [LOS, Fog & Visibility](LOS_Fog_Visibility.md) — Server-authoritative LOS, anti-wallhack design.
* [Matchmaking & Lobby](Matchmaking_Lobby.md) — Soft isolation pool integration; flag trong khi queue.
* [Camera hệ thống](Camera_System.md) — Server-side altitude gate prevents world-trạng thái reveal.
* [Looting & Inventory](Looting_Interactions.md) — Item unique IDs; duplication prevention.
* [GameDesign/LiveOps](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/LiveOps.md) — Monthly ban transparency reports.
