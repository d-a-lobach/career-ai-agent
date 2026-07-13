from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Telegram
    telegram_token: str = Field(alias="TELEGRAM_TOKEN")

    # OpenRouter
    openrouter_api_key: str = Field(alias="OPENROUTER_API_KEY")
    openrouter_model: str = Field(
        default="openai/gpt-oss-20b:free",
        alias="OPENROUTER_MODEL",
    )
    openrouter_base_url: str = Field(
        default="https://openrouter.ai/api/v1",
        alias="OPENROUTER_BASE_URL",
    )

    # Redis
    redis_url: str = Field(
        default="redis://redis:6379/0",
        alias="REDIS_URL",
    )

    # LLM Retry
    llm_max_retries: int = Field(
        default=5,
        alias="LLM_MAX_RETRIES",
    )

    llm_retry_delay: float = Field(
        default=2.0,
        alias="LLM_RETRY_DELAY",
    )

    # Cache
    vacancy_cache_ttl: int = Field(
        default=86400,
        alias="VACANCY_CACHE_TTL",
    )

    resume_cache_ttl: int = Field(
        default=86400,
        alias="RESUME_CACHE_TTL",
    )

    # Logging
    log_level: str = Field(
        default="INFO",
        alias="LOG_LEVEL",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()