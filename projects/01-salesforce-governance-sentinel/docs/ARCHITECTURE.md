# Architecture — Flow Integrity / Salesforce Governance Sentinel

> This document was missing from the previous remediation package even though five other files cited it as evidence. It is written directly from the node structure in `workflows/Salesforce-Governance-Sentinel-v1.3-public.json`, not from a redesigned or reimagined architecture. No node, connection, or calculation described below differs from the validated v1.3 workflow.

## Purpose

Show how the workflow physically separates deterministic measurement, bounded AI judgment, contract validation, and human-controlled routing — the same separation claimed in the README's decision-rights table — so a Salesforce architect or engineering reviewer can verify the claim against the real node graph instead of taking it on faith.

## Pipeline, in execution order

| Stage | Representative node(s) in the workflow JSON | Authority |
|---|---|---|
| Trigger | `When clicking 'Execute workflow'` | Manual/owner |
| Connect | `Test Salesforce Connection` | Deterministic |
| Retrieve | `Get Flows - REST API` | Deterministic (Salesforce REST, OAuth Client Credentials) |
| Test fixture path | `Synthetic Test Fixture - Flows` | Deterministic, isolated from the live retrieval path |
| Measurement | `Calculate DPMO - Flows`, `Calculate DPMO - Synthetic (Test)` | **Code-owned.** AI has no node in this path. |
| Control chart | `Calculate Control Chart - I-MR` | Deterministic |
| History | `Insert row`, `Get Scan History` (n8n Data Table) | Deterministic |
| AI judgment | `Build Gemini Prompt` → `AI Severity Judgment - Gemini` | **Bounded AI.** Prompt is code-constructed; output is not yet trusted. |
| Critique | `Build Critique Prompt` → `AI Critique - Gemini` → `Merge Critique Results` | Second-pass AI check on the first AI output — this is the "critique" referenced elsewhere in the docs, and it is a real second model call, not a documentation claim |
| Routing | `Route by Severity` (switch node) | Deterministic logic consumes the (critiqued) AI severity to route Critical vs. Minor |
| Story drafting | `Generate Story - Critical`, `Generate Story - Minor` | Draft text only — see `AGILE_TRACEABILITY.md` for why this never becomes a sprint commitment |
| Consolidation | `Generate Issue Log`, `Merge AI Judgment into Issue Log`, `Split Issue Entries`, `Initialize Run Context` | Deterministic |
| Contract validation | `Validate Final Output Schema` | **This is the deterministic gate** that catches malformed/incomplete AI output before anything downstream trusts it |
| Fail-closed path | `Human Review Queue` | Reached when validation fails or output is uncertain — not an optional branch, it's wired into the graph |
| Synchronization | `Synchronize Findings and Control Chart` (merge node) | Deterministic |
| Reporting | `Build Executive HTML Report` → `Create Downloadable HTML File` | Deterministic templating over validated data |

## Why this satisfies "deterministic before AI"

Two separate DPMO-calculation nodes exist (`Calculate DPMO - Flows` and the synthetic-test variant), and neither sits downstream of an AI node. The AI nodes (`AI Severity Judgment - Gemini`, `AI Critique - Gemini`) only ever feed into `Route by Severity` and `Validate Final Output Schema` — both deterministic consumers, not producers, of the numbers that matter for Six Sigma reporting.

## What this document does not claim

- It does not claim the workflow has been executed at production scale.
- It does not claim the AI critique node catches every possible malformed response — see `docs/ADVERSARIAL_TEST_CATALOGUE.md` for what remains unexecuted.
- It is a structural description of the real workflow, not a substitute for `docs/DEPLOYMENT.md` (runtime configuration) or `docs/TEST_EVIDENCE.md` (what was actually validated in the recorded run).
