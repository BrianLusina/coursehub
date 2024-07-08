from typing import Optional

from sqlalchemy import Engine
from common.database import make_engine

from courses.settings import CourseAppSettingsDep

_engine: Optional[Engine] = None


def course_db_engine(settings: CourseAppSettingsDep) -> Engine:
    global _engine

    if not _engine:
        _engine = make_engine(settings.database.database_url)

    return _engine
