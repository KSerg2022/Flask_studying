from peewee import *
from app.base_model import BaseModel
from app.auth.models import UserAuth


class Country(BaseModel):
    code = CharField(max_length=2, unique=True, index=True)
    name = CharField(max_length=100, unique=True, index=True)


class Capital(BaseModel):
    name = CharField(max_length=150, unique=True, index=True)
    country = ForeignKeyField(Country, backref='capital')


class City(BaseModel):
    name = CharField(max_length=100, unique=True, index=True)
    country = ForeignKeyField(Country, backref='city')


class UserCities(BaseModel):
    user_id = ForeignKeyField(UserAuth, backref='user_city')
    city_id = ForeignKeyField(City, backref='user_city')
