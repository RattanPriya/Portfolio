from dataclasses import dataclass
from typing import Iterable


RISKY_PATTERNS = ("eval(", "exec(", "subprocess.", "os.system(", "pickle.loads(")


@dataclass
class EvaluationResult:
    task_id: str
    correctness: float
    style: float
    safety: float
    usability: float
    notes: list[str]

    @property
    def overall(self) -> float:
        return round(
            0.45 * self.correctness
            + 0.2 * self.style
            + 0.2 * self.safety
            + 0.15 * self.usability,
            3,
        )

    def to_dict(self) -> dict:
        return {
            "task_id": self.task_id,
            "correctness": self.correctness,
            "style": self.style,
            "safety": self.safety,
            "usability": self.usability,
            "overall": self.overall,
            "notes": self.notes,
        }


def _style_score(code: str) -> tuple[float, list[str]]:
    notes = []
    lines = [line for line in code.splitlines() if line.strip()]
    long_lines = [line for line in lines if len(line) > 100]
    if long_lines:
        notes.append(f"{len(long_lines)} lines exceed 100 chars")
    if "def " not in code and "class " not in code:
        notes.append("candidate may lack reusable structure")
    score = 1.0 - min(0.5, 0.1 * len(long_lines))
    if len(lines) > 80:
        score -= 0.15
        notes.append("candidate is relatively large for the task")
    return max(0.0, round(score, 2)), notes


def _safety_score(code: str) -> tuple[float, list[str]]:
    hits = [pattern for pattern in RISKY_PATTERNS if pattern in code]
    if not hits:
        return 1.0, []
    return max(0.0, round(1.0 - 0.25 * len(hits), 2)), [f"risky pattern: {hit}" for hit in hits]


def evaluate_candidate(task: dict) -> EvaluationResult:
    tests_passed = task.get("tests_passed", 0)
    tests_total = max(1, task.get("tests_total", 1))
    correctness = round(tests_passed / tests_total, 2)
    style, style_notes = _style_score(task.get("candidate_code", ""))
    safety, safety_notes = _safety_score(task.get("candidate_code", ""))
    usability = 1.0 if task.get("has_explanation") else 0.65
    notes = style_notes + safety_notes
    if correctness < 1:
        notes.append(f"{tests_total - tests_passed} tests failing")
    if not task.get("has_explanation"):
        notes.append("missing developer-facing explanation")
    return EvaluationResult(
        task_id=task["task_id"],
        correctness=correctness,
        style=style,
        safety=safety,
        usability=usability,
        notes=notes,
    )


def evaluate_suite(tasks: Iterable[dict]) -> list[EvaluationResult]:
    return [evaluate_candidate(task) for task in tasks]
