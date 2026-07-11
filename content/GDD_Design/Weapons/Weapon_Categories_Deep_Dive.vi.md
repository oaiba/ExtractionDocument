---
title: "vũ khí Categories Deep Dive"
type: docs
weight: 2
---

## Tổng Quan

This tài liệu expands each vũ khí genre với design identity, engagement doctrine, hero synergy, build archetypes, matchup matrices, và top-down-cụ thể ghi chú. For full vũ khí stats và tables Xem [vũ khí Arsenal](../gameplay/weaponarsenal/index.html) và [vũ khí Master Database](weapon_master_database/index.html).

> **Cross-References:** [vũ khí Handling Settings](weapon_handling_settings/index.html) — draw, ADS, movement modifiers; [vũ khí Balance Framework](weapon_balance_framework/index.html) — DPS và TTK; [nhân vật & Operators](../nhân vật/_index.md) — class roster for synergy.

---

## Category Requirement Template

Mỗi weapon category phải trả lời cùng bộ câu hỏi production để balance, UI, audio, và loot placement đánh giá nhất quán.

| Requirement | Definition |
| :--- | :--- |
| Role | Combat job: entry, flank, precision, suppression, backup, hoặc ambush |
| Range band | Khoảng cách mà category nên đáng tin |
| Skill ask | Player phải làm tốt gì: burst, lead, flank, reload, aim, hold lane |
| Handling tax | Mobility, ADS, recoil, spread, sway, reload, hoặc draw cost |
| Attachment posture | Stat nào attachment được cải thiện và trade-off cần thêm |
| Counterplay | Opponent đọc và phản ứng với weapon như thế nào |
| UX tells | Audio/VFX/HUD cues làm hit, miss, suppression, armor interaction readable |

## Role / Counterplay Summary

| Category | Role | Preferred Range | Main Counterplay | Required UX Tell |
| :--- | :--- | :--- | :--- | :--- |
| AR | Flexible baseline | Close-mid / mid | Force reloads, break line, out-specialize | Burst cadence và armor/flesh hit clarity |
| SMG | Fast flank và CQB | Close | Keep distance, armor, pre-aim choke | High RPM audio, falloff, hip-spread bloom |
| Shotgun | Ambush và breach | Very close | Stay outside burst range, bait shot | Pellet impact, spread, reload vulnerability |
| Sniper | Long sightline denial | Long | Smoke, flank, close gap, force movement | Scope glint/sightline cue, lethal recap |
| LMG | Suppression và lane hold | Mid | Rotate, punish reload, flank setup | Suppression audio, tracer/volume cue |
| DMR | Precision pressure | Mid-long | Break sightline, force cadence | Semi-auto rhythm và hit zone clarity |
| Pistol | Backup / recovery | Close | Primary weapon advantage, armor | Fast draw cue, low capacity warning |
| Melee | Silent desperation | Contact | Spacing, awareness, light | Contact-only range và stealth tell |

---

## 1. Assault Rifles (AR)

### Design Identity

Assault rifles are the versatile backbone: effective at medium range, controllable in bursts, và adaptable via attachments. No single "best" situation — they reward positioning và đạn selection rather than raw specialization.

### Engagement Doctrine

- **Optimal range:** 15–45 m. Hold angles, controlled bursts, avoid prolonged full-auto at long range.
- **Squad role:** primary opener, flex between CQB và medium range, magazine management critical in sustained fights.
- **Positioning:** Pre-aim corners, cách dùng cover for reloads, reposition sau engagements.

### Hero Synergy matrix

| Hero Class | Synergy | Reason |
| :--------- | :------ | :----- |
| Assault | High | Damage bonuses (e.g. +25% vũ khí) amplify AR DPS; frontline AR is default. |
| Recon | High | Intel + AR holds medium range while team flanks; AR as secondary to sniper. |
| Support | Medium | AR for self-defense while healing; versatile for escort/defend. |
| Tank | Low | Often restricted to secondary hoặc LMG; AR less common. |
| Specialist | Medium | AR for neutral engagements; abilities enable repositioning for AR optimal range. |

### Build Archetypes

