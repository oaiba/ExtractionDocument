---
title: "Visual Style & Art Guidelines"
type: docs
---

## Visual Identity

**Style:** Grounded Neo-Industrial  
**Era:** Post-Collapse (Near Future 2035-2040)  
**Mood:** Desperate Survival meets Tactical Professionalism

### Design Philosophy

*   **Decay with Memory:** Every rusted panel was once new. Every ruin was a home. The world is *overgrown*, not just dirty.
*   **Tactical Clarity:** Gameplay elements (cover, loot, enemies) must be instantly readable against the chaotic background.
*   **Functional Fashion:** Gear looks practical. No glowing magical armor. Duct tape, zip ties, worn metal, and field repairs.
*   **Asymmetric Beauty:** Nothing is perfectly clean or symmetrical. Weathering, dirt, and damage tell stories.

---

## Global Color Palette

<!-- REF_IMAGE: Color palette reference sheet — showing all primary, environmental, and rarity colors as labeled swatches with hex codes -->

### Primary Game Colors (Interactive UI)

*Used for UI elements and gameplay feedback across all platforms.*

| Role              | Color Name    | Hex       | RGB         | CMYK       | Usage                                                | Accessibility                   |
| :---------------- | :------------ | :-------- | :---------- | :--------- | :--------------------------------------------------- | :------------------------------ |
| **Friendly**      | Tactical Blue | `#3B82F6` | 59,130,246  | 76,47,0,4  | Minimap Markers, Squad HUD, Objective Indicators     | WCAG AA Pass (4.5:1 on dark BG) |
| **Hostile**       | Critical Red  | `#EF4444` | 239,68,68   | 0,72,72,6  | Enemy Highlights, Damage Flash, Alert States         | WCAG AA Pass (4.5:1 on dark BG) |
| **Loot/Interact** | Neon Yellow   | `#FACC15` | 250,204,21  | 0,18,92,2  | Interactive Objects, Pickup Prompts, Quest Items     | WCAG AAA Pass (7:1 on dark BG)  |
| **Objective**     | Signal Green  | `#22C55E` | 34,197,94   | 83,0,52,23 | Extraction Zones, Completed Tasks, Success States    | WCAG AA Pass (4.5:1 on dark BG) |
| **Neutral**       | Steel Gray    | `#6B7280` | 107,114,128 | 16,11,0,50 | HUD Backgrounds, Non-Interactive UI, Disabled States | WCAG AA Pass (3:1 min)          |
| **Warning**       | Hazard Orange | `#F97316` | 249,115,22  | 0,54,91,2  | Danger Zones, Low Health, Critical Alerts            | WCAG AA Pass (4.5:1 on dark BG) |

### Environmental Base (Atmospheric Palette)

*Used for level design, lighting, and world-building.*

| Category       | Color Name       | Hex       | Usage                                                       | Material Examples                                                 |
| :------------- | :--------------- | :-------- | :---------------------------------------------------------- | :---------------------------------------------------------------- |
| **Industrial** | Rust Orange      | `#D97706` | Metal structures, decaying machinery, oxidized surfaces     | Corrugated steel, chain-link fences, shipping containers          |
| **Urban**      | Concrete Gray    | `#94A3B8` | Buildings, roads, rubble, brutalist architecture            | Cracked pavement, rebar-exposed walls, abandoned infrastructure   |
| **Nature**     | Overgrowth Green | `#166534` | Vines, moss reclaiming the city, wild vegetation            | Creeping ivy on walls, moss on concrete, saplings through asphalt |
| **Lighting**   | Sodium Vapor     | `#FBBF24` | Streetlights, old factory lamps, artificial light pollution | Flickering lamps, emergency lighting, generator-powered bulbs     |
| **Darkness**   | Shadow Blue      | `#1E293B` | Deep shadows, night ambiance, unlit areas                   | Moonlit corners, basement darkness, storm clouds                  |
| **Accent**     | Cyan Highlight   | `#06B6D4` | Tech elements, holographic UI, futuristic remnants          | AR markers, terminal screens, drone indicators                    |

