"""
Application settings
"""
from typing import Annotated
from functools import lru_cache

from fastapi import Depends
from typing import Optional, AnyStr
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env: str = "local"
    service_name: str = "course-api-service"

    db_engine: Optional[str] = "postgresql"
    db_host: Optional[str] = "course-db"
    db_port: Optional[str] = "5432"
    db_user: Optional[str] = "course"
    db_password: Optional[str] = "course"
    db_name: Optional[str] = "coursedb"
    log_sql_statements: bool = False

    log_level_threshold: str = "INFO"
    log_format: str = "json"  # "json", "verbose"
    
    api_docs_enabled: bool = True

    @property
    def database_url(self) -> str:
        return f"{self.db_engine}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

@lru_cache
def get_settings() -> Settings:
    return Settings()


SettingsDep = Annotated[Settings, Depends(get_settings)]
