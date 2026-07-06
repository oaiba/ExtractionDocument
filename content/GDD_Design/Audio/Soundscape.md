---
title: "Soundscape - Environmental Audio Design"
type: docs
---

##  Audio Design Philosophy

### Core Principles

**"Sound is the Second Eye"** - In extraction shooters, audio is a survival tool.

**Pillars:**
1. **Information First**: Every sound must provide gameplay information
2. **Realistic Propagation**: Audio must follow realistic physics
3. **Atmospheric Immersion**: Create distinctive atmosphere for each zone
4. **Mobile Consideration**: Support visual sound indicators

---

##  Ambient Soundscape By Zone

### Industrial Decay - "The Factory"

**Mood Keywords:** Oppressive, Mechanical, Echoing, Abandoned

**Layer Structure:**
```
┌────────────────────────────────────────────┐
│ Layer 4: EVENT SOUNDS (Dynamic)            │
│ └── Explosions, gunfire, player actions    │
├────────────────────────────────────────────┤
│ Layer 3: DETAIL SOUNDS (Contextual)        │
│ └── Dripping water, sparking wires         │
├────────────────────────────────────────────┤
│ Layer 2: ZONE AMBIENCE (Mid)               │
│ └── Metal groans, wind through holes       │
├────────────────────────────────────────────┤
│ Layer 1: BASE DRONE (Constant)             │
│ └── Generator hum, distant machinery       │
└────────────────────────────────────────────┘
```

**Specific Sounds:**

| Sound | Description | Volume | Loop |
|:------|:------------|:-------|:-----|
| Generator Hum | 50Hz low drone | -18dB | Yes |
| Metal Stress | Groaning steel | -24dB | Random |
| Dripping Water | Cave-like echoes | -30dB | Yes |
| Steam Vents | Periodic hiss | -20dB | Trigger |
| Distant Collapse | Rumbling debris | -28dB | Random |
| Wind Through Holes | Whistling | -26dB | Yes |
| Electrical Spark | Crackling | -22dB | Random |
| Radiation Click | Geiger counter | -20dB | Zone |

**Reverb Settings:**
```
Large Halls:
├── Pre-delay: 25ms
├── Decay Time: 2.5s
├── High Frequency Damping: 0.6
└── Wet/Dry Mix: 40%

Tight Corridors:
├── Pre-delay: 5ms
├── Decay Time: 0.8s
├── High Frequency Damping: 0.8
└── Wet/Dry Mix: 25%

Underground/Labs:
├── Pre-delay: 15ms
├── Decay Time: 1.8s
├── High Frequency Damping: 0.4 (bright)
└── Wet/Dry Mix: 35%
```

---

### Urban Ruins - "District 14"

**Mood Keywords:** Eerie, Abandoned Life, Nature Reclaiming, Echo

**Layer Structure:**
```
┌────────────────────────────────────────────┐
│ Layer 4: LIFE SIGNS (Random)               │
│ └── Distant dogs, car alarms              │
├────────────────────────────────────────────┤
│ Layer 3: NATURE RETURN (Contextual)        │
│ └── Birds, insects, rustling leaves       │
├────────────────────────────────────────────┤
│ Layer 2: URBAN DECAY (Mid)                 │
│ └── Creaking buildings, broken glass      │
├────────────────────────────────────────────┤
│ Layer 1: WIND & SILENCE (Constant)         │
│ └── Wind channels, dead air               │
└────────────────────────────────────────────┘
```

**Specific Sounds:**

| Sound | Description | Volume | Location |
|:------|:------------|:-------|:---------|
| Wind Channel | Between buildings | -20dB | Outdoor |
| Bird Calls | Crows, pigeons | -28dB | Outdoor |
| Creaking Structure | Wood, metal | -26dB | Indoor |
| Broken Glass Tinkle | Wind-blown shards | -30dB | Window areas |
| Distant Dog Bark | Feral pack | -32dB | Random |
| Paper Rustling | Scattered debris | -28dB | Indoor |
| Subway Rumble | Underground train | -15dB | Subway areas |
| Water Drip Echo | Flooded basements | -24dB | Underground |

