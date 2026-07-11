---
title: "Thiết Kế AI & Kẻ Địch"
linkTitle: AI
type: docs
weight: 1
---

### Tổng Quan Hệ Thống

AI trong **Extraction Shooter** không chỉ là mục tiêu để bắn, mà là một trụ cột của vòng lặp extraction. Kẻ địch AI đóng vai trò **điều tiết nhịp độ**, **canh giữ loot**, và **bẫy âm thanh** để đẩy tương tác giữa người chơi với nhau.

Hệ thống được xây trên hai thành phần chính:

1. **Hành Vi Cá Thể:** Một đơn vị suy nghĩ, chiến đấu, và phản ứng như thế nào.
2. **Sinh Thái Faction:** Các nhóm AI tương tác với thế giới và với nhau như thế nào.

{{< cards cols="2" >}}
{{< card link="enemybehavior/index.html" title="Hành Vi Kẻ Địch" icon="chip" subtitle="Archetype, state, chiến thuật combat, và difficulty scaling." >}}
{{< card link="factionbehaviors/index.html" title="Sinh Thái Faction" icon="users" subtitle="Quan hệ giữa Scavengers, Syndicate, UN-PK, và Wildlife." >}}
{{< /cards >}}

***

### Trụ Cột Thiết Kế

#### 1. Thử Thách Không Gian Lận

AI nên khó vì **chiến thuật và quân số**, không phải vì có aimbot hoặc máu bị thổi phồng.

* **Tốt:** AI dùng cover, flank, và suppressing fire.
* **Xấu:** AI quay 180 độ tức thì hoặc theo dõi người chơi xuyên tường.

#### 2. Chiến Tranh Thông Tin

AI hoạt động như một **hệ thống phát tín hiệu** trong trận.

* **Tiếng súng:** Báo cho người chơi biết giao tranh đang diễn ra ở đâu.
* **Tiếng hô/Callout:** Tiết lộ trạng thái AI (Relaxed hay Combat) và có thể làm lộ vị trí người chơi cho bên thứ ba đáng tin.

#### 3. Dễ Đoán vs. Đe Dọa

Người chơi cần học được pattern của AI để làm chủ PvE encounter, nhưng sai lầm vẫn phải bị trừng phạt.

* **AI Tier 1 (Scavengers):** hỗn loạn, ồn ào, bắn thiếu chính xác.
* **AI Tier 3 (Elites):** kỷ luật, yên lặng, nguy hiểm.

***

### Snapshot Sinh Thái

Thế giới được lấp đầy bởi các faction riêng biệt, mỗi nhóm có mục tiêu và quan hệ riêng.

| Faction | Vai Trò | Mức Đe Dọa | Đặc Điểm Chính |
| -------------- | ----------------- | ------------ | ------------------------------------ |
| **Scavengers** | "Chuột" | Thấp | cơ chế bầy đàn, ồn ào, khó đoán |
| **Syndicate** | "Tinh nhuệ" | Cao | squad chiến thuật, dùng gear nâng cao |
| **UN-PK** | "Luật lệ" | Cực cao | phòng thủ, cảnh báo trước khi bắn |
| **Wildlife** | "Môi trường" | Biến thiên | thú săn mồi phục kích, sợ lửa |

> > > [**Xem đầy đủ Faction Matrix & Behaviors**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/AI/FactionBehaviors/README.md)

***

### Archetype AI

Các loại kẻ địch khác nhau cần cách tiếp cận chiến thuật khác nhau.

* **Fodder (Scavengers):** Rush hoặc bắn hạ từng mục tiêu. Chúng dựa vào quân số.
* **Soldiers (Guards):** yêu cầu dùng cover. Chúng sẽ suppress bạn.
* **Specialists (Snipers/Medics):** mục tiêu ưu tiên. Hạ chúng trước.
* **Bosses (The Warden):** objective của raid. Yêu cầu squad phối hợp và hỏa lực nặng.

> > > [**Xem Enemy Stats & Logic chi tiết**](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/AI/EnemyBehavior/README.md)
