from PIL import Image

def interpret_first_column(image_path):
    # Load the image
    img = Image.open(image_path)
    # Convert the image to grayscale to simplify the analysis
    img = img.convert('L')
    
    # Initialize the result string
    result = ''
    
    # Process the first column of the image
    for y in range(img.height):
        # Get the pixel value (in grayscale, 0 is black and 255 is white)
        pixel = img.getpixel((0, y))
        
        # Interpret pixel value (assuming the middle ground is 128)
        if pixel > 128:
            result += '1'  # White
        else:
            result += '0'  # Black

    return result

# Example usage
image_path = 'solved.bmp'
binary_sequence = interpret_first_column(image_path)
print(binary_sequence)
