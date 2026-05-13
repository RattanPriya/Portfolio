# Code Eval Studio

## Product bet

AI coding products need a first-party eval workbench for coding models and developer agents. The winning coding product will not be judged only by benchmark pass rates; teams need to know whether generated code is correct, idiomatic, secure, maintainable, explainable, and accepted by developers inside real workflows.

Developer agents are training users to expect end-to-end coding support. The durable product moat is the eval and data loop behind code quality: task taxonomies, human review, regression dashboards, and organization-specific benchmarks.

## Target users

- Product and research teams improving coding models.
- Enterprise platform teams evaluating AI coding adoption.
- Engineering leaders who need trust metrics before allowing autonomous coding workflows.

## MVP

1. Define coding task families: bug fix, refactor, test generation, code review response, migration, explanation, and performance optimization.
2. Evaluate outputs across correctness, style, safety, usefulness, and trust.
3. Compare model variants or agent policies across task families.
4. Add human reviewer judgment for maintainability, idiomatic style, and confidence calibration.
5. Produce a regression report before promoting a model or agent workflow.

## Platform advantage

- Private repo-specific benchmarks.
- Human review flows for maintainability, style, and trust.
- Enterprise trust controls: IAM, audit logs, and data boundaries.
- Evaluation discipline borrowed from search, ads, and recommendation systems: rater programs, task taxonomies, and experiment rigor.

## Prototype

The included Python harness demonstrates the scoring skeleton:

```bash
python -m code_eval_lab examples/tasks.json
```

It scores candidate code on correctness, style, safety, and developer usability. A production version would plug into model runs, repo-specific test suites, and human review.

## North-star metrics

- Regression detection rate before model launch.
- Human preference win rate vs baseline model.
- Task-family coverage across top developer workflows.
- Accepted suggestion rate in IDE/CLI/CI surfaces.
- Reduction in post-merge defects from AI-authored code.

## Risks and mitigations

- Risk: evals overfit to synthetic tasks.
  Mitigation: add enterprise repo-specific private evals and post-edit deltas.
- Risk: correctness dominates style and trust.
  Mitigation: multi-axis scorecards and human reviewer calibration.
- Risk: teams do not trust aggregate scores.
  Mitigation: show evidence: tests, diffs, reviewer comments, and failure exemplars.
