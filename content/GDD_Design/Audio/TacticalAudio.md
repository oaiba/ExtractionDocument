# Tactical Audio - Combat Sound Design

**[← Back to Soundscape](./Soundscape.md)** | **[Index](../README.md)** | **[Next: Voice Lines →](./VoiceLines.md)**

---

## 👣 Footstep Audio System

### Philosophy

**"Footsteps are the Meta"** - In extraction shooters, footsteps are the most important information source for tracking enemies.

### Movement Mode Audio

**Hearing Ranges:**
```
┌─────────────────────────────────────────────────┐
│ Movement Mode │ Range │ Volume │ Character     │
├─────────────────────────────────────────────────┤
│ Sprint        │ 40m   │ -6dB   │ Heavy, urgent │
│ Run           │ 30m   │ -10dB  │ Clear, rhythmic│
│ Walk          │ 20m   │ -16dB  │ Moderate pace │
│ Crouch Walk   │ 8m    │ -24dB  │ Soft shuffle  │
│ Crouch Idle   │ 3m    │ -32dB  │ Fabric rustle │
│ Prone (future)│ 5m    │ -28dB  │ Scraping      │
└─────────────────────────────────────────────────┘
```

### Surface Materials

#### Concrete/Asphalt (Most Common)
```
Sound Character: Solid, neutral boot impact
Frequency Focus: Mid-range (500Hz-2kHz)
Variations: 8 samples per movement type

Walking:
├── Step_Concrete_Walk_01 → Standard boot clop
├── Step_Concrete_Walk_02 → Slight scuff
├── Step_Concrete_Walk_03 → Heel first
└── ... (8 variations)

Running:
├── Heavier impact
├── Faster cadence
└── More bass content
```

#### Metal Grating (LOUDEST - High Risk)
```
Sound Character: Hollow, resonant, metallic ring
Frequency Focus: High-mids (1kHz-4kHz) + low resonance
Hearing Bonus: +50% range (60m sprint audible)

Distinctive traits:
├── Hollow "clang" on impact
├── Structural vibration tail
├── Very high recognition factor
└── Players AVOID this surface
```

#### Water/Mud (DISTINCTIVE)
```
Sound Character: Wet, splashing, sucking
Frequency Focus: Broadband splash + low squelch
Hearing Bonus: +30% range

Shallow Water (ankle):
├── Splash on step
├── Dripping on lift
└── Rhythmic sloshing

Deep Water (knee+):
├── Heavy displacement
├── Wading sounds
├── Movement speed penalty (audio cue: slower)

Mud:
├── Sucking sound on lift
├── Squelch on step
├── Sticky, labored feel
```

#### Grass/Vegetation
```
Sound Character: Soft, rustling, organic
Frequency Focus: High frequencies (2kHz-6kHz)
Hearing Range: Reduced by 20%

Dry Grass:
├── Crisp crackle
├── Swishing sound
└── Light footfall

Wet Grass:
├── Muffled steps
├── Occasional squish
└── Quieter overall
```

#### Wood (Flooring/Platforms)
```
Sound Character: Creaky, hollow, resonant
Frequency Focus: Low-mids with creaks

Old Wood:
├── Creaking boards (random)
├── Hollow resonance
├── Distinct from concrete

Solid Wood:
├── Thud-like impact
├── Less creak
└── Moderate resonance
```

#### Glass/Debris (DANGER - Noise Trap)
```
Sound Character: Sharp, high-pitched crunch
Frequency Focus: High (4kHz-8kHz)
Hearing Bonus: +60% range (cannot stealth)

Behavior:
├── Unavoidable crunch sound
├── Alerts nearby players/AI
├── Environmental hazard for stealth
└── Can be seen and avoided
```

#### Carpet/Fabric (Indoor - Quietest)
```
Sound Character: Muffled, soft, dampened
Frequency Focus: Very low presence
Hearing Range: Reduced by 40%

Benefits:
├── Ideal for stealth approaches
├── Near-silent at crouch
└── Found in offices, hotels
```

---

## 🔫 Weapon Audio

### Gunfire Characteristics

**Audio Components:**
```
Every gunshot = 4 layers:

1. MUZZLE BLAST (Source)
   └── The explosion at barrel end
   └── Defines weapon "punch"

2. MECHANICAL ACTION (Source)
   └── Bolt cycling, hammer strike
   └── Adds detail and rhythm

3. SUPERSONIC CRACK (If applicable)
   └── Bullet breaking sound barrier
   └── Heard before muzzle blast at distance

4. TAIL/REVERB (Environment)
   └── Reflections and decay
   └── Changes by location
```

### Weapon Audio Profiles

#### Assault Rifles
```
┌─────────────────────────────────────────────────┐
│ Weapon    │ Character        │ Distant Sound   │
├─────────────────────────────────────────────────┤
│ AK-47     │ Heavy, punchy    │ "Thunderclaps"  │
│ M4/AR-15  │ Sharp, snappy    │ "Crackling"     │
│ SCAR      │ Balanced, solid  │ "Deep pops"     │
└─────────────────────────────────────────────────┘

Fire Rate Audio: Distinct rhythm per weapon
Magazine Empty: Click sound (no more firing)
```

