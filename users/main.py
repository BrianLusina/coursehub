from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from users.api.routes import router
from users.settings import get_user_settings
from users import bootstrap

def create_user_app() -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
        # When the lifespan callback triggers, we don't get magical access to resolve dependencies from the FastAPI
        # container.  We therefore have to do a little manual foo here.  The following allows for simple dependency
        # resolution and caters for dependencies that are overridden in tests.
        # See https://github.com/tiangolo/fastapi/discussions/8208
        settings = app.dependency_overrides.get(get_user_settings, get_user_settings)()

        bootstrap(settings)

        yield

    app = FastAPI(
        title="User API",
        description="User Service to manage users",
        docs_url="/docs" if get_user_settings().api_docs_enabled else None,
        redoc_url="/redoc" if get_user_settings().api_docs_enabled else None,
        lifespan=lifespan,
    )

    app.include_router(router)
    
    return app

app = create_user_app()
