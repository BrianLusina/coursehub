from fastapi import APIRouter
from sqlalchemy import text

from common.di.database_providers import DBSessionDep

monitoring_router = APIRouter(tags=["monitoring"])


@monitoring_router.get("/healthz")
def healthz(session: DBSessionDep):
    session.execute(text("SELECT 1"))

    return dict(status=200, message="ok")
