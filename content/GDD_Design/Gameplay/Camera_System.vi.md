---
title: "Camera hệ thống (Top-Down)"
type: docs
weight: 11
---

### Tổng Quan

The camera hệ thống defines how người chơi perceive the game world và is one of the most critical design elements unique to this top-down extraction shooter. Unlike FPS hoặc third-person games, the top-down perspective tạo a **natural information asymmetry** — người chơi see more of the environment nhưng less of the third axis (vertical). Every camera parameter affects tactical quyết định-making, spatial awareness, và the cảm xúc intensity of each raid.

> **Cross-References:** [LOS, Fog of War & Visibility](los_fog_visibility/index.html) — field of view và fog clearing; [Gear cơ chế](gear_mechanics/index.html) — inertia và weight; [Movement & Stamina](movement_and_stamina/index.html) — movement trạng thái affecting zoom; [Controls](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Controls.md) — platform-cụ thể camera input.

***

### Design Philosophy

The camera fulfills three simultaneous roles:

1. **Tactical Display** — Show enough of the map for informed quyết định mà không removing tension.
2. **cảm xúc Amplifier** — Zoom và behavior must reflect cảm xúc trạng thái (calm loot run vs. firefight chaos).
3. **Accessibility Tool** — All người chơi on all platforms receive the same information density.

**cốt lõi rule:** The camera must never be a strategic advantage in itself. A người chơi với better equipment hoặc position không nên gain extra camera range. LOS controls what is _revealed_; the camera controls what is _displayed_.

***

### Camera Parameters

#### Base Configuration

| Parameter                     | giá trị                                                                     | Rationale                                                                         |
| ----------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Camera type**               | Orthographic top-down (fixed)                                             | nhất quán visual scale across the map. No perspective distortion.                |
| **Default altitude**          | 18–22 m above ground                                                      | người chơi model hiển thị rõ at \~20% màn hình height; enough context around them.          |
| **Default FOV (world-space)** | 24×18 m hiển thị rõ area (at 1080p)                                           | Roughly 1.5 người chơi-nhân vật widths of buffer on each side.                       |
| **Camera tilt**               | 90° (true overhead), optional 10–15° isometric lean                       | 90° is fairest for hitbox alignment; mild tilt adds depth cue mà không distorting. |
| **Aspect ratio**              | 16:9 (primary); 18:9 và 21:9 supported với wider horizontal view        | Ultrawide không nên meaningfully extend LOS beyond the 16:9 baseline.            |
| **Frame rate**                | Camera follows nhân vật at render rate (uncapped); physics sync to 60 hz | Smooth camera at high FPS mà không simulation advantage.                           |

#### Dynamic Altitude trạng thái

Camera altitude adjusts based on người chơi action to reflect situational awareness và cảm xúc trạng thái:

| trạng thái            | Trigger                          | Camera Altitude | World-Space FOV | Design Intent                                             |
| ---------------- | -------------------------------- | --------------- | --------------- | --------------------------------------------------------- |
| **Default**      | Walking / idle                   | 20 m            | 24×18 m         | Standard tactical overview                                |
| **Sprinting**    | Sprint trạng thái active              | 22 m (+2 m)     | 26×20 m         | Slight zoom-out — see more ahead khi rotating fast       |
| **Crouching**    | Crouch trạng thái active              | 17 m (−3 m)     | 20×15 m         | Zoom-in — increased awareness of immediate surroundings   |
| **Prone**        | Prone trạng thái active               | 14 m (−6 m)     | 16×12 m         | Most zoomed-in — maximum stealth chi tiết; limited overview |
| **Slow Walk**    | Slow walk trạng thái                  | 16 m (−4 m)     | 19×14 m         | Cautious mode — focus on immediate environment            |
| **In fight**     | Taking damage in last 3 s        | 21 m (+1 m)     | 25×19 m         | Slight zoom-out trong khi combat for địch tracking          |
| **Extraction**   | In extraction zone, timer active | 19 m (−1 m)     | 23×17 m         | Slight zoom-in — heightens vulnerability feeling          |
| **ADS / Aiming** | Aiming/ADS active                | 16 m (−4 m)     | 19×14 m         | Focus on precise aim point                                |

