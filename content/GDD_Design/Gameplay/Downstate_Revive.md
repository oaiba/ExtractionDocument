---
title: "Downstate & Revive System"
type: docs
weight: 18
---

## Overview

The Downstate & Revive system determines what happens when a player's HP reaches zero. Instead of instant death, players enter a vulnerable "Downed" state from which squadmates can rescue them. This system adds a critical cooperation mechanic — and a strategic decision for enemies: finish the downed player or push forward? It is one of the most team game–feel moments in the entire raid loop.

> **Cross-References:** [Medical System](Medical_System.md) — HP and body part rules; [Hero Abilities](Hero_Abilities.md) — operator-specific revive interactions; [Extraction Mechanics](Extraction_Mechanics.md) — downed state during extraction; [Camera System](Camera_System.md) — downed camera behavior; [Quest & Objective System](Quest_Objective_System.md) — "Revive 3 teammates" quest type.

---

## Design Philosophy

- **Revive is earned, not automatic.** Getting a teammate up requires physical proximity, time, and vulnerability. Both the reviver and the downed player are exposed.
- **Solo players still have a meaningful death.** Solo queue players go to the standard [death sequence](Camera_System.md) — no self-revive. This maintains consequence parity.
- **The downed state is a team moment, not a spectator state.** The downed player can shoot back, slow their bleed, and communicate — they are not helpless.
- **Enemies have meaningful choices.** Leaving a downed player is a valid tactic (they will die eventually); finishing them is faster but takes time and exposure.

---

## Trigger Conditions

### When Does Downstate Occur?

| Condition | Result |
| :-------- | :----- |
| HP reaches 0 from any damage source | Enter Downstate |
| Solo player HP reaches 0 | **Instant death** — no downstate |
| Squad of 2+, at least 1 squadmate alive | Downstate activates |
| Squad of 2+, all squadmates already dead | **Instant death** (last member alive dies instantly) |
| Explosion / fall damage / bleed tick at 0 HP | Downstate, with accompanying injury status effects |
| Downed player's bleedout timer reached 0 | Instant death while downed |

---

## The Downed State

### Visual & Camera

- Camera perspective changes to a low-altitude top-down (altitude drops to **8m**, zoomed in).
- The player's character collapses and is **crawling** — they can move at 15% normal speed.
- Health bar is replaced by a **Bleedout Timer** (red countdown) and a limited **Downed HP pool**.

### Downed HP Pool

| Property | Value |
| :------- | :---- |
| **Downed HP** | 30 points (independent of body-part HP) |
| **Damage while downed** | Any incoming damage reduces Downed HP. At 0 = instant death. |
| **Passive bleedout** | −1 Downed HP per 5 seconds (default) |
| **Bleed status effect while downed** | −2 Downed HP per 3 seconds (accelerated) |
| **Maximum downed duration** | 2 minutes (at 30 HP with no damage and no bleed) |
| **Typical downed duration** | 45–90 seconds in combat conditions |

### Downed Player Capabilities

| Capability | Available | Detail |
| :--------- | :-------: | :----- |
| **Move (crawl)** | ✅ | 15% speed; visible crawl animation |
| **Fire sidearm (pistol)** | ✅ | Primary weapon unavailable; pistol auto-equipped if carried |
| **Fire primary weapon** | ❌ | Cannot use two-handed weapons while prone |
| **Use medical items (self)** | ✅ Limited | Can use Bandage or Painkiller from pockets only (not backpack) |
| **Apply tourniquet (slow bleedout)** | ✅ | Slows bleed from −2/3s to −0.5/5s for 30s |
| **Voice comms / ping** | ✅ | Normal team communication |
| **See squad positions** | ✅ | Minimap remains active |
| **Access inventory** | ❌ | Grid inventory locked while downed |
| **Activate active ability** | ❌ | No ability use while downed |

### Enemy Interaction with Downed Player

| Action | Notes |
| :----- | :---- |
| Shooting downed player | Reduces Downed HP; lethal at 0 |
| Looting downed player | Cannot loot downed player — must wait for kill or leave them |
| Finishing (execution) | 1.5s interaction, silenced (no gunshot noise). Instant kill. Makes player lootable. |
| Ignoring downed player | Valid tactic — downed player will die eventually if not revived. Risk: pistol has 3m lethal range. |

---

## Revive Mechanic

### Revive Process

1. Reviving squadmate moves within **2m** of downed player.
2. Hold interact button to begin revive (default: hold `F` on PC / hold circle prompt on mobile/console).
3. **Revive timer: 8 seconds** (regardless of gear or class — no speed-up by default).
4. Both players are vulnerable during revive: reviver cannot move or shoot; downed player can still fire pistol.
5. If reviver takes any damage during revive, the revive is **cancelled** (progress lost — full 8s required again).
6. On successful revive, downed player stands up at **15% of max HP** on each damaged body part.

### Revive Cooldown on Revived Player

After being revived, the same player can be downed again and revived again — with an escalating penalty:

