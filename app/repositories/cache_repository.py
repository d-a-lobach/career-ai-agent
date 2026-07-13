import logging

from app.cache.keys import RedisKeys
from app.cache.redis_client import redis_client
from app.config.settings import settings

logger = logging.getLogger(__name__)


class CacheRepository:

    async def save_vacancy(
        self,
        user_id: int,
        description: str,
    ):
        key = RedisKeys.vacancy(user_id)

        logger.info(
            "Сохранение вакансии в Redis. user_id=%s key=%s size=%d",
            user_id,
            key,
            len(description),
        )

        logger.debug(
            "Vacancy preview: %s",
            description[:300],
        )

        await redis_client.set(
            key,
            description,
            ttl=settings.vacancy_cache_ttl,
        )

        logger.info(
            "Вакансия успешно сохранена. key=%s ttl=%s",
            key,
            settings.vacancy_cache_ttl,
        )

    async def get_vacancy(
        self,
        user_id: int,
    ):
        key = RedisKeys.vacancy(user_id)

        logger.info(
            "Чтение вакансии из Redis. user_id=%s key=%s",
            user_id,
            key,
        )

        vacancy = await redis_client.get(key)

        if vacancy is None:
            logger.warning(
                "Вакансия не найдена в Redis. key=%s",
                key,
            )
        else:
            logger.info(
                "Вакансия успешно получена. size=%d",
                len(vacancy),
            )
            logger.debug(
                "Vacancy preview: %s",
                vacancy[:300],
            )

        return vacancy

    async def save_resume(
        self,
        user_id: int,
        description: str,
    ):
        key = RedisKeys.resume(user_id)

        logger.info(
            "Сохранение резюме в Redis. user_id=%s key=%s size=%d",
            user_id,
            key,
            len(description),
        )

        logger.debug(
            "Resume preview: %s",
            description[:300],
        )

        await redis_client.set(
            key,
            description,
            ttl=settings.resume_cache_ttl,
        )

        logger.info(
            "Резюме успешно сохранено. key=%s ttl=%s",
            key,
            settings.resume_cache_ttl,
        )

    async def get_resume(
        self,
        user_id: int,
    ):
        key = RedisKeys.resume(user_id)

        logger.info(
            "Чтение резюме из Redis. user_id=%s key=%s",
            user_id,
            key,
        )

        resume = await redis_client.get(key)

        if resume is None:
            logger.warning(
                "Резюме не найдено в Redis. key=%s",
                key,
            )
        else:
            logger.info(
                "Резюме успешно получено. size=%d",
                len(resume),
            )
            logger.debug(
                "Resume preview: %s",
                resume[:300],
            )

        return resume


cache_repository = CacheRepository()