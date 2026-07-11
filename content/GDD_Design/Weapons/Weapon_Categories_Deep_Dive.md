---
title: "Weapon Categories Deep Dive"
type: docs
weight: 2
---

## Overview

This document expands each weapon genre with design identity, engagement doctrine, hero synergy, build archetypes, matchup matrices, and top-down-specific notes. For full weapon stats and tables see [Weapon Arsenal](../Gameplay/WeaponArsenal.md) and [Weapon Master Database](Weapon_Master_Database.md).

> **Cross-References:** [Weapon Handling Settings](Weapon_Handling_Settings.md) — draw, ADS, movement modifiers; [Weapon Balance Framework](Weapon_Balance_Framework.md) — DPS and TTK; [Characters & Operators](../Characters/_index.md) — class roster for synergy.

---

## Category Requirement Template

Every weapon category must answer the same production questions so balance, UI, audio, and loot placement can evaluate it consistently.

| Requirement | Definition |
| :--- | :--- |
| Role | The combat job: entry, flank, precision, suppression, backup, or ambush |
| Range band | The distance where the category should feel trusted |
| Skill ask | What the player must do well: burst, lead, flank, reload, aim, hold lane |
| Handling tax | Mobility, ADS, recoil, spread, sway, reload, or draw cost |
| Attachment posture | Which stats attachments may improve and what trade-off they must add |
| Counterplay | How opponents read and respond to the weapon |
| UX tells | Audio/VFX/HUD cues that make hits, misses, suppression, and armor interaction readable |

## Role / Counterplay Summary

| Category | Role | Preferred Range | Main Counterplay | Required UX Tell |
| :--- | :--- | :--- | :--- | :--- |
| AR | Flexible baseline | Close-mid / mid | Force reloads, break line, out-specialize | Burst cadence and armor/flesh hit clarity |
| SMG | Fast flank and CQB | Close | Keep distance, armor, pre-aim choke | High RPM audio, falloff, hip-spread bloom |
| Shotgun | Ambush and breach | Very close | Stay outside burst range, bait shot | Pellet impact, spread, reload vulnerability |
| Sniper | Long sightline denial | Long | Smoke, flank, close gap, force movement | Scope glint/sightline cue, lethal recap |
| LMG | Suppression and lane hold | Mid | Rotate, punish reload, flank setup | Suppression audio, tracer/volume cue |
| DMR | Precision pressure | Mid-long | Break sightline, force cadence | Semi-auto rhythm and hit zone clarity |
| Pistol | Backup / recovery | Close | Primary weapon advantage, armor | Fast draw cue, low capacity warning |
| Melee | Silent desperation | Contact | Spacing, awareness, light | Contact-only range and stealth tell |

---

## 1. Assault Rifles (AR)

### Design Identity

Assault rifles are the versatile backbone: effective at medium range, controllable in bursts, and adaptable via attachments. No single "best" situation — they reward positioning and ammo selection rather than raw specialization.

### Engagement Doctrine

- **Optimal range:** 15–45 m. Hold angles, controlled bursts, avoid prolonged full-auto at long range.
- **Squad role:** Primary opener, flex between CQB and medium range, magazine management critical in sustained fights.
- **Positioning:** Pre-aim corners, use cover for reloads, reposition after engagements.

### Hero Synergy Matrix

| Hero Class | Synergy | Reason |
| :--------- | :------ | :----- |
| Assault | High | Damage bonuses (e.g. +25% weapon) amplify AR DPS; frontline AR is default. |
| Recon | High | Intel + AR holds medium range while team flanks; AR as secondary to sniper. |
| Support | Medium | AR for self-defense while healing; versatile for escort/defend. |
| Tank | Low | Often restricted to secondary or LMG; AR less common. |
| Specialist | Medium | AR for neutral engagements; abilities enable repositioning for AR optimal range. |

### Build Archetypes

