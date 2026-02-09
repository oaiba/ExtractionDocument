---
title: "Economy & Monetization Design"
type: docs
---
# Economy & Monetization Design

**[← Previous: Progression](./Progression.md)** | **[Index](../README.md)** | **[Next: Live Ops →](./LiveOps.md)**

---

## Overview

This document defines the **monetization strategy, currency design, pricing structure, and anti-fraud measures** for the game's economy. Focused on ethical monetization that respects player time and investment.

**Related Documents:**
- [Items & In-Game Economy](../Combat/Items.md) - Item values, marketplace, trading
- [Progression](./Progression.md) - XP, leveling, Battle Pass
- [Live Ops](./LiveOps.md) - Events, seasonal content

---

## Philosophy

### Core Principles

| Principle               | Description                               | Implementation                  |
| :---------------------- | :---------------------------------------- | :------------------------------ |
| **No Pay-to-Win**       | Real money cannot buy gameplay advantages | Paid items are cosmetic only    |
| **Respect Player Time** | Free players can progress meaningfully    | All content earnable eventually |
| **Transparent Value**   | Players always know what they're buying   | No loot boxes with hidden odds  |
| **Fair Pricing**        | Prices match regional purchasing power    | Regional pricing adjustments    |
| **Player Investment**   | Spending feels rewarding, not required    | Cosmetics enhance experience    |

### Monetization Goals

1. **Sustainable Revenue** - Long-term player spending over whale hunting
2. **Player Satisfaction** - Happy players spend more over time
3. **Competitive Integrity** - Gear parity between free and paying players
4. **Community Trust** - Transparent practices build loyalty

---

## Currency System

### Currency Types

| Currency       | Type        | Acquisition     | Primary Use                         |
| :------------- | :---------- | :-------------- | :---------------------------------- |
| **Credits**    | Soft        | Gameplay earned | Weapons, gear, repairs              |
| **Tokens**     | Premium     | Purchased       | Cosmetics, Battle Pass, convenience |
| **Reputation** | Progression | Faction quests  | Faction rewards, unlocks            |

---

### Credits (Soft Currency)

**Primary in-game currency for gameplay progression**

**Earning Methods:**
| Source                | Amount        | Frequency     |
| :-------------------- | :------------ | :------------ |
| Successful extraction | $500-3,000    | Per match     |
| Selling loot          | Varies        | Per match     |
| Quest completion      | $1,000-10,000 | Per quest     |
| Daily login           | $500-5,000    | Day 1-7 cycle |
| Level up              | $500-2,000    | Per level     |
| Achievement           | $1,000-25,000 | One-time      |

**Typical Player Balance:**
- New player: $10,000 (starting balance)
- Casual player: $30,000-80,000
- Active player: $100,000-300,000
- Veteran player: $300,000-1,000,000

**Credit Sinks:**
- Weapon purchases: $500-25,000
- Armor purchases: $800-15,000
- Medical supplies: $50-2,500
- Stash expansion: $10,000-50,000
- Marketplace fees: 15% of transactions
- Repair costs (future): 10-30% of item value

---

### Tokens (Premium Currency)

**Real-money currency for cosmetics and convenience**

**Token Bundles:**

| Bundle   | Tokens | Price (USD) | Bonus | Value/Token |
| :------- | :----- | :---------- | :---- | :---------- |
| Starter  | 100    | $0.99       | 0%    | $0.0099     |
| Small    | 500    | $4.99       | 0%    | $0.0100     |
| Medium   | 1,100  | $9.99       | 10%   | $0.0091     |
| Large    | 2,400  | $19.99      | 20%   | $0.0083     |
| Mega     | 5,200  | $39.99      | 30%   | $0.0077     |
| Ultimate | 11,000 | $79.99      | 37.5% | $0.0073     |

