# Methodology

## Defect model

The validated release declares three governance opportunities per Flow:

1. Active version exists.
2. Description is present.
3. Latest version is the active version.

Each failed opportunity counts as one defect.

## DPMO

```text
DPMO = total defects / total opportunities × 1,000,000
```

Validated run:

```text
7 defects / (7 Flows × 3 opportunities) × 1,000,000
= 333,333.33 DPMO
```

## Sigma

The workflow converts yield to a long-term Sigma estimate using a 1.5-sigma shift. The report labels the result as a governance defect-density indicator, not a certification of process capability.

## Cpk

Cpk is excluded. A defensible Cpk calculation requires:

- a continuous process characteristic;
- a stable process distribution;
- customer-approved upper and lower specification limits.

Those conditions do not exist for the current binary metadata checks. Displaying a decorative Cpk value would be methodologically false.

## Priority and routing

```text
Priority score = exposure score × AI impact score
```

Exposure is derived deterministically from observed defect density. AI provides contextual impact and rationale. Routing uses the validated score and output contract.

| Route | Treatment |
| --- | --- |
| Critical | Draft immediate-review remediation story |
| Minor | Draft governed maintenance-backlog story |
| Review Required | Preserve finding for human assessment |

AI does not estimate effort, assign story points, approve implementation, close findings, or commit work to a sprint.

## Statistical process control

The workflow stores DPMO by run and calculates I-MR limits:

```text
Individuals sigma estimate = MR-bar / 1.128
I-chart UCL/LCL = mean ± 3 × sigma estimate
MR-chart UCL = 3.267 × MR-bar
MR-chart LCL = 0
```

The formulas are mathematically valid from two observations, but the report marks early limits low-confidence until approximately 20 observations exist.

## AI governance

1. Constrained structured-output prompt.
2. Explicit prohibition on inventing facts.
3. Independent critique pass.
4. Deterministic parsing and schema validation.
5. Duplicate and unexpected-ID checks.
6. Confidence validation.
7. Safe fallback on malformed or inconsistent AI responses.
8. Human authority over remediation.

