from typing import Any, Generator, Annotated

from fastapi import Depends

from sqlalchemy import Engine
from sanctumlabs_dbkit.sql import SessionLocal
from sanctumlabs_dbkit.sql.session import Session

from users.database import users_db_engine


DBEngineDep = Annotated[Engine, Depends(users_db_engine)]


def users_db_session(engine: DBEngineDep) -> Generator[Session, Any, None]:
    with SessionLocal(bind=engine) as session:
        yield session


UsersDBSessionDep = Annotated[Session, Depends(users_db_session)]
