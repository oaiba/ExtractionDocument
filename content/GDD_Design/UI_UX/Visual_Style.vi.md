---
title: "Visual Style & Art Guidelines"
type: docs
weight: 24
---

## Điều Hướng Nhanh

| điểm đến | cách dùng |
| :--- | :--- |
| [UI/UX Index](_index.md) | Full UI/UX documentation hub |
| [màn hình Groups Overview](Screen_Groups_Overview.md) | Lifecycle taxonomy và designer-ready spec template |
| [global UX Standards](Global_UX_Standards.md) | shared navigation, focus, trạng thái, modal, và accessibility rules |
| [HUD Design](HUD_Design.md) | In-raid HUD element placement và visual constraints |
| [Notification hệ thống](Notification_Systems.md) | Feedback, danger, toast, và status visual treatment |
| [UX flow](UX_Flows.md) | Journey và wireframe context for visual handoff |

---

## Visual Identity

**Style:** Grounded Neo-Industrial  
**Era:** Post-Collapse (Near Future 2035-2040)  
**Mood:** Desperate Survival meets Tactical Professionalism

### Design Philosophy

*   **Decay với Memory:** Every rusted panel was once new. Every ruin was a home. The world is *overgrown*, not just dirty.
*   **Tactical Clarity:** Gameplay elements (cover, loot, địch) phải được instantly dễ đọc against the chaotic background.
*   **Functional Fashion:** Gear looks practical. No glowing magical giáp. Duct tape, zip ties, worn metal, và field repairs.
*   **Asymmetric Beauty:** Nothing is perfectly clean hoặc symmetrical. Weathering, dirt, và damage tell stories.

---

## global Color Palette

<!-- REF_IMAGE: Color palette reference sheet — showing all primary, environmental, và rarity colors as labeled swatches với hex codes -->

### primary Game Colors (Interactive UI)

*Used for UI elements và gameplay feedback across all platforms.*

| Role              | Color Name    | Hex       | RGB         | CMYK       | Usage                                                | Accessibility                   |
| :---------------- | :------------ | :-------- | :---------- | :--------- | :--------------------------------------------------- | :------------------------------ |
| **Friendly**      | Tactical Blue | `#3B82F6` | 59,130,246  | 76,47,0,4  | Minimap Markers, Squad HUD, Objective Indicators     | WCAG AA Pass (4.5:1 on dark BG) |
| **Hostile**       | Critical Red  | `#EF4444` | 239,68,68   | 0,72,72,6  | địch Highlights, Damage Flash, Alert trạng thái         | WCAG AA Pass (4.5:1 on dark BG) |
| **Loot/Interact** | Neon Yellow   | `#FACC15` | 250,204,21  | 0,18,92,2  | Interactive Objects, Pickup Prompts, Quest Items     | WCAG AAA Pass (7:1 on dark BG)  |
| **Objective**     | Signal Green  | `#22C55E` | 34,197,94   | 83,0,52,23 | Extraction Zones, Completed Tasks, success trạng thái    | WCAG AA Pass (4.5:1 on dark BG) |
| **Neutral**       | Steel Gray    | `#6B7280` | 107,114,128 | 16,11,0,50 | HUD Backgrounds, Non-Interactive UI, disabled trạng thái | WCAG AA Pass (3:1 min)          |
| **cảnh báo**       | Hazard Orange | `#F97316` | 249,115,22  | 0,54,91,2  | Danger Zones, Low máu, Critical Alerts            | WCAG AA Pass (4.5:1 on dark BG) |

### Environmental Base (Atmospheric Palette)

*Used for level design, lighting, và world-building.*

| Category       | Color Name       | Hex       | Usage                                                       | Material Examples                                                 |
| :------------- | :--------------- | :-------- | :---------------------------------------------------------- | :---------------------------------------------------------------- |
| **Industrial** | Rust Orange      | `#D97706` | Metal structures, decaying machinery, oxidized surfaces     | Corrugated steel, chain-link fences, shipping containers          |
| **Urban**      | Concrete Gray    | `#94A3B8` | Buildings, roads, rubble, brutalist architecture            | Cracked pavement, rebar-exposed walls, abandoned infrastructure   |
| **Nature**     | Overgrowth Green | `#166534` | Vines, moss reclaiming the city, wild vegetation            | Creeping ivy on walls, moss on concrete, saplings thông qua asphalt |
| **Lighting**   | Sodium Vapor     | `#FBBF24` | Streetlights, old factory lamps, artificial light pollution | Flickering lamps, emergency lighting, generator-powered bulbs     |
| **Darkness**   | Shadow Blue      | `#1E293B` | Deep shadows, night ambiance, unlit areas                   | Moonlit corners, basement darkness, storm clouds                  |
| **Accent**     | Cyan Highlight   | `#06B6D4` | Tech elements, holographic UI, futuristic remnants          | AR markers, terminal màn hình, drone indicators                    |

