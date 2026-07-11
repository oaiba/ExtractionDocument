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

The Dedicated Server must not directly modify database tables. It calls protected backend APIs.

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
- server registry;
- match records;
- live operations configuration;
- feature flags;
- moderation and sanctions;
- audit logs;
- admin APIs;
- persistence;
- analytics event publishing.

The backend is the source of truth for persistent live-service data.

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
1. Client logs in through Redpoint EOS.
2. Client obtains an EOS identity token.
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

---

# 8. Dedicated Server Authentication

Dedicated Server credentials must be separate from player tokens.

Recommended model:

```text
Server process
    -> workload identity
    -> short-lived server access token
    -> protected internal backend endpoints
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
```

Never reuse client credentials for server actions.

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
7. Backend selects or allocates a Dedicated Server.
8. Dedicated Server registers an EOS Session.
9. Backend assigns players to the session.
10. Clients join through Redpoint EOS.
11. Dedicated Server loads authoritative player loadouts.
12. Gameplay runs through Unreal networking.
13. Dedicated Server produces authoritative results.
14. Dedicated Server commits match results to backend.
15. Backend applies database transaction.
16. Client refreshes profile or receives a delta.
```

---

# 13. Matchmaking and Sessions

Use:

- EOS Lobby for party state;
- backend matchmaking tickets for queue decisions;
- EOS Sessions for active match instances.

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

Add a message broker only when scaling requirements are proven.

---

# 22. Security Rules

Mandatory rules:

- all production APIs use HTTPS;
- clients never contain backend secrets;
- server credentials are isolated;
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
- timeout and retry logic.

### Exit criteria

- iPhone and Android can enter queue;
- both receive the same match assignment;
- both join the correct session.

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
EOS Session Join
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
    Backend-authoritative persistence
    EOS for online platform services

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
