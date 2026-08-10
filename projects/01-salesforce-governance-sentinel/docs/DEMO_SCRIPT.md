# 60–90 Second Demo Script — Flow Integrity

> Recording status: **PENDING OWNER RECORDING**.  
> This script is a presentation aid only; it is not execution evidence.

## 0–10 seconds — Problem and control boundary

Open the Project README.

Say:

“Flow Integrity converts Salesforce Flow metadata into deterministic governance measurements, bounded AI judgment and human-controlled remediation. AI does not own the measured facts.”

## 10–25 seconds — Source and deterministic measurement

Open the public workflow JSON and point to the Salesforce metadata query and deterministic calculation nodes.

Show that:
- only customer-owned Flow metadata is in scope;
- defect/opportunity counts are code-owned;
- DPMO and Sigma are calculated deterministically.

## 25–40 seconds — AI is bounded, not authoritative

Show the AI assessment, critique and deterministic validation stages.

Say:

“The model assesses context and confidence, but its response is challenged and validated before routing. Invalid or uncertain output is sent to human review.”

## 40–55 seconds — Real preserved run evidence

Open `evidence/executive-report.html`.

Show:
- Run ID `VGS-20260730062123-IKKOFEN8`;
- 7 in-scope Flows;
- 7 governance defects;
- DPMO `333,333.33`;
- Sigma `1.931`;
- 0 Critical / 7 Minor / 0 Human Review.

State the boundary:

“These are governance defect-density indicators for the declared opportunity model, not Cpk or production process capability.”

## 55–70 seconds — Failure-safe governance

Return to the architecture diagram or workflow routing.

Show the Critical, Minor and Review Required paths.

Say:

“Measured facts stay deterministic; AI remains advisory; uncertain or invalid output cannot silently become an autonomous action.”

## 70–90 seconds — Credibility close

Open:
- `docs/EVIDENCE_INDEX.md`;
- `docs/QUALITY_SCORECARD.md`;
- `docs/SECURITY_THREAT_MODEL.md`.

Say:

“The repository publishes the evidence, the limitations and the unearned points. The Portfolio Preview is intentionally not presented as production readiness or external certification.”

## Recording rule

When the real demo is recorded:
1. use the actual repository and actual preserved evidence;
2. do not simulate a green CI run;
3. do not claim adversarial cases as executed unless their evidence exists;
4. place the final link in the root README and Project README.
