# Dev Agent Workflow Sim

`dev-agent-workflow-sim` models a developer agent that triages failing test logs and recommends the next best action. It is not an LLM wrapper; it is a workflow scaffold for thinking about developer-agent product behavior.

## Why this matters

The DeepMind role explicitly mentions an agent to support developers in critical workflows. A strong PM should reason about the workflow, control points, trust boundaries, and handoff between model suggestions and developer action.

## Quick start

```bash
python -m dev_agent_workflow_sim examples/failure_log.txt
```

## Product extensions

- Add IDE and CLI surface variants.
- Add confidence thresholds and escalation to human review.
- Track time-to-fix, accepted suggestion rate, and rollback rate.
- Connect triage labels to eval task families.
