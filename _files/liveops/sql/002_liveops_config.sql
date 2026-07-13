-- Immutable LiveOps configuration and review/publication draft.
CREATE TABLE liveops_configs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  config_id TEXT NOT NULL,
  config_type TEXT NOT NULL,
  environment TEXT NOT NULL CHECK (environment IN ('development','stage','production')),
  active_version BIGINT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (config_id, environment)
);

CREATE TABLE liveops_config_versions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  config_id UUID NOT NULL REFERENCES liveops_configs(id),
  version BIGINT NOT NULL CHECK (version > 0),
  schema_version BIGINT NOT NULL CHECK (schema_version > 0),
  status TEXT NOT NULL CHECK (status IN ('draft','validated','in_review','approved','scheduled','published','active','rolled_back','archived','rejected','expired')),
  payload JSONB NOT NULL,
  checksum TEXT NOT NULL,
  effective_from TIMESTAMPTZ NOT NULL,
  effective_to TIMESTAMPTZ,
  created_by UUID NOT NULL REFERENCES admin_identities(id),
  published_by UUID REFERENCES admin_identities(id),
  reason TEXT NOT NULL CHECK (char_length(reason) >= 3),
  rollback_of UUID REFERENCES liveops_config_versions(id),
  client_build_constraints JSONB NOT NULL DEFAULT '[]'::jsonb,
  server_build_constraints JSONB NOT NULL DEFAULT '[]'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  published_at TIMESTAMPTZ,
  UNIQUE (config_id, version),
  CHECK (effective_to IS NULL OR effective_to > effective_from)
);

CREATE UNIQUE INDEX liveops_one_active_idx ON liveops_config_versions(config_id) WHERE status = 'active';
CREATE INDEX liveops_versions_status_idx ON liveops_config_versions(status, effective_from);

CREATE TABLE liveops_config_reviews (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  version_id UUID NOT NULL REFERENCES liveops_config_versions(id),
  status TEXT NOT NULL CHECK (status IN ('in_review','approved','rejected')),
  reviewer_id UUID NOT NULL REFERENCES admin_identities(id),
  reason TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE liveops_config_publications (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  version_id UUID NOT NULL REFERENCES liveops_config_versions(id),
  published_by UUID NOT NULL REFERENCES admin_identities(id),
  published_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  request_id TEXT NOT NULL,
  UNIQUE (version_id)
);

CREATE TABLE liveops_config_targets (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  version_id UUID NOT NULL REFERENCES liveops_config_versions(id) ON DELETE CASCADE,
  target_type TEXT NOT NULL CHECK (target_type IN ('client','server','region','build')),
  target_value TEXT NOT NULL,
  priority INTEGER NOT NULL DEFAULT 0,
  UNIQUE (version_id, target_type, target_value)
);
