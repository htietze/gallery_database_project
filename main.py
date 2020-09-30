from db_initial import db_initialize
from db_contact import *
import ui


def main():
    db_initialize()

    menu_selection = ''
    while menu_selection.lower() != 'q':
        menu_selection = ui.display_menu()

        if menu_selection == '1':
            add_artist()
        elif menu_selection == '2':
            data = display_artists()
            ui.display_artists(data)
        else:
            ui.message('This is not an available selection, try again.')
        

    ui.quit()


# def display_artwork():

# def search_artist_work():

# def show_all_available():

# def add_artwork():

# def delete_artwork():

# def update_availability():

main()