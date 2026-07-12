---
title: "Unreal Engine Multiplayer Live Services Architecture"
linkTitle: "Live Services Architecture"
type: docs
weight: 2
---

> Cloned from `_files/UE_Multiplayer_Live_Services_Architecture_Go_RedpointEOS.md`. The source file remains unchanged and is the archive reference.

# Unreal Engine Multiplayer Live Services
## Architecture, Technology Stack, Delivery Workflow, and Implementation Phases

**Primary audience:** Unreal Engine developers, backend developers, DevOps engineers, technical leads, QA, and AI coding agents  
**Current development environment:** macOS on Apple Silicon  
**Current test topology:** Mac runs Unreal Dedicated Server + Go backend; physical iPhone and Android devices are game clients  
**Online services integration:** Redpoint EOS + Epic Online Services  
**Recommended production direction:** Linux-hosted Go backend and Linux Unreal Dedicated Servers

---

# 1. Purpose

This document defines a practical technical foundation for building a multiplayer live-service game with:

- Unreal Engine C++
- Unreal Dedicated Server
- Redpoint EOS
- Epic Online Services
- Go backend services
- PostgreSQL
- Redis
- Mobile clients on iOS and Android
- macOS development and test infrastructure
- Linux production deployment

The document is intended to act as:

- the technical source of truth for the team;
- an architecture baseline;
- a planning reference for implementation phases;
- a guide for AI agents generating plans, code, tests, migrations, and infrastructure;
- a guardrail against premature complexity.

The main principle is:

> EOS and Redpoint provide online platform capabilities.  
> The custom backend owns authoritative live-service data.  
> The Unreal Dedicated Server owns real-time gameplay authority.

---

# 2. Core Architecture Decision

The system is divided into three authority layers.

## 2.1 Unreal Client

Responsibilities:

- player input;
- UI and presentation;
- local prediction;
- EOS login flow through Redpoint;
- obtain the EOS Connect ID token through `IIdentitySystem` / `FIdentityUser::GetIdToken`;
- party, lobby, session discovery;
- profile and inventory display;
- matchmaking requests;
- sending gameplay intentions to the Dedicated Server.

The client must never be authoritative for:

- currency;
- inventory ownership;
- match rewards;
- extracted items;
- damage results;
- quest completion;
- insurance outcomes;
- progression;
- premium purchases.

---

## 2.2 Unreal Dedicated Server

Responsibilities:

- gameplay authority;
- movement validation;
- combat validation;
- abilities and cooldown validation;
- loot and extraction validation;
- authoritative match state;
- authoritative player participation;
- verify the backend-issued join ticket after Redpoint has verified EOS transport identity;
- match result generation;
- server registration and heartbeat;
- authoritative result commit to backend.

The Dedicated Server must be the trusted writer for match outcome data.

Examples:

- raid started;
- player joined;
- player died;
- player extracted;
- authoritative item changes;
- match finished;
- result commit.

The Dedicated Server must not directly modify database tables. It calls protected backend APIs using mTLS and a short-lived, server-scoped token. Redpoint transport authentication proves the connecting EOS Product User ID; the backend join ticket proves that this player is authorized for this specific match.

---

## 2.3 Custom Go Backend

Responsibilities:

- identity mapping;
- backend session management;
- player profile;
- inventory and stash;
- wallet and economy;
- item ownership;
- progression and quests;
- matchmaking tickets;
- matchmaking decisions, server allocation, and join-ticket issuance;
- server registry;
- match records;
- live operations configuration;
- feature flags;
- moderation and sanctions;
- audit logs;
- admin APIs;
- persistence;
- analytics event publishing.

The backend is the source of truth for persistent live-service data and match admission. Redpoint EOS does not become a second persistent matchmaker.

---

# 3. High-Level System Diagram

```text
                         Epic Online Services
                 Auth / Connect / Lobby / Session
              Friends / Presence / RTC / Reports / EAC
                               |
                        Redpoint EOS Framework
                               |
              +----------------+----------------+
              |                                 |
      Unreal Mobile Client              Unreal Dedicated Server
      iOS / Android                     macOS during development
              |                                 |
              | HTTPS / JSON                    | HTTPS / JSON
              +----------------+----------------+
                               |
                         Go Backend API
                               |
              +----------------+----------------+
              |                |                |
         PostgreSQL          Redis       Object Storage
        source of truth      cache        replay/log/blob
```

---

# 4. Recommended Technology Stack

## 4.1 Unreal Layer

| Area | Technology |
|---|---|
| Game client | Unreal Engine C++ |
| Dedicated server | Unreal Engine Server Target |
| Online services | Redpoint EOS |
| Identity | EOS Connect |
| Party | EOS Lobby |
| Match instance discovery | EOS Sessions |
| Presence and friends | EOS social interfaces |
| Voice | EOS RTC where applicable |
| Network gameplay | Unreal Replication |
| HTTP API client | `FHttpModule` |
| JSON | Unreal JSON utilities / `FJsonObjectConverter` |
| Async abstraction | futures, promises, subsystem callbacks, or project-specific async tasks |

---

## 4.2 Backend Layer

| Area | Recommended choice |
|---|---|
| Language | Go |
| HTTP stack | `net/http` + `chi` |
| Database | PostgreSQL |
| PostgreSQL driver | `pgx` |
| SQL code generation | `sqlc` |
| Migrations | Goose |
| Cache | Redis |
| Redis client | `go-redis` |
| API contract | OpenAPI |
| OpenAPI generation | `oapi-codegen` |
| Logging | `log/slog` |
| Validation | explicit validation or `go-playground/validator` |
| JWT/JWK | `lestrrat-go/jwx` or another actively maintained library |
| Tracing and metrics | OpenTelemetry |
| Local object storage | MinIO |
| Production object storage | S3-compatible storage |
| Containerization | Docker |
| Local orchestration | Docker Compose |
| Reverse proxy | Caddy or Nginx |
| Testing | Go test + Testcontainers |
| Load testing | k6 |

---

## 4.3 Deployment Layer

### Development

```text
macOS native:
- Unreal Editor
- Unreal Dedicated Server

Docker Compose:
- Go API
- PostgreSQL
- Redis
- MinIO
- Caddy
- optional observability stack
```

### Production

```text
Linux:
- Go backend containers
- Linux Unreal Dedicated Server processes
- Managed PostgreSQL where possible
- Redis
- Object storage
- Reverse proxy / load balancer
- OpenTelemetry collector
```

Do not begin with Kubernetes unless the project already requires:

- multiple regions;
- many independently scaled services;
- automated game server fleets;
- a team capable of operating Kubernetes.

---

# 5. Why Go Is Suitable

Go is appropriate for this project because it provides:

- good concurrency support;
- simple deployment;
- small binaries;
- fast startup;
- low memory overhead;
- straightforward cross-compilation;
- good support for Linux and Apple Silicon;
- strong standard library networking;
- excellent fit for API, matchmaker, allocator, workers, and server agents.

Go should be preferred over a heavier framework approach for this project, but it must still be structured carefully.

Avoid the following mistakes:

- putting business logic in HTTP handlers;
- using Redis as the source of truth;
- hiding important transaction logic behind a heavy ORM;
- creating microservices too early;
- using framework benchmarks as the main architecture criterion.

---

# 6. Backend Architecture

Use a **modular monolith** first.

## 6.1 Suggested Repository Layout

```text
game-backend/
├── cmd/
│   ├── api/
│   │   └── main.go
│   ├── worker/
│   │   └── main.go
│   └── migrate/
│       └── main.go
│
├── internal/
│   ├── auth/
│   ├── player/
│   ├── inventory/
│   ├── economy/
│   ├── matchmaking/
│   ├── match/
│   ├── gameserver/
│   ├── progression/
│   ├── liveops/
│   ├── moderation/
│   └── admin/
│
├── internal/platform/
│   ├── database/
│   ├── redis/
│   ├── httpserver/
│   ├── security/
│   ├── objectstorage/
│   └── observability/
│
├── api/
│   └── openapi.yaml
│
├── db/
│   ├── migrations/
│   ├── queries/
│   └── sqlc.yaml
│
├── deployments/
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── Caddyfile
│
├── scripts/
├── tests/
├── go.mod
└── Makefile
```

Organize code by business domain, not only by technical layer.

Preferred:

```text
inventory/
    handler.go
    service.go
    model.go
    repository.go
    commands.go
```

Avoid:

```text
controllers/
services/
repositories/
models/
```

for the entire application, because feature code becomes scattered.

---

# 7. Identity and Authentication

## 7.1 Identity Model

Do not use EOS Product User ID as the only primary key for the entire backend.

Use an internal UUID.

In Redpoint EOS, the runtime user representation is `UE::Online::FAccountId`. Convert it to/from the EOS Product User ID only at the Unreal/EOS boundary using `RedpointEOSCore` helpers. Store the Product User ID as `player_identities.provider_user_id` with provider `eos_connect`; do not make an Epic Games Account ID the gameplay primary key because it is optional and not portable across identity providers.

```text
InternalPlayerID
    ├── EOS ProductUserId
    ├── Epic Account ID
    ├── Apple identity
    ├── Google identity
    ├── guest/device identity
    └── future platform identities
```

Suggested tables:

```sql
players
-------
id UUID PRIMARY KEY
display_name TEXT
status TEXT
created_at TIMESTAMPTZ
updated_at TIMESTAMPTZ
revision BIGINT

player_identities
-----------------
id UUID PRIMARY KEY
player_id UUID NOT NULL
provider TEXT NOT NULL
provider_user_id TEXT NOT NULL
linked_at TIMESTAMPTZ NOT NULL
last_login_at TIMESTAMPTZ

UNIQUE(provider, provider_user_id)
```

---

## 7.2 Client Login Flow

