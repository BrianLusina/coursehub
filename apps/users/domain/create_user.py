from typing import Annotated
from dataclasses import dataclass

from pydantic import EmailStr, StringConstraints
import bcrypt

from apps.users.di.repository_providers import UserRepositoryDep
from shared.domain.usecase import UseCase
from .entities import User


@dataclass(frozen=True)
class CreateUserRequest:
    email: EmailStr
    name: str
    password: Annotated[str, StringConstraints(min_length=8)]
    
    @property
    def hashed_password(self) -> str:
        """
        Return a BCrypt hash of the user's password.
        """

        # Core does not support the newer 2b variant of BCrypt. We therefore explicitly force the prefix to 2a.
        # This implementation is a copy of that from hello-yoco's `BCryptPasswordHasher`.
        salt = bcrypt.gensalt()

        password_as_bytes = self.password.encode("utf-8")

        return bcrypt.hashpw(password_as_bytes, salt).decode("utf-8")


class CreateUser(UseCase):
    """
    Create user is a use case that handles creating a new user
    """
    
    def __init__(self, user_repository: UserRepositoryDep) -> None:
        self.user_repository = user_repository
    
    async def execute(self, request: CreateUserRequest) -> User | None:
        try:
            user = User(
                name=request.name,
                email=request.email,
                password=request.hashed_password
            )
            created_user = await self.user_repository.create(user)
            return created_user
        except Exception as exc:
            raise exc
