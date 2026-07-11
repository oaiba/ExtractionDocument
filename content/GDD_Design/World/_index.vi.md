---
title: "World & Level Design"
linkTitle: World
type: docs
weight: 12
---

> \[!IMPORTANT] **Thông Báo Di Chuyển Thư Mục:** Tài liệu Story & World đã được gộp vào section thống nhất [**NarrativeWorld/**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/README.md). Các file map design và environmental narrative bên dưới được giữ để tham khảo, nhưng **GDD canonical và mới nhất** nằm trong `NarrativeWorld/`. Work mới nên được thực hiện ở đó.
>
> **Tài liệu canonical mới:** [Map Design Bible](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/MapBible/README.md) (gộp `MapDesign.md` + `EnvironmentalNarrative_Guidelines.md`), [Industrial Decay Map Lore](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/MapLore_Industrial/README.md), [Urban Ruins Map Lore](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/MapLore_Urban/README.md), [Faction Territories](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/NarrativeWorld/FactionTerritories/README.md).

### Map Là Nhân Vật Chính

Trong extraction shooter, hiểu biết về map là skill ceiling cao nhất. Level của chúng ta được thiết kế với **choke point**, **sniping lane**, và **flank route** cụ thể để buộc người chơi tương tác.

#### Nguyên Tắc Level Design

* **The Swiss Cheese:** Không có dead end. Mỗi phòng có ít nhất hai lối ra.
* **Verticality:** Vị trí mạnh tồn tại nhưng luôn có counter.
* **Landmarks:** Visual anchor rõ ràng để người chơi không cần compass vẫn biết mình đang ở đâu.

***

#### Core Maps & Zones

{{< cards cols="3" >}}
{{< card link="mapdesign_industrialzone/index.html" title="Industrial Zone" icon="cog" subtitle="Tập trung CQC. Nhà máy nhiều tầng. Mật độ loot cao." >}}
{{< card link="mapdesign_neonslums/index.html" title="Neon Slums" icon="office-building" subtitle="Urban warfare. Hẻm hẹp và rooftop." >}}
{{< card link="mapdesign_wilderness/index.html" title="The Wilderness" icon="cloud" subtitle="Tầm xa. Rừng và đồng mở." >}}
{{< /cards >}}

***

#### Systems & Mechanics

{{< cards cols="2" >}}
{{< card link="lootdistribution/index.html" title="Loot Economy" icon="gift" subtitle="Spawning logic, container type, và heatmap." >}}
{{< card link="maplayouts/index.html" title="Blueprints" icon="map" subtitle="Top-down view và tactical overlay." >}}
{{< card link="environmentalnarrative/index.html" title="Storytelling" icon="book-open" subtitle="Kể chuyện không dùng lời." >}}
{{< card link="environmentalnarrative_guidelines/index.html" title="Level Art Rules" icon="pencil" subtitle="Quy tắc đặt prop và decal." >}}
{{< /cards >}}