#### SMGs
```
┌─────────────────────────────────────────────────┐
│ Weapon    │ Character        │ Distant Sound   │
├─────────────────────────────────────────────────┤
│ MP5       │ Rapid, contained │ "Sewing machine"│
│ Vector    │ Ultra-fast, light│ "Zipper"        │
│ UMP       │ Slower, thumpier │ "Stapler"       │
└─────────────────────────────────────────────────┘

Note: Higher fire rate = more blended sound
```

#### Sniper Rifles
```
┌─────────────────────────────────────────────────┐
│ Weapon    │ Character            │ Distant     │
├─────────────────────────────────────────────────┤
│ AWM       │ Massive boom         │ "Thunder"   │
│ SVD       │ Sharp crack          │ "Whip crack"│
│ M24       │ Deep, echoing        │ "Distant boom"│
└─────────────────────────────────────────────────┘

Characteristic: Long reverb tail, unmistakable
```

#### Shotguns
```
┌─────────────────────────────────────────────────┐
│ Weapon    │ Character            │ Distant     │
├─────────────────────────────────────────────────┤
│ Pump      │ Massive low-end      │ "Cannon"    │
│ Semi-Auto │ Rapid booms          │ "Drum beats"│
│ Double    │ Two-shot thunder     │ "Double tap"│
└─────────────────────────────────────────────────┘

Pump Action: Distinct "chunk-chunk" between shots
```

#### Suppressed Weapons
```
Sound Reduction: -15dB to -25dB
Range Reduction: 70% less audible distance

Components:
├── Muzzle: Hissing gas release
├── Mechanical: Bolt action prominent
├── Supersonic: Still audible (unless subsonic ammo)
└── Tail: Minimal reverb

Distant Sound: "Stapler" or "Nail gun"
Player Advantage: Harder to pinpoint direction
```

### Distance-Based Gunfire

```
┌─────────────────────────────────────────────────┐
│ Distance  │ Sound Character                     │
├─────────────────────────────────────────────────┤
│ 0-20m     │ Full impact, all frequencies        │
│ 20-50m    │ -6dB, losing high end               │
│ 50-100m   │ -12dB, muffled, delay noticeable    │
│ 100-200m  │ -18dB, mostly crack/thump           │
│ 200-400m  │ -24dB, distant rumble               │
│ 400m+     │ Very faint, directional hint only   │
└─────────────────────────────────────────────────┘
```

---

## 🔄 Reload Audio

### Reload Sound Design

**Philosophy:** Reload sounds must be:
1. **Distinctive** per weapon type
2. **Informative** about reload progress
3. **Satisfying** with clear feedback

### Reload Phases

```
STANDARD RELOAD (2-3 seconds):

Phase 1: Magazine Release (0.3s)
├── Button click
├── Magazine slide out
└── Magazine drop (if empty)

Phase 2: New Magazine (0.5s)
├── Magazine grab (fabric)
├── Magazine orient
└── Magazine insert (click)

Phase 3: Chamber (0.3s) - If needed
├── Bolt pull
├── Bolt release
└── Weapon ready

Phase 4: Ready (0.1s)
└── Subtle weapon settle
```

### Reload Audio by Weapon Type

```
Assault Rifle:
├── Mag release: Metallic click
├── Mag out: Sliding metal
├── Mag in: Solid click confirmation
├── Bolt: If chamber empty
└── Total: 2.5-3.0 seconds

Pistol:
├── Mag release: Small click
├── Mag drop: Light clatter
├── Mag slam: Quick insertion
├── Slide release: Sharp snap
└── Total: 1.5-2.0 seconds

Shotgun (Shell by shell):
├── Port open: Mechanical chunk
├── Shell insert: Per shell click
├── Chamber: Pump sound
└── Total: 4-6 seconds (full reload)

Sniper (Bolt Action):
├── Bolt up: Mechanical lift
├── Bolt back: Heavy slide
├── Mag/Round: Insert sound
├── Bolt forward/down: Locking sounds
└── Total: 3-4 seconds
```

---

## 💥 Combat Audio Feedback

### Bullet Impact Sounds

**On Enemy (Confirmation):**
```
┌─────────────────────────────────────────────────┐
│ Hit Type    │ Sound              │ Purpose      │
├─────────────────────────────────────────────────┤
│ Body        │ Wet thud           │ Confirm hit  │
│ Armor       │ Metallic clang     │ Reduced damage│
│ Helmet      │ Sharp ring         │ Headshot armor│
│ Headshot    │ Critical sound     │ High damage  │
│ Kill        │ Distinct chime     │ Enemy down   │
└─────────────────────────────────────────────────┘
```

