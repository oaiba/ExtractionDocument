---
title: "Localization Strategy"
type: docs
---

##  Localization Philosophy

**Core Principle:** "Speak the player's language, respect their culture"

Localization is NOT just translation. It includes:
- **Language translation** - Text, voice, UI
- **Cultural adaptation** - References, humor, imagery
- **Regional compliance** - Laws, ratings, content restrictions
- **Market customization** - Pricing, events, partnerships

---

##  Supported Languages

### Launch Languages (Tier 1)

| Language               | Code  | Region      | Priority | Notes                      |
| :--------------------- | :---- | :---------- | :------- | :------------------------- |
| **English**            | en-US | Global      | P0       | Source language            |
| **Simplified Chinese** | zh-CN | China       | P0       | Largest mobile market      |
| **Japanese**           | ja-JP | Japan       | P0       | High ARPU market           |
| **Korean**             | ko-KR | South Korea | P0       | Competitive gaming culture |
| **Portuguese (BR)**    | pt-BR | Brazil      | P0       | Largest LATAM market       |

### Post-Launch Languages (Tier 2)

| Language                | Code  | Region        | Target  |
| :---------------------- | :---- | :------------ | :------ |
| **Spanish (LATAM)**     | es-MX | Latin America | Month 2 |
| **Spanish (Spain)**     | es-ES | Spain         | Month 2 |
| **German**              | de-DE | Germany       | Month 2 |
| **French**              | fr-FR | France        | Month 2 |
| **Russian**             | ru-RU | Russia/CIS    | Month 3 |
| **Traditional Chinese** | zh-TW | Taiwan/HK     | Month 3 |
| **Thai**                | th-TH | Thailand      | Month 3 |
| **Vietnamese**          | vi-VN | Vietnam       | Month 3 |
| **Indonesian**          | id-ID | Indonesia     | Month 4 |
| **Turkish**             | tr-TR | Turkey        | Month 4 |
| **Arabic**              | ar-SA | MENA          | Month 6 |
| **Hindi**               | hi-IN | India         | Month 6 |

### Future Languages (Tier 3)

| Language | Code  | Region      | Consideration   |
| :------- | :---- | :---------- | :-------------- |
| Italian  | it-IT | Italy       | Based on demand |
| Polish   | pl-PL | Poland      | Based on demand |
| Dutch    | nl-NL | Netherlands | Based on demand |
| Swedish  | sv-SE | Scandinavia | Based on demand |

---

##  Text Localization

### Text Categories

| Category            | Volume          | Update Frequency   | Priority |
| :------------------ | :-------------- | :----------------- | :------- |
| **UI Text**         | ~2,000 strings  | Low (stable)       | P0       |
| **Gameplay Text**   | ~3,000 strings  | Medium             | P0       |
| **Quest/Narrative** | ~10,000 strings | High (new content) | P1       |
| **Marketing**       | ~500 strings    | Per campaign       | P1       |
| **Legal**           | ~200 strings    | Per region         | P0       |

### String Guidelines

**DO:**
```
 Use placeholder tokens: "You earned {0} credits"
 Provide context notes: [Button label, max 10 chars]
 Include plural forms: "{0} item" / "{0} items"
 Handle gender where needed: "He/She extracted"
 Keep strings modular: Avoid concatenation
```

**DON'T:**
```
 Hardcode numbers: "Kill 5 enemies" → "Kill {0} enemies"
 Embed formatting: "KILL enemies" → Mark as [UPPERCASE]
 Use idioms blindly: "Piece of cake" → "Easy task"
 Assume left-to-right: Support RTL layouts
 Ignore text expansion: German is ~30% longer than English
```

### Text Expansion Guidelines

| Source Language    | Average Expansion        |
| :----------------- | :----------------------- |
| English → German   | +30%                     |
| English → French   | +20%                     |
| English → Spanish  | +25%                     |
| English → Japanese | -10% (but height needed) |
| English → Chinese  | -30% (but height needed) |
| English → Arabic   | +25% (plus RTL)          |

