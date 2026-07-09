---
title: "Art Direction"
type: docs
weight: 1
---

## Visual Identity

**Art Style:** Cyberpunk Neo-Industrial — Semi-Realistic Cartoon Hybrid  
**Tone:** High-tech decay, neon-lit ruins, tactical tension  
**Perspective:** Top-down (isometric-style camera)  
**Platform:** Cross-platform (PC, Console, Mobile)

```
REALISTIC ──────────────●──────→ STYLIZED
                        ▲
                   Game Position
               (40% Realistic, 60% Stylized)
```

The visual language blends **grounded tactical realism** (authentic gear, weathered materials, PBR lighting) với **stylized cartoon readability** (exaggerated silhouettes, bold color accents, clean edges). A cyberpunk layer adds neon technology, holographic elements, và digital decay on top of a post-collapse industrial foundation.

<!-- REF_IMAGE: Art style reference collage — showing the spectrum from realistic tactical gear to stylized nhân vật proportions với cyberpunk neon accents -->

---

## Art Pillars

### 1. Neon Decay

**Concept:** A ruined industrial world where advanced technology persists in fragments — holographic billboards still flicker over collapsed buildings, abandoned drones rust beside cracked neon signs.

**Implementation:**
- Environments combine industrial ruin với cyberpunk tech remnants
- Neon lighting cuts thông qua desaturated decay (orange và cyan against gray/black)
- Holographic UI elements on in-world surfaces (broken terminals, vending machines)
- Nature reclaims technology — vines grow over circuit boards, moss on server racks

**Visual Rule:** Every scene must contain at least one **warm neon source** (orange/amber) và one **cool neon source** (cyan/teal) to maintain the cyberpunk identity even in outdoor areas.

<!-- REF_IMAGE: Neon Decay mood board — showing industrial ruins với flickering neon signs, overgrown tech, và orange-cyan lighting contrast -->

### 2. Tactical Clarity

**Concept:** Every element phải được dễ đọc from a top-down perspective at gameplay speed. Silhouettes, color coding, và contrast hierarchy serve gameplay first.

**Hierarchy:**
```
Priority 1: PLAYER        → Brightest silhouette, orange-cyan accent rim light
Priority 2: ENEMIES       → High-contrast red markers, distinct silhouettes
Priority 3: LOOT          → Rarity-coded glow (white, green, blue, purple, gold)
Priority 4: COVER          → Neutral tones, readable shapes
Priority 5: BACKGROUND    → Desaturated, atmospheric, minimal noise
```

**Rules:**
- người chơi nhân vật always have a hiển thị rõ **rim light** (customizable color)
- địch types distinguishable by silhouette alone at 100+ units
- Interactive objects have subtle **emissive outlines** (toggle in settings)
- UI elements never overlap gameplay-critical màn hình areas

### 3. Stylized Grit

**Concept:** nhân vật và object proportions lean toward stylized — slightly exaggerated shoulders, vũ khí, và gear — while materials và lighting cách dùng realistic PBR rendering. This tạo memorable, iconic designs that remain grounded.

**Not This:** Photorealistic military sim, pure cartoon, anime  
**nhưng This:** Overwatch meets The Division meets Cyberpunk 2077 — tactical gear với personality

**nhân vật Proportions:**
```
Head-to-body ratio:   1:6.5 (slightly larger head for readability)
Shoulder width:       1.8-2.2 heads wide (heroic proportions)
Hands:                110% realistic scale (weapon grip visible from top-down)
Gear:                 Exaggerated 10-15% for silhouette reads
```

### 4. Cross-Platform Scalability

**Concept:** Art assets are authored at the highest quality tier (PC Ultra) và scaled down thông qua LOD chains và quality settings. Mobile is not the floor — it is one target among three.

**Quality Tiers:**

| Tier | Platform | Target FPS | Visual ghi chú |
| :--- | :------- | :--------- | :----------- |
| Ultra | PC High-End | 120+ | Full PBR, Nanite, ray-traced reflections, max particles |
| High | PC Mid / Console | 60 | Full PBR, standard LODs, most effects |
| Medium | Console Low / Tablet | 30-60 | Simplified shaders, reduced particles |
| Low | Mobile | 30 | Texture streaming, simplified lighting, min particles |

