import struct
import lfsr

# Constants
ENCRYPTED_FILE_PATH = './transcript.wav.enc'
WAV_HEADER_START = b"RIFF"
WAV_FORMAT = b"WAVEfmt "
FORMAT_SECTION_SIZE = 0x10

def polynomial_to_int(polynomial):
    """
    Convert a binary polynomial representation to an integer.
    :param polynomial: List representing the polynomial.
    :return: Integer representation of the polynomial.
    """
    return int(''.join(map(str, polynomial))[::-1], 2)

def extract_keystream(encrypted_contents, header):
    """
    Determine the keystream used for encryption by XORing with known header.
    :param encrypted_contents: Bytearray of the encrypted contents.
    :param header: Bytearray of the expected WAV file header.
    :return: Extracted keystream as a bytearray.
    """
    return bytearray(
        [enc_byte ^ wav_byte for enc_byte, wav_byte in zip(encrypted_contents, header)]
    )

try:
    # Load the encrypted file content
    with open(ENCRYPTED_FILE_PATH, 'rb') as encrypted_file:
        encrypted_contents = bytearray(encrypted_file.read())

    # Construct the expected header for a standard WAV file
    wav_header = WAV_HEADER_START
    wav_header += struct.pack('<I', len(encrypted_contents) - 8)  # Adjusted file size
    wav_header += WAV_FORMAT
    wav_header += struct.pack('<I', FORMAT_SECTION_SIZE)

    # Extract keystream
    keystream_extracted = extract_keystream(encrypted_contents, wav_header)

    # Convert the extracted keystream to an integer for further processing
    keystream_integer = int.from_bytes(keystream_extracted, byteorder='little')

    # Isolate the seed (defined as the first 64 bits of the keystream)
    seed = keystream_integer & 0xffffffffffffffff
    print(f"Extracted Seed (64-bit): {seed:016X}")

    # Convert the keystream to a binary sequence
    binary_keystream = [
        int(bit) for bit in bin(keystream_integer)[2:].rjust(len(keystream_extracted) * 8, '0')[::-1]
    ]

    # Apply the Berlekamp-Massey algorithm to find the minimal polynomial
    minimal_poly = list(lfsr.bm(binary_keystream))[-1]

    # Convert the obtained polynomial to an integer to represent the encryption key
    key = polynomial_to_int(minimal_poly)
    print(f"Derived Encryption Key (as Hex): {key:016X}")

except IOError as e:
    print(f"Error opening file: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
