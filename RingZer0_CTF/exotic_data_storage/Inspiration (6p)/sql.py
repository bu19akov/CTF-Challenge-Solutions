import requests
from urllib.parse import quote

base_url = "http://challenges.ringzer0ctf.com:10303/api/quotes/"

headers = {
    'Content-Type': 'application/json'
}

string = """PLACE FOR QUERY"""
encoded_string = quote(string)  # URL encode the character
url = f"{base_url}{encoded_string}"
response = requests.get(url, headers=headers)
print(f"Response: {response.text}")