### Rarity System (Loot & Items)

Consistent across all platforms for instant recognition.

| Tier         | Color      | Hex       | Item Drop Rate | Visual Treatment                    |
| :----------- | :--------- | :-------- | :------------- | :---------------------------------- |
| Common       | Gray       | `#9CA3AF` | 60%            | No outline, matte finish            |
| Uncommon     | Green      | `#10B981` | 25%            | Thin outline, slight sheen          |
| Rare         | Blue       | `#3B82F6` | 10%            | Medium outline, subtle glow         |
| Epic         | Purple     | `#A855F7` | 4%             | Thick outline, pulsing glow         |
| Legendary    | Gold       | `#F59E0B` | 0.9%           | Double outline, particle effects    |
| Unique/Quest | Orange-Red | `#F97316` | Story-locked   | Animated outline, unique icon badge |

---

## Typography System

### Primary Font: **"Oxanium"** (Google Fonts)

*   **Usage:** Headings, UI headers, important stats, timers
*   **Style:** Cyber-industrial but legible. Square letterforms with subtle chamfered edges
*   **Weights:** Regular (400), Medium (500), Bold (700)
*   **License:** Open Font License (safe for commercial use)

**Character Set:** Latin, Cyrillic (for localization)

### Secondary Font: **"Inter"** (Google Fonts)

*   **Usage:** Body text, item descriptions, dialogue, tutorials
*   **Style:** Clean sans-serif, highly readable at small sizes, excellent kerning
*   **Weights:** Regular (400), Semi-Bold (600)
*   **License:** Open Font License

**Character Set:** Latin Extended, Cyrillic, Vietnamese (full localization support)

### Monospace Font: **"JetBrains Mono"** (Google Fonts)

*   **Usage:** Numerical stats, damage numbers, coordinates, code-like elements
*   **Style:** Developer-focused monospace, clear distinction between similar characters (0/O, 1/I/l)
*   **Weights:** Regular (400), Bold (700)

---

### Font Hierarchy & Platform Scaling

#### **Desktop/Console (1080p Base)**

| Level     | Font           | Size | Weight    | Use Case                              |
| :-------- | :------------- | :--- | :-------- | :------------------------------------ |
| **H1**    | Oxanium        | 48px | Bold      | Screen titles, main menu headers      |
| **H2**    | Oxanium        | 32px | Semi-Bold | Section headers, modal titles         |
| **H3**    | Oxanium        | 24px | Medium    | Sub-sections, tab labels              |
| **Body**  | Inter          | 16px | Regular   | Item descriptions, dialogue, tooltips |
| **Small** | Inter          | 14px | Regular   | Secondary info, timestamps, hints     |
| **Micro** | JetBrains Mono | 12px | Regular   | Stat numbers, ammo count, coordinates |

#### **Mobile (Adaptive Scaling)**

Base multiplier: **1.2x** for touch targets

| Level     | Font    | Size (Mobile) | Adjustments                        |
| :-------- | :------ | :------------ | :--------------------------------- |
| **H1**    | Oxanium | 40px          | Reduced to fit smaller screens     |
| **H2**    | Oxanium | 28px          | Maintains hierarchy ratio          |
| **Body**  | Inter   | 18px          | Increased for readability          |
| **Small** | Inter   | 16px          | Never below 14px (iOS HIG minimum) |

**Safe Area Margins:**
*   **iOS:** 44pt top/bottom, 20pt sides (for notch/home bar)
*   **Android:** 48dp top, 16dp sides

---

## Iconography System

<!-- REF_IMAGE: Icon sheet preview — showing weapon silhouettes, gear icons, consumables, ammo types, and status icons at 64x64 and 32x32 sizes -->

### Design Principles

*   **Style:** Flat vector, minimal gradients (solid fills preferred)
*   **Stroke Width:** 2px consistent across all icons (scalable)
*   **Fill:** Transparent background, solid or semi-transparent fill
*   **Canvas Size:** 64x64px base (upscales to 128x128px for high-DPI)
*   **Metaphor:** Real-world objects (specific, not generic)

