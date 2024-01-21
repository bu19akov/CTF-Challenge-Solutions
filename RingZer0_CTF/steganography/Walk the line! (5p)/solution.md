# Walk the line!

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Steganography
- **Points:** 5

## Provided Materials

- Image:

![Image](./file.jpg)

## Solution

We can see there is some hidden data with [binwalk](https://www.kali.org/tools/binwalk/) *(search a given binary image for embedded files*):

```sh
$ binwalk file.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.02
30            0x1E            TIFF image data, big-endian, offset of first image directory: 8
332           0x14C           JPEG image data, JFIF standard 1.02
7527          0x1D67          JPEG image data, JFIF standard 1.02
1783905       0x1B3861        JPEG image data, JFIF standard 1.02
1811631       0x1BA4AF        PGP RSA encrypted session key - keyid: EC6C8BA8 8B76173E RSA (Encrypt or Sign) 1024b
1811861       0x1BA595        PGP armored data,
1813879       0x1BAD77        Zip archive data, at least v1.0 to extract, compressed size: 230, uncompressed size: 230, name: flag.txt.gpg
1814261       0x1BAEF5        End of Zip archive, footer length: 22
```

We can see, what `binwalk` can extract with `-e` flag:

```sh
$ binwalk -e file.jpg
```

So we have a `.zip` file, that contains `flag.txt.gpg` inside. Let's see the file format:

```sh
$ file flag.txt.gpg 
flag.txt.gpg: PGP RSA encrypted session key - keyid: EC6C8BA8 8B76173E RSA (Encrypt or Sign) 1024b .
```

Let's try to find the `key`inside the image:

```sh
$ strings file.jpg | grep -i pgp
-----BEGIN PGP PRIVATE KEY BLOCK-----
-----END PGP PRIVATE KEY BLOCK-----
```

And indeed, it's here, let's extract this key now:

```sh
$ strings file.jpg | grep -A 33 "BEGIN PGP PRIVATE KEY BLOCK"
-----BEGIN PGP PRIVATE KEY BLOCK-----
Version: GnuPG v2.0.14 (GNU/Linux)
lQH+BFMJmU0BBAC7J3IMTZRiWsK9KlFC/UXQ1p5XerK2z2u3UqoZuHJfEKY81HNK
6kd6Ar134Mc80ItJl0JGdCgt56zNO68PHvLpLMTm3N6vjUUhEW4sJYbRQqk8AD5c
HKT5Hfb+WGGzPC4ZYqqmS39YNmx829Y58mDCKQX1uWAHh60Y1vUclZUp9wARAQAB
/gIDAhOLmBU0A0WY0PNdHjFHSA8M2efZJa2m/J0wIuBOQh2F1GFn3clu88fgh/uv
MwHNErzdP81oPZydnfntDUSX06l69jlc2JeLPbF5r8ndvyAmMzK9dWecB/wymjTy
DwyvQbevHAfwak30Ih3xmk6WzsTyLh9oUrAR9D6c9uDM+ce4H6Rpaz749cMiHHqC
jJh0qhDSPfSrps+gWUVbewVH0nl6JO1eUZCyEYv+GzbrwMvvzB6DKmPddWC/RUhM
rPArGLDNA7nuiErNfKPH5WxplFNgL/w8wN2JEX5WcseO3ky5RuyKNVcneDd1Ix+D
zCfXQM278P/1094/AllOEYRlyrzP/Mze6uu+5PcNEWmZbkOosFlIdL9fOiKn1kWC
9F8QGMBP5zw0VUXQXbhyJMf7QJDOHUyQWgODhvk+AI1T22sIzRowLAlxjqP45kkk
qANODqTHM4TPUpzUNsXZUn62n7jeOSXNlkBAgLM6hKAStB1zdGVldmUgKHN0ZWV2
ZSkgPHN0ZWV2ZUB0ZXN0Poi4BBMBAgAiBQJTCZlNAhsDBgsJCAcDAgYVCAIJCgsE
FgIDAQIeAQIXgAAKCRCqYfmAxT1btofZA/9gulteMQ5X2dre41sxrsMqm4Js6HPx
CwxpX99VjilkHAKCXJSnqU7JqWoFzPpyrTBtS29VoXXuFOpzL8BxYnzDoP+Q3Ybl
kq86zt4E+ryTtiaxgbSKT+BVAIp8AaIuAIWIS7pIzyacMDnEWui8GwgxBhPN/3Tu
Oi7oRetOVpDRcp0B/gRTCZlNAQQA7wnoBWSrppeWx5q0cC3G47eaXM32weHX1Kqy
Lw/Q+plHSThniy6kNEoiNBTd3pT8mIMCzz613EUwHbd2dDXf5zC8gds4Iveop+44
MgKInG8io2KYtXQOaRN5ivcD6ccjsp0t/5i7FjSH6XU14KzENJW0CQBPAgdoLmW/
+OTKVBcAEQEAAf4CAwITi5gVNANFmNBcvRhALhfr9KSDntvXJ0y3X8nAoCyInWW2
cmGgD2FTttpqskxKFpH7a0y0JtqMCMye3/EYtlEUFbASL1zHMNh2KAIRZeXmcsdt
a8me78xc3wNjyC0J4xHFqs3UBt9XhqxmaubjisEz2J6apqfMVS+TrP5dTF9N46Sl
LTBSXhwOKMlR+1HILiSBuNHuDPR757+jT/aUzSSqYSdUSipsHx6k8FCKhfBhnpJq
k6dNNjweYJWaV9n9ZHLSpsZBwJj9STy0lXvTURK9EjPJrwIJbN+BDl2ipftWsEbm
D8OjjOHWY7YjDwe/X9U46W5Z2sfgMS0NBR+uS+v8MA+ww3Ez+ND3vwT+MAGMU55a
F7G9URgZQiBOgrr1OX8657t0N9KynkSKPUXVgrU0V93UAWdE/hplxy3Im1zeU0fL
ntwC/Pa6lVJk11Rizs/laJIerhjpGwn1I6J6bt+B2m4aRDVUAkSUJTKnq4ifBBgB
AgAJBQJTCZlNAhsMAAoJEKph+YDFPVu2M9oEALT4GOGNKlVV5j+JzGhG+OP1ojru
CVe7InSEtVUdQKeN4w/1myoz0SbAm+jGIFz4TFoZ+rP2d8DcBtqGFiwXzL9MaDnT
Y4Nb6ts5capH8OEp6MOPxssIiNa3W6dIqucWSVVnCm2PAU+q2Q22PFe/+wZyRNtS
vkwFlWNWJ2oR7DdF
=vDAR
-----END PGP PRIVATE KEY BLOCK-----
```

So we can also extract it to the file with:

```sh
$ strings file.jpg | grep -A 33 "BEGIN PGP PRIVATE KEY BLOCK" > key.gpg
```

We need to add empty line to `key.gpg` after version part in order to make it valid private key, as `strings` doesn't print any blank lines. Next, we need to import this `key` in our `keyring`:

```sh
$ gpg --import key.gpg
```

The `key.gpg` is also password encoded, so we can crack it with [John](https://www.openwall.com/john/) *(password cracking tool)*. So firstly we convert our `.gpg` file to `john's` format:

```sh
$ gpg2john key.gpg > gpg.john

File key.gpg
```

After that we can crack it:

```sh
$ john --wordlist=dictionaries/rockyou.txt gpg.john
Warning: detected hash type "gpg", but the string is also recognized as "gpg-opencl"
Use the "--format=gpg-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (gpg, OpenPGP / GnuPG Secret Key [32/64])
Warning: invalid UTF-8 seen reading ./tools/john/run/john.pot
Cracked 1 password hash (is in ./tools/john/run/john.pot), use "--show"
No password hashes left to crack (see FAQ)

$ john gpg.john --show 
steeve:1234:::steeve (steeve) <steeve@test>::key.gpg

1 password hash cracked, 0 left
```

The password is `1234`.

Now we can decrypt `flag.txt.gpg` with our password encoded private key `key.gpg` (We will be prompted to enter the password `1234`):

```sh
gpg -d flag.txt.gpg
gpg: encrypted with rsa1024 key, ID EC6C8BA88B76173E, created 2014-02-23
      "steeve (steeve) <steeve@test>"
FLAG-f9f$9{!-_4F"+
```

## Final Flag

`FLAG-f9f$9{!-_4F"+`

*Created by [bu19akov](https://github.com/bu19akov)*

