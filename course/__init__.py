from sanctumlabs_dbkit.sql import SessionLocal
from .database.database import make_engine
from .settings import Settings

def bootstrap(settings: Settings) -> None:
    # init_sentry(settings)

    SessionLocal.configure(bind=make_engine(settings.database_url))

    # configure_logging(settings)
    # configure_caching(settings)