**On Environment:**
```
┌─────────────────────────────────────────────────┐
│ Surface     │ Sound              │ Visual       │
├─────────────────────────────────────────────────┤
│ Concrete    │ Dry chip/dust      │ Dust puff    │
│ Metal       │ Ping + ricochet    │ Spark        │
│ Wood        │ Splintering crack  │ Splinters    │
│ Glass       │ Shatter            │ Glass break  │
│ Water       │ Splash             │ Water spout  │
│ Dirt        │ Soft thud          │ Dirt spray   │
└─────────────────────────────────────────────────┘
```

### Bullet Whiz/Crack (Near Misses)

```
When bullets pass near player:

Close Miss (within 2m):
├── Supersonic crack: Very loud
├── Directional: Clear left/right
├── Heart rate increase (audio)
└── Player flinch (visual)

Medium Miss (2-5m):
├── Softer whiz
├── Directional cue
└── Alerting effect

Far Miss (5-10m):
├── Distant snap
├── General direction
└── Awareness prompt
```

---

## 💊 Ability & Item Audio

### Ability Sound Design

**ASSAULT - Combat Stim:**
```
Activation: Injection hiss + heartbeat spike
Active: Pulsing bass undertone
Duration: Rhythmic pulse matching timer
Deactivation: Exhale + return to normal
```

**SUPPORT - Healing Drone:**
```
Deploy: Mechanical whir + propeller spin
Active: Gentle hum + healing chime
Healing: Soft positive tones per tick
Recall/Destroy: Drone shutdown sound
```

**RECON - UAV Scan:**
```
Activation: Beep + radar sweep sound
Scanning: Sonar ping (expanding circle)
Enemy Detected: Alert chime per enemy
Duration End: Power down beep
```

**TANK - Riot Shield:**
```
Deploy: Heavy metal clank
Bullets Hitting: Impact sounds (no damage)
Taking Damage: Shield stress sounds
Breaking: Shattering + vulnerability alert
```

**SPECIALIST - EMP Blast:**
```
Charging: Electrical buildup
Release: Massive electrical discharge
Effect: Static zap on affected targets
Recovery: Systems coming back online
```

### Grenade Audio

```
Frag Grenade:
├── Throw: Arm movement whoosh
├── Flight: Air whistle
├── Land: Bounce based on surface
├── Fuse: Hissing (0.5s warning)
└── Explosion: Massive boom + debris

Flashbang:
├── Flight: Same as frag
├── Detonation: Bright audio pop
├── Effect: Ringing tinnitus (affected)
└── Duration: 3-5 second ring fade

Smoke Grenade:
├── Deploy: Pop + hiss
├── Active: Continuous hissing
├── Ambience: Muffled sounds inside
└── Duration: Hiss fades as smoke clears
```

---

## 📍 Directional Audio System

### 3D Audio Implementation

**Spatial Audio Requirements:**
```
HRTF (Head-Related Transfer Function):
├── Enabled for: Footsteps, gunfire, abilities
├── 360° horizontal accuracy
├── Vertical distinction (above/below)
└── Distance-based filtering

Stereo Fallback (No headphones):
├── Left/Right panning
├── Volume for distance
├── Visual indicators supplement
```

### Audio Compass Accuracy

```
Directional Precision:
├── 0-30m: ±15° accuracy
├── 30-60m: ±30° accuracy
├── 60-100m: ±45° accuracy
└── 100m+: General direction only
```

### Vertical Audio Cues

```
Same Level:
└── Normal playback

Above (1+ floors):
├── Muffled
├── Creaking/footstep overhead feel
└── Reverb suggests height

Below (1+ floors):
├── More muffled
├── Bass-heavy
└── Rumbling quality
```

---

## 🎮 Player Feedback Audio

### Damage Indicators

```
Taking Damage:
├── Direction indicator: Whoosh from hit direction
├── Severity: Audio varies with damage amount
├── Low health: Heartbeat overlay
└── Critical: Urgent warning tone

Damage Sources:
├── Bullet: Sharp impact + direction
├── Explosion: Bass boom + tinnitus
├── Fire: Burning sound + pain
├── Poison/Gas: Coughing + labored breathing
```

### Status Effects Audio

```
Bleeding:
└── Dripping sound, heartbeat

Poisoned:
└── Nausea undertone, distorted audio

Stunned:
└── Ringing, muffled world audio

Low Stamina:
└── Heavy breathing

Overweight:
└── Labored steps, grunting
```

---

## 🔊 Audio Settings Options

### Player Customization

```
Audio Options Menu:
├── Master Volume: 0-100%
├── Music Volume: 0-100%
├── SFX Volume: 0-100%
├── Voice Volume: 0-100%
├── Footstep Volume: 50-150% (boost option)
├── Teammate Audio: On/Off
├── HRTF: On/Off
├── Visual Sound Indicators: On/Off
└── Voice Chat Volume: 0-100%
```

### Accessibility

```
Visual Sound Indicators:
├── Footstep direction markers
├── Gunfire direction + distance
├── Ability sound visualized
└── Important audio events shown

Subtitle Options:
├── Operator callouts shown
├── Environmental audio described
└── Combat events captioned
```

---

**[← Back to Soundscape](./Soundscape.md)** | **[Index](../README.md)** | **[Next: Voice Lines →](./VoiceLines.md)**
