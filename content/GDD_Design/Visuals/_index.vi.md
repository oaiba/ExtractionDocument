---
title: "Visuals & Art"
linkTitle: "Visuals"
type: docs
weight: 3
sidebar:
  open: false
---

## Art Direction

Visual identity là **Cyberpunk Neo-Industrial** - một bản lai giữa rendering bán thực tế và tỉ lệ cartoon được stylize (40% realistic, 60% stylized). Palette xoay quanh **cam, trắng, đen, và cyan**. Tất cả asset được author cho cross-platform delivery (PC, Console, Mobile) với các quality tier có thể scale.

### Trụ Cột Visual

| Trụ Cột | Ý Tưởng Cốt Lõi |
| :----- | :-------- |
| **Neon Decay** | Thế giới công nghiệp sụp đổ nơi công nghệ hấp hối vẫn tồn tại; bảng hiệu neon chớp tắt trên đống đổ nát, quảng cáo holographic lặp lại trên màn hình nứt |
| **Tactical Clarity** | Mọi element đọc được từ top-down: rim light cho player, glow theo rarity, hierarchy tương phản theo khoảng cách |
| **Stylized Grit** | Tỉ lệ nhân vật heroic với material PBR đáng tin; tactical gear có cá tính, không photorealism thuần |
| **Cross-Platform Scale** | Author ở PC Ultra, scale qua LOD chain; Mobile là một trong ba target, không phải sàn chất lượng |

---

## Tài Liệu

{{< cards >}}
  {{< card link="ArtDirection" title="Art Direction" icon="color-swatch" subtitle="Art pillar, brand palette, character/weapon/environment/VFX guideline, poly budget" >}}
  {{< card link="StyleGuide" title="Style Guide - Art Bible" icon="eye" subtitle="Visual pillar, master palette, lighting design, composition, mood board reference" >}}
  {{< card link="AssetGuidelines" title="Asset Guidelines" icon="cube" subtitle="Naming convention, cross-platform poly/texture budget, LOD, pipeline, quality checklist" >}}
  {{< card link="UserInterface" title="UI Visual Design" icon="template" subtitle="UI component, cyberpunk treatment, cross-platform control, screen wireframe" >}}
{{< /cards >}}

---

## Art Style Quick Reference

```
REALISTIC ------------------o--> STYLIZED
                            ^
                       Game Position
                  (40% Realistic, 60% Stylized)
```

**Brand Colors:**

| Color | Hex | Vai Trò |
| :---- | :-- | :--- |
| Signal Orange | #F97316 | Primary accent, warm neon, CTA button |
| Bone White | #F8FAFC | Text, clean surface, highlight |
| Void Black | #0A0A0B | Background, shadow, panel base |
| Tactical Cyan | #06B6D4 | Tech element, cool neon, secondary accent |

**Polygon Tiers (Operator Example):**

| Platform | Total Tris |
| :------- | :--------- |
| Mobile | 12,300 |
| Console | 21,300 |
| PC Ultra | 33,500 |
