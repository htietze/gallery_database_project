from peewee import *
from config import db_path
import os
from db_initial import Artist, Artwork

def add_artist(data):
    artist = Artist(name=data[0], email=data[1])
    try:
        artist.save()
        return 'Artist added'
    except IntegrityError:
        # I don't understand why I can't raise the custom pass exception without the
        # program just ending and the test needs it to be raised as opposed to excepted?
        raise DatabaseError
        # return('That artist is already entered.')

def add_artwork(data):
    artwork = Artwork(artist_id=data[0], artwork_name=data[1], price=data[2], availability=data[3])
    try:
        artwork.save()
        return 'Artwork added'
    except IntegrityError as err:
        # return(f'Unable to add artwork: {err}')
        raise DatabaseError

def select_artists():
    artists = Artist.select()
    return artists

def select_artworks(given_id):
    artworks = Artwork.select().where(Artwork.artist_id == given_id)
    return artworks

def select_available_artworks(given_id):
    artworks = Artwork.select().where(Artwork.artist_id == given_id and Artwork.availability == 1)
    return artworks