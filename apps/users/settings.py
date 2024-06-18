"""
User application settings
"""
from typing import Annotated
from functools import lru_cache

from fastapi import Depends
from typing import Optional
from common.settings import CommonSettings

class UserAppSettings(CommonSettings):
    service_name: str = "users-api-service"

    db_engine: Optional[str] = "postgresql"
    db_host: Optional[str] = "localhost"
    db_port: Optional[str] = "5432"
    db_user: Optional[str] = "coursehub-users"
    db_password: Optional[str] = "coursehub-users"
    db_name: Optional[str] = "coursehub-users-db"

    @property
    def database_url(self) -> str:
        return f"{self.db_engine}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

@lru_cache
def get_user_settings() -> UserAppSettings:
    return UserAppSettings()


UserSettingsDep = Annotated[UserAppSettings, Depends(get_user_settings)]
