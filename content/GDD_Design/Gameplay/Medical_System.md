---
title: Medical System
type: docs
weight: 3
---

# Medical System

### System Overview

The medical system prioritizes realistic injury management over arcade-style HP regeneration. Players must diagnose the specific type of injury and apply the correct treatment. This creates a secondary layer of tactical decision-making: _you are never truly safe until you are healed._

**Core Principles:**

* **Body Part Health**: Total HP (e.g., 440) is distributed across Head, Thorax, Stomach, Right Arm, Left Arm, Right Leg, Left Leg. Each part has independent HP.
* **No Auto-Regen**: Health does not recover over time without specific Stimulant buffs.
* **Animation Lock**: Using medical items prevents shooting. Players must find cover before treating injuries.
* **Correct Treatment Required**: Using the wrong item wastes resources and time. A bandage cannot fix a fracture.

***

### Body Part Health Distribution

| Body Part | Base HP | Destruction Consequence                         | Critical? |
| --------- | :-----: | ----------------------------------------------- | :-------: |
| Head      |    35   | Instant death                                   |    Yes    |
| Thorax    |    85   | Instant death                                   |    Yes    |
| Stomach   |    70   | Rapid dehydration and energy loss (-4/sec each) |     No    |
| Right Arm |    60   | Aim instability, reduced search speed (-30%)    |     No    |
| Left Arm  |    60   | Aim instability, reduced search speed (-30%)    |     No    |
| Right Leg |    65   | Cannot sprint, movement speed -45%              |     No    |
| Left Leg  |    65   | Cannot sprint, movement speed -45%              |     No    |
| **Total** | **440** |                                                 |           |

**Damage Overflow**: When a non-critical limb reaches 0 HP, further damage to that limb distributes to adjacent body parts at 1.5x multiplier. This prevents players from ignoring limb damage entirely.

***

### Status Effects and Injuries

| Status Effect    | Visual/Audio Cue                                                                | Gameplay Impact                                                                        | Treatment                                             |
| ---------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **Light Bleed**  | Minor blood drips on HUD edges, persistent dripping sound                       | Drains 0.8 HP/sec distributed across all limbs                                         | Bandage, Army Bandage, any Medkit                     |
| **Heavy Bleed**  | Heavy blood splatter on screen, gushing sound                                   | Drains 4.0 HP/sec. Leaves a visible blood trail on the ground that enemies can follow  | Tourniquet (Esmarch/CAT), Hemostatic Syringe          |
| **Fracture**     | Cracking sound on impact. Character gasps/grunts during movement                | **Leg**: Cannot sprint, speed -45%. **Arm**: Aim unsteady, search speed -30%           | Splints (Aluminum/Grizzly Kit)                        |
| **Pain**         | Screen blurs, tunnel vision. Character moans (audible to nearby players at 10m) | Visual distortion. Aim tremors. Reduced turn speed                                     | Analgesics (Painkillers, Morphine, Propital)          |
| **Blacked Limb** | Limb icon turns black/red on the body HUD display                               | **Leg**: Permanent limp. **Stomach**: Rapid resource drain. **Arm**: Major aim penalty | Surgical Kit (CMS/Surv12) restores limb to partial HP |
| **Contusion**    | Tinnitus ringing, all audio muffled for duration                                | Cannot hear footsteps or environmental audio for 20-60 seconds                         | None (time decay) or specific Stimulant injection     |

#### Cross-Platform

Triage rules, body-part HP, and treatment effects are the same on all platforms. **Input:** PC uses hotkeys for meds (rig slots); mobile may use a heal wheel or quick-select; console uses d-pad or radial menu. Animation lock and vulnerability during healing apply regardless of input. See [Controls](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Controls.md) for platform-specific bindings.

***

### Healing Priority Flowchart

When injured, players must triage in the correct order to survive:

