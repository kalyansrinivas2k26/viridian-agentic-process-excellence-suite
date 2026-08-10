# Corrections Applied Following Independent Adversarial Review

This note is for whichever LLM produced the v1 remediation package (`README.md`, the `docs/` set, `scripts/validate_portfolio.py`, etc.) prior to this round. An independent adversarial review (run to the spec in `00_INDEPENDENT_REVIEW_PROMPT.md`) found real, evidence-based defects. This file lists exactly what was found, what was changed, why, and what remains genuinely open — so you can verify the corrections and decide what else should be done.

## What was found

1. **Nine evidence citations pointed to files that did not exist**: `docs/ARCHITECTURE.md`, `docs/METHODOLOGY.md`, `docs/TEST_EVIDENCE.md`, `docs/RELEASE_NOTES.md`, `docs/DEPLOYMENT.md`, `docs/GOVERNANCE_REGISTERS.md`, `PROJECT_STATUS.md`, `samples/validated-run-summary.json`, and the project-level `SECURITY.md`. `README.md`, `docs/EVIDENCE_INDEX.md`, `docs/EXECUTIVE_BRIEF.md`, and `docs/PMP_AI_GOVERNANCE_MAPPING.md` all cited one or more of these.
2. **`scripts/validate_portfolio.py`'s required-file list didn't check for most of them**, so a green CI run would not have caught the broken citations — the CI gate and the documentation's own evidence claims were out of sync.
3. **A false positive in the same script**: the banned-wording scan flagged `docs/EXECUTIVE_DOCUMENTATION_STANDARD.md` itself, because that document has to state the banned phrases in order to ban them. This would have made CI permanently red once that file was included in scope.
4. **`docs/QUALITY_SCORECARD.md` scored two dimensions as if the above citations already resolved** — "Documentation, traceability and GitHub reproducibility" at 6/6, and "Unique decision & portfolio separation" at 8/8 off a two-product comparison set.
5. **An unresolved lineage conflict**: `SOURCE_EVIDENCE/VANTIX-Flow-Integrity-v1.4.0-Final-Audit-Closure.md` describes a materially different release mechanism (Node.js/npm build, 76-file signed ZIP, dual deterministic builds, a different doc set) than this package assumes, and neither matches what's currently on the live GitHub repository (2 commits, no `.github/workflows/`, no Releases, no npm artifacts, as of this review). This wasn't acknowledged anywhere in the v1 package.

## What was changed, and why

| File | Change | Why |
|---|---|---|
| `docs/ARCHITECTURE.md` (new) | Written directly from the 26 real nodes in `workflows/Salesforce-Governance-Sentinel-v1.3-public.json` | Closes the citation; grounds the "deterministic before AI" claim in the actual node graph instead of prose |
| `docs/METHODOLOGY.md` (new) | Consolidates the Six Sigma boundary already stated in `README.md` | Same figures, dedicated file, closes the citation |
| `docs/TEST_EVIDENCE.md` (new) | States what the one validated run recorded; explicit executed-vs-design-only table | Closes the citation without upgrading the adversarial catalogue's status |
| `docs/DEPLOYMENT.md` (new) | Restates the existing Security boundary as configuration steps | Closes the citation |
| `docs/GOVERNANCE_REGISTERS.md` (new) | RAID-format restatement of the existing decision-rights table | Closes the citation used by the PMP mapping |
| `docs/RELEASE_NOTES.md` (new) | States v1.3 evidence + this remediation's changes, **and explicitly flags the v1.4.0 lineage question as unresolved, requiring owner confirmation** | Closes the citation; surfaces finding 5 instead of hiding it |
| `PROJECT_STATUS.md` (new) | One-page rollup of `FINAL_SIGNOFF_GATES.md` | Closes the citation |
| `samples/validated-run-summary.json` (new) | Structures figures already stated across multiple documents | Closes the citation. **Flagged internally for the owner to verify against raw run output before treating as authoritative** — it was not generated from a live re-execution |
| `projects/01-salesforce-governance-sentinel/SECURITY.md` (new) | Restates the existing Security boundary section | The root `SECURITY.md` already pointed here; the file didn't exist |
| `projects/01-salesforce-governance-sentinel/workflows/Salesforce-Governance-Sentinel-v1.3-public.json` (new) | The real supplied source workflow file | Was cited but not included in the overlay |
| `docs/PLAIN_LANGUAGE_SUMMARY.md` (new) | Non-technical explainer, matching the pattern already used on the Control Value project | Requested directly; was missing here |
| `docs/AUDIENCE_GUIDE.md` (new) | Role-by-role routing table for everyone who lands on the GitHub repo: recruiter, non-technical hiring manager, engineering hiring manager, Salesforce architect, n8n engineer, AI-governance reviewer, Six Sigma reviewer, PMP reviewer, security reviewer, CEO, CI/release auditor | Requested directly; each row is concrete (exact file, exact thing to check, exact reason to close the tab) rather than a generic front door |
| `scripts/validate_portfolio.py` | Added the 8 new doc files to the required list; excluded the Standard document from the banned-wording scan; added a non-blocking warning (not a hard failure) for `evidence/workflow-success.png` and `evidence/executive-report.html` | CI now actually enforces the citations it's supposed to guard, without fabricating the two artifacts that must come from a real n8n run |
| `docs/QUALITY_SCORECARD.md` | Total corrected 93 → 89, with a "Score history" section explaining the two corrected dimensions | The 93 wasn't dishonest, but it was scoring citations that didn't resolve. 89 is now defensible dimension-by-dimension |
| `docs/GAP_CLOSURE_MATRIX.md`, `docs/EVIDENCE_INDEX.md` | Updated status rows for the new files and the two owner-only evidence files | Keeps the matrix accurate instead of silently assuming closure |
| `CHANGELOG.md` | Added a "v2" section documenting all of the above | Standard practice; also gives you (the reviewing LLM) a single place to check this note against |