### Rarity hệ thống (Loot & Items)

nhất quán across all platforms for instant recognition.

| Tier         | Color      | Hex       | Item Drop Rate | Visual Treatment                    |
| :----------- | :--------- | :-------- | :------------- | :---------------------------------- |
| Common       | Gray       | `#9CA3AF` | 60%            | No outline, matte finish            |
| Uncommon     | Green      | `#10B981` | 25%            | Thin outline, slight sheen          |
| Rare         | Blue       | `#3B82F6` | 10%            | Medium outline, subtle glow         |
| Epic         | Purple     | `#A855F7` | 4%             | Thick outline, pulsing glow         |
| Legendary    | Gold       | `#F59E0B` | 0.9%           | Double outline, particle effects    |
| Unique/Quest | Orange-Red | `#F97316` | Story-locked   | Animated outline, unique icon badge |

---

## Typography hệ thống

### primary Font: **"Oxanium"** (Google Fonts)

*   **Usage:** Headings, UI headers, quan trọng stats, timers
*   **Style:** Cyber-industrial nhưng legible. Square letterforms với subtle chamfered edges
*   **Weights:** Regular (400), Medium (500), Bold (700)
*   **License:** Open Font License (safe for commercial cách dùng)

**nhân vật Set:** Latin, Cyrillic (for localization)

### secondary Font: **"Inter"** (Google Fonts)

*   **Usage:** Body text, item descriptions, dialogue, tutorials
*   **Style:** Clean sans-serif, highly dễ đọc at small sizes, excellent kerning
*   **Weights:** Regular (400), Semi-Bold (600)
*   **License:** Open Font License

**nhân vật Set:** Latin Extended, Cyrillic, Vietnamese (full localization support)

### Monospace Font: **"JetBrains Mono"** (Google Fonts)

*   **Usage:** Numerical stats, damage thông số, coordinates, code-like elements
*   **Style:** Developer-focused monospace, rõ distinction between similar nhân vật (0/O, 1/I/l)
*   **Weights:** Regular (400), Bold (700)

---

### Font Hierarchy & Platform Scaling

#### **Desktop/Console (1080p Base)**

| Level     | Font           | Size | Weight    | cách dùng Case                              |
| :-------- | :------------- | :--- | :-------- | :------------------------------------ |
| **H1**    | Oxanium        | 48px | Bold      | màn hình titles, main menu headers      |
| **H2**    | Oxanium        | 32px | Semi-Bold | Section headers, modal titles         |
| **H3**    | Oxanium        | 24px | Medium    | Sub-sections, tab labels              |
| **Body**  | Inter          | 16px | Regular   | Item descriptions, dialogue, tooltips |
| **Small** | Inter          | 14px | Regular   | secondary info, timestamps, hints     |
| **Micro** | JetBrains Mono | 12px | Regular   | Stat thông số, đạn count, coordinates |

#### **Mobile (Adaptive Scaling)**

Base multiplier: **1.2x** for touch targets

| Level     | Font    | Size (Mobile) | Adjustments                        |
| :-------- | :------ | :------------ | :--------------------------------- |
| **H1**    | Oxanium | 40px          | Reduced to fit smaller màn hình     |
| **H2**    | Oxanium | 28px          | Maintains hierarchy ratio          |
| **Body**  | Inter   | 18px          | Increased for readability          |
| **Small** | Inter   | 16px          | Never below 14px (iOS HIG minimum) |

**Safe Area Margins:**
*   **iOS:** 44pt top/bottom, 20pt sides (for notch/home bar)
*   **Android:** 48dp top, 16dp sides

---

## Iconography hệ thống

<!-- REF_IMAGE: Icon sheet preview — showing vũ khí silhouettes, gear icons, consumables, đạn types, và status icons at 64x64 và 32x32 sizes -->

### Nguyên Tắc Thiết Kế