```
STEP 1: Am I dying?
    |
  Heavy Bleed (4 HP/sec)?  ──YES──>  Apply Tourniquet FIRST
    |                                 (You have ~20 seconds before critical)
    NO
    |
  Light Bleed (0.8 HP/sec)?  ──YES──>  Apply Bandage
    |                                   (Less urgent, but still constant drain)
    NO
    |
STEP 2: Am I functional?
    |
  Fracture (Leg)?  ──YES──>  Apply Splint
    |                         (Cannot escape without sprint capability)
    NO
    |
  Pain active?  ──YES──>  Use Painkiller
    |                      (Aim tremors make fighting impossible)
    NO
    |
STEP 3: Am I healthy enough?
    |
  Low HP on any limb?  ──YES──>  Use Medkit to restore HP
    |                              (Prioritize Thorax > Stomach > Legs > Arms)
    NO
    |
  Blacked limb?  ──YES──>  Use Surgical Kit (only if safe, takes 16-20 seconds)
    |
    NO
    |
  COMBAT READY — Return to action
```

**Design Intent**: This triage system rewards medical knowledge. A player who heals in the wrong order (e.g., using a medkit before stopping a heavy bleed) wastes precious time and resources while still losing HP.

***

### Medical Items

#### Bleeding Control

| Item               | Use Time | Uses | Effect                                         | Animation                    |
| ------------------ | :------: | :--: | ---------------------------------------------- | ---------------------------- |
| Aseptic Bandage    |   2.0s   |   1  | Cures Light Bleed                              | Wrapping gauze around limb   |
| Army Bandage       |   2.0s   |   2  | Cures Light Bleed                              | Wrapping olive-drab dressing |
| Esmarch Tourniquet |   5.0s   |   1  | Cures Heavy Bleed                              | Tightening red rubber strap  |
| CAT Tourniquet     |   3.0s   |   1  | Cures Heavy Bleed                              | Cranking plastic windlass    |
| Hemostatic Syringe |   2.0s   |   3  | Cures Heavy Bleed (deals 10 HP damage to limb) | Injecting coagulant          |

#### Trauma Kits (HP Restoration)

Kits can stop bleeds but consume significantly more durability than dedicated items.

| Item            | Use Time | Capacity | Special Properties                                           |
| --------------- | :------: | :------: | ------------------------------------------------------------ |
| AI-2 ("Cheese") |   2.0s   |  100 HP  | Fast use. **Cannot** stop bleeds.                            |
| Car First Aid   |   3.0s   |  220 HP  | Stops Light Bleed (consumes 40 durability)                   |
| Salewa Kit      |   3.0s   |  400 HP  | Stops Light (45) and Heavy Bleed (175)                       |
| IFAK            |   3.0s   |  300 HP  | Compact (1 inventory slot). Stops Light (30) and Heavy (210) |
| AFAK            |   3.0s   |  400 HP  | Military grade. Stops Light (30) and Heavy (170)             |
| Grizzly Kit     |   5.0s   |  1800 HP | Backpack-size item. Heals Fractures, Bleeds, and HP          |

#### Surgery Kits

| Item                | Use Time | Uses | Effect                                                                    |
| ------------------- | :------: | :--: | ------------------------------------------------------------------------- |
| Immobilizing Splint |   3.0s   |   1  | Removes Fracture                                                          |
| Aluminum Splint     |   3.0s   |   5  | Removes Fracture. Lightweight, reusable                                   |
| CMS Kit             |   16.0s  |   5  | Restores Blacked Limb to 40% Max HP. **Cannot** operate on Head or Thorax |
| Surv12 Field Kit    |   20.0s  |  15  | Restores Blacked Limb to 80% Max HP. Also removes Fractures               |

#### Injectors and Painkillers

