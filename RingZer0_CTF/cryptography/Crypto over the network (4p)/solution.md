# Crypto over the network

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Cryptography
- **Points:** 4

## Provided Materials

- Netcat credentials

## Solution

As we connect with Netcat, we can enter passwords. With a bit of playing we can notice, that passwords with 8 characters in length have higher process time:

```sh
$ nc challenges.ringzer0team.com 10066
Password: 1234567
Wrong password. Server take 0.000013 seconds
Password: 12345678
Wrong password. Server take 0.008519 seconds
```

That's called [Timing Attack](https://ropesec.com/articles/timing-attacks/#). We can assume, that the password will consist of 8 characters. Also, we can notice, that when we send some characters, the response time is lower than `0.008` seconds:

```sh
Password: aaaaaaaa
Wrong password. Server take 0.008512 seconds
Password: GGGGGGGG
Wrong password. Server take 0.007448 seconds
```

We can assume, that if some character is correctly placed on its position, the response time will be lower than `0.008` seconds, so we can write a script, that will iterate all `ASCII` characters, and if the response time will be lower than `0.008` seconds, we will add this character to our password string:

```python
import re
from pwn import remote

def get_server_time(response):
    match = re.search(r'Server take ([0-9.]+) seconds', response)
    if match:
        return float(match.group(1))
    return None

def receive_until_colon(nc):
    prompt = b''
    while b':' not in prompt:
        prompt += nc.recv(1)
    return prompt

def find_password(nc):
    # ASCII range for testing: from space (32) to tilde (126)
    ascii_range = range(32, 127)
    password = ''

    # Iterate through each character position in the password
    for i in range(8):
        for ascii_code in ascii_range:
            # Construct the test password
            test_char = chr(ascii_code)
            test_password = 'a' * len(password) + test_char + 'a' * (7 - len(password))
            nc.sendline(test_password.encode())

            # Receive the response and extract server time
            response = receive_until_colon(nc).decode()
            server_time = get_server_time(response)

            # Check the server response time
            if server_time is not None and server_time < 0.008:
                password += test_char
                print(f"Found character: {test_char}")
                break

        if len(password) == 8:
            break

    return password

def main():
    # Connect to the remote server
    nc = remote('challenges.ringzer0team.com', 10066)

    # Receive initial prompt
    print(receive_until_colon(nc).decode())

    # Find the password
    password = find_password(nc)
    print(f"Password: {password}")

    # Close the connection
    nc.close()

if __name__ == "__main__":
    main()
```

And indeed here is the output:

```sh
[+] Opening connection to challenges.ringzer0team.com on port 10066: Done
Password:
Found character: G
Found character: 0
Found character: O
Found character: d
Found character: P
Found character: w
Found character: d
Found character: !
Password: G0OdPwd!
[*] Closed connection to challenges.ringzer0team.com port 10066
```

So we send found password and get our flag:

```sh
Password: G0OdPwd!
Nice job you got the right timing FLAG-qkboj26ynulhnzkdltdqsohesl
```

## Final Flag

`FLAG-qkboj26ynulhnzkdltdqsohesl`

*Created by [bu19akov](https://github.com/bu19akov)*