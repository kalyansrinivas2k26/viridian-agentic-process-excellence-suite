# Flow Integrity — What This Is (Plain-Language Summary)

*Written for recruiters, hiring managers, and anyone reviewing this project without a technical background. For full engineering detail, start at `README.md`.*

## The problem, in one sentence

Salesforce automations (Flows) pile up over the years, and nobody has a repeatable, evidence-backed way to say which ones are actually a governance risk — most reviews are manual, occasional, and forgotten the moment the reviewer moves to the next task.

## What this project does

Flow Integrity reads a company's Salesforce Flow metadata and turns it into a scored, evidence-backed decision, in four steps that never blur together:

1. **Count the facts.** Code — not AI — counts governance defects (like a Flow with no description) and calculates a standard quality score (DPMO / Sigma level, the same measurement Six Sigma teams use on a factory floor, applied here to Salesforce configuration).
2. **Ask AI what it means.** An AI model looks at the counted facts and judges how serious each one is — but it can't change the numbers code already calculated.
3. **Double-check the AI.** A second AI pass challenges the first one's judgment before anything moves forward.
4. **Let a human decide what happens next.** The system can draft a suggested fix, but only a person can approve it or put it on a sprint.

If the AI's answer doesn't match the expected format, or looks unsupported, the system doesn't guess — it routes the item to a human review queue instead.

## Why this is a meaningful piece of work

Three skills come together here, each independently checkable against the actual files in this repository:

- **Salesforce administration** — real OAuth-based, least-privilege integration with the Salesforce Flow metadata API.
- **Six Sigma measurement discipline** — the DPMO/Sigma calculation is deterministic and reproducible by hand from the stated defect count and opportunity denominator; it's shown with its full context (unit, defect definition, dataset), never as a bare, unexplained number.
- **Responsible AI / governance engineering** — the AI is never allowed to invent a fact, override a calculation, or approve its own recommendation. That boundary is enforced in the actual workflow structure, not just claimed in a document.

## What this is, honestly

- A **Portfolio Preview** — one validated run against a controlled dataset, not a live production deployment.
- Real engineering: a 26-node n8n workflow export with governed execution paths, a genuine second-opinion AI check, and a human fallback path that's actually wired in, not just described.

## What this is not (yet)

- It hasn't been tested against a large, live company's Salesforce org.
- It hasn't been reviewed by an outside security or Salesforce expert.
- A short recorded demo is still pending — check `README.md` for the current status.

## The one-line pitch

*"A Salesforce governance checker that measures problems the same rigorous way a factory measures defects — and never lets AI make the final call."*
