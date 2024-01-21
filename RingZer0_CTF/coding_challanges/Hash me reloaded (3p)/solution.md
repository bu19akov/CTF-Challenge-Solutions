# Hash me reloaded

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Coding Challenges
- **Points:** 3

## Provided Materials

- Web page with message


## Solution

We need to hash the message using sha512 algorithm and send the answer back to `http://challenges.ringzer0team.com:10014/?r=[your_response]`

```python
import requests
import re
import hashlib
from bs4 import BeautifulSoup

# The URL of the challenge
challenge_url = "http://challenges.ringzer0team.com:10014"

# Start a session to persist cookies and headers
session = requests.Session()

def extract_message(page_content):
    """
    This function extracts the message from the HTML content using BeautifulSoup.
    """
    soup = BeautifulSoup(page_content, 'html.parser')
    message_div = soup.find('div', class_='message')
    if message_div:
        # Extracting text within the '----- BEGIN MESSAGE -----' and '----- END MESSAGE -----'
        message_text = message_div.get_text(strip=True)
        # Using regex to extract the exact message
        match = re.search(r'----- BEGIN MESSAGE -----(.*)----- END MESSAGE -----', message_text, re.DOTALL)
        if match:
            return match.group(1).strip()
    return None

def binary_to_text(binary_str):
    """
    This function converts a binary string to ASCII text.
    It assumes that binary_str is a string of binary characters ('0' or '1').
    """
    # Ensure that the binary string has a length that is a multiple of 8
    if len(binary_str) % 8:
        # If not, it's likely that the binary string is not properly formatted
        raise ValueError("The binary string length must be a multiple of 8")

    # Split the binary string into chunks of 8 characters (1 byte)
    binary_values = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    
    # Convert each binary value to an ASCII character
    ascii_string = ''.join(chr(int(bv, 2)) for bv in binary_values)
    return ascii_string

def hash_message_sha512(message):
    """
    This function returns the SHA-512 hash of the given message.
    """
    return hashlib.sha512(message.encode('utf-8')).hexdigest()

def send_response(message_hash):
    """
    This function sends the hash response back to the server.
    """
    response_url = f"{challenge_url}/?r={message_hash}"
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

# Main logic to perform the task
def main():
    # Get the page content from the challenge URL
    response = session.get(challenge_url)
    if response.ok:
        # Extract the message from the page
        message = extract_message(response.text)
        if message:
            # Convert binary message to text if necessary
            if re.match(r'[01\s]+$', message):
                message = binary_to_text(message)
            # Hash the message using SHA-512
            message_hash = hash_message_sha512(message)
            # Send the response back to the server
            result = send_response(message_hash)
            print(extract_flag(result))
        else:
            print("Could not find the message in the page.")
    else:
        print(f"Failed to retrieve the challenge page, status code: {response.status_code}")

if __name__ == "__main__":
    main()
```

## Final Flag

`FLAG-jz145p93ei75buh1kpx9bul9xl`

*Created by [bu19akov](https://github.com/bu19akov)*