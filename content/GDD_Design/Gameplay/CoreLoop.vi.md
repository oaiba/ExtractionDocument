---
title: "Core Gameplay Loop & Progression"
type: docs
weight: 1
---

### The Extraction Loop

Vòng lặp engagement cốt lõi được thiết kế để tạo a "Hero's Journey" in miniature, built on the cycle of **Risk Assessment, Execution, và Consequence**. Mỗi raid đi theo five distinct phases, each với its own cảm xúc arc và cơ chế mục đích.

> Xem [cốt lõi Gameplay cơ chế](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/CoreGameplay/README.md) để xem chi tiết per-minute match timeline, combat hệ thống thông số, và control sơ đồ specifications.

#### Phase Contract

Core Loop dùng cùng phase vocabulary với [Core Gameplay Mechanics](../GameDesign/CoreGameplay.md). Bất kỳ feature nào thay đổi một phase đều phải nói rõ nó cải thiện câu hỏi nào của player.

| Phase | Player Question | Must Provide | Must Not Do |
| :--- | :--- | :--- | :--- |
| Preparation | Tôi đang risk gì và vì sao? | Loadout validity, objective, mode rules, squad readiness, insurance state | Giấu blocker đến tận matchmaking |
| Infiltration | Tôi đang ở đâu và gần đó có gì? | Spawn orientation, extraction options, objective marker, first cover route | Spawn player vào danger không đọc được |
| Execution | Value này có đáng exposure không? | Loot value, threat cues, objective progress, ammo/health/squad status | Reward blind looting hơn route reading |
| Extraction | Tôi có thể bank value này ngay không? | Extract distance, timer, activation rule, contest risk, squad state | Đổi extraction rules mà không cảnh báo |
| Recovery | Chuyện gì xảy ra và tôi làm gì tiếp? | Lost/kept/insured items, XP, quest state, death cause, next CTA | Để player kẹt không có rebuild/redeploy path |

#### Session Length & Pacing

