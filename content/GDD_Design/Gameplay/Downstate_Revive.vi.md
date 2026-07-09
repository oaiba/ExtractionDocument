---
title: "Downstate & Revive hệ thống"
type: docs
weight: 18
---

## Tổng Quan

The Downstate & Revive hệ thống determines what happens khi a người chơi's HP reaches zero. Instead of instant death, người chơi enter a vulnerable "Downed" trạng thái from which squadmates can rescue them. This hệ thống adds a critical cooperation cơ chế — và a strategic quyết định for địch: finish the downed người chơi hoặc push forward? It is one of the most team game–feel moments in the entire raid loop.

> **Cross-References:** [Medical hệ thống](Medical_System.md) — HP và body part rules; [Hero Abilities](Hero_Abilities.md) — operator-cụ thể revive interactions; [Extraction cơ chế](Extraction_Mechanics.md) — downed trạng thái trong khi extraction; [Camera hệ thống](Camera_System.md) — downed camera behavior; [Quest & Objective hệ thống](Quest_Objective_System.md) — "Revive 3 teammates" quest type.

---

## Design Philosophy

- **Revive is earned, not automatic.** Getting a teammate up requires physical proximity, thời gian, và vulnerability. Both the reviver và the downed người chơi are exposed.
- **Solo người chơi still have a meaningful death.** Solo queue người chơi go to the standard [death sequence](Camera_System.md) — no self-revive. This maintains consequence parity.
- **The downed trạng thái is a team moment, not a spectator trạng thái.** The downed người chơi can shoot back, slow their bleed, và communicate — they are not helpless.
- **địch have meaningful choices.** Leaving a downed người chơi is a valid tactic (they will die eventually); finishing them is faster nhưng takes thời gian và exposure.

---

## Trigger Conditions

### khi Does Downstate Occur?

| Condition | kết quả |
| :-------- | :----- |
| HP reaches 0 from any damage source | Enter Downstate |
| Solo người chơi HP reaches 0 | **Instant death** — no downstate |
| Squad of 2+, at least 1 squadmate alive | Downstate activates |
| Squad of 2+, all squadmates already dead | **Instant death** (last member alive dies instantly) |
| Explosion / fall damage / bleed tick at 0 HP | Downstate, với accompanying injury status effects |
| Downed người chơi's bleedout timer reached 0 | Instant death while downed |

---

## The Downed trạng thái

### Visual & Camera

- Camera perspective changes to a low-altitude top-down (altitude drops to **8m**, zoomed in).
- The người chơi's nhân vật collapses và is **crawling** — they can move at 15% normal speed.
- máu bar is replaced by a **Bleedout Timer** (red countdown) và a limited **Downed HP pool**.

### Downed HP Pool

| Property | giá trị |
| :------- | :---- |
| **Downed HP** | 30 points (independent of body-part HP) |
| **Damage while downed** | Any incoming damage reduces Downed HP. At 0 = instant death. |
| **Passive bleedout** | −1 Downed HP per 5 seconds (default) |
| **Bleed status effect while downed** | −2 Downed HP per 3 seconds (accelerated) |
| **Maximum downed duration** | 2 minutes (at 30 HP với no damage và no bleed) |
| **Typical downed duration** | 45–90 seconds in combat conditions |

### Downed người chơi Capabilities

| Capability | available | chi tiết |
| :--------- | :-------: | :----- |
| **Move (crawl)** |  | 15% speed; hiển thị rõ crawl animation |
| **Fire sidearm (pistol)** |  | primary vũ khí unavailable; pistol auto-equipped nếu carried |
| **Fire primary vũ khí** |  | Cannot cách dùng two-handed vũ khí while prone |
| **cách dùng medical items (self)** |  Limited | Can cách dùng Bandage hoặc Painkiller from pockets only (not backpack) |
| **Apply tourniquet (slow bleedout)** |  | Slows bleed from −2/3s to −0.5/5s for 30s |
| **Voice comms / ping** |  | Normal team communication |
| **See squad positions** |  | Minimap remains active |
| **Access inventory** |  | Grid inventory locked while downed |
| **Activate active ability** |  | No ability cách dùng while downed |

### địch Interaction với Downed người chơi

| Action | ghi chú |
| :----- | :---- |
| Shooting downed người chơi | Reduces Downed HP; lethal at 0 |
| Looting downed người chơi | Cannot loot downed người chơi — must wait for kill hoặc leave them |
| Finishing (execution) | 1.5s interaction, silenced (no gunshot noise). Instant kill. Makes người chơi lootable. |
| Ignoring downed người chơi | Valid tactic — downed người chơi will die eventually nếu not revived. Risk: pistol has 3m lethal range. |

---

## Revive cơ chế

### Revive Process

1. Reviving squadmate moves within **2m** of downed người chơi.
2. Hold interact button to begin revive (default: hold `F` on PC / hold circle prompt on mobile/console).
3. **Revive timer: 8 seconds** (regardless of gear hoặc class — no speed-up by default).
4. Both người chơi are vulnerable trong khi revive: reviver cannot move hoặc shoot; downed người chơi can still fire pistol.
5. nếu reviver takes any damage trong khi revive, the revive is **cancelled** (progress lost — full 8s required again).
6. On successful revive, downed người chơi stands up at **15% of max HP** on each damaged body part.

