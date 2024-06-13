from typing import Sequence

from sanctumlabs_dbkit.sql.repository import Repository
from sanctumlabs_dbkit.sql.session import Session

from .models import User

class UserRepository(Repository[User]):

    def __init__(self, session: Session):
        super().__init__(model=User, session=session)

    def find_all(self) -> Sequence[User]:
        return self.all()
