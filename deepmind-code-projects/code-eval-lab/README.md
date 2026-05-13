# Code Eval Lab

`code-eval-lab` is a compact evaluation harness for AI-generated code. It scores candidate outputs on:

- unit-test pass rate
- style/readability signals
- risky patterns such as shell execution or unsafe dynamic evaluation
- developer usability notes

## Why this matters

The DeepMind Code PM role calls for a strong set of evaluations for coding use cases and a data strategy for quality, style, and collection approaches. This project demonstrates a practical skeleton for that work.

## Quick start

```bash
python -m code_eval_lab examples/tasks.json
```

## Product extensions

- Add benchmark families for bug fixing, refactoring, test generation, and code explanation.
- Track model regressions by task family and developer workflow.
- Add human preference review for style, maintainability, and trust.
- Segment evals by IDE, CLI, notebook, and code-review surfaces.
