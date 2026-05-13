import json
import sys

from .strategy import prioritize_use_cases


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python -m code_data_strategy_kit examples/use_cases.json")
        return 2
    with open(sys.argv[1], "r", encoding="utf-8") as handle:
        use_cases = json.load(handle)
    print(json.dumps(prioritize_use_cases(use_cases), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
