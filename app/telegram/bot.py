from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.config.settings import settings

bot = Bot(
    token=settings.telegram_token,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
    ),
)