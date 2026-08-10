# Release Lineage — Flow Integrity

## Canonical public engineering baseline

The repository documentation in this remediation preserves **v1.3** as the canonical executed engineering evidence baseline from 30 July 2026.

## Historical v1.4.0 audit artifact

The owner's retained project files also contain a later **v1.4.0 release-engineering/audit artifact** with deterministic-build and archive-verification controls, including a recorded SHA-256 beginning `3565077f4bacec...`.

That historical artifact demonstrates that a later hardening/release-engineering branch existed. It is **not treated here as a currently published GitHub Release**, because the live public repository state being remediated does not presently expose the corresponding release/tag/tooling set.

Accordingly:

- v1.3 remains the public executed workflow-evidence baseline used by this Portfolio Preview documentation;
- the retained v1.4.0 audit artifact is preserved as historical lineage;
- this remediation does not silently merge v1.4.0 release mechanics into v1.3;
- no claim is made that v1.4.0 is currently published on GitHub unless the matching tag/release/artifacts are visibly restored and verified.

This resolves the *documentation conflict* — the two audit documents no longer contradict each other in text. It does **not** resolve the underlying question of whether v1.4.0's release mechanics should eventually become authoritative for this project; that remains open, pending the owner's confirmation.
