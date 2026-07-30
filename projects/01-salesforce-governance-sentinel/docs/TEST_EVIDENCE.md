# Test Evidence

## Validated production-style run

| Field | Result |
| --- | --- |
| Date | 2026-07-30 |
| Run ID | `VGS-20260730082713-4RYZ4BR5` |
| Workflow | Salesforce Governance Sentinel v1.3 – Secure Governed Agentic |
| Connected nodes | All green |
| In-scope records | 7 |
| Managed-package records | Excluded |
| AI judgment | Valid JSON |
| Critique | VALIDATED |
| Final schema | PASSED |
| Critical | 0 |
| Minor | 7 |
| Human Review | 0 |
| Report | Generated |

## Security tests

| Test | Result |
| --- | --- |
| API-only user blocked from Salesforce UI | Passed |
| OAuth Client Credentials token obtained | Passed |
| `/limits` endpoint called as integration identity | Passed |
| FlowDefinitionView query permitted | Passed |
| Managed-package records excluded | Passed |
| Runtime no longer uses administrator credential | Passed |
| Export secret scan | Passed |

## Routing tests

### Synthetic Critical

- Priority: Immediate Escalation
- Human approval required
- Story points not auto-assigned
- Sprint placement remains a human decision
- Result: Passed

### Synthetic Minor

- Priority: Backlog – No Immediate Urgency
- Human backlog review required
- Effort remains team-estimated
- Result: Passed

### Invalid AI response

- Malformed JSON did not terminate the workflow.
- Findings were marked unassigned.
- All entries routed to Review Required.
- Result: Passed

### Invalid critique response

- Malformed critique did not terminate the workflow.
- Self-critique status recorded the parsing failure.
- Final schema remained deterministic.
- Result: Passed

## Calculation check

```text
Flows = 7
Opportunities per Flow = 3
Total opportunities = 21
Defects = 7
DPMO = 7 / 21 × 1,000,000 = 333,333.33
Sigma = 1.931
```

## Evidence files

- `evidence/executive-report.html`
- `evidence/workflow-success.png`

## Known presentation observation

The report does not currently display exposure and priority score columns. This can make High impact and Minor routing look inconsistent without the scoring explanation. The underlying output contains the values and the routing result is valid.

