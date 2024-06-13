from fastapi import APIRouter

from users.api.user_api import user_router
from users.api.monitoring_routes import monitoring_router


router = APIRouter()

router.include_router(user_router)
router.include_router(monitoring_router)