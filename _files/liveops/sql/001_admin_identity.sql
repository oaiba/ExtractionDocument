-- LiveOps Admin identity, role, permission, and environment binding draft.
-- Apply through the project's immutable migration runner after review.
CREATE TABLE admin_identities (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  oidc_subject TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL,
  display_name TEXT,
  status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active','disabled')),
  last_login_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE admin_roles (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL UNIQUE,
  description TEXT NOT NULL DEFAULT '',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE admin_permissions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL UNIQUE,
  description TEXT NOT NULL DEFAULT '',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE admin_role_bindings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  admin_identity_id UUID NOT NULL REFERENCES admin_identities(id),
  role_id UUID NOT NULL REFERENCES admin_roles(id),
  environment TEXT NOT NULL CHECK (environment IN ('development','stage','production')),
  granted_by UUID REFERENCES admin_identities(id),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (admin_identity_id, role_id, environment)
);

CREATE TABLE admin_role_permissions (
  role_id UUID NOT NULL REFERENCES admin_roles(id) ON DELETE CASCADE,
  permission_id UUID NOT NULL REFERENCES admin_permissions(id) ON DELETE CASCADE,
  PRIMARY KEY (role_id, permission_id)
);

CREATE INDEX admin_role_bindings_lookup_idx ON admin_role_bindings(admin_identity_id, environment);
