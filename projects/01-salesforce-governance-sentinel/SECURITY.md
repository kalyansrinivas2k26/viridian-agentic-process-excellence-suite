# Security — Flow Integrity / Salesforce Governance Sentinel

> Required by `scripts/validate_portfolio.py` and referenced by root `SECURITY.md`, but did not exist in the prior remediation package. Content below restates the "Security boundary" section already published in `README.md` as a dedicated file — no new control is introduced here.

## Boundary

- OAuth 2.0 Client Credentials.
- Dedicated Salesforce Integration user, distinct from any human administrator account.
- API-only access and a least-privilege permission set.
- Customer-owned Flow metadata only.
- Managed-package metadata excluded by `NamespacePrefix = null`.
- No business-record retrieval is part of the stated workflow scope.
- Repository credentials are prohibited — see `scripts/validate_portfolio.py`'s secret-pattern scan.
- AI output (Gemini severity judgment and critique) is advisory and contract-validated before routing; it has no write path to defect counts, DPMO, Sigma, or control limits.

## Deployment configuration

See `docs/DEPLOYMENT.md` for the step-by-step setup of the above.

## Threat model

See `docs/SECURITY_THREAT_MODEL.md` for the full OWASP LLM/GenAI-aligned review, including open evidence gaps (dedicated prompt-injection test IDs are not yet published).

## Reporting a vulnerability

Follow the process in the root `SECURITY.md`. Do not place secret material or exploit details in a public GitHub issue.

## No certification claim

This file and the linked threat model are portfolio evidence only. They are not a penetration test, external security audit, or certification.
