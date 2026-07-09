---
title: "Asset Guidelines"
type: docs
weight: 3
---

## Asset Naming Convention

### Folder Structure

```
Content/
├── Characters/
│   ├── Operators/
│   │   ├── SK_Operator_Assault_Male.uasset
│   │   ├── T_Operator_Assault_Male_D.uasset
│   │   └── ...
│   ├── Enemies/
│   └── NPCs/
├── Weapons/
│   ├── AssaultRifles/
│   ├── SMGs/
│   ├── Shotguns/
│   ├── SniperRifles/
│   ├── Pistols/
│   └── Melee/
├── Environment/
│   ├── Industrial/
│   ├── Urban/
│   ├── Military/
│   ├── Nature/
│   ├── Underground/
│   └── Props/
├── VFX/
│   ├── Combat/
│   ├── Abilities/
│   ├── Environmental/
│   └── Cyberpunk/          (glitch, neon, holographic effects)
├── UI/
│   ├── HUD/
│   ├── Menus/
│   ├── Icons/
│   └── Common/
└── Audio/
```

### Naming Pattern

```
[Prefix]_[Category]_[Name]_[Variant]_[Suffix]

Prefixes:
SK_  = Skeletal Mesh
SM_  = Static Mesh
T_   = Texture
M_   = Material
MI_  = Material Instance
A_   = Animation
S_   = Sound
NS_  = Niagara System
NE_  = Niagara Emitter
WBP_ = Widget Blueprint
BP_  = Blueprint
DT_  = Data Table
DA_  = Data Asset

Suffixes (Textures):
_D   = Diffuse / Base Color
_N   = Normal Map
_R   = Roughness
_M   = Metallic
_AO  = Ambient Occlusion
_E   = Emissive
_MSK = Mask (combined channels)
_ORM = Combined AO + Roughness + Metallic
```

**Examples:**
```
SK_Operator_Assault_Male.fbx
T_Operator_Assault_Male_D.png
T_Operator_Assault_Male_E.png      (emissive for cyberpunk tech glow)
SM_Weapon_AR_AK74M.fbx
SM_Prop_Crate_Military_A.fbx
NS_VFX_Glitch_Terminal.uasset     (cyberpunk glitch effect)
MI_Neon_Sign_Orange.uasset
```

---

## nhân vật Asset Specifications

### Operator Models

**Cross-Platform Polygon Budget:**

| Component | Mobile (Low) | Console (Mid) | PC Ultra (High) |
| :-------- | :----------- | :------------ | :-------------- |
| Body Base | 6,000 | 10,000 | 16,000 |
| Head | 2,000 | 3,500 | 5,000 |
| giáp / Gear | 3,000 | 5,500 | 8,000 |
| Accessories | 800 | 1,500 | 3,000 |
| Backpack | 500 | 800 | 1,500 |
| **Total** | **12,300** | **21,300** | **33,500** |

<!-- REF_IMAGE: Operator model LOD comparison — showing the same nhân vật at Mobile, Console, và PC Ultra quality levels side-by-side -->

**Texture Specifications:**

| Map Type | Mobile | Console | PC Ultra | Format |
| :------- | :----- | :------ | :------- | :----- |
| Base Color | 1024x1024 | 2048x2048 | 4096x4096 | BC1 (DXT1) |
| Normal | 1024x1024 | 2048x2048 | 4096x4096 | BC5 |
| ORM (AO/R/M) | 1024x1024 | 2048x2048 | 2048x2048 | BC1 |
| Emissive | 512x512 | 1024x1024 | 2048x2048 | BC1 |

**Skeleton yêu cầu:**
```
Base:          UE5 Mannequin compatible
Total Bones:   70-80
  Spine:       4 bones
  Arms:        3 bones each + hand (15 bones per hand)
  Legs:        4 bones each + foot (5 bones per foot)
  Neck/Head:   3 bones
  Accessories: 5-10 extra bones (pouches, antenna, tech devices)

IK Setup:      Required for weapon handling
Physics:       Cloth sim on pouches/straps (PC/Console)
               Baked cloth on Mobile
Facial Rig:    Optional (cinematics only)
```

### Operator LOD Settings

| LOD | Distance | Triangles (PC) | Triangles (Mobile) | cách dùng Case |
| :-- | :------- | :------------- | :----------------- | :------- |
| LOD0 | 0-50 units | 33,500 | 12,300 | người chơi, close |
| LOD1 | 50-100 units | 21,000 | 8,000 | Mid range |
| LOD2 | 100-200 units | 12,000 | 5,000 | Far |
| LOD3 | 200+ units | 5,000 | 2,500 | Distant |
| Cull | 500+ units | — | — | Not rendered |

