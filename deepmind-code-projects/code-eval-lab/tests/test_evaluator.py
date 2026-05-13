from code_eval_lab import evaluate_candidate, evaluate_suite


def test_scores_correct_candidate_highly():
    result = evaluate_candidate(
        {
            "task_id": "ok",
            "tests_passed": 10,
            "tests_total": 10,
            "has_explanation": True,
            "candidate_code": "def add(a, b):\n    return a + b\n",
        }
    )
    assert result.overall > 0.9
    assert result.safety == 1.0


def test_flags_risky_patterns():
    result = evaluate_candidate(
        {
            "task_id": "risky",
            "tests_passed": 1,
            "tests_total": 2,
            "has_explanation": False,
            "candidate_code": "def run(x):\n    return eval(x)\n",
        }
    )
    assert result.safety < 1.0
    assert any("risky pattern" in note for note in result.notes)


def test_evaluate_suite_returns_all_results():
    assert len(evaluate_suite([{"task_id": "a", "candidate_code": ""}])) == 1
