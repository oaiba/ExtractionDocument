---
title: "Post-Game Debrief & Replay"
type: docs
weight: 21
---

### Tổng Quan

The Post-Game Debrief is the màn hình that appears immediately sau a raid ends — whether thông qua successful extraction, death, disconnection, hoặc server end. It is the **most read màn hình in the game** sau the stash: người chơi spend significant thời gian reviewing their performance, examining loot giá trị, và understanding how they died. A well-designed debrief provides closure, learning, và motivation to queue again.

> **Cross-References:** [cốt lõi Gameplay Loop](coreloop/index.html) — Phase 5 Recovery; [Extraction cơ chế](extraction_mechanics/index.html) — extraction kết quả codes; [Medical hệ thống](medical_system/index.html) — body part HP summary in debrief; [Camera hệ thống](camera_system/index.html) — death cam into debrief transition; [GameDesign/Progression](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Progression.md) — XP gains displayed in debrief.

***

### Design Philosophy

* **Show the thông số, nhưng make them feel earned.** Every XP point earned has a source — show it. người chơi who know why they earned XP are more likely to chase it next raid.
* **Death is a teacher, not a wall.** The debrief must answer "why did I die?" clearly. Death replay is the most quan trọng tool for người chơi improvement.
* **Quick to leave.** người chơi who want to queue immediately should reach "Deploy Again" in ≤2 taps/clicks. Never lock the người chơi in the debrief.
* **Calm và focused.** Post-raid is recovery thời gian. The debrief UI should feel quieter than in-raid — dark theme, subdued music, no animations that demand attention.

***

### Debrief Sections

#### 1. Outcome Banner

The first thing displayed — large, dễ đọc, emotive.

| Outcome                                    | Banner Text      | Color    |
| ------------------------------------------ | ---------------- | -------- |
| Extracted successfully                     | **"EXTRACTED"**  | Gold     |
| Died to địch người chơi                       | **"K.I.A."**     | Red      |
| Died to AI                                 | **"ELIMINATED"** | Orange   |
| Died to environment (bleed, contamination) | **"LOST"**       | Dark red |
| MIA (disconnection/timeout)                | **"MIA"**        | Grey     |
| Survived raid end (no extraction)          | **"thời gian OUT"**   | Purple   |

Below the banner: **survival thời gian** (e.g., "14:32 survived") và **cause** (e.g., "Headshot by \[người chơi Name]" hoặc "AI Rifle · Industrial Zone").

***

#### 2. XP Breakdown

Every XP source itemized in a scrollable list:

| XP source                 |    Example giá trị    | Explanation                   |
| ------------------------- | :-----------------: | ----------------------------- |
| Raid survival bonus       |       +200 XP       | Alive for 10+ minutes         |
| Kills — AI (per kill)     |     +15 XP each     | Standard AI reward            |
| Kills — Boss              |       +300 XP       | One-thời gian per boss             |
| Kills — người chơi (per kill) |     +50 XP each     | PvP reward                    |
| Extraction bonus          |       +500 XP       | Only on successful extract    |
| Quest objective completed |     +250 XP each    | Per objective (not per quest) |
| Damage dealt total        | +1 XP per 10 damage | Traceable participation       |
| Teammate revived          |  +150 XP per revive | Co-op reward                  |
| First extract of session  |       +100 XP       | Daily first-extract bonus     |
| **TOTAL**                 |      **XXX XP**     | Rolls up at bottom            |

**XP bar animation:** sau all line items display, the XP bar fills from hiện tại to new giá trị. nếu leveling up, large level-up celebration plays.

***

#### 3. Loot Summary

Items extracted this raid, với economy context:

| Column     | Content                                                    |
| ---------- | ---------------------------------------------------------- |
| Item icon  | 32×32 icon                                                 |
| Item name  | Full item name                                             |
| Qty        | Stack count                                                |
| Condition  | % durability for gear items                                |
| Est. giá trị | Server's hiện tại flea market average (hoặc trader mua giá) |
| FIR status |  (FIR) hoặc  (not FIR)                                     |

**Total estimated giá trị:** Sum of all extracted loot displayed at bottom of list.\
**Sort options:** By giá trị (desc), by name, by category.

