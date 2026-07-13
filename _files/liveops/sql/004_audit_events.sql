-- Append-only audit event draft.
CREATE TABLE admin_audit_events (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  actor_id UUID REFERENCES admin_identities(id),
  actor_subject TEXT NOT NULL,
  actor_role TEXT,
  action TEXT NOT NULL,
  target JSONB NOT NULL,
  before_state JSONB,
  after_state JSONB,
  reason TEXT NOT NULL,
  environment TEXT NOT NULL CHECK (environment IN ('development','stage','production')),
  request_id TEXT NOT NULL,
  command_id UUID REFERENCES admin_commands(id),
  config_version_id UUID REFERENCES liveops_config_versions(id),
  occurred_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX admin_audit_events_actor_idx ON admin_audit_events(actor_subject, occurred_at DESC);
CREATE INDEX admin_audit_events_target_idx ON admin_audit_events USING GIN(target);
CREATE INDEX admin_audit_events_action_idx ON admin_audit_events(action, occurred_at DESC);

-- Application policy: no UPDATE/DELETE grants on this table; retention is archive-only.
