import pytest

from app.cache.redis_client import redis_client


@pytest.mark.asyncio
async def test_cache():

    await redis_client.set(
        "test",
        "hello"
    )

    value = await redis_client.get(
        "test"
    )

    assert value == "hello"