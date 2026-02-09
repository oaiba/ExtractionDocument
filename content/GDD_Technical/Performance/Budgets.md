---
title: "Performance Budgets & Technical Constraints"
type: docs
---
# Performance Budgets & Technical Constraints

**[← Back to Index](../README.md)**

---

## 📈 Platform Targets

Each platform has strict resource limits. Failure to meet these means the feature will be **cut or simplified**.

| Metric | PC (Max / Recommend) | PS5 / Series X | Mobile (High-End) |
| :--- | :--- | :--- | :--- |
| **FPS Target** | Unlocked (144hz Ideal) | Solid 60 FPS | Solid 60 FPS (Vsync) |
| **Draw Calls** | ~5000 | ~3500 | ~1000 |
| **Triangle Count** | ~3,000,000 / Screen | ~2,000,000 / Screen | ~500,000 / Screen |
| **Texture Memory** | 8GB - 12GB | 8GB Max | 2GB Max |
| **Shader Complexity** | High (Ray Tracing) | Medium | Mobile Optimized |
| **Network B/W** | 60 KB/s Up/Down | 40 KB/s Up/Down | 20 KB/s Up/Down |

---

## 🎨 Asset Guidelines

### Character Models (LODs Required)
*   **LOD 0 (Cinematic):** 60k - 80k Tris
*   **LOD 1 (Close Gameplay):** 30k Tris
*   **LOD 2 (Mid Range):** 10k Tris
*   **LOD 3 (Distant):** 3k Tris (Mobile Max)

### Weapon Models (Detailed)
*   **First Person View (FPV):** 20k - 30k Tris (Detailed hands/gun)
*   **Third Person View (TPV):** 5k Tris (Attachments baked)
*   **Dropped Item:** 1k Tris (Simplified physics mesh)

### Environmental Props
*   **Loot Crates:** 1k - 2k Tris (Must be readable)
*   **Small Props (Bottles, Cans):** < 300 Tris
*   **Buildings (Modular Use):** Use Instances (HISM) for optimal draw calls.

---

## ⚡ Shader Complexity

### PC / Console
*   **Global Illumination:** Lumen (Software Ray Tracing) enabled.
*   **Reflections:** Screen Space Reflections (SSR) + LumenFallback.
*   **Translucency:** Use `Default Lit` sparingly. Prefer `Masked` where possible.
*   **Virtual Textures:** Enabled for Landscape and huge assets.

### Mobile Optimization
*   **Lighting:** Fully baked lighting (Static) for everything except Characters.
*   **Shadows:** 1 directional cascading shadow map. No point light shadows.
*   **Materials:** Unlit or Mobile Specular only. No complex PBR networks. Use specific Mobile Quality Switch nodes.
*   **Post Processing:** Minimal (Bloom only). Disable expensive effects like Depth of Field or Motion Blur.

---

## 💾 Memory Management

### Maximum Memory Footprint (RAM)
*   **PC:** 16GB Recommended (Game uses ~4-6GB)
*   **Console:** Fixed budget (Game uses ~8GB shared)
*   **Mobile:** 4GB Device (Game uses ~1.5GB Max)

### Streaming
*   **Level Streaming:** Use `World Partition` for open-world maps. Grid size: 256m x 256m.
*   **Texture Streaming:** Ensure MipMaps are generated for ALL textures. No exceptions.
*   **Audio Streaming:** Music and long SFX must be streamed. Gunshots and UI sounds must be in memory.

---

## 🚨 Performance Audit Checklist

Before checking in any asset or code, verify:

1.  [ ] **Does it work on Mobile?** (Test on device, not editor preview).
2.  [ ] **Is the Poly Count within budget?** based on screen size/importance.
3.  [ ] **Are all Textures power of 2?** (1024, 2048). No 1000x1000.
4.  [ ] **Does code run in Tick()?** If yes, have you profiled it (`stat unit`)?

---


