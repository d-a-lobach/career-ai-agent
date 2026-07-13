from aiogram.fsm.state import State
from aiogram.fsm.state import StatesGroup


class UserState(StatesGroup):
    """
    FSM-состояния пользователя.
    """

    # Ожидание ввода ссылки на вакансию
    waiting_for_vacancy = State()

    # Ожидание выбора резюме
    waiting_for_resume = State()

    # Режим диалога с ИИ-рекрутером
    # После каждого ответа состояние НЕ очищается,
    # чтобы пользователь мог задавать несколько вопросов подряд.
    waiting_for_question = State()