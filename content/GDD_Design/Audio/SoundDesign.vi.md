---
title: "Audio Design & Soundscapes"
type: docs
---

## Audio Design Philosophy

In an Extraction Shooter, **Sound is Information**.

*   **Tactical Priority:** Every sound must have a gameplay mục đích. nếu it doesn't giúp the người chơi survive, it's noise.
*   **Occlusion & Propagation:** Sounds must react realistically to walls, floors, và distance.
*   **Mobile Enhancement:** Since many play mà không headphones, we cách dùng **Visual Sound Indicators** (Xem [Navigation Map](../gamedesign/navigationandmap/index.html)) to complement the audio.

---

## The Soundscape (By Zone)

### 1. Industrial Zone ("The Factory")
*   **chính Mood:** Oppressive, cơ chế, Echoing.
*   **Ambience:** Low-frequency hum of generators (50Hz), distant metal stress groans, dripping water in tunnels.
*   **Reverb:** Large halls have long decay (2-3s). Tight offices have short, dry slap-back.
*   **Unique Cue:** *The Alarm*. khi the "Lab" opens, a klaxon blares for 10s, masking footsteps.

### 2. Neon Slums ("The Undercity")
*   **chính Mood:** Chaotic, Cyberpunk, Wet.
*   **Ambience:** Constant heavy rain (White noise masking distant shots), neon lights buzzing, distant police sirens.
*   **Vertical Audio:** Critical distinction between footsteps "Above" (Metal/Roof) vs "Below" (Wet Concrete/Street).
*   **Unique Cue:** *The Train*. Every 5 mins, a subway passes underground, shaking the màn hình và drowning out ALL audio for 15s.

### 3. The Wilderness ("The Mire")
*   **chính Mood:** Isolation, Organic, Deceptive.
*   **Ambience:** Wind howling thông qua trees, flies buzzing near bodies, squishing mud.
*   **Occlusion:** Fog dampens high frequencies. Gunshots sound "duller" và harder to pinpoint directionally.
*   **Unique Cue:** *Heartbeat*. Within the chemical gas zones, the người chơi's heartbeat becomes audible và speeds up.

---

## vũ khí & Combat Audio

### vũ khí Signatures
Every gun phải được instantly identifiable by its "Crack" (Supersonic snap) và "Thump" (Muzzle blast).

| vũ khí Class   | Audio Profile                            | Distant Read   |
| :------------- | :--------------------------------------- | :------------- |
| **Sniper**     | Sharp, high-pitch crack. Long tail echo. | "Thunder clap" |
| **Shotgun**    | Low-end boom. Short decay.               | "Heavy slam"   |
| **SMG**        | Rapid, lighter pops. Like a zipper.      | "Typewriter"   |
| **Surpressed** | cơ chế bolt click > Muzzle gas hiss. | "Stapler"      |

### Impact Sounds (Material Physics)
*   **Flesh:** Wet "Thud".
*   **Helmet/giáp:** Distinct "Dink" hoặc "Crack" to confirm hits.
*   **Concrete:** Dry "Chip".
*   **Metal:** Loud "Ping" (Richochet).

---

## Movement & Foley

### Footsteps (The Meta)
Footsteps are the #1 way người chơi track each other.

*   **Walk:** Audible up to 20m.
*   **Sprint:** Audible up to 40m. Heavier bass impact.
*   **Crouch:** Audible up to 5m. Very soft shuffle.
*   **Stationary (Aiming):** Fabric rustle only khi turning quickly.

### Surface Materials
1.  **Concrete:** Standard boot clop.
2.  **Metal Grate:** Hollow, metallic resonance (Loudest).
3.  **Water/Mud:** Splashing/Sucking sound (Distinctive).
4.  **Glass/Crunch:** Sharp, high-frequency crunch (Dangerous).

---

## Voice & Dialogue

### Operator Barks (Automatic)
nhân vật react to game trạng thái automatically (can be muted in "Tactical Mode").
*   *Reloading:* "Dry!" hoặc "Mag out!"
*   *Taking Damage:* Pained grunt (Directional).
*   *Throwing Grenade:* "Frag out!"

### Gestural Wheel
Silent hand signals triggers cụ thể localized whispers:
*   "Hold fire."
*   "On me."
*   "địch ahead."

---

## Technical Implementation

*   **Wwise / FMOD Integration:** For dynamic mixing.
*   **Priority hệ thống:**
    1.  địch Footsteps within 10m (High Priority).
    2.  Incoming Fire (High Priority).
    3.  Teammate Audio (Medium).
    4.  Ambience (Low - Ducks khi shooting).
