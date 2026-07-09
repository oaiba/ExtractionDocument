---
title: "Non-Goals & Explicit Exclusions"
type: docs
---

## Purpose of This Document

**Vì sao cần định nghĩa những thứ KHÔNG làm?**

Tài liệu này nêu rõ các feature, system, và approach được **cố ý loại khỏi game**. Mục tiêu là tránh:

- **Scope creep** - "Sao không thêm X luôn?"
- **Design drift** - Mất tập trung khỏi core pillars
- **Resource waste** - Xây thứ không phù hợp
- **Team confusion** - Mọi người hiểu cùng một ranh giới

**Quan trọng:** Non-goal không có nghĩa là "không bao giờ"; nó nghĩa là "không phải bây giờ và không phải ưu tiên." Một số mục có thể được xét lại post-launch dựa trên data.

---

## Gameplay Non-Goals

### Chúng Ta KHÔNG Xây Battle Royale

| Aspect | Our Game | Battle Royale |
| :-------------- | :----------------- | :----------------- |
| Player count | 15-20 | 100+ |
| Win condition | Extract with loot | Be last alive |
| Match structure | Enter/exit anytime | Single elimination |
| Loadout | Bring your own | Find in-match |
| Progression | Persistent | Per-match reset |

**Vì sao không:**

- Thị trường BR đã bão hòa
- Core fantasy khác
- Technical complexity không đáng với lợi ích
- Extraction loop là điểm khác biệt chính

**Decision status:** Final - Will not change

---

### Chúng Ta KHÔNG Xây MMORPG

**Excluded features:**

- Persistent open world (dùng instance-based)
- Massive player count trong cùng không gian
- World boss cần 50+ người
- Player housing/persistent base
- Deep crafting với gathering profession
- Story-driven questing làm primary content

**Vì sao không:**

- Scope phình nổ
- Lo ngại performance/battery trên mobile
- Không khớp session time (10-15 phút vs nhiều giờ)
- Kỳ vọng audience khác

**Decision status:** Final

---

### Chúng Ta KHÔNG Xây Esport Lúc Đầu

**Excluded at launch:**

- Spectator mode (add post-launch)
- Tournament infrastructure
- Official competitive leagues
- LAN event support
- Detailed replay system

**Vì sao không:**

- Launch tập trung vào core game
- Esport feature đắt nếu làm đúng
- Phải chứng minh game thành công trước
- Community cần phát triển tự nhiên

**Decision status:** Deferred to Year 2+

---

### Chúng Ta KHÔNG Nhắm Ultra-Realism

**Excluded approaches:**

- Simulation-level weapon ballistics
- Complex medical system kiểu EFT surgery
- Realistic magazine management
- Permanent character injury
- Hunger/thirst survival mechanics

**Vì sao không:**

- Mobile audience cần accessibility cao hơn
- Giới hạn session time
- Learning curve quá dốc làm hại retention
- Mục tiêu là "tactical", không phải "tedious"

**Decision status:** Final

---

### Chúng Ta KHÔNG Thêm Vehicles Lúc Đầu

**Excluded:**

- Drivable vehicles
- Vehicle combat
- Vehicle customization

**Vì sao không:**

- Map size chưa cần vehicle
- Physics complexity trên mobile
- Ảnh hưởng lớn tới balance extraction
- Dev time nên dùng cho phần khác

**Decision status:** Consider for large desert map (Season 4+)

---

### Chúng Ta KHÔNG Xây Base Building

**Excluded:**

- Player-constructed structures
- Fortification mechanics
- Clan bases/hideouts

**Vì sao không:**

- Tăng scope rất mạnh
- Server/persistence complexity
- Không khớp extraction loop
- Fortnite đã sở hữu không gian này

**Decision status:** Final

---

## Monetization Non-Goals

### Chúng Ta KHÔNG Bán Gameplay Advantage

**Explicitly NOT for sale:**

- Weapon có stat tốt hơn
- Armor bảo vệ tốt hơn
- Operator stat boost
- Giảm matchmaking time bằng tiền
- Tăng loot chance cho người trả tiền
- Thêm protected slot bằng tiền thật (chỉ dùng credits nếu có)

**Vì sao không:**

- Phá competitive integrity
- Chắc chắn bị community backlash
- Long-term player value > short-term revenue
- Đây là pillar không thương lượng

**Decision status:** Final - Red line

---

### Chúng Ta KHÔNG Có Loot Boxes (Randomized Purchases)

**Excluded:**

- Blind random item box bằng tiền thật
- Gacha-style character pull
- Mystery bundle

**What we DO have:**

- Battle Pass (reward biết trước)
- Direct purchase cosmetic
- Occasional free random reward (gameplay only)

**Vì sao không:**

- Vấn đề pháp lý ở nhiều khu vực
- Vấn đề đạo đức
- Nhận thức tiêu cực từ player
- Model minh bạch tạo niềm tin

**Decision status:** Final

---

### Chúng Ta KHÔNG Có Energy Systems

**Excluded:**

- Giới hạn số lần chơi mỗi ngày
- Lives hồi theo thời gian
- Pay-to-play-more mechanics

**Vì sao không:**

- Người chơi nên được chơi bao nhiêu tùy thích
- Energy system gây ức chế
- Revenue đến từ engagement, không phải gating

**Decision status:** Final

---

### Chúng Ta KHÔNG Có Forced Ads

**Excluded:**

- Interstitial ads giữa match
- Ads bắt buộc cho core gameplay
- Banner ads trong gameplay

**What we MIGHT have:**

- Optional rewarded ads (xem để nhận bonus nhỏ)
- Chỉ trong context cụ thể (post-match, daily reward)

**Vì sao không:**

