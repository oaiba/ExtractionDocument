# Localization System - Technical Specification

**[← Back to Index](../README.md)** | **[Next: Accessibility System →](./AccessibilitySystem.md)**

**Reference:** [High-Level Localization Design](../../GDD_HighLevel/GameDesign/Localization.md)

---

## Overview

The **Localization System** handles multi-language support, text management, font loading, and cultural adaptation.

---

## Enums & Types

### Language
Supported languages organized by launch tier priority.

**Tier 1 - Launch Languages:**

| Code Name | Display Name   | Locale | Script | Voice    | Font         | Description         |
| :-------- | :------------- | :----- | :----- | :------- | :----------- | :------------------ |
| `L_en_US` | English (US)   | en-US  | Latin  | Full Dub | Roboto       | Source language     |
| `L_zh_CN` | 简体中文       | zh-CN  | CJK    | Full Dub | Noto Sans SC | Simplified Chinese  |
| `L_ja_JP` | 日本語         | ja-JP  | CJK    | Full Dub | Noto Sans JP | Japanese            |
| `L_ko_KR` | 한국어         | ko-KR  | CJK    | Full Dub | Noto Sans KR | Korean              |
| `L_pt_BR` | Português (BR) | pt-BR  | Latin  | Full Dub | Roboto       | Portuguese (Brazil) |

**Tier 2 - Post-Launch Languages:**

| Code Name | Display Name     | Locale | Script   | Voice     | Font           | Description             |
| :-------- | :--------------- | :----- | :------- | :-------- | :------------- | :---------------------- |
| `L_es_MX` | Español (LATAM)  | es-MX  | Latin    | Partial   | Roboto         | Spanish (Latin America) |
| `L_es_ES` | Español (España) | es-ES  | Latin    | Partial   | Roboto         | Spanish (Spain)         |
| `L_de_DE` | Deutsch          | de-DE  | Latin    | Partial   | Roboto         | German                  |
| `L_fr_FR` | Français         | fr-FR  | Latin    | Partial   | Roboto         | French                  |
| `L_ru_RU` | Русский          | ru-RU  | Cyrillic | Partial   | Roboto         | Russian                 |
| `L_zh_TW` | 繁體中文         | zh-TW  | CJK      | Subtitles | Noto Sans TC   | Traditional Chinese     |
| `L_th_TH` | ภาษาไทย          | th-TH  | Thai     | Subtitles | Noto Sans Thai | Thai                    |
| `L_vi_VN` | Tiếng Việt       | vi-VN  | Latin    | Subtitles | Roboto         | Vietnamese              |
| `L_id_ID` | Bahasa Indonesia | id-ID  | Latin    | Subtitles | Roboto         | Indonesian              |
| `L_tr_TR` | Türkçe           | tr-TR  | Latin    | Subtitles | Roboto         | Turkish                 |

**Tier 3 - Future Languages:**

| Code Name | Display Name | Locale | Script       | Voice     | Font                 | Description |
| :-------- | :----------- | :----- | :----------- | :-------- | :------------------- | :---------- |
| `L_ar_SA` | العربية      | ar-SA  | Arabic (RTL) | Subtitles | Noto Sans Arabic     | Arabic      |
| `L_hi_IN` | हिन्दी          | hi-IN  | Devanagari   | Subtitles | Noto Sans Devanagari | Hindi       |

---

### TextCategory
Text string category for localization management.

| Code Name      | Display Name    | Priority | Context               | Example               |
| :------------- | :-------------- | :------- | :-------------------- | :-------------------- |
| `TC_UI`        | UI              | Critical | Buttons, labels       | "PLAY", "SETTINGS"    |
| `TC_Gameplay`  | Gameplay        | Critical | In-game text          | "Reload", "2 enemies" |
| `TC_Quest`     | Quest/Narrative | High     | Dialogue, quests      | Quest descriptions    |
| `TC_Marketing` | Marketing       | Medium   | Store, promotions     | Sale banners          |
| `TC_Legal`     | Legal           | Low      | Terms, privacy        | Legal documents       |
| `TC_Tutorial`  | Tutorial        | High     | Help, onboarding      | Tutorial tips         |
| `TC_System`    | System          | Critical | Errors, notifications | Error messages        |

