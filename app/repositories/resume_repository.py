import json
import logging
from pathlib import Path

from app.models.resume import Resume

logger = logging.getLogger(__name__)


class ResumeRepository:

    def __init__(
        self,
        file_path: str = "app/data/resumes.json",
    ):
        self.file_path = Path(file_path)

        logger.info(
            "ResumeRepository initialized. file=%s",
            self.file_path,
        )

    def get_all(self) -> list[Resume]:

        logger.info("Loading resumes...")

        with open(
            self.file_path,
            encoding="utf-8",
        ) as f:
            data = json.load(f)

        base_dir = self.file_path.parent

        resumes: list[Resume] = []

        for item in data:

            md_file = base_dir / item["file"]

            logger.info(
                "Loading resume '%s' from %s",
                item["name"],
                md_file,
            )

            description = md_file.read_text(
                encoding="utf-8",
            )

            resumes.append(
                Resume(
                    id=item["id"],
                    name=item["name"],
                    description=description,
                )
            )

        logger.info(
            "Loaded %d resumes",
            len(resumes),
        )

        return resumes

    def get_by_id(
        self,
        resume_id: int,
    ) -> Resume | None:

        logger.info(
            "Searching resume by id=%s",
            resume_id,
        )

        for resume in self.get_all():

            if resume.id == resume_id:

                logger.info(
                    "Resume found: %s",
                    resume.name,
                )

                return resume

        logger.warning(
            "Resume id=%s not found",
            resume_id,
        )

        return None

    def get_by_name(
        self,
        name: str,
    ) -> Resume | None:

        logger.info(
            "Searching resume by name='%s'",
            name,
        )

        for resume in self.get_all():

            if resume.name == name:

                logger.info(
                    "Resume found: id=%s",
                    resume.id,
                )

                return resume

        logger.warning(
            "Resume '%s' not found",
            name,
        )

        return None


resume_repository = ResumeRepository()