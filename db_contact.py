from peewee import *
from config import db_path
import os
from db_initial import Artist, Artwork

db_path = os.path.join('database', db_path)
db = SqliteDatabase(db_path)

def add_artist(data):
    print(data[0])
    print(data[1])
    test = Artist(name=data[0], email=data[1])
    try:
        test.save()
        return 'Artist added'
    except IntegrityError:
        return('That artist is already entered.')


def add_artwork():
    test = Artwork(artist_id=1, artwork_name='Test', price='500', availability='Available')
    try:
        test.save()
        return 'Artwork added'
    except IntegrityError as err:
        return(f'Unable to add artwork: {err}')


def select_artists():
    artists = Artist.select()
    return artists

def select_artworks(test):
    artworks = Artwork.select().where(Artwork.artist_id == test)
    return artworks