
def display_menu():
    print('''
    1. Add artist
    2. Display artists
    3. Display artist's works
    4. Display artist's available works
    5. Add artwork
    6. Delete artwork
    7. Change artwork availability
    Q. Quit program
    ''')

    return(input("Enter selection: "))

def display_artists(data):
    for x in data:
        print(x)

def message(message_text):
    print(message_text)

def quit():
    print("Ending program!")