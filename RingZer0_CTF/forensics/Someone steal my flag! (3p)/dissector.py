import re
import base64

# Path to your file (change this to the actual path of your file)
file_path = './diss.txt'

# Regular expression to match the relevant part of the lines
regex = r'Name: ([0-9a-f]+)\.192\.168\.191\.129'

# List to hold extracted hex parts
hex_parts = []

# Read the file and extract hex parts and remove duplicates
current = ""
with open(file_path, 'r') as file:
    for line in file:
        match = re.search(regex, line)
        if match:
            hex_part = match.group(1)
            if hex_part != current:
                current = hex_part
                hex_parts.append(hex_part)

# Combine all hex parts into a single string
combined_hex = "".join(hex_parts)

# Convert hex to bytes
bytes_from_hex = bytes.fromhex(combined_hex)

# Convert bytes to string assuming it's ASCII
ascii_string = bytes_from_hex.decode('ascii')

# Base64 decode the ASCII string
decoded_base64 = base64.b64decode(ascii_string)

print(decoded_base64)
