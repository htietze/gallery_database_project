import re

name_pattern = '^[a-zA-Z0-9 ]+$'
email_pattern = '^[a-zA-Z0-9_@.]+$'

# This feels almost useless? Checking the input name and email against some regex patterns
def artist_name_validation(name):
    if name.strip() == '':
        return False
    else:
        name_status = re.match(f'{name_pattern}', name)
        return name_status

def artist_email_validation(email):
    if email.strip() == '':
        return False
    else:
        email_status = re.match(f'{email_pattern}', email)
        return email_status