```text
1. Client calls `IIdentitySystem::Login` through Redpoint EOS.
2. Client obtains its EOS Connect ID token from `FIdentityUser::GetIdToken`.
3. Client sends the EOS token to the Go backend.
4. Backend verifies the token.
5. Backend extracts EOS identity.
6. Backend maps EOS identity to InternalPlayerID.
7. Backend creates the player if this is the first login.
8. Backend issues its own short-lived access token.
9. Client uses the backend token for game APIs.
```

Example:

```http
POST /v1/auth/eos
Content-Type: application/json
```

```json
{
  "token": "<eos-token>",
  "deviceId": "<device-id>",
  "clientBuild": "1.0.0"
}
```

Backend response:

```json
{
  "accessToken": "<backend-access-token>",
  "refreshToken": "<rotating-refresh-token>",
  "expiresIn": 900,
  "player": {
    "id": "<internal-player-uuid>",
    "displayName": "Player"
  }
}
```

```mermaid
sequenceDiagram
    autonumber
    participant C as Unreal Client
    participant R as Redpoint EOS / EOS Connect
    participant B as Go Backend
    participant DB as PostgreSQL
    C->>R: Login / obtain EOS identity token
    R-->>C: Product User ID + identity token
    C->>B: POST /v1/auth/eos (token, deviceId, build)
    B->>R: Verify EOS Connect token and Product User ID
    R-->>B: Verified EOS identity
    B->>DB: Find or create player + identity + session
    DB-->>B: Internal player ID
    B-->>C: Access token + rotating refresh token + player
```

---

## 7.3 Token Policy

Recommended baseline:

- access token lifetime: 10 to 15 minutes;
- rotating refresh tokens;
- session tracked per device;
- revocation supported;
- server credentials separate from player credentials;
- secrets stored in environment variables or a secret manager;
- no client secret embedded in the mobile build.

```mermaid
sequenceDiagram
    autonumber
    participant C as Client
    participant B as Go Backend
    participant DB as PostgreSQL
    C->>B: POST /v1/auth/refresh (refresh token)
    B->>DB: Lock active session and compare token hash
    alt Valid, active session
        B->>DB: Replace hash; revoke previous refresh token
        B-->>C: New access token and refresh token
    else Invalid, expired, reused, or revoked
        B->>DB: Revoke session when reuse is detected
        B-->>C: 401 auth_session_revoked or auth_token_invalid
    end
```

---

# 8. Dedicated Server Authentication

Dedicated Server credentials must be separate from player tokens.

Recommended model:

```text
Server process
    -> mTLS bootstrap credential (development: local CA; production: secret manager)
    -> POST /internal/servers/register
    -> server ID + short-lived scoped server token
    -> protected internal backend endpoints over mTLS
```

Suggested scopes:

```text
player:
    profile.read
    inventory.read
    matchmaking.create

game-server:
    server.register
    server.heartbeat
    match.start
    match.commit
    match.admit_player
    inventory.authoritative_write

admin:
    player.lookup
    economy.grant
    moderation.manage
```

Protected internal endpoints:

```text
POST /v1/internal/servers/register
POST /v1/internal/servers/{serverId}/heartbeat
POST /v1/internal/matches/start
POST /v1/internal/matches/{matchId}/commit
POST /v1/internal/matches/{matchId}/admit-player
```

The bootstrap credential is used only for registration and rotation. The issued token is bound to the registered `serverId`, expiry, certificate identity, and scopes; heartbeat, admission, start, and commit reject expired/revoked tokens or non-active servers. Never reuse client credentials for server actions.

```mermaid
sequenceDiagram
    autonumber
    participant DS as Dedicated Server
    participant I as Workload Identity / Secret Store
    participant B as Go Backend
    participant DB as PostgreSQL
    DS->>I: Obtain mTLS bootstrap credential
    DS->>B: POST /internal/servers/register over mTLS
    B->>DB: Register server and issue short-lived server token
    B-->>DS: serverId + scoped token
    loop Every 2 seconds
        DS->>B: Heartbeat (capacity, match state)
        B->>DB: Update last_heartbeat_at
        B-->>DS: Acknowledgement
    end
```

---

# 9. EOS and Redpoint Responsibility Boundary

Use Redpoint EOS and EOS for:

- authentication and identity;
- account connection;
- friends;
- presence;
- lobby;
- session;
- social overlay where needed;
- voice;
- achievements;
- simple stats;
- reports;
- sanctions;
- anti-cheat integration.

For the selected hybrid model, Redpoint provides EOS identity, party/lobby, session discovery, and encrypted Unreal transport. The Redpoint networking layer on a Dedicated Server requests the client EOS Connect ID token over the encrypted control channel and verifies it against the connecting Product User ID. This is required transport identity verification, not persistent match authorization.

Use the custom backend for:

- internal account model;
- inventory;
- stash;
- loadout;
- wallet;
- economy ledger;
- progression;
- quests;
- battle pass;
- match history;
- raid results;
- insurance;
- purchases and entitlements;
- live operations;
- server allocation;
- matchmaking decisions;
- admin tools;
- audit and fraud analysis.

EOS is not a replacement for a transactional authoritative database.

Do **not** invoke `IMatchmakingEngine` or the `Matchmaking` / `MatchmakingMatchmaker` modules in the production runtime path. Those modules maintain their own queue, timeout, candidate matching, dedicated-server beacon reservation, and session-join lifecycle. Running them alongside the Go matchmaking worker would create conflicting allocation authority. They may be used as a development reference only.

---

# 10. Data Ownership Rules

## 10.1 PostgreSQL Is the Source of Truth

Use PostgreSQL for:

- players;
- identities;
- inventories;
- item instances;
- wallets;
- economy ledger;
- loadouts;
- match records;
- progression;
- entitlements;
- sanctions;
- server registrations;
- audit logs.

## 10.2 Redis Is Ephemeral

Use Redis for:

- rate limits;
- short-lived sessions;
- matchmaking tickets;
- server heartbeat cache;
- idempotency cache;
- hot live configuration;
- short locks;
- temporary presence.

Redis must never be the only storage for:

- premium currency;
- permanent inventory;
- purchases;
- rewards;
- item ownership;
- sanctions history.

## 10.3 Object Storage

Use object storage for:

- replays;
- crash dumps;
- large telemetry files;
- binary assets;
- exports;
- snapshots;
- archives;
- build manifests.

---

# 11. Inventory and Economy Model

The client must never directly state authoritative reward outcomes.

Incorrect:

```text
Client -> Backend
"I won and should receive 5000 currency."
```

Correct:

```text
Dedicated Server -> Backend
Authoritative match result with:
- match ID
- player ID
- extraction state
- item changes
- quest changes
- idempotency key
- server identity
```

---

## 11.1 Recommended Tables

```text
inventory_containers
inventory_items
item_instances
item_properties
wallets
economy_transactions
loadouts
loadout_items
match_results
```

Do not store the entire inventory as a single JSON blob if the system needs:

- atomic updates;
- item-level ownership;
- fraud analysis;
- locking;
- partial updates;
- marketplace support;
- audit history.

JSONB is appropriate for flexible metadata, not as the only inventory model.

---

## 11.2 Idempotency

Every authoritative write must include an idempotency key.

```http
Idempotency-Key: 7f339ea0-1d51-42c0-91e0-1bd2907f8407
```

If a server retries the same request because of timeout, the backend must return the original result instead of applying the reward again.

---

## 11.3 Revisions and Optimistic Concurrency

Every player aggregate should have a revision.

```text
player revision: uint64
inventory revision: uint64
```

Client or server sends the expected revision.

If the actual revision differs:

```http
409 Conflict
```

This prevents concurrent devices or servers from overwriting state.

---

# 12. Match Lifecycle

Recommended end-to-end flow:

```text
1. Client logs in using Redpoint EOS.
2. Client exchanges EOS token for backend token.
3. Client loads profile and inventory.
4. Client forms or joins a party through EOS Lobby.
5. Client creates a matchmaking ticket with the backend.
6. Matchmaker groups compatible players.
7. Go backend selects or allocates a Dedicated Server and creates the match record.
8. Dedicated Server publishes a small EOS Session discovery record.
9. Go reserves the participants' loadouts and issues a one-time, short-lived join ticket for each participant.
10. Client joins the EOS Session through Redpoint EOS.
11. Redpoint's Dedicated Server NetDriver verifies the client's EOS Connect ID token over the encrypted control channel.
12. Dedicated Server calls Go to consume and validate the join ticket against the match, internal player ID, and EOS Product User ID.
13. Dedicated Server loads the authoritative reserved loadout and admits gameplay.
14. Gameplay runs through Unreal networking; the Dedicated Server produces authoritative results.
15. Dedicated Server commits match results with idempotency.
16. Backend applies inventory/economy/outbox changes in one transaction; client refreshes state.
```

```mermaid
sequenceDiagram
    autonumber
    participant C as Client / Party
    participant RP as Redpoint EOS
    participant MM as Go Matchmaker
    participant DS as Dedicated Server
    participant B as Go Backend
    participant DB as PostgreSQL
    C->>B: Create matchmaking ticket
    B->>DB: Persist ticket
    MM->>DB: Claim compatible tickets
    MM->>DS: Allocate capacity and create match
    DS->>RP: Publish EOS Session discovery metadata
    B->>DB: Create match + participants + assignments
    B-->>C: Assignment + one-time join ticket
    C->>RP: Join EOS Session
    RP->>DS: Encrypted Unreal connection
    Note over DS: Redpoint requests and verifies EOS Connect ID token
    DS->>B: Consume join ticket; validate PUID + match
    B->>DB: Atomically mark ticket consumed and participant joined
    B-->>DS: Admission approved + internal player ID
    DS->>B: Start match
    Note over DS: Server validates all real-time gameplay
    DS->>B: Commit result with idempotency key
    B->>DB: Apply result and write outbox event atomically
    B-->>C: Profile/inventory revision changed
```

---

# 13. Matchmaking and Sessions

Use:

- EOS Lobby for party state;
- backend matchmaking tickets for queue decisions;
- EOS Sessions for active match instances.

