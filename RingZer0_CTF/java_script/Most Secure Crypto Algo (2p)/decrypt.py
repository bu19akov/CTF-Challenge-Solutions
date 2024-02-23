from Crypto.Cipher import AES
import base64
import hashlib
from binascii import unhexlify

print("username=\x68\x34\x78\x30\x72")

crypted_pass = "ob1xQz5ms9hRkPTx+ZHbVg=="
crypted_pass = base64.b64decode(crypted_pass)

k = "\x93\x39\x02\x49\x83\x02\x82\xf3\x23\xf8\xd3\x13\x37"
k = bytes(k, "utf-8")

key = hashlib.sha256(k).hexdigest()
key = bytes(key, "utf-8")

IV = key[32:64]
key = key[0:32]

IV = unhexlify(IV)
key = unhexlify(key)

cipher = AES.new(key, AES.MODE_CBC, IV)

decrypted = cipher.decrypt(crypted_pass)
decrypted = str(decrypted, "utf-8")

print("password=" + decrypted[:-1])

