from app.telegram.keyboards import main_keyboard


def test_keyboard():

    kb = main_keyboard()

    assert kb is not None
    assert len(kb.keyboard) == 2