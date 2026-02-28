---
title: "Camera System (Top-Down)"
type: docs
weight: 11
---

## Overview

The camera system defines how players perceive the game world and is one of the most critical design elements unique to this top-down extraction shooter. Unlike FPS or third-person games, the top-down perspective creates a **natural information asymmetry** — players see more of the environment but less of the third axis (vertical). Every camera parameter affects tactical decision-making, spatial awareness, and the emotional intensity of each raid.

> **Cross-References:** [LOS, Fog of War & Visibility](LOS_Fog_Visibility.md) — field of view and fog clearing; [Gear Mechanics](Gear_Mechanics.md) — inertia and weight; [Movement & Stamina](Movement_and_Stamina.md) — movement states affecting zoom; [Controls](../../GameDesign/Controls.md) — platform-specific camera input.

---

## Design Philosophy

The camera fulfills three simultaneous roles:

1. **Tactical Display** — Show enough of the map for informed decisions without removing tension.
2. **Emotional Amplifier** — Zoom and behavior must reflect emotional state (calm loot run vs. firefight chaos).
3. **Accessibility Tool** — All players on all platforms receive the same information density.

**Core rule:** The camera must never be a strategic advantage in itself. A player with better equipment or position should not gain extra camera range. LOS controls what is *revealed*; the camera controls what is *displayed*.

---

## Camera Parameters

### Base Configuration

| Parameter | Value | Rationale |
| :-------- | :---- | :-------- |
| **Camera type** | Orthographic top-down (fixed) | Consistent visual scale across the map. No perspective distortion. |
| **Default altitude** | 18–22 m above ground | Player model visible at ~20% screen height; enough context around them. |
| **Default FOV (world-space)** | 24×18 m visible area (at 1080p) | Roughly 1.5 player-character widths of buffer on each side. |
| **Camera tilt** | 90° (true overhead), optional 10–15° isometric lean | 90° is fairest for hitbox alignment; mild tilt adds depth cue without distorting. |
| **Aspect ratio** | 16:9 (primary); 18:9 and 21:9 supported with wider horizontal view | Ultrawide should not meaningfully extend LOS beyond portrait specs. |
| **Frame rate** | Camera follows character at render rate (uncapped); physics sync to 60 hz | Smooth camera at high FPS without simulation advantage. |

### Dynamic Altitude States

Camera altitude adjusts based on player action to reflect situational awareness and emotional state:

| State | Trigger | Camera Altitude | World-Space FOV | Design Intent |
| :---- | :------ | :-------------- | :-------------- | :------------ |
| **Default** | Walking / idle | 20 m | 24×18 m | Standard tactical overview |
| **Sprinting** | Sprint state active | 22 m (+2 m) | 26×20 m | Slight zoom-out — see more ahead when rotating fast |
| **Crouching** | Crouch state active | 17 m (−3 m) | 20×15 m | Zoom-in — increased awareness of immediate surroundings |
| **Prone** | Prone state active | 14 m (−6 m) | 16×12 m | Most zoomed-in — maximum stealth detail; limited overview |
| **Slow Walk** | Slow walk state | 16 m (−4 m) | 19×14 m | Cautious mode — focus on immediate environment |
| **In fight** | Taking damage in last 3 s | 21 m (+1 m) | 25×19 m | Slight zoom-out during combat for enemy tracking |
| **Extraction** | In extraction zone, timer active | 19 m (−1 m) | 23×17 m | Slight zoom-in — heightens vulnerability feeling |
| **ADS / Aiming** | Aiming/ADS active | 16 m (−4 m) | 19×14 m | Focus on precise aim point |

**Transition timing:** Camera altitude transitions are smooth. Transition speed = `distance / 0.25 s` (adjustable in User Settings). Fast transitions preserve responsiveness; very slow transitions feel cinematic but lose tactical value.

---

## Camera Follow Behavior

### Follow Mode

The camera always centers on the **local player character** as anchor. The camera does not drift or pan to teammates or ability effects.

| Property | Value | Notes |
| :------- | :---- | :---- |
| **Follow offset** | Character centered, with 30% offset toward aim direction | Camera leans toward where the player is looking, giving more visible space ahead |
| **Offset distance** | 0–4 m (scales with aim distance from center) | Capped at 4 m to prevent character going off-screen |
| **Offset active at** | Any time aim direction is >15° from camera center | Dead zone prevents jitter on small mouse movements |
| **Follow smoothing** | 0.05 s lag (very snap — nearly instant) | Any more lag feels "floaty." Player receives camera feedback within 1 frame at 60Hz |
| **Rotation** | Camera does NOT rotate. Always north-up. | Rotating camera in top-down creates disorientation; fixed north-up is standard for tactical games |

### Inertia Integration

Per [Gear Mechanics](Gear_Mechanics.md), heavier players have movement inertia. Camera follow dampening scales slightly with weight:

