from abc import ABC, abstractmethod

from app.models.vacancy import Vacancy


class BaseVacancyParser(ABC):

    @abstractmethod
    async def parse(self, url: str) -> Vacancy:
        pass