from peewee import *
from config import db_path
import os

# joins the database path and database so it goes to the right folder I think
# then establishes a sqlite database with that path
db_path = os.path.join('database', db_path)
db = SqliteDatabase(db_path)

# I don't understand these. Custom exceptions? Why pass?
class DatabaseError(Exception):
    pass

# This makes it so the models can all use the meta class which links them to the database
class BaseModel(Model):
    class Meta:
        database = db

class Artist(BaseModel):
    # AutoField assigns a more usable ID I think?
    # I know the name and email have to be unique and have a max length, unsure of
    # what other constraints or their syntax
    artist_id = AutoField(primary_key=True, null=False)
    name = CharField(unique=True, max_length=70, null=False)
    email = CharField(unique=True, max_length=100, null=False)

    def __str__(self):
        return f'ID: {self.artist_id}, Artist: {self.name}, Email: {self.email}'

class Artwork(BaseModel):
    # tried to use the foreign key like described in the documentation
    # but I don't really know if it worked, because sqlite didn't throw any exceptions.
    # so I'd have to validate a new artwork's artist ID using a search beforehand.
    artwork_id = AutoField(primary_key=True, null=False)
    artist_id = ForeignKeyField(Artist, backref='test', null=False)
    # realizing the default would only go off if it were Null, but I don't think
    # an empty string would count for that, so it's not going off
    artwork_name = CharField(max_length=100, default='Untitled', null=False)
    price = FloatField(constraints=[Check('price > 0.0')])
    availability = BooleanField()

    def __str__(self):
        availability = 'Available' if self.availability else 'Unavailable'
        return f'Artwork ID: {self.artwork_id}, Artist ID: {self.artist_id}, \
Artwork title: {self.artwork_name}, Price: {self.price}, Availability: {self.availability}'

def db_initialize():
    db.connect()
    db.create_tables([Artist, Artwork])