---

### FontFamily
Font family for language script support.

| Code Name       | Display Name | Languages                      | Primary Font         | Size Mult | Description               |
| :-------------- | :----------- | :----------------------------- | :------------------- | :-------- | :------------------------ |
| `FF_Latin`      | Latin        | EN, ES, FR, DE, PT, VI, ID, TR | Roboto               | 1.0×      | Latin script languages    |
| `FF_CJK`        | CJK          | ZH, JA, KO                     | Noto Sans CJK        | 1.1×      | Chinese, Japanese, Korean |
| `FF_Cyrillic`   | Cyrillic     | RU                             | Roboto               | 1.0×      | Russian, Ukrainian        |
| `FF_Arabic`     | Arabic       | AR                             | Noto Sans Arabic     | 1.0×      | Arabic (RTL)              |
| `FF_Thai`       | Thai         | TH                             | Noto Sans Thai       | 1.0×      | Thai script               |
| `FF_Devanagari` | Devanagari   | HI                             | Noto Sans Devanagari | 1.0×      | Hindi script              |

---

### TextDirection
Text direction for layout management.

| Code Name | Display Name  | UI Mirror | Text Align | Languages            |
| :-------- | :------------ | :-------- | :--------- | :------------------- |
| `TD_LTR`  | Left-to-Right | No        | Left       | EN, ZH, JA, KO, etc. |
| `TD_RTL`  | Right-to-Left | Yes       | Right      | AR (Arabic)          |

---

### VoiceLocStrategy
Voice localization strategy per language.

| Code Name           | Display Name   | Coverage | Languages          | Description                |
| :------------------ | :------------- | :------- | :----------------- | :------------------------- |
| `VLS_FullDub`       | Full Dub       | 100%     | EN, ZH, JA, KO, PT | All dialogue dubbed        |
| `VLS_PartialDub`    | Partial Dub    | 30-50%   | DE, FR, ES         | Key lines only             |
| `VLS_SubtitlesOnly` | Subtitles Only | 0%       | TH, VI, ID, TR, AR | Original audio + subtitles |

---

### TextExpansion
Text expansion rate from English source.

| Code Name         | Display Name  | Expansion | Design Buffer | Description              |
| :---------------- | :------------ | :-------- | :------------ | :----------------------- |
| `TE_Compact`      | Compact       | -30%      | 0%            | ZH, JA (character-based) |
| `TE_Normal`       | Normal        | 0%        | 20%           | EN (source)              |
| `TE_Expanded`     | Expanded      | +20%      | 30%           | FR, ES                   |
| `TE_VeryExpanded` | Very Expanded | +30%      | 50%           | DE, AR                   |

---

## Code Names

### System Events

| Code Name              | Trigger        | Parameters        | Description                  |
| :--------------------- | :------------- | :---------------- | :--------------------------- |
| `LOC_LANGUAGE_CHANGED` | Language set   | OldLang, NewLang  | Language preference changed  |
| `LOC_STRING_LOADED`    | Strings loaded | Language, Count   | Localization file loaded     |
| `LOC_STRING_MISSING`   | Key not found  | Key, Language     | Missing translation fallback |
| `LOC_FALLBACK_USED`    | Fallback used  | Key, FallbackLang | Non-primary language used    |
| `LOC_FONT_CHANGED`     | Font switched  | FontFamily        | Font family changed          |
| `LOC_FONT_LOADED`      | Font loaded    | FontFamily, Size  | Font asset loaded            |

### Validation Events

