# Security Policy

## Reporting

Do not open a public issue containing credentials, access tokens, customer metadata, Salesforce usernames, org identifiers, or production evidence. Report security concerns privately to the repository owner.

## Secrets

This repository must never contain:

- Salesforce Consumer Key or Consumer Secret
- OAuth access or refresh tokens
- Salesforce passwords or security tokens
- Gemini API keys
- n8n credential IDs tied to a live instance
- customer records or personally identifiable information

Credentials belong only in n8n's encrypted credential store or an approved secrets manager.

## Supported release

Security fixes are applied to the latest release only. The validated release is `v1.3`.

## Runtime controls

- Use one External Client App and one dedicated integration user per integration.
- Use OAuth Client Credentials for server-to-server execution.
- Keep the integration user API-only.
- Grant access through task-specific permission sets.
- Do not use a System Administrator as the Run As user.
- Rotate the Client Secret after suspected exposure.
- Revoke the External Client App or deactivate the integration user to stop access immediately.
- Restrict outbound IP addresses when the n8n hosting plan provides fixed egress.

