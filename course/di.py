
from flask_injector import singleton, Binder
from .repository import CourseRepository
from sanctumlabs_dbkit.sql.session import Session

# Dependency configurations
def configure(binder: Binder):
    binder.bind(Session, to=Session())
    binder.bind(CourseRepository, to=CourseRepository(Session()), scope=singleton)
    # binder.bind(Logger, to=Logger(), scope=singleton)
    # binder.bind(DataService, to=DataService(Database(), Logger()), scope=singleton)
