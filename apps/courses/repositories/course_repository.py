from typing import Sequence

from sanctumlabs_dbkit.sql.repository import Repository
from sanctumlabs_dbkit.sql.session import Session

from .models import Course

class CourseRepository(Repository[Course]):

    def __init__(self, session: Session):
        super().__init__(model=Course, session=session)

    def find_all(self) -> Sequence[Course]:
        return self.all()
