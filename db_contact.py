from peewee import *
from config import db_path
import os
from db_initial import Artist, Artwork

db_path = os.path.join('database', db_path)
db = SqliteDatabase(db_path)

def add_artist(data):
    artist = Artist(name=data[0], email=data[1])
    try:
        artist.save()
        return 'Artist added'
    except IntegrityError:
        return('That artist is already entered.')


def add_artwork(data):
    artwork = Artwork(artist_id=data[0], artwork_name=data[1], price=data[2], availability=data[3])
    try:
        artwork.save()
        return 'Artwork added'
    except IntegrityError as err:
        return(f'Unable to add artwork: {err}')


def select_artists():
    artists = Artist.select()
    return artists

def select_artworks(given_id):
    artworks = Artwork.select().where(Artwork.artist_id == given_id)
    return artworks

def select_available_artworks(given_id):
    artworks = Artwork.select().where(Artwork.artist_id == given_id and Artwork.availability == 1)
    return artworks