- Người chơi kỳ vọng premium experience
- Ads phá immersion
- Whale không chấp nhận ads

**Decision status:** Final

---

## Technical Non-Goals

### Chúng Ta KHÔNG Support Ancient Devices

**Minimum specs (firm):**

- Android: 3GB RAM, Snapdragon 660 equivalent, Android 8.0+
- iOS: iPhone 8 / iPad 6th gen hoặc mới hơn, iOS 14+

**NOT supported:**

- Thiết bị dưới 3GB RAM
- Android 7.x hoặc thấp hơn
- iPhone 7 hoặc cũ hơn
- Thiết bị không có OpenGL ES 3.0

**Vì sao không:**

- Compromise performance làm hại tất cả người chơi
- Lợi ích giảm dần khi đuổi theo hardware quá cũ
- Security concern với OS cũ
- Future-proof codebase

**Decision status:** Final

---

### Chúng Ta KHÔNG Xây Offline Mode

**Excluded:**

- Single-player offline play
- Chơi không cần internet
- Local multiplayer

**Vì sao không:**

- Anti-cheat cần server authority
- Progression phải được verify
- Core experience là multiplayer
- Data sync complexity không đáng

**Decision status:** Final

---

### Ban Đầu KHÔNG Native Trên Mọi Platform

**Launch platforms:**

- Android (Google Play)
- iOS (App Store)
- PC (Epic/Steam) - Post-launch

**NOT at launch:**

- Console (PlayStation, Xbox, Switch)
- Web version
- Mac native

**Vì sao không:**

- Tập trung resource vào core platforms
- Console certification đắt/chậm
- Mobile-first nghĩa là ưu tiên mobile quality trước

**Decision status:** Console considered for Year 2

---

## Content Non-Goals

### Chúng Ta KHÔNG Theo Licensing/IP Crossovers

**Excluded:**

- Skin nhân vật Movie/TV
- Crossover character từ game khác
- Celebrity athlete partnership
- Brand collaboration (energy drink, v.v.)

**Vì sao không:**

- Licensing fee đắt
- Có thể xung đột lore
- Phụ thuộc external partner
- Muốn xây IP value riêng

**Decision status:** Reconsider after Year 1 success

---

### Chúng Ta KHÔNG Tạo Player-Generated Content

**Excluded:**

- Custom maps
- Mod support
- User-created skins
- Workshop/marketplace

**Vì sao không:**

- QA cực khó trên mobile
- Moderation requirement lớn
- Technical complexity
- Security vulnerabilities

**Decision status:** Final for mobile

---

### Chúng Ta KHÔNG Làm Voice Acting Quá Rộng

**Excluded:**

- Full narrative voice acting
- Voiced quest dialogues
- NPC conversations

**What we DO have:**

- Operator combat callouts
- Tutorial narration
- Announcer voice

**Vì sao không:**

- Budget constraint
- Localization cost nhân lên nhiều lần
- Download size concern
- Text linh hoạt hơn

**Decision status:** Final for launch

---

## Social/Community Non-Goals

### Chúng Ta KHÔNG Xây Social Media

**Excluded:**

- In-game feed/timeline
- Public profile có post
- Following/followers system
- Content sharing trong game

**Vì sao không:**

- Moderation nightmare
- Liability concern
- Làm phân tán khỏi gameplay
- Dùng existing platforms thay thế

**Decision status:** Final

---

### Chúng Ta KHÔNG Cho Real-Money Trading

**Excluded:**

- Player-to-player item sale bằng cash
- Official marketplace bằng tiền thật
- NFT hoặc blockchain item

**Vì sao không:**

- Legal complexity (gambling, securities)
- Khuyến khích black market
- Tạo incentive exploit cho hacker
- Phá economy design

**Decision status:** Final - Red line

---

## Non-Goal Review Process

### Adding to Non-Goals

1. Feature request được xác định
2. Evaluate với design pillars
3. Assess scope/resource impact
4. Team discussion
5. Nếu reject: thêm vào Non-Goals với rationale
6. Communicate cho team

### Reconsidering Non-Goals

Non-goals có thể được xét lại khi:

- Market condition thay đổi đáng kể
- Post-launch data cho thấy cơ hội
- Technical constraint được giải quyết
- Resource khả dụng
- Community demand rất lớn VÀ khớp vision

**Review frequency:** Quarterly

---

## Trade-Off Principles

Khi phải lựa chọn, chúng ta ưu tiên:

| Priority | Over | Rationale |
| :---------------- | :------------ | :------------------------------ |
| Core loop quality | More features | Fun first, breadth later |
| Mobile experience | PC parity | Mobile-first philosophy |
| Player fairness | Revenue | Trust is our currency |
| Launch quality | Launch date | Better to delay than fail |
| Team health | Crunch | Sustainable pace wins long-term |

---

## Summary Table

| Non-Goal | Category | Status |
| :--------------------- | :----------- | :--------- |
| Battle Royale mode | Gameplay | Final |
| MMO features | Gameplay | Final |
| Esport infrastructure | Gameplay | Deferred |
| Ultra-realism | Gameplay | Final |
| Vehicles | Gameplay | Deferred |
| Base building | Gameplay | Final |
| Pay-to-win | Monetization | Red Line |
| Loot boxes | Monetization | Final |
| Energy systems | Monetization | Final |
| Forced ads | Monetization | Final |
| Ancient device support | Technical | Final |
| Offline mode | Technical | Final |
| Console launch | Technical | Deferred |
| IP crossovers | Content | Deferred |
| User-generated content | Content | Final |
| Extensive voice acting | Content | Final |
| Social media features | Social | Final |
| Real-money trading | Social | Red Line |