### địch AI Models

**Standard địch:**

| Property | Mobile | Console | PC Ultra |
| :------- | :----- | :------ | :------- |
| Poly Budget | 8,000-10,000 | 12,000-15,000 | 15,000-20,000 |
| Texture | 1024x1024 (shared atlas) | 1024x1024 (shared atlas) | 2048x2048 |
| Bones | 50-60 | 50-60 | 50-60 |
| Animation Set | shared với operators (retarget) | Same | Same |

**Elite địch:**

| Property | Mobile | Console | PC Ultra |
| :------- | :----- | :------ | :------- |
| Poly Budget | 10,000-14,000 | 15,000-18,000 | 18,000-25,000 |
| Texture | 1024x1024 | 2048x2048 | 2048x2048 |
| Bones | 60-70 | 60-70 | 65-75 |
| Unique Elements | Required (cybernetic augmentations hiển thị rõ) | Same | Same |

**Boss địch:**

| Property | Mobile | Console | PC Ultra |
| :------- | :----- | :------ | :------- |
| Poly Budget | 18,000-25,000 | 30,000-40,000 | 40,000-55,000 |
| Texture | 2048x2048 | 2048x2048 | 4096x4096 (unique) |
| Bones | 70-80 | 70-90 | 80-100 |
| Special | VFX attachments, energy shield mesh, unique animations | Same | Same |

---

## vũ khí Asset Specifications

### vũ khí Models

**Cross-Platform Polygon Budget by Category:**

| vũ khí Type | Mobile | Console | PC Ultra | Attachment Budget |
| :---------- | :----- | :------ | :------- | :---------------- |
| Pistol | 1,500 | 2,500 | 4,000 | +800 max |
| SMG | 2,000 | 3,500 | 5,000 | +1,200 max |
| Assault Rifle | 3,000 | 4,500 | 6,500 | +1,500 max |
| Shotgun | 2,500 | 4,000 | 5,500 | +1,200 max |
| Sniper Rifle | 3,500 | 5,000 | 7,000 | +1,800 max |
| LMG | 4,000 | 5,500 | 7,500 | +1,500 max |
| Melee | 800 | 1,500 | 2,500 | N/A |

**Modular Setup:**
```
Every weapon = Base Mesh + Attachment Slots

Attachment Slots:
├── Slot_Optic       (Top rail — scope, red dot, holographic)
├── Slot_Muzzle      (Barrel end — suppressor, flash hider, compensator)
├── Slot_Underbarrel  (Bottom rail — foregrip, laser, bipod)
├── Slot_Magazine    (Fixed position — standard, extended, drum)
└── Slot_Stock       (Rear — folding, fixed, adjustable)

Required Sockets (for VFX/SFX):
├── Socket_Muzzle_Flash    (fire VFX origin)
├── Socket_Ejection_Port   (shell casing VFX)
├── Socket_Magazine_Eject  (reload animation)
└── Socket_LED_Indicator   (cyberpunk ammo counter position)
```

**Texture Specifications:**

| Property | Mobile | Console / PC |
| :------- | :----- | :----------- |
| Resolution | 1024x1024 | 2048x2048 |
| Maps | Base Color, Normal, ORM | Base Color, Normal, ORM, Emissive |
| Skin Support | Material parameter switching | Same + vertex color (R = wear level) |

### Attachment Models

| Attachment Type | Triangles | Texture | ghi chú |
| :-------------- | :-------- | :------ | :---- |
| Red Dot Sight | 200-400 | shared atlas (1024x1024) | Holographic reticle emissive |
| Holographic Sight | 300-500 | shared atlas | Emissive HUD window |
| Scope (4x+) | 500-800 | shared atlas | Lens reflection material |
| Suppressor | 200-400 | shared atlas | Matte black, heat discoloration |
| Foregrip | 150-300 | shared atlas | Ergonomic polymer |
| Laser Module | 100-200 | shared atlas | hiển thị rõ beam effect (Niagara) |
| Extended Magazine | 100-200 | shared atlas | Digital round counter (emissive) |

---

## Environment Asset Specifications

### Modular Building hệ thống