**UI Design Consideration:**
- Buttons: Allow 150% text width
- Labels: Use dynamic sizing
- Tooltips: No fixed width

### Localization File Format

**Structure (JSON example):**
```json
{
  "ui.button.play": {
    "en-US": "PLAY",
    "zh-CN": "开始游戏",
    "ja-JP": "プレイ",
    "context": "Main menu button, max 8 chars",
    "maxLength": 8
  },
  "gameplay.kill.notification": {
    "en-US": "You eliminated {playerName}",
    "zh-CN": "你击败了 {playerName}",
    "ja-JP": "{playerName}を倒した",
    "context": "Kill notification, {playerName} is victim",
    "variables": ["playerName"]
  }
}
```

---

##  Voice Localization

### Voice Strategy

| Content Type             | Localization Approach        | Languages                |
| :----------------------- | :--------------------------- | :----------------------- |
| **Operator Voice Lines** | Full dub                     | Tier 1 only              |
| **Quest NPC Dialogue**   | Full dub                     | Tier 1 + Selected Tier 2 |
| **Tutorial VO**          | Full dub                     | All supported languages  |
| **Announcer**            | Full dub                     | Tier 1 only              |
| **Ambient Chatter**      | Keep original (authenticity) | N/A                      |

### Voice Casting Guidelines

**Operator Voices:**
- Match personality across languages
- Maintain age/gender consistency
- Allow regional accents (character backstory permitting)
- Record same emotional range

**Recording Specs:**
- Format: WAV, 48kHz, 24-bit
- Environment: Professional studio, noise floor < -60dB
- Delivery: Dry recordings, no processing

---

##  Visual Localization

### UI Adaptations

**Right-to-Left (RTL) Languages:**
- Arabic, Hebrew, Persian
- Mirror entire UI layout
- Keep numbers left-to-right
- Adjust text alignment

**Vertical Text Support:**
- Japanese, Chinese, Korean can be vertical
- Currently: Horizontal only (no vertical mode planned)

### Icon & Image Localization

| Element                       | Localization Required                        |
| :---------------------------- | :------------------------------------------- |
| Universal icons (play, pause) | No                                           |
| Text-in-image                 | Yes (create variants)                        |
| Cultural symbols              | Review per region                            |
| Hand gestures                 | Review (thumbs up OK globally)               |
| Colors                        | Review (red = luck in China, danger in West) |

### Font Requirements

| Language    | Font Family          | Notes            |
| :---------- | :------------------- | :--------------- |
| Latin-based | Roboto, Inter        | Default          |
| Chinese     | Noto Sans SC/TC      | Full CJK support |
| Japanese    | Noto Sans JP         | Full CJK support |
| Korean      | Noto Sans KR         | Full CJK support |
| Arabic      | Noto Sans Arabic     | RTL support      |
| Thai        | Noto Sans Thai       | Complex script   |
| Hindi       | Noto Sans Devanagari | Complex script   |

---

##  Cultural Adaptation

### Content Review Categories

**Violence & Gore:**
| Region    | Consideration                            |
| :-------- | :--------------------------------------- |
| China     | No blood/skulls, modify death animations |
| Germany   | Review for USK rating                    |
| Australia | Review for ACB rating                    |
| Japan     | CERO rating requirements                 |

**Religious & Political:**
| Region | Consideration                         |
| :----- | :------------------------------------ |
| Global | Avoid real-world religious symbols    |
| China  | No political references, map accuracy |
| MENA   | Review cultural sensitivities         |

**Gambling Mechanics:**
| Region      | Consideration                   |
| :---------- | :------------------------------ |
| Belgium     | Loot boxes may require changes  |
| Netherlands | Probability disclosure required |
| China       | Require probability disclosure  |
| Japan       | Gacha regulations apply         |

