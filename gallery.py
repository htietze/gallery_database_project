from peewee import *

db = SqliteDatabase('gallery_db.sqlite')

class Artist(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = db

    def __str__(self):
        return False

class Artwork():
    artist_name = CharField()
    artwork_name = CharField()
    price = IntegerField()
    availability = BooleanField()

    class Meta:
        database = db

    def __str__(self):
        return False

db.connect()
db.create_tables([Artist, Artwork])

def main():

def display_artists():

def display_artwork():

def add_artist():

def search_artist_work():

def show_all_available():

def add_artwork():

def delete_artwork():

def update_availability():


