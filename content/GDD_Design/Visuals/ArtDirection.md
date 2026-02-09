---
title: "Art Direction"
type: docs
---

## Visual Identity

**Art Style:** Realistic with stylized elements  
**Tone:** Gritty, industrial, post-disaster  
**Perspective:** Top-down (isometric-style camera)  
**Platform:** Mobile-optimized

---

## Art Pillars

### 1. Clarity Above All
**Why:** Top-down mobile perspective needs instant readability

**Implementation:**
- Strong silhouettes
- High contrast
- Clear color coding
- Minimal visual noise

### 2. Grounded Realism
**Why:** Extraction gameplay requires a believable world

**Implementation:**
- Realistic materials (metal, concrete, fabric)
- Weathered, lived-in environments
- Physics-based rendering (PBR)
- Authentic military gear

### 3. Distinct Faction Identity
**Why:** Visual storytelling through environment

**Implementation:**
- Color schemes per faction
- Unique architectural styles
- Branded props and signage
- Consistent art language

### 4. Performance First
**Why:** Mobile platform limitations

**Implementation:**
- Optimized polygon counts
- Texture atlasing
- LOD systems
- Efficient shaders

---

## Color Palette

### Primary Palette (Environments)

**Industrial Zones:**
- Base: Grays (cool: #4A5568, warm: #6B7280)
- Accent: Rust Orange (#D97706)
- Highlight: Safety Yellow (#FBBF24)
- Shadow: Deep Blue-Gray (#1E293B)

**Natural Areas:**
- Base: Muted Greens (#65A30D, #84CC16)
- Earth Tones: Browns (#92400E, #78350F)
- Sky: Overcast Blue (#64748B)

**Urban Ruins:**
- Concrete: Light Gray (#D1D5DB)
- Weathered Paint: Faded Blues, Greens
- Rust: Orange-Brown (#C2410C)
- Vegetation Overgrowth: Dark Green (#166534)

---

### UI Color Palette

**Team Colors:**
- Friendly: Bright Blue (#3B82F6)
- Enemy: Bright Red (#EF4444)
- Neutral AI: Bright Yellow (#FACC15)

**Item Rarity:**
- Common: Gray (#9CA3AF)
- Uncommon: Green (#22C55E)
- Rare: Blue (#3B82F6)
- Epic: Purple (#A855F7)
- Legendary: Gold (#EAB308)

**UI Accents:**
- Primary: Cyan (#06B6D4)
- Warning: Orange (#F97316)
- Danger: Red (#DC2626)
- Success: Green (#10B981)

---

## Character Art Guidelines

### Operator Design

**Core Principles:**
**Core Principles:**
- Instant recognition from top-down perspective
- Clear silhouette differences
- Functional, believable gear
- Mobile polygon budget: 15,000-25,000 tris

**Silhouette Checklist:**
```
Tank:     ████████  (Bulky, wide shoulders)
Assault:  ███████   (Athletic, balanced)
Support:  ██████    (Medium, medical gear visible)
Recon:    █████     (Slim, low-profile)
Specialist: ██████  (Medium, tech visible)
```

---

### Character Art Specs

**Model Specifications:**
- Base body: 12,000 tris
- Gear/accessories: 3,000-8,000 tris
- Weapon: 2,000-4,000 tris
- Total: 15,000-25,000 tris

**Texture Resolution:**
- Main character: 2048x2048 (diffuse, normal, mask)
- Weapons: 1024x1024
- Accessories: 512x512
- Format: PNG (development), compressed in-engine

**Rigging:**
- UE5 Mannequin skeleton compatible
- 70-80 bones
- Facial rig: Optional (for cutscenes)

---

### Operator Visual Themes

**Assault:**
- Military vest over tactical shirt
- Ammo pouches prominent
- Combat boots
- Optional helmet
- **Color Accent:** Orange bands/patches
- **Material:** Durable fabrics, kevlar

**Support:**
- Medical cross markings (sleeve, vest)
- First aid pouches
- Lighter armor
- Clean, organized look
- **Color Accent:** Blue/white medical colors
- **Material:** Performance fabrics

**Recon:**
- Sleek, minimal gear
- Tech devices (headset, wrist display)
- Camouflage patterns
- Compact backpack
- **Color Accent:** Cyan tech glow
- **Material:** High-tech synthetics

**Tank:**
- Heavy armor plating
- Riot gear aesthetic
- Reinforced shoulders
- Large boots
- **Color Accent:** Red警告 stripes
- **Material:** Metal plates, heavy fabric

**Specialist:**
- Utility vest with many pockets
- Tool belt
- Fingerless gloves
- Casual-tactical mix
- **Color Accent:** Yellow utility markings
- **Material:** Canvas, tool leather

---

### AI Enemy Design

**Basic Soldiers:**
- Generic military gear
- Neutral colors (tan, olive)
- Clear enemy silhouette
- Lower poly: 8,000-12,000 tris

**Elite Enemies:**
- More armored
- Red accent colors
- Unique helmets
- 12,000-15,000 tris

**Boss Enemies:**
- Distinctive silhouettes
- Heavy armor
- Glowing weak points
- 20,000-30,000 tris

---

## Weapon Art Guidelines

### Design Philosophy
- Authentic military aesthetics
- Functional designs
- Clear weapon type identification
- Mobile-optimized

### Weapon Categories Visual

**Assault Rifles:**
- Modern military look
- Medium length
- Magazine prominent
- Rails for attachments

**SMGs:**
- Compact, boxy
- Short barrel
- Large magazine
- Folding stock

**Shotguns:**
- Wide barrel
- Pump action visible
- Shell holder on side
- Heavy, intimidating

**Sniper Rifles:**
- Long barrel
- Large scope
- Bipod
- Precision aesthetic

**Pistols:**
- Compact
- Simple silhouette
- Visible slide action
- Holsterable look

**Melee:**
- Combat knife
- Tactical baton
- Clear blade shine

---

### Weapon Art Specs

**Model:**
- Polygon count: 2,000-4,000 tris
- Modular parts (barrel, stock, magazine)
- Separate attachments

**Textures:**
- Resolution: 1024x1024
- PBR materials (metallic, roughness)
- Wear and tear details
- Different skins support

**Animations:**
- Idle, fire, reload
- Aim down sights
- Holster/draw
- Top-down friendly (no FP needed)

---

## Environment Art Guidelines

### Building Exteriors

**Industrial Buildings:**
- Corrugated metal siding
- Rust và weathering
- Broken windows
- Graffiti (lore-friendly)
- Safety signage (faded)

**Urban Buildings:**
- Concrete and brick
- Variety in window types
- Fire escapes
- Damage (cracks, collapse)
- Overgrown vegetation

**Military Structures:**
- Reinforced concrete
- Camouflage netting
- Barbed wire
- Watchtowers
- Blast walls

---

**Interior Spaces**

**Lighting:**
- Motivated light sources (windows, fixtures)
- Dramatic shadows
- God rays through damaged roof
- Emergency lighting (red)

**Clutter:**
- Abandoned items (chairs, papers, tools)
- Environmental storytelling
- Not too dense (performance)
- Lootable items stand out

**Materials:**
- Dirty, weathered surfaces
- Graffiti and posters
- Water damage, mold
- Broken equipment

---

### Props

**Loot Containers:**
- **Common Crate:** Gray metal box, simple
- **Military Locker:** Green, numbered
- **Rare Safe:** Blue glow, reinforced
- **Epic Vault:** Purple energy, high-tech
- **Legendary Cache:** Gold shimmer, ornate

**Cover Objects:**
- Concrete barriers (full cover)
- Wooden crates (half cover)
- Metal drums
- Vehicles (varied states)
- Sandbags

**Interactive Objects:**
- Doors (sliding, hinged)
- Switches
- Computers
- Elevators (future)

---

### Prop Specifications

**High-Detail Props:**
- Hero loot containers: 2,000-3,000 tris
- Vehicles: 5,000-10,000 tris
- Large machinery: 3,000-5,000 tris

**Medium Props:**
- Cover objects: 500-1,500 tris
- Furniture: 300-800 tris
- Debris: 100-500 tris

**Low-Detail Props:**
- Small items: 50-200 tris
- Clutter: 20-100 tris

---

## VFX & Particle Effects

### Combat Effects

**Muzzle Flashes:**
- Bright, instant burst
- Color: Orange-yellow
- Size varies by weapon type
- Smoke trail

**Bullet Impacts:**
- Material-specific (sparks on metal, dust on concrete)
- Decals (bullet holes)
- Small particle burst
- Audio-visual sync

**Blood Effects:**
- Minimal, stylized (rating considerations)
- Red particle spray
- Small decal
- Quick fade

**Explosions:**
- Fireball center
- Smoke plume
- Debris particles
- Screen shake
- Light flash

---

### Ability Effects

**Combat Stim (Assault):**
- Orange energy outline on character
- Speed lines
- Pulsing aura
- Screen vignette (first-person view)

**Healing Drone (Support):**
- Green floating drone
- Healing particles (downward)
- Soft glow
- Holographic health cross

**UAV Scan (Recon):**
- Blue radar pulse wave (expanding circle)
- Sonar effect
- Enemy highlights
- Minimap update flash

**Riot Shield (Tank):**
- Transparent blue shield
- Energy flicker on edges
- Impact cracks (when hit)
- Deployment animation

**EMP Blast (Specialist):**
- Blue electric sphere
- Lightning arcs
- Screen static (enemies hit)
- Tech shutdown visuals

---

### Environmental Effects

**Weather:**
- Rain: Falling particles, puddle ripples, wet surfaces
- Fog: Volumetric fog, reduced visibility
- Sandstorm: Brown particle swirl, wind audio

**Contamination:**
- Red/green toxic fog
- Particle density
- Screen vignette
- Damage number popup

**Fire:**
- Flickering flames
- Smoke column
- Heat distortion
- Embers

---

### Effect Budget (Mobile)

**Max Simultaneous Particles:**
- Low-end: 500 particles
- Mid-range: 1,500 particles
- High-end: 3,000 particles

**Optimization:**
- Particle pooling
- Distance-based culling
- LOD for effects
- Simple materials

---

## UI Art Style

### Visual Style
- Clean, modern military interface
- Semi-transparent panels
- Sharp edges, minimal curves
- Futuristic tactical aesthetic

### UI Elements

**Buttons:**
**Buttons:**
- Dark background with bright borders
- Hover: Glow effect
- Press: Color shift
- Icon + text combo

**Panels:**
- 80% opacity dark background
- Cyan accent borders
- Drop shadow
- Blur background (mobile-optimized)

**Health Bars:**
- Segmented (chunky pixels)
- Red base
- Animated depletion
- Damage flash (white)

**Icons:**
- Line art style
- Consistent stroke width (3-4px)
- Color fills for categories
- Readable at small sizes (64x64px minimum)

---

## Animation Guidelines

### Character Animations

**Movement:**
- Walk: 1.0 sec loop, medium pace
- Sprint: 0.7 sec loop, fast
- Crouch Walk: 1.3 sec loop, slow
- Idle: 3 sec loop with subtle breathing

**Combat:**
- Fire weapon: 0.1-0.3 sec (weapon-dependent)
- Reload: 1.5-3.0 sec (weapon-dependent)
- Melee attack: 0.5 sec
- Hit reaction: 0.2 sec

**Abilities:**
- Ability activate: 0.5-1.0 sec
- Ability loop (if persistent)
- Ability deactivate: 0.3 sec

**Death:**
- Death animation: 1.0 sec
- Ragdoll transition: 0.3 sec
- Body fade (after looting): 3 sec fade

---

### Camera & Camera Shake

**Default Camera:**
- Top-down isometric (45° angle)
- Height: 1500-2000 units above player
- Follow smoothing: 0.3 sec lag

**Camera Shake:**
- Weapon fire: Minimal (1-2 units)
- Explosion near: Medium (5-10 units)
- Ability use: Light (2-3 units)
- Death: Heavy (10-15 units)

---

## Performance Art Guidelines

### Mobile Optimization

**Polygon Budget:**
- On-screen total: < 2M triangles
- Per character: 15K-25K tris
- Per weapon: 2K-4K tris
- Environment props: Varies by type

**Texture Memory:**
- Total budget: < 800MB (mid-range)
- Character: 2048x2048
- Environment: 2048x2048 (tiled), 512x512 (props)
- UI: 1024x1024 (atlased)

**Draw Calls:**
- Target: < 2000 draw calls
- Technique: Texture atlasing, instancing
- LOD system: 3 levels minimum

**Shader Complexity:**
- Mobile-optimized shaders only
- Minimize texture samples (< 4 per shader)
- Avoid complex math
- Use vertex colors cho variation

---

## Style References

**Games:**
- The Division (UI, realistic gear)
- Escape from Tarkov (weapon detail, gritty)
- PUBG Mobile (mobile optimization)
- Gears Tactics (top-down combat)

**Visual Media:**
- Industrial photography
- Urban exploration (abandoned places)
- Military gear catalogs
- Post-apocalyptic films

---

## Art Asset Pipeline

**Modeling:**
1. Concept art approval
2. Blockout (proportions)
3. High-poly sculpt (ZBrush/Blender)
4. Low-poly retopology
5. UV unwrapping
6. Baking (normal, AO, curvature)

**Texturing:**
1. Base materials (Substance Painter)
2. Weathering and details
3. Export PBR maps
4. Engine integration
5. Optimization

**Implementation:**
1. Import to UE5
2. Material setup
3. LOD generation
4. Collision
5. Testing

**Approval:**
1. Art lead review
2. Technical check (performance)
3. In-game lighting test
4. Final approval

---

## Outsourcing Guidelines

**When Outsourcing:**
- Provide detailed art bible
- Reference images
- Technical specs document
- Review milestones (blockout, high-poly, final)

**What to Outsource:**
- Environment props (bulk)
- Weapon models
- Character skins (cosmetics)
- VFX (simple effects)

**Keep In-House:**
- Hero characters
- Key environment pieces
- UI design
- Art direction decisions

---

## Art Team Tools

**3D Software:**
- Primary: Blender (free, powerful)
- Sculpting: ZBrush
- Texturing: Substance Painter
- Rigging: Maya/Blender

**2D Software:**
- Concept: Photoshop/Procreate
- UI: Figma/Adobe XD
- Icons: Illustrator

**Engine:**
- Unreal Engine 5
- Version control: Git LFS for assets



