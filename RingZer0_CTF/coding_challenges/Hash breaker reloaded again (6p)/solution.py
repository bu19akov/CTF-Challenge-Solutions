from requests import get
import requests
from bs4 import BeautifulSoup
import re

# The URL of the challenge
url = "http://challenges.ringzer0team.com:10159"

# The URL to send the response to
response_url_template = "http://challenges.ringzer0team.com:10159/?r={}"

# Start a session to persist cookies and headers
session = requests.Session()

def extract_flag(page_content):
    """
    This function extracts the FLAG from the HTML content using BeautifulSoup.
    """
    soup = BeautifulSoup(page_content, 'html.parser')
    message_div = soup.find('div', class_='alert alert-info')
    if message_div:
        message = message_div.get_text(strip=True)
        return message
    return None

def main():
    print('Getting hash from challenge webpage...')
    html = get(url).text
    match = re.search(r'----- BEGIN HASH -----(.*)----- END HASH -----', html, re.DOTALL | re.S)
    if match:
        # Clean the matched hash value by removing <br> tags
        message = re.sub(r'<br\s*/?>', '', match.group(1).strip()).strip()
    print('Hash is: %s' % message)

    f = open("hashes/" + message[:4])
    lines = f.read().splitlines()
    answer = ""
    for line in lines:
        if re.search(message, line):
            answer = line.split(',')[0]    

    if len(answer) > 0:
        # Submit the answer
        print("Answer: ", answer)
        print('Submitting answer to challenge page...')
        response_url = response_url_template.format(answer)
        response = session.get(response_url)
        print(extract_flag(response.content.decode('utf-8')))
    else:
        print("No answer")

if __name__ == '__main__':
    main()