import sqlite3
import unittest
from unittest import TestCase
from peewee import *

import config

import db_contact
import db_initial
from db_initial import Artist, Artwork

class TestArtworkDB(TestCase):

    test_db_path = 'database/test_gallery_db.sqlite'
  

    def setUp(self):
        config.db_path = self.test_db_path
        db = SqliteDatabase(self.test_db_path)
        with sqlite3.connect(self.test_db_path) as conn:
            conn.execute('DELETE FROM artist')
        conn.close()
        
    def test_add_artist(self):
        test_artist = ('test', 'test@email')
        db_contact.add_artist(test_artist)
        artist = Artist.select().where(Artist.name == 'test')
        self.assertEqual(Artist.name, 'test')
        



    # def test_add_artwork(self):

    # def test_select_artists(self):

    # def test_select_artworks(self):

    # def test_select_available_artworks(self):



if __name__ == '__main__':
    unittest.main()