**Transition timing:** Camera altitude transitions are smooth. Transition speed = `distance / 0.25 s` (adjustable in User Settings). Fast transitions preserve responsiveness; very slow transitions feel cinematic nhưng lose tactical giá trị.

***

### Camera Follow Behavior

#### Follow Mode

The camera always centers on the **local người chơi nhân vật** as anchor. The camera does not drift hoặc pan to teammates hoặc ability effects.

| Property             | giá trị                                                    | ghi chú                                                                                             |
| -------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Follow offset**    | nhân vật centered, với 30% offset toward aim direction | Camera leans toward where the người chơi is looking, giving more hiển thị rõ space ahead                  |
| **Offset distance**  | 0–4 m (scales với aim distance from center)             | Capped at 4 m to prevent nhân vật going off-màn hình                                               |
| **Offset active at** | Any thời gian aim direction is >15° from camera center        | Dead zone prevents jitter on small mouse movements                                                |
| **Follow smoothing** | 0.05 s lag (very snap — nearly instant)                  | Any more lag feels "floaty." người chơi receives camera feedback within 1 frame at 60Hz               |
| **Rotation**         | Camera does NOT rotate. Always north-up.                 | Rotating camera in top-down tạo disorientation; fixed north-up is standard for tactical games |

#### Inertia Integration

Per [Gear cơ chế](gear_mechanics/index.html), heavier người chơi have movement inertia. Camera follow dampening scales slightly với weight:

| Weight Tier | Extra camera lag | Effect                                                  |
| ----------- | ---------------- | ------------------------------------------------------- |
| Light       | +0.0 s           | Camera is snappy                                        |
| Medium      | +0.02 s          | Nearly imperceptible                                    |
| Heavy       | +0.05 s          | Subtle "weight" feeling                                 |
| Critical    | +0.08 s          | Camera feels like it's pulling a heavy nhân vật        |
| Overweight  | +0.10 s          | Maximum lag; combined với inertia = very sluggish feel |

**Design intent:** The camera dampening reinforces the weight hệ thống. A heavily encumbered người chơi doesn't just move slowly — the camera carries that feeling of burden.

***

### Indoor & Vertical Geometry

Top-down cameras must handle indoor spaces where walls và rooftops would obscure the người chơi.

#### Building Interior Handling

| Situation                                 | Camera Behavior                                                                       | Trigger                                                   |
| ----------------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| người chơi indoors (ground floor)             | Roof section above người chơi becomes **transparent** (alpha-fade to \~15% opacity)       | người chơi nhân vật collider enters building interior volume |
| người chơi under mezzanine/second floor       | Only the floor section above is transparent; rest of building opaque                  | Per-section trigger, not whole-building                   |
| người chơi on second floor                    | Ground floor becomes slightly opaque (30%) to show floor người chơi is on                 | Vertical zone tag                                         |
| người chơi in tunnel/basement                 | Camera altitude drops to 12 m; ceiling is fully removed                               | Underground volume tag                                    |
| địch inside building (not in người chơi LOS) | Building opacity stays normal — địch silhouette NOT hiển thị rõ thông qua walls            | Server-authoritative LOS; no wallhack                     |
| địch inside building (in người chơi LOS)     | địch renders với building at normal opacity — LOS confirmed from nearby window/door | LOS hệ thống handles render                                 |

**Fade transition:** khi entering/exiting a building, the roof fade transitions in 0.3 s to avoid popping. người chơi in covered positions cannot be spotted thông qua wall opacity from outside (opacity is local render only, no gameplay effect).

#### Multi-Story Map Design Guideline

* Each building với interior access must have at least one **rõ sight-line entry** (doorway, window) hiển thị rõ from outside trước the roof becomes transparent.
* Maximum building height supported by camera: **3 floors**. Taller buildings (tower exteriors) are not entered — used as sniper positions from windows với floor-by-floor LOS.
* Staircases appear as **top-down cross-sections** — stairs look like diagonal lines. người chơi on stairs animate a position "blend" between floor levels.

***

### Camera Zoom — User Control

Người chơi có thể manually adjust camera zoom within a constrained range. This is a preference setting, not a tactical tool (same zoom for all người chơi in the same match).

