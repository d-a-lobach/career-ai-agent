from dataclasses import dataclass


@dataclass(slots=True)
class RecruiterQuestion:
    user_id: int
    question: str