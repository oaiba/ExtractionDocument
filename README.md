# Extraction Topdown Mobile Multiplayer
## Game Design Documentation

**Version:** 1.0  
**Last Updated:** February 6, 2026  
**Platform:** Mobile (iOS/Android)  
**Engine:** Unreal Engine 5 (C++)  
**Genre:** Extraction Shooter, Top-down, Multiplayer  

---

## Overview

Đây là tài liệu thiết kế game toàn diện cho dự án **Extraction Topdown Mobile Multiplayer**. Tài liệu được chia thành hai phần chính:

### 1. High-Level GDD (Game Design)
**Dành cho:** Game Designers, Artists, 3D Artists, Level Designers, Sound Designers

Tập trung vào:
- Game concept và vision
- Gameplay mechanics và player experience
- Art direction và visual style
- Character design và world building
- Audio design
- UI/UX design

**[📖 Truy cập High-Level GDD](./GDD_HighLevel/README.md)**

---

### 2. Technical GDD (Development)
**Dành cho:** Programmers, Technical Artists, DevOps, QA

Tập trung vào:
- System architecture
- Technical implementation (C++)
- Network và multiplayer systems
- Performance optimization
- Development roadmap và TODO tracking
- Technical specifications

**[⚙️ Truy cập Technical GDD](./GDD_Technical/README.md)**

---

## Quick Links

### High-Level Documentation
- [Game Overview & Concept](./GDD_HighLevel/01_GameOverview.md)
- [Core Gameplay Loop](./GDD_HighLevel/02_CoreGameplay.md)
- [Character Systems](./GDD_HighLevel/03_Characters.md)
- [World & Map Design](./GDD_HighLevel/04_WorldDesign.md)
- [Art Direction](./GDD_HighLevel/05_ArtDirection.md)
- [Audio Design](./GDD_HighLevel/06_AudioDesign.md)
- [User Interface](./GDD_HighLevel/07_UserInterface.md)
- [Progression & Monetization](./GDD_HighLevel/08_Progression.md)

### Technical Documentation
- [System Architecture](./GDD_Technical/01_Architecture.md)
- [Networking System](./GDD_Technical/02_NetworkingSystem.md)
- [Character System](./GDD_Technical/03_CharacterSystem.md)
- [Weapon & Combat System](./GDD_Technical/04_WeaponSystem.md)
- [Inventory & Loot System](./GDD_Technical/05_InventorySystem.md)
- [AI System](./GDD_Technical/06_AISystem.md)
- [Map & Environment System](./GDD_Technical/07_MapSystem.md)
- [Performance Optimization](./GDD_Technical/08_PerformanceOptimization.md)
- [Development Roadmap & TODO](./GDD_Technical/09_DevelopmentRoadmap.md)

---

## Game Pillars

1. **Risk vs Reward** - Mỗi quyết định đều có giá trị, death means losing everything
2. **Tactical Combat** - Top-down perspective cho strategic gameplay
3. **Persistent Progression** - Extracted loot được giữ vĩnh viễn
4. **Mobile Optimization** - Intuitive controls, 10-15 minute matches

---

## Key Features

- ⚔️ Real-time multiplayer (8-16 players)
- 🎯 Top-down tactical combat
- 💰 Extraction-based gameplay với permanent loot loss
- 📊 Deep progression system
- 📱 Mobile-optimized controls
- 🌍 Cross-platform matchmaking
- 🎮 Season-based content updates

---

## Team Structure

**Design Team:**
- Game Designer
- Level Designer
- UI/UX Designer

**Art Team:**
- 3D Character Artist
- Environment Artist
- Technical Artist
- Sound Designer

**Development Team:**
- Lead Programmer (UE5 C++)
- Gameplay Programmers (2)
- Network Programmer
- UI Programmer

**Support:**
- Product Manager
- QA Lead
- Community Manager

---

## Version History

| Version | Date       | Changes                         | Author |
| ------- | ---------- | ------------------------------- | ------ |
| 1.0     | 2026-02-06 | Initial documentation structure | Team   |

---

## Contact

**Project Management:**
- Product Manager: [Contact]
- Lead Designer: [Contact]
- Technical Director: [Contact]

**Documentation Maintainers:**
- Game Design: [Contact]
- Technical: [Contact]


Note:

🛠️ CÁC MỤC CẦN BỔ SUNG & SỬA ĐỔI
Dưới đây là danh sách các tài liệu GDD cần bổ sung để hoàn thiện hồ sơ thiết kế:

