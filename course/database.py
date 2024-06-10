from typing import Any, Generator, Optional

from sqlalchemy import Engine, create_engine
from sanctumlabs_dbkit.sql import SessionLocal
from sanctumlabs_dbkit.sql.session import Session

_engine: Optional[Engine] = None


def make_engine(database_url: str) -> Engine:
    return create_engine(database_url)


def db_engine(database_url: str) -> Engine:
    global _engine

    if not _engine:
        _engine = make_engine(database_url)

    return _engine


def db_session(engine: Engine) -> Generator[Session, Any, None]:
    with SessionLocal(bind=engine) as session:
        yield session

