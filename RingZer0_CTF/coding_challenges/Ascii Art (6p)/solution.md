# Ascii Art

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Coding Challenges
- **Points:** 6

## Provided Materials

- Web page with `ASCII Art` numbers

## Solution

We have to send the `ASCII Art` numbers back to the `http://challenges.ringzer0team.com:10119/?r=[your_response]`, so we can map each ASCII digit represantation to it's normal representation and send them to the server:

```python
import re
import requests
from bs4 import BeautifulSoup

# The URL of the challenge
challenge_url = "http://challenges.ringzer0team.com:10119"

# The URL to send the response to
response_url_template = "http://challenges.ringzer0team.com:10119/?r={}"

# Start a session to persist cookies and headers
session = requests.Session()

def extract_ascii(page_content):
    # Extract the content between the BEGIN and END markers
    match = re.search(r'----- BEGIN MESSAGE -----(.*)----- END MESSAGE -----', page_content, re.DOTALL | re.S)
    if match:
        # Remove HTML line breaks and non-breaking spaces
        ascii_art = match.group(1).strip()
        ascii_art = re.sub(r'<br\s*/?>', '\n', ascii_art)  # Remove HTML line breaks
        ascii_art = ascii_art.replace('&nbsp;', ' ').strip()     # Replace HTML non-breaking spaces with regular spaces
        return ascii_art

    return None

def send_response(response):
    response_url = response_url_template.format(response)
    response = session.get(response_url)
    return response.content

def decode_ascii_art(ascii_art):
    # Define the ASCII representation of numbers 0-9
    numbers = {
        'xxx \nx   x\nx   x\nx   x\n xxx': '0',
        'xx  \nx x  \n  x  \n  x  \nxxxxx': '1', 
        'xxx \nx   x \n  xx \n x   \nxxxxx': '2', 
        'xxxxx\n    x\n xxxx\n    x\nxxxxx': '3',
        'x   x\nx    x\n xxxxx\n     x\n    x': '4', 
        'xxxxx\nx    \n xxxx\n    x\nxxxxx': '5', 
        'xxxxx\nx    \nxxxxx\nx   x\nxxxxx': '6',
        'xxxxx\n    x\n    x\n    x\n    x': '7',
        'xxx \nx   x\n  xx \nx   x\n xxx': '8', 
        'xxxxx\nx   x\nxxxxx\n    x\nxxxxx': '9'
    }

    # Split the ASCII art into lines
    lines = [line for line in ascii_art.split('\n') if line]

    # Group lines into characters (assuming each number is 5 lines high and 5 characters wide)
    characters = ['\n'.join(lines[i:i+5]).strip() for i in range(0, len(lines), 5)]

    # Decode each character
    decoded = ''.join(numbers.get(c, '?') for c in characters)

    return decoded

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
        ascii = extract_ascii(response.text)

        if ascii:
            print(ascii)
            number = decode_ascii_art(ascii)
            if number:
                # Send the response back to the server
                print(number)
                final_result = send_response(number)
                print(extract_flag(final_result.decode('utf-8')))
            else:
                print("Failed to decode the numbers.")
        else:
            print("Could not find the message in the page.")
    else:
        print(f"Failed to retrieve the challenge page, status code: {response.status_code}")

if __name__ == "__main__":
    main()
```

## Final Flag

`FLAG-ioXVYPyk4sjtsPydks1pph84Gs`

*Created by [bu19akov](https://github.com/bu19akov)*