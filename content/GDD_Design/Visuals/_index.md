---
title: "Visuals & Art"
linkTitle: "Visuals"
type: docs
weight: 3
sidebar:
  open: true
---

## Art Direction

The visual identity is **Cyberpunk Neo-Industrial** — a hybrid of semi-realistic rendering and stylized cartoon proportions (40% realistic, 60% stylized). The palette centers on **orange, white, black, and cyan**. All assets are authored for cross-platform delivery (PC, Console, Mobile) with scalable quality tiers.

### Visual Pillars

| Pillar | Core Idea |
| :----- | :-------- |
| **Neon Decay** | Collapsed industrial world where dying technology persists — neon signs flicker over ruins, holographic ads loop on cracked screens |
| **Tactical Clarity** | Every element readable from top-down: player rim lights, rarity-coded glow, contrast hierarchy by distance |
| **Stylized Grit** | Heroic proportions with realistic PBR materials — tactical gear with personality, not photorealism |
| **Cross-Platform Scale** | Author at PC Ultra, scale through LOD chains — Mobile is one target among three, not the floor |

---

## Documents

{{< cards >}}
  {{< card link="ArtDirection" title="Art Direction" icon="color-swatch" subtitle="Art pillars, brand palette, character/weapon/environment/VFX guidelines, poly budgets" >}}
  {{< card link="StyleGuide" title="Style Guide - Art Bible" icon="eye" subtitle="Visual pillars, master palette, lighting design, composition, mood board references" >}}
  {{< card link="AssetGuidelines" title="Asset Guidelines" icon="cube" subtitle="Naming conventions, cross-platform poly/texture budgets, LOD, pipeline, quality checklist" >}}
  {{< card link="UserInterface" title="UI Visual Design" icon="template" subtitle="UI components, cyberpunk treatment, cross-platform controls, screen wireframes" >}}
{{< /cards >}}

---

## Art Style Quick Reference

```
REALISTIC ──────────────────●──→ STYLIZED
                            ▲
                       Game Position
                  (40% Realistic, 60% Stylized)
```

**Brand Colors:**

| Color | Hex | Role |
| :---- | :-- | :--- |
| Signal Orange | #F97316 | Primary accent, warm neon, CTA buttons |
| Bone White | #F8FAFC | Text, clean surfaces, highlights |
| Void Black | #0A0A0B | Backgrounds, shadows, panel bases |
| Tactical Cyan | #06B6D4 | Tech elements, cool neon, secondary accent |

**Polygon Tiers (Operator Example):**

| Platform | Total Tris |
| :------- | :--------- |
| Mobile | 12,300 |
| Console | 21,300 |
| PC Ultra | 33,500 |
