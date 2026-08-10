# Evidence Index — Flow Integrity / Salesforce Governance Sentinel

> Evidence scope: public/sanitized v1.3 Portfolio Preview. This index is a navigation layer, not new evidence.

| Evidence question | Artifact | What it supports | What it does not support |
|---|---|---|---|
| What workflow is being reviewed? | `workflows/Salesforce-Governance-Sentinel-v1.3-public.json` | Public workflow structure | Live credentials or production operation |
| Was a run recorded? | `evidence/executive-report.html` + `evidence/README.md` | Preserved real run output with run ID/date and visible metrics/routing | Repeated production reliability or every intermediate validation state |
| What did the executive output look like? | `evidence/executive-report.html` | Actual preserved HTML report from run `VGS-20260730062123-IKKOFEN8` | Production SLA or customer outcome |
| How does this reconcile with the v1.4.0 audit artifact? | `docs/RELEASE_LINEAGE.md` | v1.3 as the current public baseline; v1.4.0 preserved as historical, not silently merged | That v1.4.0 is currently published on GitHub |
| What was the summarized validated result? | `samples/validated-run-summary.json` | Recorded metrics, validation and routing summary — structured from figures already stated in README.md/EXECUTIVE_BRIEF.md; owner should verify against raw run output | Broader statistical generalization |
| How were tests described? | `docs/TEST_EVIDENCE.md` | Existing validation evidence | Tests not listed there |
| How are DPMO/Sigma interpreted? | `docs/METHODOLOGY.md` | Declared defect/opportunity model and interpretation | Cpk/process capability |
| What is the architecture? | `docs/ARCHITECTURE.md` | Separation of measurement, AI, validation and human control | Production deployment topology |
| How is the integration secured? | `SECURITY.md`, `docs/DEPLOYMENT.md` | Intended OAuth/least-privilege controls | External penetration testing |
| What release is preserved? | `docs/RELEASE_NOTES.md`, `PROJECT_STATUS.md` | v1.3 evidence boundary | A GitHub Release unless separately published |
| What does this remediation add? | `.github/workflows/portfolio-validation.yml`, `scripts/validate_portfolio.py` | Repository-level CI gate | Re-execution of Salesforce/n8n workflow |

## Evidence classification

- **Verified in repository:** directly represented by a named artifact.
- **Partially verified:** design/documentation exists but operational breadth is not proven.
- **Not verified:** no public artifact supports the claim.
- **Not applicable:** the claim is outside the Portfolio Preview boundary.

## Explicit non-evidence

The following must not be treated as evidence unless a dedicated artifact is later added:

- recruiter opinions;
- external certification;
- practitioner review;
- production-scale results;
- real-customer business outcomes;
- competitor superiority;
- production SLO attainment.
