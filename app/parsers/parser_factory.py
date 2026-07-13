from app.parsers.hh_parser import HHParser


class ParserFactory:

    @staticmethod
    def create(url: str):

        if "hh.ru" in url:
            return HHParser()

        raise ValueError(
            "Неподдерживаемый сайт вакансий."
        )