# Deployment — Flow Integrity / Salesforce Governance Sentinel

> This document was cited by `README.md` ("Import and configure") and `docs/EVIDENCE_INDEX.md` before it existed. It states the intended deployment/configuration controls already described in `SECURITY.md` and the project README's "Security boundary" section, in step form. It is a configuration guide, not a claim that this exact sequence has been executed against a specific external environment.

## Prerequisites

- A Salesforce org (sandbox or Developer Edition) with a dedicated **API-only integration user**.
- n8n (cloud or self-hosted) with the ability to store OAuth 2.0 Client Credentials securely in n8n's credential store — never in the workflow JSON itself.
- A model-provider API key (Gemini, at the time of the validated run) stored the same way.

## Salesforce-side setup

1. Create a Connected App configured for **OAuth 2.0 Client Credentials Flow**.
2. Create a dedicated integration user, distinct from any human administrator account.
3. Assign a **least-privilege permission set** scoped to read access on Flow metadata only — no broader object or record access.
4. Confirm managed-package metadata is excluded by filtering on `NamespacePrefix = null` in the retrieval query (matches the `Get Flows - REST API` node's intended scope).

## n8n-side setup

1. Import `workflows/Salesforce-Governance-Sentinel-v1.3-public.json`.
2. Configure the Salesforce HTTP Request nodes (`Test Salesforce Connection`, `Get Flows - REST API`) with the OAuth 2.0 credential created above — stored in n8n's credential manager, never pasted into node parameters.
3. Configure the Gemini HTTP Request nodes (`AI Severity Judgment - Gemini`, `AI Critique - Gemini`) with the model-provider API key, also via n8n's credential manager.
4. Confirm the n8n Data Table used by `Insert row` / `Get Scan History` exists and is reachable — this is what feeds the I-MR control chart across runs.

## Before publishing any evidence externally

- Sanitize any exported JSON, screenshot, or HTML report for org identifiers, real Flow names, and any value that could identify a live customer environment.
- Run `scripts/validate_portfolio.py`'s secret-pattern scan locally before committing.

## What this document does not establish

- It does not certify that this exact sequence was followed for the validated v1.3 run — it states the intended, documented configuration.
- It does not replace a live-org permission audit.
- It is not a substitute for Salesforce's own Connected App / OAuth documentation for environment-specific edge cases.
