# Audio Design

**[← Previous: User Interface](../Visuals/UserInterface.md)** | **[Index](../README.md)** | **[Next: Progression →](../GameDesign/Progression.md)**

---

## Audio Vision

**Sound Philosophy:** Tactical, immersive, informative

**Core Goals:**
1. **Situational Awareness** - Audio cues cho combat decisions
2. **Immersion** - Believable soundscape
3. **Clarity** - Clear feedback
4. **Performance** - Mobile-optimized

---

## Audio Pillars

### 1. Information Through Sound
**Why:** Players cần hear threats

**Implementation:**
- Distinct footstep materials
- Directional gunshots
- Reload audio cues
- Ability sound signatures

### 2. Dynamic Mix
**Why:** Prioritize important sounds

**Implementation:**
- Combat sounds louder
- Ambient ducks during action
- 3D audio positioning
- Distance-based attenuation

### 3. Tactical Authenticity
**Why:** Realistic military feel

**Implementation:**
- Real weapon recordings
- Military radio chatter
- Authentic gear sounds
- Environmental realism

### 4. Mobile Optimization
**Why:** Battery và memory constraints

**Implementation:**
- Compressed audio formats
- Streaming vs loaded
- Max channel limits
- Voice chat integration

---

## Combat Audio

### Weapon Sounds

**Design Principles:**
- Each weapon type sounds distinct
- Distance affects sound (near vs far)
- Environment affects sound (indoor echo)
- Suppressed variants available

---

#### Assault Rifles
**Sound Character:** Powerful, rapid, military

**Layers:**
- Mechanical (bolt, action): Metallic click
- Gunshot: Sharp crack, mid-low frequency
- Tail: Outdoor reverb, echo
- Casings: Brass hitting ground

**Reference:** AK-47, M4A1 sounds

**Variants:**
- Single shot vs full-auto
- Suppressed version (muffled)

---

#### SMGs
**Sound Character:** Fast, lighter, compact

**Layers:**
- Mechanical: Quick, tight action
- Gunshot: Higher pitch than ARs
- Tail: Shorter decay
- Fire rate: 900-1100 RPM audio

**Reference:** MP5, UMP sounds

---

#### Shotguns
**Sound Character:** Heavy, impactful, intimidating

**Layers:**
- Pump action: Distinctive rack
- Gunshot: Deep boom, bass-heavy
- Tail: Long rumble
- Shell eject: Heavy casing drop

**Reference:** Remington 870, SPAS-12

---

#### Sniper Rifles
**Sound Character:** Long-range crack, powerful

**Layers:**
- Bolt action: Mechanical precision
- Gunshot: Sharp supersonic crack
- Tail: Very long echo (outdoor)
- Suppressed: Deep thump

**Reference:** AWP, Barrett sounds

---

#### Pistols
**Sound Character:** Compact, sharp, quick

**Layers:**
- Slide action: Metallic snap
- Gunshot: Sharp pop
- Tail: Short
- Suppressed: Quiet pfft

---

#### Melee Weapons
**Sound Character:** Swish, impact, brutal

**Sounds:**
- Swing: Whoosh through air
- Hit flesh: Thud, squelch
- Hit armor: Clang, metal
- Miss: Air swish

---

### Impact Sounds

**Material-Based:**

**Metal:**
- Ricochet: Pang, whine
- Penetration: Clang, crunch
- Sparks audio sync

**Concrete:**
- Impact: Crack, chip
- Dust puff sync
- Debris scatter

**Wood:**
- Splinter: Crack
- Thud: Deeper
- Break: Cracking

**Flesh (Minimal):**
- Impact: Muted thud
- No gore sounds (rating)

---

### Explosion Sounds

**Grenade:**
- Fuse: Ticking (if cooked)
- Explosion: Boom với bass
- Debris: Scatter, rain down
- Shockwave: Low-frequency rumble

