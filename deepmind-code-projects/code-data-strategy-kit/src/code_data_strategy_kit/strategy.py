def _score(use_case: dict) -> float:
    return round(
        0.3 * use_case.get("developer_frequency", 0)
        + 0.25 * use_case.get("business_impact", 0)
        + 0.2 * use_case.get("model_gap", 0)
        + 0.15 * use_case.get("data_availability", 0)
        - 0.1 * use_case.get("safety_risk", 0),
        3,
    )


def _collection_plan(use_case: dict) -> list[str]:
    name = use_case["name"].lower()
    plan = ["Collect prompt, repository context, accepted output, and post-edit delta."]
    if "bug" in name or "fix" in name:
        plan.append("Capture failing test, root cause label, patch diff, and regression test.")
    if "review" in name:
        plan.append("Capture reviewer comment, suggested change, developer acceptance, and follow-up edits.")
    if "explain" in name:
        plan.append("Collect readability ratings and factuality checks from developers with repo context.")
    return plan


def _eval_plan(use_case: dict) -> list[str]:
    return [
        "Correctness: tests pass or expected behavior satisfied.",
        "Style: output follows project conventions and readable structure.",
        "Usefulness: developer accepts or minimally edits the suggestion.",
        "Trust: model states uncertainty and avoids unsafe actions when confidence is low.",
    ]


def prioritize_use_cases(use_cases: list[dict]) -> list[dict]:
    ranked = []
    for use_case in use_cases:
        ranked.append(
            {
                "name": use_case["name"],
                "priority_score": _score(use_case),
                "collection_plan": _collection_plan(use_case),
                "eval_plan": _eval_plan(use_case),
            }
        )
    return sorted(ranked, key=lambda item: item["priority_score"], reverse=True)
