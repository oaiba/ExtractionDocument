---
title: "Thiết Kế Âm Thanh & Soundscape"
linkTitle: "Audio"
type: docs
weight: 2
---

## Tầm Nhìn Âm Thanh

Trong extraction shooter, âm thanh là **sinh tồn**. Sound design phải truyền đạt thông tin trước, rồi mới đến immersion. Mỗi tiếng bước chân, thao tác reload, và tiếng súng xa đều kể một câu chuyện về mức đe dọa trong khu vực gần người chơi.

Các trụ cột audio tập trung vào **độ rõ**, **độ chính xác vị trí**, và **phản hồi chiến thuật**.

{{< cards cols="2" >}}
  {{< card link="sounddesign/index.html" title="Audio Guidelines" icon="music-note" subtitle="Trụ cột cốt lõi, chuẩn mix, và giới hạn kỹ thuật." >}}
  {{< card link="tacticalaudio/index.html" title="Tactical Audio" icon="bell" subtitle="Footstep, weapon foley, và combat feedback cue." >}}
  {{< card link="soundscape/index.html" title="World Ambience" icon="globe-alt" subtitle="Bản sắc âm thanh theo zone và environmental storytelling." >}}
  {{< card link="voicelines/index.html" title="Voice & Dialogue" icon="chat-alt-2" subtitle="Operator bark, announcer line, và narrative voiceover." >}}
{{< /cards >}}

---

## Tính Năng Audio Chính

### 1. Occlusion & Propagation

Âm thanh phải hành xử đáng tin.

* **Indoor/Outdoor:** EQ thay đổi rõ rệt khi di chuyển giữa môi trường trong nhà và ngoài trời.
* **Verticality:** Phân biệt rõ âm thanh ở phía trên và phía dưới người chơi.

### 2. "Info Layer"

Các âm thanh gameplay quan trọng (bước chân, reload, rút chốt) phải xuyên qua mix.

* **High Priority:** Di chuyển của kẻ địch trong phạm vi 30m.
* **Medium Priority:** Tiếng súng xa, vụ nổ.
* **Low Priority:** Gió môi trường, tiếng máy móc nền.

### 3. Xây Dựng Căng Thẳng

Sự im lặng cũng quan trọng như tiếng động. Việc wildlife ambience đột ngột dừng lại có thể báo hiệu predator hoặc người chơi ở gần.
