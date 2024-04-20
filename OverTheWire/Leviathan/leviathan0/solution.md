# Level 0

## Challenge Details 

- **CTF:** OverTheWire
- **Category:** Leviathan

## Provided Materials

- username: `leviathan0`
- password: `leviathan0`

## Solution

Let's login to the level with ssh and see what do we have in directory:

```sh
leviathan0@gibson:~$ ls -al
total 24
drwxr-xr-x  3 root       root       4096 Oct  5  2023 .
drwxr-xr-x 83 root       root       4096 Oct  5  2023 ..
drwxr-x---  2 leviathan1 leviathan0 4096 Oct  5  2023 .backup
-rw-r--r--  1 root       root        220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root       root       3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root       root        807 Jan  6  2022 .profile
```

Let's navigate to `.backup` folder and look what's inside it:

```sh
leviathan0@gibson:~$ cd .backup/
leviathan0@gibson:~/.backup$ ls -al
total 140
drwxr-x--- 2 leviathan1 leviathan0   4096 Oct  5  2023 .
drwxr-xr-x 3 root       root         4096 Oct  5  2023 ..
-rw-r----- 1 leviathan1 leviathan0 133259 Oct  5  2023 bookmarks.html
```

By searching for word `password` in `bookmarks.html` we can find `leviathan1` credentials:

```sh
leviathan0@gibson:~/.backup$ cat bookmarks.html | grep password
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is PPIfmI1qsA" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```

## Password

`leviathan1`:`PPIfmI1qsA`

*Created by [bu19akov](https://github.com/bu19akov)*