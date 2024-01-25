# Crypto Leak

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Cryptography
- **Points:** 4

## Provided Materials

- 2 Files: `RC8_Encrypt.py` and `transcript.wav.enc`

## Solution

We have an encrypted audio file with a `.wav` extension. Our goal is to decrypt it. The encryption method used is a stream cipher known as the [Linear Feedback Shift Register](https://en.wikipedia.org/wiki/Linear-feedback_shift_register).

The `.wav` format is quite predictable, especially in its header part. This predictability is crucial for our attack method.

A typical `.wav` file starts with a standard header. For example, it begins with the ASCII characters `RIFF` followed by the file size, `WAVE`, `fmt `, and a section indicating the format size (usually 0x10 or 16 in decimal).

Example of a .wav header:

- `RIFF` (4 bytes)
- File size minus 8 bytes (4 bytes)
- `WAVE` (4 bytes)
- `fmt ` (4 bytes)
- Format size (4 bytes, typically 0x10)
	
By comparing the first 20 bytes of the encrypted `.wav` file with a standard `.wav` header, we can extract the first 20 bytes of the keystream. This is done by XORing these bytes with the encrypted bytes.

Example:

- Encrypted bytes (first 20 bytes)
- Standard WAV header bytes (first 20 bytes)
- XORing these two gives us the first 20 bytes of the keystream

[Berlekamp-Massey Algorithm](https://en.wikipedia.org/wiki/Berlekamp–Massey_algorithm) helps us find the shortest sequence of bits (the minimal polynomial) that can generate our keystream.

The minimal polynomial from the Berlekamp-Massey algorithm is effectively our encryption key. The seed is the first 64 bits of our keystream. We use an implementation from a [GitHub repository](https://github.com/mfukar/lfsr/tree/master) for this step:

```python
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
```

With the key and seed, we use the `RC8_Encrypt.py` script to recreate the original keystream (we need to slightly modify it):

```python
def main():
    seed_str, key_str = "30EE66FD6A3DEAD3", "008000021DCDC007"
    seed = int(seed_str, 16)  # Convert hexadecimal string to integer
    key = int(key_str, 16)    # Convert hexadecimal string to integer

    with open("./transcript.wav.enc", 'rb') as fin:
        data = bytearray(fin.read())

    for i,x in enumerate(rc8(seed, key, len(data))):
        data[i] ^= x

    with open("./transcript.wav", 'wb') as fout:
        fout.write(data)
```

After decryption, we receive the new audio file, and when we play it, we hear: "Well done! Check your file metadata for your flag!"

```sh
$ exiftool transcript.wav
ExifTool Version Number         : 12.60
File Name                       : transcript.wav
Directory                       : .
File Size                       : 348 kB
File Modification Date/Time     : 2024:01:25 20:10:08+01:00
File Access Date/Time           : 2024:01:25 20:14:13+01:00
File Inode Change Date/Time     : 2024:01:25 20:10:08+01:00
File Permissions                : -rw-r--r--
File Type                       : WAV
File Type Extension             : wav
MIME Type                       : audio/x-wav
Encoding                        : Microsoft PCM
Num Channels                    : 1
Sample Rate                     : 44100
Avg Bytes Per Sec               : 88200
Bits Per Sample                 : 16
Date Created                    : 2018
Track Number                    : 0
ID3 Size                        : 155
Track                           : 0
Artist                          : NorthSec 2018
Recording Time                  : 2018
Genre                           : Flagstep
Comment                         :  FLAG-ccfd9b48a255a25e2557373e429d9dc5
User Defined Text               : (Band) Towel
Date/Time Original              : 2018
Duration                        : 3.95 s
```
	
## Final Flag

`FLAG-ccfd9b48a255a25e2557373e429d9dc5`

*Created by [bu19akov](https://github.com/bu19akov)*