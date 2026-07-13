import pytest

from app.parsers.parser_factory import ParserFactory


@pytest.mark.asyncio
async def test_hh_parser_factory():

    parser = ParserFactory.create(
        "https://hh.ru/vacancy/123456"
    )

    assert parser is not None


def test_unknown_parser():

    with pytest.raises(ValueError):
        ParserFactory.create(
            "https://google.com"
        )