from typing import Sequence, Optional

from sanctumlabs_dbkit.sql.repository import Repository
from sanctumlabs_dbkit.sql.session import Session

from users.domain.entities import User
from .models import UserModel

class UserRepository(Repository[UserModel]):

    def __init__(self, session: Session):
        super().__init__(model=UserModel, session=session)

    def find_all(self) -> Sequence[UserModel]:
        return self.all()

    def create(self, user: User) -> Optional[User]:
        pass
        