**Supply Drop:**
- Plane flyover: Distant to close
- Parachute deploy: Fabric whoosh
- Container impact: Heavy thud
- Smoke hiss

---

### Ability Sounds

**Combat Stim (Assault):**
- Activation: Injector hiss
- Active loop: Heartbeat increase
- Enhanced movement: Faster footsteps
- Deactivation: Exhale, heartbeat slows

**Healing Drone (Support):**
- Deploy: Mechanical unfold
- Flight: Propeller hum (soft)
- Healing: Medical beep, energy hum
- Recall: Fold up, power down

**UAV Scan (Recon):**
- Activation: Sonar ping
- Scan pulse: Electronic beep wave
- Enemy detected: Alert beep
- Complete: Power down chirp

**Riot Shield (Tank):**
- Deploy: Heavy metal unfold
- Active: None (silent readiness)
- Impact hits: Loud metal clangs
- Stow: Fold, lock sound

**EMP Blast (Specialist):**
- Charge: Electric whine up
- Blast: Electronic discharge burst
- Effect hit: Static crackle
- Disable: Tech shutdown sounds

---

## Environmental Audio

### Footsteps

**Critical for gameplay** - Enemy detection

**Surface Types:**
- Concrete: Hard clack
- Metal grating: Hollow clang
- Wood: Creak
- Gravel: Crunch
- Grass: Soft rustle
- Water: Splash

**Movement Variations:**
- Walk: Normal volume
- Sprint: Louder, faster
- Crouch: Quieter, slower
- Jump/Land: Thud

**Distance Attenuation:**
- 0-10m: Full volume
- 10-30m: Reduced
- 30m+: Faint
- Indoor: Echo amplification

---

### Doors & Interactions

**Doors:**
- Open: Creak, squeak
- Close: Slam, latch
- Locked: Rattle, reject

**Containers:**
- Open crate: Wood creak, lid lift
- Open locker: Metal screech
- Open safe: Lock clicks, heavy swing
- Close: Reverse sounds

**Switches:**
- Flip: Click
- Press button: Mechanical press
- Hack terminal: Keyboard clacks

---

### Ambient Soundscapes

**Industrial Zone:**
- Distant machinery creaks
- Wind through metal
- Dripping water
- Electrical buzzing
- Occasional metal stress groans

**Urban Ruins:**
- Wind whistling
- Distant thunder (weather)
- Debris settling
- Birds (sparse)
- Water dripping

**Forest Perimeter:**
- Leaves rustling
- Bird calls (tense, sparse)
- Branch creaks
- Wildlife movimento (rare)

**Contamination Zone:**
- Ominous low drone
- Geiger counter crackle
- Wind with particle hiss
- Danger musical sting

---

### Dynamic Weather

**Rain:**
- Rainfall loop: Patter intensity varies
- Puddle impacts: Splash
- Thunder: Distant rumble
- Indoor: Muffled rain on roof

**Sandstorm:**
- Wind: Howling, intense
- Sand particles: Hissing rush
- Visibility reduction cue: Muffled audio
- Objects hitting: Clatter

---

## UI Audio

### Menu Sounds

**Navigation:**
- Hover: Soft click
- Select: Confirm beep
- Back: Negative beep
- Error: Buzz

**Inventory:**
- Pick up item: Mechanical grab
- Drop item: Item-specific thud
- Drag: Subtle scrape
- Equip weapon: Lock-in click

**Loadout:**
- Attach mod: Mechanical snap
- Remove mod: Release click
- Weapon select: Metal clink

---

### HUD Sounds

**Notifications:**
- Quest update: Positive chime
- Kill: Satisfying ding
- Death: Low, negative tone
- Level up: Victory fanfare

**Warnings:**
- Low health: Heartbeat warning
- Low ammo: Subtle alert beep
- Contamination: Urgent alarm
- Extraction ready: Positive alert

**Extraction:**
- Call extraction: Radio confirmation
- Countdown: Beep per second (final 10 sec)
- Success: Helicopter swell, victory
- Interrupted: Alarm, negative

