"""
Common settings
"""
from typing import Annotated
from functools import lru_cache

from fastapi import Depends
from typing import Optional
from pydantic_settings import BaseSettings


# pylint: disable=too-few-public-methods
class DatabaseSettings(BaseSettings):
    """
    Database Settings
    """
    db_engine: Optional[str] = "postgresql"

    db_host: str = "localhost"
    db_port: int = 5432

    db_name: str = "coursehub"
    
    db_user: Optional[str] = "coursehub"
    db_password: Optional[str] = "coursehub"

    db_dialect: str = "postgresql"
    db_driver: str = "psycopg2"
    db_logging_enabled: bool = False
    db_log_level: str = "INFO"
    
    log_sql_statements: bool = False
    
    db_url: Optional[str] = f'{db_dialect}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

    @property
    def database_url(self) -> str:
        return f"{self.db_engine}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

class CommonSettings(BaseSettings):
    app_env: str = "local"
    service_name: str = "api-service"
    
    database: DatabaseSettings = DatabaseSettings()

    log_sql_statements: bool = False

    log_level_threshold: str = "INFO"
    log_format: str = "json"  # "json", "verbose"
    
    api_docs_enabled: bool = True

    @property
    def database_url(self) -> str:
        return f"{self.db_engine}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

@lru_cache
def get_settings() -> CommonSettings:
    return CommonSettings()


CommonSettingsDep = Annotated[CommonSettings, Depends(get_settings)]
