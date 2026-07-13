# LiveOps Admin UI Page Specification

## Global UI Rules

- Admin Web uses Next.js + TypeScript after this design phase.
- Every page gets data only through Admin API.
- Permission checks occur in the backend and are mirrored in navigation.
- All mutating actions show environment, target, reason, before/after, and confirmation.
- Loading, empty, error, stale, and permission-denied states are explicit.
- All timestamps are rendered in UTC with local-time disclosure only as a secondary view.

## Navigation Wireframe

```text
Admin Web
├── Overview
├── LiveOps
│   ├── Config List
│   ├── Draft Editor
│   ├── Validation
│   ├── Diff
│   ├── Review / Approval
│   └── Publish / Rollback
├── Player Support
│   ├── Search
│   ├── Player Detail
│   ├── Inventory Audit
│   ├── Wallet Ledger
│   └── Commands
├── Moderation
├── Infrastructure
│   ├── Servers
│   └── Queues
├── Incidents
└── Audit Log
```

## Page Contract Matrix

| Page | Route | API | Required permission | Dangerous action |
|---|---|---|---|---|
| Login/session | `/admin/login` | OIDC redirect, `/admin/me` | authenticated | logout/revoke |
| Overview | `/admin` | dashboard/summary | `dashboard.read` | none |
| Config list | `/admin/liveops` | configs list | `config.read` | archive |
| Config editor | `/admin/liveops/new`, `/admin/liveops/:id` | create/get/patch | `config.create`/`config.write` | edit draft |
| Validation | `/admin/liveops/:id/validation` | validate | `config.validate` | none |
| Diff | `/admin/liveops/:id/diff` | diff | `config.read` | none |
| Review | `/admin/liveops/:id/review` | submit/approve | `config.submit_review`/`config.approve` | approve |
| Publish | `/admin/liveops/:id/publish` | publish | `config.publish` | production activation |
| Rollback | `/admin/liveops/:id/rollback` | rollback | `config.rollback` | production rollback |
| Player search | `/admin/players` | players list | `player.read` | none |
| Player detail | `/admin/players/:id` | player detail | `player.read` | revoke sessions |
| Inventory/wallet | `/admin/players/:id/audit` | inventory/ledger | `inventory.read`/`ledger.read` | none |
| Commands | `/admin/players/:id/commands` | grant/revoke/sanction | command permission | grant/ban |
| Servers | `/admin/infrastructure/servers` | servers | `server.read` | drain/escalate |
| Queues | `/admin/infrastructure/queues` | queues | `queue.read` | disable queue |
| Incident | `/admin/incidents/:id` | incidents | `incident.read` | status change |
| Audit | `/admin/audit` | audit events | `audit.read` | none |

## Config Editor Layout

```text
┌─ Environment / Config Type / Version ───────────────────────────────┐
│ Status badge   Effective UTC window   Compatibility                  │
├─ Payload editor ───────────────┬─ Validation / references ──────────┤
│ typed fields or JSON view       │ errors, warnings, impacted systems │
├─ Change reason ─────────────────┴────────────────────────────────────┤
│ [Save Draft] [Validate] [Submit Review]                              │
└──────────────────────────────────────────────────────────────────────┘
```

## Publish and Rollback Confirmation

The confirmation screen must show:

- environment and target config;
- current active version;
- proposed version;
- diff summary;
- compatibility result;
- affected queues/servers/players;
- reason and incident reference;
- actor and required approval;
- explicit `CONFIRM` input for high-risk actions.

## State Requirements

Every page must define loading, empty, API error, stale data, 403, 404, conflict, validation failure, and retry behavior. After a successful mutation, the UI refreshes the active version and audit event rather than trusting the mutation response alone.