---

## Brand Color Palette

The game's visual identity is built on four brand colors. All UI, marketing materials, chính art, và in-world signage derive from this palette.

### primary Brand Colors

| Role | Name | Hex | Usage |
| :--- | :--- | :-- | :---- |
| **primary Accent** | Signal Orange | #F97316 | người chơi highlights, critical UI, call-to-action buttons, warm neon |
| **cốt lõi Neutral** | Bone White | #F8FAFC | Text, clean UI surfaces, bright highlights |
| **Foundation** | Void Black | #0A0A0B | Backgrounds, shadows, panel bases, deep contrast |
| **secondary Accent** | Tactical Cyan | #06B6D4 | Tech elements, friendly markers, cool neon, secondary UI |

<!-- REF_IMAGE: Brand color palette card — showing all 4 primary colors as large swatches với hex codes và usage examples -->

### Extended Palette

#### Gameplay Colors

| Function | Color | Hex | Context |
| :------- | :---- | :-- | :------ |
| Friendly | Blue | #3B82F6 | Teammate markers, squad info |
| Hostile | Red | #EF4444 | địch indicators, damage, danger zones |
| Neutral / AI | Amber | #F59E0B | Unaffiliated NPCs, caution |
| Objective | Green | #22C55E | Extraction points, quest markers, success |
| cảnh báo | Orange | #F97316 | Low đạn, weight limit, moderate alert |
| Critical | Red | #DC2626 | Low máu, critical damage, hệ thống failure |

#### Item Rarity Colors

| Rarity | Color | Hex | In-World Effect |
| :----- | :---- | :-- | :-------------- |
| Common | Steel Gray | #9CA3AF | No glow |
| Uncommon | Lime Green | #22C55E | Subtle pulse (0.5s cycle) |
| Rare | Cobalt Blue | #3B82F6 | Soft glow + faint hum |
| Epic | Neon Purple | #A855F7 | Medium glow + particle wisps |
| Legendary | Molten Gold | #EAB308 | Strong glow + particle trail + audio sting |

#### Environmental Palette

