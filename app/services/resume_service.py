import logging

from app.repositories.cache_repository import cache_repository
from app.repositories.resume_repository import resume_repository

logger = logging.getLogger(__name__)


class ResumeService:

    def get_all(self):

        resumes = resume_repository.get_all()

        logger.info(
            "Returning %d resumes",
            len(resumes),
        )

        return resumes

    async def select(
        self,
        user_id: int,
        resume_id: int,
    ):

        logger.info(
            "Selecting resume. user=%s id=%s",
            user_id,
            resume_id,
        )

        resume = resume_repository.get_by_id(
            resume_id
        )

        if resume is None:

            logger.warning(
                "Resume not found."
            )

            return None

        await cache_repository.save_resume(
            user_id,
            resume.description,
        )

        logger.info(
            "Resume '%s' saved to cache.",
            resume.name,
        )

        return resume

    async def select_by_name(
        self,
        user_id: int,
        resume_name: str,
    ):

        logger.info(
            "Searching resume '%s'",
            resume_name,
        )

        resume = resume_repository.get_by_name(
            resume_name
        )

        if resume is None:

            logger.warning(
                "Resume not found."
            )

            return None

        await cache_repository.save_resume(
            user_id,
            resume.description,
        )

        logger.info(
            "Resume '%s' saved to cache.",
            resume.name,
        )

        return resume


resume_service = ResumeService()