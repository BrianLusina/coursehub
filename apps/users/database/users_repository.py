from typing import Sequence, Optional

from sanctumlabs_dbkit.sql.repository import Repository
from sanctumlabs_dbkit.sql.session import Session

from apps.users.domain.entities import User
from .models import Users

class UserRepository(Repository[Users]):

    def __init__(self, session: Session):
        super().__init__(model=Users, session=session)

    def find_all(self) -> Sequence[Users]:
        return self.all()

    async def create(self, user: User) -> Optional[User]:
        try:
            new_user = Users.from_user(user)
            self.session.add(new_user)
            self.session.flush()
            self.session.refresh(new_user)
            return user
        except Exception as exc:
            raise exc
