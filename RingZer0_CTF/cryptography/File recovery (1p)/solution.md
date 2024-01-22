# File recovery

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Cryptography
- **Points:** 1

## Provided Materials

- 2 files: `flag.enc` and `private.pem`

## Solution

To decrypt a file `flag.enc` using a private key file `private.pem` we firstly need to identify which encryption algorithm was used to encrypt `flag.enc`:

```sh
$ file flag.enc 
flag.enc: OpenPGP Secret Key
$ file private.pem 
private.pem: PEM RSA private key
```

`private.pem` is [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) private key, so we can use [OpenSsl](https://www.openssl.org) to decrypt our 'flag.enc' with our private key:

```sh
openssl rsautl -decrypt -inkey private.pem -in flag.enc -out flag.txt
```

## Final Flag

`FLAG-vOAM5ZcReMNzJqOfxLauakHx`

*Created by [bu19akov](https://github.com/bu19akov)*