| Zoom Level         | Altitude | hiển thị rõ area | cách dùng Case                    |
| ------------------ | -------- | ------------ | --------------------------- |
| **Min (−30%)**     | 14 m     | 16×12 m      | Close-quarters combat focus |
| **Default (100%)** | 20 m     | 24×18 m      | Standard                    |
| **Max (+30%)**     | 26 m     | 31×23 m      | Open-field navigation       |

**Rules:**

* Zoom level is **persistent per-session** (saved to User Settings).
* Zoom cannot be temporarily changed trong khi the match as a tactical rotation (no scroll-wheel combat zoom).
* In the Options menu: discrete steps (5 levels), not a continuous slider — prevents micro-optimized zoom advantages.
* **Anti-abuse:** Max zoom is server-validated. No client can display more than `26 m altitude` equivalent of world trạng thái. Wider zoom beyond 26 m would expose LOS-unrevealed areas.

***

### Mobile Camera Controls

Mobile uses touch input; camera behavior adapts mà không changing game information:

| cơ chế                  | PC (mouse + keyboard)                        | Mobile (touch)                                        | ghi chú                                                     |
| ------------------------- | -------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------------- |
| **Camera follow**         | Automatic                                    | Automatic                                             | Same — no manual pan                                      |
| **Aim offset**            | Mouse naturally offsets camera toward cursor | Right thumb stick hoặc drag rotates aim, offsets camera | Same offset logic, different input                        |
| **Zoom adjustment**       | Scroll wheel (in settings menu only)         | Pinch-to-zoom in pause/settings menu only             | Never mid-combat                                          |
| **Building transparency** | Automatic                                    | Automatic                                             | Same trigger                                              |
| **Camera smoothing**      | Slider in settings                           | Slider in settings                                    | Mobile default: +0.03 s extra smoothing for touch comfort |
| **HUD minimap**           | Bottom-left hoặc top-right                     | Bottom-left (thumb reachable)                         | Same information; layout adapts                           |

**Haptic feedback on camera:** Mobile devices produce a short vibration khi the camera altitude transitions (e.g., entering crouch zoom-in). This reinforces trạng thái change mà không a UI prompt.

***

### Ability & Event Camera Overrides

Certain game events temporarily override normal camera behavior:

| Event                         | Override                                                     | Duration                                 | Return                                    |
| ----------------------------- | ------------------------------------------------------------ | ---------------------------------------- | ----------------------------------------- |
| Flashbang within 5 m          | màn hình whites out (overlay); camera altitude unchanged       | 2.5 s (as defined in Hero\_Abilities.md) | Fades back; no camera motion              |
| Signature activation (người chơi) | Camera briefly zooms-out +2 m (0.2 s), then zooms back       | 0.2 s out, 0.5 s return                  | Cinematic "moment" mà không losing control |
| Successful extraction         | Camera altitude rises to 50 m over 3 s (cinematic pull-back) | Until results màn hình                     | Shows nhân vật departing                 |
| Death                         | Camera holds at người chơi's last position for 2 s, then fades   | 2 s hold                                 | Prevents instant spectator confusion      |
| Supply drop (approach)        | No override (informational ping only)                        | —                                        | Map mark is enough                        |
| Contamination entering        | màn hình edges pulse red (vignette); camera unchanged          | Per phase                                | Visual pressure mà không camera disruption |

**Death cam:** sau 2 s fade, transitions to passive spectator mode. người chơi can observe surviving squadmates from the same top-down perspective, với fog-of-war based on that teammate's LOS — not a free-camera ghost view. Xem [Extraction cơ chế](extraction_mechanics/index.html) for spectator post-death rules.

***

### Spectator và Death Camera

#### Post-Death Phase

khi a người chơi dies:

1. **0–2 s:** Camera holds at death position, fade-to-black begins at 1.5 s.
2. **2–4 s:** Transition màn hình: "You have been eliminated." Shows death cause (killed by \[người chơi/AI], location).
3. **4 s+:** người chơi can choose:
   * **Spectate Squad** — top-down camera follows a living teammate (cycle với button). Teammate's LOS applies. Spectator cannot communicate game trạng thái info to teammates (voice chat allowed, text disabled).
   * **Return to Stash** — go to post-game debrief immediately.

#### Spectator Rules

