# Agile Traceability — Flow Integrity

## Purpose

Show how a governance finding becomes delivery-ready evidence without allowing AI to commit work or impersonate Scrum decision authority.

## Traceability chain

```text
Salesforce Flow metadata
        ↓
Deterministic governance finding
        ↓
Measured defect / opportunity context
        ↓
Bounded AI impact assessment
        ↓
Critique + deterministic response validation
        ↓
Governed route
        ↓
Controlled remediation-story draft
        ↓
Human review / prioritisation
        ↓
Human sprint or backlog decision
```

## Decision traceability

| Stage | Evidence / control | Authority |
|---|---|---|
| Source | Customer-owned Salesforce Flow metadata | Salesforce source evidence |
| Finding | Deterministic governance rule identifies the declared condition | Code |
| Measurement | Defect/opportunity count, DPMO, Sigma and I-MR logic | Code |
| Context | Business-impact interpretation | Bounded AI advisory |
| Challenge | Critique checks unsupported/inconsistent AI response | AI advisory within bounded contract |
| Validation | Required response structure is checked before routing | Deterministic code |
| Route | Critical / Minor / uncertain disposition | Governed logic; uncertain fails to human review |
| Story draft | Remediation can be expressed as a controlled Agile story | Draft only |
| Priority / sprint commitment | Human decides whether and when work enters delivery | Human authority |

## Agile controls demonstrated

### Definition of Ready principle
A remediation item should not be treated as delivery-ready merely because AI generated text. It needs:
- an identifiable source finding;
- evidence of the governance condition;
- a bounded route;
- acceptance intent that can be reviewed;
- a human decision before backlog/sprint commitment.

### Acceptance-criteria discipline
The project may draft remediation acceptance criteria, but they remain reviewable text. The AI is not permitted to transform an unsupported assumption into an authoritative requirement.

### Human Scrum authority
The project does not allow AI to:
- assign story points as fact;
- commit work to a sprint;
- approve remediation;
- represent Product Owner or Scrum Master authority.

## Example using the validated v1.3 evidence

**Source condition:** missing Flow description is recorded as the declared governance defect in the validated dataset.

**Deterministic evidence:** the condition contributes to the declared defect/opportunity count and resulting DPMO/Sigma model.

**Route:** the validated v1.3 result records seven Minor routes.

**Delivery implication:** a Minor result can become a remediation-story candidate, but backlog priority and sprint commitment remain human decisions.

This example uses the published validated result only. It does not invent a completed sprint, story-point estimate, velocity outcome or customer benefit.
