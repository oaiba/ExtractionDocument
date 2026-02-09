# Asset Guidelines

**[← Back to Style Guide](./StyleGuide.md)** | **[Index](../README.md)** | **[Next: User Interface →](./UserInterface.md)**

---

## 📋 Asset Naming Convention

### Folder Structure

```
Assets/
├── Characters/
│   ├── Operators/
│   │   ├── SK_Operator_Assault.fbx
│   │   ├── T_Operator_Assault_D.png
│   │   └── ...
│   ├── Enemies/
│   └── NPCs/
├── Weapons/
│   ├── AssaultRifles/
│   ├── SMGs/
│   └── ...
├── Environment/
│   ├── Industrial/
│   ├── Urban/
│   └── Props/
├── VFX/
└── UI/
```

### Naming Pattern

```
[Prefix]_[Category]_[Name]_[Variant]_[Suffix]

Prefixes:
SK_ = Skeletal Mesh
SM_ = Static Mesh
T_  = Texture
M_  = Material
MI_ = Material Instance
A_  = Animation
S_  = Sound
P_  = Particle/Niagara
WBP_= Widget Blueprint
BP_ = Blueprint

Suffixes (Textures):
_D  = Diffuse/Base Color
_N  = Normal Map
_R  = Roughness
_M  = Metallic
_AO = Ambient Occlusion
_E  = Emissive
_MSK= Mask (combined channels)
```

**Examples:**
```
SK_Operator_Assault_Male.fbx
T_Operator_Assault_Male_D.png
SM_Weapon_AR_AK47.fbx
T_Weapon_AR_AK47_D.png
SM_Prop_Crate_Military_A.fbx
```

---

## 👤 Character Asset Specifications

### Operator Models

**Polygon Budget:**
```
┌─────────────────────────────────────────────┐
│ Component       │ Low LOD │ Mid LOD │ High  │
├─────────────────────────────────────────────┤
│ Body Base       │ 4,000   │ 8,000   │ 12,000│
│ Head            │ 1,500   │ 2,500   │ 4,000 │
│ Armor/Gear      │ 2,000   │ 4,000   │ 6,000 │
│ Accessories     │ 500     │ 1,000   │ 2,000 │
│ Backpack        │ 300     │ 600     │ 1,000 │
├─────────────────────────────────────────────┤
│ TOTAL           │ 8,300   │ 16,100  │ 25,000│
└─────────────────────────────────────────────┘
```

**Texture Specifications:**
```
┌─────────────────────────────────────────────┐
│ Map Type        │ Resolution │ Format      │
├─────────────────────────────────────────────┤
│ Base Color      │ 2048x2048  │ BC1 (DXT1)  │
│ Normal          │ 2048x2048  │ BC5         │
│ ORM (AO/R/M)    │ 2048x2048  │ BC1         │
│ Emissive (opt)  │ 1024x1024  │ BC1         │
└─────────────────────────────────────────────┘
```

**Skeleton Requirements:**
```
Base: UE5 Mannequin compatible
Bones: 70-80 total
  - Spine: 4 bones
  - Arms: 3 bones each + hand (15 bones)
  - Legs: 4 bones each + foot (5 bones)
  - Neck/Head: 3 bones
  - Accessories: 5-10 extra bones

IK Setup: Required for weapon handling
Physics: Cloth simulation for pouches/straps
```

### Operator LOD Settings

| LOD  | Distance | Triangles | Use Case      |
| :--- | :------- | :-------- | :------------ |
| LOD0 | 0-50m    | 25,000    | Player, close |
| LOD1 | 50-100m  | 16,000    | Mid range     |
| LOD2 | 100-200m | 8,000     | Far           |
| LOD3 | 200m+    | 3,000     | Distant       |

---

### Enemy AI Models

**Standard Enemy:**
```
Polygon Budget: 8,000 - 12,000 tris
Texture: 1024x1024 (shared atlas preferred)
Bones: 50-60
Animation Set: Shared with Operators (retarget)
```

