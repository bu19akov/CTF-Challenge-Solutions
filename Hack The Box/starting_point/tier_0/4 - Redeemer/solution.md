# Redeemer

## Machine Details 

- **CTF:** Hack The Box
- **Category:** Tier 0

## Solution

#### 1. Which TCP port is open on the machine?

```sh
$ nmap -p- 10.129.136.187
Starting Nmap 7.94 ( https://nmap.org ) at 2024-03-02 09:15 CET
Stats: 0:00:32 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 6.99% done; ETC: 09:23 (0:07:19 remaining)
Nmap scan report for 10.129.136.187
Host is up (0.033s latency).
Not shown: 65534 closed tcp ports (conn-refused)
PORT     STATE SERVICE
6379/tcp open  redis

Nmap done: 1 IP address (1 host up) scanned in 517.67 seconds
```

> 6379

#### 2. Which service is running on the port that is open on the machine?

> redis

#### 3. What type of database is Redis? Choose from the following options: (i) In-memory Database, (ii) Traditional Database

> In-memory Database

#### 4. Which command-line utility is used to interact with the Redis server? Enter the program name you would enter into the terminal without any arguments.

> redis-cli

#### 5. Which flag is used with the Redis command-line utility to specify the hostname?

> -h

#### 6. Once connected to a Redis server, which command is used to obtain the information and statistics about the Redis server?

> info

#### 7. What is the version of the Redis server being used on the target machine?

```sh
10.129.136.187:6379> info
# Server
redis_version:5.0.7
...
```

> 5.0.7

#### 8. Which command is used to select the desired database in Redis?

> select

#### 9. How many keys are present inside the database with index 0?

```sh
10.129.136.187:6379> keys *
1) "temp"
2) "flag"
3) "numb"
4) "stor"
```

> 4

#### 10. Which command is used to obtain all the keys in a database?

> keys *

#### Submit root flag

```sh
10.129.136.187:6379> get flag
"03e1d2b376c37ab3f5319922053953eb"
```

## Final Flag

> 03e1d2b376c37ab3f5319922053953eb

*Created by [bu19akov](https://github.com/bu19akov)*