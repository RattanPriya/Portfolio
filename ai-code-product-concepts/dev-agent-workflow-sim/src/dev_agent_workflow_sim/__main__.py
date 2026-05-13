import json
import sys

from .triage import triage_failure_log


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python -m dev_agent_workflow_sim examples/failure_log.txt")
        return 2
    with open(sys.argv[1], "r", encoding="utf-8") as handle:
        result = triage_failure_log(handle.read())
    print(json.dumps(result.to_dict(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
