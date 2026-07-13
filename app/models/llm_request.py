from dataclasses import dataclass


@dataclass(slots=True)
class LLMRequest:
    system_prompt: str
    vacancy: str
    resume: str
    question: str