Go owns ticket creation/cancellation, party eligibility, compatibility, grouping, server selection, reservation, assignment, and all state transitions. The client calls Go for queue state; it does not call Redpoint's matchmaking engine. Redpoint EOS is used only after Go has selected an assignment, to discover and join the selected session.

Do not put large content manifests or long arrays into Session Settings.

Session metadata should remain small:

```text
SESSION_ID
SERVER_ID
BUILD_ID
MODE_ID
MAP_ID
REGION
COMPATIBILITY_HASH
```

Do not put player lists, join tickets, loadouts, inventory identifiers, or authoritative match state in EOS Session Settings. A session ID is discovery/transport metadata only. Go stores the participant list and issues a signed, one-time ticket bound to `matchId`, internal `playerId`, EOS Product User ID, nonce/JTI, expiry, and optional build/region constraints.

The backend or CDN should expose content requirements.

Example:

```http
GET /v1/builds/{buildId}/compatibility
```

The session only needs a compatibility hash.

---

# 14. API Design

Use REST + JSON over HTTPS initially.

Benefits:

- easy debugging;
- native support in Unreal;
- good proxy and observability support;
- easy versioning;
- easier mobile testing;
- lower operational complexity than gRPC.

Public endpoints:

```text
POST /v1/auth/eos
POST /v1/auth/refresh
GET  /v1/profile
GET  /v1/inventory
POST /v1/loadouts/reserve
POST /v1/matchmaking/tickets
GET  /v1/matchmaking/tickets/{ticketId}
DELETE /v1/matchmaking/tickets/{ticketId}
GET  /v1/liveops/config
```

Internal endpoints:

```text
POST /v1/internal/servers/register
POST /v1/internal/servers/{serverId}/heartbeat
POST /v1/internal/matches/start
POST /v1/internal/matches/{matchId}/commit
POST /v1/internal/matches/{matchId}/admit-player
```

Use gRPC only later for internal service-to-service communication if justified.

---

# 15. API Contract Rules

Every request and response should include explicit versioning where applicable.

Example:

```json
{
  "schemaVersion": 1,
  "matchId": "uuid",
  "serverId": "uuid",
  "players": []
}
```

The admission endpoint is called only by the assigned Dedicated Server after Redpoint transport identity verification. It accepts the server-authenticated context plus the join ticket; it does not trust a client-provided player ID. It validates server/match assignment, ticket signature, JTI, expiry, Product User ID, internal player ID, and build/region claims, then atomically consumes the JTI and marks the participant joined. A repeated consumption returns a stable `match_join_ticket_consumed` response and must not admit a second connection.

Rules:

- use UTC;
- use ISO-8601 timestamps;
- use UUID strings;
- use integer currency values;
- do not use floating point for money;
- do not expose database entities directly;
- use explicit DTOs;
- validate all request fields;
- attach request IDs and trace IDs;
- use consistent error envelopes.

Suggested error format:

```json
{
  "error": {
    "code": "inventory_revision_conflict",
    "message": "Inventory revision does not match.",
    "requestId": "uuid",
    "details": {
      "expected": 24,
      "actual": 25
    }
  }
}
```

---

# 16. Real-Time Gameplay Boundary

Do not route gameplay simulation through the backend API.

The following stays inside Unreal networking:

- movement;
- fire;
- damage;
- hit validation;
- ability activation;
- interaction;
- replication;
- short-lived match state.

The backend is called at lifecycle boundaries:

- login;
- profile load;
- matchmaking;
- loadout reservation;
- match start;
- match end;
- extraction;
- reward claim;
- progression commit;
- purchase;
- moderation.

For a Dedicated Server join, the order is mandatory: Redpoint EOS encrypted transport and Connect ID-token verification first; then GameMode/PreLogin admission calls Go with the verified Product User ID and join ticket; only a successful one-time backend admission may create the playable participant. Do not accept an internal player ID, Product User ID, ticket, or match result from a client RPC as authoritative input.

---

# 17. macOS Development Topology

Recommended local setup:

```text
Mac mini
├── Unreal Editor
├── Unreal Dedicated Server :7777/UDP
├── Go API                  :8080/TCP
├── PostgreSQL              :5432/TCP
├── Redis                   :6379/TCP
├── MinIO                   :9000/TCP
└── Caddy                   :443/TCP
```

Recommended execution model:

- run Unreal Dedicated Server natively on macOS;
- run backend infrastructure in Docker Compose;
- optionally run the Go API natively during active debugging;
- use LAN IP from mobile devices;
- do not use `localhost` from iOS or Android.

Example:

```text
Mac LAN IP: 192.168.1.50

Backend:
http://192.168.1.50:8080

Dedicated Server:
192.168.1.50:7777
```

---

# 18. Mobile Client Considerations

## 18.1 iOS

For local HTTP testing:

- iOS App Transport Security may block cleartext HTTP;
- use a development exception only for Development builds;
- prefer HTTPS for shared testing and production.

## 18.2 Android

For local HTTP testing:

- Android may block cleartext traffic;
- allow cleartext only in Development configuration;
- Shipping builds must use HTTPS.

## 18.3 Firewall and LAN

Allow inbound access for:

- Go API TCP port;
- Unreal Dedicated Server UDP port;
- additional EOS-related ports if required.

Ensure the Mac does not sleep during tests.

---

# 19. Docker Compose Baseline

```yaml
services:
  api:
    build:
      context: ..
      dockerfile: deployments/Dockerfile
    environment:
      HTTP_ADDR: ":8080"
      DATABASE_URL: "postgres://game:game@postgres:5432/game?sslmode=disable"
      REDIS_ADDR: "redis:6379"
    ports:
      - "8080:8080"
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_started

  postgres:
    image: postgres:18
    environment:
      POSTGRES_USER: game
      POSTGRES_PASSWORD: game
      POSTGRES_DB: game
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U game -d game"]
      interval: 5s
      timeout: 5s
      retries: 10

  redis:
    image: redis:8
    ports:
      - "6379:6379"

  minio:
    image: minio/minio
    command: server /data --console-address ":9001"
    environment:
      MINIO_ROOT_USER: minio
      MINIO_ROOT_PASSWORD: minio123
    ports:
      - "9000:9000"
      - "9001:9001"
    volumes:
      - minio_data:/data

volumes:
  postgres_data:
  minio_data:
```

Pin exact image versions before production.

---

# 20. Observability

Implement observability from the beginning.

Required signals:

- structured logs;
- metrics;
- distributed traces;
- request IDs;
- match IDs;
- player IDs;
- server IDs;
- latency;
- error rates;
- database lock time;
- queue length;
- active servers;
- match commit failures.

Recommended stack:

```text
OpenTelemetry SDK
OpenTelemetry Collector
Prometheus
Grafana
Loki
Tempo
```

Do not log:

- EOS tokens;
- access tokens;
- refresh tokens;
- client secrets;
- passwords;
- private keys;
- raw sensitive payment information.

---

# 21. Background Jobs and Outbox

Do not add RabbitMQ, NATS, or Kafka at the start unless the project already needs them.

Use PostgreSQL transactional outbox.

```text
Business transaction
    -> write domain state
    -> write outbox event
    -> commit once
    -> worker reads outbox
    -> publish or process asynchronously
```

Use this for:

- analytics;
- email;
- notifications;
- insurance returns;
- inbox expiry;
- daily resets;
- retrying external callbacks;
- archival;
- delayed rewards.

```mermaid
sequenceDiagram
    autonumber
    participant S as Domain Service
    participant DB as PostgreSQL
    participant W as Outbox Worker
    participant X as External Service / Inbox
    S->>DB: Begin transaction
    S->>DB: Write authoritative state
    S->>DB: Insert outbox event
    S->>DB: Commit
    W->>DB: Claim pending events (FOR UPDATE SKIP LOCKED)
    W->>X: Process event with event ID
    alt Success
        W->>DB: Mark processed_at
    else Retryable failure
        W->>DB: Increment attempts; set available_at backoff
    else Terminal failure
        W->>DB: Mark failed; alert operator
    end
```

Add a message broker only when scaling requirements are proven.

---

# 22. Security Rules

Mandatory rules:

- all production APIs use HTTPS;
- clients never contain backend secrets;
- server credentials are isolated;
- Dedicated Server internal traffic uses mTLS and a short-lived token bound to `serverId`, certificate identity, and scope;
- Redpoint EOS transport verification and backend join-ticket authorization are both required before gameplay admission;
- join tickets are signed, match/PUID-bound, short-lived, and atomically consumed once;
- server APIs require server scope;
- client APIs require player scope;
- admin APIs require strong authentication and audit;
- rate limit public endpoints;
- verify ownership for every resource;
- validate every request;
- use parameterized SQL;
- rotate secrets;
- maintain Dev, Stage, and Production environments;
- never trust IDs sent by the client without authorization checks;
- never let the client directly grant currency or items.

Committed configuration must contain only non-secret identifiers and environment-independent defaults. Store EOS client secrets, backend server bootstrap credentials, mTLS private keys, signing keys, and production endpoints in environment-specific secret management. Maintain separate Dev, Stage, and Production EOS deployments and certificate authorities.

---

# 23. Testing Strategy

## 23.1 Unit Tests

Focus on:

- reward rules;
- inventory validation;
- wallet arithmetic;
- revision checks;
- permission checks;
- idempotency behavior;
- quest progression;
- insurance timing.

## 23.2 Integration Tests

Use Testcontainers for:

- PostgreSQL;
- Redis;
- object storage if required.

Important integration tests:

- duplicate idempotency key does not duplicate reward;
- two servers cannot commit the same match;
- player token cannot call server endpoint;
- expired token is rejected;
- revision mismatch returns 409;
- transaction rollback occurs if one inventory operation fails;
- server heartbeat expiry removes stale assignment;
- failed match commit can be retried safely.
- a player token cannot call a server endpoint, and a server token cannot exceed its server/match scope;
- an expired, revoked, wrong-match, wrong-PUID, or previously consumed join ticket is rejected;
- concurrent admission requests consume one ticket exactly once;

