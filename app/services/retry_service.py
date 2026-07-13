import asyncio


class RetryService:

    async def execute(
        self,
        func,
        retries: int,
        delay: float,
    ):
        last_exception = None

        for attempt in range(retries):

            try:
                return await func()

            except Exception as ex:
                last_exception = ex

                if attempt == retries - 1:
                    break

                await asyncio.sleep(delay)

                delay *= 2

        raise last_exception


retry_service = RetryService()