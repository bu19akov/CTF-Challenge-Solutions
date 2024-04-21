# Level 6

## Challenge Details 

- **CTF:** OverTheWire
- **Category:** Leviathan

## Provided Materials

- username: `leviathan6`
- password: `YZ55XPVk2l`

## Solution

Let's see what do we have:

```sh
leviathan6@gibson:~$ ls -al
total 36
drwxr-xr-x  2 root       root        4096 Oct  5  2023 .
drwxr-xr-x 83 root       root        4096 Oct  5  2023 ..
-rw-r--r--  1 root       root         220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root       root        3771 Jan  6  2022 .bashrc
-r-sr-x---  1 leviathan7 leviathan6 15024 Oct  5  2023 leviathan6
-rw-r--r--  1 root       root         807 Jan  6  2022 .profile
```

Let's run `leviathan6` with `ltrace`:

```sh
leviathan6@gibson:~$ ltrace ./leviathan6 
__libc_start_main(0x80491d6, 1, 0xffffd654, 0 <unfinished ...>
printf("usage: %s <4 digit code>\n", "./leviathan6"usage: ./leviathan6 <4 digit code>
) = 35
exit(-1 <no return ...>
+++ exited (status 255) +++
```

So we must find 4-digit password. We can create simple `bash` script under `/tmp` directory, that will run our binary with all passwords from `0000` to `9999`:

```sh
#!/bin/bash

for a in {0000..9999}
do
~/leviathan6 $a
done
```

Give it executable permissions with `leviathan6@gibson:/tmp$ chmod +x script.sh` and run it:

```sh
...
Wrong
Wrong
$ cat /etc/leviathan_pass/leviathan7
8GpZ5f8Hze
```

## Password

`leviathan7`:`8GpZ5f8Hze`

*Created by [bu19akov](https://github.com/bu19akov)*