from dataclasses import dataclass


@dataclass
class ChatMessage:
    role: str
    content: str


@dataclass
class LLMResponse:
    text: str