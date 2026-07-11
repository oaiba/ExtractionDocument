# Plan mở rộng tài liệu UE Multiplayer Live Services Architecture

## Confirmed Parameters

| Parameter | Answer |
|---|---|
| **Game genre** | Extraction Shooter (Escape from Tarkov / The Cycle / Delta Force Operator style) |
| **Monetization** | Full model: premium currency + gacha/lootbox + battle pass + cosmetic shop |
| **Initial CCU target** | ~1,000 |
| **Timeline** | Flexible — no hard deadline |
| **Team** | Solo dev — 1 person handling both backend (Go) and Unreal Engine |
| **Document structure** | Expand directly on the master file — no sub-documents |
| **Language** | English |

---

## Key Implications for the Plan

> [!IMPORTANT]
> **Solo dev** means:
> - Phases must be **strictly sequential** — no parallel workstreams
> - Each section should be **self-contained** and immediately usable
> - Priority is depth on sections that unblock coding, not breadth
> - Document expansion doubles as **personal design reference** and **AI agent instruction set**

> [!NOTE]
> **Extraction Shooter** confirms the following systems are core, not optional:
> - Stash / Hideout inventory
> - Loadout bring-in / risk-reward
> - Insurance (return items after death)
> - Loot tables + in-raid item spawns
> - Extraction points + extraction validation
> - Secure containers
> - Flea market / player marketplace (later phase)

> [!NOTE]
> **Full monetization** means the economy section must cover:
> - Soft currency (earned in-game)
> - Premium currency (purchased with real money)
> - Gacha / lootbox probability tables + pity system
> - Cosmetic shop
> - Battle pass (free + premium tracks)
> - Economy ledger must handle all currency types with audit trail

> [!NOTE]
> **1,000 CCU** means:
> - Single PostgreSQL instance is sufficient
> - Redis standalone (no cluster needed)
> - No multi-region for initial release
> - PgBouncer optional but recommended
> - Scaling section focuses on **when to scale**, not complex distributed architecture

---

## Delivery Plan — 4 Phases

