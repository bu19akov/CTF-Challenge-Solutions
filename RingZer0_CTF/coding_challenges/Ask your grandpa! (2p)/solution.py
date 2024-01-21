from PIL import Image

# Constants defining the dimensions and positions for decoding
COLUMN_WIDTH = 52
ROW_HEIGHT = 150
START_X = 155
START_Y = 170
THRESHOLD = 25  # Threshold for determining whether a position is punched
NUM_COLUMNS = 80
NUM_ROWS = 12

# Mapping of punched positions to characters
CHAR_MAP = {
    0: ' ',  # No punches
    1: "0123456789?-&",  # Single punch mapping
    2: {  # Double punch mapping
        12: "ABCDEFGHI",
        11: "JKLMNOPQR",
        0: "/STUVWXYZ",
        8: ":#@'\"="
    },
    3: {  # Triple punch mapping
        12: " .<|(+",
        11: "$*);)",
        0: "_%,>?"
    }
}

def get_punched_positions(pixels, column_index):
    """Determines the punched positions for a given column."""
    punched = []
    for row_index in range(NUM_ROWS):
        x = column_index * COLUMN_WIDTH + START_X
        y = row_index * ROW_HEIGHT + START_Y
        if pixels[x, y][0] < THRESHOLD:
            punched.append(row_index)
    return adjust_punched_positions(punched)

def adjust_punched_positions(punched):
    """Adjusts punched positions to match the character map indices."""
    adjusted = []
    for p in punched:
        if p > 1:
            adjusted.append(p - 2)
        else:
            adjusted.append(12 - p)
    return adjusted

def decode_character(punched):
    """Decodes a character from the list of punched positions."""
    length = len(punched)
    if length == 0:
        return CHAR_MAP[0]
    elif length == 1:
        return CHAR_MAP[1][punched[0]]
    elif length >= 2:
        special_key = punched[0] if punched[0] in CHAR_MAP[length] else punched[1]
        index = punched[1] if punched[0] == special_key else punched[0]
        return CHAR_MAP[length][special_key][index - 1]

def decode_card(image_path):
    """Decodes the entire card from the image file."""
    card = Image.open(image_path)
    pixels = card.load()
    w, _ = card.size

    decoded_text = []
    for column in range(NUM_COLUMNS):
        if column * COLUMN_WIDTH + START_X > w:
            break
        punched = get_punched_positions(pixels, column)
        decoded_text.append(decode_character(punched))

    return "".join(decoded_text)

# Usage
decoded_data = decode_card("file.jpg")
print(decoded_data)
