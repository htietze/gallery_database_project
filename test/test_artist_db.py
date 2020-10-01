from peewee import *
import unittest
from unittest import TestCase
import os
from db_initial import Artist, Artwork
import db_contact
from config import test_db_path

test_db_path = os.path.join('database', test_db_path)
db = SqliteDatabase(test_db_path)

db.connect()
db.create_tables([Artist, Artwork])

class TestArtworkDB(TestCase):
        
    def test_add_artist(self):
        test_artist = ('test', 'test@email')
        db_contact.add_artist(test_artist)
        artist = Artist.select().where(Artist.artist_name == 'test')
        self.assertEqual(Artist.artist_name, 'test')
        



    # def test_add_artwork(self):

    # def test_select_artists(self):

    # def test_select_artworks(self):

    # def test_select_available_artworks(self):



if __name__ == '__main__':
    unittest.main()