import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.telegram.keyboards import main_keyboard

logger = logging.getLogger(__name__)

router = Router()


@router.message(CommandStart())
async def start_handler(
    message: Message,
    state: FSMContext,
):
    """
    Команда /start.
    Сбрасывает текущее состояние пользователя
    и показывает главное меню.
    """

    logger.info(
        "User %s started bot.",
        message.from_user.id,
    )

    # Сбрасываем текущее состояние FSM
    await state.clear()

    await message.answer(
        (
            "👋 Добро пожаловать!\n\n"
            "Я помогу отвечать на вопросы AI-рекрутеров.\n\n"
            "Для начала:\n"
            "1️⃣ Загрузите URL вакансии\n"
            "2️⃣ Выберите резюме\n"
            "3️⃣ Задавайте вопросы рекрутера\n"
        ),
        reply_markup=main_keyboard(),
    )

    logger.info(
        "Main menu sent to user %s.",
        message.from_user.id,
    )


@router.message(lambda m: m.text == "Главное меню")
async def main_menu_handler(
    message: Message,
    state: FSMContext,
):
    """
    Возврат в главное меню.
    """

    logger.info(
        "User %s returned to main menu.",
        message.from_user.id,
    )

    # Выходим из любого режима (ввод вакансии, выбор резюме и т.д.)
    await state.clear()

    await message.answer(
        "🏠 Главное меню.\nВыберите действие:",
        reply_markup=main_keyboard(),
    )

    logger.info(
        "Main menu displayed for user %s.",
        message.from_user.id,
    )