| Times Revived in Same Raid | Bleedout Timer Reduction |
| :------------------------: | :----------------------- |
| 1st revive | Normal bleedout timer (120s) |
| 2nd revive | 50% bleedout timer (60s) |
| 3rd revive | 25% bleedout timer (30s) — very urgent |
| 4th+ | No bleedout timer — must be revived within 15s or instant death |

**Design intent:** Prevents "tank" gameplay where one player gets revived repeatedly without consequence. Third-time-down creates extreme urgency.

---

## Operator Interactions

| Operator | Downstate Interaction |
| :------- | :-------------------- |
| **Hawk** (Scout) | Spotter Drone can detect nearby enemies during YOUR downstate — the drone continues operating. Drone shares reviver squad's LOS while Hawk is down. |
| **Glitch** (Specialist) | Tactical Overlay (if active when downed) fades to last-known position pings. Does not update while Glitch is down. |
| **Mamba** (Assault) | Adrenaline Rush passive: first time downed per raid, automatically receives one free tourniquet application. |
| **Bastion** (Tank) | Last Stand: at 15% HP (before going down), triggers 3-second immunity window. If healed above 15% during this window, avoids downstate. |
| **Ghost** (Support) | **"Field Medic"** — Revive ability reduced from 8s to 5s. Can revive twice before requiring a 90s cooldown. Unique class-specific mechanic. |

> **Ghost's Field Medic** is the only ability that directly modifies the revive mechanic and is a key class differentiator. Supporting teammates with fast revives is Ghost's primary role in squad meta.

---

## Extraction While Downed

| Scenario | Behavior |
| :------- | :------- |
| Downed player inside extraction zone | Timer still counts for standing squadmates, NOT for downed player |
| Revived inside extraction zone | Revived player CAN continue extraction if timer is still running |
| Downed player extracted by squad | Not possible — downed player must be revived first to extract |
| Downed player drags self to extraction zone | No extraction while downed — must be revived |
| All squad members extract while player is downed | Downed player is left behind — dies when bleedout timer expires |

> **Design note:** The squad cannot "carry" a downed player to extraction. This is intentional — the revive mechanic forces the squad to stay in the raid together and risk extraction, rather than reaching safety and abandoning a downed member.

---

## Solo Player Death (No Downstate)

Solo players die instantly at 0 HP. To compensate for no revive:
- Solo players receive a **10% HP max boost** (per operator passive, scaled for solo queue).
- Solo-specific operator skill — see Operators 6–10 expansion in [Hero Abilities](Hero_Abilities.md).
- Solo debrief screen triggers immediately showing cause of death, damage received, loot lost.

---

## Post-Death Sequence (Squad Context)

```
Player HP → 0
  |
  ├── Solo queue → Instant death → Post-game debrief
  |
  └── Squad queue (squadmate alive)
        ↓
    DOWNED STATE (crawl, pistol, self-aid)
        ↓
    ┌── Squadmate reaches & revives
    │     ↓ Revived at 15% HP; continues raid
    |
    └── Bleedout timer expires / enemy executes / Downed HP → 0
          ↓ DEAD
          ↓
      Spectate squad camera (see Camera_System.md)
      OR
      Return to Stash → Post-game debrief
```

---

## HUD & UI Elements During Downstate

| Element | Behavior |
| :------ | :------- |
| **HP bar** | Replaced by Downed HP bar (red) |
| **Bleedout timer** | Large red countdown in center-bottom HUD |
| **Crawl speed indicator** | Footstep icon shows 15% speed state |
| **Pistol ammo** | Displayed (primary weapon HUD slot greyed) |
| **Squad HP bars** | Remain visible — can see who is still alive |
| **Squad positions (minimap)** | Active — can direct reviving squadmate |
| **Ability bar** | Greyed out — abilities unavailable |
| **Reviver proximity indicator** | Revive icon appears when squadmate is within 2m range |

---

## Anti-Abuse Rules

| Abuse Case | Prevention |
| :--------- | :--------- |
| Solo-queue players using external voice chat to coordinate with squadmates | Server enforces solo queue rule; cannot join match as squad |
| Crawling downed player hiding in inaccessible spot | Crawl speed 15% and camera altitude 8m limit hiding spots |
| Infinite revive cycle | Escalating bleedout timer reduces tolerance per revive |
| Squad using downed player as bait indefinitely | Bleedout timer + Downed HP passive drain from combat pressure |

---

## Cross-References

- [Medical System](Medical_System.md) — Body part HP; Bleed status effect while downed.
- [Hero Abilities](Hero_Abilities.md) — Operator-specific downstate and revive abilities.
- [Extraction Mechanics](Extraction_Mechanics.md) — Downed player cannot extract without revive.
- [Camera System](Camera_System.md) — Low-altitude camera during downstate; spectator after death.
- [Quest & Objective System](Quest_Objective_System.md) — "Revive 3 teammates" quest type.
- [Movement & Stamina](Movement_and_Stamina.md) — Crawl speed as a movement state.
