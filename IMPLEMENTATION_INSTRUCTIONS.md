# PROJECT 1 — IMPLEMENTATION INSTRUCTIONS

## Scope

Apply this overlay to `viridian-agentic-process-excellence-suite`.

This package deliberately does **not** modify:
- the v1.3 n8n workflow JSON;
- validated calculation logic;
- historical evidence;
- existing release notes;
- existing test evidence;
- existing screenshots/reports.

## Files to replace

1. `/README.md`
2. `/projects/01-salesforce-governance-sentinel/README.md`

## Files to add

3. `/.github/workflows/portfolio-validation.yml`
4. `/scripts/validate_portfolio.py`
5. `/projects/01-salesforce-governance-sentinel/docs/EXECUTIVE_BRIEF.md`
6. `/projects/01-salesforce-governance-sentinel/docs/EVIDENCE_INDEX.md`
7. `/projects/01-salesforce-governance-sentinel/docs/QUALITY_SCORECARD.md`
8. `/projects/01-salesforce-governance-sentinel/docs/SECURITY_THREAT_MODEL.md`
9. `/projects/01-salesforce-governance-sentinel/docs/PMP_AI_GOVERNANCE_MAPPING.md`
10. `/projects/01-salesforce-governance-sentinel/docs/FINAL_SIGNOFF_GATES.md`

## Required owner actions after upload

1. Commit the files to `main`.
2. Open **Actions → Validate Flow Integrity Portfolio Preview**.
3. Confirm the latest run is green.
4. Do **not** create a new maturity claim until the green run is visible.
5. Add the real 60–90 second demo URL later. Do not insert a fake or placeholder external link.

## GitHub About description

Use:

`Governed Salesforce Flow integrity using deterministic Six Sigma measurement, bounded AI critique, schema validation and human-controlled remediation in n8n.`

## Suggested topics

`salesforce`, `n8n`, `ai-governance`, `six-sigma`, `pmp`, `agile`, `responsible-ai`, `workflow-automation`, `human-in-the-loop`, `portfolio-preview`

## Release handling

Do not rewrite or rename historical v1.3 evidence. If you publish a GitHub release for the documentation/CI remediation, use a new release identifier that clearly separates the engineering version from the portfolio packaging, for example:

`flow-integrity-v1.3-portfolio-preview.1`

Only publish it **after** CI is green.

## Final freeze condition

Project 1 can be marked `PASS — FREEZE` only after the public CI run is green and the final sign-off document is updated with that evidence. The demo remains required by the current Executive Documentation Standard unless that standard is intentionally amended.


## Checksum closure — mandatory

Because this remediation changes tracked files, the existing root `SHA256SUMS` must be regenerated **after all files are in their final locations**.

From a local checkout of the updated repository run:

```bash
python scripts/checksums.py --write
python scripts/checksums.py --check
python scripts/validate_portfolio.py
```

Commit the regenerated `SHA256SUMS` with the remediation.

GitHub Actions is deliberately configured to fail if the checksum ledger is stale. Do not weaken this gate merely to make CI green.

## Files additionally added/replaced by the final package

- `/SECURITY.md`
- `/CHANGELOG.md`
- `/docs/PORTFOLIO_ROADMAP.md`
- `/docs/EXECUTIVE_DOCUMENTATION_STANDARD.md`
- `/scripts/checksums.py`


## Additional evidence-backed documentation in v3

Also add:
- `projects/01-salesforce-governance-sentinel/docs/COMPETITIVE_POSITIONING.md`
- `projects/01-salesforce-governance-sentinel/docs/AGILE_TRACEABILITY.md`
- `projects/01-salesforce-governance-sentinel/docs/ADVERSARIAL_TEST_CATALOGUE.md`
- `projects/01-salesforce-governance-sentinel/docs/GAP_CLOSURE_MATRIX.md`

The internal scorecard is raised from 91/100 to **93/100** only because two evidence-backed documentation gaps were closed:
- competitive positioning: 7/8 → 8/8;
- Agile evidence: 5/6 → 6/6.

No points were added for unexecuted adversarial tests, the missing demo, production evidence, or external review.
