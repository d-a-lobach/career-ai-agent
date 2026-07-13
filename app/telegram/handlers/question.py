import logging

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.services.recruiter_service import recruiter_service
from app.telegram.keyboards import resume_selected_keyboard
from app.telegram.states import UserState

logger = logging.getLogger(__name__)

router = Router()


@router.message(lambda m: m.text == "Задать вопрос")
async def request_question(
    message: Message,
    state: FSMContext,
):
    """
    Переход в режим диалога с ИИ-рекрутером.
    После этого пользователь может задавать
    неограниченное количество вопросов подряд.
    """

    logger.info(
        "User %s entered question mode.",
        message.from_user.id,
    )

    await state.set_state(
        UserState.waiting_for_question
    )

    logger.info(
        "FSM -> waiting_for_question"
    )

    await message.answer(
        (
            "💬 Режим вопросов активирован.\n\n"
            "Введите вопрос рекрутера.\n\n"
            "Например:\n"
            "• Какие проекты были наиболее успешными?\n"
            "• Почему хотите сменить работу?\n"
            "• Какие зарплатные ожидания?"
        ),
        reply_markup=resume_selected_keyboard(),
    )


@router.message(UserState.waiting_for_question)
async def answer_question(
    message: Message,
    state: FSMContext,
):
    """
    Ответ на вопрос рекрутера.

    Состояние НЕ очищается,
    поэтому пользователь может задавать
    несколько вопросов подряд.
    """

    user_id = message.from_user.id
    question = message.text.strip()

    logger.info(
        "Question received from user %s",
        user_id,
    )

    logger.debug(
        "Question: %s",
        question,
    )

    if not question:

        logger.warning(
            "Empty question from user %s",
            user_id,
        )

        await message.answer(
            "Введите вопрос рекрутера."
        )

        return

    try:

        logger.info(
            "Sending question to RecruiterService..."
        )

        answer = await recruiter_service.answer(
            user_id=user_id,
            question=question,
        )

        logger.info(
            "Answer generated successfully."
        )

        logger.debug(
            "Answer preview: %s",
            answer[:500],
        )

        await message.answer(
            answer,
            reply_markup=resume_selected_keyboard(),
        )

        logger.info(
            "Answer sent to user %s",
            user_id,
        )

        # ВАЖНО:
        # await state.clear() НЕ вызываем.
        # Пользователь остаётся в режиме вопросов.

    except Exception:

        logger.exception(
            "Failed to generate answer."
        )

        await message.answer(
            (
                "❌ Произошла ошибка при обращении "
                "к языковой модели."
            ),
            reply_markup=resume_selected_keyboard(),
        )

@router.message()
async def debug_all(message: Message):
    logger.warning(
        "QUESTION ROUTER GOT: %r",
        message.text,
    )