*   **Style:** Flat vector, minimal gradients (solid fills preferred)
*   **Stroke Width:** 2px nhất quán across all icons (scalable)
*   **Fill:** Transparent background, solid hoặc semi-transparent fill
*   **Canvas Size:** 64x64px base (upscales to 128x128px for high-DPI)
*   **Metaphor:** Real-world objects (cụ thể, not generic)

### Icon Set Categories

#### **vũ khí (Silhouette Recognition)**

Icons phải được recognizable even at 32x32px (minimap size).

*   **Assault Rifle:** AK-74M silhouette (not generic "rifle")
*   **SMG:** MP5 profile
*   **Sniper:** SVD Dragunov long barrel shape
*   **Shotgun:** M870 pump-action
*   **Pistol:** Makarov PM compact frame
*   **Melee:** Combat knife (KA-BAR style)

#### **Gear & Equipment**

*   **giáp:** Plate Carrier vest (3A/4/5 variants by thickness)
*   **Helmet:** Fast MT tactical helmet (với NVG mount)
*   **Backpack:** MOLLE tactical pack (size = capacity)
*   **Rig:** Chest rig với hiển thị rõ mag pouches

#### **Consumables**

*   **Medkit:** IFAK pouch với red cross badge
*   **Bandage:** Rolled gauze với tape
*   **Painkiller:** Pill bottle silhouette
*   **Food:** MRE pack (not generic apple icon)
*   **Water:** Military canteen

#### **Ammunition (Caliber-cụ thể)**

Icons show actual bullet shapes for realism.

*   **5.56x45mm NATO:** Shorter, tapered
*   **7.62x39mm:** Slightly longer, straight case
*   **9x19mm Parabellum:** Short pistol round
*   **12 Gauge:** Shotgun shell (red hoặc green tip)

#### **Status Icons**

*   **máu:** Medical cross inside tactical patch
*   **Stamina:** Running figure silhouette
*   **Hunger:** Fork + knife (not apple)
*   **Thirst:** Water droplet in canteen
*   **Bleed:** Blood drop với timer bar
*   **Fracture:** Bone với crack line

---

## Lighting và Readability (Top-Down View)

<!-- REF_IMAGE: Lighting comparison — showing the same scene under Daytime, Overcast, và Nighttime conditions với nhân vật rim lighting hiển thị rõ -->

The game is **Top-Down Isometric**, so lighting is critical for depth perception và nhân vật visibility.

### nhân vật Lighting Rules

#### **1. Rim Lighting (Fresnel Effect)**

All nhân vật MUST have a subtle rim light to pop from the background.

*   **người chơi nhân vật:** Cyan rim light (`#06B6D4`, 10% intensity)
*   **Squadmates:** Blue rim light (`#3B82F6`, 8% intensity)
*   **địch người chơi:** Red rim light (`#EF4444`, 12% intensity) – brighter for clarity
*   **AI Scavs:** Yellow-orange rim light (`#FACC15`, 6% intensity)

**Technical Implementation:**
*   Shader-based fresnel calculation
*   Intensity fades với distance (closer = brighter)
*   Always hiển thị rõ thông qua light foliage/smoke

#### **2. Silhouette Priority**

Props và environment không được have visual noise that confuses nhân vật outlines.

*   **nhân vật Contrast:** 30% minimum luminance difference from ground
*   **Outline Shader:** 1-2px black outline on nhân vật (optional setting)
*   **Shadow Quality:** Soft shadows preferred (hard shadows = visual clutter)

#### **3. Playable vs. Non-Playable Areas**

*   **Playable Zones:** 20-30% brighter ambient lighting
*   **Out of Bounds:** 50% darker, desaturated colors
*   **Transition Zones:** Gradual vignette darkening (3-meter fade)

### Environmental Lighting Scenarios

#### **Daytime (rõ)**
*   **Sun Angle:** 45-60 degrees (mid-morning/afternoon)
*   **Shadow Softness:** Medium (soft penumbra)
*   **Skybox Tint:** Pale blue với haze
*   **Ambient Occlusion:** Subtle (no hard black corners)

#### **Overcast/Storm**
*   **Sun Angle:** Diffused overhead (no hard shadows)
*   **Shadow Softness:** Very soft / nearly absent
*   **Skybox Tint:** Gray-blue với clouds
*   **Rain VFX:** Diagonal rain streaks, puddle reflections