**Weather Variations:**
```
Clear Day:
├── Bird activity: High
├── Wind: Light
└── Visibility sounds: Normal

Rain (If implemented):
├── Rain on surfaces: Loud (-10dB)
├── Puddle splashes: Prominent
├── Thunder: Random events
└── Masking effect: +20% (harder to hear footsteps)

Fog (If implemented):
├── Dampened high frequencies
├── Muffled distant sounds
└── Close sounds: Louder feel
```

---

### Wilderness - "The Mire"

**Mood Keywords:** Isolated, Organic, Threatening Nature, Deceptive

**Layer Structure:**
```
┌────────────────────────────────────────────┐
│ Layer 4: PREDATOR HINTS (Tension)          │
│ └── Unseen movement, branch snaps          │
├────────────────────────────────────────────┤
│ Layer 3: WILDLIFE (Dense)                  │
│ └── Insects, frogs, birds                  │
├────────────────────────────────────────────┤
│ Layer 2: VEGETATION (Wind-driven)          │
│ └── Rustling leaves, swaying grass         │
├────────────────────────────────────────────┤
│ Layer 1: WIND & WATER (Constant)           │
│ └── Wind through trees, distant stream     │
└────────────────────────────────────────────┘
```

**Specific Sounds:**

| Sound | Description | Volume | Condition |
|:------|:------------|:-------|:----------|
| Wind Through Trees | Constant rustle | -18dB | Always |
| Insect Chorus | Crickets, cicadas | -22dB | Always |
| Frog Croaks | Near water | -26dB | Swamp areas |
| Bird Calls | Various species | -24dB | Random |
| Branch Snap | Sudden, nearby | -20dB | Random/AI |
| Leaves Underfoot | Player-caused | -16dB | Movement |
| Water Stream | Flowing water | -20dB | River areas |
| Flies Buzzing | Near corpses | -24dB | Loot areas |

**Contamination Zone Sounds:**
```
Chemical Gas Zone:
├── Player Heartbeat: Audible, accelerating
├── Breathing: Labored, filtered (mask)
├── Tinnitus: High frequency ring
├── Muffled exterior: -20dB reduction
└── Geiger clicks: Increasing rate
```

---

##  Dynamic Audio States

### Tension System

**Combat States:**
```
┌─────────────────────────────────────────────┐
│ State      │ Trigger              │ Effect  │
├─────────────────────────────────────────────┤
│ PASSIVE    │ No threats nearby    │ 100% amb│
│ ALERT      │ Gunfire heard        │ 70% amb │
│ COMBAT     │ Player takes fire    │ 40% amb │
│ DANGER     │ Low health           │ 20% amb │
│ EXTRACTION │ Exit timer active    │ 50% amb │
└─────────────────────────────────────────────┘
```

**Transition Rules:**
- PASSIVE → ALERT: Fade over 0.5s
- ALERT → COMBAT: Immediate snap
- COMBAT → PASSIVE: 10 second delay, fade 2s
- Any → DANGER: Immediate + heartbeat layer

### Time-Based Variations

**Match Timeline Audio:**
```
0:00-5:00   │ Full ambience, peaceful start
5:00-10:00  │ Tension subtly increases (+5% bass)
10:00-12:00 │ Heightened alertness (faster ambient events)
12:00-15:00 │ Urgency layer (subtle pulse in mix)
Last 60s    │ Extraction urgency (low freq pulse)
```

---

##  Occlusion & Propagation

### Sound Occlusion Rules

