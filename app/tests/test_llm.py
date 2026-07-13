import pytest

from app.llm.models import ChatMessage
from app.llm.openrouter import openrouter


@pytest.mark.asyncio
async def test_llm():

    result = await openrouter.chat(
        [
            ChatMessage(
                role="user",
                content="Ответь одним словом: OK"
            )
        ]
    )

    assert isinstance(result, str)