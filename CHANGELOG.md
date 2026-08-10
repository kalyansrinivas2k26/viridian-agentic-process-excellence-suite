# Changelog

All notable portfolio-packaging changes to this repository are recorded here.

Historical Flow Integrity v1.3 engineering evidence remains governed by the existing project release notes and is not rewritten by this changelog.

## Unreleased — Documentation-traceability correction round (v2)

Follows an independent adversarial review of the v1 remediation package below. That review found nine evidence citations across `EVIDENCE_INDEX.md`, `EXECUTIVE_BRIEF.md`, and `PMP_AI_GOVERNANCE_MAPPING.md` pointed to files that did not exist, and that `scripts/validate_portfolio.py`'s required-file list did not check for them — meaning a green CI run would not have guaranteed the documentation's own evidence citations resolved.

### Added
- `docs/ARCHITECTURE.md` — written directly from the 26-node structure of `workflows/Salesforce-Governance-Sentinel-v1.3-public.json`, not from a redesigned architecture.
- `docs/METHODOLOGY.md` — consolidates the Six Sigma interpretation boundary previously stated only inline in `README.md`.
- `docs/TEST_EVIDENCE.md` — states what the validated run actually recorded, with an explicit executed-vs-design-only split; does not mark any `ADVERSARIAL_TEST_CATALOGUE.md` item as executed.
- `docs/DEPLOYMENT.md` — restates the existing Security boundary section as configuration steps.
- `docs/GOVERNANCE_REGISTERS.md` — restates the existing decision-rights table in RAID-log format for the PMP mapping to cite.
- `docs/RELEASE_NOTES.md` — includes an explicit, unresolved lineage question against the supplied `VANTIX-Flow-Integrity-v1.4.0-Final-Audit-Closure.md`, which describes a different (Node.js/npm, signed-ZIP) release mechanism not reflected in this package or the live repository at review time. Not resolved by assumption — flagged for owner confirmation.
- `PROJECT_STATUS.md` — single-page status rollup of `FINAL_SIGNOFF_GATES.md`.
- `samples/validated-run-summary.json` — structures the run figures already stated repeatedly across existing documents; flagged internally for owner verification against raw run output before being treated as authoritative.
- `projects/01-salesforce-governance-sentinel/SECURITY.md` — restates the existing Security boundary section as its own file, matching what root `SECURITY.md` already pointed to.
- `projects/01-salesforce-governance-sentinel/workflows/Salesforce-Governance-Sentinel-v1.3-public.json` — the actual supplied source workflow file, not previously included in the overlay package.
- Extended `scripts/validate_portfolio.py`'s required-artifact list to include the eight new documentation files above, and added a non-blocking warning check for `evidence/workflow-success.png` and `evidence/executive-report.html`.

### Explicitly not added
- `evidence/workflow-success.png`, `evidence/executive-report.html` — these must be a real screenshot and real generated report from an actual n8n execution. They are not created here because doing so would be fabricated evidence. `scripts/validate_portfolio.py` now warns (non-blocking) if they're absent so the gap stays visible instead of silently passing.

### Changed
- `docs/QUALITY_SCORECARD.md` — total corrected from 93 to 89. This is **not** new work being penalized; it's a correction of two dimensions (documentation/traceability, competitive-positioning) that were scored as if the citations they depended on already resolved. See that file's "Score history" section for the itemized reasoning.
- `docs/GAP_CLOSURE_MATRIX.md`, `docs/EVIDENCE_INDEX.md` — updated to reflect the new files and to mark the two owner-only evidence files and the v1.4.0 lineage question as explicitly open rather than silently assumed closed.

## Unreleased — Portfolio Preview repository-assurance remediation (v1)

### Added
- Root Portfolio Preview maturity boundary and current portfolio navigation.
- Executive Documentation Standard.
- Executive brief and evidence index for Flow Integrity.
- Internal 100-point quality scorecard using the canonical portfolio rubric.
- OWASP LLM/GenAI-aligned security threat model.
- PMP / PMI AI governance mapping.
- Final sign-off gates.
- Evidence-safe competitive-positioning source register.
- Agile evidence-to-human-authority traceability.
- Adversarial evidence-closure catalogue with non-executed states explicitly labeled.
- Documentation/evidence gap-closure matrix.
- Root security policy.
- Deterministic GitHub Actions repository-validation gate.
- Deterministic checksum-ledger generator/checker.

### Changed
- Removed obsolete root-roadmap presentation that treated old PMP Risk Radar and Scrum Velocity Intelligence Agent concepts as the active Projects 2 and 3.
- Reframed Project 1 as `Portfolio Preview — validated v1.3 evidence package` without changing the v1.3 engineering evidence.
- Strengthened README limitations, evidence traceability and recruiter-facing decision structure.

### Not changed
- n8n workflow architecture.
- deterministic measurement logic.
- validated v1.3 run results.
- historical project release notes.
- screenshots or executive run evidence.
- Salesforce/n8n runtime configuration.

### Release condition
Do not publish the remediation as a closed release until:
1. the final checksum ledger is regenerated;
2. GitHub Actions is green;
3. the sign-off gate records that evidence.


## Unreleased — final evidence-integrity hardening

- Added preserved real `evidence/executive-report.html` and evidence provenance.
- Added `docs/RELEASE_LINEAGE.md`.
- Added internal Markdown-link validation to CI.
- Corrected Audience Guide persona count and root Security link.
- Expanded competitive review to include Copado.
- Corrected the internal scorecard arithmetic and remaining-points explanation; current evidence-backed score is 92/100.
- Kept `workflow-success.png` optional/pending rather than fabricating it.


## Unreleased — merge-ready preservation closure

- Restored root `.gitignore` to the merge-ready package.
- Restored root and project-level MIT `LICENSE` files.
- Added `docs/DEMO_SCRIPT.md` so the existing demo-documentation slot is preserved.
- CI required-artifact checks now include these files.
- SHA-256 ledger regenerated after the final file set.


## Final v5 presentation cleanup

- Archived the historical v4 handoff note under `docs/history/` and added one canonical `FINAL_HANDOFF.md`.
- Corrected mojibake punctuation in the public workflow comments/warnings and executive HTML presentation only; no control logic or evidence values changed.
