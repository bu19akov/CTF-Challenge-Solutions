# Can you understand this sentence?

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Cryptography
- **Points:** 3

## Provided Materials

- Piece of text `xipak-comok-repuk-vanik-dytuk-dimyk-sinyx`

## Solution

A little bit of research provides me, that is [Bubble Babble encoding](https://www.easytechjunkie.com/what-is-bubble-babble.htm). So with the help of [bubblepy](https://pypi.org/project/bubblepy/) python library we can decrypt our text:

```sh
$ python3
>>> from bubblepy import BubbleBabble
>>> bb = BubbleBabble()
>>> bb.decode("xipak-comok-repuk-vanik-dytuk-dimyk-sinyx")
b'hackingbubble'
```

## Final Flag

`hackingbubble`

*Created by [bu19akov](https://github.com/bu19akov)*