**Elite Enemy:**
```
Polygon Budget: 12,000 - 18,000 tris
Texture: 2048x2048
Bones: 65-75
Unique visual elements required
```

**Boss Enemy:**
```
Polygon Budget: 20,000 - 35,000 tris
Texture: 2048x2048 (unique)
Bones: 70-90 (extra for unique animations)
Special VFX attachments
```

---

## 🔫 Weapon Asset Specifications

### Weapon Models

**Polygon Budget by Category:**
```
┌─────────────────────────────────────────────┐
│ Weapon Type     │ Triangles  │ Attachments │
├─────────────────────────────────────────────┤
│ Pistol          │ 1,500-2,500│ +500 max    │
│ SMG             │ 2,000-3,000│ +800 max    │
│ Assault Rifle   │ 3,000-4,000│ +1,000 max  │
│ Shotgun         │ 2,500-3,500│ +800 max    │
│ Sniper Rifle    │ 3,500-4,500│ +1,200 max  │
│ LMG             │ 4,000-5,000│ +1,000 max  │
│ Melee           │ 800-1,500  │ N/A         │
└─────────────────────────────────────────────┘
```

**Modular Setup:**
```
Every weapon = Base + Attachments

Attachment Slots:
├── Slot_Optic     (Top rail)
├── Slot_Muzzle    (Barrel end)
├── Slot_Underbarrel (Bottom rail)
├── Slot_Magazine  (Fixed position)
└── Slot_Stock     (Rear, if applicable)

Sockets required in skeleton:
- Muzzle_Flash (for VFX)
- Ejection_Port (for shell casings)
- Magazine_Eject (for reload)
```

**Texture Specifications:**
```
Resolution: 1024x1024 per weapon
Maps: Base Color, Normal, ORM
Skin Support: Material parameter switching
Wear Levels: Vertex color channel (R = wear)
```

### Attachment Models

```
┌─────────────────────────────────────────────┐
│ Attachment Type │ Triangles  │ Texture     │
├─────────────────────────────────────────────┤
│ Red Dot Sight   │ 200-400    │ Shared atlas│
│ Holographic     │ 300-500    │ Shared atlas│
│ Scope (4x+)     │ 500-800    │ Shared atlas│
│ Suppressor      │ 200-400    │ Shared atlas│
│ Foregrip        │ 150-300    │ Shared atlas│
│ Laser           │ 100-200    │ Shared atlas│
│ Extended Mag    │ 100-200    │ Shared atlas│
└─────────────────────────────────────────────┘

Total Attachment Atlas: 1024x1024 (all attachments)
```

---

## 🏗️ Environment Asset Specifications

### Building Exteriors

**Modular Building System:**
```
Grid Size: 4m x 4m modules
Height: 3.5m per floor

Module Types:
├── Wall_Solid (no opening)
├── Wall_Window (standard window)
├── Wall_Door (door frame)
├── Wall_Damaged (hole/destruction)
├── Corner_Internal
├── Corner_External
├── Floor_Standard
├── Ceiling_Standard
└── Roof_Variants
```

**Polygon Budget (per module):**
```
Wall Module:    200-500 tris
Floor/Ceiling:  100-300 tris
Decoration:     100-400 tris per piece
```

**Texture Atlasing:**
```
Industrial Atlas:  2048x2048 (tiled)
Urban Atlas:       2048x2048 (tiled)
Detail Atlas:      1024x1024 (decals)
```

### Props & Objects

**Hero Props (High Detail):**
```
Loot Container (Legendary):
├── Triangles: 2,000-3,000
├── Texture: 1024x1024
├── Materials: 2 (base + emissive)
├── VFX: Particle attachment
└── Animation: Open/Close

Vehicles:
├── Triangles: 5,000-10,000
├── Texture: 2048x2048
├── Destruction states: 3 variants
└── LODs: 4 levels
```

