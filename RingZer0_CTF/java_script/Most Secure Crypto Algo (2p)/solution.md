# Most Secure Crypto Algo

## Challenge Details 

- **CTF:** RingZer0
- **Category:** JavaScript
- **Points:** 2

## Provided Materials

- Login form

## Solution

We can find following script while analyzing the page with `Web-Inspector`:

```javascript
<script>
$(".c_submit").click(function(event) {
    event.preventDefault();
    var k = CryptoJS.SHA256("\x93\x39\x02\x49\x83\x02\x82\xf3\x23\xf8\xd3\x13\x37");
    var u = $("#cuser").val();
    var p = $("#cpass").val();
    var t = true;

    if (u == "\x68\x34\x78\x30\x72") {
        if (!CryptoJS.AES.encrypt(p, CryptoJS.enc.Hex.parse(k.toString().substring(0, 32)), {
            iv: CryptoJS.enc.Hex.parse(k.toString().substring(32, 64))
        }) == "ob1xQz5ms9hRkPTx+ZHbVg==") {
            t = false;
        }
    } else {
        $("#cresponse").html("<div class='alert alert-danger'>Wrong password sorry.</div>");
        t = false;
    }
    if (t) {
        if (document.location.href.indexOf("?p=") == -1) {
            document.location = document.location.href + "?p=" + p;
        }
    }
});
</script>
```

So it’s an [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) encryption in [CBC](https://www.educative.io/answers/what-is-cbc) mode with an [IV](https://www.techtarget.com/whatis/definition/initialization-vector-IV). We can write python script to get the password:

```python
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
```

Output:

```
username=h4x0r
password=PassW0RD!289%!*
```

## Final Flag

`FLAG-gYtLBa66178DG7l28Uu5lW45CR`

*Created by [bu19akov](https://github.com/bu19akov)*