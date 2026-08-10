# Security Threat Model — Flow Integrity / Salesforce Governance Sentinel

## Scope

This threat model covers the public v1.3 Portfolio Preview architecture: Salesforce Flow metadata retrieval, deterministic processing, bounded AI judgment/critique, validation, routing, n8n orchestration and repository evidence.

It is a design/evidence review, not an external security audit or penetration test.

## Assets

- Salesforce OAuth credential material (must remain outside the repository).
- Flow metadata obtained through the integration identity.
- Deterministic measurement results.
- AI prompt/response payloads.
- routing and human-review decisions.
- run/evidence identifiers and generated reports.

## Trust boundaries

1. Salesforce ↔ n8n
2. n8n deterministic code ↔ model provider
3. model response ↔ deterministic validator
4. governed route ↔ human reviewer
5. runtime evidence ↔ public sanitized repository

## OWASP LLM / GenAI review lens

| Risk lens | Applicability | Control in this project | Evidence status |
|---|---|---|---|
| Prompt injection | Applicable to model-bound metadata/text | AI output is advisory; deterministic facts are calculated before AI; response must pass validation; uncertain/invalid output routes to human review | Control design documented; no dedicated public prompt-injection test ID is currently visible |
| Insecure output handling | Applicable | Second AI critique plus deterministic schema/contract validation before routing | Existing README/test evidence records critique `VALIDATED` and schema `PASSED`; adversarial breadth should not be overstated |
| Sensitive-information disclosure | Applicable | Customer-owned Flow metadata only; managed-package filtering; no business-record retrieval in stated scope; credentials excluded from repo | Documented security model; no external DLP test claimed |
| Excessive agency | Applicable | AI cannot calculate Six Sigma metrics, approve remediation, assign story points or commit work; human authority retained | Explicit architecture/control boundary |
| Governance / accountability failure | Applicable | Deterministic trace, routing contracts, executive evidence, human review | Documented design and validated run evidence |

## Threats and mitigations

### T1 — Credential disclosure

**Threat:** OAuth/client secrets are committed or embedded in workflow nodes.

**Mitigation:** credential values remain in n8n credential storage; repository publication is sanitized; CI performs an obvious-secret-pattern scan.

**Residual risk:** repository CI cannot prove a runtime credential store is configured correctly.

### T2 — Over-privileged Salesforce identity

**Threat:** compromise of the integration identity exposes broader org data.

**Mitigation:** dedicated Salesforce Integration user, API-only access, least-privilege permission set and Flow-metadata scope.

**Residual risk:** public documentation does not substitute for a live-org permission audit.

### T3 — AI changes deterministic facts

**Threat:** model output alters defect counts, DPMO, Sigma or control limits.

**Mitigation:** those values are code-owned; AI is limited to contextual judgment.

### T4 — Malformed/unsupported model output reaches action

**Threat:** invalid structure or unsupported content proceeds downstream.

**Mitigation:** critique plus deterministic contract validation; invalid or uncertain output routes to human review.

### T5 — Prompt injection through model-bound metadata

**Threat:** text embedded in metadata attempts to redirect the model.

**Mitigation:** model authority is bounded and validated; no autonomous remediation authority exists.

**Open evidence gap:** a dedicated prompt-injection test identifier is not currently published. Do not claim this threat is empirically closed until such evidence exists.

### T6 — Public evidence leaks environment identifiers

**Threat:** screenshots, JSON or reports expose secrets/customer data.

**Mitigation:** sanitized public workflow/evidence boundary and CI obvious-secret scanning.

**Residual risk:** automated patterns are not exhaustive; human release review remains necessary.

## Security conclusion

The architecture uses strong authority separation for a Portfolio Preview. The repository supports a documented least-privilege model, deterministic control boundaries and fail-closed handling of invalid AI output. It does **not** support claims of penetration testing, production hardening, complete prompt-injection coverage or external security certification.
