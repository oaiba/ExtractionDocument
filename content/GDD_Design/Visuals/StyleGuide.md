---
title: "Style Guide - Art Bible"
type: docs
weight: 2
---

## Visual Identity Overview

### Style Definition

**Primary Style: Cyberpunk Neo-Industrial**

```
REALISTIC ──────────────────●──→ STYLIZED
                            ▲
                       Game Position
                  (40% Realistic, 60% Stylized)
```

**Characteristics:**
- Stylized character proportions with realistic PBR materials and lighting
- Post-collapse industrial decay layered with cyberpunk technology remnants
- Bold color accents (orange, cyan) against desaturated environments
- Exaggerated silhouettes for top-down readability
- Tech elements glow — neon signs, holographic displays, LED strips

**Style Comparison:**

| Element | Realistic Side | Stylized Side |
| :------ | :------------- | :------------ |
| Materials | PBR metal/roughness, genuine wear patterns | Slightly exaggerated contrast, cleaner spec |
| Lighting | Motivated sources, realistic falloff | Stronger rim lights, bolder color tints |
| Characters | Authentic gear silhouettes, real proportions as base | 1:6.5 head ratio, 10-15% exaggerated gear |
| Environments | Industrial architecture, real-world reference | Neon density beyond realistic, stylized decay |
| VFX | Physical particle behavior | Brighter, more saturated, longer trails |

---

## Visual Pillars

### Pillar 1: Neon Decay

**Concept:** A collapsing world where advanced technology persists in fragments. The contrast between ruin and tech is the game's visual signature.

**Past vs. Present:**

| Before Collapse | After Collapse |
| :-------------- | :------------- |
| Corporate logos, clean glass towers | Faded signage, cracked facades, vine overgrowth |
| Holographic billboards advertising products | Glitched loops, fragmented images, static |
| Automated transit, smart infrastructure | Rusted rails, dead drones, jury-rigged power |
| Climate-controlled interiors | Water damage, mold, emergency lighting only |

**Visual Rule:** Every exterior scene requires at least **one warm neon source** (orange/amber) and **one cool neon source** (cyan/teal) to maintain cyberpunk identity.

<!-- REF_IMAGE: Neon Decay before-and-after comparison — showing a corporate district in its prime vs. post-collapse with overgrown tech and flickering neon -->

### Pillar 2: Tactical Clarity

**Concept:** Gameplay readability is non-negotiable. From the top-down camera, every element must be instantly identifiable.

**Visual Hierarchy Rules:**
```
Layer 1:  PLAYER CHARACTER  — Brightest element, orange/cyan rim light, sharpest detail
Layer 2:  HOSTILE TARGETS   — High contrast, red indicators, distinct from environment
Layer 3:  INTERACTIVE LOOT  — Rarity-coded glow, subtle emissive outline
Layer 4:  COVER OBJECTS     — Neutral tones, clear geometric shapes, no visual noise
Layer 5:  ENVIRONMENT BG    — Desaturated, atmospheric fog, reduced detail at distance
```

**Readability Zones (from camera):**

| Distance | Detail Level | Effect |
| :------- | :----------- | :----- |
| 0-50 units | Full detail, all effects, max particles | Player immediate area |
| 50-100 units | High detail, reduced particles | Engagement range |
| 100-200 units | Medium detail, billboard vegetation | Awareness range |
| 200+ units | Low detail, fog, simplified shapes | Atmospheric backdrop |

### Pillar 3: Stylized Grit

**Concept:** Everything looks functional and worn, but with stylized proportions that make designs memorable and iconic. No fantasy magic — all technology, all grounded.

**Not This:** Fantasy armor, magical runes, anime proportions  
**But This:** Tactical gear with personality, cybernetic enhancements, custom modifications

**Material Focus:**
- Kevlar, ballistic nylon, carbon fiber composites
- Weathered metal with cyberpunk LED accents
- Medical-grade fabrics with holographic diagnostic patches
- Industrial rubber, tool leather, polymer plates
- Tech surfaces: matte black with orange/cyan indicator lights

---

## Master Color Palette

### Brand Core (4 Colors)

These four colors define the game's entire visual identity. All other colors derive from or complement this foundation.

