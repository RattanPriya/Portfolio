# CI Doctor

## Product bet

The fastest path to trusted autonomous coding is not "write any feature from scratch." It is fixing the work developers already hate: failing tests, flaky CI, broken dependencies, migration fallout, and release-blocking regressions.

Agentic coding tools increasingly emphasize running tests, fixing failures, and creating PRs. This wedge turns that promise into a controlled product workflow for CI, logs, source control, ownership metadata, and enterprise-controlled repos.

## Target users

- Engineering teams with large test suites and noisy CI.
- Platform teams responsible for developer productivity.
- Release managers who need confidence before merging AI-authored fixes.

## MVP

1. Watch CI failures from Cloud Build, GitHub Actions, or GitLab.
2. Classify failures: flaky, dependency/import, assertion mismatch, performance timeout, infra issue, security regression.
3. Identify likely root cause using changed files, logs, ownership, and historical failures.
4. Draft a minimal patch and rerun relevant tests.
5. Open a PR with evidence: failure summary, patch, tests run, confidence, and rollback plan.

## Platform advantage

- Native CI and observability integration.
- Reliability playbooks and incident-management practices.
- Enterprise IAM and audit logs for safe automation.
- BigQuery for failure clustering across repos and teams.
- Collaboration handoff: PR summaries, incident docs, launch notes.

## Prototype

The included Python simulator classifies a failure log and recommends the next agent action:

```bash
python -m dev_agent_workflow_sim examples/failure_log.txt
```

The production product would connect this triage layer to repo context, test reruns, patch generation, and PR creation.

## North-star metrics

- Mean time to green for CI failures.
- Percent of failures correctly classified.
- Percent of AI-authored CI-fix PRs accepted.
- Reduction in flaky-test noise.
- Rollback or revert rate for AI-authored patches.

## Risks and mitigations

- Risk: agent applies incorrect patches to make tests pass.
  Mitigation: require behavior-preserving evidence, minimal diffs, and reviewer approval for high-risk changes.
- Risk: noisy CI causes low trust.
  Mitigation: start with classification and explanation before autonomous fixes.
- Risk: enterprise permission concerns.
  Mitigation: IAM-scoped actions, audit logs, and policy controls by repo/service.
