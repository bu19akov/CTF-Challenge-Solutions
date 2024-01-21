# I hate mathematics

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Coding Challenges
- **Points:** 3

## Provided Materials

- Web page with equation

## Solution

We need to solve the equation, where the first part is in `decimal` format, second part - `hex` and the third part - `binary` and send the answer back to `http://challenges.ringzer0team.com:10032/?r=[your_response]`

```python
import requests
import re
from bs4 import BeautifulSoup

# The URL of the challenge
challenge_url = "http://challenges.ringzer0team.com:10032"

# Start a session to persist cookies and headers
session = requests.Session()

# Precompile the regular expressions
message_re = re.compile(r'----- BEGIN MESSAGE -----(.*)----- END MESSAGE -----', re.DOTALL)
hex_re = re.compile(r'0x[0-9A-Fa-f]+')
binary_re = re.compile(r'\b[01]+\b')

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
        match = message_re.search(message_text)
        if match:
            return match.group(1).strip()
    return None

def send_response(result):
    """
    This function sends the response back to the server.
    """
    response_url = f"{challenge_url}/?r={result}"
    response = session.get(response_url)
    return response.content

def evaluate_expression(expression):
    """
    Evaluate a mathematical expression that may contain decimal, hexadecimal, and binary numbers.
    """
    print(expression)
    # Remove the '= ?' part from the expression
    expression = expression.split('=')[0].strip()

    # Find all hexadecimal and bin numbers in the expression and convert them to decimal
    expression = hex_re.sub(lambda match: str(int(match.group(0), 16)), expression)
    expression = binary_re.sub(lambda match: str(int(match.group(0), 2)), expression)

    # Evaluate the mathematical expression
    try:
        print(expression)
        print(eval(expression))
        return eval(expression)
    except Exception as e:
        # Handle any exceptions that may occur during evaluation
        print(f"An error occurred while evaluating the expression: {e}")
        return None

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
            # Evaluate the expression within the message
            result = evaluate_expression(message)
            # Send the response back to the server
            final_result = send_response(result)
            print(extract_flag(final_result))
        else:
            print("Could not find the message in the page.")
    else:
        print(f"Failed to retrieve the challenge page, status code: {response.status_code}")

if __name__ == "__main__":
    main()
```

## Final Flag

`FLAG-JsxIhjHJekAiVaxJlNe2PAYZ`

*Created by [bu19akov](https://github.com/bu19akov)*