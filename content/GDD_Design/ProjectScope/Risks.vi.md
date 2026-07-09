---
title: "Project Risks & Mitigation"
type: docs
---

### Risk Management Philosophy

**Core Principle:** "Identify risks early, plan mitigation, monitor continuously"

Tài liệu này xác định risk tiềm năng trên toàn dự án:

* **Design risks** - Rủi ro về gameplay và experience
* **Technical risks** - Thách thức implementation
* **Business risks** - Rủi ro market và revenue
* **Operational risks** - Rủi ro team và process

***

### Design Risks

#### Risk D1: Core Loop Not Fun Enough

| Aspect | Details |
| --------------- | -------------------------------------------------------------------------- |
| **Risk** | Extraction gameplay loop có thể chưa đủ hấp dẫn cho mobile players |
| **Probability** | Medium |
| **Impact** | Critical |
| **Indicators** | D1/D7 retention thấp, session time ngắn, review tiêu cực |

**Mitigation:**

1. Playtest rộng trước launch
2. Iterate nhanh core loop trong soft launch
3. Thêm engagement hook ngoài extraction (quest, progression)
4. Onboarding rõ để truyền đạt appeal

**Contingency:**

* Pivot loop nếu soft launch cho thấy D7 retention < 30%
* Thêm mode thân thiện casual bên cạnh core

***

#### Risk D2: Too Hardcore for Mobile Audience

| Aspect | Details |
| --------------- | ------------------------------------------------------------------------ |
| **Risk** | Permanent loot loss có thể làm casual mobile players ức chế |
| **Probability** | Medium-High |
| **Impact** | High |
| **Indicators** | Churn cao sau lần chết đầu, review nói "unfair" |

**Mitigation:**

1. Protected slots system để không mất tất cả
2. Insurance hào phóng cho new players (20 match đầu)
3. Communicate rõ risk/reward
4. Có low-risk game modes

**Contingency:**

* Introduce "Casual Mode" với penalty thấp hơn
* Điều chỉnh protected slot count theo data

***

#### Risk D3: Pay-to-Win Perception

| Aspect | Details |
| --------------- | ---------------------------------------------------------------- |
| **Risk** | Người chơi cảm nhận monetization là pay-to-win, làm hại reputation |
| **Probability** | Medium |
| **Impact** | Critical |
| **Indicators** | Community backlash, review tiêu cực, influencer criticism |

**Mitigation:**

1. Monetization strict cosmetic-only
2. Không bán gameplay advantage
3. Communicate minh bạch về model
4. Community council để nhận feedback

**Contingency:**

* Gỡ ngay item bị nhận là P2W
* Public apology và compensation nếu vượt red line

***

#### Risk D4: Poor Cross-Platform Balance

| Aspect | Details |
| --------------- | --------------------------------------------------------------- |
| **Risk** | Mobile players cảm thấy bất lợi trước PC/controller players |
| **Probability** | High |
| **Impact** | High |
| **Indicators** | Complaint từ mobile players, mobile retention thấp hơn |

**Mitigation:**

1. Tuning aim assist cho mobile
2. Optional input-based matchmaking
3. Separate ranked queues theo input nếu cần
4. Monitor balance liên tục

**Contingency:**

* Disable cross-play by default nếu imbalance nghiêm trọng
* Platform-specific balancing

**Owner:** Lead Designer. **Review cadence:** Monthly (xem [Scope Review & Planning](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/ProjectScope/project-scope-review-and-planning.html) section 5.3).

***

#### Risk D5: Content Drought

| Aspect | Details |
| --------------- | -------------------------------------------------------------------- |
| **Risk** | Player hoàn thành content nhanh hơn tốc độ sản xuất, dẫn đến boredom |
| **Probability** | Medium |
| **Impact** | High |
| **Indicators** | DAU giảm sau vài tuần đầu, community complaint |

**Mitigation:**

1. Progression system đủ sâu
2. Seasonal content calendar trước 6+ tháng
3. Procedural/random elements cho replayability
4. Community events giữa major update

**Contingency:**

* Accelerate content pipeline
* Repurpose asset hiện có một cách sáng tạo
* Tăng event frequency

***

### Technical Risks

#### Risk T1: Performance on Low-End Devices

| Aspect | Details |
| --------------- | ------------------------------------------------------- |
| **Risk** | Game chạy kém trên target min-spec mobile devices |
| **Probability** | Medium |
| **Impact** | High |
| **Indicators** | Low FPS, crash trên device cũ, review 1-star |

**Mitigation:**

1. Define min-spec sớm (ví dụ 3GB RAM, Snapdragon 660)
2. Scalable graphics settings
3. Performance testing xuyên suốt development
4. Separate "Lite" APK nếu cần

**Contingency:**

