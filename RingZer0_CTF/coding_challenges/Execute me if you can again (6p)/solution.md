# Execute me if you can again

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Coding Challenges
- **Points:** 6

## Provided Materials

- Web page with shell code as in [Execute me if you can](https://github.com/bu19akov/CTF-Challenge-Solutions/blob/main/RingZer0_CTF/coding_challenges/Execute%20me%20if%20you%20can%20(5p)/solution.md)

## Solution

The same way as in `Execute me if you can`:

```python
import requests
import re
from ctypes import *
from bs4 import BeautifulSoup

session = requests.Session()

# Function to get the changed bytes from shellcode
def run_shellcode(shellcode):
    sc = bytes.fromhex(shellcode.replace('\\x', ''))

    # Extract a portion of the shellcode and convert it to hexadecimal string
    hx = sc[0x57:0x57+0x0c].hex()

    # Perform bitwise XOR with 0xFF and convert back to string
    result = ''.join(chr(int(x, 16) ^ 0xFF) for x in re.findall('..', hx))
    print(result)
    return result

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
    url = "http://challenges.ringzer0team.com:10125"
    response = session.get(url)
    html = response.text  # No need to decode
    match = re.search(r'----- BEGIN SHELLCODE -----(.*)----- END SHELLCODE -----', html, re.DOTALL | re.S)
    if match:
        # Clean the matched hash value by removing <br> tags
        shellcode = re.sub(r'<br\s*/?>', '', match.group(1).strip()).strip()
    output = run_shellcode(shellcode)

    url = f"http://challenges.ringzer0team.com:10125/?r={output}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Print the response content (HTML)
    print(extract_flag(response.text))


if __name__ == '__main__':
    main()
```

## Final Flag

`FLAG-0nAKFEd048B3hf76jR0Oy41x2I`

*Created by [bu19akov](https://github.com/bu19akov)*