**Standard Props:**
```
Crates/Boxes:     300-600 tris
Barrels/Drums:    200-400 tris
Furniture:        300-800 tris
Equipment:        200-500 tris
Small Debris:     50-150 tris
```

**Vegetation:**
```
Trees:            2,000-4,000 tris (billboard at distance)
Bushes:           500-1,000 tris
Grass:            Instanced mesh, 10-30 tris per blade
Vines/Overgrowth: 200-500 tris (decal + mesh combo)
```

### Cover Objects

**Cover Classification:**
```
┌─────────────────────────────────────────────┐
│ Cover Type  │ Height │ Protection │ Tris   │
├─────────────────────────────────────────────┤
│ Full        │ 1.5m+  │ 100%       │ 500+   │
│ Half        │ 0.7-1.5│ 60%        │ 300-500│
│ Soft        │ Any    │ 30%        │ 200-400│
│ None        │ <0.5m  │ 0%         │ <200   │
└─────────────────────────────────────────────┘

Cover objects MUST have:
- Clear collision shape
- Appropriate material response
- Destruction state (if applicable)
```

---

## 🎭 Animation Guidelines

### Character Animation Specs

**Locomotion Set:**
```
┌─────────────────────────────────────────────┐
│ Animation        │ Frames │ Loop │ Priority│
├─────────────────────────────────────────────┤
│ Idle_Unarmed     │ 90     │ Yes  │ Low     │
│ Idle_Rifle       │ 90     │ Yes  │ Low     │
│ Walk_Forward     │ 30     │ Yes  │ Med     │
│ Walk_Backward    │ 30     │ Yes  │ Med     │
│ Walk_Left        │ 30     │ Yes  │ Med     │
│ Walk_Right       │ 30     │ Yes  │ Med     │
│ Run_Forward      │ 20     │ Yes  │ High    │
│ Sprint           │ 15     │ Yes  │ High    │
│ Crouch_Idle      │ 60     │ Yes  │ Med     │
│ Crouch_Walk      │ 40     │ Yes  │ Med     │
└─────────────────────────────────────────────┘
```

**Combat Animations:**
```
┌─────────────────────────────────────────────┐
│ Animation        │ Frames │ Blend │ Notes  │
├─────────────────────────────────────────────┤
│ Fire_Rifle       │ 8      │ Add   │ Upper  │
│ Fire_Pistol      │ 6      │ Add   │ Upper  │
│ Reload_Rifle     │ 60-90  │ Full  │ Events │
│ Reload_Pistol    │ 45     │ Full  │ Events │
│ Melee_Attack     │ 20     │ Full  │ Combo  │
│ Throw_Grenade    │ 40     │ Full  │ Release│
│ Hit_React_Light  │ 15     │ Add   │ Random │
│ Hit_React_Heavy  │ 25     │ Full  │ Stagger│
│ Death_Front      │ 45     │ Full  │ Ragdoll│
│ Death_Back       │ 45     │ Full  │ Ragdoll│
└─────────────────────────────────────────────┘
```

**Animation Events Required:**
```
Reload Animations:
├── Event: MagOut (magazine detach)
├── Event: MagIn (magazine attach)
├── Event: BoltPull (if applicable)
└── Event: Ready (weapon ready)

Melee Animations:
├── Event: DamageStart
├── Event: DamageEnd
└── Event: CanCombo

Death Animations:
├── Event: RagdollStart
└── Event: LootableStart
```

---

## ⚡ VFX Asset Specifications

### Particle System Limits

**Per-Effect Budget:**
```
Combat Effects:
├── Muzzle Flash:   50 particles, 0.1s lifetime
├── Bullet Impact:  20 particles, 0.5s lifetime
├── Blood Splatter: 15 particles, 0.3s lifetime
└── Explosion:      200 particles, 1.5s lifetime

Environmental Effects:
├── Smoke:          100 particles, 3s lifetime
├── Fire:           150 particles, continuous
├── Rain:           500 particles, continuous (pooled)
└── Dust:           50 particles, 2s lifetime
```

