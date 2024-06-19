from typing import Annotated
from fastapi import Depends

from apps.users.domain import CreateUser
from apps.users.di.repository_providers import UserRepositoryDep


def create_user_dep(user_repo: UserRepositoryDep) -> CreateUser:
    return CreateUser(user_repo)


CreateUserDep = Annotated[
    CreateUser, Depends(create_user_dep)
]
