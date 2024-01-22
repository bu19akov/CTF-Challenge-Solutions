# Find the right word

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Coding Challenges
- **Points:** 7

## Provided Materials

- Web page with 7 shuffled words

## Solution

We need to identify the shuffled words and send them back to `http://challenges.ringzer0team.com:10126/?r=[your_response]`. We will use [this](https://github.com/dwyl/english-words/blob/master/words_alpha.txt) dictionary of words that only have letters (no numbers or symbols):

```python
import requests
from nltk.corpus import words
import re
from bs4 import BeautifulSoup


# Start a session to persist cookies and headers
session = requests.Session()

# The URL of the challenge
url = "http://challenges.ringzer0team.com:10126/"

def unscramble_word(scrambled, word_list):
    # Sort the letters of the scrambled word
    sorted_scrambled = sorted(scrambled)

    # Iterate over the word list and compare sorted letters
    for word in word_list:
        if sorted(word) == sorted_scrambled:
            return word  # Return the word if a match is found

    # If no match is found, return None or an empty string
    return None


def extract_scrambled_words(text):
    match = re.search(r'----- BEGIN WORDS -----(.*)----- END WORDS -----', text, re.DOTALL | re.S)
    if match:
        # Clean the matched hash value by removing <br> tags
        scrambled_words_str = re.sub(r'<br\s*/?>', '', match.group(1).strip()).strip()
        scrambled_words_list = scrambled_words_str.split(',')
        return scrambled_words_list
    return None

def load_word_list(file_path):
    with open(file_path, 'r') as file:
        return set(word.strip() for word in file.readlines())
    
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
    response = session.get(url)
    if response.ok:
        # Extract the hash from the page
        scrambled_words = extract_scrambled_words(response.text)

        if scrambled_words:
            print(scrambled_words)
            # Step 2: Unscramble the words
            word_list = load_word_list('./words_alpha.txt')
            unscrambled_words = []
            for scrambled in scrambled_words:
                unscrambled = unscramble_word(scrambled, word_list) 
                unscrambled_words.append(unscrambled)
            if len(unscrambled_words) > 0:
                # Step 3: Send the answer back
                print(unscrambled_words)
                answer = ','.join(unscrambled_words)
                response_url = f"{url}?r={answer}"
                response = requests.get(response_url)
                print(extract_flag(response.text))
            else:
                print("Failed to unscramble.")
        else:
            print("Could not find words in the page.")
    else:
        print(f"Failed to retrieve the challenge page, status code: {response.status_code}")

if __name__ == "__main__":
    main()

```

## Final Flag

``

*Created by [bu19akov](https://github.com/bu19akov)*