---

### Match Flow Audio

**Pre-Match:**
- Loadout music: Tense, preparing
- Matchmaking: Ambient, waiting
- Loading: Minimal, anticipation build

**Match Start:**
- Deploy: Dramatic sting
- Protection timer: Countdown beeps
- Go signal: Release tone

**In-Match:**
- Supply drop warning: Alarm, announcement
- Contamination warning: Siren, dramatic music
- Time warnings: Tense music increases

**Post-Match:**
- Victory: Triumphant theme
- Defeat: Somber, reflective
- Loot reveal: Item rarity sounds

---

## Voice Lines

### Operator Callouts

**Combat:**
- "Enemy spotted!" (directional)
- "Taking fire!"
- "Reloading!"
- "Grenade!"
- "Man down!"

**Tactical:**
- "Moving up"
- "In position"
- "Covering you"
- "Fall back"

**Loot:**
- "Found something" (rare item)
- "Could use this"
- "Grabbing supplies"

**Extraction:**
- "Calling extraction"
- "Extraction point clear"
- "Get to the LZ!"
- "We're leaving!"

**Abilities:**
- Each operator: Unique ability callout
- "Combat stim active!"
- "Deploying drone!"
- "UAV online!"
- "Shield up!"
- "EMP out!"

---

### Radio Chatter (AI/System)

**Operator Selection:**
- Brief character introduction
- Voice actor per operator

**Match Start:**
- "Operators deploying"
- "Good hunting"

**Events:**
- "Supply drop inbound"
- "Warning: Contamination detected"
- "Extraction available"

**Match End:**
- "Mission complete"
- "Operator KIA"

---

### Voice Acting Direction

**Assault:** Confident, aggressive, military
**Support:** Calm, professional, caring
**Recon:** Quiet, calculated, precise
**Tank:** Deep, imposing, protective
**Specialist:** Quick, clever, technical

**Languages:**
- English (primary)
- Future: Localization (Vietnamese, Chinese, etc.)

---

## Music & Soundtrack

### Music Style
**Genre:** Electronic/Orchestral hybrid  
**Mood:** Tense, tactical, heroic moments  
**Inspiration:** Hans Zimmer (tactical scores), Daft Punk (electronic)

---

### Menu Music

**Main Menu:**
- Ambient, atmospheric
- Low intensity
- Loopable
- 2-3 minute loop

**Loadout Screen:**
- Tension building
- Preparation mood
- Slightly faster tempo

---

### In-Game Music

**Dynamic System:**

**Low Intensity (No Combat):**
- Ambient pads
- Subtle percussion
- Exploration mood
- 60-80 BPM

**Medium Intensity (Combat Nearby):**
- Drums enter
- Rise in energy
- Tactical feel
- 100-120 BPM

**High Intensity (Active Combat):**
- Full orchestra/electronic
- Driving rhythm
- Adrenaline pumping
- 130-150 BPM

**Extraction:**
- Climactic swell
- Heroic theme
- Final push energy
- 140+ BPM

---

### Stinger/Cues

**Event Stingers:**
- Kill: Short, satisfying (0.5 sec)
- Death: Dramatic low (1 sec)
- Level up: Victory chord (1 sec)
- Quest complete: Positive resolve (2 sec)
- Rare loot: Magical shimmer (1 sec)

---

## Audio Technical Specifications

### File Formats

**Mobile:**
- Music: Streamed Vorbis (.ogg), 128 kbps
- SFX: Loaded Vorbis (.ogg), 96 kbps
- Voice: Vorbis (.ogg), 64 kbps
- UI: WAV (uncompressed, small files)

**Sample Rate:**
- 44.1 kHz (standard)
- 22 kHz for lo-fi effects (optimization)

---

### Channel Limits

**Simultaneous Audio:**
- Low-end device: 16 channels
- Mid-range: 32 channels
- High-end: 64 channels