#### **Nighttime (Limited Visibility)**
*   **Moon Lighting:** Cool blue-white (`#CBD5E1`)
*   **Artificial Lights:** Sodium vapor lamps (`#FBBF24`) in cities
*   **NVG Mode:** Green monochrome filter + grain noise
*   **Flashlight Cone:** 60-degree cone, 15-meter range

---

## Visual Effects (VFX) Guidelines

<!-- REF_IMAGE: VFX reference sheet — showing muzzle flash sprite sheet, blood splatter decals, và extraction helicopter dust effect -->

### Muzzle Flash

*   **Duration:** 1-2 frames (60 FPS) for realism
*   **Color:** Yellow-orange cốt lõi, white-hot center
*   **Sprite Sheet:** 4x4 grid (16 variations for randomization)

### Blood Splatter (Age-Gated Content)

*   **Impact:** Small particle burst (5-10 droplets)
*   **Decal Lifespan:** 30 seconds trước fade
*   **Color:** Dark red `#7F1D1D` (not bright cartoon red)

### Extraction Helicopter Effect

*   **Arrival:** Dust particle cloud, rotor wash
*   **Sound:** Bass-heavy engine hum (sub-bass for immersion)
*   **Visual Marker:** Green smoke grenade (`#22C55E`)

---

## Platform-cụ thể Visual Adaptations

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
*   **Post-Processing:** disabled (raw performance)
*   **Draw Distance:** 100 meters
*   **Shadow Quality:** Low (baked shadows where possible)
*   **Particle Count:** 500 active particles
*   **LOD Switching:** Aggressive (3 tiers: 10m, 50m, 100m)

#### **Mobile-cụ thể Optimizations**
*   **Shader Complexity:** Mobile-optimized shaders (fewer texture samples)
*   **Mesh Poly Count:** 50% reduction from PC version
*   **UI Texture Atlas:** Single 2048x2048 sheet for all UI icons
*   **Battery Saver Mode:** 30 FPS lock, reduced particle density

---

## UI Mockup Standards

### Designer-Ready Spec Translation

ASCII wireframes in the màn hình group trang define hierarchy, region ownership, trạng thái placement, và required information. They are not final artboards. Designers should translate them into polished layouts while preserving the same information priority.

| source Spec Element | Visual Design yêu cầu |
| :--- | :--- |
| Header | stable account/màn hình context; no decorative treatment that hides status |
| primary content | largest dễ đọc area; carries the màn hình's main người chơi task |
| chi tiết panel | fixed hoặc predictable width; selected item/trạng thái chi tiết do not resize the trang |
| cảnh báo lane | close to the CTA it affects; rõ severity label và cách sửa trực tiếp route |
| Action bar | stable CTA placement across default, cảnh báo, blocked, và success trạng thái |
| trạng thái badge | text label plus icon/shape; color only is not acceptable |
| ASCII grid/row | cách dùng nhất quán spacing, alignment, và target size in final layout |

### Density và Readability Rules

| Area | yêu cầu |
| :--- | :--- |
| Operational màn hình | dense nhưng scannable; prioritize labels, aligned values, và stable panels |
| Combat/in-raid overlays | minimal center obstruction; critical trạng thái only |
| Commerce màn hình | plain, high-trust copy; giá, contents, balance impact, và confirmation near CTA |
| Settings/hệ thống màn hình | consequence, recovery, và account safety copy near CTA |
| Social màn hình | privacy-safe identity display; compatibility blockers hiển thị rõ |
| Mobile | avoid shrinking desktop tables; cách dùng tabs, sheets, sticky CTAs, và larger touch rows |

### Mockup Acceptance

- [ ] Every trạng thái shown in a màn hình spec has at least one visual treatment in mockups.
- [ ] disabled và locked CTAs include dễ đọc reason text.
- [ ] Long labels fit mà không overlap at target language length và 200% text scale.
- [ ] Icons và colors are backed by labels, shape, position, hoặc pattern.
- [ ] primary CTA placement is stable between default, cảnh báo, và blocked trạng thái.

Layout (PC/Console)

```
+------------------------------------------------------------------+
| 12-col composition grid                                          |
|------------------------------------------------------------------|
| NAV  | MAIN CONTENT AREA                         | CONTEXT PANEL |
| 2col | 7col: cards, lists, preview, workbench     | 3col detail  |
|      |                                             | CTA / state |
|------------------------------------------------------------------|
| Footer: hints, warnings, controller focus help                   |
+------------------------------------------------------------------+
```

#### hệ thống Diagram

