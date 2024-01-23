def rot_cipher_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Check if character is an alphabet
            # Shift character, keeping case in mind
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def contains_all_letters(text, letters):
    return all(letter in text for letter in letters)

def find_letters(text, letters):
    for shift in range(26):
        decrypted = rot_cipher_decrypt(text, shift)
        if contains_all_letters(decrypted, letters):
            print(f"Shift {shift}: {decrypted}")

# Your string
encrypted_string = "GMODCDOOKCDBIOYDRMKDPQLDPVWYOIVRVSEOV"
letters_to_find = "FLAG"
find_letters(encrypted_string, letters_to_find)