## 23.3 End-to-End Tests

Required scenarios:

- iPhone login through EOS;
- Android login through EOS;
- both clients receive backend tokens;
- party creation;
- matchmaking;
- server allocation;
- EOS Session registration;
- both mobile clients join the Mac Dedicated Server;
- Redpoint rejects an unencrypted or invalid EOS Connect ID-token transport handshake;
- a Redpoint-authenticated client is rejected when its Go join ticket does not match the assigned raid;
- authoritative match completion;
- backend result commit;
- inventory refresh;
- disconnect and reconnect.

## 23.4 Load Tests

Use k6.

Measure:

- p50;
- p95;
- p99;
- error rate;
- database connection count;
- lock duration;
- Redis latency;
- API CPU;
- memory;
- GC behavior;
- queue depth.

---

# 24. CI/CD Workflow

## 24.1 Backend Pipeline

```text
1. Format and lint.
2. Run unit tests.
3. Start Testcontainers.
4. Run integration tests.
5. Generate sqlc code.
6. Validate OpenAPI contract.
7. Build Go binary.
8. Build Docker image.
9. Run migration dry-check.
10. Publish image.
11. Deploy to target environment.
12. Run smoke tests.
```

Recommended checks:

```bash
go fmt ./...
go vet ./...
go test ./...
```

Optional:

```bash
golangci-lint run
```

## 24.2 Unreal Pipeline

```text
1. Compile game modules.
2. Compile Server Target.
3. Validate Redpoint EOS configuration.
4. Package iOS/Android Development builds.
5. Build Dedicated Server.
6. Run smoke server.
7. Execute automated login/join test where possible.
8. Publish artifacts.
```

## 24.3 Database Migration Rules

- migrations are immutable after merge;
- every schema change is reviewed;
- migrations are tested against clean database;
- migrations are tested against an upgraded database;
- destructive changes use a staged rollout;
- application code must tolerate rolling deployment when production scale requires it.

---

# 25. Implementation Phases

## Phase 0 — Technical Proof of Concept

### Goal

Prove the critical platform path before building business systems.

### Deliverables

- Mac Unreal Server Target builds successfully;
- Redpoint EOS works on macOS ARM64;
- EOS native libraries contain required ARM64 support;
- iPhone client logs in;
- Android client logs in;
- Mac Dedicated Server registers a session;
- iPhone and Android join the session;
- Redpoint encrypted DS transport verifies an EOS Connect ID token for a joining mobile client;
- Dedicated Server calls a minimal Go API;
- mobile clients call the Go API over LAN;
- ports and firewall are documented.

### Exit criteria

- one repeatable end-to-end test;
- no unresolved platform blocker;
- setup steps documented.

---

## Phase 1 — Repository and Local Infrastructure

### Goal

Create the backend foundation.

### Deliverables

- Go repository structure;
- `chi` HTTP server;
- configuration loading;
- PostgreSQL;
- Redis;
- MinIO;
- Docker Compose;
- Goose migrations;
- `sqlc`;
- health endpoints;
- structured logs;
- request IDs;
- basic OpenTelemetry;
- Makefile and scripts.

### Required endpoints

```text
GET /health/live
GET /health/ready
```

### Exit criteria

- new developer can run the stack with one documented command;
- tests run locally and in CI.

---

## Phase 2 — EOS Identity and Backend Sessions

### Goal

Create a secure player identity chain.

### Deliverables

- EOS token exchange endpoint;
- EOS token verification;
- `IIdentitySystem::Login` and `FIdentityUser::GetIdToken` integration on each target platform;
- Product User ID conversion and persistence as the `eos_connect` identity;
- InternalPlayerID;
- player and identity tables;
- first-login player creation;
- backend access tokens;
- refresh token rotation;
- session revocation;
- device session tracking;
- authentication tests.

### Exit criteria

- iOS and Android log in and call authenticated backend endpoints;
- duplicate identity does not create duplicate player records.

---

## Phase 3 — Player Profile

### Goal

Provide stable player data.

### Deliverables

- player profile schema;
- profile read endpoint;
- profile update rules;
- revision number;
- optimistic concurrency;
- validation;
- profile audit fields.

### Exit criteria

- profile reads and controlled updates work;
- concurrent update conflicts are handled.

---

## Phase 4 — Inventory and Economy Foundation

### Goal

Establish authoritative persistent game value.

### Deliverables

- item definitions;
- item instances;
- inventory containers;
- loadouts;
- wallets;
- economy ledger;
- idempotency store;
- transaction boundaries;
- inventory revision;
- admin-safe grant and revoke logic;
- tests for duplication and rollback.

### Exit criteria

- duplicate writes do not duplicate value;
- failed operations roll back fully;
- audit trail explains every wallet change.

---

## Phase 5 — Dedicated Server Registry

### Goal

Allow the backend to know which servers are available.

### Deliverables

- server authentication;
- mTLS bootstrap and certificate identity validation;
- short-lived server token issuance, rotation, revocation, and scope checks;
- register endpoint;
- heartbeat endpoint;
- server status;
- region;
- build version;
- map;
- mode;
- player capacity;
- stale server cleanup;
- server logs and metrics.

### Exit criteria

- server appears online;
- stale server is removed automatically;
- unauthorized callers cannot register.

---

## Phase 6 — Match Lifecycle

### Goal

Create authoritative match records.

### Deliverables

- match creation;
- player reservation;
- match start;
- player participation records;
- one-time match join-ticket issuance and atomic admission consumption;
- match end;
- authoritative commit;
- idempotency;
- retry handling;
- audit events;
- result read endpoint.

### Exit criteria

- one server can commit a match once;
- retries are safe;
- client cannot forge match results.

---

## Phase 7 — Matchmaking

### Goal

Connect party formation to server assignment.

### Deliverables

- matchmaking ticket API;
- party-aware tickets;
- region selection;
- mode and build compatibility;
- queue cancellation;
- matchmaker worker;
- server selection;
- assignment response;
- EOS Session linkage;
- Go is the sole queue/allocation authority; Redpoint Matchmaking runtime modules are not invoked;
- signed, match/PUID-bound join-ticket delivery;
- timeout and retry logic.

### Exit criteria

- iPhone and Android can enter queue;
- both receive the same match assignment;
- both join the correct session.
- both are admitted only after Redpoint token verification and Go join-ticket consumption.

---

## Phase 8 — Loadout Reservation and Match Commit

### Goal

Protect inventory during a match.

### Deliverables

- reserve loadout;
- lock or reservation records;
- match-bound inventory state;
- death result;
- extraction result;
- item consumption;
- item acquisition;
- commit transaction;
- abandoned match recovery;
- conflict handling.

```mermaid
sequenceDiagram
    autonumber
    participant C as Client
    participant B as Backend
    participant DB as PostgreSQL
    participant DS as Dedicated Server
    C->>B: Reserve loadout (match ID, expected revision)
    B->>DB: Lock eligible instances and create reservation
    B-->>C: Reservation confirmed
    DS->>B: Start match / validate reservations
    Note over DS: Items are authoritative in raid
    DS->>B: Commit results + idempotency key
    B->>DB: Atomically apply deltas, release locks, outbox event
    alt Commit fails before transaction completion
        B->>DB: Roll back; reservation recovery job evaluates expiry
    end
```

### Exit criteria

- a loadout cannot be used in two simultaneous matches;
- authoritative result updates inventory exactly once.

---

## Phase 9 — LiveOps

### Goal

Support runtime operations without rebuilding the client.

### Deliverables

- remote configuration;
- feature flags;
- maintenance mode;
- event schedules;
- map rotation;
- queue availability;
- minimum build;
- content compatibility;
- ETag caching;
- config versioning.

### Exit criteria

- operators can disable a queue safely;
- incompatible builds are blocked;
- config updates are observable and auditable.

---

## Phase 10 — Moderation and Admin Tools

### Goal

Provide operational control.

### Deliverables

- player search;
- match history;
- inventory audit;
- wallet ledger;
- grant/revoke with reason;
- ban and sanction workflow;
- server status;
- queue monitoring;
- admin audit log;
- role-based access control.

### Exit criteria

- every privileged action is attributable;
- sensitive actions require reason and permissions.

---

## Phase 11 — Analytics and Fraud Signals

### Goal

Create reliable operational and gameplay insights.

### Deliverables

- event schema;
- transactional outbox;
- analytics worker;
- event retention rules;
- economy anomaly detection;
- match anomaly signals;
- dashboards;
- alert thresholds.

### Exit criteria

- gameplay transaction does not wait for analytics processing;
- failed analytics processing can retry.

---

## Phase 12 — Production Hardening

### Goal

Prepare for external players.

### Deliverables

- Linux backend deployment;
- Linux Dedicated Server build;
- TLS;
- secret management;
- backups;
- database restore test;
- load test;
- abuse rate limiting;
- deployment rollback;
- environment separation;
- monitoring and alerting;
- incident runbook;
- cost monitoring.

### Exit criteria

- restore procedure is tested;
- rollback procedure is tested;
- load target is met;
- security checklist is complete.

---

# 26. Work Breakdown Rules for AI Agents

AI agents working on this project must follow these constraints.

## 26.1 Planning Rules

Every implementation plan must include:

- scope;
- assumptions;
- dependencies;
- affected modules;
- data model changes;
- API changes;
- security considerations;
- concurrency considerations;
- failure and retry behavior;
- migration steps;
- test plan;
- observability;
- rollout and rollback;
- acceptance criteria.

## 26.2 Coding Rules

AI-generated code must:

- compile;
- include error handling;
- pass context through Go APIs;
- avoid global mutable state;
- use parameterized SQL;
- use transactions for authoritative writes;
- use idempotency for retryable writes;
- validate authorization;
- avoid logging secrets;
- include tests;
- preserve module boundaries;
- avoid adding infrastructure without justification.