```
Grid Size:     4m x 4m modules
Floor Height:  3.5m per floor

Module Types:
├── Wall_Solid           (no opening)
├── Wall_Window          (standard window — glass breakable state)
├── Wall_Window_Neon     (window + neon sign mounting point)
├── Wall_Door            (door frame — sliding or hinged)
├── Wall_Damaged         (destruction hole, rebar exposed)
├── Wall_TechPanel       (cyberpunk wall with screen/LED strip)
├── Corner_Internal
├── Corner_External
├── Floor_Standard
├── Floor_TechGrate      (see-through floor grating with LED under-glow)
├── Ceiling_Standard
├── Ceiling_Pipes        (exposed pipe network, dripping)
└── Roof_Variants        (flat, angled, damaged)
```

**Polygon Budget (per module):**

| Module Type | Mobile | Console / PC |
| :---------- | :----- | :----------- |
| Wall Module | 200-400 | 400-600 |
| Wall_TechPanel | 300-500 | 500-800 |
| Floor/Ceiling | 100-250 | 200-400 |
| Decoration | 100-300 each | 200-500 each |

**Texture Atlasing:**

| Atlas | Resolution | Content |
| :---- | :--------- | :------ |
| Industrial Atlas | 2048x2048 (tiled) | Metal, rust, concrete, pipe |
| Urban Atlas | 2048x2048 (tiled) | Brick, glass, asphalt, paint |
| Tech Atlas | 2048x2048 (tiled + emissive) | màn hình, LED strips, panels, cables |
| chi tiết Decal Atlas | 1024x1024 | Graffiti, signs, damage, stains |
| Neon Sign Atlas | 1024x1024 (emissive) | Sign shapes, text, faction logos |

### Props và Objects

**Hero Props (High chi tiết):**
```
Legendary Loot Container:
├── Triangles: 2,000-4,000 (Console/PC), 1,500-2,500 (Mobile)
├── Texture: 1024x1024 (unique)
├── Materials: 2 (base + emissive for holographic lock)
├── VFX: Particle attachment (gold glow + trail)
└── Animation: Open/Close + holographic display activation

Vehicles:
├── Triangles: 5,000-12,000 (Console/PC), 3,000-6,000 (Mobile)
├── Texture: 2048x2048 (Console/PC), 1024x1024 (Mobile)
├── Destruction States: 3 variants (intact, damaged, wrecked)
├── Hazard Lights: Emissive material, blinking (active on some)
└── LODs: 4 levels
```

**Standard Props:**

| Prop Category | Mobile Tris | Console/PC Tris |
| :------------ | :---------- | :-------------- |
| Crates / Boxes | 200-400 | 400-800 |
| Barrels / Drums | 150-300 | 300-500 |
| Furniture | 200-600 | 400-1,000 |
| Equipment | 150-400 | 300-600 |
| Small Debris | 30-100 | 50-200 |
| Neon Signs | 100-200 | 200-400 (+ emissive) |
| Vending Machines | 400-600 | 600-1,000 (+ màn hình emissive) |
| Terminals / màn hình | 200-400 | 400-600 (+ emissive) |

**Vegetation:**

| Type | Mobile | Console/PC | ghi chú |
| :--- | :----- | :--------- | :---- |
| Trees | 1,500-3,000 | 3,000-5,000 | Billboard at 200+ units |
| Bushes | 400-800 | 800-1,200 | Instanced, wind sway |
| Grass | 8-20 tris/blade | 10-30 tris/blade | Instanced mesh, GPU-driven |
| Vines / Overgrowth | 150-300 | 300-600 | Decal + mesh combo |

### Cover Objects

| Cover Type | Height | Protection | Poly Budget | Destructible |
| :--------- | :----- | :--------- | :---------- | :----------- |
| Full (concrete wall) | 1.5m+ | 100% | 400-800 | No |
| Half (crates, sandbags) | 0.7-1.5m | 60% | 250-500 | Some |
| Soft (foliage, thin walls) | Any | 30% | 150-400 | Yes |
| None (low debris) | <0.5m | 0% | 50-200 | N/A |

**Cover objects must have:**
- rõ collision shape matching visual
- Material-appropriate impact response (sparks on metal, dust on concrete)
- Destruction trạng thái nếu applicable (với debris mesh)
- nhất quán visual language — cover objects cách dùng neutral tones to avoid confusion với interactive items

---

## Animation Guidelines

### nhân vật Animation Specifications

**Locomotion Set:**

