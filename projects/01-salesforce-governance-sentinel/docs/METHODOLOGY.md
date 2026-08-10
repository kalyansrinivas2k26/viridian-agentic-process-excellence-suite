# Methodology — Six Sigma Interpretation Boundary

> This document consolidates the interpretation boundary that was previously stated only inline in `README.md`. No figure, definition, or boundary here differs from what the README already asserts — this file exists so `docs/EVIDENCE_INDEX.md` and `docs/PMP_AI_GOVERNANCE_MAPPING.md` can cite a real, dedicated methodology artifact instead of a broken link.

## Unit

One in-scope Salesforce Flow.

## Declared defect

A governance condition counted by the v1.3 deterministic rule set. The validated run records **missing Flow description** as the declared defect type.

## Opportunity denominator

Three declared governance opportunities per in-scope Flow in the validated dataset. Seven Flows × three opportunities = **21 total opportunities**.

## Input dataset

The sanitized/controlled v1.3 validated run, summarized in `samples/validated-run-summary.json` and further described in `docs/TEST_EVIDENCE.md`.

## Calculation

```
DPMO = (Defects / (Units × Opportunities per unit)) × 1,000,000
     = (7 / (7 × 3)) × 1,000,000
     = (7 / 21) × 1,000,000
     = 333,333.33
```

Sigma level (long-term, 1.5σ shift convention) corresponding to this DPMO: **1.931**.

## Cpk — explicitly not reported

Cpk requires customer specification limits (upper/lower spec limits against a continuous measured characteristic). This project's declared-defect model is attribute (pass/fail per opportunity), and no customer specification limits have been established for it. Reporting a Cpk here would be a fabricated capability claim. This exclusion is intentional and should remain intentional in every future revision of this project.

## What DPMO/Sigma do and do not establish

**They establish:** a repeatable, deterministic way to convert a declared governance-defect count into a standard Six Sigma quality signal for this specific dataset and rule set.

**They do not establish:**
- process capability in the classical Six Sigma sense (that requires Cpk, which is intentionally not claimed);
- generalization beyond the seven in-scope Flows in the validated run;
- anything about production-scale Salesforce orgs not included in this dataset.

## I-MR control chart

The `Calculate Control Chart - I-MR` node in the workflow produces an Individuals–Moving Range chart across scan history (via the n8n Data Table `Get Scan History` node). With a single validated run recorded to date, the chart has one data point — it is structurally present and correctly wired, but statistically uninformative until multiple runs accumulate. Do not present a single-point I-MR chart as evidence of process stability.
