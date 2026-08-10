# Test Evidence — Flow Integrity

> This document was cited by `docs/EVIDENCE_INDEX.md`, `docs/EXECUTIVE_BRIEF.md`, and `docs/PMP_AI_GOVERNANCE_MAPPING.md` before it existed. It states what the validated v1.3 run actually recorded. It does **not** claim any item from `docs/ADVERSARIAL_TEST_CATALOGUE.md` has been executed — those remain explicitly open, per that document's own closure rule.

## Validated run — recorded result

| Measure | Result |
|---|---:|
| Run date | 30 July 2026 |
| In-scope Flows | 7 |
| Declared governance defects | 7 (missing description) |
| Declared opportunities | 21 |
| DPMO | 333,333.33 |
| Sigma level | 1.931 |
| AI critique | VALIDATED |
| Schema validation | PASSED |
| Routing result | 7 Minor, 0 Critical, 0 Human Review |
| Executive report | Generated |

Evidence sources:
- `evidence/executive-report.html` directly corroborates the run ID/date, 7 Flows, 7 defects, DPMO 333,333.33, Sigma 1.931 and 0/7/0 routing.
- `samples/validated-run-summary.json` is the structured Portfolio Preview summary.
- AI critique `VALIDATED` and schema validation `PASSED` are documented validated-result fields; they are not independently displayed by the preserved HTML report.

## What "schema validation PASSED" means here

The `Validate Final Output Schema` node checked that the AI-produced response for this run conformed to the required contract (expected fields, types, and severity enum values) before the result was allowed to reach the routing/reporting stages. A PASS means the contract held for this run's actual AI output — it does not mean every possible malformed-input scenario was tried against it.

## What "AI critique VALIDATED" means here

The second-pass `AI Critique - Gemini` node reviewed the first-pass severity judgment and did not flag it as unsupported or inconsistent for this run's data. This is one execution of the critique mechanism, not a statement about its reliability across many adversarial inputs.

## Design-level tests vs. executed tests — explicit distinction

| Test class | Status |
|---|---|
| Contract/schema validation against real AI output | **Executed** — this run |
| AI critique pass against real AI output | **Executed** — this run |
| Fail-closed routing under valid Minor classification | **Executed** — this run (7 Minor routed correctly) |
| Fail-closed routing under invalid/malformed AI output | **Not executed** — design present (`Human Review Queue` node), no negative-case run recorded |
| Prompt-injection resistance (PI-01) | **Not executed** — see `docs/ADVERSARIAL_TEST_CATALOGUE.md` |
| AI attempting to overwrite deterministic DPMO/Sigma (AI-03) | **Not executed** — architecturally prevented (AI has no write path to those nodes), but no adversarial run has attempted and recorded this |

Do not represent the "Not executed" rows above as closed. Closing them is the job of `docs/ADVERSARIAL_TEST_CATALOGUE.md`'s closure rule, not this document.
