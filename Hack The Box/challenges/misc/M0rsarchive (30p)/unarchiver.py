import zipfile
import os
import re
from PIL import Image

# Morse code alphabet for encoding and decoding
morseAlphabet = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", " ": "/", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", ".": ".-.-.-",
    ",": "--..--", ":": "---...", "?": "..--..", "'": ".----.", "-": "-....-", "/": "-..-.", "@": ".--.-.", "=": "-...-"
}

# Reverse the morse code alphabet for decoding
inverseMorseAlphabet = {v: k for k, v in morseAlphabet.items()}

# Function to decode a morse code message
def decodedMorse(message):
    messageSeparated = message.split(' ')
    decodedMessage = ''
    for char in messageSeparated:
        decodedMessage += inverseMorseAlphabet.get(char, '<CNF>')  # Use get() for default value
    return decodedMessage

# Function to process image and extract binary string
def process_image_to_binary_string(image_path):
    image = Image.open(image_path)
    rgb = image.convert("RGB")
    width, height = image.size
    binString = ""
    color1, color2 = None, None  # Initialize color variables

    for y in range(height):
        for x in range(width):
            pixel = rgb.getpixel((x, y))
            if color1 is None:
                color1 = pixel
            elif pixel != color1 and color2 is None:
                color2 = pixel
            binString += "1" if pixel == color1 else "0"

    # Simplify the binary string representation of the morse code
    binString = re.sub('0001', '-', binString)
    binString = re.sub('01', '.', binString)
    binString = re.sub('1+', ' ', binString)
    binString = re.sub('\s+', ' ', binString).strip()
    return binString

# Function to unzip a file with a password
def unzip_file_with_password(zip_path, password, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(path=output_dir, pwd=bytes(password, 'utf-8'))
    print(f"Unzipped {zip_path} with password: {password}")

# Main function to iterate over zip files and process them
def main():
    image_path = "./pwd.png"

    for i in range(999, -1, -1):
        zip_file = f"flag_{i}.zip"
        binary_string = process_image_to_binary_string(image_path)
        password = decodedMorse(binary_string).lower()
        try:
            unzip_file_with_password(zip_file, password, ".")
            os.chdir("flag")
        except Exception as e:
            print(f"Failed to unzip {zip_file} with error: {e}")
    os.system("cat flag")

if __name__ == "__main__":
    main()
