import requests
import base64
from string import printable
import re
from bs4 import BeautifulSoup

# The URL of the challenge
challenge_url = "http://challenges.ringzer0team.com:10016"

# The URL to send the response to
response_url_template = "http://challenges.ringzer0team.com:10016/?r={}"

# Start a session to persist cookies and headers
session = requests.Session()

def extract_key_and_message(page_content):
    match_key = re.search(r'----- BEGIN XOR KEY -----(.*)----- END XOR KEY -----', page_content, re.DOTALL | re.S)
    match_message = re.search(r'----- BEGIN CRYPTED MESSAGE -----(.*)----- END CRYPTED MESSAGE -----', page_content, re.DOTALL | re.S)
    if match_key and match_message:
        key = re.sub(r'<br\s*/?>', '', match_key.group(1).strip()).strip()
        message = re.sub(r'<br\s*/?>', '', match_message.group(1).strip()).strip()
        return key, message
    return None

def xor_message(key, message):
    # Decode the base64 encoded message
    decoded_message = base64.b64decode(message)

    # Iterate over the key in 10-character sliding windows
    for i in range(len(key) - 9):
        current_key = key[i:i+10]

        # XOR the message with the current key
        xored_result = ''.join(chr(byte ^ ord(current_key[i % len(current_key)])) for i, byte in enumerate(decoded_message))

        # Check if the result contains only printable characters
        if all(char in printable for char in xored_result):
            print("Decoded message with key '{}': {}".format(current_key, xored_result))
            return xored_result

    return None
    

def send_response(response):
    """
    This function sends the response back to the server.
    """
    response_url = response_url_template.format(response)
    response = session.get(response_url)
    return response.content

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
    # Get the page content from the challenge URL
    response = session.get(challenge_url)
    if response.ok:
        extraction_result = extract_key_and_message(response.text)

        if extraction_result is not None:
            key, message = extraction_result
            print(key)
            print(message)
            decoded_string = xor_message(key, message)
            if decoded_string:
                # Send the response back to the server
                final_result = send_response(decoded_string)
                print(extract_flag(final_result.decode('utf-8')))
            else:
                print("Failed to decode the string.")
        else:
            print("Could not find the key and message in the page.")
    else:
        print(f"Failed to retrieve the challenge page, status code: {response.status_code}")

if __name__ == "__main__":
    main()
