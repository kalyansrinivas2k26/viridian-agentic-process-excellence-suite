# Governance Registers

## Decision register

| ID | Decision | Reason | Status |
| --- | --- | --- | --- |
| D-001 | Use deterministic code for DPMO, Sigma, and control limits | Measured facts must be reproducible | Accepted |
| D-002 | Use AI only for contextual judgment | Separates probability from measurement | Accepted |
| D-003 | Require a critique pass | Reduces unreviewed model inconsistency | Accepted |
| D-004 | Route malformed output to humans | Fail-safe operation is preferable to silent failure | Accepted |
| D-005 | Exclude Cpk until specification limits exist | Prevents decorative statistics | Accepted |
| D-006 | Use a dedicated Salesforce Integration user | Least privilege and auditability | Accepted |
| D-007 | Use OAuth Client Credentials | Appropriate for server-to-server execution | Accepted |
| D-008 | Exclude namespaced Flows | Customers cannot govern managed-package metadata | Accepted |
| D-009 | Preserve human sprint and closure authority | AI must not commit delivery work | Accepted |

## Assumptions register

| ID | Assumption | Validation |
| --- | --- | --- |
| A-001 | Three governance opportunities are meaningful for the MVP | Documented and visible in methodology |
| A-002 | Flow labels and types provide limited impact context | Confidence and human oversight retained |
| A-003 | Missing descriptions count as governance defects | Confirmed MVP rule |
| A-004 | `NamespacePrefix = null` represents customer-owned metadata | Validated against returned records |
| A-005 | n8n securely encrypts configured credentials | Credential values absent from export |

## Risk register

| ID | Risk | Likelihood | Impact | Treatment |
| --- | --- | --- | --- | --- |
| R-001 | AI overstates impact from a label | Medium | Medium | Critique, confidence, human approval |
| R-002 | Secret exposure | Low | High | Encrypted credentials, secret scan, rotation |
| R-003 | Large org exceeds one REST page | Medium | Medium | Add pagination before enterprise rollout |
| R-004 | Dynamic cloud IP prevents strict allowlisting | Medium | Medium | Select fixed-egress hosting |
| R-005 | Control chart misinterpreted with few runs | High initially | Medium | Low-confidence label and observation threshold |
| R-006 | Report readers misunderstand High impact and Minor severity | Medium | Medium | Add exposure and priority columns |
| R-007 | Metadata names reveal process intent | Low | Medium | Restrict logs and report distribution |

## Open questions

| ID | Question | Owner |
| --- | --- | --- |
| Q-001 | Which fixed-egress n8n hosting option will be used? | Product owner |
| Q-002 | What retention period applies to scan history and reports? | Product/Security |
| Q-003 | Which ticket platform will receive approved stories? | Product owner |
| Q-004 | Which additional metadata types enter v1.4? | Salesforce architect |
| Q-005 | What customer-approved specification limits could support future capability analysis? | Process owner |

## Technical debt

| ID | Item | Priority | Target |
| --- | --- | --- | --- |
| TD-001 | Add REST pagination | High | Before large-org pilot |
| TD-002 | Display exposure and priority in report | Medium | v1.4 |
| TD-003 | Add fixed outbound IP restrictions | High | Before production |
| TD-004 | Replace manual trigger with governed schedule/webhook | Medium | Pilot |
| TD-005 | Add durable external evidence store | High | Commercial beta |
| TD-006 | Add automated alerting and failure dashboard | Medium | Pilot |

## Future enhancements

- Flow complexity and element-level analysis
- Apex, validation rule, permission, and object-governance modules
- Jira or Salesforce work-item integration after human approval
- Multi-org tenancy and tenant-isolated secrets
- Scheduled rescans and trend alerts
- Executive PDF rendering
- Remediation verification scan
- Benchmark library based on validated customer cohorts

## Progress log

| Date | Progress |
| --- | --- |
| 2026-07-30 | v1.3 OAuth and least-privilege architecture implemented |
| 2026-07-30 | Managed-package scope filtered |
| 2026-07-30 | End-to-end run passed |
| 2026-07-30 | Executive report and schema evidence captured |
| 2026-07-30 | Public-safe repository package prepared |

## Phase 2 roadmap

1. Add pagination, fixed egress, scheduling, and centralized logging.
2. Add metadata types beyond FlowDefinitionView.
3. Add approval persistence and ticket-system integration.
4. Add multi-tenant isolation, retention controls, and customer onboarding.
5. Validate scoring thresholds against real customer governance outcomes.

