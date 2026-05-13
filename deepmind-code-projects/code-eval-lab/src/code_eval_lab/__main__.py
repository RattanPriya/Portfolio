import json
import sys

from .evaluator import evaluate_suite


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python -m code_eval_lab examples/tasks.json")
        return 2
    with open(sys.argv[1], "r", encoding="utf-8") as handle:
        tasks = json.load(handle)
    results = evaluate_suite(tasks)
    print(json.dumps([result.to_dict() for result in results], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
