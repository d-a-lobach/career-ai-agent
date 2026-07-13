import logging
import time

from openai import AsyncOpenAI

from app.config.settings import settings
from app.services.retry_service import retry_service

logger = logging.getLogger(__name__)


class LLMService:

    def __init__(self):

        logger.info(
            "Initializing LLMService..."
        )

        logger.info(
            "OpenRouter base_url=%s",
            settings.openrouter_base_url,
        )

        logger.info(
            "Model=%s",
            settings.openrouter_model,
        )

        self.client = AsyncOpenAI(
            api_key=settings.openrouter_api_key,
            base_url=settings.openrouter_base_url,
        )

        logger.info("LLM client initialized.")

    async def ask(self, prompt: str):

        logger.info(
            "Preparing request to OpenRouter..."
        )

        logger.info(
            "Prompt length: %d characters",
            len(prompt),
        )

        logger.debug(
            "Prompt preview:\n%s",
            prompt[:1000],
        )

        async def request():

            start = time.perf_counter()

            logger.info(
                "Sending request to model '%s'...",
                settings.openrouter_model,
            )

            completion = await self.client.chat.completions.create(
                model=settings.openrouter_model,
                messages=[
                    {
                        "role": "system",
                        "content": prompt,
                    }
                ],
            )

            elapsed = time.perf_counter() - start

            logger.info(
                "OpenRouter responded in %.2f sec",
                elapsed,
            )

            answer = completion.choices[0].message.content

            logger.info(
                "Received response. Length=%d characters",
                len(answer),
            )

            logger.debug(
                "Response preview:\n%s",
                answer[:1000],
            )

            return answer

        try:

            result = await retry_service.execute(
                request,
                retries=settings.llm_max_retries,
                delay=settings.llm_retry_delay,
            )

            logger.info(
                "LLM request completed successfully."
            )

            return result

        except Exception:

            logger.exception(
                "OpenRouter request failed."
            )

            raise


llm_service = LLMService()