| Item                | Duration | Hydration Cost | Effect                                                           |
| ------------------- | :------: | :------------: | ---------------------------------------------------------------- |
| Analgin Painkillers |    80s   |       -15      | Removes Pain. Cheap, blister pack                                |
| Ibuprofen           |   280s   |       -5       | Removes Pain. Bottle with 15 uses                                |
| Golden Star Balm    |   350s   |  -5 (+Energy)  | Removes Pain + Regenerates Energy                                |
| Morphine Injector   |   300s   |       -10      | Instant use (no animation delay). Removes Pain                   |
| Propital            |   240s   |       -5       | Removes Pain + Passive Health Regen (1 HP/sec)                   |
| Adrenaline          |    60s   |       -20      | Removes Pain + Strength/Endurance boost. Improved recoil control |

***

### Interaction Design

#### Animation Lock Rules

* **Cannot shoot, sprint, or use abilities** while healing
* **Can crouch and slow-walk** during healing animations
* **Cancellation**: Player can cancel healing by pressing the fire button, but the item is still partially consumed (50% durability loss on cancel)
* **Interrupt on damage**: Taking damage during healing cancels the animation. The item is not consumed, but the player must restart

#### Teammate Healing

* Players can heal teammates who are within 1.5m and stationary
* Teammate healing takes **1.5x the normal use time** (requires more careful application)
* The healer is fully animation-locked and cannot defend themselves
* **Design Intent**: Teammates become vulnerable together, creating high-risk high-reward cooperative moments

#### Healing in Different Contexts

| Context                          | Recommended Approach                                        |
| -------------------------------- | ----------------------------------------------------------- |
| Behind hard cover                | Full healing sequence — triage all injuries                 |
| Soft cover (can be shot through) | Quick-fix only — stop worst bleed, painkiller, re-engage    |
| In the open                      | Retreat first. Never heal without cover                     |
| During extraction timer          | Pre-heal before entering zone. Cannot heal while extracting |

***

### Toxicity and Overdose

#### Toxicity System

Overusing injectors accumulates a hidden "Toxin" bar:

* Each injection adds 15-25 Toxin points (varies by item)
* Toxin naturally decays at 2 points/sec when not using stimulants
* **Toxin Thresholds:**

| Toxin Level | Effect                                              |
| ----------- | --------------------------------------------------- |
| 0-30        | No effect                                           |
| 30-60       | Mild tremors (cosmetic only)                        |
| 60-80       | Aim tremors (+15% sway), slight screen desaturation |
| 80-100      | Heavy tremors, vision darkening, -1 HP/sec damage   |
| 100         | Overdose — immediate blackout (death in-raid)       |

#### Overdose Mechanic

Using 2+ painkiller-class items simultaneously triggers an overdose state:

* Vision blurring and color desaturation
* Rapid dehydration (-4 Hydration/sec)
* Cannot sprint for the overdose duration (30 seconds)

#### Tolerance Buildup

Over multiple raids within a session window (2 hours), repeated stimulant use builds tolerance:

* First use: Full effect duration
* Second use in window: 80% effect duration
* Third use in window: 60% effect duration
* Tolerance resets after 2 hours of real time or after using a Detox item (rare consumable)

***

### Design Rationale

#### Why Not Simple HP Bars?

A simple "take damage, use medkit, full health" system removes several critical design layers:

1. **Tactical Depth**: Triage order creates a skill ceiling. Experienced players heal faster and more efficiently.
2. **Resource Tension**: Players must choose which medical items to carry, sacrificing inventory space for loot.
3. **Decision Under Pressure**: Healing mid-fight requires finding cover, choosing the right item, and accepting the animation lock vulnerability.
4. **Audio Information**: Healing sounds (bandage wrapping, syringe injection) are audible to nearby enemies, creating risk during treatment.
5. **Persistent Consequence**: A blacked limb cannot be fully restored in-raid. The player must operate at reduced capacity for the remainder of the session.

> See [Combat, Weapons & Gear](https://github.com/oaiba/ExtractionDocument/blob/main/content/Combat/README.md) for how armor durability and penetration interact with the body part damage system.