```
┌──────────────────────────────────────────────────────┐
│  BRAND PALETTE                                       │
├──────────────────────────────────────────────────────┤
│  Signal Orange   │ #F97316 │ Primary accent, warmth  │
│  Bone White      │ #F8FAFC │ Clean surfaces, text    │
│  Void Black      │ #0A0A0B │ Foundations, shadows    │
│  Tactical Cyan   │ #06B6D4 │ Tech, cool accent       │
└──────────────────────────────────────────────────────┘
```

<!-- REF_IMAGE: Brand palette reference card — showing all 4 colors as large swatches with full hex values, RGB, and HSL breakdowns -->

### Gameplay Colors

```
┌──────────────────────────────────────────────────────┐
│  GAMEPLAY MARKERS                                    │
├──────────────────────────────────────────────────────┤
│  Friendly Blue    │ #3B82F6 │ Teammate markers       │
│  Enemy Red        │ #EF4444 │ Hostile indicators      │
│  Neutral Amber    │ #F59E0B │ AI, unaffiliated NPCs   │
│  Objective Green  │ #22C55E │ Extraction, quest goals │
│  Warning Orange   │ #F97316 │ Caution states          │
│  Critical Red     │ #DC2626 │ Danger, low health      │
└──────────────────────────────────────────────────────┘
```

### Environmental Base Colors

```
┌──────────────────────────────────────────────────────┐
│  INDUSTRIAL                                          │
├──────────────────────────────────────────────────────┤
│  Concrete Gray    │ #6B7280 │ Walls, floors, pipes   │
│  Rust Bloom       │ #D97706 │ Metal decay, age       │
│  Safety Amber     │ #FBBF24 │ Warning signage        │
│  Deep Shadow      │ #1E293B │ Dark interiors         │
└──────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────┐
│  URBAN                                               │
├──────────────────────────────────────────────────────┤
│  Brick Tone       │ #92400E │ Building facades       │
│  Faded Surface    │ #94A3B8 │ Weathered paint        │
│  Asphalt Dark     │ #374151 │ Roads, parking lots    │
│  Overgrowth       │ #166534 │ Nature reclaiming      │
└──────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────┐
│  NATURE / OUTSKIRTS                                  │
├──────────────────────────────────────────────────────┤
│  Forest Canopy    │ #65A30D │ Trees, dense foliage   │
│  Grass Field      │ #84CC16 │ Open ground cover      │
│  Earth Base       │ #78350F │ Dirt paths, hillsides  │
│  Overcast Sky     │ #64748B │ Default atmosphere     │
└──────────────────────────────────────────────────────┘
```

### Faction Color Schemes

| Faction | Primary | Secondary | Neon Accent | Use |
| :------ | :------ | :-------- | :---------- | :-- |
| Salvage Corps | Orange #D97706 | Gray #6B7280 | Amber #FBBF24 | Warm, industrial worker |
| Tech Syndicate | Cyan #06B6D4 | Black #111827 | White #F9FAFB | Cold, digital precision |
| Underground Network | Purple #7C3AED | Gold #EAB308 | Magenta #EC4899 | Mysterious, luxurious |
| Peacekeepers | Blue #2563EB | White #F9FAFB | Red #DC2626 | Military authority |

### Item Rarity Colors

```
COMMON      │ #9CA3AF │ Steel Gray  │ No glow
UNCOMMON    │ #22C55E │ Lime Green  │ Subtle pulse (0.5s)
RARE        │ #3B82F6 │ Cobalt Blue │ Soft glow + hum
EPIC        │ #A855F7 │ Neon Purple │ Medium glow + wisps
LEGENDARY   │ #EAB308 │ Molten Gold │ Strong glow + trail + audio
```

---

## Lighting Design

### Lighting Philosophy

**Goals:**
1. Enhance readability from top-down camera
2. Create atmosphere through neon-lit decay
3. Guide player attention with motivated light sources
4. Differentiate zones through color temperature and neon density

**Cyberpunk Lighting Rules:**
- Every indoor area has at least one **emissive tech light source** (terminal glow, LED strip, holographic display)
- Outdoor areas use **neon signage** and **flickering holographic billboards** as accent lights
- Shadows are deep and sharp — the contrast between lit and unlit areas is dramatic
- Rim lighting on characters is **always active** for gameplay readability

### Outdoor Lighting Presets

**Primary: Overcast Day (Default)**
```
Sun Direction:    45 degree angle (soft directional shadows)
Sun Color:        Warm white #FFF7ED
Intensity:        2.0 lux
Sky Color:        Gray-blue overcast #94A3B8
Ambient Fill:     Cool blue #E0E7FF
Shadow Softness:  0.7
Neon Visibility:  Medium (visible but not dominant)
Mood:             Industrial tension, somber but functional
```