### Revive Cooldown on Revived người chơi

sau being revived, the same người chơi can be downed again và revived again — với an escalating penalty:

| Times Revived in Same Raid | Bleedout Timer Reduction |
| :------------------------: | :----------------------- |
| 1st revive | Normal bleedout timer (120s) |
| 2nd revive | 50% bleedout timer (60s) |
| 3rd revive | 25% bleedout timer (30s) — very urgent |
| 4th+ | No bleedout timer — phải được revived within 15s hoặc instant death |

**Design intent:** Prevents "tank" gameplay where one người chơi gets revived repeatedly mà không consequence. Third-thời gian-down tạo extreme urgency.

---

## Operator Interactions

| Operator | Downstate Interaction |
| :------- | :-------------------- |
| **Hawk** (Scout) | Spotter Drone can detect nearby địch trong khi YOUR downstate — the drone continues operating. Drone shares reviver squad's LOS while Hawk is down. |
| **Glitch** (Specialist) | Tactical Overlay (nếu active khi downed) fades to last-known position pings. Does not update while Glitch is down. |
| **Mamba** (Assault) | Adrenaline Rush passive: first thời gian downed per raid, automatically receives one free tourniquet application. |
| **Bastion** (Tank) | Last Stand: at 15% HP (trước going down), triggers 3-second immunity window. nếu healed above 15% trong khi this window, avoids downstate. |
| **Ghost** (Support) | **"Field Medic"** — Revive ability reduced from 8s to 5s. Can revive twice trước requiring a 90s cooldown. Unique class-cụ thể cơ chế. |

> **Ghost's Field Medic** is the only ability that directly modifies the revive cơ chế và is a chính class differentiator. Supporting teammates với fast revives is Ghost's primary role in squad meta.

---

## Extraction While Downed

| Scenario | Behavior |
| :------- | :------- |
| Downed người chơi inside extraction zone | Timer still counts for standing squadmates, NOT for downed người chơi |
| Revived inside extraction zone | Revived người chơi CAN continue extraction nếu timer is still running |
| Downed người chơi extracted by squad | Not possible — downed người chơi phải được revived first to extract |
| Downed người chơi drags self to extraction zone | No extraction while downed — phải được revived |
| All squad members extract while người chơi is downed | Downed người chơi is left behind — dies khi bleedout timer expires |

> **Design note:** The squad cannot "carry" a downed người chơi to extraction. This is intentional — the revive cơ chế forces the squad to stay in the raid together và risk extraction, rather than reaching safety và abandoning a downed member.

---

## Solo người chơi Death (No Downstate)

Solo người chơi die instantly at 0 HP. To compensate for no revive:
- Solo người chơi receive a **10% HP max boost** (per operator passive, scaled for solo queue).
- Solo-cụ thể operator skill — see Operators 6–10 expansion in [Hero Abilities](Hero_Abilities.md).
- Solo debrief màn hình triggers immediately showing cause of death, damage received, loot lost.

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

## HUD & UI Elements trong khi Downstate

| Element | Behavior |
| :------ | :------- |
| **HP bar** | Replaced by Downed HP bar (red) |
| **Bleedout timer** | Large red countdown in center-bottom HUD |
| **Crawl speed indicator** | Footstep icon shows 15% speed trạng thái |
| **Pistol đạn** | Displayed (primary vũ khí HUD slot greyed) |
| **Squad HP bars** | Remain hiển thị rõ — can see who is still alive |
| **Squad positions (minimap)** | Active — can direct reviving squadmate |
| **Ability bar** | Greyed out — abilities unavailable |
| **Reviver proximity indicator** | Revive icon appears khi squadmate is within 2m range |

---

## Anti-Abuse Rules

| Abuse Case | Prevention |
| :--------- | :--------- |
| Solo-queue người chơi using external voice chat to coordinate với squadmates | Server enforces solo queue rule; cannot join match as squad |
| Crawling downed người chơi hiding in inaccessible spot | Crawl speed 15% và camera altitude 8m limit hiding spots |
| Infinite revive cycle | Escalating bleedout timer reduces tolerance per revive |
| Squad using downed người chơi as bait indefinitely | Bleedout timer + Downed HP passive drain from combat pressure |

---

## Tham Chiếu Chéo

- [Medical hệ thống](Medical_System.md) — Body part HP; Bleed status effect while downed.
- [Hero Abilities](Hero_Abilities.md) — Operator-cụ thể downstate và revive abilities.
- [Extraction cơ chế](Extraction_Mechanics.md) — Downed người chơi cannot extract mà không revive.
- [Camera hệ thống](Camera_System.md) — Low-altitude camera trong khi downstate; spectator sau death.
- [Quest & Objective hệ thống](Quest_Objective_System.md) — "Revive 3 teammates" quest type.
- [Movement & Stamina](Movement_and_Stamina.md) — Crawl speed as a movement trạng thái.
