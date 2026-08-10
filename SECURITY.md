# Security Policy

## Portfolio boundary

This public repository contains sanitized Portfolio Preview artifacts. Do not commit passwords, API keys, OAuth secrets, access tokens, customer records, live credential identifiers or unsanitized environment details.

## Project-specific control model

Flow Integrity's detailed security boundary is documented at:

`projects/01-salesforce-governance-sentinel/SECURITY.md`

and its AI/security review is at:

`projects/01-salesforce-governance-sentinel/docs/SECURITY_THREAT_MODEL.md`

## Reporting a vulnerability

Do not place secret material or exploit details in a public issue. Use GitHub's private vulnerability-reporting channel when enabled, or contact the repository owner privately.

Include:
- affected file/version;
- reproducible condition;
- impact;
- whether any credential or customer data may have been exposed.

## Supported portfolio version

The current public evidence boundary is the latest `main` revision plus any explicitly published Portfolio Preview release.

Historical artifacts are preserved for traceability; a historical artifact is not automatically a supported production version.

## No certification claim

Repository security controls and CI checks are portfolio evidence only. They are not a penetration test, external security audit, certification or guarantee of production security.
