from course.di.repository_providers import CourseRepositoryDep
from course.di.database_providers import DBSessionDep

__all__ = [
    "CourseRepositoryDep",
    "DBSessionDep"
]
