import logging
import re

import httpx
from bs4 import BeautifulSoup

from app.models.vacancy import Vacancy
from app.parsers.base import BaseVacancyParser

logger = logging.getLogger(__name__)


class HHParser(BaseVacancyParser):

    async def parse(self, url: str) -> Vacancy:

        logger.info("Loading HH vacancy: %s", url)

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/138.0.0.0 Safari/537.36"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,"
                "application/xml;q=0.9,*/*;q=0.8"
            ),
            "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
            "Referer": "https://hh.ru/",
            "Cache-Control": "no-cache",
        }

        async with httpx.AsyncClient(
            headers=headers,
            timeout=30,
            follow_redirects=True,
            http2=True,
        ) as client:

            response = await client.get(url)

            logger.info(
                "HH response: %s",
                response.status_code,
            )

            response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser",
        )

        title = ""

        title_tag = soup.find("h1")

        if title_tag:
            title = title_tag.get_text(strip=True)

        company = ""

        company_tag = soup.find(
            attrs={
                "data-qa": "vacancy-company-name"
            }
        )

        if company_tag:
            company = company_tag.get_text(
                strip=True
            )

        description = ""

        block = soup.find(
            attrs={
                "data-qa": "vacancy-description"
            }
        )

        if block:
            description = block.get_text(
                "\n",
                strip=True,
            )

        description = re.sub(
            r"\n{3,}",
            "\n\n",
            description,
        )

        logger.info(
            "Vacancy parsed successfully. "
            "title='%s' company='%s' description_length=%d",
            title,
            company,
            len(description),
        )

        return Vacancy(
            url=url,
            title=title,
            company=company,
            description=description,
        )