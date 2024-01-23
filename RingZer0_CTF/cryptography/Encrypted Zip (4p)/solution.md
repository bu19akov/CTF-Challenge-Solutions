# Encrypted Zip

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Cryptography
- **Points:** 4

## Provided Materials

- Text: `weird.zip` and `flag.zip` apparently have the same password. We also found a unzipped version of `weird.txt`

## Solution

With a bit of searching we find the [Known plaintext attack](https://cn.elcomsoft.com/help/en/archpr/known_plaintext_attack_(zip).html).

There is a tool called [pkcrack](https://github.com/keyunluo/pkcrack), that allows us to retrieve `zip` password, if we have zipped file and its unzipped content. Firstly we need to zip the unzipped content:

```sh
$ zip weird-new.zip weird.txt
```

And then perform the attack:

```sh
$ pkcrack -C weird.zip -c "weird.txt" -P weird-new.zip -p "weird.txt" -a
```

It took a lot of time, but here is our password: `testtest`.

So we can unzip our `flag.zip` with the password and get our `flag`.

## Final Flag

`FLAG-Mk5N1z6PDbcw6alA1G8ixz85`

*Created by [bu19akov](https://github.com/bu19akov)*