| Build | Focus | Typical Attachments | Use Case |
| :---- | :---- | :------------------ | :------- |
| **Suppressed Recon** | Stealth, range | Suppressor, ACOG, heavy barrel | Flank, overwatch, first shot advantage |
| **CQB Blitz** | Speed, hip-fire | Short barrel, reflex, angled grip, laser | Building clear, aggressive push |
| **Ranged DMR Hybrid** | Accuracy, damage at range | Heavy barrel, ACOG, bipod (optional) | Hold long angles, semi-auto precision |

### Matchup Matrix (vs Other Genres)

| vs Genre | Close (0–15 m) | Medium (15–40 m) | Long (40 m+) |
| :------- | :-------------: | :--------------: | :----------: |
| SMG | Lose | Win | Win |
| Shotgun | Lose | Win | Win |
| Sniper | Win | Win (if first shot) | Lose |
| LMG | Win | Tie/Lose (sustained) | Lose |
| DMR | Win | Tie | Lose |
| Pistol | Win | Win | Win |
| Melee | Win | Win | Win |

### Top-Down Specific Notes

- Full spatial awareness makes AR angle-holding stronger; enemies cannot approach unseen from above.
- Burst fire and recoil control are more readable from overhead (cone bloom visible). Pre-aim before exposing.

---

## 2. Submachine Guns (SMG)

### Design Identity

SMGs dominate close quarters: high RPM, low per-shot damage, minimal movement penalty. Weak at range; strength is mobility and room-clearing.

### Engagement Doctrine

- **Optimal range:** 0–20 m. Building clear, corners, tight corridors.
- **Squad role:** Entry fragger, flanker, high ammo consumption — carry extra mags.
- **Positioning:** Push with movement, use hip-fire in CQB, avoid open medium-range duels.

### Hero Synergy Matrix

| Hero Class | Synergy | Reason |
| :--------- | :------ | :----- |
| Assault | High | Aggressive push pairs with SMG; stim + SMG TTK in CQB. |
| Recon | Medium | SMG as secondary for when forced into close range. |
| Support | Low | Prefer AR for versatility; SMG niche. |
| Tank | Low | LMG/secondary focus. |
| Specialist | High | Flank + SMG for quick kills; gadget then SMG cleanup. |

### Build Archetypes

| Build | Focus | Typical Attachments | Use Case |
| :---- | :---- | :------------------ | :------- |
| **CQB Assassin** | ADS speed, recoil | Suppressor, reflex, vertical grip | Stealth push, headshot focus |
| **Suppressive Hose** | Capacity, hip-fire | Drum mag, laser, light stock | Hold room, multiple contacts |
| **Budget Runner** | Cost, reliability | Iron sights, comp, standard mag | Rat runs, low risk |

### Matchup Matrix (vs Other Genres)

| vs Genre | Close (0–15 m) | Medium (15–40 m) | Long (40 m+) |
| :------- | :-------------: | :--------------: | :----------: |
| AR | Win | Lose | Lose |
| Shotgun | Lose | Win | Win |
| Sniper | Win | Lose | Lose |
| LMG | Win (mobility) | Lose | Lose |
| DMR | Win | Lose | Lose |
| Pistol | Win | Tie | Lose |
| Melee | Win | Win | Win |

### Top-Down Specific Notes

- Overhead view makes flank routes obvious; SMG players can choose engagement range. Avoid open sightlines.
- Hip-fire cone is forgiving at close range — top-down doesn't change that; movement + hip-fire remains key.

---

## 3. Shotguns

### Design Identity

Shotguns deliver point-blank devastation: high per-pellet damage, limited range, high risk/reward. One-shot potential in confined spaces; useless at distance.

### Engagement Doctrine

- **Optimal range:** 0–12 m. Ambush, corner hold, room clear.
- **Squad role:** Close defense, breach follow-up, ammo count critical (4–8 shells typical).
- **Positioning:** Hold tight angles, never challenge at 20 m+; reposition to force close range.

### Hero Synergy Matrix

| Hero Class | Synergy | Reason |
| :--------- | :------ | :----- |
| Assault | High | Breach + shotgun clear; stim for push. |
| Recon | Low | Range-focused; shotgun contradicts. |
| Support | Medium | Defend point with shotgun; situational. |
| Tank | High | Tank draws aggro; shotgun for CQB when rushed. |
| Specialist | Medium | Trap + shotgun ambush; one-shot potential. |