### Icon Set Categories

#### **Weapons (Silhouette Recognition)**

Icons must be recognizable even at 32x32px (minimap size).

*   **Assault Rifle:** AK-74M silhouette (not generic "rifle")
*   **SMG:** MP5 profile
*   **Sniper:** SVD Dragunov long barrel shape
*   **Shotgun:** M870 pump-action
*   **Pistol:** Makarov PM compact frame
*   **Melee:** Combat knife (KA-BAR style)

#### **Gear & Equipment**

*   **Armor:** Plate Carrier vest (3A/4/5 variants by thickness)
*   **Helmet:** Fast MT tactical helmet (with NVG mount)
*   **Backpack:** MOLLE tactical pack (size = capacity)
*   **Rig:** Chest rig with visible mag pouches

#### **Consumables**

*   **Medkit:** IFAK pouch with red cross badge
*   **Bandage:** Rolled gauze with tape
*   **Painkiller:** Pill bottle silhouette
*   **Food:** MRE pack (not generic apple icon)
*   **Water:** Military canteen

#### **Ammunition (Caliber-Specific)**

Icons show actual bullet shapes for realism.

*   **5.56x45mm NATO:** Shorter, tapered
*   **7.62x39mm:** Slightly longer, straight case
*   **9x19mm Parabellum:** Short pistol round
*   **12 Gauge:** Shotgun shell (red or green tip)

#### **Status Icons**

*   **Health:** Medical cross inside tactical patch
*   **Stamina:** Running figure silhouette
*   **Hunger:** Fork + knife (not apple)
*   **Thirst:** Water droplet in canteen
*   **Bleed:** Blood drop with timer bar
*   **Fracture:** Bone with crack line

---

## Lighting and Readability (Top-Down View)

<!-- REF_IMAGE: Lighting comparison — showing the same scene under Daytime, Overcast, and Nighttime conditions with character rim lighting visible -->

The game is **Top-Down Isometric**, so lighting is critical for depth perception and character visibility.

### Character Lighting Rules

#### **1. Rim Lighting (Fresnel Effect)**

All characters MUST have a subtle rim light to pop from the background.

*   **Player Character:** Cyan rim light (`#06B6D4`, 10% intensity)
*   **Squadmates:** Blue rim light (`#3B82F6`, 8% intensity)
*   **Enemy Players:** Red rim light (`#EF4444`, 12% intensity) – brighter for clarity
*   **AI Scavs:** Yellow-orange rim light (`#FACC15`, 6% intensity)

**Technical Implementation:**
*   Shader-based fresnel calculation
*   Intensity fades with distance (closer = brighter)
*   Always visible through light foliage/smoke

#### **2. Silhouette Priority**

Props and environment must NOT have visual noise that confuses character outlines.

*   **Character Contrast:** 30% minimum luminance difference from ground
*   **Outline Shader:** 1-2px black outline on characters (optional setting)
*   **Shadow Quality:** Soft shadows preferred (hard shadows = visual clutter)

#### **3. Playable vs. Non-Playable Areas**

*   **Playable Zones:** 20-30% brighter ambient lighting
*   **Out of Bounds:** 50% darker, desaturated colors
*   **Transition Zones:** Gradual vignette darkening (3-meter fade)

### Environmental Lighting Scenarios

#### **Daytime (Clear)**
*   **Sun Angle:** 45-60 degrees (mid-morning/afternoon)
*   **Shadow Softness:** Medium (soft penumbra)
*   **Skybox Tint:** Pale blue with haze
*   **Ambient Occlusion:** Subtle (no hard black corners)

#### **Overcast/Storm**
*   **Sun Angle:** Diffused overhead (no hard shadows)
*   **Shadow Softness:** Very soft / nearly absent
*   **Skybox Tint:** Gray-blue with clouds
*   **Rain VFX:** Diagonal rain streaks, puddle reflections