1. 🌍 World Building & Level Design (Xây dựng Thế giới) - Mức độ: Ưu tiên Cao
Hiện tại thư mục GDD_Design/World đang trống hoặc chưa chi tiết. Game Extraction Shooter sống chết nhờ thiết kế bản đồ.

Cần bổ sung:
Map Layouts (Bố cục bản đồ): Tài liệu mô tả các khu vực chính (POIs), điểm nóng (Hotspots), vị trí Choke points và các lối ra (Extraction Points).
Environmental Narrative (Kể chuyện qua môi trường): Mô tả không khí, dấu vết lịch sử của từng khu vực (Tại sao khu thí nghiệm này bị bỏ hoang? Vết máu này từ đâu?).
Loot Distribution (Phân bổ tài nguyên): Bản đồ nhiệt phân bố loot (Khu nào high-tier, khu nào lính mới an toàn).
2. 📖 Narrative & Lore (Cốt truyện & Bối cảnh) - Mức độ: Trung bình
Thư mục GDD_Design/Story cần được xây dựng.

Cần bổ sung:
Factions (Phe phái): Chi tiết về các phe phái trong game (Lính đánh thuê, Tập đoàn, Người bản địa...). Quan hệ giữa các phe (Đồng minh/Thù địch).
Quest Lines (Hệ thống nhiệm vụ): Mẫu thiết kế nhiệm vụ (Nhiệm vụ cốt truyện chính vs Nhiệm vụ hàng ngày/tuần).
Legend/Backstory: Lịch sử thế giới game dẫn đến sự kiện hiện tại (The Collapse/The Outbreak).
3. 🎨 Art Direction (Định hướng Nghệ thuật) - Mức độ: Trung bình
Thư mục GDD_Design/Visuals mới chỉ có UI.

Cần bổ sung:
Art Bible/Style Guide: Quy chuẩn về phong cách hình ảnh (Realistic, Stylized, Cyberpunk...?). Bảng màu (Color Palette), ánh sáng (Lighting mood).
Asset Guidelines: Quy chuẩn thiết kế nhân vật 3D, vũ khí, môi trường để đảm bảo đồng bộ.
4. 🔊 Audio Design (Thiết kế Âm thanh) - Mức độ: Quan trọng cho Game Shooter
Thư mục GDD_Design/Audio đang trống. Với game bắn súng sinh tồn, âm thanh là "đôi mắt thứ hai".

Cần bổ sung:
Soundscape (Không gian âm thanh): Tiếng gió, tiếng côn trùng, tiếng vọng trong nhà máy.
Tactical Audio (Âm thanh chiến thuật): Chi tiết về tiếng bước chân trên các bề mặt khác nhau (cỏ, kim loại, nước), tiếng súng xa/gần, tiếng thay đạn.
Voice Lines: Danh sách các câu thoại (Callouts) của nhân vật và NPC.
5. 📅 Project Management & Scope (Phạm vi & Quản lý)
Thư mục GDD_Design/ProjectScope cần chi tiết hơn.

Cần bổ sung:
MVP Scope (Phạm vi bản thử nghiệm): Định nghĩa chính xác những tính năng nào CÓ trong bản Alpha/Beta và những gì để lại sau.
Risk Analysis (Phân tích rủi ro): Các rủi ro kỹ thuật (Lag, Hack) và thiết kế (Gameplay loop chán) cùng phương án dự phòng.
📝 ĐỀ XUẤT HÀNH ĐỘNG TIẾP THEO
Để lấp đầy các khoảng trống này, tôi đề xuất chúng ta thực hiện theo thứ tự sau:

Tạo GDD_Design/World/MapDesign_IndustrialZone.md: Thiết kế chi tiết bản đồ đầu tiên (Khu công nghiệp/Phòng thí nghiệm) - đây là nơi gameplay diễn ra.
Tạo GDD_Design/Audio/SoundDesign.md: Định nghĩa hệ thống âm thanh chiến thuật (quan trọng cho cả Mobile khi chơi không tai nghe - tính năng Sound Radar).
Tạo GDD_Design/Story/FactionsAndLore.md: Xây dựng bối cảnh để tạo chiều sâu cho game.
Bạn muốn tôi bắt đầu với mục nào trước? (Khuyên dùng: World/MapDesign vì nó ảnh hưởng trực tiếp đến code Map System).