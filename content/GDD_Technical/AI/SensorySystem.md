---
title: "AI Sensory System & Perception"
type: docs
---

##  The "Fair" AI Principle

AI must play by the same rules as the player. **No Omniscience.**
If a player is obscured by smoke, the AI cannot see them. If a player walks slowly (Sneak), the AI cannot hear them.

---

##  Visual Perception (Sight)

### Components
We use `UAIPerceptionComponent` with a customized **Sight Config**.

### 1. Vision Cone (Frustum)
*   **Peripheral Vision Angle:** 90 degrees (Total 180 FOV).
*   **Focus Vision Angle:** 30 degrees (Total 60 FOV).
    *   *Note:* Detection speed is 2x faster inside the Focus cone.

### 2. Detection Ranges (Meters)
| State | Detection Range | Lose Sight Range |
| :--- | :--- | :--- |
| **Clear Day** | 60m | 75m |
| **Night / Fog** | 20m | 30m |
| **Flashlight On** | 40m (Beam only) | 50m |

### 3. Visibility Modifiers (The "Stealth" Formula)
Every tick, the AI calculates a `VisibilityScore` (0.0 to 1.0) for the target.
*   **Distance Factor:** Closer = Higher Score.
*   **Lighting Factor:** Player in Shadow (-50%), Player under Light (+50%).
*   **Posture:** Standing (1.0), Crouching (0.6), Prone (0.3).
*   **Movement:** Sprinting (1.2), Walking (1.0), Stationery (0.8).
*   **Camouflage:** Ghillie Suit reduces score by 30% in foliage.

> **Technical Note:** Use `LineOfSightTo()` with channel `ecc_Visibility`. Check for foliage blocking using `Masked` material opacity.

---

##  Auditory Perception (Hearing)

### Components
We use `UAISense_Hearing`.

### 1. Stickiness of Sound
AI remembers the location where the sound was *generated*, not where the player *is*.
*   *Example:* Player shoots at point A, then sprints to point B. AI will investigate point A first.

### 2. Noise Levels (Radius)
| Action | Radius (Meters) | Loudness (0-1) |
| :--- | :--- | :--- |
| **Gunshot (Unsuppressed)** | 150m | 1.0 |
| **Gunshot (Suppressed)** | 40m | 0.4 |
| **Explosion** | 300m | 1.0 |
| **Sprint Footstep** | 25m | 0.8 |
| **Walk Footstep** | 15m | 0.5 |
| **Crouch Walk** | 3m | 0.1 |
| **Looting Container** | 5m | 0.3 |
| **Reloading** | 2m | 0.2 |

### 3. Occlusion (Walls)
*   Sounds pass through walls but are dampened.
*   **Algorithm:** Raycast from Source to Listener. If hit Wall -> Reduce Loudness by 50%.
*   **Material matters:** Concrete dampens more than Wood.

---

##  Memory & Investigation

### Short-Term Memory (0-10s)
*   AI tracks the `LastKnownPosition` (LKP).
*   If Line of Sight is broken, AI will:
    1.  Move to LKP.
    2.  Wait 2s.
    3.  Look around (animate head).
    4.  Resume patrol or enter "Search Mode".

### Long-Term Memory (10s - 2min)
*   AI remembers that "An enemy was in this sector".
*   Readiness state remains `Alert` (Weapon raised).
*   Patrol speed is slower; perception responsiveness increased.

---

##  Communication (The "Hive Mind")

AI agents share information within a squad radius (20m).

1.  **Direct Witness:** AI_1 sees Player.
2.  **Broadcast:** AI_1 shouts "Contact!" (State Switch).
3.  **Propagation:**
    *   AI_2 (within 20m) receives location data immediately.
    *   AI_3 (50m away) hears the shout but *doesn't* know exact location; enters Alert state.

---

##  Optimization (Budget)

| LOD Level | Distance | Perception Update Rate |
| :--- | :--- | :--- |
| **LOD 0** | < 30m | Every 0.1s (10Hz) |
| **LOD 1** | 30m - 60m | Every 0.5s (2Hz) |
| **LOD 2** | > 60m | Every 2.0s (0.5Hz) or Disabled |

*   **Sense Deactivation:** Disable Sight/Hearing if AI is not rendered and > 200m from any player.


