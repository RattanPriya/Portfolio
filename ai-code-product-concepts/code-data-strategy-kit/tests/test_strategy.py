from code_data_strategy_kit import prioritize_use_cases


def test_prioritizes_high_score_first():
    result = prioritize_use_cases(
        [
            {"name": "low", "developer_frequency": 0.1},
            {"name": "high", "developer_frequency": 1.0, "business_impact": 1.0},
        ]
    )
    assert result[0]["name"] == "high"


def test_bug_fix_gets_regression_collection_plan():
    result = prioritize_use_cases([{"name": "bug fix from failing test"}])
    assert any("regression test" in step for step in result[0]["collection_plan"])
