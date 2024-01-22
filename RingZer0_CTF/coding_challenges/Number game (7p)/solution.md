# Number game

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Coding Challenges
- **Points:** 7

## Provided Materials

- SSH credentials

## Solution

We have to guess 10 numbers between `0` and `10000` in less than 30 seconds. It will take too much time, if we just iterate all numbers from `0` to `10000`, so we will use [Binary Search Algorithm](https://www.geeksforgeeks.org/number-guessing-game-in-python-using-binary-search/). The main idea is, that we will take middle number every time and based on the response we will reduce the search area twice. For example if the guessed number is 7500:

- Without `Binary Search` we will need to send each number from `0` to `7500` to the server.
- With `Binary Search` we will need to send 2 numbers:
	1. Firstly, we send `((0 + 10000) // 2) = 5000` and get the response `Your number is too small`
	2. In the second guess we send `((5001 + 10000) // 2) = 7500`, that is our guessed number!

Here is the code:

```python
import paramiko
import time

# Game configuration
username = 'number'
password = 'Z7IwIMRC2dc764L'
hostname = 'challenges.ringzer0team.com'
port = 10130
total_rounds = 10
guess_range = 10000

def play_round(channel, round_number):
    """Play a single round of the guessing game."""
    print(f"Initiating round {round_number}...")
    upper_bound = guess_range
    lower_bound = 0
    guess_found = False

    while not guess_found:
        guess = (upper_bound + lower_bound) // 2
        channel.send(f"{guess}\n")
        time.sleep(0.22)
        response = channel.recv(1024)

        if b"too big" in response:
            upper_bound = guess
        elif b"too small" in response:
            lower_bound = guess
        elif b"Game that you win" in response:
            guess_found = True
            print(f"Round {round_number} completed. Correct guess: {guess}")
            if round_number == total_rounds:
                print("Congratulations! Final message: " + response.decode("utf-8"))

def setup_ssh_connection():
    """Establishes an SSH connection and returns the channel."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password, port=port)

    channel = ssh.invoke_shell()
    time.sleep(1)
    if channel.recv_ready():
        print(channel.recv(9999).decode('utf-8'))
    return channel

# Main game execution
try:
    channel = setup_ssh_connection()
    start_time = time.time()

    for round_number in range(1, total_rounds + 1):
        play_round(channel, round_number)

    print("Game completed.")
    if channel.recv_ready():
        print(channel.recv(1024).decode('utf-8'))

    end_time = time.time()
    print(f"Total time elapsed: {end_time - start_time:.2f} seconds")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'channel' in locals() and channel:
        channel.close()
```

## Final Flag

`FLAG-M8Vr5z6O0323y719c4p3NIrP9l`

*Created by [bu19akov](https://github.com/bu19akov)*