**Regional Pricing:**
| Region        | Price Adjustment | Example ($9.99 USD) |
| :------------ | :--------------- | :------------------ |
| US/EU/Tier 1  | 100%             | $9.99               |
| Brazil/SEA    | 60-70%           | ~$6.99              |
| India/LATAM   | 45-55%           | ~$4.99              |
| Africa/Tier 3 | 30-40%           | ~$3.99              |

**Token Spending:**
| Item                      | Token Cost | USD Equivalent |
| :------------------------ | :--------- | :------------- |
| Operator Skin (Common)    | 200        | ~$2            |
| Operator Skin (Rare)      | 500        | ~$5            |
| Operator Skin (Epic)      | 1,000      | ~$10           |
| Operator Skin (Legendary) | 2,000      | ~$20           |
| Weapon Skin (Rare)        | 300        | ~$3            |
| Weapon Skin (Epic)        | 700        | ~$7            |
| Weapon Skin (Legendary)   | 1,500      | ~$15           |
| Emote                     | 200-500    | ~$2-5          |
| Spray/Voice Line          | 100-200    | ~$1-2          |
| Battle Pass               | 1,000      | ~$10           |
| Battle Pass + 25 Tiers    | 2,500      | ~$25           |

**Cannot Buy With Tokens:**
- Weapons
- Armor
- Gameplay-affecting items
- Operators (unlock through gameplay)
- Experience points
- Rank rating

---

### Reputation (Faction Currency)

**Earned through faction quests, cannot be purchased**

| Faction       | Standing | Rep Required | Unlock Examples   |
| :------------ | :------- | :----------- | :---------------- |
| Salvage Corps | Neutral  | 0            | Basic quests      |
| Salvage Corps | Friendly | 1,000        | Faction cosmetics |
| Salvage Corps | Honored  | 5,000        | Unique weapons    |
| Salvage Corps | Revered  | 15,000       | Exclusive gear    |
| Salvage Corps | Exalted  | 50,000       | Legendary rewards |

**Reputation cannot be purchased** - Preserves prestige of faction rewards.

---

## Monetization Structure

### Battle Pass

**The primary monetization driver - fair value for player investment**

**Battle Pass Tiers:**
| Track              | Price               | Tiers             | Rewards                         |
| :----------------- | :------------------ | :---------------- | :------------------------------ |
| Free Track         | Free                | 100               | Credits, basic cosmetics, XP    |
| Premium Track      | 1,000 Tokens (~$10) | 100               | All above + exclusive cosmetics |
| Premium + 25 Tiers | 2,500 Tokens (~$25) | 100 (start at 26) | Accelerated progress            |

**Battle Pass Value:**
- Total Premium value: ~15,000 Tokens worth of content
- Player pays: 1,000 Tokens
- Value ratio: 15:1 (player gets 15x what they pay)
- Token earning: 300 Tokens included in Premium track
- **Net cost if continuing**: 700 Tokens per season

**Season Duration:** 90 days (3 months)

**Design Philosophy:**
- Completing free track shows value
- Premium feels like upgrade, not requirement
- Returns tokens to encourage re-purchase
- Progression feels achievable (1 hour/day = complete by season end)

---

### Direct Purchase Store

**Rotating cosmetic shop with fair pricing**

**Store Structure:**
| Section          | Refresh     | Items          | Price Range      |
| :--------------- | :---------- | :------------- | :--------------- |
| Daily Featured   | 24 hours    | 4 items        | 200-2,000 Tokens |
| Weekly Featured  | 7 days      | 6 items        | 500-3,000 Tokens |
| Always Available | Permanent   | Core cosmetics | 100-1,500 Tokens |
| Limited Time     | Event-based | Exclusive      | 500-2,500 Tokens |

**Bundle Discounts:**
| Bundle Type                      | Discount | Example                      |
| :------------------------------- | :------- | :--------------------------- |
| Operator Bundle (Skin + 3 items) | 25% off  | 1,500 vs 2,000 if separate   |
| Weapon Bundle (5 matching skins) | 30% off  | 1,400 vs 2,000 if separate   |
| Starter Pack (Best value, once)  | 50% off  | 2,000 value for 1,000 Tokens |

