# Photon Lockdown

## Challenge Details 

- **CTF:** Hack The Box
- **Category:** Hardware
- **Points:** 10

## Provided Materials

- `.zip` file

## Solution

The password for `.zip` file is `hackthebox`. Inside the `.zip` file we have:

```sh
$ file *
fwu_ver: ASCII text
hw_ver:  X1 archive data
rootfs:  Squashfs filesystem, little endian, version 4.0, zlib compressed, 10936182 bytes, 910 inodes, blocksize: 131072 bytes, created: Sun Oct  1 07:02:43 2023
```

To extract files from `Squashfs filesystem` we can use [unsquashfs](https://manpages.ubuntu.com/manpages/focal/man1/unsquashfs.1.html):

```sh
$ sudo unsquashfs rootfs
Password:
Parallel unsquashfs: Using 8 processors
865 inodes (620 blocks) to write

[=============================================================|] 1485/1485 100%

created 440 files
created 45 directories
created 187 symlinks
created 238 devices
created 0 fifos
created 0 sockets
created 0 hardlinks
```

Let's see the extracted files:

```sh
$ ls -al
total 0
drwxrwxr-x   19 root      wheel   608 10 авг  2022 .
drwxr-xr-x@   6 vladimir  staff   192 29 фев 15:02 ..
-rw-rw-r--    1 root      wheel     0 10 авг  2022 .lstripped
drwxrwxr-x  226 root      wheel  7232 10 авг  2022 bin
lrwxrwxrwx    1 root      wheel    13 10 авг  2022 config -> ./var/config/
drwxrwxr-x  240 root      wheel  7680 10 авг  2022 dev
drwxrwxr-x   51 root      wheel  1632  1 окт 08:48 etc
drwxrwxr-x    3 root      wheel    96  1 окт 08:51 home
drwxrwxr-x    2 root      wheel    64  1 окт 08:53 image
drwxrwxr-x  114 root      wheel  3648 10 авг  2022 lib
lrwxrwxrwx    1 root      wheel     8 10 авг  2022 mnt -> /var/mnt
drwxrwxr-x    2 root      wheel    64 10 авг  2022 overlay
drwxrwxr-x    2 root      wheel    64 10 авг  2022 proc
drwxrwxr-x    2 root      wheel    64 10 авг  2022 run
lrwxrwxrwx    1 root      wheel     4 10 авг  2022 sbin -> /bin
drwxrwxr-x    2 root      wheel    64 10 авг  2022 sys
lrwxrwxrwx    1 root      wheel     8 10 авг  2022 tmp -> /var/tmp
drwxrwxr-x    3 root      wheel    96 10 авг  2022 usr
drwxrwxr-x    2 root      wheel    64 10 авг  2022 var
```

We can use `grep --include='*.filetype' -rnw . -e 'password' 2>&/dev/null` to search all `filetype` files for `password` occurences:

```
$ grep --include='*.xml' -rnw . -e 'HTB' 2>&/dev/null
./etc/config_default.xml:244:<Value Name="SUSER_PASSWORD" Value="HTB{N0w_Y0u_C4n_L0g1n}"/>
```

## Final Flag

`HTB{N0w_Y0u_C4n_L0g1n}`

*Created by [bu19akov](https://github.com/bu19akov)*