**Priority System:**
1. Player weapon/ability sounds
2. Nearby enemy sounds
3. Impact sounds
4. Ambient sounds
5. Music

---

### 3D Audio (Spatial)

**Implementation:**
- Unreal Audio Engine
- HRTF for headphones
- Stereo speaker optimization

**Distance Attenuation:**
- Linear falloff: 0-50m
- Logarithmic: 50m+
- Max distance: 100m (most sounds)
- Gunshots: 300m+ (danger awareness)

**Occlusion:**
- Wall muffling
- Indoor/outdoor transitions
- Material-based filtering

---

### Memory Budget

**Total Audio Memory:**
- Target: < 150 MB
- Music (streaming): 30 MB buffer
- SFX (loaded): 80 MB
- Voice (loaded): 30 MB
- Reserve: 10 MB

**Optimization:**
- Adaptive quality based on device
- Unload distant sounds
- Sound pooling (reuse instances)

---

## Audio Implementation (UE5)

### Sound Cues

**Weapon Fire:**
```
SoundCue_AR_Fire
├─ Random (variations)
│  ├─ AR_Fire_01.wav
│  ├─ AR_Fire_02.wav
│  └─ AR_Fire_03.wav
├─ Attenuation (distance falloff)
├─ Reverb Send (environment)
└─ Concurrency Limit (max 8)
```

### Sound Classes

**Hierarchy:**
```
Master
├─ Music (ducking target)
├─ SFX
│  ├─ Weapons
│  ├─ Footsteps
│  ├─ Abilities
│  └─ Ambient
├─ Voice
│  ├─ Player
│  └─ AI
└─ UI
```

---

### Audio Mixers

**Combat Mix:**
- Weapon sounds: +3 dB
- Ambient: -6 dB
- Music: -3 dB

**Menu Mix:**
- UI: 0 dB
- Music: -2 dB
- SFX previews: -4 dB

---

## Audio Asset List

### Priority Assets (MVP)

**Weapons:** (5 types x 3 variations = 15 sounds)
- Assault Rifle fire
- SMG fire
- Shotgun fire
- Sniper fire
- Pistol fire

**Movement:** (6 surfaces x 3 speeds = 18 sounds)
- Footsteps all surfaces

**UI:** (~20 sounds)
- Menu navigation
- Item pickup
- Notifications

**Abilities:** (5 operators x 3 sounds each = 15 sounds)
- Activation, loop, deactivation

**Ambient:** (3 zones x 5 layers = 15 loops)
- Environmental soundscapes

**Music:** (4 tracks)
- Menu, Low, Medium, High intensity

**Total MVP:** ~100 audio assets

---

### Post-Launch Expansion

- Additional weapon sounds
- Weather variations
- More voice lines
- Seasonal music
- Event-specific audio
- Cosmetic audio (kill effects, emotes)

---

## Audio Middleware

**Tool:** Unreal Audio Engine (built-in)

**Alternative (Future):** Wwise or FMOD
- Better mobile optimization
- Advanced mixing
- More designer control

---

## Accessibility Options

**Audio Settings:**
- Master volume
- Music volume
- SFX volume
- Voice volume
- Mono audio option (hearing impaired)
- Visual sound indicators (gunshot directions)

---

## Audio Testing Checklist

**Per Sound:**
- [ ] Correct file format
- [ ] Proper sample rate
- [ ] Normalized volume
- [ ] No clipping
- [ ] Loopable (if loop)
- [ ] No pops/clicks at start/end

**In-Game:**
- [ ] 3D positioning correct
- [ ] Distance falloff appropriate
- [ ] Occlusion working
- [ ] Priority system functioning
- [ ] No audio crashes
- [ ] Performance within budget

---

**[← Previous: Art Direction](./05_ArtDirection.md)** | **[High-Level Index](./README.md)** | **[Next: User Interface →](./07_UserInterface.md)**
