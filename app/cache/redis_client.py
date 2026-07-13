from redis.asyncio import Redis
import logging
from app.config.settings import settings

logger = logging.getLogger(__name__)
class RedisClient:

    def __init__(self):

        self.redis = Redis.from_url(
            settings.redis_url,
            decode_responses=True,
        )

    async def get(
        self,
        key: str,
    ):
        logger.info("Redis GET key=%s", key)
        return await self.redis.get(key)

    async def set(
        self,
        key: str,
        value: str,
        ttl: int | None = None,
    ):
        logger.info("Redis SET key=%s ttl=%s", key, ttl)
        await self.redis.set(
            key,
            value,
            ex=ttl,
        )
        logger.info("Redis SET completed")

    async def delete(
        self,
        key: str,
    ):
        await self.redis.delete(key)

    async def exists(
        self,
        key: str,
    ):
        return await self.redis.exists(key)


redis_client = RedisClient()