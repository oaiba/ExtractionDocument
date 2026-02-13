---
title: "Networking"
linkTitle: "Networking"
type: docs
weight: 1
---

## 🌐 Networking & Replication

Technical implementation of multiplayer systems, synchronization, and latency management.

{{< cards cols="2" >}}
  {{< card link="../Core/NetworkingSystem" title="Networking Core" icon="server" subtitle="Architecture, session management, and EOS integration." >}}
  {{< card link="ReplicationStrategy" title="Replication Strategy" icon="refresh" subtitle="Actor replication, bandwidth optimization, and relevancy settings." >}}
  {{< card link="LagCompensation" title="Lag Compensation" icon="clock" subtitle="Client-side prediction, server reconciliation, and rewind techniques." >}}
{{< /cards >}}

---

### Networking Pillars

*   **Trust No One:** The client is untrusted; all critical actions are validated on the server.
*   **Responsive Feel:** Movement and shooting use client-side prediction to hide latency.
*   **Bandwidth Efficient:** Only replicate what is necessary, when it is relevant.
