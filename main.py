from db_initial import db_initialize
from db_contact import *
import ui
import controller

'''
Hey Professor, I guess I just want to preface with saying I didn't understand what I should've been
doing. Or how most of this works. This is the first time that I've just totally crashed on a project.
I honestly wasn't sure how to split my modules, how to get importing to work too. I'm not sure where 
to put validation, or really how to effectively do validation this time. And I don't think I would've
ever figured out how to get peewee to make a test database without the help I got. I kind of hate peewee?
Could make excuses about this and that, but doesn't change stuff. Going forward I know I need to read 
more and watch more, but if there were other ways to practice on smaller examples, I would really 
appreciate those. I will try to comment the parts I understand best I can.
'''

def main():
    db_initialize()

    # basic menu I think, I'm not sure if I should've put validation here or elsewhere.
    menu_selection = ''
    while menu_selection.lower() != 'q':
        menu_selection = ui.display_menu()

        if menu_selection == '1':
            # selection 1 goes to the UI to get info from the user
            # then puts those together to add the artist, taking the response
            # and sending it to be displayed.
            controller.add_artist()
        elif menu_selection == '2':
            # adding artwork does much the same, requests info and then attemps to add
            # if it's successful, the response gives an ok.
            # move these into a function in the controller module
            artwork_data = ui.get_artwork_info()
            response = add_artwork(artwork_data)
            ui.message(response)     
        elif menu_selection == '3':
            # move these into a function in the controller module
            data = select_artists()
            ui.display_artists(data)
        elif menu_selection == '4':
            # move these into a function in the controller module
            artist_id = ui.get_artist_id()
            data = select_artworks(artist_id)
            ui.display_artworks(data)
        # elif menu_selection == '5':
            
    ui.quit()

main()