| Animation | Frames | Loop | Priority | Blend |
| :-------- | :----- | :--- | :------- | :---- |
| Idle_Unarmed | 90 | Yes | Low | — |
| Idle_Rifle | 90 | Yes | Low | — |
| Walk_Forward | 30 | Yes | Medium | Directional |
| Walk_Backward | 30 | Yes | Medium | Directional |
| Walk_Left | 30 | Yes | Medium | Directional |
| Walk_Right | 30 | Yes | Medium | Directional |
| Run_Forward | 20 | Yes | High | Blend Space |
| Sprint | 15 | Yes | High | Blend Space |
| Crouch_Idle | 60 | Yes | Medium | — |
| Crouch_Walk | 40 | Yes | Medium | Blend Space |

**Combat Animations:**

| Animation | Frames | Blend Type | ghi chú |
| :-------- | :----- | :--------- | :---- |
| Fire_Rifle | 8 | Additive (upper) | hiển thị rõ recoil from top-down |
| Fire_Pistol | 6 | Additive (upper) | Snap recoil |
| Reload_Rifle | 60-90 | Full body | MagOut, MagIn, BoltPull events |
| Reload_Pistol | 45 | Full body | SlideRelease event |
| Melee_Attack | 20 | Full body | Combo chain (CanCombo event) |
| Throw_Grenade | 40 | Full body | Release at frame 25 |
| Hit_React_Light | 15 | Additive | Randomized direction variants |
| Hit_React_Heavy | 25 | Full body | Stagger với recovery |
| Death_Front | 45 | Full body | RagdollStart at frame 30 |
| Death_Back | 45 | Full body | RagdollStart at frame 30 |

**Required Animation Events:**
```
Reload Animations:
├── Event: MagOut       (magazine detach — sound + VFX)
├── Event: MagIn        (magazine attach — sound + snap)
├── Event: BoltPull     (if applicable — charging handle)
└── Event: Ready        (weapon ready to fire)

Melee Animations:
├── Event: DamageStart  (hitbox activation)
├── Event: DamageEnd    (hitbox deactivation)
└── Event: CanCombo     (input window for chain)

Death Animations:
├── Event: RagdollStart (physics takeover)
└── Event: LootableStart (body becomes interactable)
```

---

## VFX Asset Specifications

### Particle hệ thống Limits

**Per-Effect Budget:**

| Effect | Max Particles | Lifetime | Texture |
| :----- | :------------ | :------- | :------ |
| Muzzle Flash | 50 | 0.1s | 256x256 sprite |
| Bullet Impact | 20 | 0.5s | 256x256 sprite |
| Blood Splatter | 15 | 0.3s | 256x256 sprite |
| Explosion | 200 | 1.5s | 512x512 flipbook |
| Smoke | 100 | 3.0s | 512x512 flipbook |
| Fire | 150 | Continuous | 512x512 flipbook |
| Rain | 500 | Continuous (pooled) | 128x128 streak |
| Dust | 50 | 2.0s | 256x256 sprite |
| Digital Glitch | 30 | 0.5s | 256x256 (RGB split) |
| Neon Trail | 20 | 1.5s | 128x128 gradient |
| Holographic | 40 | Continuous | 512x512 (scan lines) |

**VFX Material Rules:**

| Platform | Max Texture Samples | Shader Complexity | Blend Mode |
| :------- | :------------------ | :---------------- | :--------- |
| Mobile | 2 per material | Simple (no complex math) | Additive hoặc Translucent |
| Console | 4 per material | Standard PBR | Any |
| PC Ultra | 6 per material | Full (distortion, refraction) | Any |

All particle effects must cách dùng **soft particles** (depth fade) to avoid hard clipping against geometry.

---

## LOD yêu cầu

### Standard LOD Settings

**nhân vật:**
```
LOD0:  100% triangles    |  0-50 units     |  Full detail + cloth sim
LOD1:   65% triangles    |  50-100 units   |  Reduced detail, no cloth
LOD2:   35% triangles    |  100-200 units  |  Simplified geometry
LOD3:   15% triangles    |  200+ units     |  Minimal silhouette
Cull:   —               |  500+ units     |  Not rendered
```

**Props:**
```
LOD0:  100% triangles    |  0-30 units     |  Full detail
LOD1:   50% triangles    |  30-80 units    |  Reduced
LOD2:   25% triangles    |  80-150 units   |  Simplified
Cull:  Small props 200+  |  Large 400+     |  Not rendered
```

