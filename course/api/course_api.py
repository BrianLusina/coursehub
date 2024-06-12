from fastapi import APIRouter
from course.di import CourseRepositoryDep


course_router = APIRouter(prefix="/api/course")


@course_router.get('/')
def courses(course_repository: CourseRepositoryDep):
    courses = course_repository.find_all()
    data = []
    for course in courses:
        data.append(course.toDict())
    return data
