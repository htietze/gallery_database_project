import unittest
from unittest import TestCase
from peewee import *

import config

import db_contact
import db_initial
from db_initial import Artist, Artwork

test_db_path = 'database/test_gallery_db.sqlite'
config.db_path = test_db_path
db = SqliteDatabase(config.db_path)

# http://docs.peewee-orm.com/en/latest/peewee/database.html
# and help from Tom to figure out getting it to connect to a test database
# how I understand it, takes the models from the true database setup
models = [Artist, Artwork]
# then those models get bound to the test database. then connects and creates tables
# from those models.
db.bind(models, bind_refs=False, bind_backrefs=False)
db.connect()
db.create_tables(models)

class TestArtworkDB(TestCase):

    # setup at the start to clear any leftover info, then teardown at the end so the database is emptied.
    def setUp(self):
        self.clear_info()

    def tearDown(self):
        self.clear_info()

    # adding artists for duplicate checks later
    def add_artists_for_testing(self):
        self.artist1 = Artist(name='Sam', email='sam@sam.test')
        self.artist2 = Artist(name='John', email='john@john.test')
        self.artwork1 = Artwork(artist_id=1, artwork_name='test artwork', price=300.00, availability=True)
        self.artwork2 = Artwork(artist_id=2, artwork_name='another artwork', price=250.99, availability=False)
        self.artist1.save()
        self.artist2.save()

    def test_add_artist_with_new_artist(self):
        # clears, goes to add the artist data, then a search to see if it was saved properly
        self.clear_info()
        db_contact.add_artist(('test', 'test@email'))
        check = Artist.select().where(Artist.name == 'test')
        self.assertEquals('test', check[0].name)

    def test_add_artist_with_duplicate_name(self):
        self.clear_info()
        self.add_artists_for_testing()
        # after the test artists are added, this add_artist() causes the assert raise,
        # which it should because that artist is there.
        with self.assertRaises(DatabaseError):
            db_contact.add_artist(('John', 'new@test.test'))

    def test_add_new_artwork(self):
        self.clear_info()
        self.add_artists_for_testing()
        db_contact.add_artwork((1, 'test artwork', 300.00, True))
        check = Artwork.select().where(Artwork.artwork_name == 'test artwork')
        self.assertEquals('test artwork', check[0].artwork_name)

    def clear_info(self):
        Artist.delete().execute()
        Artwork.delete().execute()

if __name__ == '__main__':
    unittest.main()