**Buildings:**
```
LOD0:  Full detail       |  0-100 units    |  All modules visible
LOD1:  Simplified mesh   |  100-200 units  |  Merged geometry
LOD2:  Billboard/Impostor|  200+ units     |  Flat card with baked image
```

**Nanite (PC Ultra Only):**
- enabled for hero environment assets và large props
- Not used for nhân vật, vũ khí, hoặc UI elements
- Nanite-enabled meshes do not need manual LODs
- Fallback LOD chain required for non-Nanite platforms

---

## UE5 Import Settings

### Static Meshes
```yaml
Import Settings:
  Auto Generate Collision: false
  Combine Meshes: false
  Generate Lightmap UVs: true
  
Build Settings:
  Distance Field Resolution: 1.0
  Nanite: Enabled (hero assets on PC only)
  Allow CPUAccess: false (unless needed for runtime modification)
```

### Skeletal Meshes
```yaml
Import Settings:
  Import Morph Targets: false
  Update Skeleton Reference: true
  Import Mesh LODs: true
  
Animation Settings:
  Animation Length: Exported Time
  Frame Range: Custom (0 to end)
  Sampling Rate: 30 FPS
  
Physics:
  Create Physics Asset: true (characters)
  Cloth Simulation: PC/Console only
```

### Textures
```yaml
Compression:
  Base Color: Default (DXT1/BC1)
  Normal Map: Normalmap (BC5)
  ORM Mask: Masks (no sRGB)
  Emissive: Default (DXT1/BC1)
  
Settings:
  sRGB: true (Base Color and Emissive only)
  Mip Gen Settings: NoMipmaps (UI textures), FromTextureGroup (3D)
  LOD Bias: 0 (PC), 1 (Console), 2 (Mobile)
  Virtual Texture: Enabled for large environment textures (PC)
```

---

## Quality checklist

### trước Submission

**Model checklist:**
- [ ] Correct naming convention (prefix, category, name, suffix)
- [ ] Polygon count within platform budget
- [ ] Clean topology (no N-gons, no floating vertices, no interior faces)
- [ ] Proper UV layout (no overlapping for lightmaps, nhất quán texel density)
- [ ] Origin point at logical location (center-bottom for nhân vật, center for props)
- [ ] Scale matches world units (1 unit = 1 centimeter)
- [ ] LODs generated và tested across all platform tiers
- [ ] Emissive areas defined for cyberpunk glow elements

**Texture checklist:**
- [ ] Correct resolution per platform tier
- [ ] Power of 2 dimensions
- [ ] No hiển thị rõ seams at UV edges
- [ ] nhất quán texel density across model
- [ ] All maps exported (Base Color, Normal, ORM, Emissive nếu applicable)
- [ ] sRGB settings correct per map type
- [ ] Emissive map correctly defines tech glow, LED, và neon areas

**Animation checklist:**
- [ ] Root motion correct (nếu applicable)
- [ ] All animation events placed và named correctly
- [ ] Blend transitions smooth between trạng thái
- [ ] No foot sliding in locomotion
- [ ] Loops seamless (first và last frame match)
- [ ] Tested in top-down camera — reads well from above

---

## Asset Budget Summary

### Per-Scene Budget

| Category | Mobile | Console | PC Ultra | Priority |
| :------- | :----- | :------ | :------- | :------- |
| nhân vật (hiển thị rõ) | 200K tris | 500K tris | 1M tris | High |
| vũ khí (hiển thị rõ) | 40K tris | 80K tris | 150K tris | High |
| Environment Props | 600K tris | 1.5M tris | 3M tris | Medium |
| Vegetation | 300K tris | 800K tris | 1.5M tris | Low |
| VFX | 100K tris | 300K tris | 500K tris | Medium |
| **Total On-màn hình** | **1.24M** | **3.18M** | **6.15M** | — |

**Memory Budgets:**

| Resource | Mobile | Console | PC Ultra |
| :------- | :----- | :------ | :------- |
| Texture VRAM | 400-600 MB | 1.2 GB | 2.0+ GB |
| Draw Calls | < 1,500 | < 3,000 | < 5,000 |
| Shader Complexity | 4 samples max | 8 samples max | Unlimited |
| Max Active Emitters | 8-15 | 30 | 50 |

<!-- REF_IMAGE: Performance comparison screenshot — showing the same scene rendered at Mobile Low, Console, và PC Ultra quality tiers -->
