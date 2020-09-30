from peewee import *
from config import db_path
import os
from db_initial import Artist, Artwork

db_path = os.path.join('database', db_path)
db = SqliteDatabase(db_path)

def add_artist():
    db.connect()
    test = Artist(name='test', email='test@test.com')
    try:
        test.save()
    except IntegrityError:
        print('That artist is already entered.')