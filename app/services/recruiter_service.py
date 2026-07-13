from app.config.prompts import (
    SYSTEM_PROMPT,
    build_prompt,
)
import logging
import traceback
from app.repositories.cache_repository import cache_repository
from app.services.llm_service import llm_service

logger = logging.getLogger(__name__)
class RecruiterService:
    
    
    async def answer(
        self,
        user_id: int,
        question: str,
    ):
        logger.info(f"Получаем вакансию")
        logger.info(
            "RecruiterService.answer called\n%s",
            "".join(traceback.format_stack(limit=8)),
        )
        vacancy = await cache_repository.get_vacancy(
            user_id
        )
        logger.info(f"Вакансия: {vacancy}")
        if vacancy is None:
            return (
                "❌ Сначала загрузите ссылку "
                "на вакансию."
            )
        
        logger.info("Получаем резюме из кэша...")
        resume = await cache_repository.get_resume(
            user_id
        )
        logger.info("Резюме:")
        logger.info(resume)
        if resume is None:
            return (
                "❌ Сначала выберите резюме."
            )

        prompt = (
            SYSTEM_PROMPT
            + "\n\n"
            + build_prompt(
                vacancy=vacancy,
                resume=resume,
                question=question,
            )
        )
        logger.info("Отправляем запрос в OpenRouter...")
        return await llm_service.ask(prompt)


recruiter_service = RecruiterService()