| Code Name                 | Trigger          | Parameters              | Description                     |
| :------------------------ | :--------------- | :---------------------- | :------------------------------ |
| `LOC_VALIDATION_START`    | Validation began | Language                | Localization validation started |
| `LOC_VALIDATION_COMPLETE` | Validation done  | Language, MissingCount  | Validation finished             |
| `LOC_OVERFLOW_DETECTED`   | Text too long    | Key, Language, Overflow | Text exceeds max length         |
| `LOC_VARIABLE_MISMATCH`   | Variables differ | Key, Expected, Found    | Variable count mismatch         |

### Voice Events

| Code Name            | Trigger            | Parameters        | Description            |
| :------------------- | :----------------- | :---------------- | :--------------------- |
| `LOC_VOICE_LOADED`   | Voice pack loaded  | Language, Size    | Voice audio loaded     |
| `LOC_VOICE_SWITCHED` | Voice language set | OldLang, NewLang  | Voice language changed |
| `LOC_VOICE_MISSING`  | Voice not found    | VoiceID, Language | Missing voice fallback |

---

## Architecture

### Localization Manager

**Purpose:** Manage language settings, text retrieval, and font loading.

```
CLASS LocalizationManager:
    currentLanguage: Language
    stringTable: Map<String, String>
    
    // Events
    OnLanguageChanged: Event<(OldLang, NewLang)>
    
    FUNCTION SetLanguage(language: Language):
        oldLang = currentLanguage
        currentLanguage = language
        
        LoadStrings(language)
        UpdateFonts(language)
        
        EMIT EVENT "LOC_LANGUAGE_CHANGED" WITH (oldLang, language)
        OnLanguageChanged.Broadcast(oldLang, language)
    END FUNCTION
    
    FUNCTION GetLocalizedText(key: String) -> String:
        IF stringTable.ContainsKey(key):
             RETURN stringTable[key]
        END IF
        
        EMIT EVENT "LOC_STRING_MISSING" WITH (key, currentLanguage)
        RETURN GetFallbackText(key)
    END FUNCTION
    
    FUNCTION GetLocalizedTextFormatted(key: String, args: List<String>) -> String:
        template = GetLocalizedText(key)
        RETURN FormatText(template, args)
    END FUNCTION
    
    FUNCTION GetPluralText(key: String, count: Integer) -> String:
        template = GetLocalizedText(key)
        RETURN GetPluralForm(template, count)
    END FUNCTION
    
    FUNCTION GetFontForLanguage(language: Language) -> FontAsset:
        config = FontRegistry[language]
        RETURN LoadFont(config.PrimaryFont)
    END FUNCTION
    
    FUNCTION FormatText(template: String, args: List<String>) -> String:
        result = template
        FOR i = 0 TO args.Count - 1:
            result = result.Replace("{" + i + "}", args[i])
        END FOR
        RETURN result
    END FUNCTION
```

---

## Data Structures

```
STRUCT LocString:
    Key: String
    Translations: Map<Language, String>
    Context: String
    MaxLength: Integer = 0
    bSupportsPlural: Boolean = false
    Variables: List<String>

STRUCT FontConfig:
    Language: Language
    FontFamily: FontFamily
    PrimaryFont: AssetPath
    FallbackFont: AssetPath
    SizeMultiplier: Float = 1.0

STRUCT RTLLayoutHelper:
    FUNCTION ApplyRTLLayout(widget: Widget):
        // Mirror UI hierarchy for RTL languages
    END FUNCTION
```

---

## TODO: Implementation Tasks

### HIGH Priority 🔴
- [ ] LocalizationManager core
- [ ] String table loading (JSON)
- [ ] Variable substitution
- [ ] Font loading by language

### MEDIUM Priority 🟡
- [ ] Pluralization support
- [ ] RTL layout system
- [ ] Voice audio switching
- [ ] Image localization

### LOW Priority 🟢
- [ ] In-game language switcher
- [ ] Translation memory integration
- [ ] Coverage reporting

---

**[← Back to Index](../README.md)** | **[Next: Accessibility System →](./AccessibilitySystem.md)**
