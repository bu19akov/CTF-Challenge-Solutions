# Level 3

## Challenge Details 

- **CTF:** OverTheWire
- **Category:** Leviathan

## Provided Materials

- username: `leviathan3`
- password: `Q0G8j4sakn`

## Solution

Let's see what do we have:

```sh
leviathan3@gibson:~$ ls -al
total 40
drwxr-xr-x  2 root       root        4096 Oct  5  2023 .
drwxr-xr-x 83 root       root        4096 Oct  5  2023 ..
-rw-r--r--  1 root       root         220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root       root        3771 Jan  6  2022 .bashrc
-r-sr-x---  1 leviathan4 leviathan3 18072 Oct  5  2023 level3
-rw-r--r--  1 root       root         807 Jan  6  2022 .profile
```

Let's execute `level3` with `ltrace`:

```sh
leviathan3@gibson:~$ ltrace ./level3
__libc_start_main(0x80492bf, 1, 0xffffd654, 0 <unfinished ...>
strcmp("h0no33", "kakaka")                      = -1
printf("Enter the password> ")                  = 20
fgets(Enter the password> aaa
"aaa\n", 256, 0xf7e2a620)                 = 0xffffd42c
strcmp("aaa\n", "snlprintf\n")                  = -1
puts("bzzzzzzzzap. WRONG"bzzzzzzzzap. WRONG
)                      = 19
+++ exited (status 0) +++
```

Our input is compared to string `snlprintf`. Let's try to input it as password:

```sh
leviathan3@gibson:~$ ./level3
Enter the password> snlprintf
[You've got shell]!
$ cat /etc/leviathan_pass/leviathan4
AgvropI4OA
```

## Password

`leviathan4`:`AgvropI4OA`

*Created by [bu19akov](https://github.com/bu19akov)*