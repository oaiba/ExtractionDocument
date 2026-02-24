---
title: "Project Risks & Mitigation"
type: docs
---

## ⚠️ Risk Management Philosophy

**Core Principle:** "Identify risks early, plan mitigation, monitor continuously"

This document identifies potential risks to the project across:
- **Design risks** - Gameplay and experience concerns
- **Technical risks** - Implementation challenges
- **Business risks** - Market and revenue concerns
- **Operational risks** - Team and process concerns

---

## 🎮 Design Risks

### Risk D1: Core Loop Not Fun Enough

| Aspect          | Details                                                                    |
| :-------------- | :------------------------------------------------------------------------- |
| **Risk**        | The extraction gameplay loop may not be engaging enough for mobile players |
| **Probability** | Medium                                                                     |
| **Impact**      | Critical                                                                   |
| **Indicators**  | Low D1/D7 retention, short session times, negative reviews                 |

**Mitigation:**
1. Extensive playtesting before launch
2. Quick iteration on core loop in soft launch
3. Multiple engagement hooks beyond extraction (quests, progression)
4. Clear onboarding to communicate the appeal

**Contingency:**
- Pivot loop if soft launch shows < 30% D7 retention
- Add more casual-friendly modes alongside core

---

### Risk D2: Too Hardcore for Mobile Audience

| Aspect          | Details                                                                  |
| :-------------- | :----------------------------------------------------------------------- |
| **Risk**        | Permanent loot loss may frustrate casual mobile players                  |
| **Probability** | Medium-High                                                              |
| **Impact**      | High                                                                     |
| **Indicators**  | High churn after first death, negative store reviews mentioning "unfair" |

