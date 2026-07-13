from dataclasses import dataclass


@dataclass(slots=True)
class Vacancy:
    url: str
    title: str
    company: str
    description: str