**Starter Pack (New Player Special):**
- 1 Epic Operator Skin
- 2 Rare Weapon Skins
- 500 Tokens bonus
- 10,000 Credits
- 3-Day XP Boost
- Price: $4.99 (one-time purchase)
- Value: ~$15 worth of content

---

### Convenience Items

**Time-savers that don't affect gameplay balance**

| Item              | Price (Tokens) | Effect              | Balance                 |
| :---------------- | :------------- | :------------------ | :---------------------- |
| XP Boost (1 Day)  | 150            | +25% Account XP     | Does not affect gear    |
| XP Boost (7 Days) | 800            | +25% Account XP     | Cosmetic unlocks faster |
| Stash Upgrade     | 500            | +20 stash slots     | Quality of life         |
| Name Change       | 300            | Change display name | Unlimited               |
| Loadout Slot      | 200            | +1 loadout preset   | Convenience             |

**NOT Sold:**
- Weapon boosts
- Armor boosts
- Damage increases
- Speed increases
- Anything affecting PvP balance

---

## Pricing Philosophy

### Price Anchoring

**Strategic pricing to guide purchase decisions:**

| Tier          | Purpose                    | Example               |
| :------------ | :------------------------- | :-------------------- |
| Low Anchor    | Entry point, easy decision | 100 Token spray       |
| Mid Anchor    | Standard purchase          | 500 Token skin        |
| High Anchor   | Premium option             | 2,000 Token legendary |
| Bundle Anchor | "Best value" perception    | Bundle saves 25%      |

### Psychological Fairness

**Practices we AVOID:**
- ❌ Hidden odds (all chances disclosed)
- ❌ FOMO manipulation (items can return)
- ❌ Artificial scarcity (no fake limited editions)
- ❌ Pay-to-win mechanics
- ❌ Aggressive pop-up ads
- ❌ Dark patterns in UI

**Practices we EMBRACE:**
- ✅ Clear value communication
- ✅ Refund window (24 hours, unused items)
- ✅ Purchase confirmation prompts
- ✅ Spending history accessible
- ✅ Parental controls available
- ✅ Regional pricing

---

## Marketplace Economy

**Player-to-player trading for in-game items**

*See [Items & Economy](../Combat/Items.md) for detailed marketplace rules*

### Marketplace Overview

| Feature     | Description                         |
| :---------- | :---------------------------------- |
| Currency    | Credits only (not Tokens)           |
| Listing Fee | 5% of asking price (non-refundable) |
| Sale Tax    | 10% of final price                  |
| Duration    | 24, 48, or 72 hours                 |
| Bid System  | Auction with buyout option          |

### Price Controls

**Preventing market manipulation:**

| Control        | Implementation                              |
| :------------- | :------------------------------------------ |
| Price Floor    | Items cannot sell below vendors             |
| Price Ceiling  | Max 10x average historical price            |
| Rate Limit     | 50 transactions per day per player          |
| Volume Limit   | Cannot corner market (max 20% of item type) |
| Velocity Alert | Rapid price changes trigger review          |

---

## Anti-Fraud Systems

### Payment Fraud Prevention

**Multi-layer fraud detection:**

| Layer      | Detection Method          | Action                    |
| :--------- | :------------------------ | :------------------------ |
| Device     | Device fingerprinting     | Flag new device purchases |
| Behavior   | Unusual spending patterns | Manual review trigger     |
| Velocity   | Rapid purchases           | Temporary lock            |
| Chargeback | Dispute detection         | Account suspension        |
| Geographic | IP location mismatch      | Additional verification   |

**Fraud Response:**
| Offense             | Action                               |
| :------------------ | :----------------------------------- |
| First chargeback    | Warning + account restriction        |
| Second chargeback   | Permanent purchase ban               |
| Fraudulent payment  | Account suspension + legal action    |
| Credit card testing | IP ban + report to payment processor |

### Account Security

