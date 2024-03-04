def decrypt(ct_bytes):
    decrypted_msg = ""
    for ct in ct_bytes:
        for char in range(256):  # Try all possible characters
            if (123 * char + 18) % 256 == ct:
                decrypted_msg += chr(char)
                break
    return decrypted_msg

encrypted_bytes = bytes.fromhex("6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921")
message = decrypt(encrypted_bytes)
print(message)


