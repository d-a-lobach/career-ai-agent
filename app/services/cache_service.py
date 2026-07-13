from redis.asyncio import Redis

from app.config.settings import settings


class CacheService:
    def __init__(self):
        self.redis = Redis.from_url(
            settings.redis_url,
            decode_responses=True,
        )

    @staticmethod
    def vacancy_key(user_id: int) -> str:
        return f"user:{user_id}:vacancy"

    @staticmethod
    def resume_key(user_id: int) -> str:
        return f"user:{user_id}:resume"

    async def save_vacancy(
        self,
        user_id: int,
        description: str,
    ):
        await self.redis.set(
            self.vacancy_key(user_id),
            description,
            ex=settings.vacancy_cache_ttl,
        )

    async def get_vacancy(self, user_id: int):
        return await self.redis.get(
            self.vacancy_key(user_id)
        )

    async def save_resume(
        self,
        user_id: int,
        description: str,
    ):
        await self.redis.set(
            self.resume_key(user_id),
            description,
            ex=settings.resume_cache_ttl,
        )

    async def get_resume(self, user_id: int):
        return await self.redis.get(
            self.resume_key(user_id)
        )


cache_service = CacheService()