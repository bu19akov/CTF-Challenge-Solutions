# SysAdmin Part 2

## Challenge Details 

- **CTF:** RingZer0
- **Category:** SysAdmin Linux
- **Points:** 1

## Provided Materials

- SSH credentials

## Solution

We should look at `/etc/fstab` *(Configuration file for mounting filesystems on Linux/Unix systems.*):

```sh
morpheus@sysadmin-track:/home$ cat /etc/fstab
LABEL=rootfs  /         ext4  defaults  0 0
LABEL=UEFI    /boot/efi vfat  defaults  0 0
#//TheMAtrix/phone  /media/Matrix  cifs  username=architect,password=$(base64 -d "RkxBRy0yMzJmOTliNDE3OGJkYzdmZWY3ZWIxZjBmNzg4MzFmOQ=="),iocharset=utf8,sec=ntlm  0  0
```

We can then decode it:

```sh
morpheus@sysadmin-track:/home$ echo "RkxBRy0yMzJmOTliNDE3OGJkYzdmZWY3ZWIxZjBmNzg4MzFmOQ==" | base64 -d
FLAG-232f99b4178bdc7fef7eb1f0f78831f9
```

## Final Flag

`FLAG-232f99b4178bdc7fef7eb1f0f78831f9`

*Created by [bu19akov](https://github.com/bu19akov)*