#### **Nighttime (Limited Visibility)**
*   **Moon Lighting:** Cool blue-white (`#CBD5E1`)
*   **Artificial Lights:** Sodium vapor lamps (`#FBBF24`) in cities
*   **NVG Mode:** Green monochrome filter + grain noise
*   **Flashlight Cone:** 60-degree cone, 15-meter range

---

## Visual Effects (VFX) Guidelines

<!-- REF_IMAGE: VFX reference sheet — showing muzzle flash sprite sheet, blood splatter decals, and extraction helicopter dust effect -->

### Muzzle Flash

*   **Duration:** 1-2 frames (60 FPS) for realism
*   **Color:** Yellow-orange core, white-hot center
*   **Sprite Sheet:** 4x4 grid (16 variations for randomization)

### Blood Splatter (Age-Gated Content)

*   **Impact:** Small particle burst (5-10 droplets)
*   **Decal Lifespan:** 30 seconds before fade
*   **Color:** Dark red `#7F1D1D` (not bright cartoon red)

### Extraction Helicopter Effect

*   **Arrival:** Dust particle cloud, rotor wash
*   **Sound:** Bass-heavy engine hum (sub-bass for immersion)
*   **Visual Marker:** Green smoke grenade (`#22C55E`)

---

## Platform-Specific Visual Adaptations

### PC (High Fidelity)

*   **Texture Resolution:** 2K-4K (based on VRAM)
*   **Post-Processing:** Full suite (bloom, DOF, motion blur, SSAO)
*   **Draw Distance:** Maximum (500-meter visibility)
*   **Shadow Quality:** Ultra (4096x4096 shadow maps)
*   **Particle Count:** 10,000+ active particles

### Console (Optimized Balance)

#### **Next-Gen (PS5/Xbox Series X)**
*   **Texture Resolution:** 2K base
*   **Post-Processing:** Reduced bloom, no motion blur (60 FPS mode)
*   **Draw Distance:** 300 meters
*   **Shadow Quality:** High (2048x2048 shadow maps)
*   **Particle Count:** 5,000 active particles

#### **Last-Gen (PS4/Xbox One)**
*   **Texture Resolution:** 1K base
*   **Post-Processing:** Minimal (FXAA only)
*   **Draw Distance:** 150 meters
*   **Shadow Quality:** Medium (1024x1024 shadow maps)
*   **Particle Count:** 2,000 active particles

### Mobile (Performance Priority)

*   **Texture Resolution:** 512px-1K max
*   **Post-Processing:** Disabled (raw performance)
*   **Draw Distance:** 100 meters
*   **Shadow Quality:** Low (baked shadows where possible)
*   **Particle Count:** 500 active particles
*   **LOD Switching:** Aggressive (3 tiers: 10m, 50m, 100m)

#### **Mobile-Specific Optimizations**
*   **Shader Complexity:** Mobile-optimized shaders (fewer texture samples)
*   **Mesh Poly Count:** 50% reduction from PC version
*   **UI Texture Atlas:** Single 2048x2048 sheet for all UI icons
*   **Battery Saver Mode:** 30 FPS lock, reduced particle density

---

## UI Mockup Standards

### Design Tool Requirements

*   **Primary Tool:** Figma (collaborative, cloud-based)
*   **Prototyping:** Figma + Protopie (for complex interactions)
*   **Asset Handoff:** Zeplin or Figma Dev Mode
*   **Version Control:** Figma version history + Abstract (for large files)

### Artboard Sizes (Figma Templates)