```
Color roles -> Component states -> Screen composition -> QA checks
     |               |                    |              |
     v               v                    v              v
 Friendly       Normal/Focus        Rail/Main/CTA    Contrast
 Hostile        Hover/Pressed       Overlay/Modal    Scale
 Warning        Locked/Error        Toast/System     Safe zone
 Objective      Success             Footer/Hints     Motion
```

### Design Tool yêu cầu

*   **primary Tool:** Figma (collaborative, cloud-based)
*   **Prototyping:** Figma + Protopie (for complex interactions)
*   **Asset Handoff:** Zeplin hoặc Figma Dev Mode
*   **Version Control:** Figma version history + Abstract (for large files)

### Artboard Sizes (Figma Templates)

#### hệ thống Diagram

```
+----------------------+  +----------------------+  +----------------------+
| Desktop 1920 x 1080  |  | Console TV 1920x1080 |  | Ultrawide 2560x1080  |
| full density         |  | 5% safe zone         |  | centered content     |
+----------------------+  +----------------------+  +----------------------+
          |                         |                         |
          v                         v                         v
   shared components        larger focus rings        side context panels
```

| Platform             | Resolution                 | Artboard Name     | Safe Area Margins               |
| :------------------- | :------------------------- | :---------------- | :------------------------------ |
| **PC 16:9**          | 1920x1080                  | Desktop_Standard  | None (full bleed)               |
| **PC Ultrawide**     | 2560x1080                  | Desktop_Ultrawide | Center 1920px content           |
| **Console**          | 1920x1080                  | Console_TV        | 5% edge margin (TV overscan)    |

---

## Animation và Motion Design

### UI Animation Timing (Following Material Design Principles)

*   **Fast Actions:** 100-200ms (button press, toggle switch)
*   **Standard Transitions:** 300-400ms (menu slide, fade-in/out)
*   **Complex Animations:** 500-700ms (card flip, modal entrance)
*   **Cinematic Moments:** 1000ms+ (victory màn hình, level transition)

### Easing Curves

*   **Ease-Out (Deceleration):** cách dùng for entering elements (menu slides in)
    *   Cubic-bezier: `(0.0, 0.0, 0.2, 1)`
*   **Ease-In (Acceleration):** cách dùng for exiting elements (menu slides out)
    *   Cubic-bezier: `(0.4, 0.0, 1, 1)`
*   **Ease-In-Out (Standard):** cách dùng for property changes (color transition)
    *   Cubic-bezier: `(0.4, 0.0, 0.2, 1)`

### Platform-cụ thể Frame Rates

*   **PC:** 144 FPS capable (animation deltas scale với FPS)
*   **Console:** 60 FPS locked (hoặc 30 FPS in quality mode)
*   **Mobile:** 60 FPS target, 30 FPS fallback

---

## Visual QA checklist

### Pre-Release Validation

- [ ] **Colorblind Simulation:** Test với all 3 major types (Protanopia, Deuteranopia, Tritanopia)
- [ ] **Contrast Ratios:** WCAG AA minimum for all text/icons (cách dùng Stark plugin)
- [ ] **Scale Testing:** UI dễ đọc at 720p, 1080p, 1440p, 4K
- [ ] **Safe Zones:** No critical UI elements in outer 5% (console overscan)
- [ ] **Font Rendering:** Anti-aliasing enabled on all platforms
- [ ] **Animation Smoothness:** No stuttering at target FPS per platform
- [ ] **Texture Compression:** Proper compression format per platform (BC7 PC, ASTC mobile)
- [ ] **Memory Budget:** UI textures <100MB total per scene
- [ ] **Load thời gian:** All UI assets load <2 seconds on HDD (not just SSD)

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
*   **Call of Duty: Warzone:** Tactical map design, loadout màn hình

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

| Asset Type            | Format      | Compression | ghi chú                                   |
| :-------------------- | :---------- | :---------- | :-------------------------------------- |
| **UI Icons**          | PNG / SVG   | Lossless    | SVG for scaling, PNG for raster effects |
| **Textures (PC)**     | TGA / PNG   | DXT5 / BC7  | Alpha channel required                  |
| **Textures (Mobile)** | PNG         | ASTC 4x4    | iOS/Android optimized                   |
| **Fonts**             | TTF / WOFF2 | N/A         | WOFF2 for web builds                    |
| **3D Models**         | FBX         | N/A         | Triangulated, <10k poly for UI elements |
