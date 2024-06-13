from sanctumlabs_dbkit.sql import SessionLocal
from common.database import make_engine
from .settings import UserAppSettings

def bootstrap(settings: UserAppSettings) -> None:
    # init_sentry(settings)

    SessionLocal.configure(bind=make_engine(settings.database_url))

    # configure_logging(settings)
    # configure_caching(settings)
