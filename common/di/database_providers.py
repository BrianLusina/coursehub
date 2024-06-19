from typing import Any, Generator, Annotated

from fastapi import Depends

from sqlalchemy import Engine
from sanctumlabs_dbkit.sql import SessionLocal
from sanctumlabs_dbkit.sql.session import Session

from common.database import db_engine


DBEngineDep = Annotated[Engine, Depends(db_engine)]


def db_session(engine: DBEngineDep) -> Generator[Session, Any, None]:
    with SessionLocal(bind=engine) as session:
        yield session


DBSessionDep = Annotated[Session, Depends(db_session)]
