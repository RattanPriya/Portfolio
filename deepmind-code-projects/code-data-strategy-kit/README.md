# Code Data Strategy Kit

`code-data-strategy-kit` converts coding-product bets into a prioritization and data-collection plan. It is aimed at PMs working on AI coding models and developer agents.

## Why this matters

The DeepMind Code PM role asks for a data strategy that covers quality, style, and collection approaches. This project shows how to move from product use cases to measurable eval and data plans.

## Quick start

```bash
python -m code_data_strategy_kit examples/use_cases.json
```

## Product extensions

- Add persona-specific weighting for enterprise developers, students, and Google-internal engineers.
- Add eval ownership by model, UX surface, and data collection source.
- Connect collection cost to launch milestones.
