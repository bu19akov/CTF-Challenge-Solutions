def shuffle_alphabet(keyword):
    """
    Shuffles the alphabet based on the given keyword.
    The keyword characters are moved to the beginning of the alphabet.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in keyword.upper():
        index = alphabet.find(char)
        alphabet = alphabet[index+1:] + char + alphabet[:index]
    return alphabet

def decrypt(ciphertext, shuffled_alphabet):
    """
    Decrypts the given ciphertext using the shuffled alphabet.
    The shuffled alphabet is dynamically updated based on the decrypted characters.
    """
    regular_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""

    for char in ciphertext:
        if char in shuffled_alphabet:
            index = shuffled_alphabet.find(char)
            plaintext_char = regular_alphabet[index]
            plaintext += plaintext_char

            # Shuffle the alphabet using the plaintext character
            index = shuffled_alphabet.find(plaintext_char)
            shuffled_alphabet = shuffled_alphabet[index+1:] + plaintext_char + shuffled_alphabet[:index]

    return plaintext

def try_decrypt_with_keywords(ciphertext, file_path):
    """
    Tries to decrypt the ciphertext using keywords from a file.
    Each line in the file is treated as a potential keyword.
    Returns the plaintext and keyword if the flag is found.
    """
    with open(file_path, 'r') as file:
        for line in file:
            keyword = line.strip().upper()
            # Skip the keyword if it contains non-letter characters
            if not keyword.isalpha():
                continue

            shuffled_alphabet = shuffle_alphabet(keyword)
            plaintext = decrypt(ciphertext, shuffled_alphabet)
            
            # Check if the plaintext contains "FLAGHYPHEN"
            if "FLAGHYPHEN" in plaintext:
                print(f"Decrypted text: {plaintext}")
                print(f"Found flag with keyword: {keyword}")
                return plaintext, keyword  # Return the plaintext and keyword if flag is found

    print("Flag not found. Try different keywords or check the ciphertext.")

# Define the ciphertext here or read from an external file if it's too long
ciphertext = "TQSBAODTTABMRUHDKNVUORAKATOZLFBFDWPHQLANSZIKOSEDESXZLDYEUBJRROAVZRBSLWESCEGGOCEMLFMAHAYSRNMCXATHGNZQBCLSCEMKIVELCRXCJTBBTXGBRNDQTLJMLUOEQWTHWVBAZHAABXPZELKBNWSNCZLNSBELFFKDLVFWOWNDQWMLFXEQWAQOQRIAAVSXAADYEUUAMTHYLSCVILMNE"

# Attempt to decrypt the ciphertext using keywords from a file
plaintext, keyword = try_decrypt_with_keywords(ciphertext, './words.txt')

# If a keyword is found, decrypt the message using it
if keyword:
    shuffled_alphabet = shuffle_alphabet(keyword)
    plaintext = decrypt(ciphertext, shuffled_alphabet)
    print(plaintext)
