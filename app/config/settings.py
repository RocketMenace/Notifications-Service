from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",
    )

    # Project metadata
    project_name: str = Field(default="Jobsites Integration Platform")
    version: str = Field(default="0.1.0")
    debug: bool = Field(default=True)

    # Database configuration
    postgres_db: str = Field(default="jobsites_integration", alias="POSTGRES_DB")
    postgres_user: str = Field(default="postgres", alias="POSTGRES_USER")
    postgres_password: str = Field(default="postgres", alias="POSTGRES_PASSWORD")
    postgres_host: str = Field(default="postgres", alias="POSTGRES_HOST")
    postgres_port: str = Field(default="5432", alias="POSTGRES_PORT")

    # Database connection pool settings
    db_pool_size: str = Field(default="5", alias="DB_POOL_SIZE")
    db_max_overflow: str = Field(default="10", alias="DB_MAX_OVERFLOW")
    db_pool_timeout: str = Field(default="30", alias="DB_POOL_TIMEOUT")
    db_url: str = Field(default="", alias="DATABASE_URL")

    # Application settings
    app_port: str = Field(default="8000", alias="APP_PORT")

    # Logging
    log_level: str = Field(default="INFO")


settings = Settings()
