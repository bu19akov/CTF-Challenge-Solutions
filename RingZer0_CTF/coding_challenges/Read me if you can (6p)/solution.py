import cv2
from PIL import Image
import pytesseract
import base64
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import os

# The URL of the challenge
challenge_url = "http://challenges.ringzer0team.com:10017"

# The URL to send the response to
response_url_template = "http://challenges.ringzer0team.com:10017/?r={}"

session = requests.Session()

def extract_image(page_content):
    base64_image = page_content.split('src="data:image/png;base64,')[1].split('"')[0]

    # Decode the Base64 string to bytes
    image_data = base64.b64decode(base64_image)

    # Convert bytes data to an image
    image = Image.open(BytesIO(image_data))

    # Save the image
    image.save("image.png")

    # Check if the file is saved correctly
    if os.path.exists("image.png"):
        print("Image saved successfully.")
    else:
        print("Failed to save the image.")

    return image


def extract_text():
    # Load the image using OpenCV
    image_cv = cv2.imread("./image.png")  # Update the path to your image

    # Convert to grayscale
    gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

    # Resize the image
    resized = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Define the threshold for white (in grayscale)
    lower_white = 220  # You might need to adjust this value
    upper_white = 255

    # Create a mask to keep only white pixels
    mask = cv2.inRange(resized, lower_white, upper_white)

    # Apply the mask to get an image with only white text
    result = cv2.bitwise_and(resized, resized, mask=mask)

    # Save the preprocessed image temporarily
    cv2.imwrite("./preprocessed.png", result)

    # Load the preprocessed image with PIL
    img = Image.open("./preprocessed.png")

    # Extract text
    text = pytesseract.image_to_string(img, lang='eng')
    # config = '-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # text = pytesseract.image_to_string(img, lang='eng', config=config)


    # Print the text
    print(text[:6])

    return text

def send_response(response):
    """
    This function sends response back to the server.
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
        # Extract the hash from the page
        image = extract_image(response.text)

        if image:
            # Attempt to crack the hash
            text = extract_text()
            if text:
                # Send the response back to the server
                final_result = send_response(text[:6])
                print(extract_flag(final_result.decode('utf-8')))
            else:
                print("Failed to crack the hash.")
        else:
            print("Could not find the hash in the page.")
    else:
        print(f"Failed to retrieve the challenge page, status code: {response.status_code}")

if __name__ == "__main__":
    main()
