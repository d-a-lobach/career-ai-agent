from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup


def main_keyboard() -> ReplyKeyboardMarkup:
    """
    Главное меню (/start)
    """
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="URL вакансии"),
            ],
            [
                KeyboardButton(text="Выбрать резюме"),
            ],
            [
                KeyboardButton(text="Задать вопрос"),
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие...",
    )


def vacancy_loaded_keyboard() -> ReplyKeyboardMarkup:
    """
    После успешной загрузки вакансии.
    """
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Выбрать резюме"),
            ],
            [
                KeyboardButton(text="Задать вопрос"),
            ],
            [
                KeyboardButton(text="Главное меню"),
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие...",
    )


def resume_selected_keyboard() -> ReplyKeyboardMarkup:
    """
    После выбора резюме.
    """
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Задать вопрос"),
            ],
            [
                KeyboardButton(text="URL вакансии"),
                KeyboardButton(text="Выбрать резюме"),
            ],
            [
                KeyboardButton(text="Главное меню"),
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder="Введите вопрос или выберите действие...",
    )