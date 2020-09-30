from db_initial import db_initialize
from db_contact import *
import ui


def main():
    db_initialize()

    add_artist()

    data = display_artists()
    ui.display_artists(data)




# def display_artwork():

# def search_artist_work():

# def show_all_available():

# def add_artwork():

# def delete_artwork():

# def update_availability():

main()