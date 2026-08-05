from .database import Base, get_db, engine
from . import models

Base.metadata.create_all(engine)