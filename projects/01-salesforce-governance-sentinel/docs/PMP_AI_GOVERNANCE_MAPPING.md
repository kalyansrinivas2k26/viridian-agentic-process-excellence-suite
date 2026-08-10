# PMP / PMI AI Governance Mapping — Flow Integrity

> Purpose: map project controls to the portfolio's June 2026 PMI AI-standard review areas. This is a portfolio governance mapping, not a PMI certification or endorsement.

| PMI AI review area | Project control | Artifact |
|---|---|---|
| Value and benefits | Governance findings are converted into measurable, reviewable remediation evidence rather than unstructured metadata observations | `README.md`, `docs/EXECUTIVE_BRIEF.md` |
| Governance | Deterministic measurements, response contracts, governed routing and recorded evidence | `docs/ARCHITECTURE.md`, `docs/GOVERNANCE_REGISTERS.md` |
| Stakeholder accountability | Human retains remediation approval and sprint-commitment authority | `README.md`, `docs/GOVERNANCE_REGISTERS.md` |
| Risk | Governance findings and assumptions/issues are captured in the existing governance registers; security threats are explicitly bounded | `docs/GOVERNANCE_REGISTERS.md`, `docs/SECURITY_THREAT_MODEL.md` |
| Human oversight | Invalid/uncertain AI output routes to human review; AI cannot approve remediation | `README.md`, workflow JSON |
| Adaptive / predictive delivery fit | Draft Agile remediation stories may be produced, but AI does not assign story points or commit work | `README.md`, `docs/METHODOLOGY.md` |
| Decision authority | Code owns measured facts; AI is advisory; human owns approval | `README.md`, `docs/ARCHITECTURE.md` |
| Transparency | Validated run metrics, limitations and evidence artifacts are published | `docs/EXECUTIVE_BRIEF.md`, `docs/EVIDENCE_INDEX.md`, `docs/TEST_EVIDENCE.md` |
| Responsible AI | Bounded agency, output validation, critique and explicit non-production claims | `docs/SECURITY_THREAT_MODEL.md`, `docs/FINAL_SIGNOFF_GATES.md` |

## Governance interpretation

This mapping demonstrates that the repository has intentionally connected delivery governance to named project controls. It does not claim formal conformance assessment by PMI.
