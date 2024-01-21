# I saw a little elf

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Coding Challenges
- **Points:** 4

## Provided Materials

- Web page with `elf message` and `checksum`

## Solution

We see the `base64` encoded message and the name of the challenge gives us a hint, that it will be [Elf binary](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format).

So we can retrieve the flag with the `python`:

```python
import urllib.request
import base64
from bs4 import BeautifulSoup
import urllib.parse

def open_url_get_code():
    """Fetches data from the specified URL and extracts the binary message."""
    # Create a request opener with custom headers (e.g., cookie)
    request = urllib.request.build_opener()
    request.addheaders.append(('Cookie', 'cookievalue'))

    # Open the URL and read the response
    response = request.open('http://challenges.ringzer0team.com:10015')
    content = BeautifulSoup(str(response.readlines()), 'lxml')

    # Extract the binary message from the response content
    binary_message = content.find('div', {'class': 'message'}).get_text()
    binary_message = binary_message.replace('----- BEGIN Elf Message -----', '').replace('----- End Elf Message -----', '')
    binary_message = binary_message[24:-24]  # Remove extra characters
    return binary_message

def convert_to_elf_bytes(code):
    """Decodes the base64 encoded string and returns a bytearray."""
    code_bytes = code.encode()  # Convert to byte string
    try:
        while True:
            # Add padding if necessary
            padding = 4 - len(code_bytes) % 4
            if padding:
                code_bytes += b'=' * padding

            # Decode the base64 string
            code_bytes = base64.b64decode(code_bytes)
            if len(code_bytes) < 10000:
                break
    except Exception as e:
        print('Error:', e)
    return bytearray(code_bytes[::-1])  # Reverse the byte array

def get_code(bytes_data):
    """Extracts a specific portion of the byte data."""
    # Extract specific bytes based on predefined offsets
    byte_segment = bytes_data[0x5E6:0x5EA] + bytes_data[0x5EE:0x5F0]
    return ''.join(chr(b) for b in byte_segment)

def send(code):
    """Sends the extracted code to the server and prints the response."""
    # Create a request opener with custom headers
    request = urllib.request.build_opener()
    request.addheaders.append(('Cookie', 'cookievalue'))

    # URL encode the code and construct the request URL
    encoded_code = urllib.parse.quote(code)
    url = f'http://challenges.ringzer0team.com:10015/?r={encoded_code}'

    try:
        # Send the request and parse the response
        response = request.open(url)
        content = BeautifulSoup(str(response.readlines()), 'lxml')
        flag = content.find('div', {'class': 'alert alert-info'})
        
        return flag
    except Exception as e:
        print('Error:', e)

if __name__ == "__main__":
    binary_code = open_url_get_code()
    elf_bytes = convert_to_elf_bytes(binary_code)
    extracted_code = get_code(elf_bytes)
    print(extracted_code)
    flag = send(extracted_code)
    if flag:
        print(flag.get_text())
```

## Final Flag

`FLAG-ip561ug06vrwcfl3zhvoyy229r`

*Created by [bu19akov](https://github.com/bu19akov)*