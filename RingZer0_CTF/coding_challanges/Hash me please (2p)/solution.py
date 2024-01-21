import requests
import re
import hashlib
from bs4 import BeautifulSoup

# The URL of the challenge
challenge_url = "http://challenges.ringzer0team.com:10013"

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

def send_response(message_hash):
    """
    This function sends the hash response back to the server.
    """
    response_url = f"{challenge_url}/?r={message_hash}"
    response = session.get(response_url)
    return response.content

def hash_message_sha512(message):
    """
    This function returns the SHA-512 hash of the given message.
    """
    return hashlib.sha512(message.encode('utf-8')).hexdigest()

# Main logic to perform the task
def main():
    # Get the page content from the challenge URL
    response = session.get(challenge_url)
    if response.ok:
        # Extract the message from the page
        message = extract_message(response.text)
        if message:
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