**Material Attenuation:**
```
┌─────────────────────────────────────────────┐
│ Material          │Attenuation │ Freq Cut   │
├─────────────────────────────────────────────┤
│ Air (open)        │ -0dB/m     │ None       │
│ Glass             │ -8dB       │ -2kHz      │
│ Wood (thin)       │ -12dB      │ -3kHz      │
│ Drywall           │ -15dB      │ -4kHz      │
│ Concrete (thin)   │ -20dB      │ -6kHz      │
│ Concrete (thick)  │ -30dB      │ -8kHz      │
│ Metal             │ -25dB      │ -5kHz      │
└─────────────────────────────────────────────┘
```

**Distance Attenuation:**
```
Close (0-10m):    Full frequency, full volume
Near (10-30m):    -6dB, slight HF roll-off
Medium (30-60m):  -12dB, noticeable HF cut
Far (60-100m):    -18dB, mostly low-mid
Distant (100m+):  -24dB, bass-heavy
```

### Vertical Audio

**Floor Separation:**
```
Same Floor:      Normal propagation
1 Floor Apart:   -10dB, muffled
2+ Floors Apart: -20dB, very muffled

Stairwells: Reduced occlusion (sound travels)
Ventilation: Sound channels (connects rooms)
```

---

##  Audio Mix Priorities

### Priority Hierarchy

```
Priority 1 (CRITICAL - Never duck):
├── Enemy footsteps within 10m
├── Incoming fire (bullets passing)
├── Player damage indicators
└── Extraction timer beeps

Priority 2 (HIGH - Slight duck allowed):
├── All gunfire
├── Explosions
├── Ability sounds
└── Reload sounds

Priority 3 (MEDIUM - Ducks during combat):
├── Teammate audio
├── AI enemy callouts
├── Interactive object sounds
└── Loot pickup sounds

Priority 4 (LOW - Heavy duck):
├── Ambient soundscape
├── Music (if any)
├── Distant events
└── Environmental details
```

### Voice Channel Limits

```
Max Simultaneous Voices: 64

Allocation:
├── Player sounds: 8 reserved
├── Nearby combat: 16 reserved
├── Ambience: 12 reserved
├── UI/Feedback: 4 reserved
└── Dynamic pool: 24 shared
```

---

##  Special Audio Events

### Map Events

**Supply Drop:**
```
Sequence:
1. Distant plane engine (10s before) → -20dB, panning
2. Overhead pass (3s) → -8dB, doppler effect
3. Parachute deploy → Fabric flutter
4. Impact → Thud based on terrain
5. Beacon → Rhythmic ping for 30s
```

**Contamination Zone Expansion:**
```
Warning Phase (30s before):
├── Siren wail: Distant, ominous
├── Building to urgency
└── Radio static bursts

Active Phase:
├── Gas hiss: Constant
├── Toxic ambience layer
└── Heartbeat (player in zone)
```

**Extraction Vehicle:**
```
Helicopter:
├── Distant rotor (30s out): -28dB, growing
├── Approach (15s): -18dB, getting loud
├── Hover: -10dB, constant rotor wash
├── Departure: Doppler fade

Truck:
├── Engine start: Rumble
├── Idle: Low frequency vibration
├── Horn: Warning signal
├── Departure: Diesel acceleration
```

---

##  Technical Specifications

### Audio Format Standards

```
Ambient Loops:
├── Format: OGG Vorbis
├── Sample Rate: 44.1kHz
├── Bit Depth: 16-bit
├── Channels: Stereo
└── Loop: Seamless

Sound Effects:
├── Format: WAV
├── Sample Rate: 48kHz
├── Bit Depth: 24-bit (source), 16-bit (runtime)
├── Channels: Mono (3D), Stereo (UI)
└── Length: < 5 seconds

Voice Lines:
├── Format: OGG Vorbis
├── Sample Rate: 44.1kHz
├── Bit Depth: 16-bit
├── Channels: Mono
└── Compression: -4 quality
```

### Memory Budget

```
Total Audio Memory: < 150MB (mobile)

Allocation:
├── Weapon sounds: 30MB
├── Footsteps/Foley: 20MB
├── Ambience (streaming): 25MB
├── Voice lines: 40MB
├── UI sounds: 10MB
└── VFX sounds: 25MB
```



