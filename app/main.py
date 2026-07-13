import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.config.settings import settings
from app.telegram.router import setup_router


async def main() -> None:
    print("MAIN STARTED")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    logger = logging.getLogger(__name__)

    logger.info("Starting application...")


    # Telegram Bot
    bot = Bot(
        token=settings.telegram_token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        ),
    )

    dp = Dispatcher()

    # Регистрация всех роутеров
    setup_router(dp)

    logger.info("Bot started")

    try:
        await dp.start_polling(bot)
    finally:
        logger.info("Stopping bot...")
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())