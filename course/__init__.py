from sanctumlabs_dbkit.sql import SessionLocal
from .database import make_engine
import os

def bootstrap(database_url: str) -> None:
    # init_sentry(settings)

    SessionLocal.configure(bind=make_engine(database_url))

    # configure_logging(settings)
    # configure_caching(settings)
