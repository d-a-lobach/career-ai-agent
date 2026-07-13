import logging

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.services.vacancy_service import vacancy_service
from app.telegram.keyboards import (
    main_keyboard,
    vacancy_loaded_keyboard,
)
from app.telegram.states import UserState
from app.utils.validators import validate_hh_url

logger = logging.getLogger(__name__)

router = Router()


@router.message(lambda m: m.text == "URL вакансии")
async def request_vacancy(
    message: Message,
    state: FSMContext,
):
    """
    Переход в режим ожидания ссылки на вакансию.
    """

    logger.info(
        "User %s requested vacancy input.",
        message.from_user.id,
    )

    await state.set_state(
        UserState.waiting_for_vacancy
    )

    logger.info(
        "FSM -> waiting_for_vacancy"
    )

    await message.answer(
        "🔗 Отправьте ссылку на вакансию HH.ru.",
        reply_markup=main_keyboard(),
    )


@router.message(UserState.waiting_for_vacancy)
async def save_vacancy(
    message: Message,
    state: FSMContext,
):
    """
    Получение ссылки, парсинг вакансии,
    сохранение в Redis.
    """

    user_id = message.from_user.id
    url = message.text.strip()

    logger.info(
        "Received vacancy URL from user %s: %s",
        user_id,
        url,
    )

    if not validate_hh_url(url):

        logger.warning(
            "Invalid HH URL: %s",
            url,
        )

        await message.answer(
            "❌ Некорректная ссылка.\n"
            "Отправьте ссылку на вакансию HH.ru."
        )

        return

    try:

        logger.info(
            "Start parsing vacancy..."
        )

        vacancy = await vacancy_service.load(
            user_id=user_id,
            url=url,
        )

        logger.info(
            "Vacancy parsed successfully."
        )

        logger.info(
            "Title: %s",
            vacancy.title,
        )

        await state.clear()

        logger.info(
            "FSM cleared."
        )

        await message.answer(
            (
                "✅ Вакансия успешно загружена.\n\n"
                f"<b>{vacancy.title}</b>\n\n"
                "Теперь выберите резюме."
            ),
            reply_markup=vacancy_loaded_keyboard(),
        )

        logger.info(
            "Vacancy confirmation sent."
        )

    except Exception:

        logger.exception(
            "Failed to load vacancy."
        )

        await message.answer(
            "❌ Не удалось загрузить вакансию.\n"
            "Проверьте ссылку и попробуйте снова.",
            reply_markup=main_keyboard(),
        )