**Mitigation:**
1. Protected slots system (can't lose everything)
2. Generous insurance for new players (first 20 matches)
3. Clear communication about risk/reward
4. Low-risk game modes available

**Contingency:**
- Introduce "Casual Mode" with reduced penalties
- Adjust protected slot count based on data

---

### Risk D3: Pay-to-Win Perception

| Aspect          | Details                                                          |
| :-------------- | :--------------------------------------------------------------- |
| **Risk**        | Players perceive monetization as pay-to-win, damaging reputation |
| **Probability** | Medium                                                           |
| **Impact**      | Critical                                                         |
| **Indicators**  | Community backlash, negative reviews, influencer criticism       |

**Mitigation:**
1. Strict cosmetic-only monetization
2. No gameplay advantages for sale
3. Transparent communication about model
4. Community council for feedback

**Contingency:**
- Immediate removal of any perceived P2W items
- Public apology and compensation if crossed

---

### Risk D4: Poor Cross-Platform Balance

| Aspect          | Details                                                         |
| :-------------- | :-------------------------------------------------------------- |
| **Risk**        | Mobile players feel disadvantaged against PC/controller players |
| **Probability** | High                                                            |
| **Impact**      | High                                                            |
| **Indicators**  | Mobile player complaints, lower mobile retention                |

**Mitigation:**
1. Aim assist tuning for mobile
2. Optional input-based matchmaking
3. Separate ranked queues by input (if needed)
4. Continuous balance monitoring

**Contingency:**
- Disable cross-play by default if imbalance severe
- Platform-specific balancing

**Owner:** Lead Designer. **Review cadence:** Monthly (see [Scope Review & Planning](project-scope-review-and-planning.html) §5.3).

---

### Risk D5: Content Drought

| Aspect          | Details                                                              |
| :-------------- | :------------------------------------------------------------------- |
| **Risk**        | Players finish content faster than we produce it, leading to boredom |
| **Probability** | Medium                                                               |
| **Impact**      | High                                                                 |
| **Indicators**  | Declining DAU after initial weeks, community complaints              |

**Mitigation:**
1. Deep progression systems (take time to max)
2. Seasonal content calendar planned 6+ months ahead
3. Procedural/random elements for replayability
4. Community events between major updates

**Contingency:**
- Accelerate content pipeline
- Repurpose existing assets creatively
- Increase event frequency

---

## 💻 Technical Risks

### Risk T1: Performance on Low-End Devices

| Aspect          | Details                                                 |
| :-------------- | :------------------------------------------------------ |
| **Risk**        | Game doesn't run well on target min-spec mobile devices |
| **Probability** | Medium                                                  |
| **Impact**      | High                                                    |
| **Indicators**  | Low FPS, crashes on older devices, 1-star reviews       |

**Mitigation:**
1. Define min-spec early (e.g., 3GB RAM, Snapdragon 660)
2. Scalable graphics settings
3. Performance testing throughout development
4. Separate "Lite" APK if needed

**Contingency:**
- Aggressive optimization pass
- Reduce visual quality on low-end
- Drop support for lowest tier (last resort)

---

### Risk T2: Network Latency Issues

| Aspect          | Details                                                      |
| :-------------- | :----------------------------------------------------------- |
| **Risk**        | High latency makes real-time combat feel unfair/unresponsive |
| **Probability** | Medium                                                       |
| **Impact**      | High                                                         |
| **Indicators**  | Lag complaints, hit registration issues, player frustration  |

**Mitigation:**
1. Client-side prediction for movement
2. Lag compensation for hit detection
3. Server locations in major regions
4. Graceful degradation on bad connections

**Contingency:**
- Implement more aggressive lag hiding
- Add latency-based matchmaking
- Consider turn-based elements for critical actions

---

### Risk T3: Cheating & Exploits

| Aspect          | Details                                                             |
| :-------------- | :------------------------------------------------------------------ |
| **Risk**        | Widespread cheating ruins competitive integrity                     |
| **Probability** | High                                                                |
| **Impact**      | Critical                                                            |
| **Indicators**  | Community reports, abnormal player stats, Reddit/Discord complaints |

**Mitigation:**
1. Server-authoritative game logic
2. Anti-cheat system (kernel-level on PC)
3. Behavioral analysis for detection
4. Fast response team for new cheats

**Contingency:**
- Emergency patches for exploits
- Hardware/device bans
- Separate "trusted" matchmaking pools

---

### Risk T4: Scaling Issues at Launch

| Aspect          | Details                                      |
| :-------------- | :------------------------------------------- |
| **Risk**        | Servers can't handle player load at launch   |
| **Probability** | Medium                                       |
| **Impact**      | Critical                                     |
| **Indicators**  | Login queues, server crashes, unable to play |

**Mitigation:**
1. Load testing before launch
2. Auto-scaling infrastructure
3. Staged rollout by region
4. Queue system ready

**Contingency:**
- Pre-prepared maintenance messaging
- Server emergency scaling
- Staggered feature disable (non-critical first)

---

## 💰 Business Risks

### Risk B1: Market Competition

| Aspect          | Details                                                |
| :-------------- | :----------------------------------------------------- |
| **Risk**        | Competing extraction game launches and captures market |
| **Probability** | Medium                                                 |
| **Impact**      | High                                                   |
| **Indicators**  | Competitor announcements, market share loss            |

**Mitigation:**
1. Focus on unique mobile-first design
2. Build community loyalty before launch
3. Speed to market while maintaining quality
4. Differentiation in marketing

**Contingency:**
- Accelerate key differentiating features
- Adjust positioning in marketing
- Consider partnership/acquisition

---

### Risk B2: Low Monetization

| Aspect          | Details                                           |
| :-------------- | :------------------------------------------------ |
| **Risk**        | Players don't spend enough to sustain development |
| **Probability** | Medium                                            |
| **Impact**      | Critical                                          |
| **Indicators**  | Low ARPU, low conversion rate, poor LTV           |

**Mitigation:**
1. Multiple monetization streams (BP, cosmetics, convenience)
2. Compelling Battle Pass value
3. Regular new content worth purchasing
4. A/B testing of pricing and offers

**Contingency:**
- Introduce new monetization types (carefully)
- Increase cosmetic frequency
- Review pricing strategy

---

### Risk B3: Hyper-Inflation of Economy
| Aspect          | Details                                                                                  |
| :-------------- | :--------------------------------------------------------------------------------------- |
| **Risk**        | In-game currency becomes worthless as players accumulate wealth, removing the "Struggle" |
| **Probability** | High (Likely in all extraction shooters eventually)                                      |
| **Impact**      | High                                                                                     |
| **Indicators**  | Flea market prices skyrocket, players only run "Meta" kits                               |

**Mitigation:**
1. Money Sinks (High repair costs, Taxes, Hideout upgrades)
2. Seasonal Wipes (Hard or Soft resets)
3. Dynamic Trader Pricing (Adjusts based on global supply)
4. "Black Swan" events that destabilize currency

**Contingency:**
- Emergency price adjustments
- Introduce new high-tier currency (e.g., Gold Bars)
- Force a mid-season wipe (Last Resort)

**Owner:** Economy Lead / Live Ops. **Review cadence:** Monthly (see [Scope Review & Planning](project-scope-review-and-planning.html) §5.3).

---

### Risk B4: Platform Policy Changes

| Aspect          | Details                                                                  |
| :-------------- | :----------------------------------------------------------------------- |
| **Risk**        | App store policy changes negatively impact game (30% cut, content rules) |
| **Probability** | Low-Medium                                                               |
| **Impact**      | High                                                                     |
| **Indicators**  | Policy announcements from Apple/Google                                   |

**Mitigation:**
1. Monitor platform policy changes
2. Prepare for multiple distribution channels
3. Build direct player relationships (email, Discord)
4. Budget assumes current revenue split

**Contingency:**
- Explore alternative payment methods (where legal)
- Adjust pricing to maintain margins
- Legal review of policy compliance

---

### Risk B5: Negative Launch Reviews

| Aspect          | Details                                     |
| :-------------- | :------------------------------------------ |
| **Risk**        | Poor reviews at launch tank discoverability |
| **Probability** | Medium                                      |
| **Impact**      | High                                        |
| **Indicators**  | Below 4.0 average on app stores             |

**Mitigation:**
1. Extensive soft launch for polish
2. Community beta for early feedback
3. Strong onboarding to reduce confusion
4. In-game review request timing optimization

**Contingency:**
- Rapid response to common complaints
- Update app store listing with fixes
- Request updated reviews after improvements

---

## 👥 Operational Risks

### Risk O1: Key Personnel Loss

| Aspect          | Details                                                     |
| :-------------- | :---------------------------------------------------------- |
| **Risk**        | Critical team members leave, losing institutional knowledge |
| **Probability** | Medium                                                      |
| **Impact**      | High                                                        |
| **Indicators**  | Turnover increases, knowledge gaps                          |

**Mitigation:**
1. Documentation culture (this GDD!)
2. Cross-training team members
3. Competitive compensation
4. Positive work culture

**Contingency:**
- Knowledge transfer protocols
- External contractor pool identified
- Recruiting pipeline maintained

---

### Risk O2: Scope Creep

| Aspect          | Details                                       |
| :-------------- | :-------------------------------------------- |
| **Risk**        | Feature requests expand scope beyond capacity |
| **Probability** | High                                          |
| **Impact**      | Medium                                        |
| **Indicators**  | Milestone slipping, team burnout              |

**Mitigation:**
1. Clear MVP definition
2. Change request process
3. Regular scope reviews
4. Feature prioritization framework

**Contingency:**
- Cut features not on critical path
- Delay non-essential features to post-launch
- Adjust timeline if quality at risk

---

### Risk O3: External Dependencies

| Aspect          | Details                                   |
| :-------------- | :---------------------------------------- |
| **Risk**        | Third-party services fail or change terms |
| **Probability** | Low-Medium                                |
| **Impact**      | Medium-High                               |
| **Indicators**  | Vendor communications, service outages    |

**Mitigation:**
1. Identify all external dependencies
2. Have backup vendors identified
3. Abstract integrations for portability
4. SLA monitoring

**Contingency:**
- Switch to backup vendor
- Build in-house solution (long-term)
- Negotiate with vendor

---

## 📊 Risk Tracking Matrix

| ID   | Risk                   | Probability | Impact      | Priority | Owner             | Status         |
| :--- | :--------------------- | :---------- | :---------- | :------- | :---------------- | :------------- |
| D1   | Core Loop Not Fun      | Medium      | Critical    | P0       | Game Director     | Monitoring     |
| D2   | Too Hardcore           | Medium-High | High        | P0       | Game Director     | Monitoring     |
| D3   | P2W Perception         | Medium      | Critical    | P0       | Producer          | Mitigated      |
| D4   | Cross-Platform Balance | High        | High        | P1       | Lead Designer     | Monitoring     |
| D5   | Content Drought        | Medium      | High        | P1       | Live Ops          | Planned        |
| T1   | Low-End Performance    | Medium      | High        | P1       | Tech Lead         | In Progress    |
| T2   | Network Latency        | Medium      | High        | P1       | Network Lead      | In Progress    |
| T3   | Cheating               | High        | Critical    | P0       | Security Lead     | In Progress    |
| T4   | Launch Scaling         | Medium      | Critical    | P0       | DevOps Lead       | Planned        |
| B1   | Market Competition     | Medium      | High        | P1       | Producer          | Monitoring     |
| B2   | Low Monetization       | Medium      | Critical    | P1       | Monetization Lead | Monitoring     |
| B3   | Platform Policies      | Low-Medium  | High        | P2       | Legal             | Monitoring     |
| B4   | Negative Reviews       | Medium      | High        | P1       | Community Lead    | Planned        |
| O1   | Key Personnel          | Medium      | High        | P1       | HR Lead           | Monitoring     |
| O2   | Scope Creep            | High        | Medium      | P1       | Producer          | Active Control |
| O3   | External Dependencies  | Low-Medium  | Medium-High | P2       | Tech Lead         | Documented     |

---

## 📅 Risk Review Schedule

| Frequency | Activity                                       |
| :-------- | :--------------------------------------------- |
| Weekly    | Team leads review active risks                 |
| Bi-weekly | Risk status update in sprint review            |
| Monthly   | Full risk matrix review with leadership; **D4 (Cross-Platform)** and **B3 (Economy inflation)** owners report (see [Scope Review & Planning](project-scope-review-and-planning.html) §5.3). |
| Quarterly | Risk retrospective and new risk identification |



