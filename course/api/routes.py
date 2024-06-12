from fastapi import APIRouter

from course.api.course_api import course_router
from course.api.monitoring_routes import monitoring_router


router = APIRouter()

router.include_router(course_router)
router.include_router(monitoring_router)