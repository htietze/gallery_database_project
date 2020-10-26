import ui
import db_contact

def add_artist():
    artist_name = ui.get_artist_name()
    artist_email = ui.get_artist_email()
    response = db_contact.add_artist((artist_name, artist_email))
    ui.message(response)


# plus the rest of the functions 