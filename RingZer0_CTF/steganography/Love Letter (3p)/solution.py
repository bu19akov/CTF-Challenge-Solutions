# Initialize an empty string to hold the binary representation
binary = ""

# Open the file in binary read mode
with open("./file.txt", "rb") as file:
    # Read the file byte by byte
    for byte in file.read():
        # Check if the byte value is 128 or greater (not ASCII)
        if byte >= 128:
            binary += "1" 
        # Check if the byte is a space character
        elif chr(byte) == ' ':
            binary += "0"

# Function to convert a binary string to text
def binary_to_text(binary_str):
    text = "" 
    # Process each 8-bit chunk of the binary string
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]  # Extract an 8-bit chunk
        text += chr(int(byte, 2))  # Convert the chunk to an integer, then to a character, and append it to the text
    return text  # Return the resulting text

# Convert the binary string to text and print it
print(binary_to_text(binary))