| Build | Focus | Typical Attachments | cách dùng Case |
| :---- | :---- | :------------------ | :------- |
| **Suppressed Recon** | Stealth, range | Suppressor, ACOG, heavy barrel | Flank, overwatch, first shot advantage |
| **CQB Blitz** | Speed, hip-fire | Short barrel, reflex, angled grip, laser | Building rõ, aggressive push |
| **Ranged DMR Hybrid** | Accuracy, damage at range | Heavy barrel, ACOG, bipod (optional) | Hold long angles, semi-auto precision |

### Matchup matrix (vs Other Genres)

| vs Genre | Close (0–15 m) | Medium (15–40 m) | Long (40 m+) |
| :------- | :-------------: | :--------------: | :----------: |
| SMG | Lose | Win | Win |
| Shotgun | Lose | Win | Win |
| Sniper | Win | Win (nếu first shot) | Lose |
| LMG | Win | Tie/Lose (sustained) | Lose |
| DMR | Win | Tie | Lose |
| Pistol | Win | Win | Win |
| Melee | Win | Win | Win |

### Top-Down cụ thể ghi chú

- Full spatial awareness makes AR angle-holding stronger; địch cannot approach unseen from above.
- Burst fire và recoil control are more dễ đọc from overhead (cone bloom hiển thị rõ). Pre-aim trước exposing.

---

## 2. Submachine Guns (SMG)

### Design Identity

SMGs dominate close quarters: high RPM, low per-shot damage, minimal movement penalty. Weak at range; strength is mobility và room-clearing.

### Engagement Doctrine

- **Optimal range:** 0–20 m. Building rõ, corners, tight corridors.
- **Squad role:** Entry fragger, flanker, high đạn consumption — carry extra mags.
- **Positioning:** Push với movement, cách dùng hip-fire in CQB, avoid open medium-range duels.

### Hero Synergy matrix

| Hero Class | Synergy | Reason |
| :--------- | :------ | :----- |
| Assault | High | Aggressive push pairs với SMG; stim + SMG TTK in CQB. |
| Recon | Medium | SMG as secondary for khi forced into close range. |
| Support | Low | Prefer AR for versatility; SMG niche. |
| Tank | Low | LMG/secondary focus. |
| Specialist | High | Flank + SMG for quick kills; gadget then SMG cleanup. |

### Build Archetypes

| Build | Focus | Typical Attachments | cách dùng Case |
| :---- | :---- | :------------------ | :------- |
| **CQB Assassin** | ADS speed, recoil | Suppressor, reflex, vertical grip | Stealth push, headshot focus |
| **Suppressive Hose** | Capacity, hip-fire | Drum mag, laser, light stock | Hold room, multiple contacts |
| **Budget Runner** | chi phí, reliability | Iron sights, comp, standard mag | Rat runs, low risk |

### Matchup matrix (vs Other Genres)

| vs Genre | Close (0–15 m) | Medium (15–40 m) | Long (40 m+) |
| :------- | :-------------: | :--------------: | :----------: |
| AR | Win | Lose | Lose |
| Shotgun | Lose | Win | Win |
| Sniper | Win | Lose | Lose |
| LMG | Win (mobility) | Lose | Lose |
| DMR | Win | Lose | Lose |
| Pistol | Win | Tie | Lose |
| Melee | Win | Win | Win |

### Top-Down cụ thể ghi chú

- Overhead view makes flank routes obvious; SMG Người chơi có thể choose engagement range. Avoid open sightlines.
- Hip-fire cone is forgiving at close range — top-down doesn't change that; movement + hip-fire remains chính.

---

## 3. Shotguns

### Design Identity

Shotguns deliver point-blank devastation: high per-pellet damage, limited range, high risk/reward. One-shot potential in confined spaces; useless at distance.

### Engagement Doctrine

- **Optimal range:** 0–12 m. Ambush, corner hold, room rõ.
- **Squad role:** Close defense, breach follow-up, đạn count critical (4–8 shells typical).
- **Positioning:** Hold tight angles, never challenge at 20 m+; reposition to force close range.

### Hero Synergy matrix

| Hero Class | Synergy | Reason |
| :--------- | :------ | :----- |
| Assault | High | Breach + shotgun rõ; stim for push. |
| Recon | Low | Range-focused; shotgun contradicts. |
| Support | Medium | Defend point với shotgun; situational. |
| Tank | High | Tank draws aggro; shotgun for CQB khi rushed. |
| Specialist | Medium | Trap + shotgun ambush; one-shot potential. |

