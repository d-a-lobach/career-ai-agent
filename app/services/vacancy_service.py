from app.parsers.hh_parser import HHParser
from app.repositories.cache_repository import cache_repository
import logging

logger = logging.getLogger(__name__)
class VacancyService:

    def __init__(self):
        self.parser = HHParser()

    async def load(
        self,
        user_id: int,
        url: str,
    ):

        vacancy = await self.parser.parse(url)

        await cache_repository.save_vacancy(
            user_id,
            vacancy.description,
        )

        return vacancy


vacancy_service = VacancyService()