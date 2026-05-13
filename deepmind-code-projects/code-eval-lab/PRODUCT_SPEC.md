# Product Spec: Code Eval Studio

## Problem

Developer-agent products can look impressive in demos while failing in production workflows. Coding quality is multi-dimensional: passing tests is necessary but insufficient. Enterprise adoption requires a reliable answer to: "Can we trust this model or agent to work inside our codebase?"

## Proposal

Build a Code Eval Studio that lets teams create, run, review, and monitor evals for coding use cases.

## Key workflows

1. **Create a benchmark**
   - Select task families.
   - Import repo-specific tasks.
   - Define quality rubric and safety constraints.

2. **Run model or agent variants**
- Compare model versions.
   - Compare agent policies such as ask-before-edit vs autonomous patch.
   - Track latency, cost, correctness, and acceptance.

3. **Human review**
   - Route samples to reviewers in Workspace.
   - Capture style, maintainability, confidence, and usefulness ratings.
   - Calibrate rubric drift across reviewers.

4. **Launch gate**
   - Detect regressions by task family.
   - Require minimum score thresholds.
   - Generate release notes for model/policy changes.

## MVP scope

- Python/TypeScript SDK for task schema.
- Dashboard for model comparison.
- Human review queue.
- Regression report.
- Export to BigQuery.

## Out of scope for MVP

- Full IDE integration.
- Automatic model fine-tuning.
- Multi-org benchmark marketplace.

## Success metrics

- 80% of major coding-model launches use Eval Studio as a launch gate.
- 30% reduction in coding-model regressions reaching users.
- 20% lift in accepted suggestions on workflows with eval-backed improvements.