### Build Archetypes

| Build | Focus | Typical Attachments | cách dùng Case |
| :---- | :---- | :------------------ | :------- |
| **Room rõ** | Spread, capacity | Extended tube, choke (tight spread) | Indoor dominance |
| **Ambush One-Shot** | Damage per pellet | Heavy barrel, no choke (wide) | Corner, door camp |
| **Semi-Auto Spam** | Fire rate (Saiga/AA-12) | Extended mag, comp | CQB suppression |

### Matchup matrix (vs Other Genres)

| vs Genre | Close (0–15 m) | Medium (15–40 m) | Long (40 m+) |
| :------- | :-------------: | :--------------: | :----------: |
| AR | Win | Lose | Lose |
| SMG | Win | Lose | Lose |
| Sniper | Win | Lose | Lose |
| LMG | Win | Lose | Lose |
| DMR | Win | Lose | Lose |
| Pistol | Win | Lose | Lose |
| Melee | Win | Win | Win |

### Top-Down cụ thể ghi chú

- From overhead, pellet spread covers a wider effective angle; shotguns are stronger in top-down CQB than in narrow FPS corridors.
- địch approach vectors are hiển thị rõ — ideal for pre-aiming doorways và corners.

---

## 4. Sniper Rifles

### Design Identity

Snipers excel at long-range elimination: high per-shot damage, bolt hoặc slow semi-auto, overwatch và first-shot advantage. Vulnerable nếu rushed.

### Engagement Doctrine

- **Optimal range:** 50–120+ m. Overwatch, hold long sightlines, patience.
- **Squad role:** Pick priority targets, suppress movement, cover extraction.
- **Positioning:** Elevated hoặc long corridor; minimize exposure; relocate sau shots.

### Hero Synergy matrix

| Hero Class | Synergy | Reason |
| :--------- | :------ | :----- |
| Assault | Low | AR frontline; sniper redundant. |
| Recon | High | cốt lõi identity; intel + sniper overwatch. |
| Support | Medium | Sniper for defense while team heals. |
| Tank | Low | Tank holds front; sniper different role. |
| Specialist | Medium | Intel + one-shot; follow-up với abilities. |

### Build Archetypes

| Build | Focus | Typical Attachments | cách dùng Case |
| :---- | :---- | :------------------ | :------- |
| **Overwatch** | Range, stability | 8× scope, heavy barrel, bipod | Fixed position, long angles |
| **Aggressive Sniper** | ADS, follow-up | 4× hoặc ACOG, lighter stock | Semi-auto (SVD/VSS), mid-range |
| **Stealth** | Sound, concealment | Suppressor, low-profile stock | Avoid detection, reposition |

### Matchup matrix (vs Other Genres)

| vs Genre | Close (0–15 m) | Medium (15–40 m) | Long (40 m+) |
| :------- | :-------------: | :--------------: | :----------: |
| AR | Lose | Win (first shot) | Win |
| SMG | Lose | Win | Win |
| Shotgun | Lose | Win | Win |
| LMG | Lose | Tie | Win |
| DMR | Lose | Tie | Win (higher damage) |
| Pistol | Lose | Win | Win |
| Melee | Lose | Win | Win |

### Top-Down cụ thể ghi chú

- Top-down reduces "scope tunnel vision" nhưng long sightlines remain valuable. Sniping is still about positioning và first shot.
- địch movement is fully hiển thị rõ from above — leading moving targets và holding angles are easier to read.

---

## 5. Light Machine Guns (LMG)

### Design Identity

LMGs provide sustained fire và area denial: large magazines, bipod option, heavy và slow. Best for holding chokepoints và suppression.

### Engagement Doctrine

- **Optimal range:** 25–55 m. Choke points, open corridors, defensive positions.
- **Squad role:** Suppression, area denial, long reload = vulnerability window.
- **Positioning:** Deploy bipod khi possible; avoid CQB; plan reload cover.

### Hero Synergy matrix

