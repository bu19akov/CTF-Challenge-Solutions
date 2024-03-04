# The Last Dance

## Challenge Details 

- **CTF:** Hack The Box
- **Category:** Crypto
- **Points:** 10

## Provided Materials

- `Python` code:

```py
from Crypto.Cipher import ChaCha20
from secret import FLAG
import os


def encryptMessage(message, key, nonce):
    cipher = ChaCha20.new(key=key, nonce=iv)
    ciphertext = cipher.encrypt(message)
    return ciphertext


def writeData(data):
    with open("out.txt", "w") as f:
        f.write(data)


if __name__ == "__main__":
    message = b"Our counter agencies have intercepted your messages and a lot "
    message += b"of your agent's identities have been exposed. In a matter of "
    message += b"days all of them will be captured"

    key, iv = os.urandom(32), os.urandom(12)

    encrypted_message = encryptMessage(message, key, iv)
    encrypted_flag = encryptMessage(FLAG, key, iv)

    data = iv.hex() + "\n" + encrypted_message.hex() + "\n" + encrypted_flag.hex()
    writeData(data)
```

- Message

## Solution

In a stream cipher like `ChaCha`, encryption is performed by generating a key stream (a sequence of bits) based on the secret key and a nonce. Each bit of the plaintext is `XORed` with a corresponding bit from the key stream to produce the ciphertext. Decryption is the same operation: the ciphertext is `XORed` with the same key stream to retrieve the original plaintext.

We have two plaintext messages (`P1` and `P2`), and they are both encrypted with the same key stream (`K`) due to a nonce reuse *(a common mistake in the implementation of cryptographic protocols)*. This gives us two ciphertexts:

`C1` = `P1` xor `K`
`C2` = `P2` xor `K`

We know `C1`, `C2`, as also `P1`. Based on that we can decrypt `P2` without knowing the key:

`C1` xor `C2` = (`P1` xor `K`) xor (`P2` xor `K`)
`K` xor `K` = 0 => `C1` xor `C2` = `P1` xor `P2`
`P2` = `C1` xor `C2` xor `P1`:

```py
import pwn

cipertext1 = '7aa34395a258f5893e3db1822139b8c1f04cfab9d757b9b9cca57e1df33d093f07c7f06e06bb6293676f9060a838ea138b6bc9f20b08afeb73120506e2ce7b9b9dcd9e4a421584cfaba2481132dfbdf4216e98e3facec9ba199ca3a97641e9ca9782868d0222a1d7c0d3119b867edaf2e72e2a6f7d344df39a14edc39cb6f960944ddac2aaef324827c36cba67dcb76b22119b43881a3f1262752990'
cipertext2 = '7d8273ceb459e4d4386df4e32e1aecc1aa7aaafda50cb982f6c62623cf6b29693d86b15457aa76ac7e2eef6cf814ae3a8d39c7'

message = b"Our counter agencies have intercepted your messages and a lot "
message += b"of your agent's identities have been exposed. In a matter of "
message += b"days all of them will be captured"

cipertext1 = bytes.fromhex(cipertext1)
cipertext2 = bytes.fromhex(cipertext2)
plaintext1 = message

plaintext2 = pwn.xor(cipertext1, cipertext2, plaintext1)

print("FLAG:", plaintext2)
```

Output:

```
FLAG: b'HTB{und3r57AnD1n9_57R3aM_C1PH3R5_15_51mPl3_a5_7Ha7}...
```

## Final Flag

`HTB{und3r57AnD1n9_57R3aM_C1PH3R5_15_51mPl3_a5_7Ha7}`

*Created by [bu19akov](https://github.com/bu19akov)*