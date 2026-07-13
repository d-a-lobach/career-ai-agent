from openai import AsyncOpenAI

from app.config.settings import settings
from app.llm.models import ChatMessage
import logging


class OpenRouterClient:
    
    def __init__(self):

        self.client = AsyncOpenAI(
            api_key=settings.openrouter_api_key,
            base_url=settings.openrouter_base_url,
        )

    async def chat(
        self,
        messages: list[ChatMessage],
    ) -> str:
        
        response = await self.client.chat.completions.create(
            model=settings.openrouter_model,
            messages=[
                {
                    "role": m.role,
                    "content": m.content,
                }
                for m in messages
            ],
        )
        logger = logging.getLogger(__name__)
        logger.info("LLM request: model=%s", settings.openrouter_model)
        return response.choices[0].message.content


openrouter = OpenRouterClient()