**Secondary: Neon Night (Events / High-Tier Zones)**
```
Sun Direction:    None (night sky)
Moon Color:       Cool blue-white #DBEAFE
Intensity:        0.3 lux
Sky Color:        Deep navy #0F172A
Primary Light:    Neon signs (orange #F97316, cyan #06B6D4)
Secondary Light:  Holographic ads, vehicle lights, burning barrels
Shadow Contrast:  Very high
Neon Visibility:  Maximum (primary light source)
Mood:             Cyberpunk showcase, dangerous, visually rich
```

**Tertiary: Golden Hour (Transitional)**
```
Sun Direction:    Low angle (15 degrees)
Sun Color:        Deep orange #F97316
Intensity:        1.5 lux
Sky Color:        Gradient orange to purple
Shadow Color:     Deep blue #1E3A8A
Shadow Length:    Long, dramatic
Neon Visibility:  High (warm ambient complements neon)
Mood:             Beautiful danger, tension before darkness
```

<!-- REF_IMAGE: Lighting preset comparison — showing the same environment under Overcast Day, Neon Night, and Golden Hour conditions -->

### Indoor Lighting Presets

**Industrial Interior:**
```
Primary:      Overhead fluorescent (flickering, some broken)
Color:        Cool white #F0F9FF with slight green tint
Fill:         Window light (motivated, directional)
Tech Accent:  Orange LED strips along machinery, amber warning panels
Shadow:       High contrast, deep pools of darkness
Mood:         Abandoned factory, industrial unease
```

**Corporate / Office Interior:**
```
Primary:      Soft overhead panels (some still powered)
Color:        Neutral white #FAFAFA
Fill:         Computer screen glow (cyan #06B6D4)
Tech Accent:  Holographic presentation screens (glitched), emergency exit signs
Shadow:       Soft, diffused
Mood:         Corporate ghost town, eerie quiet
```

**Underground / Lab Interior:**
```
Primary:      Emergency lighting only
Color:        Red #DC2626 or Cyan #06B6D4 (alternating zones)
Fill:         Equipment indicator lights, bio-containment glow
Tech Accent:  Server rack LEDs, holographic warning projections
Shadow:       Extreme contrast, near-total darkness between sources
Mood:         High danger, sci-fi horror, hidden secrets
```

### Zone Lighting Summary

| Zone | Color Temp | Key Light | Neon Density | Mood |
| :--- | :--------- | :-------- | :----------- | :--- |
| Edge / Forest | 5500K | Overcast daylight | Sparse (abandoned tech) | Natural, cautious |
| Mid / Urban | 4500K | Mixed natural + neon | Medium (signs, screens) | Transitional tension |
| Hot / Industrial | 4000K | Harsh spots + neon | High (LED strips, warnings) | Industrial danger |
| Core / Labs | 6500K+ | Colored emergency | Maximum (full cyberpunk) | Extreme danger |

---

## Environment Style Guide

### Industrial Zone

**Key Visual Elements:**
- Massive smokestacks (landmark silhouettes)
- Rusted catwalks and gantry networks
- Conveyor systems (non-functional, some jammed mid-cycle)
- Chemical storage tanks with faded warning labels
- Graffiti — survivor messages and faction territory tags
- Nature reclaiming: vines through grating, moss on pipes

**Cyberpunk Layer:**
- Malfunctioning LED strip lights along rooflines
- Holographic "DANGER" and "NEXUS CORP" signs still projecting
- Automated systems running empty cycles (robotic arms, conveyors)
- Data cables bundled and hanging from overhead structures

**Material Breakdown:**
```
60% — Corrugated metal (rusted, dented, paint remnants)
20% — Concrete (cracked, stained, rebar exposed)
10% — Tech panels (broken screens, LED indicators)
10% — Organic intrusion (plants, mold, water damage)
```

<!-- REF_IMAGE: Industrial zone concept art — showing rusted infrastructure with orange neon warning signs and cyan data cable bundles -->

### Urban Zone

**Key Visual Elements:**
- High-rise buildings in varied damage states (intact to collapsed)
- Street-level storefronts (shattered glass, looted interiors)
- Abandoned vehicles (some with operational hazard lights)
- Billboard frames — many still displaying glitched holographic ads
- Public art installations (damaged, repurposed as cover)
- Makeshift barricades from debris and furniture