All content will be added as **new sections directly into** [UE_Multiplayer_Live_Services_Architecture_Go_RedpointEOS.md](file:///C:/Users/oaipb/Downloads/plan/UE_Multiplayer_Live_Services_Architecture_Go_RedpointEOS.md).

Current document: 31 sections. After expansion: ~50+ sections.

---

## Phase A — Core Depth (ưu tiên cao nhất)

> **Goal**: Nâng các section hiện có lên mức actionable — có diagram, có schema, có API spec đầy đủ
>
> **Estimated effort**: ~3–4 solo days

### A1. Mermaid Sequence Diagrams

Thêm Mermaid diagrams vào các sections hiện có:

| Diagram | Target Section |
|---|---|
| Client Login Flow (EOS → Redpoint → Backend → Token) | Section 7.2 |
| Token Refresh Flow | Section 7.3 |
| Dedicated Server Authentication | Section 8 |
| Full Match Lifecycle (16 steps) | Section 12 |
| Matchmaking → Server Assignment → Session Join | Section 13 |
| Loadout Reserve → Match → Commit/Rollback | Phase 8 description |
| Transactional Outbox processing | Section 21 |

### A2. Full Database DDL (NEW Section 32)

Complete DDL for all core tables with:

**Identity & Auth:**
- `players` — full columns, indexes, constraints
- `player_identities` — composite unique, FK
- `player_sessions` — device tracking, refresh token hash
- `idempotency_keys` — TTL cleanup strategy

**Inventory & Economy:**
- `item_definitions` — game data catalog
- `inventory_containers` — stash, secure container, equipped
- `item_instances` — individual item with durability, mods
- `item_properties` — JSONB metadata per instance
- `wallets` — soft currency, premium currency, per-player
- `economy_transactions` — immutable ledger (credit/debit)
- `loadouts` — bring-in set per raid
- `loadout_items` — items in loadout, reservation state

**Match & Server:**
- `server_registrations` — heartbeat, capacity, region
- `match_records` — lifecycle state machine
- `match_participants` — per-player match data, extraction state
- `match_item_changes` — authoritative item delta per match

**Outbox:**
- `outbox_events` — transactional outbox for async processing

All tables include: indexes, FK constraints, `created_at`/`updated_at`, revision columns.

### A3. Expanded OpenAPI Contract (NEW Section 33)

Full request/response schemas for every endpoint in Sections 14:

**Public API:**
| Endpoint | Request Body | Response | Errors |
|---|---|---|---|
| `POST /v1/auth/eos` | EOS token, deviceId, clientBuild | accessToken, refreshToken, expiresIn, player | 400, 401, 403, 429 |
| `POST /v1/auth/refresh` | refreshToken | accessToken, refreshToken, expiresIn | 400, 401 |
| `GET /v1/profile` | — | player profile + revision | 401, 404 |
| `GET /v1/inventory` | — | containers + items + revision | 401, 404 |
| `POST /v1/loadouts/reserve` | loadoutId, matchId | reservation confirmation | 400, 401, 409, 423 |
| `POST /v1/matchmaking/tickets` | mode, region, partyId | ticketId, status | 400, 401, 429 |
| `GET /v1/matchmaking/tickets/{id}` | — | ticket status, assignment | 401, 404 |
| `DELETE /v1/matchmaking/tickets/{id}` | — | 204 | 401, 404 |
| `GET /v1/liveops/config` | — | config + ETag | 304, 401 |

**Internal API:**
| Endpoint | Request Body | Response | Errors |
|---|---|---|---|
| `POST /v1/internal/servers/register` | server info | serverId, token | 400, 401, 403 |
| `POST /v1/internal/servers/{id}/heartbeat` | status, players | ack | 401, 404 |
| `POST /v1/internal/matches/start` | serverId, playerIds, mode, map | matchId | 400, 401, 403 |
| `POST /v1/internal/matches/{id}/commit` | results, item changes, idempotency key | commit confirmation | 400, 401, 403, 409, 422 |

### A4. Error Catalog (NEW Section 34)

Complete error code table:
- `auth_*` errors (token_expired, token_invalid, session_revoked, device_mismatch)
- `inventory_*` errors (revision_conflict, item_not_found, container_full, item_locked)
- `economy_*` errors (insufficient_funds, duplicate_transaction, ledger_mismatch)
- `matchmaking_*` errors (queue_full, ticket_expired, already_in_queue, incompatible_build)
- `server_*` errors (capacity_exceeded, not_registered, heartbeat_expired)
- `match_*` errors (already_committed, invalid_state, player_not_in_match)

Retry policy:
- Client retry: exponential backoff (1s, 2s, 4s, 8s, max 30s) + jitter
- DS retry: immediate once, then exponential (500ms, 1s, 2s, max 10s)
- Idempotent endpoints safe to retry; non-idempotent require idempotency key

### A5. Rate Limiting Policy (NEW Section 35)

| Endpoint Category | Limit | Window | Scope |
|---|---|---|---|
| Auth endpoints | 10 req | 60s | per IP |
| Profile read | 60 req | 60s | per player |
| Inventory read | 60 req | 60s | per player |
| Matchmaking create | 5 req | 60s | per player |
| Server heartbeat | 30 req | 60s | per server |
| Match commit | 10 req | 60s | per server |
| Admin endpoints | 120 req | 60s | per admin |

Response headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`

---

## Phase B — Extraction Shooter & Economy Systems (ưu tiên cao)

> **Goal**: Define tất cả hệ thống core cho thể loại Extraction Shooter + full monetization
>
> **Estimated effort**: ~4–6 solo days

### B1. Extraction Shooter Core Mechanics (NEW Section 36)

- Raid lifecycle: lobby → deploy → in-raid → extract/die/MIA
- Extraction points: validation, timer, conditions
- Secure container rules
- Stash management (grid-based vs slot-based — define approach)
- Hideout concept (if applicable)
- Scav/PMC concept (if applicable)
- Found-in-raid status
- Item condition / durability
- Loot spawn tables (server-authoritative)
- State machine diagram for raid lifecycle

### B2. Insurance System (NEW Section 37)

- Insurance providers (different tiers, costs, return times)
- Data model: `insurance_policies`, `insurance_claims`, `insurance_returns`
- Flow: insure items before raid → die → items not looted by other players → return after delay
- State machine: `insured` → `claim_pending` → `returned` / `lost`
- Worker job for delayed insurance returns (outbox pattern)
- Fraud prevention: cannot insure → drop to friend → claim
- API endpoints: `POST /v1/insurance/insure`, `GET /v1/insurance/claims`
- Integration with match commit flow

### B3. Loot Tables & Item Spawning (NEW Section 38)

- Server-authoritative loot generation
- Loot table structure: zones, containers, rarity weights
- Dynamic loot modifiers (live ops adjustable)
- Item spawn validation (backend provides seed/tables, DS generates)
- Data model: `loot_tables`, `loot_table_entries`, `loot_zones`
- Integration with live ops config

### B4. Premium Currency & Shop (NEW Section 39)

- Currency types: soft (roubles equivalent), premium (purchased)
- Premium currency purchase flow (App Store / Google Play → receipt validation → grant)
- Receipt validation architecture (server-side only)
- Shop catalog: `shop_items`, `shop_bundles`, `shop_rotations`
- Purchase transaction flow with ledger
- Refund handling
- API endpoints: `POST /v1/shop/purchase`, `GET /v1/shop/catalog`
- Price table versioning

### B5. Gacha / Lootbox System (NEW Section 40)

- Lootbox types and rarity distribution
- Pity system / guarantee mechanic
- Probability tables: `gacha_pools`, `gacha_pool_entries`, `gacha_pity_counters`
- Regulatory compliance: probability disclosure
- Server-side roll (never client-determined)
- Audit trail for every roll
- API endpoints: `POST /v1/gacha/open`, `GET /v1/gacha/pools`

### B6. Quest & Progression System (NEW Section 41)

- Quest types: daily, weekly, seasonal, storyline (trader quests like Tarkov)
- Trader reputation / loyalty levels
- Data model: `quest_definitions`, `quest_objectives`, `quest_progress`, `trader_standings`
- Quest objective types: kill, extract, find-in-raid, deliver, survive
- Server-side objective tracking (DS reports events, backend validates)
- Reward distribution (items, XP, currency, trader reputation)
- API endpoints: `GET /v1/quests`, `POST /v1/quests/{id}/complete`

### B7. Battle Pass / Season System (NEW Section 42)

- Season structure: start date, end date, tiers
- Free track + premium track
- XP sources: raids, quests, daily/weekly
- Data model: `seasons`, `season_tiers`, `season_tier_rewards`, `player_season_progress`
- Tier reward claim flow
- End-of-season handling (unclaimed rewards)
- API endpoints: `GET /v1/season/current`, `POST /v1/season/claim-tier`

---

## Phase C — Operational Readiness (ưu tiên trung bình)

> **Goal**: Chuẩn bị cho vận hành thực tế, bao gồm reconnection, anti-cheat, scaling, backup
>
> **Estimated effort**: ~3–4 solo days

### C1. Notification & Inbox System (NEW Section 43)

- Push notifications (APNS for iOS, FCM for Android)
- In-game inbox: insurance returns, rewards, admin messages
- Data model: `inbox_messages`, `push_registrations`
- Message lifecycle: created → read → claimed → expired
- API endpoints: `GET /v1/inbox`, `POST /v1/inbox/{id}/claim`
- Cleanup worker for expired messages

### C2. Reconnection & Session Recovery (NEW Section 44)

- Client disconnect during raid: timeout window, rejoin flow
- DS crash recovery: match state persistence, player state recovery
- Backend reconnection API: `POST /v1/matches/rejoin`
- State recovery: which data is recoverable vs lost
- Timeout thresholds (e.g., 3 min reconnect window)
- Mermaid diagram for disconnect/reconnect flow

### C3. Anti-Cheat Integration (NEW Section 45)

- EAC (Easy Anti-Cheat) integration on Dedicated Server
- EAC client-side for mobile (iOS/Android capabilities & limitations)
- Server-side validation checks: movement speed, damage values, loot amounts
- Report → Investigation → Sanction pipeline
- Data model: `player_reports`, `sanctions`
- Integration with moderation workflow (Section 10)

### C4. Scaling Strategy for 1K CCU (NEW Section 46)

- Current architecture capacity analysis
- PostgreSQL: single instance with connection pooling (PgBouncer)
- Redis: standalone with persistence (AOF)
- Go API: single instance, horizontal if needed (stateless)
- DS fleet: manual allocation at 1K CCU
- Monitoring thresholds for "time to scale"
- Growth milestones: 1K → 5K → 10K → 50K+ (what changes at each)
- Cost estimation per tier

### C5. Disaster Recovery & Backup (NEW Section 47)

- PostgreSQL backup: daily pg_dump + WAL archiving
- Redis: RDB snapshots + AOF
- Object storage: versioned buckets
- RTO target: < 4 hours (for 1K CCU scale)
- RPO target: < 1 hour
- Restore test schedule: monthly
- Runbook: step-by-step restore procedure

### C6. Data Retention & GDPR Compliance (NEW Section 48)

- Player data export (`GET /v1/admin/players/{id}/export`)
- Player data deletion (`DELETE /v1/admin/players/{id}/gdpr`)
- Data retention per type:
  - Match records: 1 year
  - Economy ledger: permanent
  - Audit logs: 2 years
  - Analytics: 90 days (anonymized)
  - Chat logs: 30 days
- Anonymization strategy for deleted accounts

### C7. Deployment Runbooks (Section 24 expansion)

- Step-by-step deployment procedure for solo dev
- Database migration pre-check
- Rollback procedure (Go binary + migration rollback)
- Canary deployment (10% → 50% → 100%) — simplified for solo dev
- Incident response template
- Health check verification after deploy

---

## Phase D — Advanced Features & Roadmap (ưu tiên thấp)

> **Goal**: Roadmap cho features nâng cao — chỉ cần design overview, không cần full DDL
>
> **Estimated effort**: ~2–3 solo days

### D1. Flea Market / Player Marketplace (NEW Section 49)

- Peer-to-peer marketplace (like Tarkov's Flea Market)
- Listing → Bidding/Buy → Escrow → Settlement
- Fee structure + tax sink
- Fraud prevention: price manipulation, item duplication
- Reputation / trader level gate
- Data model overview (not full DDL)

### D2. Content Delivery & Patching (NEW Section 50)

- Asset bundle management for mobile
- Hot-fix delivery without app store update
- Client version compatibility matrix
- Forced update flow
- CDN strategy

### D3. WebSocket / Real-time Updates (NEW Section 51)

- Use cases: matchmaking status polling → push, inbox notifications, live ops updates
- When to use WebSocket vs REST polling vs SSE
- Authentication over WebSocket
- Connection lifecycle
- Fallback to polling for mobile reliability

### D4. Multi-Region Roadmap (NEW Section 52)

- When to go multi-region (>10K CCU, regulatory, latency)
- Database strategy: read replicas by region
- DS fleet per region
- Matchmaking region affinity
- Global server registry
- This is a roadmap section, not implementation detail

---

## Execution Order Summary

```text
Phase A — Core Depth
  A1. Mermaid Diagrams (add to existing sections)
  A2. Full Database DDL (NEW Section 32)
  A3. Expanded OpenAPI Contract (NEW Section 33)
  A4. Error Catalog (NEW Section 34)
  A5. Rate Limiting Policy (NEW Section 35)

Phase B — Extraction Shooter & Economy
  B1. Extraction Shooter Core Mechanics (NEW Section 36)
  B2. Insurance System (NEW Section 37)
  B3. Loot Tables & Item Spawning (NEW Section 38)
  B4. Premium Currency & Shop (NEW Section 39)
  B5. Gacha / Lootbox System (NEW Section 40)
  B6. Quest & Progression System (NEW Section 41)
  B7. Battle Pass / Season System (NEW Section 42)

Phase C — Operational Readiness
  C1. Notification & Inbox System (NEW Section 43)
  C2. Reconnection & Session Recovery (NEW Section 44)
  C3. Anti-Cheat Integration (NEW Section 45)
  C4. Scaling Strategy for 1K CCU (NEW Section 46)
  C5. Disaster Recovery & Backup (NEW Section 47)
  C6. Data Retention & GDPR Compliance (NEW Section 48)
  C7. Deployment Runbooks (expand Section 24)

Phase D — Advanced Features & Roadmap
  D1. Flea Market / Player Marketplace (NEW Section 49)
  D2. Content Delivery & Patching (NEW Section 50)
  D3. WebSocket / Real-time Updates (NEW Section 51)
  D4. Multi-Region Roadmap (NEW Section 52)
```

**Total estimated effort**: ~12–17 solo dev days (document writing only, not coding)

**Output**: 1 expanded master document (~5000–7000+ lines) containing the complete architecture, design specs, schemas, API contracts, and operational procedures.

---

## Proposed Changes

### [MODIFY] [UE_Multiplayer_Live_Services_Architecture_Go_RedpointEOS.md](file:///C:/Users/oaipb/Downloads/plan/UE_Multiplayer_Live_Services_Architecture_Go_RedpointEOS.md)

- Add Mermaid sequence diagrams into Sections 7, 8, 12, 13, 21
- Add ~20 new sections (Section 32–52) covering all expansion areas
- Expand Section 24 with deployment runbooks
- All content in English, consistent with existing style
- No sub-documents — everything in the single master file

## Verification Plan

### Manual Verification
- Review each new section for consistency with existing architecture principles
- Verify DDL schemas match API contract fields
- Verify error catalog covers all API error responses
- Verify Mermaid diagrams accurately represent the text flows
- Cross-check extraction shooter mechanics against Tarkov/Delta Force reference games

### Checklist
- [ ] Every major flow has a Mermaid diagram
- [ ] Every table has full DDL with indexes and constraints
- [ ] Every API endpoint has request/response schema + error codes
- [ ] Insurance, Quest, Battle Pass, Gacha all have data models + API + flow
- [ ] Error catalog covers all error codes referenced in API spec
- [ ] Rate limiting policy covers all endpoint categories
- [ ] Scaling section has clear thresholds for each growth milestone
- [ ] GDPR section has actionable data export/deletion flows
- [ ] No contradictions between new and existing sections