### Build Archetypes

| Build | Focus | Typical Attachments | Use Case |
| :---- | :---- | :------------------ | :------- |
| **Room Clear** | Spread, capacity | Extended tube, choke (tight spread) | Indoor dominance |
| **Ambush One-Shot** | Damage per pellet | Heavy barrel, no choke (wide) | Corner, door camp |
| **Semi-Auto Spam** | Fire rate (Saiga/AA-12) | Extended mag, comp | CQB suppression |

### Matchup Matrix (vs Other Genres)

| vs Genre | Close (0–15 m) | Medium (15–40 m) | Long (40 m+) |
| :------- | :-------------: | :--------------: | :----------: |
| AR | Win | Lose | Lose |
| SMG | Win | Lose | Lose |
| Sniper | Win | Lose | Lose |
| LMG | Win | Lose | Lose |
| DMR | Win | Lose | Lose |
| Pistol | Win | Lose | Lose |
| Melee | Win | Win | Win |

### Top-Down Specific Notes

- From overhead, pellet spread covers a wider effective angle; shotguns are stronger in top-down CQB than in narrow FPS corridors.
- Enemy approach vectors are visible — ideal for pre-aiming doorways and corners.

---

## 4. Sniper Rifles

### Design Identity

Snipers excel at long-range elimination: high per-shot damage, bolt or slow semi-auto, overwatch and first-shot advantage. Vulnerable if rushed.

### Engagement Doctrine

- **Optimal range:** 50–120+ m. Overwatch, hold long sightlines, patience.
- **Squad role:** Pick priority targets, suppress movement, cover extraction.
- **Positioning:** Elevated or long corridor; minimize exposure; relocate after shots.

### Hero Synergy Matrix

| Hero Class | Synergy | Reason |
| :--------- | :------ | :----- |
| Assault | Low | AR frontline; sniper redundant. |
| Recon | High | Core identity; intel + sniper overwatch. |
| Support | Medium | Sniper for defense while team heals. |
| Tank | Low | Tank holds front; sniper different role. |
| Specialist | Medium | Intel + one-shot; follow-up with abilities. |

### Build Archetypes

| Build | Focus | Typical Attachments | Use Case |
| :---- | :---- | :------------------ | :------- |
| **Overwatch** | Range, stability | 8× scope, heavy barrel, bipod | Fixed position, long angles |
| **Aggressive Sniper** | ADS, follow-up | 4× or ACOG, lighter stock | Semi-auto (SVD/VSS), mid-range |
| **Stealth** | Sound, concealment | Suppressor, low-profile stock | Avoid detection, reposition |

### Matchup Matrix (vs Other Genres)

| vs Genre | Close (0–15 m) | Medium (15–40 m) | Long (40 m+) |
| :------- | :-------------: | :--------------: | :----------: |
| AR | Lose | Win (first shot) | Win |
| SMG | Lose | Win | Win |
| Shotgun | Lose | Win | Win |
| LMG | Lose | Tie | Win |
| DMR | Lose | Tie | Win (higher damage) |
| Pistol | Lose | Win | Win |
| Melee | Lose | Win | Win |

### Top-Down Specific Notes

- Top-down reduces "scope tunnel vision" but long sightlines remain valuable. Sniping is still about positioning and first shot.
- Enemy movement is fully visible from above — leading moving targets and holding angles are easier to read.

---

## 5. Light Machine Guns (LMG)

### Design Identity

LMGs provide sustained fire and area denial: large magazines, bipod option, heavy and slow. Best for holding chokepoints and suppression.

### Engagement Doctrine

- **Optimal range:** 25–55 m. Choke points, open corridors, defensive positions.
- **Squad role:** Suppression, area denial, long reload = vulnerability window.
- **Positioning:** Deploy bipod when possible; avoid CQB; plan reload cover.

### Hero Synergy Matrix

