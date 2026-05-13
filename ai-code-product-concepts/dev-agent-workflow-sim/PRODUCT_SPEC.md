# Product Spec: CI Doctor

## Problem

CI failures interrupt developer flow and slow launches. Current AI coding tools can inspect logs and patch code, but teams need a controlled workflow that separates diagnosis, patching, verification, and approval.

## Proposal

Build CI Doctor: an agentic workflow for CI triage and repair that integrates with CI systems, observability tools, and common Git providers.

## User journey

1. A CI job fails.
2. The agent summarizes the failure and classifies likely cause.
3. The agent checks recent diffs, ownership, historical failures, and related logs.
4. The agent proposes a patch plan.
5. For low-risk cases, the agent drafts a PR and reruns targeted tests.
6. The PR includes confidence, test evidence, and rollback guidance.

## MVP scope

- Failure classifier.
- Root-cause summary.
- Minimal patch plan.
- Test rerun recommendation.
- PR evidence template.

## Later bets

- Autonomous low-risk patching.
- Flaky-test quarantine workflows.
- Cross-repo dependency failure detection.
- Release-blocking regression dashboard.

## Success metrics

- 25% reduction in median time-to-green.
- 50% of known flaky failures correctly identified.
- 30% of CI-fix PRs accepted with no major revision.