### Holiday & Event Localization

| Holiday        | Regions               | Adaptation                      |
| :------------- | :-------------------- | :------------------------------ |
| Lunar New Year | China, Korea, Vietnam | Culturally accurate decorations |
| Golden Week    | Japan                 | Timing consideration            |
| Ramadan        | MENA                  | Sensitive scheduling            |
| Christmas      | Western               | Optional, secular presentation  |
| Diwali         | India                 | Future consideration            |

---

##  Regional Pricing

### Price Tier System

| Tier       | Example Regions        | USD Equivalent | Adjustment |
| :--------- | :--------------------- | :------------- | :--------- |
| **Tier 1** | US, EU, Japan, Korea   | $9.99          | Baseline   |
| **Tier 2** | Brazil, Mexico, Russia | ~$5-7          | -30-50%    |
| **Tier 3** | SEA, India             | ~$3-5          | -50-70%    |
| **Tier 4** | Developing markets     | ~$1-3          | -70-90%    |

### Currency Display

**Format by Region:**
| Region | Format Example |
| :----- | :------------- |
| US     | $9.99          |
| EU     | €9,99          |
| UK     | £8.99          |
| Japan  | ¥980           |
| Korea  | ₩12,000        |
| Brazil | R$29,99        |
| China  | ¥68.00 (CNY)   |

---

##  Localization Process

### Workflow

```
1. String Freeze (Dev)
   ├── All new strings marked for localization
   └── Context and variables documented

2. Export to TMS (Translation Management System)
   ├── Strings extracted to platform
   └── Assigned to translators

3. Translation (External Partners)
   ├── Professional translation
   └── Native speaker review

4. Import & Integration (Dev)
   ├── Strings imported to game
   └── Build with localized content

5. LQA (Localization QA)
   ├── In-context testing
   ├── Text fit verification
   └── Cultural review

6. Release
   └── Localized build published
```

### Timeline per Language

| Phase       | Duration                   |
| :---------- | :------------------------- |
| Translation | 5-7 days                   |
| Review      | 2-3 days                   |
| Integration | 1 day                      |
| LQA         | 3-5 days                   |
| **Total**   | **2-3 weeks per language** |

### Quality Metrics

| Metric                          | Target            |
| :------------------------------ | :---------------- |
| Translation accuracy            | 98%+              |
| UI text fit                     | 100%              |
| Cultural issues                 | 0 critical        |
| Player complaints (loc-related) | < 0.1% of tickets |

---

##  Technical Implementation

### Localization System

**Runtime Language Switching:**
- Player can change language anytime
- UI updates immediately
- Voice requires restart (asset loading)

**Fallback Logic:**
```
Player language preference
    ↓
Exact match (zh-CN)
    ↓ (if not available)
Language family match (zh → zh-TW)
    ↓ (if not available)
English fallback (en-US)
```

### Asset Organization

```
/Localization/
├── /Strings/
│   ├── en-US.json
│   ├── zh-CN.json
│   └── ja-JP.json
├── /Audio/
│   ├── /en-US/
│   ├── /zh-CN/
│   └── /ja-JP/
├── /Fonts/
│   ├── Latin.ttf
│   ├── CJK.ttf
│   └── Arabic.ttf
└── /Images/
    ├── /en-US/
    └── /zh-CN/
```

---

##  Localization Metrics

### Per-Language KPIs

| Metric                | How to Measure                 |
| :-------------------- | :----------------------------- |
| Market penetration    | Players by language            |
| Revenue by language   | IAP per language               |
| Retention by language | D7/D30 per language            |
| Support tickets (loc) | Tickets mentioning translation |
| Community sentiment   | Forum/social feedback          |

### Localization ROI

**Expected Impact:**
- Localized markets typically see 2-5x higher conversion
- Voice localization adds 10-20% engagement
- Poor localization = negative reviews, lower ratings



