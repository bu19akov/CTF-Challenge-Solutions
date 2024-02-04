# Dr. Pouce

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Forensics
- **Points:** 2

## Provided Materials

- JPG image and PDF file

## Solution

We need to find `in which city DR Pouce is keeped` and `who is the evil man`?

We can analyze our two files with [exiftool](https://en.wikipedia.org/wiki/ExifTool) *(program for reading, writing, and manipulating image, audio, video, and PDF metadata)*:

```sh
$ exiftool DR_Pouce.jpg 
...
GPS Position                    : 44 deg 38' 46.43" N, 63 deg 34' 23.83" W
...
```

```sh
$ exiftool DR_Pouce.pdf
...
Author                          : Steve Finger
...
```

We can then use [Google Maps](https://www.google.com/maps) to find the city using coordinates:

![map](./map.jpg)



## Final Flag

`halifaxstevefinger `

*Created by [bu19akov](https://github.com/bu19akov)*