| Zone Type | Base Tones | Neon Accent | Atmosphere |
| :-------- | :--------- | :---------- | :--------- |
| Industrial | Grays (#6B7280), Rust (#92400E) | Orange (#F97316) | Smoky, dense, vertical pipes |
| Urban Ruins | Concrete (#D1D5DB), Asphalt (#374151) | Cyan (#06B6D4) + Pink (#EC4899) | Billboard glow, puddle reflections |
| Nature / Outskirts | Muted Green (#65A30D), Earth (#78350F) | Sparse amber (#F59E0B) | Overcast, fog, minimal tech |
| Underground / Labs | Dark Blue (#1E293B), Black (#111827) | Cyan (#06B6D4) + Red (#DC2626) | Emergency lighting, high contrast |
| Military / Bunker | Olive (#4D7C0F), Concrete (#9CA3AF) | Green (#22C55E) | Tactical, clean, functional |

---

## Faction Color Schemes

Each faction has a distinct color identity that manifests in their territory, gear, và associated UI.

| Faction | primary | secondary | Neon Accent | Aesthetic |
| :------ | :------ | :-------- | :---------- | :-------- |
| **Salvage Corps** | Orange #D97706 | Gray #6B7280 | Amber #FBBF24 | Industrial worker, warm, rugged |
| **Tech Syndicate** | Cyan #06B6D4 | Black #111827 | White #F9FAFB | Cold, high-tech, digital precision |
| **Underground Network** | Purple #7C3AED | Gold #EAB308 | Magenta #EC4899 | Mysterious, luxurious, contraband |
| **Peacekeepers** | Blue #2563EB | White #F9FAFB | Red #DC2626 | Military discipline, authority |

<!-- REF_IMAGE: Faction identity sheet — showing 4 faction color swatches alongside representative nhân vật silhouettes và environmental chi tiết -->

---

## nhân vật Art Guidelines

### Operator Design Philosophy

Operators are the người chơi's avatar và phải được instantly recognizable from a top-down perspective. The design blends **tactical realism** (authentic gear silhouettes, functional pouches, proper giáp coverage) với **stylized clarity** (exaggerated proportions for readability, bold color accents, cartoon-influenced edges).

**cốt lõi Rules:**
- Every operator class has a unique **silhouette dễ đọc at 100+ units** distance
- Gear is functional — every pouch, strap, và plate has a mục đích
- Cyberpunk tech integrated subtly: wrist displays, helmet HUDs, comms earpieces
- Color accents cách dùng the brand palette (orange/cyan highlights on dark gear base)

### Silhouette Guide

```
Tank:        ████████████   Wide shoulders, heavy plates, riot visor
Assault:     ██████████     Athletic build, ammo cross-chest, medium helmet
Support:     ████████       Medium build, medical pack on back, cross armband
Recon:       ██████         Slim profile, tech goggles, compact gear
Specialist:  █████████      Utility belt, tool pouches, asymmetric loadout
```

<!-- REF_IMAGE: Operator silhouette lineup — showing all 5 classes in top-down và front view với class-defining visual elements highlighted -->

### nhân vật Model Specifications

**Cross-Platform Polygon Budget:**

| Component | Mobile (Low) | Console (Mid) | PC Ultra (High) |
| :-------- | :----------- | :------------ | :-------------- |
| Body base | 6,000 | 10,000 | 16,000 |
| Head | 2,000 | 3,500 | 5,000 |
| giáp / Gear | 3,000 | 5,500 | 8,000 |
| Accessories | 800 | 1,500 | 3,000 |
| Backpack | 500 | 800 | 1,500 |
| **Total** | **12,300** | **21,300** | **33,500** |

**Texture Resolution:**

| Map | Mobile | Console | PC Ultra |
| :-- | :----- | :------ | :------- |
| Base Color | 1024x1024 | 2048x2048 | 4096x4096 |
| Normal | 1024x1024 | 2048x2048 | 4096x4096 |
| ORM (AO/Roughness/Metallic) | 1024x1024 | 2048x2048 | 2048x2048 |
| Emissive (tech glow) | 512x512 | 1024x1024 | 2048x2048 |

**Rigging:**
- UE5 Mannequin skeleton compatible
- 70-80 bones standard
- Cloth simulation on pouches, straps (PC/Console only — baked on Mobile)
- Facial rig: optional (cinematics only)

### Operator Visual Themes

**Assault:**
- Military tactical vest, cross-chest đạn belt
- Medium helmet với visor (cyberpunk HUD glow on visor)
- Combat boots, knee pads
- **Accent:** Orange (#F97316) bands, shoulder patches
- **Materials:** Kevlar, ballistic nylon, polymer plates
- **Cyberpunk Touch:** Wrist-mounted đạn counter display

**Support:**
- Medical cross on sleeve và vest
- First aid backpack (prominent, hiển thị rõ from top-down)
- Lighter giáp for mobility
- **Accent:** Cyan (#06B6D4) và white medical cross
- **Materials:** Performance fabrics, sterile-look panels
- **Cyberpunk Touch:** Holographic diagnostic màn hình on forearm

**Recon:**
- Sleek, minimal gear profile
- Tech goggles với glowing lens (cyan)
- Wrist-mounted display, compact earpiece
- **Accent:** Cyan (#06B6D4) tech glow on goggles và devices
- **Materials:** High-tech synthetic fabrics, matte black polymer
- **Cyberpunk Touch:** Active camouflage panels (subtle shimmer effect)

**Tank:**
- Heavy giáp plating, riot-grade shoulder guards
- Full-face visor helmet với breathing apparatus
- Reinforced boots, thick gloves
- **Accent:** Red (#DC2626) cảnh báo stripes on giáp plates
- **Materials:** Ceramic plates, heavy ballistic fabric, metal reinforcements
- **Cyberpunk Touch:** Power-assist frame hiển thị rõ at joints (faint glow)

**Specialist:**
- Utility vest với many hiển thị rõ tool pockets
- Tool belt, multi-tool holster
- Fingerless gloves, work goggles pushed up
- **Accent:** Amber (#F59E0B) utility markings, caution tape strips
- **Materials:** Canvas, tool leather, industrial rubber
- **Cyberpunk Touch:** Hacking device on wrist, data cable coils

<!-- REF_IMAGE: Operator class concepts — showing all 5 classes in full gear với material callouts và cyberpunk tech chi tiết highlighted -->

### AI địch Design

**Standard Soldiers:**
| Property | Specification |
| :------- | :------------ |
| Poly budget | 10,000-15,000 tris |
| Texture | 1024x1024 (shared atlas preferred) |
| Visual style | Generic military, neutral tan/olive tones |
| Silhouette | Clearly distinct from người chơi operators |
| Cyberpunk element | Mass-produced helmet với visor slit |

**Elite địch:**
| Property | Specification |
| :------- | :------------ |
| Poly budget | 15,000-22,000 tris |
| Texture | 2048x2048 unique |
| Visual style | Enhanced giáp, red accent glow lines |
| Silhouette | Larger than standard, unique helmet shapes |
| Cyberpunk element | hiển thị rõ cybernetic augmentations, arm-mounted vũ khí |

**Boss địch:**
| Property | Specification |
| :------- | :------------ |
| Poly budget | 25,000-50,000 tris |
| Texture | 2048x2048 hoặc 4096x4096 unique |
| Visual style | Distinctive silhouette, heavy giáp với glowing weak points |
| Silhouette | phải được recognizable from 200+ units |
| Cyberpunk element | Full cybernetic augmentation, energy shields, holographic threat display |

<!-- REF_IMAGE: địch type lineup — showing Standard, Elite, và Boss địch concepts với increasing visual complexity và cyberpunk augmentation -->

---

## vũ khí Art Guidelines

### Design Philosophy

vũ khí are grounded in real-world firearms nhưng enhanced với cyberpunk modifications. Every vũ khí looks like it could exist in a near-future world where military tech meets black-market customization.

**Principles:**
- Base silhouettes derived from real firearms (AK-platform, M4-platform, etc.)
- Cyberpunk enhancements: holographic sights, LED đạn counters, polymer-composite frames
- hiển thị rõ wear và personalization (scratches, tape wraps, custom engravings)
- Attachment modularity hiển thị rõ — rails, mounting points, modular barrels
- **Color Rule:** Base vũ khí is dark gray/black; attachments và accents cách dùng brand colors

### vũ khí Category Visual Guide

| Category | Silhouette Profile | chính Visual | Cyberpunk Touch |
| :------- | :----------------- | :--------- | :-------------- |
| Assault Rifle | Medium length, magazine prominent | Rail hệ thống, standard optics | Digital đạn counter on side |
| SMG | Compact, boxy frame | Large magazine, folding stock | LED fire-mode indicator |
| Shotgun | Wide barrel, pump hiển thị rõ | Shell holder on side | Smart-choke indicator light |
| Sniper Rifle | Long barrel, large scope | Bipod, precision stock | Digital range-finder on scope |
| Pistol | Compact, clean profile | hiển thị rõ slide mechanism | Micro-LED sight dot |
| Melee | rõ blade hoặc blunt shape | Grip tape, combat edge | Vibro-edge glow (rare skins) |

### vũ khí Model Specifications

**Cross-Platform Polygon Budget:**

| vũ khí Type | Mobile | Console | PC Ultra | Attachments (max) |
| :---------- | :----- | :------ | :------- | :----------------- |
| Pistol | 1,500 | 2,500 | 4,000 | +800 |
| SMG | 2,000 | 3,500 | 5,000 | +1,200 |
| Assault Rifle | 3,000 | 4,500 | 6,500 | +1,500 |
| Shotgun | 2,500 | 4,000 | 5,500 | +1,200 |
| Sniper Rifle | 3,500 | 5,000 | 7,000 | +1,800 |
| LMG | 4,000 | 5,500 | 7,500 | +1,500 |
| Melee | 800 | 1,500 | 2,500 | N/A |

**Texture:**
- Resolution: 1024x1024 (Mobile), 2048x2048 (Console/PC)
- Maps: Base Color, Normal, ORM, Emissive (for tech glow elements)
- Skin support: Material parameter switching + vertex color channel (R = wear level)

**Wear Levels:**
```
Factory New    —  5% of drops  — Clean, sharp edges, full emissive glow
Field-Tested   — 30% of drops  — Minor scratches, slight emissive fade
Well-Worn      — 40% of drops  — Visible use marks, tape repairs, dim glow
Battle-Scarred — 20% of drops  — Heavy damage, rust patches, intermittent glow
Veteran        —  5% of drops  — Heavy wear + custom engravings + unique emissive pattern
```

<!-- REF_IMAGE: vũ khí wear level comparison — showing the same assault rifle at all 5 wear stages, với chi tiết callouts for scratches, emissive, và custom elements -->

---

## Environment Art Guidelines

### Design Philosophy

Environments tell the story of a world where advanced civilization collapsed, leaving behind a landscape of **industrial ruin laced với dying technology**. The cyberpunk layer means that even in decay, technology persists — holographic ads still loop on cracked displays, automated hệ thống still whir in dark corridors, neon signs cast colored light over rubble.

### Building Exteriors

**Industrial Buildings:**
- Corrugated metal siding với rust bloom patterns
- Broken windows revealing interior darkness
- Faded corporate logos (Nexus Corp branding)
- Safety signage — cracked, flickering LED variants
- Pipe networks, venting steam
- **Cyberpunk Layer:** Malfunctioning LED strip lights along rooflines, holographic "DANGER" signs still projecting

**Urban Buildings:**
- Concrete và brick với varied damage trạng thái
- Fire escapes, balconies với abandoned items
- Storefronts với shattered glass, looted interiors
- Billboard frames — some still displaying glitched holographic ads
- **Cyberpunk Layer:** Neon signs (some still lit), vending machines với flickering màn hình, data cable bundles running along walls

**Military Structures:**
- Reinforced concrete bunkers, blast walls
- Watchtowers với mounted searchlights
- Razor wire, barricades, sandbag positions
- Active surveillance cameras (blinking red LED)
- **Cyberpunk Layer:** Automated turret mounts, holographic perimeter cảnh báo, EMP shielding panels

<!-- REF_IMAGE: Building exterior concepts — showing Industrial, Urban, và Military building types với cyberpunk tech layer chi tiết highlighted in orange/cyan -->

### Interior Spaces

**Lighting Philosophy:**
- All interior light sources phải được **motivated** (window, fixture, màn hình, emergency light)
- Contrast is high — pools of light in dark spaces
- Cyberpunk tech provides additional light: glowing terminals, holographic displays, LED strips
- Emergency lighting uses red hoặc amber tones

**Clutter và Storytelling:**
- Abandoned items tell stories (overturned chairs, scattered papers, personal effects)
- Tech debris: broken drones, discarded data pads, tangled cables
- Not too dense — performance first, readability always
- Lootable items have subtle emissive highlight (toggleable in settings)

**Material Palette by Zone:**
```
Industrial Interior:   60% Metal (rusted)  |  20% Concrete  |  10% Tech panels  |  10% Organic
Urban Interior:        40% Concrete/Brick  |  25% Glass     |  20% Tech/Screens |  15% Fabric
Lab/Underground:       50% Tech panels     |  25% Metal     |  15% Glass        |  10% Bio-hazard
Military Interior:     45% Concrete        |  30% Metal     |  15% Tech         |  10% Utility
```

### Props

**Loot Containers (Rarity-Coded):**

| Rarity | Visual | Glow | Cyberpunk chi tiết |
| :----- | :----- | :--- | :--------------- |
| Common | Gray metal crate, simple latch | None | Basic serial number stamp |
| Uncommon | Green-striped container, slightly reinforced | Subtle green pulse | Small LED lock indicator |
| Rare | Blue-accented case, digital lock pad | Soft blue glow | Holographic lock interface |
| Epic | Purple energy-rimmed container, reinforced | Medium purple glow + particle wisps | Scanning laser pattern |
| Legendary | Gold-trimmed vault, armored plating | Strong gold glow + particle trail | Full holographic display + audio hum |

**Cover Objects:**
- Concrete barriers: full cover, 1.5m+ height
- Crates và pallets: half cover, destructible on epic loot locations
- Metal drums: partial cover, can be knocked over
- Vehicles: varied cover levels, some với active hazard lights
- Jersey walls với faded road markings

**Interactive Objects:**
- Doors: sliding (tech areas), hinged (traditional areas), damaged (jammed/breakable)
- Terminals: interact to hack, toggle lights, unlock areas — cyberpunk glitch effect on activation
- Vending machines: purchase consumables, flickering màn hình, brand logos
- Elevators: functional in some areas, broken in others

---

## VFX và Particle Effects

### Combat Effects

**Muzzle Flashes:**
- Bright orange-white burst, vũ khí-cụ thể shape
- Size scales với vũ khí caliber
- Smoke wisps trail (thin, fast-dissipating)
- Light source emitted briefly (illuminates nearby surfaces for 1 frame)

**Bullet Impacts:**
- Material-cụ thể response: sparks on metal, dust on concrete, splinters on wood, digital glitch on tech surfaces
- Decal placed at impact point (bullet hole, crack, scorch)
- Small particle burst (directional, away from impact normal)

**Blood Effects:**
- Stylized — not photorealistic (rating-appropriate)
- Red particle spray với slight orange tint (matching brand palette)
- Small decal on ground/walls
- Quick fade (0.5s)

**Explosions:**
- Fireball cốt lõi (orange-white)
- Smoke plume (dark gray, volumetric on PC, billboard on mobile)
- Debris particles (small geometry chunks)
- màn hình shake + brief light flash
- Shockwave ring (transparent distortion, ground-level)

### Cyberpunk-cụ thể Effects

**Digital Glitch:**
- Brief RGB-split flicker effect on hacked objects
- Horizontal scan lines appear momentarily
- cách dùng: Terminal hacking, EMP impact, shield disruption

**Neon Trail:**
- Persistent light trail from high-speed movement hoặc projectiles
- Color matches source (cyan for người chơi abilities, orange for địch tech)
- Fades over 1-2 seconds

**Holographic Projection:**
- Semi-transparent, slightly flickering geometry
- Scan line effect (horizontal bands)
- Color: primarily cyan, shift to orange on malfunction
- cách dùng: In-world terminals, quest markers, faction territory borders

**Energy Shield:**
- Hexagonal grid pattern, transparent until struck
- Impact tạo ripple effect from hit point
- Color: blue (friendly), red (địch), gold (boss)
- Cracking pattern as shield máu depletes

<!-- REF_IMAGE: VFX reference sheet — showing muzzle flash, impact effects, digital glitch, neon trail, holographic projection, và energy shield examples -->

### Environmental Effects

**Weather:**

| Type | Particles | Surface Effect | Cyberpunk Layer |
| :--- | :-------- | :------------- | :-------------- |
| Rain | Falling streaks + splash | Puddle ripples, wet surface PBR | Neon reflections in puddles |
| Fog | Volumetric (PC), flat layers (Mobile) | Reduced visibility | Neon glow diffusion thông qua fog |
| Dust Storm | Brown/gray particle swirl | Reduced visibility, sand accumulation | Static interference on tech objects |
| Contamination | Red/green toxic fog | màn hình vignette on người chơi | Hazmat cảnh báo holograms activate |

**Fire:**
- Flickering flame particles (orange-yellow cốt lõi, red tips)
- Smoke column (dark, rises và dissipates)
- Heat distortion shimmer (PC/Console only)
- Embers — small rising particles
- Light source: warm orange, dynamic flicker

### Effect Performance Budgets

| Platform | Max Simultaneous Particles | Max Active Emitters | ghi chú |
| :------- | :------------------------- | :------------------ | :---- |
| PC Ultra | 5,000 | 50 | Full volumetrics, ray-traced reflections |
| Console | 2,500 | 30 | Standard volumetrics, màn hình-space reflections |
| Mobile High | 1,000 | 15 | Billboard particles, simplified materials |
| Mobile Low | 500 | 8 | Minimal effects, sprite-based |

---

## Animation Guidelines

### nhân vật Animations

**Movement Set:**

| Animation | Frames | Loop | Priority | Top-Down Note |
| :-------- | :----- | :--- | :------- | :------------ |
| Idle Unarmed | 90 | Yes | Low | Subtle breathing, weight shift |
| Idle Rifle | 90 | Yes | Low | vũ khí sway, readiness stance |
| Walk Forward | 30 | Yes | Medium | rõ directional lean |
| Walk Backward | 30 | Yes | Medium | Distinctive backpedal silhouette |
| Walk Strafe L/R | 30 | Yes | Medium | Angled body, vũ khí forward |
| Run Forward | 20 | Yes | High | Exaggerated arm pump (stylized) |
| Sprint | 15 | Yes | High | Full lean, vũ khí lowered |
| Crouch Idle | 60 | Yes | Medium | Lower silhouette, compact |
| Crouch Walk | 40 | Yes | Medium | Slow, careful movement |

**Combat Animations:**

| Animation | Frames | Blend | ghi chú |
| :-------- | :----- | :---- | :---- |
| Fire Rifle | 8 | Additive (upper body) | Recoil hiển thị rõ from top-down |
| Fire Pistol | 6 | Additive (upper body) | Snap recoil |
| Reload Rifle | 60-90 | Full body | Mag-out, mag-in, bolt-pull events |
| Reload Pistol | 45 | Full body | Slide-release event |
| Melee Attack | 20 | Full body | Combo chain support |
| Throw Grenade | 40 | Full body | Release event at frame 25 |
| Hit React Light | 15 | Additive | Randomized direction |
| Hit React Heavy | 25 | Full body | Stagger animation |
| Death (multiple) | 45 | Full body | Ragdoll transition at frame 30 |

**Ability Activation:**
- Each operator class has unique ability activation animation (0.5-1.0s)
- Cyberpunk effects layer on top: holographic HUD flicker, tech glow
- Ability loop for persistent effects
- Deactivation animation (0.3s)

### Camera hệ thống

**Default Camera:**
- Top-down isometric (approximately 50-55 degree angle)
- Height: 1500-2000 units above người chơi
- Follow smoothing: 0.3 second interpolation lag

**Camera Shake:**

| Trigger | Amplitude | Duration | Platform Reduction |
| :------ | :-------- | :------- | :----------------- |
| vũ khí fire | 1-2 units | Per shot | 50% on Mobile |
| Explosion nearby | 5-10 units | 500ms | 60% on Mobile |
| Ability activation | 2-3 units | 300ms | 50% on Mobile |
| người chơi death | 10-15 units | 800ms | 70% on Mobile |

---

## Performance Art Guidelines

### Cross-Platform Polygon Budgets

**On-màn hình Budget:**

| Category | Mobile | Console | PC Ultra |
| :------- | :----- | :------ | :------- |
| nhân vật (hiển thị rõ) | 200K | 500K | 1M |
| vũ khí (hiển thị rõ) | 40K | 80K | 150K |
| Environment props | 600K | 1.5M | 3M |
| Vegetation | 300K | 800K | 1.5M |
| VFX | 100K | 300K | 500K |
| **Total on-màn hình** | **1.24M** | **3.18M** | **6.15M** |

**Texture Memory Budget:**

| Platform | Total VRAM Budget | Streaming | ghi chú |
| :------- | :---------------- | :-------- | :---- |
| Mobile Low | 400 MB | Aggressive | 1K textures max, atlas priority |
| Mobile High | 600 MB | Standard | 2K hero assets, 1K others |
| Console | 1.2 GB | Standard | 2K base, 4K hero assets |
| PC Ultra | 2.0 GB+ | Minimal | 4K textures, Nanite where applicable |

**Draw Call Targets:**

| Platform | Target | Technique |
| :------- | :----- | :-------- |
| Mobile | < 1,500 | Aggressive atlasing, instancing, merge actors |
| Console | < 3,000 | Instancing, hierarchical LOD |
| PC Ultra | < 5,000 | Nanite handles geometry, standard instancing |

**Shader Complexity:**
- Mobile: max 4 texture samples per material, avoid complex math
- Console: up to 8 texture samples, standard PBR
- PC: full PBR với subsurface, emissive chi tiết, parallax occlusion

---

## Style References

### Games

| Game | What to Reference | Our Adaptation |
| :--- | :---------------- | :------------- |
| Cyberpunk 2077 | Neon-lit urban decay, tech integration, substyle hệ thống | Scale down to top-down, cách dùng as environment mood reference |
| Overwatch 2 | Stylized nhân vật proportions, rõ silhouettes, bold colors | Match readability approach, adapt proportions for top-down |
| The Division 2 | Tactical gear authenticity, vũ khí chi tiết, ruined urban environments | Merge với cyberpunk neon layer |
| Apex Legends | nhân vật personality thông qua gear, vibrant color coding | cách dùng class distinction approach |
| Gears Tactics | Top-down tactical combat clarity, environmental chi tiết | Study camera angle và readability solutions |
| Valorant | Clean UI, nhân vật-driven design, readability-first art | Study how stylized và dễ đọc coexist |

### Visual Media

- Blade Runner 2049 — lighting, atmosphere, neon-in-decay
- Ghost in the Shell — cybernetic augmentation, tech integration
- District 9 — grounded sci-fi, industrial decay, alien tech repurposed
- Altered Carbon — future-noir, urban verticality, holographic advertising
- Akira — cyberpunk urbanism, neon-lit ruins

### Real-World Reference

- Abandoned industrial zones (Rust Belt USA, Detroit)
- Kowloon Walled City (dense vertical urbanism, chaotic wiring)
- Akihabara / Shibuya at night (neon density, signage overload)
- Chernobyl exclusion zone (nature reclaiming technology)
- Military surplus và tactical gear catalogs (authentic equipment shapes)

<!-- REF_IMAGE: Mood board collage — showing real-world industrial decay, neon cityscapes, tactical gear, và nature-reclaiming-technology photography -->

---

## Art Asset Pipeline

### Modeling Pipeline

1. **Concept art approval** — 2D concept với silhouette sheet và material callouts
2. **Blockout** — Rough proportions in engine, gameplay test
3. **High-poly sculpt** — ZBrush / Blender (chi tiết sculpt for baking)
4. **Low-poly retopology** — Target platform poly budgets
5. **UV unwrapping** — nhất quán texel density, separate lightmap UVs
6. **Baking** — Normal, AO, Curvature maps from high to low poly

### Texturing Pipeline

1. **Base materials** — Substance Painter, PBR metal/roughness workflow
2. **Weathering pass** — Rust, scratches, wear (driven by vertex color masks)
3. **Cyberpunk chi tiết pass** — Emissive maps for tech glow, LED elements
4. **Export** — PBR maps (Base Color, Normal, ORM, Emissive)
5. **Engine integration** — Material instances, parameter setup, LOD textures

### Implementation Pipeline

1. **Import to UE5** — Following naming conventions (see AssetGuidelines)
2. **Material setup** — Material instances from master materials
3. **LOD generation** — Auto/manual LODs per platform tier
4. **Collision** — Simple collision for gameplay, complex for hero assets
5. **Testing** — In-engine lighting test, top-down camera readability check

### Outsourcing Guidelines

**Outsource:**
- Environment props (bulk production)
- vũ khí base models (trước customization pass)
- nhân vật cosmetic skins
- Simple VFX

**Keep In-House:**
- Hero nhân vật và operator designs
- chính environment hero pieces (landmarks, extraction zones)
- All UI/UX design
- Art direction quyết định và final polish pass
- Cyberpunk chi tiết layer (emissive, holographic, tech elements)

---

## Art Team Tools

| Category | Tool | mục đích |
| :------- | :--- | :------ |
| 3D Modeling | Blender | primary modeling, UV, retopology |
| Sculpting | ZBrush | High-poly chi tiết sculpting |
| Texturing | Substance Painter | PBR texturing, weathering |
| Material Authoring | Substance Designer | Tileable materials, tech patterns |
| 2D Concept | Photoshop / Procreate | Concept art, mood boards |
| UI Design | Figma | Interface mockups, component library |
| Icons | Illustrator | Vector icon creation |
| Engine | Unreal Engine 5 | Final implementation |
| Version Control | Perforce / Git LFS | Asset versioning |