**Cyberpunk Layer:**
- Neon signs at storefronts (some lit, most flickering or broken)
- Vending machines with glowing screens (functional — sell consumables)
- Holographic crosswalk signals still cycling
- Data cable bundles running wall-to-wall between buildings

**Material Breakdown:**
```
40% — Concrete and brick (varied weathering)
25% — Glass (broken, boarded, some intact with reflections)
20% — Tech surfaces (screens, signs, vending machines)
15% — Nature overgrowth and water damage
```

### Military Zone

**Key Visual Elements:**
- Reinforced bunkers, blast walls, sandbag positions
- Watchtowers with mounted searchlights
- Razor wire perimeters, jersey barriers
- Vehicle wrecks (APCs, trucks) in varied destruction states
- Camouflage netting stretched over key positions

**Cyberpunk Layer:**
- Automated turret emplacements (some still active)
- Holographic perimeter warning projections
- EMP shielding panels on key structures
- Surveillance camera networks (blinking red LEDs)
- Digital camo patterns on surfaces — pixelated, tech-derived

**Material Breakdown:**
```
50% — Reinforced concrete (blast-resistant texture)
25% — Olive drab / gray metal (military standard)
15% — Sandbags, earthworks, natural cover
10% — High-tech panels, sensor arrays, antenna clusters
```

### Nature / Outskirts Zone

**Key Visual Elements:**
- Dense tree canopy filtering light
- Overgrown roads and paths
- Abandoned vehicles slowly being consumed by vegetation
- Old fence lines, collapsed utility poles
- Wildlife traces (nests, burrows — environmental storytelling)

**Cyberpunk Layer (Minimal):**
- Occasional abandoned tech: dead drones tangled in branches, solar panel arrays covered in moss
- Old data relay stations, antenna towers (rusted, non-functional)
- Faded road signs with QR codes and digital displays (dark)
- The absence of technology IS the design — nature has won here

**Material Breakdown:**
```
50% — Organic (trees, grass, undergrowth, flowers)
25% — Earth (dirt, rocks, mud, creek beds)
15% — Deteriorated infrastructure (asphalt, concrete, rebar)
10% — Abandoned tech (rusted metal, dead screens)
```

<!-- REF_IMAGE: Zone comparison grid — showing Industrial, Urban, Military, and Nature zones side-by-side at the same time of day -->

---

## Character Style Guide

### Operator Visual Identity

**Body Proportions:**
```
Style:       Semi-realistic heroic hybrid
Head Ratio:  1:6.5 body heights (slightly larger for readability)
Shoulders:   2.0 head widths (men), 1.8 head widths (women)
Hands:       110% realistic scale (weapon grip must read from top-down)
Gear:        10-15% exaggerated for silhouette definition
```

**Gear Layering System:**
```
Layer 1:  Base clothing   — Undersuit, tactical shirt, pants
Layer 2:  Primary armor   — Vest, chest plate, shoulder guards
Layer 3:  Pouches/Gear    — Ammo, medical, utility pouches
Layer 4:  Head/Accessories — Helmet, goggles, comms equipment
Layer 5:  Backpack        — If equipped, visible from top-down
Layer 6:  Cyberpunk Tech  — Wrist displays, HUD visors, LED accents
```

### Class Visual Distinction

| Class | Build | Key Visual | Cyberpunk Element | Color Accent |
| :---- | :---- | :--------- | :---------------- | :----------- |
| Assault | Athletic | Cross-chest ammo belt, medium helmet | Wrist ammo counter | Orange #F97316 |
| Support | Medium | Medical backpack, red cross armband | Forearm diagnostic hologram | Cyan #06B6D4 |
| Recon | Slim | Tech goggles, compact profile | Active camo shimmer panels | Cyan #06B6D4 |
| Tank | Heavy | Shield plates, riot visor, thick armor | Power-assist frame glow | Red #DC2626 |
| Specialist | Medium | Tool belt, utility pouches, asymmetric | Wrist hacking device | Amber #F59E0B |

**Skin Tone and Diversity:**
- Operators represent diverse ethnicities and body types
- Base character models support 5+ skin tone maps
- Cosmetic customization includes face paint, tattoos, scars
- All cosmetics are non-gameplay-affecting

<!-- REF_IMAGE: Character class lineup — showing all 5 operator classes in front view and top-down view with cyberpunk details highlighted -->

---

## Weapon Style Guide

### Weapon Visual Philosophy