## 26.3 Database Rules

AI agents must not:

- alter old migrations after merge;
- use floating point for currency;
- use Redis as permanent storage;
- write authoritative economy operations without ledger entries;
- create JSON-only inventory storage without explicit approval;
- omit indexes for high-frequency queries;
- use unbounded queries.

## 26.4 Unreal Rules

AI agents must:

- keep gameplay realtime inside Unreal networking;
- avoid calling backend APIs every frame;
- separate client and server credentials;
- treat Dedicated Server as authoritative;
- avoid trusting client-provided rewards;
- ensure callbacks are safe against destroyed worlds and garbage-collected objects;
- include timeout, retry, and cancellation behavior for HTTP requests;
- keep API DTOs versioned.

---

# 27. Definition of Done

A backend feature is done only when:

- code is implemented;
- API contract is updated;
- migration is included if needed;
- unit tests pass;
- integration tests pass;
- authorization is verified;
- idempotency is addressed;
- observability is included;
- error cases are documented;
- rollback approach exists;
- acceptance criteria are met;
- team documentation is updated.

A multiplayer feature is done only when:

- client behavior works;
- Dedicated Server validation works;
- backend persistence works;
- reconnect behavior is considered;
- failure handling is tested;
- mobile device testing is completed;
- logs and metrics are available.

---

# 28. Non-Goals for the Initial Release

Do not implement these prematurely:

- Kubernetes;
- Kafka;
- service mesh;
- many microservices;
- multi-region active-active databases;
- custom transport protocol for backend APIs;
- gRPC to Unreal clients;
- full event sourcing;
- GraphQL for all game APIs;
- WebSocket for all updates;
- custom identity replacing EOS;
- distributed transactions across many services.

These may be added only when justified by measured scale or clear product requirements.

---

# 29. Initial Milestone Recommendation

The first meaningful milestone should be:

```text
Mobile EOS Login
    ->
Backend Token
    ->
Profile Load
    ->
Matchmaking Ticket
    ->
Mac Dedicated Server Assignment
    ->
EOS Session Join + Redpoint Transport Verification
    ->
Go One-Time Join-Ticket Admission
    ->
Authoritative Match Finish
    ->
Go Backend Commit
    ->
Inventory Refresh
```

This vertical slice validates the complete architecture before large feature investment.

---

# 30. Final Recommended Baseline

```text
Client:
    Unreal Engine C++
    Redpoint EOS
    iOS and Android

Dedicated Server:
    Unreal Server Target
    macOS for development
    Linux for production

Backend:
    Go
    net/http + chi
    pgx + sqlc
    PostgreSQL
    Redis
    OpenAPI
    OpenTelemetry

Architecture:
    Modular monolith
    REST + JSON
    Server-authoritative gameplay
    Go-authoritative matchmaking, allocation, admission, and persistence
    Redpoint EOS for identity, party/lobby, session discovery, and encrypted transport
    Backend-issued one-time join tickets
    mTLS + short-lived scoped Dedicated Server tokens

Local environment:
    Native Unreal Dedicated Server
    Docker Compose backend stack

Production:
    Linux containers
    Linux Unreal Dedicated Servers
    Managed PostgreSQL where possible
```

The architecture should evolve from one complete, secure vertical slice rather than from many disconnected services.

---

# 31. Suggested Next Planning Documents

The team should derive the following documents from this baseline:

1. `PHASE_0_TECHNICAL_POC.md`
2. `BACKEND_REPOSITORY_STRUCTURE.md`
3. `EOS_AUTH_FLOW.md`
4. `OPENAPI_CONTRACT.md`
5. `DATABASE_SCHEMA_V1.md`
6. `INVENTORY_ECONOMY_RULES.md`
7. `DEDICATED_SERVER_LIFECYCLE.md`
8. `MATCHMAKING_FLOW.md`
9. `LOCAL_MACOS_SETUP.md`
10. `CI_CD_PIPELINE.md`
11. `SECURITY_CHECKLIST.md`
12. `TEST_STRATEGY.md`
13. `PRODUCTION_READINESS_CHECKLIST.md`

Each document should reference this file as the top-level architecture source of truth.

---

# 32. Core Database DDL

This schema is the v1 PostgreSQL baseline. Use UUIDs generated by the application or `gen_random_uuid()`, UTC timestamps, `BIGINT` minor units for money, and immutable migrations. `updated_at` is changed by a shared trigger in the migration; event and ledger rows are intentionally append-only.

```sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE players (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  display_name TEXT NOT NULL CHECK (char_length(display_name) BETWEEN 3 AND 32),
  status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active','suspended','deleted')),
  revision BIGINT NOT NULL DEFAULT 1 CHECK (revision > 0),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE UNIQUE INDEX players_display_name_ci_uq ON players (lower(display_name));

CREATE TABLE player_identities (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(), player_id UUID NOT NULL REFERENCES players(id),
  provider TEXT NOT NULL, provider_user_id TEXT NOT NULL, linked_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  last_login_at TIMESTAMPTZ, created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (provider, provider_user_id), UNIQUE (player_id, provider)
);
CREATE INDEX player_identities_player_idx ON player_identities(player_id);

CREATE TABLE player_sessions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(), player_id UUID NOT NULL REFERENCES players(id),
  device_id TEXT NOT NULL, refresh_token_hash BYTEA NOT NULL, client_build TEXT NOT NULL,
  expires_at TIMESTAMPTZ NOT NULL, revoked_at TIMESTAMPTZ, last_used_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX player_sessions_active_idx ON player_sessions(player_id, expires_at) WHERE revoked_at IS NULL;

CREATE TABLE idempotency_keys (
  scope TEXT NOT NULL, key TEXT NOT NULL, request_hash BYTEA NOT NULL, response_code INT NOT NULL,
  response_body JSONB NOT NULL, expires_at TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(), PRIMARY KEY (scope, key)
);
CREATE INDEX idempotency_keys_expiry_idx ON idempotency_keys(expires_at);

CREATE TABLE item_definitions (
  id TEXT PRIMARY KEY, category TEXT NOT NULL, display_key TEXT NOT NULL, max_stack INT NOT NULL DEFAULT 1 CHECK(max_stack > 0),
  base_value BIGINT NOT NULL DEFAULT 0 CHECK(base_value >= 0), is_insurable BOOLEAN NOT NULL DEFAULT TRUE,
  config JSONB NOT NULL DEFAULT '{}'::jsonb, revision BIGINT NOT NULL DEFAULT 1,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE inventory_containers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(), player_id UUID NOT NULL REFERENCES players(id),
  kind TEXT NOT NULL CHECK(kind IN ('stash','secure','equipped','mail','loadout')), width INT NOT NULL CHECK(width > 0),
  height INT NOT NULL CHECK(height > 0), revision BIGINT NOT NULL DEFAULT 1,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now(), UNIQUE(player_id, kind)
);
CREATE INDEX inventory_containers_player_idx ON inventory_containers(player_id);

CREATE TABLE item_instances (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(), definition_id TEXT NOT NULL REFERENCES item_definitions(id),
  owner_player_id UUID REFERENCES players(id), container_id UUID REFERENCES inventory_containers(id),
  stack_count INT NOT NULL DEFAULT 1 CHECK(stack_count > 0), durability NUMERIC(7,2), position_x INT, position_y INT,
  rotation SMALLINT NOT NULL DEFAULT 0 CHECK(rotation IN (0,90)), state TEXT NOT NULL DEFAULT 'owned'
    CHECK(state IN ('owned','reserved','in_raid','destroyed','escrow')),
  locked_by_match_id UUID, revision BIGINT NOT NULL DEFAULT 1,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  CHECK ((container_id IS NULL) = (state IN ('in_raid','destroyed')))
);
CREATE INDEX item_instances_owner_state_idx ON item_instances(owner_player_id, state);
CREATE INDEX item_instances_container_idx ON item_instances(container_id) WHERE container_id IS NOT NULL;

CREATE TABLE item_properties (
  item_instance_id UUID PRIMARY KEY REFERENCES item_instances(id) ON DELETE CASCADE,
  properties JSONB NOT NULL DEFAULT '{}'::jsonb, created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE wallets (
  player_id UUID NOT NULL REFERENCES players(id), currency_code TEXT NOT NULL,
  balance BIGINT NOT NULL DEFAULT 0 CHECK(balance >= 0), revision BIGINT NOT NULL DEFAULT 1,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now(), PRIMARY KEY(player_id, currency_code)
);

CREATE TABLE economy_transactions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(), player_id UUID NOT NULL REFERENCES players(id), currency_code TEXT NOT NULL,
  amount BIGINT NOT NULL CHECK(amount <> 0), balance_after BIGINT NOT NULL CHECK(balance_after >= 0),
  reason TEXT NOT NULL, reference_type TEXT NOT NULL, reference_id TEXT NOT NULL, idempotency_key TEXT NOT NULL,
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb, created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(player_id, idempotency_key)
);
CREATE INDEX economy_transactions_player_created_idx ON economy_transactions(player_id, created_at DESC);

CREATE TABLE loadouts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(), player_id UUID NOT NULL REFERENCES players(id), name TEXT NOT NULL,
  revision BIGINT NOT NULL DEFAULT 1, created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX loadouts_player_idx ON loadouts(player_id);
CREATE TABLE loadout_items (
  loadout_id UUID NOT NULL REFERENCES loadouts(id) ON DELETE CASCADE, item_instance_id UUID NOT NULL REFERENCES item_instances(id),
  slot TEXT NOT NULL, reservation_state TEXT NOT NULL DEFAULT 'available' CHECK(reservation_state IN ('available','reserved','committed','released')),
  reserved_match_id UUID, reserved_at TIMESTAMPTZ, created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY(loadout_id, item_instance_id), UNIQUE(loadout_id, slot)
);
CREATE INDEX loadout_items_reservation_idx ON loadout_items(reserved_match_id) WHERE reserved_match_id IS NOT NULL;

CREATE TABLE server_registrations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(), region TEXT NOT NULL, build_id TEXT NOT NULL, endpoint TEXT NOT NULL,
  capacity INT NOT NULL CHECK(capacity > 0), current_players INT NOT NULL DEFAULT 0 CHECK(current_players >= 0),
  status TEXT NOT NULL CHECK(status IN ('ready','allocated','draining','offline')), token_hash BYTEA NOT NULL,
  last_heartbeat_at TIMESTAMPTZ NOT NULL DEFAULT now(), revision BIGINT NOT NULL DEFAULT 1,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX server_registrations_select_idx ON server_registrations(region, build_id, status, last_heartbeat_at);

CREATE TABLE match_records (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(), server_id UUID NOT NULL REFERENCES server_registrations(id), mode_id TEXT NOT NULL, map_id TEXT NOT NULL,
  state TEXT NOT NULL CHECK(state IN ('created','starting','in_progress','committing','committed','abandoned','failed')),
  loot_seed BIGINT NOT NULL, started_at TIMESTAMPTZ, ended_at TIMESTAMPTZ, committed_at TIMESTAMPTZ,
  revision BIGINT NOT NULL DEFAULT 1, created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX match_records_server_state_idx ON match_records(server_id, state);

CREATE TABLE match_participants (
  match_id UUID NOT NULL REFERENCES match_records(id), player_id UUID NOT NULL REFERENCES players(id),
  eos_product_user_id TEXT NOT NULL,
  state TEXT NOT NULL DEFAULT 'reserved' CHECK(state IN ('reserved','joined','disconnected','dead','extracted','mia')),
  extracted_at TIMESTAMPTZ, joined_at TIMESTAMPTZ, revision BIGINT NOT NULL DEFAULT 1,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now(), PRIMARY KEY(match_id, player_id)
);
CREATE INDEX match_participants_player_idx ON match_participants(player_id, created_at DESC);
CREATE UNIQUE INDEX match_participants_match_puid_uq ON match_participants(match_id, eos_product_user_id);

CREATE TABLE match_join_tickets (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(), match_id UUID NOT NULL REFERENCES match_records(id),
  player_id UUID NOT NULL REFERENCES players(id), eos_product_user_id TEXT NOT NULL, jti UUID NOT NULL UNIQUE,
  token_hash BYTEA NOT NULL, build_id TEXT, region TEXT, expires_at TIMESTAMPTZ NOT NULL,
  consumed_at TIMESTAMPTZ, consumed_by_server_id UUID REFERENCES server_registrations(id),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(match_id, player_id, jti)
);
CREATE INDEX match_join_tickets_pending_idx ON match_join_tickets(match_id, expires_at) WHERE consumed_at IS NULL;

CREATE TABLE server_credential_audit (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(), server_id UUID NOT NULL REFERENCES server_registrations(id),
  certificate_subject TEXT NOT NULL, token_jti UUID NOT NULL, token_expires_at TIMESTAMPTZ NOT NULL,
  revoked_at TIMESTAMPTZ, reason TEXT, created_at TIMESTAMPTZ NOT NULL DEFAULT now(), UNIQUE(token_jti)
);
CREATE INDEX server_credential_audit_active_idx ON server_credential_audit(server_id, token_expires_at) WHERE revoked_at IS NULL;

CREATE TABLE match_item_changes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(), match_id UUID NOT NULL REFERENCES match_records(id), player_id UUID NOT NULL REFERENCES players(id),
  item_instance_id UUID REFERENCES item_instances(id), change_type TEXT NOT NULL CHECK(change_type IN ('bring_in','acquire','consume','extract','lose','destroy')),
  definition_id TEXT, quantity INT NOT NULL DEFAULT 1 CHECK(quantity > 0), payload JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX match_item_changes_match_player_idx ON match_item_changes(match_id, player_id);

CREATE TABLE outbox_events (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(), aggregate_type TEXT NOT NULL, aggregate_id TEXT NOT NULL, event_type TEXT NOT NULL,
  payload JSONB NOT NULL, available_at TIMESTAMPTZ NOT NULL DEFAULT now(), attempts INT NOT NULL DEFAULT 0,
  processed_at TIMESTAMPTZ, failed_at TIMESTAMPTZ, last_error TEXT, created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX outbox_events_pending_idx ON outbox_events(available_at, created_at) WHERE processed_at IS NULL AND failed_at IS NULL;
```