| Hero Class | Synergy | Reason |
| :--------- | :------ | :----- |
| Assault | Medium | Can run LMG for suppression; not default. |
| Recon | Low | Mobility và stealth over LMG. |
| Support | High | Support holds position; LMG denies approach. |
| Tank | High | Tank + LMG identity; heavy vũ khí fit. |
| Specialist | Low | Prefer mobility và utility. |

### Build Archetypes

| Build | Focus | Typical Attachments | cách dùng Case |
| :---- | :---- | :------------------ | :------- |
| **Bipod Anchor** | Recoil, accuracy | Bipod, heavy barrel, ACOG | Fixed position, long suppressive fire |
| **Mobile LMG** | Ergo, speed | Light stock, red dot, no bipod (RPK-style) | Rare; still slower than AR |
| **Buzzsaw** | Fire rate, capacity | Drum, comp, foregrip | Max DPS, đạn dump |

### Matchup matrix (vs Other Genres)

| vs Genre | Close (0–15 m) | Medium (15–40 m) | Long (40 m+) |
| :------- | :-------------: | :--------------: | :----------: |
| AR | Lose (mobility) | Win (sustained) | Win |
| SMG | Lose | Win | Win |
| Shotgun | Lose | Win | Win |
| Sniper | Lose | Tie | Lose (one-shot) |
| DMR | Lose | Win | Tie |
| Pistol | Win | Win | Win |
| Melee | Win | Win | Win |

### Top-Down cụ thể ghi chú

- Suppression và "bullets near target" are hiển thị rõ from overhead; LMG area denial is easy to read for both shooter và suppressed người chơi.
- Bipod deployment và movement penalty are critical — top-down makes flanking an LMG obvious.

---

## 6. Designated Marksman Rifles (DMR)

### Design Identity

DMRs bridge AR và Sniper: semi-auto precision at medium-long range, faster follow-up than bolt-action, lower per-shot damage than sniper. For người chơi who want accuracy mà không full sniper commitment.

### Engagement Doctrine

- **Optimal range:** 40–80 m. Semi-auto precision, 2–3 shot kills, reposition between shots.
- **Squad role:** Mid-long range pressure, finish wounded targets, flexible overwatch.
- **Positioning:** Between AR và Sniper positions; cách dùng cover for reload và rechamber.

### Hero Synergy matrix

| Hero Class | Synergy | Reason |
| :--------- | :------ | :----- |
| Assault | Medium | DMR for medium range khi not pushing. |
| Recon | High | DMR as primary hoặc secondary to sniper; flexible range. |
| Support | Medium | Hold angle với DMR while team recovers. |
| Tank | Low | Prefer LMG hoặc AR. |
| Specialist | Medium | Intel + DMR for precise picks. |

### Build Archetypes

| Build | Focus | Typical Attachments | cách dùng Case |
| :---- | :---- | :------------------ | :------- |
| **Precision Marksman** | Accuracy, range | ACOG/4×, heavy barrel, bipod | Hold angles, 2-tap kills |
| **Aggressive DMR** | ADS, ergo | Red dot/ACOG, angled grip, light stock | Push với semi-auto precision |
| **Stealth DMR** | Suppressor, low profile | Suppressor, compact stock | Flank, first shot silent |

### Matchup matrix (vs Other Genres)

| vs Genre | Close (0–15 m) | Medium (15–40 m) | Long (40 m+) |
| :------- | :-------------: | :--------------: | :----------: |
| AR | Lose | Win | Win |
| SMG | Lose | Win | Win |
| Shotgun | Lose | Win | Win |
| Sniper | Lose | Tie | Lose |
| LMG | Win (mobility) | Tie | Lose |
| Pistol | Win | Win | Win |
| Melee | Win | Win | Win |

### Top-Down cụ thể ghi chú

- DMR benefits from top-down visibility: see flanks và choose khi to engage at optimal range.
- Semi-auto pacing và recoil recovery are rõ from overhead; 2–3 shot rhythm is dễ đọc.

---

## 7. Pistols

### Design Identity

Pistols are backup và last resort: fast draw, low capacity, acceptable at very close range. Sidearm for khi primary is empty hoặc inappropriate.

### Engagement Doctrine

