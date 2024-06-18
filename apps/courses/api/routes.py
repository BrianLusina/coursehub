from fastapi import APIRouter

from courses.api.course_api import course_router
from courses.api.monitoring_routes import monitoring_router


router = APIRouter()

router.include_router(course_router)
router.include_router(monitoring_router)