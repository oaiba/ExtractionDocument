-- Idempotent, auditable operator command draft.
CREATE TABLE admin_commands (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  command_type TEXT NOT NULL,
  target_type TEXT NOT NULL,
  target_id TEXT NOT NULL,
  environment TEXT NOT NULL CHECK (environment IN ('development','stage','production')),
  request_hash BYTEA NOT NULL,
  idempotency_key TEXT NOT NULL,
  actor_id UUID NOT NULL REFERENCES admin_identities(id),
  reason TEXT NOT NULL CHECK (char_length(reason) >= 3),
  status TEXT NOT NULL CHECK (status IN ('accepted','running','succeeded','failed','duplicate')),
  result JSONB,
  failure_code TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  completed_at TIMESTAMPTZ,
  UNIQUE (environment, command_type, idempotency_key)
);

CREATE TABLE admin_command_results (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  command_id UUID NOT NULL REFERENCES admin_commands(id),
  response_code INTEGER NOT NULL,
  response_body JSONB NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (command_id)
);

CREATE INDEX admin_commands_target_idx ON admin_commands(target_type, target_id, created_at DESC);
CREATE INDEX admin_commands_actor_idx ON admin_commands(actor_id, created_at DESC);
