from marshmallow import Schema, fields
from setup_db import db

class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
'''Создаем модель БД для объекта Режиссер'''

class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
'''Создаем схему сериализации для работы с json'''