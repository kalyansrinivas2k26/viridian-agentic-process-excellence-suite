# Governance Registers — Flow Integrity

> This document was cited by `docs/PMP_AI_GOVERNANCE_MAPPING.md` before it existed. It restates the decision-rights table already published in `README.md`/project `README.md` in RAID-log format, plus the risk register PMI's AI standard expects. It does not introduce any new control — every row traces to a control already described elsewhere in this repository.

## Decision-rights register

| Decision | Deterministic code | AI | Human |
|---|:---:|:---:|:---:|
| Count defects/opportunities | **Authority** | No | Review |
| Calculate DPMO/Sigma/control limits | **Authority** | No | Review |
| Assess contextual impact | Guardrails | **Advisory** | Override |
| Validate response contract | **Authority** | No | Review |
| Approve remediation | No | No | **Authority** |
| Commit work to a sprint | No | No | **Authority** |

Source: `projects/01-salesforce-governance-sentinel/README.md`, verified against `Route by Severity`, `Validate Final Output Schema`, and `Human Review Queue` nodes in the workflow JSON.

## Risk register (RAID — Risks)

| ID | Risk | Likelihood | Impact | Mitigation | Residual risk owner |
|---|---|---|---|---|---|
| R-01 | AI severity judgment overstates impact | Medium | Medium | Critique pass + deterministic contract validation before routing | Human reviewer (uncertain/invalid routes to Human Review Queue) |
| R-02 | Salesforce integration identity is compromised | Low | High | OAuth 2.0 Client Credentials, dedicated API-only user, least-privilege permission set | Repository owner |
| R-03 | DPMO/Sigma figures are quoted without their defect/opportunity context | Medium | Medium | `docs/METHODOLOGY.md` and wording-rule CI check (`validate_portfolio.py`) | Documentation maintainer |
| R-04 | Portfolio Preview status is read as production readiness | Medium | High | "What this does not prove" section in every README; banned-wording CI gate | Documentation maintainer |

## Assumptions (RAID — Assumptions)

- The v1.3 validated run (7 Flows, 30 July 2026) reflects a real recorded execution against a Developer Edition / sanitized org, not a live customer tenant.
- Gemini is the model provider used in the `AI Severity Judgment` and `AI Critique` nodes at the time of the validated run; a provider change would require re-running the contract tests referenced in `docs/ADVERSARIAL_TEST_CATALOGUE.md`.

## Issues (RAID — Issues, open)

- No dedicated prompt-injection test ID is currently published (tracked in `docs/ADVERSARIAL_TEST_CATALOGUE.md`, item PI-01).
- The 60–90 second owner demo is not yet recorded.

## Dependencies (RAID — Dependencies)

- CI gate (`scripts/validate_portfolio.py`, `scripts/checksums.py`) depends on a regenerated `SHA256SUMS` after every file change.
- Executive HTML report generation depends on the `Synchronize Findings and Control Chart` merge node receiving both the routed findings and the I-MR chart output.

## Stakeholder accountability

| Role | Accountable for |
|---|---|
| Repository owner (Kalyan) | Remediation approval, sprint/backlog commitment, demo recording, CI green run |
| Deterministic code | Defect/opportunity counts, DPMO/Sigma, control limits, contract validation |
| AI (Gemini) | Bounded contextual severity judgment and critique only — no authority over the above |