nếu the người chơi **died** (no extraction): the list shows "LOST ITEMS" — everything that was in their inventory that was not in a Secure Container. Same format nhưng highlighted red. Secure container items are shown separately as "KEPT" in green.

***

#### 4. Combat Stats

Summary of in-raid combat performance:

| Stat                | Description                             |
| ------------------- | --------------------------------------- |
| Kills (AI)          | Total AI killed                         |
| Kills (người chơi)      | Total người chơi kills                      |
| Deaths              | 0 (alive) hoặc 1 (dead)                   |
| Damage Dealt        | Total damage output                     |
| Damage Received     | Total damage taken                      |
| Headshot %          | Headshots / total hits × 100            |
| Longest kill        | Distance of furthest confirmed kill     |
| Accuracy            | Shots landed / shots fired × 100        |
| Suppressed duration | Total seconds spent in suppressed trạng thái |
| Distance traveled   | Total meters moved this raid            |

***

#### 5. Squad Summary

Shows squadmates' outcomes (even nếu they disconnected/died):

| Column        | Content                       |
| ------------- | ----------------------------- |
| Name          | người chơi name                   |
| Status        | Extracted / KIA / MIA         |
| Operator      | Operator used                 |
| Kills         | AI + người chơi kills             |
| Revives given | Times they revived a teammate |
| XP earned     | Total XP this raid            |

***

#### 6. Death Replay ("How I Died")

available only for người chơi who died this raid. Server-generated, not client-generated (cannot be modified).

| Element                | chi tiết                                                                                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Replay source**      | Server-side tick recording. 10-second window trước death + 3 seconds sau.                                                         |
| **Perspective**        | Top-down camera from người chơi's position, standard in-game view. người chơi's LOS applies — cannot see the địch trước they were hiển thị rõ. |
| **địch shown**        | địch is revealed in replay sau death occurs — 2 seconds of showing who/what killed the người chơi.                                    |
| **địch info**         | Shows: operator class; hit location; vũ khí type (not equipment chi tiết). Does NOT show địch HP, inventory, hoặc stash.               |
| **Causes highlighted** | Hit marker overlays on replay timeline show each hit. Cause of death indicated.                                                      |
| **Skip**               | người chơi can skip replay at any thời gian.                                                                                                  |
| **Save**               | "Save this clip" button saves 13-second server replay to người chơi's account (up to 10 clips stored).                                   |

**Replay unavailable Cases:**

* MIA death (disconnect — no death event to replay)
* Zone contamination death (replay shows contamination damage tick; no địch to show)
* Server crash (no replay data)

***

#### 7. Tips Contextual Panel

A single-line tip, contextually based on how the người chơi died hoặc performed:

| Death Cause                  | Tip Shown                                                                                                     |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Headshot (no helmet)         | "Tip: Helmets reduce headshot damage significantly. Class 3 helmets stop most pistol rounds."                 |
| Bleed-out                    | "Tip: Carry a Bandage in your pockets for fast access trong khi combat — you don't need to open inventory."      |
| Extraction timer interrupted | "Tip: Incoming fire trong khi extraction resets the timer. cách dùng abilities hoặc smokes to mua thời gian."                 |
| AI boss kill                 | "Tip: Boss \[Name] has a weak side — flank from the north entrance to avoid their forward fire arc."          |
| Overweight at death          | "Tip: Dropping low-giá trị loot trước extracting can move you to a lighter weight tier — và saving your run." |

Tips shown once per scenario — suppressed sau người chơi has seen it 3 times (settings reset available).

***

### Navigation & flow

#### Debrief Button Layout (PC)

| Button              | Action                                                             | Location              |
| ------------------- | ------------------------------------------------------------------ | --------------------- |
| **Deploy Again**    | Immediately enters matchmaking với same loadout (nếu stash allows) | Bottom-right, primary |
| **Return to Stash** | Goes to main stash màn hình                                          | Bottom-center         |
| **Watch Replay**    | Opens death replay (nếu available)                                  | Bottom-left           |
| **Share Clip**      | Opens clip sharing UI for saved replay                             | Below replay button   |
| **Report người chơi**   | Opens report form pre-filled với killer info                      | Top-right (small)     |