**Protecting player investments:**

| Feature                   | Description                          |
| :------------------------ | :----------------------------------- |
| Two-Factor Authentication | Required for large purchases         |
| Login Notifications       | Email alerts for new devices         |
| Purchase Confirmation     | PIN/biometric for transactions       |
| Trade Lock                | 7-day lock after password change     |
| Recovery Verification     | ID verification for account recovery |

### RMT (Real Money Trading) Prevention

**Stopping unauthorized cash-for-items trading:**

| Detection          | Method                               |
| :----------------- | :----------------------------------- |
| Unusual trades     | Tracking item value vs trade value   |
| Account linking    | Multiple accounts trading frequently |
| Price manipulation | Selling items far below value        |
| Currency mules     | Accounts that only receive/send      |

**RMT Consequences:**
| Severity            | Action                            |
| :------------------ | :-------------------------------- |
| Suspected           | Investigation, trade monitoring   |
| Confirmed (Buyer)   | 7-day ban, item removal           |
| Confirmed (Seller)  | Permanent ban                     |
| Organized operation | Legal action, all accounts banned |

### Bot/Automation Prevention

| Protection         | Implementation                 |
| :----------------- | :----------------------------- |
| CAPTCHA            | On suspicious login patterns   |
| Device attestation | Mobile device verification     |
| Behavior analysis  | Inhuman play patterns detected |
| Rate limiting      | API calls throttled            |

---

## Spending Protections

### Spending Limits

**Voluntary controls for responsible spending:**

| Feature        | Default  | Customizable              |
| :------------- | :------- | :------------------------ |
| Daily Limit    | No limit | $1-500/day                |
| Weekly Limit   | No limit | $5-1,000/week             |
| Monthly Limit  | No limit | $20-5,000/month           |
| Cooling Period | Off      | 24-72 hour purchase delay |

**How to Enable:**
1. Settings → Account → Spending Controls
2. Set desired limits
3. Confirm with password
4. Limits active for 90 days (cannot remove early)

### Parental Controls

| Control           | Function                                |
| :---------------- | :-------------------------------------- |
| Purchase PIN      | Required for any real-money transaction |
| Disable Purchases | Completely block IAP                    |
| Spending Reports  | Weekly email summaries                  |
| Age Verification  | Required for account creation           |
| Content Filters   | Chat and content restrictions           |

### Refund Policy

| Condition                    | Refund Available                             |
| :--------------------------- | :------------------------------------------- |
| Unused item, within 24 hours | ✅ Full refund (Tokens returned)              |
| Unused item, 24-72 hours     | ✅ 75% refund                                 |
| Used item                    | ❌ No refund                                  |
| Technical error              | ✅ Case-by-case review                        |
| Accidental purchase          | ✅ First 3 times per account                  |
| Real currency                | ❌ Per platform policy (App Store/Play Store) |

---

## Economic Health Metrics

### Key Performance Indicators

| Metric               | Healthy Range | Warning Range    |
| :------------------- | :------------ | :--------------- |
| ARPDAU (Revenue/DAU) | $0.05-0.15    | <$0.03 or >$0.30 |
| Conversion Rate      | 2-5%          | <1% or >10%      |
| Payer ARPPU          | $15-40/month  | <$10 or >$80     |
| D7 Payer Retention   | 60-80%        | <50%             |
| D30 Payer Retention  | 40-60%        | <30%             |
| Refund Rate          | <2%           | >5%              |
| Chargeback Rate      | <0.5%         | >1%              |

### Economy Health

| Metric                | Healthy Range    | Warning                     |
| :-------------------- | :--------------- | :-------------------------- |
| Credit inflation rate | <5%/month        | >10%/month                  |
| Average player wealth | $50K-150K        | <$20K or >$500K             |
| Market activity       | 60%+ trade/month | <30%                        |
| Price volatility      | <20% week/week   | >50%                        |
| Gini coefficient      | <0.4             | >0.6 (wealth concentration) |

