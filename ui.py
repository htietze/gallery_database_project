import validation

def display_menu():
    print('''
    1. Add artist
    2. Add artwork
    3. Display artists
    4. Display artist's works
    5. Display artist's available works
    6. Change artwork availability
    7. Delete artwork
    Q. Quit program
    ''')

    return(input("Enter selection: "))

# UI stuff for displaying the results from database queries as well as messages to the user
def display_artists(artists):
    for artist in artists:
        print(artist)

def display_artworks(artworks):
    for x in artworks:
        print(x)

# Also includes methods for getting user input, and throws them into validation
# which I'm unsure if that's right.
def get_artist_name():
    is_valid = False
    while not is_valid:
        name = input('Please enter the artist\'s name (special characters not accepted): ')
        is_valid = validation.artist_name_validation(name)
    name = name.strip()
    return (name)

def get_artist_email():
    is_valid = False
    while not is_valid:
        email = input('Please enter the artist\'s email: ')
        is_valid = validation.artist_email_validation(email)
    email = email.strip()
    return (email)

# way too long, but I'm not sure how to split it up or do better validation here.
def get_artwork_info():
    while True:
        try:
            artist_id = int(input('Enter artist\'s ID: '))
            if artist_id <= 0:
                raise ValueError
            else:
                break
        except ValueError:
            message('Please enter a positive integer.')

    artwork_name = input('Enter artwork title: ')

    while True:
        try:
            price = float(input('Enter price: '))
            break
        except ValueError:
            message('Please enter a positive integer.')

    while True:
        availability = input('Is it available for sale? yes or no: ')
        if availability.lower() == 'yes':
            availability = True
            break
        elif availability.lower() == 'no':
            availability = False
            break
        else:
            message('Please enter yes or no.')

    data = (artist_id, artwork_name, price, availability)
    return data

def get_artist_id():
    while True:
        try:
            artist_id = int(input('Please enter artist\'s ID: '))
            return artist_id
        except ValueError as err:
            message(f'Could not proceed due to: {err}')

def message(message_text):
    print(message_text)

def quit():
    print("Ending program!")