| Hero Class | Synergy | Reason |
| :--------- | :------ | :----- |
| Assault | Medium | Can run LMG for suppression; not default. |
| Recon | Low | Mobility and stealth over LMG. |
| Support | High | Support holds position; LMG denies approach. |
| Tank | High | Tank + LMG identity; heavy weapon fit. |
| Specialist | Low | Prefer mobility and utility. |

### Build Archetypes

| Build | Focus | Typical Attachments | Use Case |
| :---- | :---- | :------------------ | :------- |
| **Bipod Anchor** | Recoil, accuracy | Bipod, heavy barrel, ACOG | Fixed position, long suppressive fire |
| **Mobile LMG** | Ergo, speed | Light stock, red dot, no bipod (RPK-style) | Rare; still slower than AR |
| **Buzzsaw** | Fire rate, capacity | Drum, comp, foregrip | Max DPS, ammo dump |

### Matchup Matrix (vs Other Genres)

| vs Genre | Close (0–15 m) | Medium (15–40 m) | Long (40 m+) |
| :------- | :-------------: | :--------------: | :----------: |
| AR | Lose (mobility) | Win (sustained) | Win |
| SMG | Lose | Win | Win |
| Shotgun | Lose | Win | Win |
| Sniper | Lose | Tie | Lose (one-shot) |
| DMR | Lose | Win | Tie |
| Pistol | Win | Win | Win |
| Melee | Win | Win | Win |

### Top-Down Specific Notes

- Suppression and "bullets near target" are visible from overhead; LMG area denial is easy to read for both shooter and suppressed player.
- Bipod deployment and movement penalty are critical — top-down makes flanking an LMG obvious.

---

## 6. Designated Marksman Rifles (DMR)

### Design Identity

DMRs bridge AR and Sniper: semi-auto precision at medium-long range, faster follow-up than bolt-action, lower per-shot damage than sniper. For players who want accuracy without full sniper commitment.

### Engagement Doctrine

- **Optimal range:** 40–80 m. Semi-auto precision, 2–3 shot kills, reposition between shots.
- **Squad role:** Mid-long range pressure, finish wounded targets, flexible overwatch.
- **Positioning:** Between AR and Sniper positions; use cover for reload and rechamber.

### Hero Synergy Matrix

| Hero Class | Synergy | Reason |
| :--------- | :------ | :----- |
| Assault | Medium | DMR for medium range when not pushing. |
| Recon | High | DMR as primary or secondary to sniper; flexible range. |
| Support | Medium | Hold angle with DMR while team recovers. |
| Tank | Low | Prefer LMG or AR. |
| Specialist | Medium | Intel + DMR for precise picks. |

### Build Archetypes

| Build | Focus | Typical Attachments | Use Case |
| :---- | :---- | :------------------ | :------- |
| **Precision Marksman** | Accuracy, range | ACOG/4×, heavy barrel, bipod | Hold angles, 2-tap kills |
| **Aggressive DMR** | ADS, ergo | Red dot/ACOG, angled grip, light stock | Push with semi-auto precision |
| **Stealth DMR** | Suppressor, low profile | Suppressor, compact stock | Flank, first shot silent |

### Matchup Matrix (vs Other Genres)

| vs Genre | Close (0–15 m) | Medium (15–40 m) | Long (40 m+) |
| :------- | :-------------: | :--------------: | :----------: |
| AR | Lose | Win | Win |
| SMG | Lose | Win | Win |
| Shotgun | Lose | Win | Win |
| Sniper | Lose | Tie | Lose |
| LMG | Win (mobility) | Tie | Lose |
| Pistol | Win | Win | Win |
| Melee | Win | Win | Win |

### Top-Down Specific Notes

- DMR benefits from top-down visibility: see flanks and choose when to engage at optimal range.
- Semi-auto pacing and recoil recovery are clear from overhead; 2–3 shot rhythm is readable.

---

## 7. Pistols

### Design Identity

Pistols are backup and last resort: fast draw, low capacity, acceptable at very close range. Sidearm for when primary is empty or inappropriate.

### Engagement Doctrine

