from __future__ import print_function
import base64
from Crypto.Cipher import AES

DEFAULT_HEADER = '76492d1116743f0423413b16050a5345'
DEFAULT_ENCODING = 'utf_16le'

def decrypt_secure_string(key, encrypted_data, header=DEFAULT_HEADER, encoding=DEFAULT_ENCODING):
    # Convert key to bytes
    key_bytes = bytes(key)

    # Remove header from data
    encrypted_data = encrypted_data[len(header):]

    # Decode base64 and split
    decoded_data = base64.b64decode(encrypted_data).decode(encoding).split('|')
    if len(decoded_data) != 3 or decoded_data[0] != '2':
        raise ValueError("Invalid encrypted data format")

    # Extract IV and ciphertext
    iv = base64.b64decode(decoded_data[1])
    ciphertext = bytes.fromhex(decoded_data[2])

    # Decrypt
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext)

    # Remove padding
    padding_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding_length]

    return decrypted_data

if __name__ == '__main__':
    key = [3, 4, 2, 3, 56, 34, 254, 222, 205, 34, 2, 23, 42, 64, 33, 223, 1, 34, 2, 7, 6, 5, 35, 12]
    encrypted_message = '76492d1116743f0423413b16050a5345MgB8AEEAYQBNAHgAZQAxAFEAVABIAEEAcABtAE4ATgBVAFoAMwBOAFIAagBIAGcAPQA9AHwAZAAyADYAMgA2ADgAMwBlADcANAA3ADIAOQA1ADIAMwA0ADMAMwBlADIAOABmADIAZABlAGMAMQBiAGMANgBjADYANAA4ADQAZgAwADAANwA1AGUAMgBlADYAMwA4AGEAZgA1AGQAYgA5ADIAMgBkAGIAYgA5AGEAMQAyADYAOAA='
    try:
        decrypted_output = decrypt_secure_string(key, encrypted_message)
        print(decrypted_output.decode(DEFAULT_ENCODING))
    except Exception as e:
        print(f"Error: {e}")
