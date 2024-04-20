# Level 1

## Challenge Details 

- **CTF:** OverTheWire
- **Category:** Leviathan

## Provided Materials

- username: `leviathan1`
- password: `PPIfmI1qsA`

## Solution

Let's see our directory:

```sh
leviathan1@gibson:~$ ls -al
total 36
drwxr-xr-x  2 root       root        4096 Oct  5  2023 .
drwxr-xr-x 83 root       root        4096 Oct  5  2023 ..
-rw-r--r--  1 root       root         220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root       root        3771 Jan  6  2022 .bashrc
-r-sr-x---  1 leviathan2 leviathan1 15072 Oct  5  2023 check
-rw-r--r--  1 root       root         807 Jan  6  2022 .profile
```

We can call `check` with command `ltrace` that is used to see what library calls are made during binary execution:

```sh
leviathan1@gibson:~$ ltrace ./check
__libc_start_main(0x80491e6, 1, 0xffffd654, 0 <unfinished ...>
printf("password: ")                            = 10
getchar(0xf7fbe4a0, 0xf7fd6f90, 0x786573, 0x646f67password: password
) = 112
getchar(0xf7fbe4a0, 0xf7fd6f70, 0x786573, 0x646f67) = 97
getchar(0xf7fbe4a0, 0xf7fd6170, 0x786573, 0x646f67) = 115
strcmp("pas", "sex")                            = -1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)            = 29
+++ exited (status 0) +++
```

So the password is `sex`:

```sh
leviathan1@gibson:~$ ./check
password: sex
$ cat /etc/leviathan_pass/leviathan2
mEh5PNl10e
```

## Password

`leviathan2`:`mEh5PNl10e`

*Created by [bu19akov](https://github.com/bu19akov)*