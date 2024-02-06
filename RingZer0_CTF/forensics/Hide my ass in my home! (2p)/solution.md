# Hide my ass in my home!

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Forensics
- **Points:** 2

## Provided Materials

- Directory `68789bfba0a2a675cab56db26e5d5bb`

## Solution

Firstly we will output all files in the directory (including hidden):

```sh
$ ls -al
total 10904
drwx------@ 15 vladimir  staff      480  6 фев 01:48 .
drwxr-xr-x  15 vladimir  staff      480  6 фев 01:49 ..
-rw-------@  1 vladimir  staff     2907 20 фев  2014 .bash_history
-rw-r--r--@  1 vladimir  staff       18 18 июл  2013 .bash_logout
-rw-r--r--@  1 vladimir  staff      176 18 июл  2013 .bash_profile
-rw-r--r--@  1 vladimir  staff      124 18 июл  2013 .bashrc
drwxr-xr-x@  2 vladimir  staff       64 11 ноя  2010 .gnome2
-rw-r--r--@  1 vladimir  staff    12288 20 фев  2014 .me.swp
drwxr-xr-x@  4 vladimir  staff      128 10 янв  2014 .mozilla
-rw-------@  1 vladimir  staff     1319 20 фев  2014 .viminfo
-rw-r--r--@  1 vladimir  staff    20969 20 фев  2014 1601066_559677267463652_942103441_n.jpg
-rw-r--r--@  1 vladimir  staff  5505097 20 фев  2014 Electro - Swing || Jamie Berry Ft. Octavia Rose - Delight.mp3
-rw-rw-r--@  1 vladimir  staff        0 20 фев  2014 bob.tar.gz
-rw-rw-r--@  1 vladimir  staff    11311 20 фев  2014 index.html
-rw-rw-r--@  1 vladimir  staff      676 20 фев  2014 you
```

Let's see, what's inside of `.me.swp`:

```sh
$ strings .me.swp | head
b0VIM 7.2
test
grosse-marde
~test/me
utf-8
U3210
#"! 
Flag-1s4g76jk89f
full of full 
and sunfull and 
```

## Final Flag

`Flag-1s4g76jk89f`

*Created by [bu19akov](https://github.com/bu19akov)*