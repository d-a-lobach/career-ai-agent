import logging

from aiogram import Dispatcher

from app.telegram.handlers.question import router as question_router
from app.telegram.handlers.resume import router as resume_router
from app.telegram.handlers.start import router as start_router
from app.telegram.handlers.vacancy import router as vacancy_router

logger = logging.getLogger(__name__)


def setup_router(dp: Dispatcher) -> None:
    """
    Регистрация всех роутеров приложения.
    Порядок подключения имеет значение.
    """

    logger.info("Registering Telegram routers...")

    dp.include_router(start_router)
    logger.info("✓ start_router registered")

    dp.include_router(vacancy_router)
    logger.info("✓ vacancy_router registered")

    dp.include_router(resume_router)
    logger.info("✓ resume_router registered")

    dp.include_router(question_router)
    logger.info("✓ question_router registered")

    logger.info("All routers registered successfully.")