- **Optimal range:** 0–15 m. Emergency only; swap to primary khi possible.
- **Squad role:** Finisher, silent option (suppressed variants), sprint-speed runs (lightweight).
- **Positioning:** cách dùng sau primary empty hoặc for stealth; avoid open engagement.

### Hero Synergy matrix

| Hero Class | Synergy | Reason |
| :--------- | :------ | :----- |
| Assault | Medium | Backup sau push; not primary. |
| Recon | High | Silent pistol for stealth; sidearm for sniper. |
| Support | Medium | Defend self while healing. |
| Tank | High | Some tanks secondary-only; pistol primary. |
| Specialist | Medium | Utility first; pistol backup. |

### Build Archetypes

| Build | Focus | Typical Attachments | cách dùng Case |
| :---- | :---- | :------------------ | :------- |
| **Stealth Sidearm** | Suppressor, accuracy | Suppressor (USP-S style), night sights | Silent takedowns |
| **Hand Cannon** | Damage (Deagle/Revolver) | High damage, low capacity | Skill-based finisher |
| **Budget Backup** | chi phí, reliability | Stock; no attachments | Rat run sidearm |

### Matchup matrix (vs Other Genres)

| vs Genre | Close (0–15 m) | Medium (15–40 m) | Long (40 m+) |
| :------- | :-------------: | :--------------: | :----------: |
| AR | Lose | Lose | Lose |
| SMG | Lose | Lose | Lose |
| Shotgun | Lose | Lose | Lose |
| Sniper | Win (nếu close) | Lose | Lose |
| LMG | Win (nếu close) | Lose | Lose |
| DMR | Lose | Lose | Lose |
| Melee | Tie | Win | Win |

### Top-Down cụ thể ghi chú

- Fast draw và movement với pistol are hiển thị rõ; Người chơi có thể choose to run với pistol out for speed.
- Pistol duels at close range are decided by accuracy và movement; top-down makes strafe và aim rõ.

---

## 8. Melee vũ khí

### Design Identity

Melee is silent và lethal at touch range: backstab multiplier, no đạn, high risk. Default knife always equipped; others are upgrades.

### Engagement Doctrine

- **Optimal range:** 0–2.5 m. Stealth kill, finish downed, hoặc desperation.
- **Squad role:** Silent elimination, no sound signature; vulnerable nếu missed.
- **Positioning:** Flank, approach from blind spot; never engage armed opponent head-on in open.

### Hero Synergy matrix

| Hero Class | Synergy | Reason |
| :--------- | :------ | :----- |
| Assault | Medium | Combat knife for push; situational. |
| Recon | High | Stealth + backstab; recon identity. |
| Support | Low | Rarely in melee range. |
| Tank | Low | Prefer guns. |
| Specialist | High | Trap + melee; ambush. |

### Build Archetypes

| Build | Focus | Item | cách dùng Case |
| :---- | :---- | :--- | :------- |
| **Default** | Always available | Combat Knife | Backup, backstab |
| **Heavy Melee** | Damage, reach | Tactical Axe, Machete | Higher one-hit potential |
| **Utility Melee** | CC | Stun Baton | Stun then shoot hoặc escape |

### Matchup matrix (vs Other Genres)

| vs Genre | Close (0–15 m) | Medium (15–40 m) | Long (40 m+) |
| :------- | :-------------: | :--------------: | :----------: |
| AR | Win (nếu undetected) | Lose | Lose |
| SMG | Win (nếu undetected) | Lose | Lose |
| All guns | Win only from stealth/back | Lose | Lose |

### Top-Down cụ thể ghi chú

- Approach vectors for melee are hiển thị rõ to both parties; stealth và LOS break are essential.
- Backstab hitbox và facing are rõ from overhead — no mơ hồ about "from behind."

---

## Tham Chiếu Chéo

- [vũ khí Arsenal](../gameplay/weaponarsenal/index.html) — Full stats và đạn.
- [vũ khí Master Database](weapon_master_database/index.html) — Per-vũ khí base và modded stats.
- [vũ khí Handling Settings](weapon_handling_settings/index.html) — Draw, ADS, movement.
- [vũ khí Balance Framework](weapon_balance_framework/index.html) — DPS, TTK, balance levers.
- [nhân vật & Operators](../nhân vật/_index.md) — Hero classes và abilities.
