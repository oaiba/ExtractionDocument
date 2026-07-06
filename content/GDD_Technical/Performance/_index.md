---
title: "Performance"
linkTitle: "Performance"
type: docs
weight: 1
---

##  Performance & Optimization

Guidelines, budgets, and strategies for maintaining high framerates and memory efficiency on mobile devices.

{{< cards cols="2" >}}
  {{< card link="Budgets" title="Performance Budgets" icon="chart-bar" subtitle="Frame time, draw calls, poly counts, and texture memory limits." >}}
  {{< card link="Optimization" title="Optimization Guide" icon="lightning-bolt" subtitle="CPU/GPU profiling, LODs, HLODs, and material complexity." >}}
{{< /cards >}}

---

### Optimization Pillars

*   **Mobile First:** All assets are authored with mobile constraints in mind (lower poly, fewer bones).
*   **Early Profiling:** Performance is checked daily, not just at the end of the project.
*   **Strict Budgets:** Exceeding memory or draw call budgets requires technical director approval.
