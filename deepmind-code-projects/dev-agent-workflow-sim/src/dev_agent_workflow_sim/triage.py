from dataclasses import dataclass


@dataclass
class TriageResult:
    category: str
    confidence: float
    next_action: str
    developer_prompt: str
    trust_boundary: str

    def to_dict(self) -> dict:
        return {
            "category": self.category,
            "confidence": self.confidence,
            "next_action": self.next_action,
            "developer_prompt": self.developer_prompt,
            "trust_boundary": self.trust_boundary,
        }


def triage_failure_log(log: str) -> TriageResult:
    lower = log.lower()
    if "assert" in lower or "expected" in lower:
        return TriageResult(
            category="test_expectation_mismatch",
            confidence=0.82,
            next_action="Inspect the failing assertion, identify intended behavior, and propose a minimal patch plus a regression test.",
            developer_prompt="I found a likely behavior mismatch. Should I draft a minimal patch and show the test delta?",
            trust_boundary="Do not apply code automatically until the developer confirms intended behavior.",
        )
    if "modulenotfounderror" in lower or "importerror" in lower:
        return TriageResult(
            category="dependency_or_import_error",
            confidence=0.78,
            next_action="Check dependency declarations, import paths, and package layout before changing product code.",
            developer_prompt="This looks like an environment or import issue. Should I inspect package config first?",
            trust_boundary="Avoid broad dependency changes without showing the affected import graph.",
        )
    if "timeout" in lower:
        return TriageResult(
            category="performance_regression",
            confidence=0.7,
            next_action="Profile the slow path, compare complexity against expected input size, and propose a targeted optimization.",
            developer_prompt="This may be a performance regression. Should I identify the slowest path before drafting a fix?",
            trust_boundary="Do not trade correctness for speed without benchmark and test evidence.",
        )
    return TriageResult(
        category="unknown_failure",
        confidence=0.45,
        next_action="Summarize the failure, gather reproduction steps, and ask for developer confirmation before patching.",
        developer_prompt="I need more context before suggesting a fix. Should I collect the failing command and changed files?",
        trust_boundary="Low confidence: keep the agent in explain-and-ask mode.",
    )
