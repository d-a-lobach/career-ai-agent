import logging

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup

from app.services.resume_service import resume_service
from app.telegram.keyboards import (
    main_keyboard,
    resume_selected_keyboard,
)
from app.telegram.states import UserState

logger = logging.getLogger(__name__)

router = Router()


@router.message(lambda m: m.text == "Выбрать резюме")
async def request_resume(
    message: Message,
    state: FSMContext,
):
    """
    Переход в режим выбора резюме.
    """

    logger.info(
        "User %s requested resume selection.",
        message.from_user.id,
    )

    resumes = resume_service.get_all()

    logger.info(
        "Loaded %d resumes.",
        len(resumes),
    )

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text=resume.name
                )
            ]
            for resume in resumes
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите резюме...",
    )

    await state.set_state(
        UserState.waiting_for_resume
    )

    logger.info(
        "FSM -> waiting_for_resume"
    )

    await message.answer(
        "📄 Выберите резюме:",
        reply_markup=keyboard,
    )


@router.message(UserState.waiting_for_resume)
async def save_resume(
    message: Message,
    state: FSMContext,
):
    """
    Пользователь выбрал резюме.
    """

    user_id = message.from_user.id
    resume_name = message.text.strip()

    logger.info(
        "User %s selected '%s'.",
        user_id,
        resume_name,
    )

    try:

        resume = await resume_service.select_by_name(
            user_id=user_id,
            resume_name=resume_name,
        )

        if resume is None:

            logger.warning(
                "Resume '%s' not found.",
                resume_name,
            )

            await message.answer(
                "❌ Резюме не найдено.\n"
                "Выберите одно из списка."
            )

            return

        logger.info(
            "Resume '%s' selected successfully.",
            resume.name,
        )

        await state.clear()

        logger.info(
            "FSM cleared."
        )

        await message.answer(
            (
                "✅ Резюме выбрано.\n\n"
                f"<b>{resume.name}</b>\n\n"
                "Теперь можете задавать вопросы рекрутера."
            ),
            reply_markup=resume_selected_keyboard(),
        )

        logger.info(
            "Resume confirmation sent."
        )

    except Exception:

        logger.exception(
            "Failed to select resume."
        )

        await state.clear()

        await message.answer(
            "❌ Ошибка при выборе резюме.",
            reply_markup=main_keyboard(),
        )