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
    artwork_name = CharField(max_length=100, default='Untitled')
    price = IntegerField(constraints=[Check('price > 0')])
    availability = BooleanField()

    class Meta:
        database = db

    def __str__(self):
        return f'Artwork ID: {self.artwork_id}, Artist ID: {self.artist_id}, \
Artwork title: {self.artwork_name}, Price: {self.price}, Availability: {self.availability}'

def db_initialize():
    db.connect()
    db.create_tables([Artist, Artwork])