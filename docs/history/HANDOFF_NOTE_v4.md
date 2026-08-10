# v4 — What Changed and Why (For the LLM That Built v3)

An independent adversarial review of v3 found **one Critical code bug and two Minor documentation issues**. All three are fixed here. Nothing else changed — no new claims, no fabricated evidence, no score inflation beyond what the fix itself earns back.

## The Critical bug (fixed)

`scripts/validate_portfolio.py`'s internal Markdown-link checker (added in v3, line ~137) used this pattern:

```python
md_link = re.compile(r'(?<!!)\\[[^\\]]+\\]\\(([^)]+)\\)')
```

The double-escaped brackets (`\\[`, `\\]`, `\\(`, `\\)`) only match a literal backslash followed by a bracket character — something that never appears in real Markdown link syntax (`open-bracket`, link text, `close-bracket`, `open-paren`, target, `close-paren`, with no backslashes). The result: this check matched **zero links, ever**, and always reported "Internal Markdown links resolve" regardless of whether anything was actually broken.

**How this was proven, not just asserted:** a deliberately broken link was injected into `README.md` and the v3 script was re-run against it. It still printed `VALIDATION PASSED`. The bug was also independently visible in v3's own `FINAL_LOCAL_VALIDATION.txt`, which shows a `FutureWarning: Possible nested set at position 9` pointing at that exact line — the tooling flagged something was wrong with its own regex and it went unactioned.

**Fix:** corrected to `r'(?<!!)\[[^\]]+\]\(([^)]+)\)'` (single-escaped). Re-verified the same way: injected a broken link, confirmed the script now fails with `Broken internal Markdown link: README.md -> docs/THIS_FILE_DOES_NOT_EXIST.md`, then removed the injected link and confirmed a clean pass.

No links were actually broken in the live v3 content — this bug hadn't caused a real dead link yet, but it also couldn't have caught one going forward. It's now a functioning gate, not a decorative one.

## Two Minor doc fixes

1. **`docs/RELEASE_LINEAGE.md`** closed with "This resolves the documentation conflict" — overstated. It brackets/defers the v1.4.0 question, it doesn't resolve whether that release track should ever become authoritative. Reworded to say exactly that.
2. **`docs/RELEASE_LINEAGE.md` was orphaned** — not linked from the README review path or Evidence Index, ironic given this round's whole theme is navigation. Added as item 17 in the project README and a row in `docs/EVIDENCE_INDEX.md`.

## Score

No net change — still **92/100**. The Documentation dimension's 6/6 was flagged as *claimed but not earned* (the enforcement mechanism it cited didn't work); it's now genuinely earned, so the number stays the same but the justification is now true rather than aspirational.

## Not changed, still open

- Live GitHub Actions has still never run — that's the next real gate, not something further correction rounds can substitute for.
- The two owner-only items from prior rounds (`evidence/workflow-success.png`, the 8-point path to 100 requiring real demo + real adversarial execution) are unchanged and still require the owner's real-world action, not more documentation.

## One thing worth asking yourself before the next round

The pattern across v1→v4 has been: each round fixes what the previous round claimed but didn't fully deliver (missing files → broken citations → non-functional CI checks). Before declaring a future v5 "final," it may be worth running your own output against itself the way this review did — inject a known-bad case and confirm your own tooling actually catches it — rather than relying on a subsequent review to find it.
