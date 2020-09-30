from peewee import *
from config import db_path
import os

db_path = os.path.join('database', db_path)
db = SqliteDatabase(db_path)

class Artist(Model):
    artist_id = AutoField(primary_key=True)
    name = CharField(unique=True)
    email = CharField(unique=True)

    class Meta:
        database = db

    def __str__(self):
        return "test1"

class Artwork(Model):
    artwork_id = AutoField(primary_key=True)
    artist_id = ForeignKeyField(Artist, backref='test')
    artwork_name = CharField()
    price = IntegerField()
    availability = BooleanField(choices=([True, 'Available'], [False, 'Unavailable']))

    class Meta:
        database = db

    def __str__(self):
        return "test2"

def db_initialize():
    db.connect()
    db.create_tables([Artist, Artwork])