from typing import Optional

from sqlalchemy import Engine, create_engine

from course.settings import SettingsDep

_engine: Optional[Engine] = None


def make_engine(database_url: str) -> Engine:
    return create_engine(database_url)


def db_engine(settings: SettingsDep) -> Engine:
    global _engine

    if not _engine:
        _engine = make_engine(settings.database_url)

    return _engine