Run a scheduled cleanup for expired `idempotency_keys` (retain at least 24 hours for player writes and 7 days for match commits). Add foreign keys that depend on later sections only in their own migration; do not create circular dependencies.

# 33. OpenAPI Contract Baseline

`openapi/v1.yaml` is the executable contract and is the only source used to generate Go and Unreal DTOs. All JSON uses lower camel case. Every error has the envelope below and a stable `code` from Section 34.

```json
{"error":{"code":"inventory_revision_conflict","message":"Inventory has changed","requestId":"01J...","retryable":true}}
```

| Endpoint | Request | Success response | Primary errors |
|---|---|---|---|
| `POST /v1/auth/eos` | `token`, `deviceId`, `clientBuild` | access/refresh token, expiry, player | 400, 401, 403, 429 |
| `POST /v1/auth/refresh` | `refreshToken` | rotated token pair, expiry | 400, 401 |
| `GET /v1/profile` | — | player, `revision` | 401, 404 |
| `GET /v1/inventory` | — | containers, items, revision | 401, 404 |
| `POST /v1/loadouts/reserve` | `loadoutId`, `matchId`, expected revision | reservation and inventory revision | 400, 401, 409, 423 |
| `POST /v1/matchmaking/tickets` | `mode`, `region`, optional `partyId`, build compatibility | ticket ID and status | 400, 401, 409, 429 |
| `GET /v1/matchmaking/tickets/{id}` | — | status and optional assignment | 401, 404 |
| `DELETE /v1/matchmaking/tickets/{id}` | — | no content | 401, 404 |
| `GET /v1/liveops/config` | `If-None-Match` optional | config, ETag | 304, 401 |

| Internal endpoint | Request | Success response | Primary errors |
|---|---|---|---|
| `POST /v1/internal/servers/register` | region, build, endpoint, capacity; mTLS client certificate | server ID, scoped token, expiry | 400, 401, 403 |
| `POST /v1/internal/servers/{id}/heartbeat` | status, currentPlayers, match IDs | acknowledgement | 401, 404 |
| `POST /v1/internal/matches/start` | server ID, player IDs, mode, map, loot seed | match ID, reservations | 400, 401, 403 |
| `POST /v1/internal/matches/{id}/admit-player` | signed join ticket; verified EOS Product User ID | player admission and reserved loadout reference | 401, 403, 404, 409, 422 |
| `POST /v1/internal/matches/{id}/commit` | participant outcomes, item changes, `idempotencyKey` | committed revision and receipt | 400, 401, 403, 409, 422 |

For all mutating public endpoints, require `Idempotency-Key`; return the stored original status/body for a duplicate key with an identical request hash. Reject a duplicate key used with a different payload. Internal commit requests use a key derived from `matchId + commitVersion` and must never accept client-supplied item ownership.

## 33.1 Representative Schemas

```yaml
AuthEOSRequest:
  type: object
  required: [token, deviceId, clientBuild]
  properties:
    token: {type: string, minLength: 1}
    deviceId: {type: string, minLength: 8, maxLength: 256}
    clientBuild: {type: string, maxLength: 64}
MatchCommitRequest:
  type: object
  required: [results, itemChanges, idempotencyKey]
  properties:
    idempotencyKey: {type: string, format: uuid}
    results: {type: array, minItems: 1}
    itemChanges: {type: array}
MatchAdmissionRequest:
  type: object
  required: [joinTicket, eosProductUserId]
  properties:
    joinTicket: {type: string, minLength: 1}
    eosProductUserId: {type: string, minLength: 1}
```

# 34. Error Catalog and Retry Rules

| Family | Codes | Client action |
|---|---|---|
| Auth | `auth_token_expired`, `auth_token_invalid`, `auth_session_revoked`, `auth_device_mismatch` | Refresh once for expiry; otherwise sign in again. |
| Inventory | `inventory_revision_conflict`, `inventory_item_not_found`, `inventory_container_full`, `inventory_item_locked` | Refresh state; do not guess a correction. |
| Economy | `economy_insufficient_funds`, `economy_duplicate_transaction`, `economy_ledger_mismatch` | Never retry a failed purchase without its idempotency key; alert on mismatch. |
| Matchmaking | `matchmaking_queue_full`, `matchmaking_ticket_expired`, `matchmaking_already_in_queue`, `matchmaking_incompatible_build` | Show clear UI; retry only queue-full after a delay. |
| Server | `server_capacity_exceeded`, `server_not_registered`, `server_heartbeat_expired` | Re-register or drain; do not assign more players. |
| Match | `match_already_committed`, `match_invalid_state`, `match_player_not_in_match` | Treat already committed as success only when receipt matches. |

Player API retry: exponential backoff 1, 2, 4, 8 seconds, then up to 30 seconds, with full jitter. Dedicated Server retry: immediately once, then 500 ms, 1 s, 2 s up to 10 seconds. Retry only connection failures, 408, 429, and 5xx explicitly marked `retryable`; never retry validation/authorization errors. Stop retries when the game world or request owner is destroyed.

# 35. Rate Limiting Policy