* Aggressive optimization pass
* Giảm visual quality trên low-end
* Drop support lowest tier nếu không còn cách khác

***

#### Risk T2: Network Latency Issues

| Aspect | Details |
| --------------- | ------------------------------------------------------------ |
| **Risk** | Latency cao khiến combat real-time có cảm giác unfair/unresponsive |
| **Probability** | Medium |
| **Impact** | High |
| **Indicators** | Complaint lag, hit registration issue, player frustration |

**Mitigation:**

1. Client-side prediction cho movement
2. Lag compensation cho hit detection
3. Server location ở major regions
4. Graceful degradation khi connection xấu

**Contingency:**

* Implement lag hiding mạnh hơn
* Add latency-based matchmaking
* Cân nhắc turn-based element cho critical action nếu cần

***

#### Risk T3: Cheating & Exploits

| Aspect | Details |
| --------------- | ------------------------------------------------------------------- |
| **Risk** | Cheating lan rộng phá competitive integrity |
| **Probability** | High |
| **Impact** | Critical |
| **Indicators** | Community report, abnormal stats, Reddit/Discord complaint |

**Mitigation:**

1. Server-authoritative game logic
2. Anti-cheat system (kernel-level trên PC)
3. Behavioral analysis để detect
4. Fast response team cho cheat mới

**Contingency:**

* Emergency patch cho exploit
* Hardware/device bans
* Separate "trusted" matchmaking pools

***

#### Risk T4: Scaling Issues at Launch

| Aspect | Details |
| --------------- | -------------------------------------------- |
| **Risk** | Server không chịu được player load khi launch |
| **Probability** | Medium |
| **Impact** | Critical |
| **Indicators** | Login queue, server crash, không vào chơi được |

**Mitigation:**

1. Load testing trước launch
2. Auto-scaling infrastructure
3. Staged rollout theo region
4. Queue system sẵn sàng

**Contingency:**

* Maintenance messaging chuẩn bị trước
* Emergency server scaling
* Disable feature không critical theo thứ tự ưu tiên

***

### Business Risks

#### Risk B1: Market Competition

| Aspect | Details |
| --------------- | ------------------------------------------------------ |
| **Risk** | Game extraction cạnh tranh launch và chiếm market |
| **Probability** | Medium |
| **Impact** | High |
| **Indicators** | Competitor announcement, market share loss |

**Mitigation:**

1. Tập trung unique mobile-first design
2. Build community loyalty trước launch
3. Speed to market nhưng giữ quality
4. Differentiation rõ trong marketing

**Contingency:**

* Accelerate feature khác biệt chính
* Điều chỉnh positioning trong marketing
* Cân nhắc partnership/acquisition

***

#### Risk B2: Low Monetization

| Aspect | Details |
| --------------- | ------------------------------------------------- |
| **Risk** | Player không spend đủ để sustain development |
| **Probability** | Medium |
| **Impact** | Critical |
| **Indicators** | ARPU thấp, conversion rate thấp, LTV kém |

**Mitigation:**

1. Nhiều monetization stream (BP, cosmetic, convenience)
2. Battle Pass value hấp dẫn
3. Content mới đều đặn đáng mua
4. A/B testing pricing và offer

**Contingency:**

* Introduce monetization type mới một cách cẩn trọng
* Tăng cosmetic frequency
* Review pricing strategy

***

#### Risk B3: Hyper-Inflation of Economy

| Aspect | Details |
| --------------- | ---------------------------------------------------------------------------------------- |
| **Risk** | Currency in-game mất giá khi player tích lũy wealth, làm mất cảm giác "Struggle" |
| **Probability** | High |
| **Impact** | High |
| **Indicators** | Market price tăng mạnh, player chỉ chạy "Meta" kit |

**Mitigation:**

1. Money sink: repair cost cao, tax, Safe House upgrade
2. Seasonal wipes (hard hoặc soft reset)
3. Dynamic Trader Pricing theo global supply
4. "Black Swan" event làm destabilize currency

**Contingency:**

* Emergency price adjustment
* Introduce high-tier currency mới (ví dụ Gold Bars)
* Mid-season wipe nếu thật sự cần

**Owner:** Economy Lead / Live Ops. **Review cadence:** Monthly (xem [Scope Review & Planning](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/ProjectScope/project-scope-review-and-planning.html) section 5.3).

***

#### Risk B4: Platform Policy Changes

| Aspect | Details |
| --------------- | ------------------------------------------------------------------------ |
| **Risk** | App store policy change ảnh hưởng xấu tới game |
| **Probability** | Low-Medium |
| **Impact** | High |
| **Indicators** | Policy announcement từ Apple/Google |

**Mitigation:**

1. Monitor platform policy changes
2. Chuẩn bị nhiều distribution channel
3. Build direct player relationship (email, Discord)
4. Budget giả định revenue split hiện tại