| Weight Tier | Extra camera lag | Effect |
| :---------- | :--------------- | :----- |
| Light | +0.0 s | Camera is snappy |
| Medium | +0.02 s | Nearly imperceptible |
| Heavy | +0.05 s | Subtle "weight" feeling |
| Critical | +0.08 s | Camera feels like it's pulling a heavy character |
| Overweight | +0.10 s | Maximum lag; combined with inertia = very sluggish feel |

**Design intent:** The camera dampening reinforces the weight system. A heavily encumbered player doesn't just move slowly — the camera carries that feeling of burden.

---

## Indoor & Vertical Geometry

Top-down cameras must handle indoor spaces where walls and rooftops would obscure the player.

### Building Interior Handling

| Situation | Camera Behavior | Trigger |
| :-------- | :-------------- | :------ |
| Player indoors (ground floor) | Roof section above player becomes **transparent** (alpha-fade to ~15% opacity) | Player character collider enters building interior volume |
| Player under mezzanine/second floor | Only the floor section above is transparent; rest of building opaque | Per-section trigger, not whole-building |
| Player on second floor | Ground floor becomes slightly opaque (30%) to show floor player is on | Vertical zone tag |
| Player in tunnel/basement | Camera altitude drops to 12 m; ceiling is fully removed | Underground volume tag |
| Enemy inside building (not in player LOS) | Building opacity stays normal — enemy silhouette NOT visible through walls | Server-authoritative LOS; no wallhack |
| Enemy inside building (in player LOS) | Enemy renders with building at normal opacity — LOS confirmed from nearby window/door | LOS system handles render |

**Fade transition:** When entering/exiting a building, the roof fade transitions in 0.3 s to avoid popping. Players in covered positions cannot be spotted through wall opacity from outside (opacity is local render only, no gameplay effect).

### Multi-Story Map Design Guideline

- Each building with interior access must have at least one **clear sight-line entry** (doorway, window) visible from outside before the roof becomes transparent.
- Maximum building height supported by camera: **3 floors**. Taller buildings (tower exteriors) are not entered — used as sniper positions from windows with floor-by-floor LOS.
- Staircases appear as **top-down cross-sections** — stairs look like diagonal lines. Players on stairs animate a position "blend" between floor levels.

---

## Camera Zoom — User Control

Players can manually adjust camera zoom within a constrained range. This is a preference setting, not a tactical tool (same zoom for all players in the same match).

| Zoom Level | Altitude | Visible area | Use Case |
| :--------- | :------- | :----------- | :------- |
| **Min (−30%)** | 14 m | 16×12 m | Close-quarters combat focus |
| **Default (100%)** | 20 m | 24×18 m | Standard |
| **Max (+30%)** | 26 m | 31×23 m | Open-field navigation |

**Rules:**
- Zoom level is **persistent per-session** (saved to User Settings).
- Zoom cannot be temporarily changed during the match as a tactical rotation (no scroll-wheel combat zoom).
- In the Options menu: discrete steps (5 levels), not a continuous slider — prevents micro-optimized zoom advantages.
- **Anti-abuse:** Max zoom is server-validated. No client can display more than `26 m altitude` equivalent of world state. Wider zoom beyond 26 m would expose LOS-unrevealed areas.

---

## Mobile Camera Controls

Mobile uses touch input; camera behavior adapts without changing game information:

| Mechanic | PC (mouse + keyboard) | Mobile (touch) | Notes |
| :------- | :-------------------- | :------------- | :---- |
| **Camera follow** | Automatic | Automatic | Same — no manual pan |
| **Aim offset** | Mouse naturally offsets camera toward cursor | Right thumb stick or drag rotates aim, offsets camera | Same offset logic, different input |
| **Zoom adjustment** | Scroll wheel (in settings menu only) | Pinch-to-zoom in pause/settings menu only | Never mid-combat |
| **Building transparency** | Automatic | Automatic | Same trigger |
| **Camera smoothing** | Slider in settings | Slider in settings | Mobile default: +0.03 s extra smoothing for touch comfort |
| **HUD minimap** | Bottom-left or top-right | Bottom-left (thumb reachable) | Same information; layout adapts |

**Haptic feedback on camera:** Mobile devices produce a short vibration when the camera altitude transitions (e.g., entering crouch zoom-in). This reinforces state change without a UI prompt.

---

## Ability & Event Camera Overrides

Certain game events temporarily override normal camera behavior:

| Event | Override | Duration | Return |
| :---- | :------- | :------- | :----- |
| Flashbang within 5 m | Screen whites out (overlay); camera altitude unchanged | 2.5 s (as defined in Hero_Abilities.md) | Fades back; no camera motion |
| Signature activation (player) | Camera briefly zooms-out +2 m (0.2 s), then zooms back | 0.2 s out, 0.5 s return | Cinematic "moment" without losing control |
| Successful extraction | Camera altitude rises to 50 m over 3 s (cinematic pull-back) | Until results screen | Shows character departing |
| Death | Camera holds at player's last position for 2 s, then fades | 2 s hold | Prevents instant spectator confusion |
| Supply drop (approach) | No override (informational ping only) | — | Map mark is enough |
| Contamination entering | Screen edges pulse red (vignette); camera unchanged | Per phase | Visual pressure without camera disruption |

