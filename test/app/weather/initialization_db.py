from peewee import SqliteDatabase


from app.handlers.get_path_to_db import get_path_to_db
from app.base_model import database_proxy
from app.weather.models import Country, City, Capital


def initialization_db():
    """Convert data from json file to db"""
    path_to_db = get_path_to_db()
    try:
        db = SqliteDatabase(path_to_db)
        database_proxy.initialize(db)
        db.create_tables([Country, City, Capital])
    except None:
        pass
    return True


print(get_path_to_db())
print(initialization_db())
