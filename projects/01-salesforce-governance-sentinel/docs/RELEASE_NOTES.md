# Release Notes

## v1.3 — Secure Governed Agentic

Released: 30 July 2026

### Added

- Dedicated Salesforce API-only runtime identity
- Salesforce OAuth Client Credentials authentication
- Least-privilege setup-metadata permission set
- Admin-preapproved External Client App policy
- Customer-owned Flow filter using `NamespacePrefix = null`
- Validated end-to-end execution evidence
- Credential-safe public workflow export

### Validated

- AI judgment and critique returned valid structured output
- Deterministic final schema passed
- Seven findings routed to Minor
- Executive report generated
- No secrets present in the exported workflow

### Security correction

The External Client App previously ran as a System Administrator. v1.3 changes the Run As identity to the dedicated Vantix Governance Scanner integration user.

### Known limitations

- Manual trigger only
- One-page REST query; pagination not implemented
- n8n Data Table is local to the importing instance
- Report does not show exposure and priority score columns
- Early control limits are statistically low-confidence
- Fixed outbound IP restriction is pending hosting selection

## v1.2 — Governed Agentic

- Added critique-response validation
- Added safe fallback for malformed AI responses
- Added deterministic schema validation
- Added Critical, Minor, and Human Review routing
- Added governed story generation
- Added run correlation ID
- Added I-MR history and executive HTML report

