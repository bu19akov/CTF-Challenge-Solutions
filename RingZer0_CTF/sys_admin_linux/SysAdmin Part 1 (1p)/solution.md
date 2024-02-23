# Name

## Challenge Details 

- **CTF:** RingZer0
- **Category:** SysAdmin Linux
- **Points:** 1

## Provided Materials

- SSH credentials

## Solution

We can execute [ps aux](https://unix.stackexchange.com/questions/106847/what-does-aux-mean-in-ps-aux) to show processes for all users:

```sh
morpheus@sysadmin-track:/home$ ps -aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
...
root         401  0.0  0.0   2608   340 ?        S     2023   2:47 /bin/sh /root/backup.sh -u trinity -p Flag-7e0cfcf090a2fe53c97ea3edd3883d0d
```

## Final Flag

`Flag-7e0cfcf090a2fe53c97ea3edd3883d0d`

*Created by [bu19akov](https://github.com/bu19akov)*