| Platform             | Resolution                 | Artboard Name     | Safe Area Margins               |
| :------------------- | :------------------------- | :---------------- | :------------------------------ |
| **PC 16:9**          | 1920x1080                  | Desktop_Standard  | None (full bleed)               |
| **PC Ultrawide**     | 2560x1080                  | Desktop_Ultrawide | Center 1920px content           |
| **Console**          | 1920x1080                  | Console_TV        | 5% edge margin (TV overscan)    |
| **Mobile Portrait**  | 1170x2532 (iPhone 14 Pro)  | Mobile_Portrait   | iOS Safe Area (44pt top/bottom) |
| **Mobile Landscape** | 2532x1170                  | Mobile_Landscape  | 20pt sides                      |
| **Tablet**           | 2048x2732 (iPad Pro 12.9") | Tablet_Portrait   | 20pt all sides                  |

---

## Animation and Motion Design

### UI Animation Timing (Following Material Design Principles)

*   **Fast Actions:** 100-200ms (button press, toggle switch)
*   **Standard Transitions:** 300-400ms (menu slide, fade-in/out)
*   **Complex Animations:** 500-700ms (card flip, modal entrance)
*   **Cinematic Moments:** 1000ms+ (victory screen, level transition)

### Easing Curves

*   **Ease-Out (Deceleration):** Use for entering elements (menu slides in)
    *   Cubic-bezier: `(0.0, 0.0, 0.2, 1)`
*   **Ease-In (Acceleration):** Use for exiting elements (menu slides out)
    *   Cubic-bezier: `(0.4, 0.0, 1, 1)`
*   **Ease-In-Out (Standard):** Use for property changes (color transition)
    *   Cubic-bezier: `(0.4, 0.0, 0.2, 1)`

### Platform-Specific Frame Rates

*   **PC:** 144 FPS capable (animation deltas scale with FPS)
*   **Console:** 60 FPS locked (or 30 FPS in quality mode)
*   **Mobile:** 60 FPS target, 30 FPS fallback

---

## Visual QA Checklist

### Pre-Release Validation

- [ ] **Colorblind Simulation:** Test with all 3 major types (Protanopia, Deuteranopia, Tritanopia)
- [ ] **Contrast Ratios:** WCAG AA minimum for all text/icons (use Stark plugin)
- [ ] **Scale Testing:** UI readable at 720p, 1080p, 1440p, 4K
- [ ] **Safe Zones:** No critical UI elements in outer 5% (console overscan)
- [ ] **Font Rendering:** Anti-aliasing enabled on all platforms
- [ ] **Animation Smoothness:** No stuttering at target FPS per platform
- [ ] **Texture Compression:** Proper compression format per platform (BC7 PC, ASTC mobile)
- [ ] **Memory Budget:** UI textures <100MB total per scene
- [ ] **Load Time:** All UI assets load <2 seconds on HDD (not just SSD)

---

## Reference Materials

### Art Style Inspirations

*   **Escape from Tarkov:** Realistic gear modeling, worn textures
*   **The Division 2:** Post-apocalyptic urban decay, lighting mood
*   **Metro Exodus:** Industrial ruin aesthetics, atmospheric fog
*   **Stalker Series:** Eastern European architecture, Zone atmosphere
*   **Real-World Reference:** Pripyat, Chernobyl, abandoned Soviet infrastructure

### UI/UX Benchmarks

*   **Apex Legends:** Clean HUD, excellent readability
*   **Valorant:** Minimalist UI, high contrast
*   **Destiny 2:** Smooth transitions, sci-fi visual language
*   **Call of Duty: Warzone:** Tactical map design, loadout screens

---

## Technical Specifications

### Asset Naming Conventions

```
[Type]_[Name]_[Variant]_[Resolution].[Format]

Examples:
UI_Button_Primary_Idle_1080.png
Icon_Weapon_AK74_Legendary_64.svg
VFX_MuzzleFlash_AR_01.fbx
Font_Oxanium_Bold.ttf
```

### File Format Standards

| Asset Type            | Format      | Compression | Notes                                   |
| :-------------------- | :---------- | :---------- | :-------------------------------------- |
| **UI Icons**          | PNG / SVG   | Lossless    | SVG for scaling, PNG for raster effects |
| **Textures (PC)**     | TGA / PNG   | DXT5 / BC7  | Alpha channel required                  |
| **Textures (Mobile)** | PNG         | ASTC 4x4    | iOS/Android optimized                   |
| **Fonts**             | TTF / WOFF2 | N/A         | WOFF2 for web builds                    |
| **3D Models**         | FBX         | N/A         | Triangulated, <10k poly for UI elements |