**Principles:**
1. Base designs grounded in real-world firearms (recognizable platforms)
2. Cyberpunk modifications: digital sights, LED indicators, polymer composites
3. Visible wear that tells a story (scratches, tape repairs, custom engravings)
4. Attachment modularity clearly visible (rails, mounting points)
5. Dark base color (black/dark gray), accents in brand colors

**Wear Levels:**
```
Factory New    — Clean polymer, sharp edges, full emissive indicators
Field-Tested   — Minor scratches, slight wear on grip, emissive steady
Well-Worn      — Visible use marks, tape wraps on stock, dim emissive
Battle-Scarred — Heavy scratches, rust on metal parts, intermittent glow
Veteran        — Heavy wear + custom engravings + unique emissive pattern
```

### Attachment Visual Rules

| Attachment | Mounting Point | Silhouette Change | Cyberpunk Detail |
| :--------- | :------------- | :---------------- | :--------------- |
| Optic / Scope | Top rail | Profile height increase | Holographic reticle visible |
| Suppressor | Barrel end | +30% barrel length | Heat signature dampener ring |
| Foregrip | Under-rail | Underbarrel width increase | Ergonomic polymer, LED grip indicator |
| Magazine | Body fixed position | Size varies with capacity | Digital round counter on extended mags |
| Laser | Side rail | Minimal | Visible beam (red/green/IR toggle) |
| Stock | Rear mount | Length change (folded/extended) | Recoil dampener pad |

---

## Composition Guidelines

### Top-Down Framing

**Screen Layout:**
```
┌─────────────────────────────────────────┐
│          SAFE ZONE (UI overlay)         │  HUD, status bars, minimap
├─────────────────────────────────────────┤
│                                         │
│      FOCUS AREA (Player + Combat)       │  High detail, effects,
│           ●── player ──●               │  max readability
│                                         │
├─────────────────────────────────────────┤
│          SAFE ZONE (Controls/Info)      │  Mobile: touch controls
└─────────────────────────────────────────┘  PC/Console: empty or mini-UI
```

**Visual Weight Distribution:**
- **Center:** Player — highest contrast, sharpest rim light
- **Near field (50 units):** Immediate threats and loot — high contrast, effects active
- **Mid field (100 units):** Environment detail — medium contrast, reduced particles
- **Far field (200+ units):** Atmospheric backdrop — low contrast, fog, simplified geometry

### Color Temperature Gradient

From player outward, the image should transition:
```
Warm (player area, neon orange)  →  Neutral (mid-range)  →  Cool (distance, blue-gray fog)
```

This creates natural depth and focuses attention on the gameplay center.

---

## Mood Board References

### Game References

| Game | Reference Point |
| :--- | :-------------- |
| Cyberpunk 2077 | Neon urbanism, tech integration, environmental decay |
| Overwatch 2 | Stylized proportions, clean readability, character identity |
| The Division 2 | Urban ruins, tactical gear authenticity, cover objects |
| Apex Legends | Bold character design, vibrant color coding |
| Gears Tactics | Top-down combat clarity, environmental detail |
| Valorant | Clean visual design, readability-first |
| Ruiner | Top-down cyberpunk aesthetic, neon color grading |
| Transistor | Stylized sci-fi environment art, atmospheric lighting |

### Film and Media References

| Source | What to Study |
| :----- | :------------ |
| Blade Runner 2049 | Orange-cyan color grading, atmospheric lighting, decay |
| Ghost in the Shell | Cybernetic augmentation, holographic tech integration |
| Altered Carbon | Future noir, vertical urbanism, holographic advertising |
| District 9 | Grounded sci-fi, industrial decay, repurposed alien tech |
| Akira | Cyberpunk urbanism, neon-lit ruins, energy effects |

### Real-World Photography References

| Subject | Visual Takeaway |
| :------ | :-------------- |
| Detroit / Rust Belt abandoned factories | Industrial scale, decay patterns, material weathering |
| Kowloon Walled City (archived) | Dense vertical urbanism, chaotic wiring, human bricolage |
| Akihabara / Shibuya at night | Neon density, signage overload, puddle reflections |
| Chernobyl Exclusion Zone | Nature reclaiming technology, eerie stillness |
| Modern tactical gear catalogs | Authentic equipment shapes, material references |

<!-- REF_IMAGE: Final mood board collage — combining industrial photography, neon cityscapes, tactical gear, and concept art references in the orange-white-black-cyan palette -->