Implement Redis token buckets with a PostgreSQL-independent fallback that fails closed for auth and fails soft for non-sensitive reads during a Redis outage. Return `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, and `429` with `Retry-After`.

| Category | Limit / window | Scope |
|---|---:|---|
| Auth | 10 / 60 s | IP; additionally 20 / hour per device |
| Profile read | 60 / 60 s | player |
| Inventory read | 60 / 60 s | player |
| Matchmaking create | 5 / 60 s | player |
| Server heartbeat | 30 / 60 s | server |
| Match commit | 10 / 60 s | server |
| Admin | 120 / 60 s | admin identity |

---

# 36. Extraction Shooter Core Mechanics

The authoritative raid state machine is `lobby -> deploying -> in_raid -> extracting -> extracted | dead | mia -> committing -> complete`. The Dedicated Server owns every transition and emits a signed authoritative result. The backend only persists a valid transition for registered match participants.

```mermaid
stateDiagram-v2
    [*] --> Lobby
    Lobby --> Deploying: reservation accepted
    Deploying --> InRaid: server start
    InRaid --> Extracting: validates point/condition
    Extracting --> Extracted: timer completes
    InRaid --> Dead: lethal server event
    InRaid --> MIA: raid timeout / unrecovered disconnect
    Extracted --> Committing
    Dead --> Committing
    MIA --> Committing
    Committing --> Complete: idempotent backend commit
```

- Use a **grid-based stash**: container width/height plus item footprint and rotation. Secure containers are dedicated, small grid containers with a server-defined allowlist.
- Loadout items are locked before deployment. Items acquired in raid carry `found_in_raid=true` only when generated by the server seed/table or received from a valid in-raid action.
- Extraction validates location volume, alive status, no disallowed combat condition, team rule, required item/payment, and uninterrupted timer. UI can predict the timer; only DS completion counts.
- Durability, ammunition, attachments, and item metadata are DS changes. The client sends intent only.
- Hideout and Scav modes are optional product systems; keep their persistent changes in the same ledger/inventory transaction model.

# 37. Insurance System

Insurance is purchased before a raid for eligible owned instances. Tiers define price, return delay, and eligible categories. States are `insured -> claim_pending -> returned | lost | expired`.

```text
Insure eligible item -> lock policy to match -> player dies/MIA -> commit checks item extraction
 -> unextracted insured item becomes claim_pending -> delayed outbox job -> inbox return -> player claims
```

Create `insurance_policies(id, player_id, provider_id, item_instance_id, premium, status, expires_at)`, `insurance_claims(id, policy_id, match_id, state, return_after)`, and `insurance_returns(id, claim_id, inbox_message_id, claimed_at)`. A single item has at most one active policy. `POST /v1/insurance/insure` requires an idempotency key; `GET /v1/insurance/claims` is read-only.

At match commit, the backend creates claims only for insured instances which were not extracted by any participant. Do not model “who looted it” from untrusted client events: the DS result supplies item custody. To limit collusion, flag rapid teammate handoffs, repeated mutual deaths, abnormal same-party recovery, and insure/drop/extract patterns for review; do not automatically remove valid returns solely from a heuristic.

# 38. Loot Tables and Item Spawning

The backend versions and signs the selected loot configuration; the DS deterministically generates loot from `match.loot_seed`, map, table version, and spawn zone. The client never receives a seed or can request a roll.

Use `loot_tables(id, map_id, version, active_from, active_to)`, `loot_zones(id, table_id, zone_key, multiplier)`, and `loot_table_entries(id, zone_id, item_definition_id, min_quantity, max_quantity, weight, rarity, conditions)`. Publish table snapshots through LiveOps and retain every version used by a match for audit/replay.

Dynamic modifiers may adjust weights by event, map, or player population, but must be resolved at match start and written to the match metadata. The DS validates container opens, capacity, one-time spawn use, and every transfer; it reports only final authoritative item changes.

# 39. Premium Currency and Shop

Supported currency classes are soft earned currency, premium purchased currency, and non-currency entitlements. Never use floating point. The mobile client obtains a store transaction/receipt, backend verifies it server-side with the relevant store provider, persists a unique external transaction ID, credits premium currency in the immutable ledger, and returns the updated wallet.

Use `shop_items`, `shop_bundles`, `shop_rotations`, `purchase_receipts`, and `entitlements`; each price references a catalog version. `GET /v1/shop/catalog` returns a signed/ETagged active catalog. `POST /v1/shop/purchase` accepts a catalog item/version plus idempotency key, locks the wallet, writes debit/credit ledger entries and grants atomically. Refund webhooks reverse or freeze a specific entitlement/credit according to product policy; they never delete audit rows.

# 40. Gacha / Lootbox System

All rolls run server-side. The active pool and its probability disclosure are versioned and retained with each roll. Use `gacha_pools`, `gacha_pool_entries`, `gacha_pity_counters`, and append-only `gacha_rolls` containing pool version, roll sequence, result, pity state before/after, and transaction reference.

`POST /v1/gacha/open` requires pool ID, count, and idempotency key; it locks wallet and pity counter, validates cost, generates cryptographically secure server randomness, writes the ledger and grants in one transaction. `GET /v1/gacha/pools` exposes item probabilities, guarantee rules, and jurisdictionally required disclosures. Product/legal review must approve availability, age gates, receipts, and disclosure wording in every launch territory before release.

# 41. Quest and Progression

Use versioned `quest_definitions`, `quest_objectives`, `quest_progress`, `trader_standings`, and immutable reward grants. Quest types: daily, weekly, seasonal, and storyline/trader. Objective types: kill, extract, find-in-raid, deliver, survive.

The DS reports normalized gameplay events at match commit; the backend validates participant, mode, item provenance, and duplicate event IDs before updating progress. Offline UI is advisory only. `GET /v1/quests` returns active definitions/progress; `POST /v1/quests/{id}/complete` only claims a backend-validated completed quest and uses idempotency. Rewards (items, XP, soft currency, reputation) share one transaction and outbox event.

# 42. Battle Pass and Seasons

Create `seasons`, `season_tiers`, `season_tier_rewards`, `player_season_progress`, and `season_reward_claims`. A season has start/end timestamps, status, XP rules, free/premium tracks, and a frozen content version. XP derives from trusted raid/quest completion records only.

`GET /v1/season/current` returns current season, tiers, ownership, progress, and claim states. `POST /v1/season/claim-tier` locks progress/claim row, validates track entitlement and required XP, then grants atomically. On season close, retain the frozen record, define a fixed grace window for claims, and use inbox grants for any explicitly approved automatic rewards. Never silently carry premium entitlements or unclaimed rewards across seasons without a product rule.

---

# 43. Notifications and Inbox

Use `inbox_messages(id, player_id, type, subject_key, payload, state, expires_at, claimed_at)` and `push_registrations(id, player_id, platform, token_hash, enabled_at, revoked_at)`. Inbox state is `created -> read -> claimed | expired`; a reward-bearing message cannot be claimed twice.

`GET /v1/inbox` is paginated. `POST /v1/inbox/{id}/claim` is idempotent and grants attached rewards in the same transaction. Outbox workers send APNS/FCM as best-effort notification only; the inbox is the source of truth. Do not put rewards or sensitive player data in push payloads. Expire stale messages with a worker and retain a minimal audit record.

# 44. Reconnection and Session Recovery

On a transient disconnect, DS marks a participant `disconnected` and preserves its server state for a **three-minute** reconnect window. Client reauthenticates, calls `POST /v1/matches/rejoin`, and receives assignment only if token, build, player, match state, and DS reconnect window all match. DS finally admits the reconnecting EOS identity.

```mermaid
sequenceDiagram
    participant C as Client
    participant DS as Dedicated Server
    participant B as Backend
    C-xDS: Network lost
    DS->>B: Participant disconnected
    Note over DS: Preserve state for 3 minutes
    C->>B: POST /v1/matches/rejoin
    B->>DS: Validate active reservation/window
    DS-->>B: Join approved or rejected
    B-->>C: EOS session join data or reason
    C->>DS: Rejoin session