| Rule                           | chi tiết                                                 |
| ------------------------------ | ------------------------------------------------------ |
| Camera follows living teammate | Same altitude as that người chơi's hiện tại trạng thái           |
| LOS in spectator               | Spectator only sees what the followed teammate sees    |
| HUD in spectator               | Minimal: followed teammate HP, inventory weight, timer |
| Marking/pinging                | disabled. Spectator cannot assist teammates            |
| Voice chat                     | Squad voice remains active. Spectator CAN speak        |
| Transition between teammates   | Button cycle; 0.5 s cross-fade between cameras         |

***

### Performance và LOD Targets

| Platform      | Target FPS | Camera render budget                                | ghi chú                                             |
| ------------- | ---------- | --------------------------------------------------- | ------------------------------------------------- |
| PC (High)     | 120+ FPS   | Full world render at max altitude                   | No camera-related performance impact              |
| PC (Medium)   | 60 FPS     | Full world render                                   | Same                                              |
| Console       | 60 FPS     | World render; some particle reduction               | Camera altitude values unchanged                  |
| Mobile (High) | 60 FPS     | Reduced distant LOD beyond 25 m hiển thị rõ radius      | Gameplay identical; visual density reduced        |
| Mobile (Low)  | 30 FPS     | Further LOD reduction; shadows disabled beyond 15 m | Same camera altitudes; visual simplification only |

**Critical rule:** Camera altitude và FOV values are **never** reduced for performance. Visual density (LOD, particles, shadows) scales; what the camera shows is identical across platforms.

***

### Integration với Other hệ thống

| hệ thống               | Camera Interaction                                                                                                                           |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **LOS / Fog of War** | LOS is calculated server-side from người chơi position, not from camera position. Wider zoom does not reveal more.                               |
| **Inertia (Gear)**   | Camera lag scales với weight tier (see above).                                                                                              |
| **Weather**          | Rain, fog, và night reduce _render_ distance (visual only). LOS range is unchanged — Xem [Environmental Hazards](environmental_hazards/index.html). |
| **Minimap**          | Minimap uses merged squad vision — different from the camera view. Camera shows local viewport; minimap shows full explored trạng thái.           |
| **Hero Abilities**   | Ability effects (flashbang, cloak shimmer, smoke) render in the người chơi's viewport at hiện tại camera altitude.                                |
| **Extraction**       | Camera zooms-in trong khi extraction timer for increased tension (altitude −1 m).                                                               |

***

### Summary of chính quyết định

| Topic                      | quyết định                                                                                     |
| -------------------------- | -------------------------------------------------------------------------------------------- |
| **Camera rotation**        | Fixed north-up. Camera does NOT rotate.                                                      |
| **Zoom levels**            | 5 discrete steps within 14–26 m altitude range. No combat-moment zoom.                       |
| **Aim offset**             | Camera leans 30% toward aim direction (0–4 m offset).                                        |
| **Weight-camera coupling** | Camera lag 0.0–0.10 s scales với weight tier.                                               |
| **Indoors**                | Per-section roof transparency on người chơi entry (0.3 s fade). LOS unchanged.                   |
| **Death spectator**        | Top-down follow teammate, teammate LOS applies, no assist.                                   |
| **Mobile parity**          | Same altitude, FOV, và game information. Layout và haptics differ.                         |
| **Server authority**       | Max hiển thị rõ world-trạng thái is altitude-gated server-side. Client cannot exceed 26 m equivalent. |

***

### Tham Chiếu Chéo

* [LOS, Fog of War & Visibility](los_fog_visibility/index.html) — LOS is independent of camera; server-authoritative.
* [Gear cơ chế](gear_mechanics/index.html) — Inertia hệ thống; camera lag couples với weight tier.
* [Environmental Hazards](environmental_hazards/index.html) — Weather effects on visual render (not LOS).
* [Hero Abilities](hero_abilities/index.html) — Flashbang/smoke vision effects in viewport.
* [Extraction cơ chế](extraction_mechanics/index.html) — Extraction camera override; spectator post-death.
* [Movement & Stamina](movement_and_stamina/index.html) — Movement trạng thái driving altitude changes.
* [Controls](https://github.com/oaiba/ExtractionDocument/blob/main/content/GameDesign/Controls.md) — Platform-cụ thể camera input bindings.
