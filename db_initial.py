from peewee import *
from config import db_path
import os

db_path = os.path.join('database', db_path)
db = SqliteDatabase(db_path)

class Artist(Model):
    artist_id = AutoField(primary_key=True)
    name = CharField(unique=True, max_length=70)
    email = CharField(unique=True, max_length=100)

    class Meta:
        database = db

    def __str__(self):
        return f'ID: {self.artist_id}, Artist: {self.name}, Email: {self.email}'

class Artwork(Model):
    artwork_id = AutoField(primary_key=True)
    artist_id = ForeignKeyField(Artist, backref='test')
    artwork_name = CharField(max_length=100)
    price = IntegerField(constraints=[Check('price > 0')])
    availability = CharField(choices=((True, 'Available'),(False, 'Unavailable')))

    class Meta:
        database = db

    def __str__(self):
        return "test2"

def db_initialize():
    db.connect()
    db.create_tables([Artist, Artwork])