**Death cam:** After 2 s fade, transitions to passive spectator mode. Player can observe surviving squadmates from the same top-down perspective, with fog-of-war based on that teammate's LOS — not a free-camera ghost view. See [Extraction Mechanics](Extraction_Mechanics.md) for spectator post-death rules.

---

## Spectator and Death Camera

### Post-Death Phase

When a player dies:

1. **0–2 s:** Camera holds at death position, fade-to-black begins at 1.5 s.
2. **2–4 s:** Transition screen: "You have been eliminated." Shows death cause (killed by [Player/AI], location).
3. **4 s+:** Player can choose:
   - **Spectate Squad** — top-down camera follows a living teammate (cycle with button). Teammate's LOS applies. Spectator cannot communicate game state info to teammates (voice chat allowed, text disabled).
   - **Return to Stash** — go to post-game debrief immediately.

### Spectator Rules

| Rule | Detail |
| :--- | :----- |
| Camera follows living teammate | Same altitude as that player's current state |
| LOS in spectator | Spectator only sees what the followed teammate sees |
| HUD in spectator | Minimal: followed teammate HP, inventory weight, timer |
| Marking/pinging | Disabled. Spectator cannot assist teammates |
| Voice chat | Squad voice remains active. Spectator CAN speak |
| Transition between teammates | Button cycle; 0.5 s cross-fade between cameras |

---

## Performance and LOD Targets

| Platform | Target FPS | Camera render budget | Notes |
| :------- | :--------- | :------------------- | :---- |
| PC (High) | 120+ FPS | Full world render at max altitude | No camera-related performance impact |
| PC (Medium) | 60 FPS | Full world render | Same |
| Console | 60 FPS | World render; some particle reduction | Camera altitude values unchanged |
| Mobile (High) | 60 FPS | Reduced distant LOD beyond 25 m visible radius | Gameplay identical; visual density reduced |
| Mobile (Low) | 30 FPS | Further LOD reduction; shadows disabled beyond 15 m | Same camera altitudes; visual simplification only |

**Critical rule:** Camera altitude and FOV values are **never** reduced for performance. Visual density (LOD, particles, shadows) scales; what the camera shows is identical across platforms.

---

## Integration with Other Systems

| System | Camera Interaction |
| :----- | :----------------- |
| **LOS / Fog of War** | LOS is calculated server-side from player position, not from camera position. Wider zoom does not reveal more. |
| **Inertia (Gear)** | Camera lag scales with weight tier (see above). |
| **Weather** | Rain, fog, and night reduce *render* distance (visual only). LOS range is unchanged — see [Environmental Hazards](Environmental_Hazards.md). |
| **Minimap** | Minimap uses merged squad vision — different from the camera view. Camera shows local viewport; minimap shows full explored state. |
| **Hero Abilities** | Ability effects (flashbang, cloak shimmer, smoke) render in the player's viewport at current camera altitude. |
| **Extraction** | Camera zooms-in during extraction timer for increased tension (altitude −1 m). |

---

## Summary of Key Decisions

| Topic | Decision |
| :---- | :------- |
| **Camera rotation** | Fixed north-up. Camera does NOT rotate. |
| **Zoom levels** | 5 discrete steps within 14–26 m altitude range. No combat-moment zoom. |
| **Aim offset** | Camera leans 30% toward aim direction (0–4 m offset). |
| **Weight-camera coupling** | Camera lag 0.0–0.10 s scales with weight tier. |
| **Indoors** | Per-section roof transparency on player entry (0.3 s fade). LOS unchanged. |
| **Death spectator** | Top-down follow teammate, teammate LOS applies, no assist. |
| **Mobile parity** | Same altitude, FOV, and game information. Layout and haptics differ. |
| **Server authority** | Max visible world-state is altitude-gated server-side. Client cannot exceed 26 m equivalent. |

---

## Cross-References

- [LOS, Fog of War & Visibility](LOS_Fog_Visibility.md) — LOS is independent of camera; server-authoritative.
- [Gear Mechanics](Gear_Mechanics.md) — Inertia system; camera lag couples with weight tier.
- [Environmental Hazards](Environmental_Hazards.md) — Weather effects on visual render (not LOS).
- [Hero Abilities](Hero_Abilities.md) — Flashbang/smoke vision effects in viewport.
- [Extraction Mechanics](Extraction_Mechanics.md) — Extraction camera override; spectator post-death.
- [Movement & Stamina](Movement_and_Stamina.md) — Movement states driving altitude changes.
- [Controls](../../GameDesign/Controls.md) — Platform-specific camera input bindings.
