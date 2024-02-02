import requests
from urllib.parse import quote

base_url = "http://challenges.ringzer0ctf.com:10303/api/quotes/"

headers = {
    'Content-Type': 'application/json'
}

for i in range(256):
    char = chr(i)
    encoded_char = quote(char)  # URL encode the character
    url = f"{base_url}{encoded_char}"
    response = requests.get(url, headers=headers)
    print(f"Character: {char}, Response: {response.text}")