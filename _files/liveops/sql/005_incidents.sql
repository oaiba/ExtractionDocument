CREATE TABLE incidents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title TEXT NOT NULL,
  severity TEXT NOT NULL CHECK (severity IN ('sev1','sev2','sev3','sev4')),
  status TEXT NOT NULL CHECK (status IN ('open','mitigating','monitoring','resolved','closed')),
  environment TEXT NOT NULL CHECK (environment IN ('development','stage','production')),
  owner_subject TEXT NOT NULL,
  started_at TIMESTAMPTZ NOT NULL,
  resolved_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  CHECK (resolved_at IS NULL OR resolved_at >= started_at)
);

CREATE TABLE incident_updates (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  incident_id UUID NOT NULL REFERENCES incidents(id) ON DELETE CASCADE,
  author_subject TEXT NOT NULL,
  message TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX incidents_status_idx ON incidents(status, severity, started_at DESC);
CREATE INDEX incident_updates_incident_idx ON incident_updates(incident_id, created_at DESC);