```

If DS crashes, do not pretend a live raid can safely resume unless durable state snapshots, compatible process recovery, and playtesting prove it. For v1, mark the match `abandoned`, preserve auditable server logs, release unconsumed reserved loadouts by a controlled recovery job, and apply a documented compensation policy. Persistent inventory changes still occur only at commit.

# 45. Anti-Cheat and Trust

Integrate EAC where the platform/device supports it and keep platform-specific capability documentation current. EAC is one signal, not a replacement for authoritative gameplay. DS validates movement envelopes, fire rate, damage inputs, line-of-sight where relevant, inventory transfer rules, loot counts, extraction conditions, and signed backend assignments.

The pipeline is report -> evidence collection -> investigation -> sanction -> appeal/audit. Store `player_reports`, `sanctions`, and immutable moderation audit records. Reports require reporter identity, target, category, match, and bounded evidence metadata. Sanctions have scope, reason code, actor, start/end, and review state. Never automatically ban solely from one client report; reserve automatic immediate action for high-confidence server/EAC signals approved by policy.

# 46. Scaling Strategy: Initial 1K CCU

For approximately 1,000 CCU, use one PostgreSQL primary with backups, standalone persistent Redis, one or more stateless Go API instances behind a reverse proxy, and a manually operated Linux DS pool. PgBouncer is recommended before connection pressure appears. Keep a single region and measure before adding components.

| Milestone | Change trigger | Next action |
|---|---|---|
| 1K CCU | DB CPU >60% sustained, p95 API >250 ms, pool >70% | tune queries/indexes; PgBouncer; second API replica |
| 5K CCU | DS allocation delays, Redis >70% memory, DB read load high | automate DS allocator; read replica for safe reads; managed Redis review |
| 10K CCU | regional latency or primary write pressure | regional DS pools; partition operational workloads; formal capacity tests |
| 50K+ CCU | sustained multi-region demand | multi-region design, dedicated SRE/DBA review; do not lift-and-shift blindly |

Capacity work is driven by load tests representing login bursts, ticket creation, server heartbeats, commit spikes, and inbox workers. Track per-environment infrastructure cost, DS instance-hour, database storage/IOPS, egress, and alert on budget variance. Cost estimates must be obtained from the selected provider at purchase time, not embedded as stale architecture facts.

# 47. Disaster Recovery and Backup

Initial targets: RTO under four hours, RPO under one hour. PostgreSQL uses daily logical backup plus continuous WAL archiving; periodically test physical/base backups if data size makes logical recovery too slow. Redis uses AOF plus RDB snapshots but is rebuilt as cache when necessary. Object storage buckets are versioned and lifecycle-managed.

Monthly restore drill: (1) select a backup and target timestamp, (2) restore to isolated environment, (3) apply WAL, (4) run integrity and row-count checks, (5) verify a sampled ledger/inventory/match relationship, (6) rotate temporary credentials and destroy drill data, (7) record actual RTO/RPO and corrective work. Maintain a current contact-free solo runbook with backup locations, access procedure, DNS/reverse-proxy rollback, and customer communication templates.

# 48. Data Retention and Privacy

Define the player-facing privacy notice and jurisdictional requirements with qualified legal review before collecting data. Baseline retention: match records one year; economy ledger permanently or for the legally required financial/audit period; admin audit logs two years; raw analytics 90 days then anonymized/aggregated; chat logs 30 days unless a valid investigation hold applies.

`GET /v1/admin/players/{id}/export` creates an audited, access-controlled export job; never synchronously return a large data package. `DELETE /v1/admin/players/{id}/gdpr` starts a verified deletion/anonymization workflow, not an unaudited hard delete. Replace direct identifiers with irreversible surrogate values where records must be retained for fraud, financial, or legal obligations, revoke sessions/tokens, and retain only the documented minimum. Track requests, decisions, legal holds, and completion evidence.

# 49. Flea Market / Player Marketplace (Roadmap)

Do not implement before item locking, ledger, audit, fraud detection, and load tests are proven. The model is listing -> escrow -> buy/bid -> settlement -> delivery/expiry. At listing, lock and escrow the exact item instances in a transaction. At purchase, lock the buyer wallet and listing, debit price plus fee/tax sink, credit seller, transfer item or create inbox delivery, and write all ledger/audit rows atomically.

Initial controls: seller reputation/trader-level gate, quantity/price bounds, listing caps, cooldowns, anomaly review, immutable item provenance, and no trust in display prices supplied by the client. Design the data model later; avoid premature full DDL.

# 50. Content Delivery and Patching (Roadmap)

Use signed build manifests containing app version, content version, compatibility hash, minimum supported version, required chunks, and expiry. Distribute large mobile content through platform/CDN-supported delivery. Backend LiveOps config can gate queues by compatibility hash; it cannot safely replace a signed client patch system.

Maintain a compatibility matrix for client, DS, backend API, schema, and content. Forced updates block login before matchmaking when a critical version is unsupported. Hot fixes are restricted to pre-approved data/config changes; native code, anti-cheat, and security changes follow platform release rules.

# 51. Real-Time Backend Updates (Roadmap)

Start with REST polling: ticket status every 2–5 seconds while the queue UI is visible, inbox refresh on foreground/login, and ETag polling for LiveOps. Add WebSocket or SSE only when measured polling cost or product UX requires it. WebSocket is appropriate for ticket assignments, inbox badge updates, and LiveOps invalidation—not real-time combat.

Authenticate the connection with a short-lived backend token, authorize every subscribed topic, enforce connection/message limits, refresh before expiry, and reconnect with jitter. Mobile clients must fall back to polling when backgrounding, captive portals, or unreliable networks break a long-lived connection.

# 52. Multi-Region Roadmap

Consider multi-region only for sustained latency/product/regulatory needs, normally above 10K CCU. Start with regional DS fleets and matchmaking affinity while retaining a clearly defined primary persistence region. Avoid active-active inventory/economy writes until the team can operate conflict-free ownership boundaries and recovery procedures.

Future phases may add regional read replicas for safe reads, a global server registry, region-aware queue rules, data residency controls, and separate disaster-recovery exercises. Each step requires latency measurements, failure-mode testing, cost model, data ownership decision, and an explicit rollback plan.

---

# 53. Expanded Sequential Delivery Plan

For a solo developer, complete and verify work in this order; do not parallelize dependent persistent-state work.

1. **Phase A — Core depth:** diagrams, DDL, OpenAPI, errors, rate limiting. Exit when migrations, contract validation, and all diagrams are reviewed together.
2. **Phase B — Extraction and economy:** Sections 36–42. Exit when a simulated raid safely reserves, commits, rolls back, insures, rewards quests, and writes audit records.
3. **Phase C — Operational readiness:** Sections 43–48 plus the Section 24 runbook. Exit after reconnect, backup restore, abuse, and 1K-CCU load scenarios are tested.
4. **Phase D — Roadmap:** Sections 49–52 are design-only until measured scale/product evidence authorizes implementation.

## 53.1 Deployment Runbook Addendum

Before deployment: confirm target environment, clean migration status, backup freshness, error budget, compatible DS/client builds, and rollback artifact. Deploy backend to a small canary (or one instance), run health/auth/inventory/commit smoke tests with synthetic data, then progress 10% -> 50% -> 100% while watching error rate, latency, DB locks, and queue/heartbeat health. Roll back application binaries/config immediately for behavioral failure; use forward-fix migrations unless the migration has a tested, safe rollback. Record incident timeline, impact, mitigation, and follow-up actions.

---

# 54. Redpoint EOS Runtime Contract

This section records the selected integration boundary against the Redpoint EOS Online Framework source bundled with the project. It is normative for runtime implementation.

## 54.1 Fact, Rule, and Owner

| Redpoint EOS fact | Architecture rule | Owner |
|---|---|---|
| `IIdentitySystem::Login` produces `FIdentityUser`; `GetIdToken` returns the EOS Connect ID token. | Client exchanges this token with Go; Go maps the verified EOS Product User ID to `players.id`. | Unreal client + Go auth |
| Runtime identity is `UE::Online::FAccountId`; Redpoint core converts it to Product User ID. | Persist only the Product User ID as `eos_connect` identity; never use Epic Account ID as the gameplay primary key. | Unreal integration + DB |
| `IdTokenAuthNetworkingLayer` requests/delivers a client token over encrypted DS transport and calls `VerifyIdToken`. | DS treats successful Redpoint verification as transport identity proof only. It must then request Go admission before spawning/admitting gameplay. | DS GameMode / PreLogin |
| Redpoint Matchmaking contains queue state, candidate matching, dedicated-server beacon reservation, and client travel. | `IMatchmakingEngine`, `Matchmaking`, and `MatchmakingMatchmaker` are excluded from production runtime. Go owns all matchmaking and allocation state. | Unreal frontend + Go matchmaker |

Source references: `Docs/RedpointEOS/docs/systems/identity.md`, `Docs/RedpointEOS/docs/systems/user_id.md`, `RedpointEOSNetworking/.../IdTokenAuthNetworkingLayer.cpp`, and the plugin `Matchmaking` documentation/source.

## 54.2 Hybrid Admission Flow

```mermaid
sequenceDiagram
    autonumber
    participant C as Unreal Client
    participant R as Redpoint EOS
    participant B as Go Backend
    participant DB as PostgreSQL
    participant DS as Dedicated Server
    C->>R: IIdentitySystem.Login
    R-->>C: FIdentityUser + EOS Connect ID token
    C->>B: Exchange EOS token for backend session
    B->>DB: Verify/map PUID to InternalPlayerID
    C->>B: Create matchmaking ticket
    B->>DB: Match, reserve loadout, issue JTI-bound join ticket
    DS->>R: Publish selected EOS Session
    B-->>C: Session discovery + join ticket
    C->>DS: Connect through Redpoint EOS
    DS->>C: Request EOS Connect ID token over encrypted channel
    C-->>DS: Deliver token
    DS->>R: VerifyIdToken for connecting PUID
    DS->>B: Admit player (ticket + verified PUID) over mTLS
    B->>DB: Validate claims; consume JTI once; mark joined
    B-->>DS: Admit with internal player ID
    DS->>B: Idempotent match commit over mTLS
    B->>DB: Inventory/economy/outbox transaction
```

The join ticket claims are `matchId`, `playerId`, `eosProductUserId`, `jti`, `exp`, `buildId` when applicable, and `region` when applicable. The DS obtains the verified Product User ID from the Redpoint-authenticated connection, not from untrusted game RPC input. A ticket expiry of 60 seconds is the v1 default; refresh/reissue is allowed only while the backend assignment is active.

## 54.3 Admission and Failure Matrix

| Condition | Required behavior | Stable error / operational action |
|---|---|---|
| EOS login or backend exchange fails | No backend session or queue access. | `auth_token_invalid` / show sign-in recovery. |
| Transport is unencrypted or Redpoint token verification fails | DS disconnects before application admission. | Redpoint networking failure; record non-secret reason. |
| Ticket expired, wrong match, wrong PUID, or wrong build/region | DS rejects admission; client refreshes assignment only if still queued/assigned. | `match_join_ticket_invalid`. |
| Ticket JTI already consumed | Reject duplicate connection; never spawn a second participant. | `match_join_ticket_consumed`. |
| Server heartbeat/token is expired or revoked | Backend denies admission/start/commit; allocator drains server. | `server_heartbeat_expired` or `server_token_invalid`. |
| Duplicate commit | Return the original commit receipt without a second inventory/economy write. | `match_already_committed` with matching receipt. |
| DS crash before commit | Mark match abandoned; run controlled reservation recovery/compensation policy. | No client-side reward inference. |

## 54.4 Required Delivery Order

1. Verify `IIdentitySystem` login, Product User ID conversion, and backend token exchange on client platforms.
2. Verify Redpoint encrypted DS transport and EOS ID-token verification before any custom admission logic.
3. Implement mTLS server registration, rotation, scoped token validation, and heartbeat drain behavior.
4. Implement Go-owned ticket/allocation/session-publication flow; do not link the Redpoint matchmaking runtime modules.
5. Implement signed one-time join ticket persistence and DS admission after Redpoint verification.
6. Implement match start/commit and transactional inventory/economy/outbox processing.
7. Run the Section 23 admission, duplicate-consumption, mTLS-scope, and end-to-end mobile-to-DS scenarios before enabling external players.