**Texture Specifications:**
```
Particle Sprites: 256x256 max (atlased)
Flipbooks: 512x512 max, 4x4 or 8x8 frames
Format: BC4 (grayscale) or BC1 (color)
```

### Material Guidelines

**Effect Materials:**
```
Max texture samples: 2 per material
Shader complexity: Simple (mobile target)
Blend mode: Additive (most), Translucent (smoke)
Soft particles: Required for all
```

---

## 📦 LOD Requirements

### Standard LOD Settings

**Characters:**
```
LOD0: 100% triangles, 0-50 units
LOD1: 65% triangles, 50-100 units
LOD2: 35% triangles, 100-200 units
LOD3: 15% triangles, 200+ units
Cull: 500+ units
```

**Props:**
```
LOD0: 100% triangles, 0-30 units
LOD1: 50% triangles, 30-80 units
LOD2: 25% triangles, 80-150 units
Cull: 200+ units (small props), 400+ (large)
```

**Buildings:**
```
LOD0: Full detail, 0-100 units
LOD1: Simplified geometry, 100-200 units
LOD2: Billboard/Impostor, 200+ units
```

---

## 🔧 Import Settings (UE5)

### Static Meshes
```yaml
Import Settings:
  Auto Generate Collision: false
  Combine Meshes: false
  Generate Lightmap UVs: true
  
Build Settings:
  Distance Field Resolution: 1.0
  Nanite: Enabled (high detail assets only)
```

### Skeletal Meshes
```yaml
Import Settings:
  Import Morph Targets: false
  Update Skeleton Reference: true
  Import Mesh LODs: true
  
Animation Settings:
  Animation Length: Exported Time
  Frame Range: Custom (0-end)
  Sampling Rate: 30 FPS
```

### Textures
```yaml
Compression:
  Base Color: Default (DXT1)
  Normal Map: Normalmap (BC5)
  Masks: Masks (no sRGB)
  
Settings:
  sRGB: true (Base Color only)
  Mip Gen Settings: NoMipmaps (UI), FromTextureGroup (3D)
  LOD Bias: 0
```

---

## ✅ Quality Checklist

### Before Submission

**Model Checklist:**
- [ ] Correct naming convention
- [ ] Polygon count within budget
- [ ] Clean topology (no N-gons, no floating verts)
- [ ] Proper UV layout (no overlapping for lightmaps)
- [ ] Origin point at logical location
- [ ] Scale matches world units (1 unit = 1 cm)
- [ ] LODs generated and tested

**Texture Checklist:**
- [ ] Correct resolution
- [ ] Power of 2 dimensions
- [ ] No visible seams
- [ ] Consistent texel density
- [ ] All maps exported (D, N, ORM)
- [ ] sRGB settings correct

**Animation Checklist:**
- [ ] Root motion correct (if applicable)
- [ ] Animation events placed
- [ ] Blend transitions smooth
- [ ] No foot sliding
- [ ] Loops seamless

---

## 📊 Asset Budget Summary

### Per-Scene Budget (Mobile Target)

```
┌─────────────────────────────────────────────┐
│ Category            │ Budget    │ Priority │
├─────────────────────────────────────────────┤
│ Characters (visible)│ 300K tris │ High     │
│ Weapons (visible)   │ 50K tris  │ High     │
│ Environment Props   │ 800K tris │ Medium   │
│ Vegetation          │ 400K tris │ Low      │
│ VFX                 │ 200K tris │ Medium   │
├─────────────────────────────────────────────┤
│ TOTAL ON-SCREEN     │ 1.75M tris│          │
└─────────────────────────────────────────────┘

Texture Memory: < 800MB (mid-range device)
Draw Calls: < 2000
```

---

**[← Back to Style Guide](./StyleGuide.md)** | **[Index](../README.md)** | **[Next: User Interface →](./UserInterface.md)**