**Target session:** 15–20 minutes (mobile-friendly). Standard raid timer is 25–30 minutes so that a typical run (infiltrate, loot, extract) fits within one session; người chơi who extract early hoặc die early can queue again within the target window. An optional **Quick Raid** mode (e.g. 15-minute raid timer, smaller map hoặc reduced objectives) may be offered for người chơi who want a guaranteed short session. Design pillars: [Design Pillars](https://github.com/oaiba/ExtractionDocument/blob/main/content/ProjectScope/design-pillars-enhanced.md). cơ chế benchmark: [Gameplay Review checklist](Gameplay_Review_Checklist.md).

**Design quyết định (re-planning):** Medical depth is kept (full body-part máu, bleed, fracture, pain, blacked limb) for tactical identity. Operator abilities cách dùng cooldowns only (no per-raid charge limit); maximum \~2 signature uses per 20-minute raid.

**Cross-platform:** Same rules on all platforms (PC, console, mobile). Input và UX vary by device (e.g. hold E vs tap-và-hold for extract, keybinds vs touch layout); Xem [Controls](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Controls.md) và [Gameplay Review checklist](Gameplay_Review_Checklist.md).

***

### Phase 1: Preparation (Safety & Investment)

The preparation phase is the người chơi's last moment of safety. Every quyết định made here sets the stakes for the entire raid.

#### Loadout Philosophy

người chơi fall on a spectrum between two archetypal playstyles:

| Playstyle               | Budget         | Gear Philosophy                             | Risk Tolerance                  | mục tiêu                                                       |
| ----------------------- | -------------- | ------------------------------------------- | ------------------------------- | ---------------------------------------------------------- |
| **Rat** (Low Risk)      | $5,000-10,000  | Cheap vũ khí, minimal giáp, pistol runs   | Low — minimize loss on death    | Sneak, loot, avoid fights, extract quietly                 |
| **Standard** (Balanced) | $15,000-25,000 | Mid-tier vũ khí, medium giáp, full meds   | Medium — calculated engagements | Complete quests, loot efficiently, fight khi advantageous |
| **Chad** (High Risk)    | $40,000-60,000 | Best-in-slot vũ khí, heavy giáp, full kit | High — hunt other người chơi       | Dominate the lobby, chase PvP, extract với địch gear     |

#### Quyết Định Chính

* **Budget vs. Confidence**: "Can I afford to lose this loadout? Do I trust my skill to justify the investment?"
* **Objective Selection**: Choosing between high-traffic quest areas, mid-risk loot runs, hoặc perimeter scavenging.
* **Consumable Packing**: Balancing medical supplies, food, water, và grenades against available inventory space for loot.
* **Insurance Consideration**: Paying 10-20% of loadout giá trị for a chance to recover gear nếu the body is not looted by other người chơi.

#### Risk Tolerance Profiles

```
Conservative Player ("Rat")
  Gear value:  < $10,000
  Decision:    Extract early, dodge fights
  Frequency:   80% survive, low per-raid value
  Long-term:   Slow, steady net positive

Balanced Player ("Standard")
  Gear value:  $15,000-25,000
  Decision:    Fight if advantaged, extract at 50% timer
  Frequency:   55-65% survive, moderate per-raid value
  Long-term:   Healthy growth curve

Aggressive Player ("Chad")
  Gear value:  > $40,000
  Decision:    Seek fights, stay until late extract
  Frequency:   35-45% survive, high per-raid value (when surviving)
  Long-term:   Volatile, feast-or-famine economy
```

**Design Intent**: All three playstyles phải được viable. The economy must support rats mà không making chad gameplay feel unrewarding. Insurance acts as a safety net that scales với investment.

***

### Phase 2: Infiltration (Tension & Information)

The infiltration phase begins the moment the người chơi spawns into the raid. This is khi anticipation transitions into action.

#### Spawn hệ thống

* **Random Insertion**: người chơi spawn at the edges of the map at randomized points. No two người chơi spawn within 50m of each other.
* **10-Second Spawn Protection**: Brief invulnerability to prevent immediate spawn kills.
* **Initial Orientation**: người chơi must quickly identify their location using landmarks — there is no persistent minimap marker at spawn.

#### Sound Discipline

Sound is the most critical information tool in the infiltration phase:

* **Walking** generates low noise (audible at \~15m)
* **Sprinting** generates high noise (audible at \~30m)
* **Crouching** generates minimal noise (audible at \~5m)
* Moving slowly to listen for địch footsteps is the primary defensive skill. _Silence is the first vũ khí._

#### Information Gathering

| source                  | Range         | Reliability | Risk                             |
| ----------------------- | ------------- | ----------- | -------------------------------- |
| Footstep audio          | 15-30m        | High        | None — passive                   |
| Gunshot audio           | 100m+         | High        | None — passive                   |
| Visual spotting         | Line of sight | High        | None nếu concealed                |
| Looting sounds          | 5-10m         | Medium      | None — passive                   |
| Loot beam (Rare+ items) | 30m           | High        | Reveals your position nếu looting |

**Squad shared vision:** The minimap uses merged visibility from the whole squad — any area seen by at least one teammate (hoặc by intel abilities like Spotter Drone, Tactical Overlay) is revealed for the team. Fog of war shows explored-nhưng-unseen areas; pings và marks from teammates persist in fog as last-known info. Xem [LOS, Fog of War & Visibility](LOS_Fog_Visibility.md) for full specification.

**Operator intel roles:** Hawk (Scout) và Glitch (Specialist) provide vision proxies và intel (drone, sensor, overlay) to rõ fog và reveal địch for the whole team; smoke (Obsidian/Recon) và deployable cover (Bastion) can block LOS. chi tiết in [LOS, Fog of War & Visibility](LOS_Fog_Visibility.md) và [Hero Abilities](Hero_Abilities.md).

**Design Intent**: The infiltration phase teaches người chơi that information is more valuable than firepower. A người chơi who listens carefully has a significant advantage over one who sprints carelessly. shared team vision rewards coordination: one scout can rõ fog for the squad và feed intel mà không everyone being in the same room.

***

### Phase 3: Execution (The Peak)

The execution phase is the cảm xúc peak of the raid. Combat encounters, high-giá trị loot discoveries, và quest completions all happen here.

#### The Engagement quyết định

Every người chơi encounter triggers a rapid mental calculation:

```
DETECTION
    |
  Can I win this fight?
  What gear do they have?
  Am I healthy/well-positioned?
    |
  +----YES----+----NO----+
  |           |          |
ENGAGE      FLEE      OBSERVE
  |           |          |
  Win/Lose  Reposition  Wait for opportunity
```

#### The "Greed Check"

This is the single most quan trọng psychological cơ chế in the game. sau acquiring valuable loot, the người chơi faces a binary choice:

* **Extract now** — Secure guaranteed profit, nhưng miss potential gains.
* **Push one more room** — Risk everything for incremental reward.

The greed check intensifies as inventory giá trị increases. A người chơi carrying $50,000 in loot feels the weight of potential loss far more than one carrying $5,000.

**Design Levers:**

* hiển thị rõ loot giá trị counter on the HUD reinforces awareness of what is at stake
* Proximity pings ("Gunshots nearby") increase perceived danger
* Timer cảnh báo tạo artificial urgency
* Quest item notifications ("Found 1/3 needed items") tempt the người chơi to stay

#### Loot Discovery

The dopamine reward for finding rare loot phải được carefully calibrated:

| Rarity    | Visual Feedback        | Audio Feedback       | cảm xúc Response                   |
| --------- | ---------------------- | -------------------- | ------------------------------------ |
| Common    | Minimal highlight      | Quiet pick-up sound  | Neutral                              |
| Uncommon  | Soft glow              | Subtle chime         | Mild satisfaction                    |
| Rare      | hiển thị rõ beam (30m)     | Distinct tone        | Excitement — "Nice find"             |
| Epic      | Bright beam + particle | Rising musical sting | Adrenaline — "I need to extract NOW" |
| Legendary | Pulsing beam + glow    | Full musical phrase  | Panic — "Everyone can see this"      |

***

### Phase 4: Extraction (The Climax)

Extraction is the cảm xúc climax of every raid. The người chơi must navigate to a designated zone, survive a countdown timer, và escape với their loot.

#### Extraction Types

| Type        | Timer | Availability                                | Risk Level                                | ghi chú                            |
| ----------- | ----- | ------------------------------------------- | ----------------------------------------- | -------------------------------- |
| Standard    | 30s   | Always active, 3-4 per map                  | High — known locations, heavily contested | Most common exit                 |
| Emergency   | 15s   | Requires chính/quest item, 1-2 per map        | Medium — hidden, nhưng single-cách dùng           | Faster nhưng harder to access      |
| Vehicle     | 45s   | Limited capacity (4 người chơi), 1 per map     | Very High — arrival noise draws attention | First-come-first-served          |
| Cooperative | 20s   | Requires 2+ người chơi from different factions | Low — rewards trust                       | Reputation bonus for cooperation |

> Xem [Extraction cơ chế](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/Extraction_Mechanics/README.md) for the full interaction design, interruption rules, và counter-play hệ thống.

#### The Anxiety Arc

```
Approaching Extraction Zone
  Tension: 70% — "Am I being followed?"
      |
Enter Zone, Start Timer
  Tension: 90% — "30 seconds. Don't move."
      |
Timer at 15 seconds
  Tension: 95% — "Halfway there. Hearing footsteps?"
      |
Timer at 5 seconds
  Tension: 100% — "Almost out. Please..."
      |
EXTRACTION SUCCESSFUL
  Tension: 0% — Massive dopamine release
```

**Design Intent**: The extraction timer must feel like an eternity. The audio design — helicopter approaching, timer beeping, distant gunshots — tạo a crescendo of anxiety that makes survival feel earned.

***

### Phase 5: Recovery (The Aftermath)

The recovery phase bridges one raid to the next. It transforms raw loot into progression và sets the stage for the next cycle.

#### Post-Raid Workflow

1. **kết quả màn hình** — Display survival thời gian, kills, loot acquired, XP earned
2. **Stash Management** — Organize the "Tetris" inventory, decide what to keep vs. sell
3. **Market Interaction** — Sell excess loot to NPC traders hoặc list on the người chơi flea market
4. **Safe House Upgrades** — Invest materials into passive bonuses (Bitcoin Farm, Medical Station, Workbench)
5. **Quest Turn-In** — Complete quest objectives, unlock new trader tiers
6. **Next Raid Prep** — The loop restarts

#### The "One More Raid" Trigger

sau a successful extraction, người chơi trải nghiệm a confidence boost that drives re-engagement:

```
Successful Extract
    |
"I'm on a hot streak"  →  Queue again immediately
    |
Second Raid Result
    |
  +---------+---------+
  |                   |
  Win Again          Death
  |                   |
"Unstoppable"      "I need to win that back"
  |                   |
  Queue again        Queue again (loss aversion)
```

Both outcomes drive re-engagement. This is the cốt lõi retention cơ chế.

***

### Psychological Hooks

Why do người chơi come back? The extraction loop leverages multiple proven psychological mechanisms:

| Hook                             | Concept                    | Implementation                                                                                                                                             |
| -------------------------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Variable Ratio Reinforcement** | "The Slot Machine"         | Loot containers have random contents. You pull the lever (open the box) hoping for a jackpot. Most times it is junk, nhưng the _chance_ keeps you searching. |
| **Loss Aversion**                | "It's Mine Now"            | Once you loot an item, you feel ownership. Dying feels like having it _stolen_. This anger drives the "one more game" mentality to reclaim losses.         |
| **Sunk chi phí Fallacy**            | "I'm Committed"            | Upgrading the Safe House requires massive resource investment. người chơi play to "justify" the thời gian và money already spent.                                 |
| **Mastery Curve**                | "I'm Getting Better"       | Learning map angles, recoil patterns, và spawn timings is a permanent skill that persists thông qua death và seasonal wipes.                               |
| **Endowment Effect**             | "This Is Worth More To Me" | người chơi overvalue items they found themselves vs. identical items bought from traders. Found-in-raid status reinforces this.                               |
| **Near-Miss Design**             | "So Close..."              | Dying với $50,000 in loot at the extraction door is devastating — nhưng it guarantees the người chơi will queue again to "make up for it."                      |

***

### Economy Design: Faucets và Sinks

To prevent hyper-inflation (where every người chơi has best-in-slot gear), the economy uses a strict Faucet/Sink model.

#### Faucets (Resource Inflow)

These inject giá trị into the economy:

| Faucet         | Description                                                              | Balancing Lever                                                |
| -------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------- |
| Raid Loot      | Server-spawned items in containers và on AI địch                     | Control spawn tables per map per patch                         |
| Scav Mode      | Free zero-risk runs với random loadouts                                 | Limit frequency (1 per 20 min cooldown), moderate loot quality |
| Passive Income | Safe House modules (Bitcoin Farm, Scav Case) generate currency over thời gian | Cap output, require significant investment to build            |
| Trader Stock   | Infinite supply of basic đạn, meds, food from NPC vendors               | giá floor prevents giá trị collapse                            |
| Quest Rewards  | Credits và items for completing objectives                              | One-thời gian per quest line                                        |

#### Sinks (Resource Destruction)

These remove giá trị to maintain scarcity:

| Sink               | Description                                                                    | Impact                                             |
| ------------------ | ------------------------------------------------------------------------------ | -------------------------------------------------- |
| Death Loss         | Uninsured gear is permanently deleted nếu not looted by another người chơi          | primary sink — drives the entire economy           |
| Consumables        | đạn, meds, food, grenades are one-thời gian cách dùng                                    | High-tier đạn is the biggest recurring money sink |
| Insurance Fees     | 10-20% of item giá trị for a _chance_ of recovery                                | Only returns items not looted by others            |
| Market Tax         | Progressive tax on flea market transactions                                    | Prevents infinite money circulation                |
| Safe House Costs   | Massive material dumps required for upgrades                                   | Long-term progression sink                         |
| Repair Degradation | giáp và vũ khí lose max durability khi repaired, eventually becoming scrap | Forces gear rotation, prevents hoarding            |

#### Dynamic Balancing ("The Invisible Hand")

* **Trader Barter Adjustments**: nếu a resource (e.g., Gunpowder) becomes too common, traders demand more of it for high-tier barters, artificially increasing demand.
* **Scarcity Events**: Limited-thời gian events ("Fuel Shortage") reduce cụ thể item spawn rates, draining người chơi reserves as they panic-mua.
* **Seasonal Wipe Cycle**: Periodic economy resets (every 3-6 months) prevent terminal inflation và give all người chơi a fresh start.