#### Debrief flow (Mobile)

Same sections; scrollable single column. Tabs at top: Summary / Loot / Stats / Replay. Deploy button always pinned to màn hình bottom.

***

### Economy Integration

The moment the debrief loads, item transfer is immediate:

* **Extracted items** are already in stash — shown với "NEW" badge.
* **Insurance** returns are scheduled; ETA shown in debrief (e.g., "Standard insurance returns in 22 hours").
* **Quest turn-in** items are flagged với quest name in loot list — click takes người chơi to trader màn hình.
* **Trader XP** gained this raid shown in debrief header badge.

***

### Raid Outcome Reconciliation

Debrief là player-facing view của server reconciliation. Nó phải tách gameplay failure khỏi technical failure, và phải cho biết vì sao mỗi item, quest, reward đổi state.

| Result Code | Header Outcome | Loot Treatment | Progress Treatment | Required CTA |
| :--- | :--- | :--- | :--- | :--- |
| `EXTRACTED` | Extracted | Extracted items chuyển vào stash hoặc overflow | XP, FIR, quest, và reward rules áp dụng | Continue, manage stash, deploy again |
| `KIA` | K.I.A. | Equipped và backpack items mất trừ khi protected hoặc later insured | Allowed XP và quest progress áp dụng | Watch replay, rebuild, report nếu cần |
| `MIA_TIMEOUT` | MIA | Failed extraction item loss rules áp dụng | Limited progress chỉ khi objective rules cho phép | Review timer/extract distance, rebuild |
| `MIA_DISCONNECT` | MIA | Failed extraction sau khi reconnect window hết hạn | Không thêm penalty ngoài MIA | Show reconnect expiry và support route nếu đáng ngờ |
| `SERVER_ROLLBACK` | Raid Invalidated | Pre-raid loadout snapshot restored | Không có raid rewards; compensation có thể riêng | Return to stash, view support note |
| `PARTIAL_EXTRACT` | Squad Split | Local player result resolve độc lập | Squad summary show từng member riêng | Continue nếu alive, debrief nếu extracted/dead |
| `OBJECTIVE_UNSECURED` | Objective Unsecured | Objective item mất trừ khi protected | Objective progress phụ thuộc extraction requirement | View quest requirement và next route |

#### Lost / Kept / Insured / FIR Display

| Item State | Display Rule | Interaction |
| :--- | :--- | :--- |
| Lost | Show trong lost item list với reason: KIA, MIA, looted, expired, destroyed | Không có action trừ khi insurance active |
| Kept | Show trong kept/protected list với source: secure container, protected quest rule, rollback | Cho move to stash nếu applicable |
| Insured pending | Show return provider, chance/rule, và ETA | Link tới insurance inbox hoặc trader |
| FIR retained | Show FIR badge chỉ khi extraction và item rules giữ nó | Explain nếu FIR bị removed |
| Overflow | Show stash overflow lane và required transfer action | Block deploy-again đến khi stash valid |

#### Deploy Again Eligibility

Deploy Again chỉ enabled khi account có operator hợp lệ, loadout hợp lệ, không có blocking overflow, không có reward sync chưa resolve, và selected mode vẫn available. Nếu disabled, button phải show blocking reason đầu tiên và direct action như `Repair Gear`, `Resolve Overflow`, `Equip Ammo`, hoặc `Return to Stash`.

***

### Tham Chiếu Chéo

* [cốt lõi Gameplay Loop](coreloop/index.html) — Phase 5 Recovery; debrief as start of next loop.
* [Extraction cơ chế](extraction_mechanics/index.html) — Extraction outcome codes; MIA rule.
* [Medical hệ thống](medical_system/index.html) — Body part damage summary (in death context).
* [Camera hệ thống](camera_system/index.html) — Death cam transition into debrief màn hình.
* [GameDesign/Progression](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Progression.md) — XP values, level thresholds, XP bar.
* [Quest & Objective hệ thống](quest_objective_system/index.html) — Quest objectives flagged in debrief loot list.
* [Anti-Cheat & Fair Play](anti_cheat_fair_play/index.html) — Report người chơi button in debrief.
