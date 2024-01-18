# Look inside the house

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Steganography
- **Points:** 2

## Provided Materials

- Image:

![Image](./file.jpg)

## Solution

We need to "look inside". This means, that we probably need to extract something from the image. For that we will use the tool called [steghide](https://www.kali.org/tools/steghide/). So the command is:

```sh
steghide extract -sf file.jpg
```

This indeed gives us `flag.txt` file.

## Final Flag

`FLAG-5jk682aqoepoi582r940oow`

*Created by [bu19akov](https://github.com/bu19akov)*

