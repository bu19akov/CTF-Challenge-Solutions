# I made a dd of Agent Smith usb key

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Forensics
- **Points:** 1

## Provided Materials

- Linux rev 1.0 ext2 filesystem data

## Solution

We can analyze the file with [strings](https://linux.die.net/man/1/strings) *(print the strings of printable characters in files)*:

```sh
$ strings file | head
lost+found
secret.txt
image
to keep
mselinux
unconfined_u:object_r:file_t:s0
FLAG-ggmgk05096
01.jpeg
02.jpeg
03.jpg
```

## Final Flag

`FLAG-ggmgk05096`

*Created by [bu19akov](https://github.com/bu19akov)*