**Contingency:**

* Explore alternative payment method nơi legal
* Điều chỉnh pricing để giữ margin
* Legal review policy compliance

***

#### Risk B5: Negative Launch Reviews

| Aspect | Details |
| --------------- | ------------------------------------------- |
| **Risk** | Review launch kém làm hại discoverability |
| **Probability** | Medium |
| **Impact** | High |
| **Indicators** | Average dưới 4.0 trên app stores |

**Mitigation:**

1. Soft launch rộng để polish
2. Community beta cho early feedback
3. Onboarding mạnh để giảm confusion
4. Optimize timing request review trong game

**Contingency:**

* Rapid response cho complaint phổ biến
* Update app store listing với fix
* Request updated reviews sau improvement

***

### Operational Risks

#### Risk O1: Key Personnel Loss

| Aspect | Details |
| --------------- | ----------------------------------------------------------- |
| **Risk** | Member critical rời team, mất institutional knowledge |
| **Probability** | Medium |
| **Impact** | High |
| **Indicators** | Turnover tăng, knowledge gap |

**Mitigation:**

1. Documentation culture
2. Cross-training team members
3. Competitive compensation
4. Positive work culture

**Contingency:**

* Knowledge transfer protocol
* Xác định contractor pool
* Duy trì recruiting pipeline

***

#### Risk O2: Scope Creep

| Aspect | Details |
| --------------- | --------------------------------------------- |
| **Risk** | Feature request mở rộng scope vượt capacity |
| **Probability** | High |
| **Impact** | Medium |
| **Indicators** | Milestone trượt, team burnout |

**Mitigation:**

1. MVP definition rõ
2. Change request process
3. Scope review định kỳ
4. Feature prioritization framework

**Contingency:**

* Cut feature không nằm trên critical path
* Delay non-essential feature sang post-launch
* Điều chỉnh timeline nếu quality at risk

***

#### Risk O3: External Dependencies

| Aspect | Details |
| --------------- | ----------------------------------------- |
| **Risk** | Third-party service fail hoặc đổi terms |
| **Probability** | Low-Medium |
| **Impact** | Medium-High |
| **Indicators** | Vendor communication, service outage |

**Mitigation:**

1. Xác định toàn bộ external dependency
2. Có backup vendor
3. Abstract integration để portable
4. SLA monitoring

**Contingency:**

* Switch sang backup vendor
* Build in-house solution dài hạn
* Negotiate với vendor

***

### Risk Tracking Matrix

| ID | Risk | Probability | Impact | Priority | Owner | Status |
| -- | ---------------------- | ----------- | ----------- | -------- | ----------------- | -------------- |
| D1 | Core Loop Not Fun | Medium | Critical | P0 | Game Director | Monitoring |
| D2 | Too Hardcore | Medium-High | High | P0 | Game Director | Monitoring |
| D3 | P2W Perception | Medium | Critical | P0 | Producer | Mitigated |
| D4 | Cross-Platform Balance | High | High | P1 | Lead Designer | Monitoring |
| D5 | Content Drought | Medium | High | P1 | Live Ops | Planned |
| T1 | Low-End Performance | Medium | High | P1 | Tech Lead | In Progress |
| T2 | Network Latency | Medium | High | P1 | Network Lead | In Progress |
| T3 | Cheating | High | Critical | P0 | Security Lead | In Progress |
| T4 | Launch Scaling | Medium | Critical | P0 | DevOps Lead | Planned |
| B1 | Market Competition | Medium | High | P1 | Producer | Monitoring |
| B2 | Low Monetization | Medium | Critical | P1 | Monetization Lead | Monitoring |
| B3 | Economy Inflation | High | High | P1 | Economy Lead / Live Ops | Monitoring |
| B4 | Platform Policies | Low-Medium | High | P2 | Legal | Monitoring |
| B5 | Negative Reviews | Medium | High | P1 | Community Lead | Planned |
| O1 | Key Personnel | Medium | High | P1 | HR Lead | Monitoring |
| O2 | Scope Creep | High | Medium | P1 | Producer | Active Control |
| O3 | External Dependencies | Low-Medium | Medium-High | P2 | Tech Lead | Documented |

***

### Risk Review Schedule

| Frequency | Activity |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Weekly | Team leads review active risks |
| Bi-weekly | Risk status update trong sprint review |
| Monthly | Full risk matrix review với leadership; D4 (Cross-Platform) và B3 (Economy inflation) owners report (xem [Scope Review & Planning](https://github.com/oaiba/ExtractionDocument/blob/main/content/GDD_Design/ProjectScope/project-scope-review-and-planning.html) section 5.3). |
| Quarterly | Risk retrospective và identify risk mới |
