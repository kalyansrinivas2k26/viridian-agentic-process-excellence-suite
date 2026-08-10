#!/usr/bin/env python3
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

required = [
    ROOT / "README.md",
    ROOT / ".gitignore",
    ROOT / "LICENSE",
    ROOT / "SECURITY.md",
    ROOT / "CHANGELOG.md",
    ROOT / "docs/PORTFOLIO_ROADMAP.md",
    ROOT / "docs/EXECUTIVE_DOCUMENTATION_STANDARD.md",
    ROOT / "projects/01-salesforce-governance-sentinel/README.md",
    ROOT / "projects/01-salesforce-governance-sentinel/LICENSE",
    ROOT / "projects/01-salesforce-governance-sentinel/SECURITY.md",
    ROOT / "projects/01-salesforce-governance-sentinel/workflows/Salesforce-Governance-Sentinel-v1.3-public.json",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/EXECUTIVE_BRIEF.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/EVIDENCE_INDEX.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/QUALITY_SCORECARD.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/SECURITY_THREAT_MODEL.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/PMP_AI_GOVERNANCE_MAPPING.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/FINAL_SIGNOFF_GATES.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/AGILE_TRACEABILITY.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/COMPETITIVE_POSITIONING.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/ADVERSARIAL_TEST_CATALOGUE.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/GAP_CLOSURE_MATRIX.md",
    # Added in the documentation-completeness remediation: these files were
    # cited as evidence by EVIDENCE_INDEX.md, EXECUTIVE_BRIEF.md, and
    # PMP_AI_GOVERNANCE_MAPPING.md before they existed, which meant a green
    # CI run did not guarantee those citations resolved. Adding them here
    # closes that gap.
    ROOT / "projects/01-salesforce-governance-sentinel/docs/ARCHITECTURE.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/METHODOLOGY.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/TEST_EVIDENCE.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/RELEASE_NOTES.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/DEPLOYMENT.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/GOVERNANCE_REGISTERS.md",
    ROOT / "projects/01-salesforce-governance-sentinel/PROJECT_STATUS.md",
    ROOT / "projects/01-salesforce-governance-sentinel/samples/validated-run-summary.json",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/PLAIN_LANGUAGE_SUMMARY.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/AUDIENCE_GUIDE.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/DEMO_SCRIPT.md",
    ROOT / "projects/01-salesforce-governance-sentinel/docs/RELEASE_LINEAGE.md",
    ROOT / "projects/01-salesforce-governance-sentinel/evidence/README.md",
    ROOT / "projects/01-salesforce-governance-sentinel/evidence/executive-report.html",
]
for p in required:
    if not p.exists():
        errors.append(f"Missing required artifact: {p.relative_to(ROOT)}")

# Owner-supplied historical run evidence (screenshot + generated HTML report).
# These are not created by this remediation package because they must come
# from a real n8n execution, not be authored by documentation tooling.
# Their absence is a WARNING, not a CI failure, until the owner confirms
# whether they already exist elsewhere in repository history.
owner_supplied_evidence = [
    ROOT / "projects/01-salesforce-governance-sentinel/evidence/workflow-success.png",
]
warnings = []
for p in owner_supplied_evidence:
    if not p.exists():
        warnings.append(
            f"Owner-supplied evidence not found (non-blocking): {p.relative_to(ROOT)}. "
            "Confirm whether this already exists in repository history; if not, it "
            "must come from a real workflow run, not be authored as documentation."
        )

# Parse every JSON file in the repository.
for p in ROOT.rglob("*.json"):
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"Invalid JSON: {p.relative_to(ROOT)}: {exc}")

# Mature/endorsement wording that is prohibited by the portfolio standard.
banned = [
    r"McKinsey[- ](?:standard|style|level)",
    r"\bproduction[- ]ready\b",
    r"\bindependent external audit\b",
    r"\bindependent audit\b",
    r"\bexternally certified\b",
    r"\bexternal certification achieved\b",
    r"\bno competitor does this\b",
]
# The Standard itself must define the banned phrases in order to ban them,
# so it is excluded from this scan. This was a false-positive bug found
# during independent review: the original scan flagged the rulebook for
# containing the words it forbids everywhere else.
wording_scan_exclude = {
    ROOT / "docs/EXECUTIVE_DOCUMENTATION_STANDARD.md",
    ROOT / "SOURCE_EVIDENCE/EXECUTIVE_DOCUMENTATION_STANDARD.md",
}
for p in list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.html")):
    if p in wording_scan_exclude:
        continue
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    for pattern in banned:
        if re.search(pattern, text, flags=re.I):
            errors.append(f"Prohibited wording in {p.relative_to(ROOT)}: /{pattern}/")

# Strong secret-pattern checks only; avoid flagging instructional words such as "Consumer Secret".
secret_patterns = [
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    r"(?i)\b(?:access[_-]?token|client[_-]?secret|api[_-]?key)\s*[:=]\s*[\"']?[A-Za-z0-9_\-]{20,}",
    r"(?i)\bBearer\s+[A-Za-z0-9_\-\.]{20,}",
]
for p in ROOT.rglob("*"):
    if not p.is_file() or ".git" in p.parts:
        continue
    if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip"}:
        continue
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    for pattern in secret_patterns:
        if re.search(pattern, text):
            errors.append(f"Possible secret material in {p.relative_to(ROOT)} matching /{pattern}/")

# Core evidence-safe statements that must remain present.
root = (ROOT / "README.md").read_text(encoding="utf-8")
project = (ROOT / "projects/01-salesforce-governance-sentinel/README.md").read_text(encoding="utf-8")
for label, text, token in [
    ("root maturity boundary", root, "Portfolio Preview"),
    ("project maturity boundary", project, "Portfolio Preview"),
    ("human authority", project, "Human"),
    ("evidence link", project, "Evidence Index"),
    ("demo disclosure", project, "Demo"),
]:
    if token not in text:
        errors.append(f"Missing {label}: expected token '{token}'")


# Validate internal Markdown links so CI catches dead evidence/navigation paths.
#
# BUG FOUND IN INDEPENDENT REVIEW (v3 -> v4): the previous pattern used
# double-escaped brackets (\\[ \\] \\( \\)), which only match a literal
# backslash followed by a bracket -- something that never appears in real
# Markdown. That made this check match zero links, ever, regardless of
# whether any link was broken. Confirmed by injecting a deliberately broken
# link into README.md and re-running this script: it still printed
# "VALIDATION PASSED - Internal Markdown links resolve." The tool even
# raised a FutureWarning ("Possible nested set at position 9") pointing at
# this exact line in its own prior run log, which was not acted on.
# Corrected pattern below uses single-escaped brackets, which is what
# actually matches Markdown link syntax `[text](target)`.
md_link = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
for p in ROOT.rglob("*.md"):
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    for raw_target in md_link.findall(text):
        target = raw_target.strip().split()[0].strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = target.split("#", 1)[0]
        resolved = (p.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"Markdown link escapes repository: {p.relative_to(ROOT)} -> {raw_target}")
            continue
        if not resolved.exists():
            errors.append(f"Broken internal Markdown link: {p.relative_to(ROOT)} -> {raw_target}")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("VALIDATION PASSED")
print("- Required artifacts present")
print("- JSON files parse")
print("- Banned maturity/endorsement wording absent")
print("- No obvious committed secret pattern detected")
print("- Portfolio Preview control statements present")
print("- Internal Markdown links resolve")
if warnings:
    print("\nWARNINGS (non-blocking):")
    for w in warnings:
        print(f"- {w}")
