from typing import Annotated
from fastapi import Depends

from users.database import UserRepository
from common.di.database_providers import DBSessionDep


def user_repository_dep(session: DBSessionDep) -> UserRepository:
    return UserRepository(session)


UserRepositoryDep = Annotated[
    UserRepository, Depends(user_repository_dep)
]