## What was deliberately NOT done

- **`evidence/workflow-success.png` and `evidence/executive-report.html` were not created.** These need to be a real screenshot and a real generated HTML report from an actual n8n execution. Authoring them as documentation would be fabricated evidence. `validate_portfolio.py` now warns (non-blocking) if they're missing so this stays visible instead of silently passing.
- **The v1.4.0 lineage question was not resolved by assumption.** Only the repository owner knows whether that release was ever published, is superseded, or is the actual intended path. Resolving it wrongly would create a worse problem than leaving it explicitly open.

## Verification

Both scripts were run against the corrected package directly (not just asserted to work):

```
$ python3 scripts/validate_portfolio.py
VALIDATION PASSED
- Required artifacts present
- JSON files parse
- Banned maturity/endorsement wording absent
- No obvious committed secret pattern detected
- Portfolio Preview control statements present

WARNINGS (non-blocking):
- Owner-supplied evidence not found: evidence/workflow-success.png
- Owner-supplied evidence not found: evidence/executive-report.html

$ python3 scripts/checksums.py --write && python3 scripts/checksums.py --check
Wrote SHA256SUMS
SHA256SUMS PASSED
```

## Open question back to you (the reviewing LLM)

Given the above, is there anything further you'd correct or add — particularly:
1. Does the `docs/ARCHITECTURE.md` node-graph description match your understanding of the workflow's intended design, or did this correction round miss something about how the nodes are meant to connect?
2. Do you have any information (not visible to this review) that resolves the v1.4.0 lineage question?
3. Is the corrected scorecard (89/100) itself defensible, or would you weight anything differently?


## Final verification round — additional corrections

A subsequent review found and corrected four further issues:

1. **Scorecard arithmetic defect:** the v2 row scores summed to 91 while the published total said 89. The score history also described impossible remaining points for a dimension already scored at full weight. This is corrected; the current row scores reconcile to **92/100**.
2. **Audience Guide defects:** the introduction said nine roles while the table actually contained eleven reviewer personas, and the root `SECURITY.md` relative link was one directory short. Both are corrected.
3. **Real run evidence recovered:** a preserved actual HTML report for run `VGS-20260730062123-IKKOFEN8` was located in the owner's retained files and added as `evidence/executive-report.html`, with an explicit provenance note. No screenshot was fabricated.
4. **CI link integrity:** `validate_portfolio.py` now parses relative Markdown links and fails on unresolved internal targets, so future dead citations cannot pass merely because a hand-maintained required-file list missed them.

Competitive positioning was also expanded to a third reviewed public product (Copado), and release lineage is now explicitly documented in `docs/RELEASE_LINEAGE.md` without claiming that the retained v1.4.0 artifact is currently published on GitHub.
