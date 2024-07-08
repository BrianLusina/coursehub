"""
User application settings
"""
from typing import Annotated
from functools import lru_cache

from fastapi import Depends
from common.settings import CommonSettings, DatabaseSettings

class UserAppSettings(CommonSettings):
    service_name: str = "users-api-service"
    
    database: DatabaseSettings = DatabaseSettings(
        db_name = "usersdb"
    )

@lru_cache
def get_user_settings() -> UserAppSettings:
    return UserAppSettings()


UserSettingsDep = Annotated[UserAppSettings, Depends(get_user_settings)]
