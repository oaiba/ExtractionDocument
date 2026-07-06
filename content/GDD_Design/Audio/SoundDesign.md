---
title: "Audio Design & Soundscapes"
type: docs
---

##  Audio Design Philosophy

In an Extraction Shooter, **Sound is Information**.

*   **Tactical Priority:** Every sound must have a gameplay purpose. If it doesn't help the player survive, it's noise.
*   **Occlusion & Propagation:** Sounds must react realistically to walls, floors, and distance.
*   **Mobile Enhancement:** Since many play without headphones, we use **Visual Sound Indicators** (See [Navigation Map](../GameDesign/NavigationAndMap.md)) to complement the audio.

---

##  The Soundscape (By Zone)

### 1. Industrial Zone ("The Factory")
*   **Key Mood:** Oppressive, Mechanic, Echoing.
*   **Ambience:** Low-frequency hum of generators (50Hz), distant metal stress groans, dripping water in tunnels.
*   **Reverb:** Large halls have long decay (2-3s). Tight offices have short, dry slap-back.
*   **Unique Cue:** *The Alarm*. When the "Lab" opens, a klaxon blares for 10s, masking footsteps.

### 2. Neon Slums ("The Undercity")
*   **Key Mood:** Chaotic, Cyberpunk, Wet.
*   **Ambience:** Constant heavy rain (White noise masking distant shots), neon lights buzzing, distant police sirens.
*   **Vertical Audio:** Critical distinction between footsteps "Above" (Metal/Roof) vs "Below" (Wet Concrete/Street).
*   **Unique Cue:** *The Train*. Every 5 mins, a subway passes underground, shaking the screen and drowning out ALL audio for 15s.

### 3. The Wilderness ("The Mire")
*   **Key Mood:** Isolation, Organic, Deceptive.
*   **Ambience:** Wind howling through trees, flies buzzing near bodies, squishing mud.
*   **Occlusion:** Fog dampens high frequencies. Gunshots sound "duller" and harder to pinpoint directionally.
*   **Unique Cue:** *Heartbeat*. Within the chemical gas zones, the player's heartbeat becomes audible and speeds up.

---

##  Weapon & Combat Audio

### Weapon Signatures
Every gun must be instantly identifiable by its "Crack" (Supersonic snap) and "Thump" (Muzzle blast).

| Weapon Class   | Audio Profile                            | Distant Read   |
| :------------- | :--------------------------------------- | :------------- |
| **Sniper**     | Sharp, high-pitch crack. Long tail echo. | "Thunder clap" |
| **Shotgun**    | Low-end boom. Short decay.               | "Heavy slam"   |
| **SMG**        | Rapid, lighter pops. Like a zipper.      | "Typewriter"   |
| **Surpressed** | Mechanical bolt click > Muzzle gas hiss. | "Stapler"      |

### Impact Sounds (Material Physics)
*   **Flesh:** Wet "Thud".
*   **Helmet/Armor:** Distinct "Dink" or "Crack" to confirm hits.
*   **Concrete:** Dry "Chip".
*   **Metal:** Loud "Ping" (Richochet).

---

##  Movement & Foley

### Footsteps (The Meta)
Footsteps are the #1 way players track each other.

*   **Walk:** Audible up to 20m.
*   **Sprint:** Audible up to 40m. Heavier bass impact.
*   **Crouch:** Audible up to 5m. Very soft shuffle.
*   **Stationary (Aiming):** Fabric rustle only when turning quickly.

### Surface Materials
1.  **Concrete:** Standard boot clop.
2.  **Metal Grate:** Hollow, metallic resonance (Loudest).
3.  **Water/Mud:** Splashing/Sucking sound (Distinctive).
4.  **Glass/Crunch:** Sharp, high-frequency crunch (Dangerous).

---

##  Voice & Dialogue

### Operator Barks (Automatic)
Characters react to game states automatically (can be muted in "Tactical Mode").
*   *Reloading:* "Dry!" or "Mag out!"
*   *Taking Damage:* Pained grunt (Directional).
*   *Throwing Grenade:* "Frag out!"

### Gestural Wheel
Silent hand signals triggers specific localized whispers:
*   "Hold fire."
*   "On me."
*   "Enemy ahead."

---

##  Technical Implementation

*   **Wwise / FMOD Integration:** For dynamic mixing.
*   **Priority System:**
    1.  Enemy Footsteps within 10m (High Priority).
    2.  Incoming Fire (High Priority).
    3.  Teammate Audio (Medium).
    4.  Ambience (Low - Ducks when shooting).



