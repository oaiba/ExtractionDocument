---
title: "vũ khí & Combat hệ thống"
type: docs
---

> **Canonical source:** Full vũ khí categories, stats, đạn, attachments, damage model, TTK, và combat cơ chế are documented in **[vũ khí Arsenal & Combat hệ thống](../gameplay/weaponarsenal/index.html)**. This trang retains combat philosophy only.

---

## Combat-Facing Weapon Role Taxonomy

Weapon role được định nghĩa bằng câu hỏi combat nó đặt ra, không phải raw DPS. Một weapon mạnh phải tạo lợi thế readable trong intended band và weakness readable ngoài band đó.

| Role | Primary Range | Skill Ask | Mobility | Recoil / Spread Identity | Suppression Role | Loot / Economy Role |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| AR | Close-mid đến mid | Track target, control burst, choose cover | Medium | Controllable burst, sustained climb vừa phải | Flexible pressure | Earned/trader baseline |
| SMG | Close | Flank timing, hip-fire discipline, ammo management | High | Fast bloom, fast recovery, short falloff | Room clear pressure | Budget-to-specialist CQB option |
| Shotgun | Close burst | Angle trap, pellet discipline, reload timing | Medium | Wide spread, miss bị phạt nặng | Breach / denial | High-risk close loot value |
| DMR | Mid-long | Patience, semi-auto cadence, sightline control | Medium-low | Low bloom, moving aim penalty cao | Pick pressure | Precision economy sink |
| Sniper | Long | Setup, line control, extraction timing | Low | Sway, slow follow-up, high commitment | Area denial | Rare/high-value objective weapon |
| LMG | Mid suppression | Setup, lane control, reload planning | Low | Heavy sustained recoil, volume mạnh | Primary suppression | Expensive squad support kit |
| Pistol | Close backup | Draw timing, emergency aim | High | Spam kém ổn định | Last-resort pressure | Recovery/budget safety net |
| Melee | Contact | Stealth, ambush, desperation | Highest | No spread, exposure cao | Silent finish only | Low/no-cost fallback |

## Damage And Readability Principles

Player phải hiểu vì sao shot hit, miss, không penetrate, stagger, suppress, hoặc kill. Combat UI/audio nên dạy đủ rõ mà không biến firefight thành bảng tính.

| Event | Required Feedback | Must Avoid |
| :--- | :--- | :--- |
| Flesh hit | Hit marker rõ, impact sound, blood/cloth effect | Giống armor hit |
| Armor hit | Hard impact sound, armor spark/debris, armor hit marker variant | Hidden blocked damage |
| No penetration | Blocked/deflected cue và reduced/no HP feedback | Làm player tưởng netcode lỗi |
| Headshot | Cue distinct nhưng ngắn, death recap confirm | Celebration quá lớn giữa combat |
| Suppression | Vignette/audio ducking/aim pressure readable và ngắn | Color-only hoặc blur kéo dài |
| Ricochet | Deflect sound sắc và glancing cue visible | Silent zero-damage result |
| Low ammo / reload | Ammo color, click/VO, reload progress | Empty gun bất ngờ không warning |

## Firefight Pacing And Counterplay

| Principle | Requirement |
| :--- | :--- |
| Mistake punishment | Positioning sai bị phạt nhanh hơn cautious repositioning. |
| Counterplay window | Hầu hết non-sniper death cần cause readable: angle, sound, armor failure, reload, hoặc overexposure. |
| Armor trust | Armor phải visibly reduce/deflect damage, nhưng damaged armor phải giải thích vì sao fail sau đó. |
| Attachment trade-off | Attachment có thể cải thiện role, nhưng cần weight, ADS cost, noise, visibility, price, hoặc slot conflict. |
| No paid power | Premium cosmetics/entitlements không bao giờ grant combat-power item instances. |

## Combat QA Checklist

- Mỗi weapon role có preferred range, skill ask, và counterplay.
- Không weapon nào best ở close, mid, long, mobility, recoil, cost, và armor penetration cùng lúc.
- Armor hit, flesh hit, ricochet, blocked shot, suppression, headshot, và low ammo feedback phân biệt bằng hơn color.
- Death recap có thể nêu weapon, hit zone, armor interaction, và key cause mà không expose unfair enemy inventory data.
- Tuning changes link về [Weapon Balance Framework](../weapons/weapon_balance_framework/index.html), không tạo one-off rule ở đây.

## Combat Philosophy

**cốt lõi Principles:**

1. **Tactical Over Twitch** — Positioning và quyết định-making matter more than raw reflexes.
2. **vũ khí Variety** — Each vũ khí has a distinct role và feel.
3. **Risk vs Reward** — Better vũ khí come với higher loss penalty.
4. **Skill Expression** — High skill ceiling với recoil control và positioning.
5. **Mobile Optimized** — Controls và cơ chế designed for touch màn hình.

For vũ khí categories, specifications, ammunition, attachments, damage hệ thống, ballistics, và thời gian-to-kill data, Xem [vũ khí Arsenal & Combat hệ thống](../gameplay/weaponarsenal/index.html).