- **Optimal range:** 0–15 m. Emergency only; swap to primary when possible.
- **Squad role:** Finisher, silent option (suppressed variants), sprint-speed runs (lightweight).
- **Positioning:** Use after primary empty or for stealth; avoid open engagement.

### Hero Synergy Matrix

| Hero Class | Synergy | Reason |
| :--------- | :------ | :----- |
| Assault | Medium | Backup after push; not primary. |
| Recon | High | Silent pistol for stealth; sidearm for sniper. |
| Support | Medium | Defend self while healing. |
| Tank | High | Some tanks secondary-only; pistol primary. |
| Specialist | Medium | Utility first; pistol backup. |

### Build Archetypes

| Build | Focus | Typical Attachments | Use Case |
| :---- | :---- | :------------------ | :------- |
| **Stealth Sidearm** | Suppressor, accuracy | Suppressor (USP-S style), night sights | Silent takedowns |
| **Hand Cannon** | Damage (Deagle/Revolver) | High damage, low capacity | Skill-based finisher |
| **Budget Backup** | Cost, reliability | Stock; no attachments | Rat run sidearm |

### Matchup Matrix (vs Other Genres)

| vs Genre | Close (0–15 m) | Medium (15–40 m) | Long (40 m+) |
| :------- | :-------------: | :--------------: | :----------: |
| AR | Lose | Lose | Lose |
| SMG | Lose | Lose | Lose |
| Shotgun | Lose | Lose | Lose |
| Sniper | Win (if close) | Lose | Lose |
| LMG | Win (if close) | Lose | Lose |
| DMR | Lose | Lose | Lose |
| Melee | Tie | Win | Win |

### Top-Down Specific Notes

- Fast draw and movement with pistol are visible; players can choose to run with pistol out for speed.
- Pistol duels at close range are decided by accuracy and movement; top-down makes strafe and aim clear.

---

## 8. Melee Weapons

### Design Identity

Melee is silent and lethal at touch range: backstab multiplier, no ammo, high risk. Default knife always equipped; others are upgrades.

### Engagement Doctrine

- **Optimal range:** 0–2.5 m. Stealth kill, finish downed, or desperation.
- **Squad role:** Silent elimination, no sound signature; vulnerable if missed.
- **Positioning:** Flank, approach from blind spot; never engage armed opponent head-on in open.

### Hero Synergy Matrix

| Hero Class | Synergy | Reason |
| :--------- | :------ | :----- |
| Assault | Medium | Combat knife for push; situational. |
| Recon | High | Stealth + backstab; recon identity. |
| Support | Low | Rarely in melee range. |
| Tank | Low | Prefer guns. |
| Specialist | High | Trap + melee; ambush. |

### Build Archetypes

| Build | Focus | Item | Use Case |
| :---- | :---- | :--- | :------- |
| **Default** | Always available | Combat Knife | Backup, backstab |
| **Heavy Melee** | Damage, reach | Tactical Axe, Machete | Higher one-hit potential |
| **Utility Melee** | CC | Stun Baton | Stun then shoot or escape |

### Matchup Matrix (vs Other Genres)

| vs Genre | Close (0–15 m) | Medium (15–40 m) | Long (40 m+) |
| :------- | :-------------: | :--------------: | :----------: |
| AR | Win (if undetected) | Lose | Lose |
| SMG | Win (if undetected) | Lose | Lose |
| All guns | Win only from stealth/back | Lose | Lose |

### Top-Down Specific Notes

- Approach vectors for melee are visible to both parties; stealth and LOS break are essential.
- Backstab hitbox and facing are clear from overhead — no ambiguity about "from behind."

---

## Cross-References

- [Weapon Arsenal](../Gameplay/WeaponArsenal.md) — Full stats and ammo.
- [Weapon Master Database](Weapon_Master_Database.md) — Per-weapon base and modded stats.
- [Weapon Handling Settings](Weapon_Handling_Settings.md) — Draw, ADS, movement.
- [Weapon Balance Framework](Weapon_Balance_Framework.md) — DPS, TTK, balance levers.
- [Characters & Operators](../Characters/_index.md) — Hero classes and abilities.
