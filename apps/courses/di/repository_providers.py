from typing import Annotated
from fastapi import Depends

from courses.repositories import CourseRepository
from common.di.database_providers import DBSessionDep


def course_repository_dep(session: DBSessionDep) -> CourseRepository:
    return CourseRepository(session)


CourseRepositoryDep = Annotated[
    CourseRepository, Depends(course_repository_dep)
]
