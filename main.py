from db_initial import db_initialize
from db_contact import *
import ui


def main():
    db_initialize()

    menu_selection = ''
    while menu_selection.lower() != 'q':
        menu_selection = ui.display_menu()

        if menu_selection == '1':
            artist_name = ui.get_artist_name()
            artist_email = ui.get_artist_email()
            response = add_artist((artist_name, artist_email))
            ui.message(response)
        elif menu_selection == '2':
            artwork_data = ui.get_artwork_info()
            response = add_artwork(artwork_data)
            ui.message(response)
        elif menu_selection == '3':
            data = select_artists()
            ui.display_artists(data)
        elif menu_selection == '4':
            artist_id = ui.get_artist_id()
            data = select_artworks(artist_id)
            ui.display_artworks(data)
        # elif menu_selection == '5':
            
    ui.quit()


# def display_artwork():

# def search_artist_work():

# def show_all_available():

# def add_artwork():

# def delete_artwork():

# def update_availability():

main()