### Intervention Triggers

| Condition                   | Automatic Response      |
| :-------------------------- | :---------------------- |
| Inflation >10%/month        | Increase credit sinks   |
| Deflation (prices falling)  | Reduce loot spawn rates |
| Market dead (<10% activity) | Lower marketplace fees  |
| Item scarcity               | Increase spawn rate     |
| Whale domination            | Transaction limits      |

---

## Ethical Monetization Guidelines

### What We Promise Players

1. **Transparent Pricing** - No hidden costs, clear token-to-dollar value
2. **Achievable F2P** - Free players can compete and have fun
3. **No Gambling** - No loot boxes with random valuable items
4. **Purchase Clarity** - Always know exactly what you're buying
5. **Fair Refunds** - Reasonable refund policy for mistakes
6. **Privacy Respect** - Spending data not shared externally

### Design Rules for Monetization Team

| Rule                              | Rationale                         |
| :-------------------------------- | :-------------------------------- |
| Never create false urgency        | Builds long-term trust            |
| Never hide true costs             | Prevents regret, reduces refunds  |
| Never target vulnerable players   | Ethical responsibility            |
| Never lock content behind paywall | Gameplay equality                 |
| Always offer free path            | Respects all player types         |
| Always show odds                  | Legal requirement in many regions |

### Legal Compliance

| Region       | Requirement           | Our Compliance               |
| :----------- | :-------------------- | :--------------------------- |
| EU           | GDPR data protection  | Full compliance              |
| Belgium      | Loot box ban          | No loot boxes                |
| China        | Odds disclosure       | N/A (no random purchases)    |
| South Korea  | Refund rights         | Extended refund window       |
| COPPA (US)   | Children's protection | Age gate + parental controls |
| Apple/Google | Platform IAP rules    | 100% through official store  |

---

## Revenue Projections

### Revenue Mix (Target)

| Source           | % of Revenue | Strategy              |
| :--------------- | :----------- | :-------------------- |
| Battle Pass      | 40%          | Primary, predictable  |
| Direct Cosmetics | 30%          | Event-driven          |
| Token Bundles    | 15%          | Convenience purchases |
| Starter Packs    | 10%          | New player conversion |
| Convenience      | 5%           | Minimal reliance      |

### Player Spending Tiers

| Tier       | % of Players | Monthly Spend | % of Revenue |
| :--------- | :----------- | :------------ | :----------- |
| Non-Payers | 95%          | $0            | 0%           |
| Minnows    | 3%           | $1-10         | 15%          |
| Dolphins   | 1.5%         | $10-50        | 35%          |
| Whales     | 0.5%         | $50+          | 50%          |

**Goal:** Increase minnow/dolphin conversion, reduce whale dependency.

---

## Implementation Timeline

### Launch (v1.0)
- ✅ Soft currency (Credits)
- ✅ Premium currency (Tokens)
- ✅ Battle Pass (Free + Premium)
- ✅ Direct purchase store
- ✅ Basic anti-fraud

### Post-Launch (v1.1-1.3)
- 📋 Marketplace (player trading)
- 📋 Enhanced fraud detection
- 📋 Spending controls
- 📋 Regional pricing optimization

### Future Updates
- 📋 Gifting system
- 📋 Season bundles
- 📋 Crew/Clan cosmetics
- 📋 Tournament prizes

---

## Summary

| Aspect              | Our Approach                                    |
| :------------------ | :---------------------------------------------- |
| **Revenue Model**   | Cosmetic-only, Battle Pass primary              |
| **Player Fairness** | No pay-to-win, all gameplay earnable            |
| **Pricing**         | Regional adjustment, clear value                |
| **Security**        | Multi-layer fraud prevention                    |
| **Ethics**          | Transparent, responsible, compliant             |
| **Goal**            | Sustainable revenue through player satisfaction |

---

**[← Previous: Progression](./Progression.md)** | **[Index](../README.md)** | **[Next: Live Ops →](./LiveOps.md)**


