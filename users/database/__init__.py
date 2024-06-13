from typing import Optional

from sqlalchemy import Engine
from common.database import make_engine
from users.settings import UserSettingsDep

from .users_repository import UserRepository

_engine: Optional[Engine] = None


def users_db_engine(settings: UserSettingsDep) -> Engine:
    global _engine

    if not _engine:
        _engine = make_engine(settings.database_url)

    return _engine


__all__ = [
    "UserRepository",
    "users_db_engine"
]
