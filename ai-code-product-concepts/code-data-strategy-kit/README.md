# Workspace-to-Code Graph

## Product bet

The next generation of coding agents will need more than repository context. They need product intent: design docs, meeting notes, customer requests, support escalations, experiments, issue trackers, analytics, and past architectural decisions.

Workspace-to-Code Graph is a product concept for turning scattered product and engineering context into implementation plans, test plans, PRs, and durable team memory.

## Target users

- Product-minded engineering teams moving from ambiguous requirements to code.
- PMs and tech leads who need implementation plans from messy source material.
- Developer platform teams standardizing how agents understand team context.

## MVP

1. Ingest product docs, meeting notes, issue threads, repo history, and code ownership metadata.
2. Extract requirements, constraints, open questions, dependencies, and acceptance criteria.
3. Generate implementation plans and test plans.
4. Link generated plans back to source evidence.
5. Maintain team memory: coding conventions, architecture decisions, launch gotchas, and review preferences.

## Platform advantage

- Native connectors into documents, tickets, chats, source control, and observability.
- Permission-aware context retrieval.
- Evidence-backed planning with source links.
- Team memory that improves across repeated agent sessions.

## Prototype

The included Python toolkit prioritizes coding use cases and creates a data/eval plan:

```bash
python -m code_data_strategy_kit examples/use_cases.json
```

The production version would expand this into a context graph and planning system that connects product intent to implementation.

## North-star metrics

- Time from product brief to approved implementation plan.
- Reduction in requirement clarification loops.
- PR acceptance rate for agent-generated implementation plans.
- Source-grounding accuracy for generated requirements.
- New engineer onboarding time.

## Risks and mitigations

- Risk: context leakage across permission boundaries.
  Mitigation: source-level permissions, audit logs, and redaction.
- Risk: generated plans hallucinate requirements.
  Mitigation: evidence links and explicit open-question tracking.
- Risk: team memory becomes stale.
  Mitigation: expiration, owner review, and conflict detection.
