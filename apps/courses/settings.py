"""
Application settings
"""
from typing import Annotated
from functools import lru_cache

from fastapi import Depends
from typing import Optional
from common.settings import CommonSettings

class CourseAppSettings(CommonSettings):
    service_name: str = "course-api-service"

    db_engine: Optional[str] = "postgresql"
    db_host: Optional[str] = "localhost"
    db_port: Optional[str] = "5432"
    db_user: Optional[str] = "coursehub"
    db_password: Optional[str] = "coursehub"
    db_name: Optional[str] = "coursehub-db"

    @property
    def database_url(self) -> str:
        return f"{self.db_engine}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

@lru_cache
def get_course_app_settings() -> CourseAppSettings:
    return CourseAppSettings()


CourseAppSettingsDep = Annotated[CourseAppSettings, Depends(get_course_app_settings)]
