"""
Application settings
"""
from typing import Annotated
from functools import lru_cache

from fastapi import Depends
from common.settings import CommonSettings, DatabaseSettings

class CourseAppSettings(CommonSettings):
    service_name: str = "course-api-service"

    database: DatabaseSettings = DatabaseSettings(
        db_name = "coursesdb"
    )

@lru_cache
def get_course_app_settings() -> CourseAppSettings:
    return CourseAppSettings()


CourseAppSettingsDep = Annotated[CourseAppSettings, Depends(get_course_app_settings)]
