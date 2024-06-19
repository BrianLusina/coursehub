from fastapi import APIRouter

from apps.users.api.user_api import user_router
from apps.users.api.monitoring_routes import monitoring_router


router = APIRouter()

router.include_router(user_router)
router.include_router(monitoring_router)