# Hash breaker reloaded again

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Coding Challenges
- **Points:** 6

## Provided Materials

- Web page with hash that we need to crack and send the answer back to `http://challenges.ringzer0team.com:10159/?r=[your_response]`. 

## Solution

With the online hash cracking tool's help and a lot of time spent we can find out, that all our hashes, that we get will consist of 6 lowercase `alphanumeric` characters. But we will only have 3 seconds to crack the hash... So the solution is [rainbow table](https://en.wikipedia.org/wiki/Rainbow_table). Firstly we will need to generate our `rainbow table`, but instead of generating one large file we will generate smaller files based on the first 4 characters of the hash. Also we will need to set [ulimit](https://www.scaler.com/topics/what-is-ulimit-in-linux/) to large amount to be able to open multiple files simultaneously:

```sh
ulimit -n 70000
```

On `MacOS` you will also need to execute:

```sh
sudo sysctl -w kern.maxfiles=100000
sudo sysctl -w kern.maxfilesperproc=100000
```

And here is `rainbow table` generating code (totally there should be `65536` subfolders):

```python
import hashlib
import os

def main():
    # Define character sets
    charset_small = list(range(48, 58)) + list(range(97, 103))
    charset = list(range(48, 58)) + list(range(97, 123))    

    # Directory for storing hash files
    base_path = "hashes"

    # Create the directory if it doesn't exist
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    # Open hash files
    fs = {}
    for f1 in charset_small:
        for f2 in charset_small:
            for f3 in charset_small:
                for f4 in charset_small:
                    bucket = chr(f1) + chr(f2) + chr(f3) + chr(f4)
                    file_path = os.path.join(base_path, bucket)
                    fs[bucket] = open(file_path, 'w')            

    # Build the list of plaintext to bruteforce
    for a in charset:
        for b in charset:
            for c in charset:
                for d in charset:
                    for e in charset:
                        for f in charset:
                            p = chr(a) + chr(b) + chr(c) + chr(d) + chr(e) + chr(f)
                            h = hashlib.sha1(p.encode()).hexdigest()  # Corrected to encode the string before hashing                            
                            fs[h[:4]].write('%s,%s\n' % (p, h))

    # Close all opened files
    for f in fs.values():
        f.close()

    print('Done.')

if __name__ == '__main__':
    main()
```

So when our `rainbow table` will be ready, we can get the hash, look for it's first 4 characters, open the folder with the corresponding name and search for exactly same hash:

```python
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
```

## Final Flag

`FLAG-wkmkmpmThX5nPnHoNarKZsqvIE`

*Created by [bu19akov](https://github.com/bu19akov)*