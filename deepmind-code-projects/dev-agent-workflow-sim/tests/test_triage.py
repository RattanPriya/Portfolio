from dev_agent_workflow_sim import triage_failure_log


def test_assertion_failure_routes_to_behavior_mismatch():
    result = triage_failure_log("AssertionError: expected 4 got 5")
    assert result.category == "test_expectation_mismatch"
    assert "minimal patch" in result.next_action


def test_import_error_routes_to_dependency_check():
    result = triage_failure_log("ModuleNotFoundError: No module named yaml")
    assert result.category == "dependency_or_import_error"


def test_unknown_stays_low_confidence():
    result = triage_failure_log("something broke")
    assert result.confidence < 0.5
